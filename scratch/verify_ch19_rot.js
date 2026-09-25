const { spawn } = require('child_process');
const fs = require('fs');

async function testCh19Rot() {
  const chrome = spawn('chromium', [
    '--headless', '--no-sandbox', '--disable-gpu',
    '--window-size=1280,850',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_ch19_rot_' + Date.now(),
    'file://' + process.cwd() + '/कक्षा_६_गणित_डिजिटल_साथी.html'
  ]);
  function cleanup() { try { chrome.kill(); } catch(e) {} }
  process.on('exit', cleanup);

  await new Promise(r => setTimeout(r, 2000));
  const listRes = await fetch('http://127.0.0.1:9222/json');
  const tabs = await listRes.json();
  const ws = new WebSocket(tabs[0].webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);

  let id = 1;
  function send(method, params = {}) {
    return new Promise(resolve => {
      const msgId = id++;
      const handler = evt => {
        const d = JSON.parse(evt.data);
        if (d.id === msgId) {
          ws.removeEventListener('message', handler);
          resolve(d.result);
        }
      };
      ws.addEventListener('message', handler);
      ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  await send('Page.enable');
  await send('Runtime.enable');

  // Switch to chapter 19
  await send('Runtime.evaluate', {
    expression: `(function() {
      switchChapter(19);
      if (typeof setSymShape === 'function') {
        setSymShape('equilateral');
      }
    })()`
  });

  await new Promise(r => setTimeout(r, 600));

  // Check each shape's displayed values
  const shapeTests = await send('Runtime.evaluate', {
    expression: `(function() {
      const shapes = ['equilateral', 'isosceles', 'scalene', 'square', 'rectangle', 'rhombus', 'hexagon', 'circle'];
      const results = {};
      shapes.forEach(s => {
        setSymShape(s);
        const rEl = document.getElementById('sym-val-rot');
        results[s] = rEl ? rEl.textContent : 'NOT_FOUND';
      });
      // reset back to equilateral
      setSymShape('equilateral');
      return results;
    })()`,
    returnByValue: true
  });

  console.log('Rotational symmetry readings for all shapes:');
  console.log(shapeTests.result.value);

  // Capture screenshot of the exact card
  const shotRes = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_fixed_card.png', Buffer.from(shotRes.data, 'base64'));
  console.log('Screenshot captured to scratch/shot_ch19_fixed_card.png');

  cleanup();
  process.exit(0);
}
testCh19Rot().catch(e => { console.error(e); process.exit(1); });
