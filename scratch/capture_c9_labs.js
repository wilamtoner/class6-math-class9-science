const { spawn } = require('child_process');
const fs = require('fs');

async function capture() {
  const chrome = spawn('chromium', [
    '--headless', '--no-sandbox', '--disable-gpu',
    '--window-size=1280,850',
    '--remote-debugging-port=9222',
    'file://' + process.cwd() + '/index.html'
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

  // Shot 1: Scientific Notation Studio centered
  await send('Runtime.evaluate', {
    expression: `(function() {
      selectGrade(9);
      switchGrade9Unit(1);
      setTabC9U1('concepts');
      switchC9U1Lab('notation');
      setC9U1Preset('0.00042');
      document.getElementById('c9u1-lab-mode-notation').scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await new Promise(r => setTimeout(r, 500));
  const s1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_notation_focus.png', Buffer.from(s1.data, 'base64'));

  // Shot 2: Least Count Lab centered
  await send('Runtime.evaluate', {
    expression: `(function() {
      switchC9U1Lab('leastcount');
      selectC9U1Instrument('ruler');
      document.getElementById('c9u1-lab-mode-leastcount').scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await new Promise(r => setTimeout(r, 500));
  const s2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_leastcount_focus.png', Buffer.from(s2.data, 'base64'));

  // Shot 3: Exercises Tab centered
  await send('Runtime.evaluate', {
    expression: `(function() {
      setTabC9U1('exercises');
      document.getElementById('c9u1-view-exercises').scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await new Promise(r => setTimeout(r, 500));
  const s3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_exercises_focus.png', Buffer.from(s3.data, 'base64'));

  cleanup();
  process.exit(0);
}
capture().catch(e => { console.error(e); process.exit(1); });
