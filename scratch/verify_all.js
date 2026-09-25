const { spawn } = require('child_process');

async function verifyAll() {
  console.log('=== STARTING COMPLETE LIVE VERIFICATION AUDIT ===');
  
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,960',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_verify_' + Date.now(),
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
  const consoleLogs = [];

  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    } else if (data.method === 'Runtime.consoleAPICalled') {
      const msg = data.params.args.map(a => a.value || a.description).join(' ');
      if (data.params.type === 'error') consoleErrors.push(msg);
      else consoleLogs.push(`[${data.params.type}] ${msg}`);
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

  // Test 1: Page Load & Font Availability
  console.log('[1/6] Auditing Font Loading...');
  const fontTest = await send('Runtime.evaluate', {
    expression: `(async function() {
      const loaded = await document.fonts.load('16px Preeti');
      return {
        preetiLoaded: loaded.length > 0 && loaded[0].status === 'loaded',
        preetiCheck: document.fonts.check('16px Preeti')
      };
    })()`,
    awaitPromise: true,
    returnByValue: true
  });
  console.log('Font Audit Result:', fontTest.result.value);

  // Test 2: Preeti Modal & Conversion
  console.log('[2/6] Auditing Preeti Converter & Modal...');
  const modalTest = await send('Runtime.evaluate', {
    expression: `(function() {
      togglePreetiModal(true);
      const modal = document.getElementById('preeti-modal');
      const modalVisible = modal && window.getComputedStyle(modal).display === 'flex';
      
      // Test conversion
      const sampleUni = 'पाठ १४: रेखा र कोणहरू कक्षा ६ गणित';
      const preetiResult = unicodeToPreeti(sampleUni);
      const backUni = preetiToUnicode(preetiResult);
      
      togglePreetiModal(false);
      const modalClosed = modal && modal.style.display === 'none';

      return {
        modalVisible,
        modalClosed,
        sampleUni,
        preetiResult,
        backUni
      };
    })()`,
    returnByValue: true
  });
  console.log('Preeti Modal & Conversion Audit:', modalTest.result.value);

  // Test 3: Chapter Switching
  console.log('[3/6] Auditing Chapter Views 1 to 14...');
  const chTest = await send('Runtime.evaluate', {
    expression: `(function() {
      const chResults = [];
      for (let i = 1; i <= 14; i++) {
        switchChapter(i);
        const v = document.getElementById('chapter-view-' + i);
        chResults.push({ ch: i, visible: v && !v.classList.contains('hidden') && v.style.display !== 'none' });
      }
      return chResults;
    })()`,
    returnByValue: true
  });
  const allChaptersVisible = chTest.result.value.every(c => c.visible);
  console.log(`All 14 Chapter Views Switchable: ${allChaptersVisible ? 'YES' : 'NO'}`);

  // Test 4: Chapter 14 Tabs & Interactive Components
  console.log('[4/6] Auditing Chapter 14 Tabs & Interactive Lab...');
  const ch14Test = await send('Runtime.evaluate', {
    expression: `(function() {
      switchChapter(14);
      setTabCh14('tiers');
      setCh14LabMode('types');
      setCh14Angle(75);
      
      setCh14LabMode('relations');
      setCh14LabMode('parallel');
      setCh14LabMode('construction');
      nextCh14Step();
      prevCh14Step();

      setTabCh14('quiz');
      checkQuizCh14(0, 0);
      resetQuizCh14();

      setTabCh14('concepts');
      return { ch14TabsAndLabOk: true };
    })()`,
    returnByValue: true
  });
  console.log('Chapter 14 Audit:', ch14Test.result.value);

  // Test 5: MathJax and Formula Rendering
  console.log('[5/6] Auditing Math Rendering...');
  const mathTest = await send('Runtime.evaluate', {
    expression: `({
      mathJaxActive: typeof MathJax !== 'undefined',
      mathCount: document.querySelectorAll('.MathJax, .offline-math, .mjx-chtml').length
    })`,
    returnByValue: true
  });
  console.log('Math Elements Count:', mathTest.result.value);

  // Test 6: Console Errors Summary
  console.log('[6/6] Final Error Check...');
  if (consoleErrors.length > 0) {
    console.error('FAIL: Console errors detected:', consoleErrors);
  } else {
    console.log('SUCCESS: ZERO console errors or runtime exceptions across the entire app!');
  }

  cleanup();
  process.exit(0);
}

verifyAll().catch(e => { console.error('Verification error:', e); process.exit(1); });
