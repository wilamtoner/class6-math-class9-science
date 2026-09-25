const { spawn } = require('child_process');
const fs = require('fs');

async function shot() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,960',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_shot_k_' + Date.now(),
    'file://' + process.cwd() + '/index.html'
  ]);
  function cleanup() { try { chrome.kill(); } catch(e) {} }
  process.on('exit', cleanup);

  await new Promise(r => setTimeout(r, 2000));
  const listRes = await fetch('http://127.0.0.1:9222/json');
  const tabs = await listRes.json();
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  const ws = new WebSocket(pageTab.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);

  let msgId = 1;
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

  // Open modal and switch to keys tab
  await send('Runtime.evaluate', {
    expression: `(function() {
      togglePreetiModal(true);
      setPreetiTab('keys');
    })()`
  });

  await new Promise(r => setTimeout(r, 800));

  const shotRes = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('/tmp/preeti_keys.png', Buffer.from(shotRes.data, 'base64'));
  console.log('Screenshot saved to /tmp/preeti_keys.png');

  cleanup();
  process.exit(0);
}
shot().catch(e => { console.error(e); process.exit(1); });
