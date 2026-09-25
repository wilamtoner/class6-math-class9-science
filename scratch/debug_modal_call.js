const { spawn } = require('child_process');

async function debugModal() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,960',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_debug_' + Date.now(),
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
      if (!modal) return { err: 'No modal found' };
      const res = {};
      res.beforeClasses = modal.className;
      res.beforeStyle = modal.getAttribute('style');
      
      togglePreetiModal(true);
      res.afterClasses = modal.className;
      res.afterStyle = modal.getAttribute('style');
      res.computed = {
        display: window.getComputedStyle(modal).display,
        position: window.getComputedStyle(modal).position,
        top: window.getComputedStyle(modal).top,
        left: window.getComputedStyle(modal).left,
        width: window.getComputedStyle(modal).width,
        height: window.getComputedStyle(modal).height,
        opacity: window.getComputedStyle(modal).opacity,
        visibility: window.getComputedStyle(modal).visibility,
        zIndex: window.getComputedStyle(modal).zIndex
      };
      return res;
    })()`,
    returnByValue: true
  });
  console.log('Modal debug:', res.result.value);
  cleanup();
  process.exit(0);
}
debugModal().catch(e => { console.error(e); process.exit(1); });
