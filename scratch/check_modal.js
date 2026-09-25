const { spawn } = require('child_process');

async function checkModal() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_chk_' + Date.now(),
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

  const res = await send('Runtime.evaluate', {
    expression: `(function() {
      const modal = document.getElementById('preeti-modal');
      const before = { display: modal.style.display, classes: modal.className };
      togglePreetiModal(true);
      const after = { 
        display: modal.style.display, 
        classes: modal.className, 
        computedDisplay: window.getComputedStyle(modal).display,
        zIndex: window.getComputedStyle(modal).zIndex,
        rect: modal.getBoundingClientRect()
      };
      return { before, after };
    })()`,
    returnByValue: true
  });
  console.log('Modal status:', res.result.value);
  cleanup();
  process.exit(0);
}
checkModal().catch(e => { console.error(e); process.exit(1); });
