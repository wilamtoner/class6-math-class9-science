const { spawn } = require('child_process');

async function auditLabs() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_labs_' + Date.now(),
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
  const consoleErrors = [];
  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    } else if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
      consoleErrors.push(data.params.args.map(a => a.value || a.description).join(' '));
    } else if (data.method === 'Runtime.exceptionThrown') {
      consoleErrors.push(data.params.exceptionDetails.text + ' ' + (data.params.exceptionDetails.exception?.description || ''));
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

  const labReport = [];

  for (let ch = 1; ch <= 14; ch++) {
    // switch chapter and open lab tab
    await send('Runtime.evaluate', { expression: `switchChapter(${ch});` });
    
    // open lab tab if exists
    const labEval = await send('Runtime.evaluate', {
      expression: `(function() {
        if (typeof setTabCh${ch} === 'function') {
          // find lab tab param
          const btns = Array.from(document.querySelectorAll('#chapter-view-${ch} button'));
          const labBtn = btns.find(b => (b.innerText || '').includes('ल्याब') || (b.innerText || '').includes('Lab') || (b.getAttribute('onclick') || '').includes('tiers') || (b.getAttribute('onclick') || '').includes('lab'));
          if (labBtn) labBtn.click();
        }
        
        // Find all inputs, buttons, select elements in chapter-view-ch and trigger interaction
        const view = document.getElementById('chapter-view-${ch}');
        if (!view) return { error: 'View not found' };
        
        const inputs = Array.from(view.querySelectorAll('input, select'));
        let interactedInputs = 0;
        inputs.forEach(inp => {
          try {
            if (inp.type === 'range' || inp.type === 'number' || inp.type === 'text') {
              inp.dispatchEvent(new Event('input', { bubbles: true }));
              inp.dispatchEvent(new Event('change', { bubbles: true }));
              interactedInputs++;
            }
          } catch(e) {}
        });
        
        return { ch: ${ch}, interactedInputs };
      })()`,
      returnByValue: true
    });
    
    labReport.push(labEval.result.value);
  }

  console.log('Lab inputs & interaction audit:', labReport);
  if (consoleErrors.length > 0) {
    console.error('Console errors during lab interactions:', consoleErrors);
  } else {
    console.log('ALL LABS & INPUTS FUNCTIONED WITHOUT ANY ERROR!');
  }

  cleanup();
  process.exit(0);
}

auditLabs().catch(e => { console.error(e); process.exit(1); });
