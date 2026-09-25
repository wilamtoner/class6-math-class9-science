const { spawn } = require('child_process');

async function testPreetiLive() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_preeti_test_' + Date.now(),
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

  const testReport = await send('Runtime.evaluate', {
    expression: `(function() {
      const report = {};
      
      // Check globals
      const fns = ['unicodeToPreeti', 'preetiToUnicode', 'togglePreetiModal', 'setPreetiTab', 'changeGlobalFont', 'handleU2PLiveConvert', 'handleP2ULiveConvert', 'loadPreetiSample', 'clearPreetiInputs'];
      for (const fn of fns) {
        report[fn] = typeof window[fn];
      }

      // Test conversion
      report.u2p_test = window.unicodeToPreeti('कक्षा ६ गणित: रेखा र कोणहरू');
      report.p2u_test = window.preetiToUnicode('sIff ^ ul0ft');

      // Test modal toggle
      togglePreetiModal(true);
      const modal = document.getElementById('preeti-modal');
      report.modalOpen = modal && modal.style.display === 'flex';

      // Test loading sample
      loadPreetiSample('math');
      const uInp = document.getElementById('u2p-input');
      const preview = document.getElementById('u2p-preeti-preview');
      const ascii = document.getElementById('u2p-ascii');
      report.sampleLoaded = uInp && uInp.value.includes('रेखा र कोणहरू');
      report.previewConverted = preview && preview.textContent.length > 5;
      report.asciiConverted = ascii && ascii.value.length > 5;

      // Test switching tabs in modal
      setPreetiTab('p2u');
      loadPreetiSample('preeti');
      const pInp = document.getElementById('p2u-input');
      const pOut = document.getElementById('p2u-output');
      report.p2uConverted = pOut && pOut.value.length > 5;

      setPreetiTab('keys');
      const keysPanel = document.getElementById('preeti-panel-keys');
      report.keysVisible = keysPanel && !keysPanel.classList.contains('hidden');

      // Close modal
      togglePreetiModal(false);
      report.modalClosed = modal && modal.style.display === 'none';

      // Test font switcher
      changeGlobalFont('preeti');
      report.bodyHasPreeti = document.body.classList.contains('font-mode-preeti');
      changeGlobalFont('mukta');
      report.bodyHasMukta = document.body.classList.contains('font-mode-mukta');

      // Test font face availability
      report.fontCheck = document.fonts.check('16px Preeti');

      return report;
    })()`,
    returnByValue: true
  });

  console.log('Preeti Live Tests Result:');
  console.log(JSON.stringify(testReport.result.value, null, 2));

  if (consoleErrors.length > 0) {
    console.error('Console Errors encountered:', consoleErrors);
  } else {
    console.log('ZERO console errors encountered during Preeti tests!');
  }

  cleanup();
  process.exit(0);
}

testPreetiLive().catch(e => { console.error(e); process.exit(1); });
