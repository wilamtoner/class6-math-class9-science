const { spawn } = require('child_process');

async function runTest() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_test_' + Date.now(),
    'file://' + process.cwd() + '/index.html'
  ]);

  let closed = false;
  function cleanup() {
    if (!closed) {
      closed = true;
      try { chrome.kill(); } catch (e) {}
    }
  }

  process.on('exit', cleanup);
  process.on('SIGINT', cleanup);
  process.on('SIGTERM', cleanup);

  // Wait for CDP to be ready
  await new Promise(r => setTimeout(r, 2000));

  const listRes = await fetch('http://127.0.0.1:9222/json');
  const tabs = await listRes.json();
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  
  if (!pageTab || !pageTab.webSocketDebuggerUrl) {
    console.error('No page tab found or webSocketDebuggerUrl missing');
    cleanup();
    process.exit(1);
  }

  const ws = new WebSocket(pageTab.webSocketDebuggerUrl);

  await new Promise((resolve, reject) => {
    ws.onopen = resolve;
    ws.onerror = reject;
  });

  let msgId = 1;
  const pending = new Map();

  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    } else if (data.method === 'Runtime.consoleAPICalled') {
      console.log(`[Browser Console ${data.params.type}]:`, ...data.params.args.map(a => a.value || a.description));
    } else if (data.method === 'Runtime.exceptionThrown') {
      console.error(`[Browser Exception]:`, data.params.exceptionDetails);
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
  await send('Page.enable');

  console.log('--- Checking initial page state ---');
  let evalRes = await send('Runtime.evaluate', {
    expression: `({
      title: document.title,
      activeChapter: typeof currentChapter !== 'undefined' ? currentChapter : null,
      buttonsCount: document.querySelectorAll('button').length,
      chaptersCount: 14
    })`,
    returnByValue: true
  });
  console.log('Initial page stats:', evalRes.result.value);

  // Test switching through each chapter from 1 to 14
  console.log('--- Testing switchChapter(1..14) ---');
  for (let ch = 1; ch <= 14; ch++) {
    const res = await send('Runtime.evaluate', {
      expression: `(function() {
        try {
          if (typeof switchChapter === 'function') {
            switchChapter(${ch});
            const view = document.getElementById('chapter-view-${ch}');
            const isVisible = view && !view.classList.contains('hidden') && view.style.display !== 'none';
            return { success: true, ch: ${ch}, exists: !!view, isVisible: isVisible };
          } else {
            return { success: false, error: 'switchChapter is not a function' };
          }
        } catch(e) {
          return { success: false, error: e.message, stack: e.stack };
        }
      })()`,
      returnByValue: true
    });
    console.log(`Chapter ${ch}:`, res.result.value);
  }

  // Test tabs in Chapter 14
  console.log('--- Testing tabs in Chapter 14 ---');
  for (let tab = 1; tab <= 5; tab++) {
    const res = await send('Runtime.evaluate', {
      expression: `(function() {
        try {
          if (typeof switchCh14Tab === 'function') {
            switchCh14Tab(${tab});
            const content = document.getElementById('ch14-tab-content-' + ${tab});
            return { success: true, tab: ${tab}, exists: !!content };
          } else {
            return { success: false, error: 'switchCh14Tab is not a function' };
          }
        } catch(e) {
          return { success: false, error: e.message };
        }
      })()`,
      returnByValue: true
    });
    console.log(`Ch14 Tab ${tab}:`, res.result.value);
  }

  // Check if any offline math elements are broken
  const mathCheck = await send('Runtime.evaluate', {
    expression: `({
      mathJaxDefined: typeof MathJax !== 'undefined',
      latexElements: document.querySelectorAll('.math-tex, .offline-math, .mjx-chtml').length
    })`,
    returnByValue: true
  });
  console.log('Math stats:', mathCheck.result.value);

  cleanup();
  process.exit(0);
}

runTest().catch(err => {
  console.error('Test error:', err);
  process.exit(1);
});
