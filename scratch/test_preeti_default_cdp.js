const { spawn } = require('child_process');

async function test() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,960',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_test_pdef_' + Date.now(),
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
  const errors = [];
  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    } else if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
      errors.push(data.params.args.map(a => a.value || a.description).join(' '));
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
      const select = document.getElementById('global-font-select');
      const bodyStyle = window.getComputedStyle(document.body);
      return {
        selectedValue: select ? select.value : 'missing',
        bodyFontFamily: bodyStyle.fontFamily,
        bodyClasses: document.body.className,
        preetiLoaded: document.fonts.check('16px Preeti')
      };
    })()`,
    returnByValue: true
  });

  console.log('Result:', res.result.value);
  if (errors.length > 0) {
    console.error('Errors:', errors);
  } else {
    console.log('ZERO console errors!');
  }
  cleanup();
  process.exit(0);
}
test().catch(e => { console.error(e); process.exit(1); });
