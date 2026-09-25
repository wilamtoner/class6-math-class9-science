const { spawn } = require('child_process');
const fs = require('fs');

async function audit() {
  const content = fs.readFileSync('index.html', 'utf8');
  
  // Extract all handler calls
  const handlerMatches = [...content.matchAll(/on(click|change|input|submit)\s*=\s*["']([^"']+)["']/g)];
  console.log(`Found ${handlerMatches.length} inline event handlers.`);

  const fnNames = new Set();
  for (const m of handlerMatches) {
    const code = m[2];
    // extract leading function calls e.g. foo(bar)
    const callMatch = code.match(/([a-zA-Z0-9_$]+)\s*\(/);
    if (callMatch) {
      fnNames.add(callMatch[1]);
    }
  }
  console.log(`Extracted ${fnNames.size} distinct function names called in HTML attributes.`);

  // Launch Chromium and test each function existence
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_audit_' + Date.now(),
    'file://' + process.cwd() + '/index.html'
  ]);

  function cleanup() {
    try { chrome.kill(); } catch (e) {}
  }
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

  const checkFnList = Array.from(fnNames);
  const evalRes = await send('Runtime.evaluate', {
    expression: `(function() {
      const fns = ${JSON.stringify(checkFnList)};
      const results = {};
      const standardGlobals = new Set(['alert', 'confirm', 'prompt', 'console', 'document', 'window', 'MathJax', 'event', 'setTimeout', 'clearTimeout']);
      for (const fn of fns) {
        if (standardGlobals.has(fn)) continue;
        results[fn] = typeof window[fn];
      }
      return results;
    })()`,
    returnByValue: true
  });

  const statuses = evalRes.result.value;
  const missing = [];
  const existing = [];
  for (const [fn, type] of Object.entries(statuses)) {
    if (type !== 'function') {
      missing.push({ fn, type });
    } else {
      existing.push(fn);
    }
  }

  console.log(`Defined functions: ${existing.length}`);
  console.log(`Missing / undefined functions: ${missing.length}`);
  if (missing.length > 0) {
    console.log('MISSING FUNCTIONS:');
    console.log(missing);
  }

  cleanup();
  process.exit(0);
}

audit().catch(err => {
  console.error(err);
  process.exit(1);
});
