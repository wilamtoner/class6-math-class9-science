const { spawn } = require('child_process');

async function testTabs() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_tab_test_' + Date.now(),
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
  const errors = [];

  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    } else if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
      errors.push({ type: 'console.error', args: data.params.args });
    } else if (data.method === 'Runtime.exceptionThrown') {
      errors.push({ type: 'exception', details: data.params.exceptionDetails });
    }
  };

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = msgId++;
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  await send('Console.enable');
  await send('Runtime.enable');

  const report = [];

  for (let ch = 1; ch <= 14; ch++) {
    // switch to chapter
    await send('Runtime.evaluate', { expression: `switchChapter(${ch})` });
    
    // find all tab buttons in this chapter view
    const tabRes = await send('Runtime.evaluate', {
      expression: `(function() {
        const view = document.getElementById('chapter-view-${ch}');
        if (!view) return { error: 'View not found' };
        
        // Find buttons that look like tab buttons
        const buttons = Array.from(view.querySelectorAll('button')).filter(b => {
          const oc = b.getAttribute('onclick') || '';
          return oc.includes('setTab') || oc.includes('switchTab');
        });
        
        const results = [];
        for (const b of buttons) {
          const text = b.innerText.trim();
          const onclick = b.getAttribute('onclick');
          try {
            b.click();
            results.push({ text, onclick, ok: true });
          } catch(e) {
            results.push({ text, onclick, ok: false, error: e.message });
          }
        }
        return { tabCount: buttons.length, results };
      })()`,
      returnByValue: true
    });
    
    report.push({ ch, result: tabRes.result.value });
  }

  console.log('Tab click testing completed:');
  for (const r of report) {
    console.log(`Chapter ${r.ch}: ${r.result.tabCount} tab buttons tested.`);
    const failed = (r.result.results || []).filter(x => !x.ok);
    if (failed.length > 0) {
      console.error(`  FAILURES in ch ${r.ch}:`, failed);
    }
  }

  if (errors.length > 0) {
    console.error('JS Errors during tab switching:', errors);
  } else {
    console.log('ZERO JavaScript errors during all tab switches!');
  }

  cleanup();
  process.exit(0);
}

testTabs().catch(err => {
  console.error(err);
  process.exit(1);
});
