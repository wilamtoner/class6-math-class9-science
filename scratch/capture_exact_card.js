const { spawn } = require('child_process');
const fs = require('fs');

async function shot() {
  const chrome = spawn('chromium', [
    '--headless', '--no-sandbox', '--disable-gpu',
    '--window-size=1280,800',
    '--remote-debugging-port=9222',
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

  await send('Runtime.evaluate', {
    expression: `(function() {
      switchChapter(19);
      selectSymmetryShape('equilateral');
      const el = document.getElementById('ch19-lab-mode-symmetry');
      if (el) el.scrollIntoView();
    })()`
  });

  await new Promise(r => setTimeout(r, 800));

  const shotRes = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_fixed_card.png', Buffer.from(shotRes.data, 'base64'));
  console.log('Saved screenshot to scratch/shot_ch19_fixed_card.png');

  cleanup();
  process.exit(0);
}
shot().catch(e => { console.error(e); process.exit(1); });
