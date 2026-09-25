const { spawn } = require('child_process');
const fs = require('fs');

async function shot() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,1050',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_shot_th_' + Date.now(),
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

  // Switch to Chapter 14 concepts tab and scroll to angle slider
  await send('Runtime.evaluate', {
    expression: `(function() {
      switchChapter(14);
      setTabCh14('concepts');
      const el = document.getElementById('ch14-angle-type-badge');
      if (el) {
        el.scrollIntoView({ behavior: 'instant', block: 'center' });
      }
    })()`
  });

  await new Promise(r => setTimeout(r, 1200));

  const shotRes = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('/tmp/ch14_theta_view.png', Buffer.from(shotRes.data, 'base64'));
  console.log('Screenshot saved to /tmp/ch14_theta_view.png');

  cleanup();
  process.exit(0);
}
shot().catch(e => { console.error(e); process.exit(1); });
