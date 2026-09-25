const { spawn } = require('child_process');

async function check() {
  const chrome = spawn('chromium', [
    '--headless', '--no-sandbox', '--disable-gpu',
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
    return new Promise((resolve) => {
      const msgId = id++;
      const handler = (evt) => {
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

  const evalRes = await send('Runtime.evaluate', {
    expression: `(function() {
      // Let's test standard words in Preeti
      // In Preeti:
      // 's' = क
      // 'H' = ?
      // 'h' = ?
      // ';' = ?
      // ':' = ?
      // 'Hofldlt' -> what did user expect for ज्यामिति?
      // In Preeti, how do people type ज्यामिति?
      // Usually: Hofldlt ! Why? Because in Preeti font, 'H' is half ja (ज्) or jha?
      return {
        // Let's check what H is in PREETI_TO_UNICODE_MAP
        H_mapped: PREETI_TO_UNICODE_MAP['H'],
        h_mapped: PREETI_TO_UNICODE_MAP['h'],
        semicolon_mapped: PREETI_TO_UNICODE_MAP[';'],
        colon_mapped: PREETI_TO_UNICODE_MAP[':'],
        Z_mapped: PREETI_TO_UNICODE_MAP['Z'],
        z_mapped: PREETI_TO_UNICODE_MAP['z']
      };
    })()`,
    returnByValue: true
  });

  console.log(evalRes.value);
  cleanup();
  process.exit(0);
}
check();
