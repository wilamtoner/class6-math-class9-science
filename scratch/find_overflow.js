const { spawn } = require('child_process');

async function findOverflow() {
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

  const res = await send('Runtime.evaluate', {
    expression: `(function() {
      switchChapter(19);
      const docW = document.documentElement.clientWidth;
      const all = Array.from(document.querySelectorAll('*'));
      const overflowing = [];
      all.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.right > docW + 5) {
          overflowing.push({
            tag: el.tagName,
            id: el.id,
            className: (el.className || '').toString().slice(0, 50),
            right: Math.round(rect.right),
            width: Math.round(rect.width),
            docW: docW
          });
        }
      });
      return {
        bodyScrollWidth: document.body.scrollWidth,
        docClientWidth: docW,
        overflowCount: overflowing.length,
        topOverflowing: overflowing.slice(0, 10)
      };
    })()`,
    returnByValue: true
  });

  console.log(JSON.stringify(res.result.value, null, 2));
  cleanup();
  process.exit(0);
}
findOverflow().catch(e => { console.error(e); process.exit(1); });
