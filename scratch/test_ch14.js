const { spawn } = require('child_process');

async function testCh14() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_ch14_' + Date.now(),
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

  // Switch to Chapter 14
  await send('Runtime.evaluate', { expression: 'switchChapter(14); setTabCh14("tiers");' });

  // Test Ch14 functions
  const res = await send('Runtime.evaluate', {
    expression: `(function() {
      const results = {};
      const fns = ['drawCh14Angle', 'calcCh14Complement', 'calcCh14Supplement', 'drawCh14Vert', 'drawCh14Transversal', 'submitCh14Quiz', 'resetCh14Quiz'];
      for (const fn of fns) {
        results[fn] = typeof window[fn];
        if (typeof window[fn] === 'function') {
          try {
            window[fn]();
            results[fn + '_call'] = 'OK';
          } catch(e) {
            results[fn + '_call'] = 'ERROR: ' + e.message;
          }
        }
      }
      return results;
    })()`,
    returnByValue: true
  });
  console.log('Ch14 Interactive functions test:', res.result.value);

  cleanup();
  process.exit(0);
}
testCh14().catch(e => { console.error(e); process.exit(1); });
