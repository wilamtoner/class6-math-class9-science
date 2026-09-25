const { spawn } = require('child_process');
const fs = require('fs');

async function retake() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,1050',
    '--remote-debugging-port=9230',
    '--user-data-dir=/tmp/cdp_mirror_' + Date.now(),
    'file://' + process.cwd() + '/index.html?ch=19'
  ]);
  function cleanup() { try { chrome.kill(); } catch(e) {} }
  process.on('exit', cleanup);

  await new Promise(r => setTimeout(r, 2500));
  const listRes = await fetch('http://127.0.0.1:9230/json');
  const tabs = await listRes.json();
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  const ws = new WebSocket(pageTab.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);

  let id = 1;
  const pending = new Map();
  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    }
  };

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = msgId++;
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  await send('Runtime.enable');
  await send('Page.enable');

  await send('Runtime.evaluate', {
    expression: `(function() {
      window.switchCh19Lab('mirror');
      window.loadMirrorPreset('rocket');
      window.autoCompleteMirror();
      window.checkMirrorSymmetry();
      window.scrollTo(0, 1900);
    })()`
  });
  await new Promise(r => setTimeout(r, 500));
  let shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_mirror_lab.png', Buffer.from(shot.data, 'base64'));
  console.log('Mirror screenshot retaken successfully at 1900px!');

  cleanup();
}

retake().catch(console.error);
