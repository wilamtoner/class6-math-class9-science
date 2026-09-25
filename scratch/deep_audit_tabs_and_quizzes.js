const { spawn } = require('child_process');

async function testAllTabsAndQuizzes() {
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
  const consoleErrors = [];
  const exceptions = [];

  ws.onmessage = (evt) => {
    const d = JSON.parse(evt.data);
    if (d.method === 'Runtime.consoleAPICalled' && d.params.type === 'error') {
      consoleErrors.push(d.params.args.map(a => a.value || a.description).join(' '));
    } else if (d.method === 'Runtime.exceptionThrown') {
      exceptions.push(d.params.exceptionDetails.text + ' ' + (d.params.exceptionDetails.exception?.description || ''));
    }
  };

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

  await send('Console.enable');
  await send('Runtime.enable');

  const report = [];

  for (let ch = 1; ch <= 20; ch++) {
    const res = await send('Runtime.evaluate', {
      expression: `(function() {
        switchChapter(${ch});
        const view = document.getElementById('chapter-view-' + ${ch});
        if (!view) return { ch: ${ch}, error: 'No chapter view' };

        // 1. Test Tab Switching
        const tabFunc = (ch === 1) ? window.setTab : window['setTabCh' + ${ch}];
        const tabResults = {};
        if (typeof tabFunc === 'function') {
          ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
            try {
              tabFunc(t);
              // find if any subcontainer with t is displayed
              tabResults[t] = 'OK';
            } catch(e) {
              tabResults[t] = 'ERR: ' + e.message;
            }
          });
          // return to concepts
          tabFunc('concepts');
        } else {
          tabResults['custom'] = 'No standard setTabCh' + ${ch};
        }

        // 2. Test exercise filter buttons if any
        const filterBtns = Array.from(view.querySelectorAll('button')).filter(b => {
          const oc = b.getAttribute('onclick') || '';
          return oc.includes('filter') || oc.includes('Filter');
        });
        const filterResults = [];
        filterBtns.forEach(fb => {
          try {
            fb.click();
            filterResults.push(fb.innerText.trim().slice(0, 10));
          } catch(e) {
            filterResults.push('ERR: ' + e.message);
          }
        });

        // 3. Test Quiz options if any
        const quizOptions = Array.from(view.querySelectorAll('button')).filter(b => {
          const oc = b.getAttribute('onclick') || '';
          return oc.includes('Quiz') || oc.includes('quiz') || oc.includes('check');
        });
        let quizTested = 0;
        quizOptions.slice(0, 3).forEach(qb => {
          try {
            qb.click();
            quizTested++;
          } catch(e) {}
        });

        return {
          ch: ${ch},
          hasTabFunc: typeof tabFunc === 'function',
          tabResults,
          filterBtnsCount: filterBtns.length,
          quizTested
        };
      })()`,
      returnByValue: true
    });
    report.push(res.result.value);
  }

  console.table(report.map(r => ({
    Ch: r.ch,
    TabFunc: r.hasTabFunc,
    Concepts: r.tabResults.concepts || '-',
    Exercises: r.tabResults.exercises || '-',
    Tiers: r.tabResults.tiers || '-',
    Quiz: r.tabResults.quiz || '-',
    Filters: r.filterBtnsCount
  })));

  console.log('\nTotal Console Errors during deep interactive test:', consoleErrors.length);
  if (consoleErrors.length > 0) console.error(consoleErrors);
  console.log('Total Runtime Exceptions during deep interactive test:', exceptions.length);
  if (exceptions.length > 0) console.error(exceptions);

  cleanup();
  process.exit(0);
}
testAllTabsAndQuizzes().catch(e => { console.error(e); process.exit(1); });
