const { spawn } = require('child_process');

async function runFullAudit() {
  console.log('====================================================');
  console.log('🚀 STARTING COMPREHENSIVE FULL-SYSTEM AUDIT (1 TO 20)');
  console.log('====================================================');

  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_full_audit_' + Date.now(),
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
  const consoleWarns = [];
  const runtimeExceptions = [];

  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.id && pending.has(data.id)) {
      const { resolve, reject } = pending.get(data.id);
      pending.delete(data.id);
      if (data.error) reject(data.error);
      else resolve(data.result);
    } else if (data.method === 'Runtime.consoleAPICalled') {
      const msg = data.params.args.map(a => a.value || a.description || JSON.stringify(a)).join(' ');
      if (data.params.type === 'error') {
        consoleErrors.push(msg);
      } else if (data.params.type === 'warning') {
        consoleWarns.push(msg);
      }
    } else if (data.method === 'Runtime.exceptionThrown') {
      const details = data.params.exceptionDetails;
      const text = details.text + ' ' + (details.exception?.description || '') + ' at line ' + details.lineNumber;
      runtimeExceptions.push(text);
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

  // Step 1: Preeti Font check
  console.log('\n[1/5] Checking Preeti Font and Typography...');
  const fontRes = await send('Runtime.evaluate', {
    expression: `(async function() {
      const loaded = await document.fonts.load('16px Preeti');
      return {
        check: document.fonts.check('16px Preeti'),
        fontFaces: Array.from(document.fonts).map(f => f.family)
      };
    })()`,
    awaitPromise: true,
    returnByValue: true
  });
  console.log('Font loaded:', fontRes.result.value);

  // Step 2: Test Preeti Converter
  console.log('\n[2/5] Testing Preeti Converter Utility...');
  const preetiRes = await send('Runtime.evaluate', {
    expression: `(function() {
      if (typeof unicodeToPreeti !== 'function' || typeof preetiToUnicode !== 'function') {
        return { error: 'Converter functions not found' };
      }
      const testWords = ['कक्षा ६ गणित', 'तथ्याङ्कशास्त्र', 'निर्देशाङ्क ज्यामिति', 'क्षेत्रमिति'];
      const results = testWords.map(w => {
        const p = unicodeToPreeti(w);
        const u = preetiToUnicode(p);
        return { word: w, preeti: p, back: u, match: w === u };
      });
      return { ok: true, results };
    })()`,
    returnByValue: true
  });
  console.log('Preeti conversion results:', JSON.stringify(preetiRes.result.value, null, 2));

  // Step 3: Iterate through Chapters 1 to 20
  console.log('\n[3/5] Testing Chapter Switching, Tabs, and Interactive Controls (Chapters 1 to 20)...');
  const chAudit = [];
  for (let ch = 1; ch <= 20; ch++) {
    const res = await send('Runtime.evaluate', {
      expression: `(function() {
        const sideBtn = document.getElementById('side-ch-' + ${ch});
        if (!sideBtn) return { ch: ${ch}, error: 'Missing sidebar button side-ch-' + ${ch} };
        
        switchChapter(${ch});
        
        const view = document.getElementById('chapter-view-' + ${ch});
        if (!view) return { ch: ${ch}, error: 'Missing chapter-view-' + ${ch} };
        
        const isVisible = !view.classList.contains('hidden') && view.style.display !== 'none';
        
        // Check other views are hidden
        let othersHidden = true;
        for (let j = 1; j <= 20; j++) {
          if (j !== ${ch}) {
            const ov = document.getElementById('chapter-view-' + j);
            if (ov && !ov.classList.contains('hidden') && ov.style.display !== 'none') {
              othersHidden = false;
            }
          }
        }
        
        // Find tabs and click them
        const tabButtons = Array.from(view.querySelectorAll('button')).filter(b => {
          const onclick = b.getAttribute('onclick') || '';
          return onclick.includes('setTab') || onclick.includes('Tab');
        });
        
        const tabClicks = [];
        tabButtons.forEach(b => {
          try {
            b.click();
            tabClicks.push(b.innerText.trim().slice(0, 15));
          } catch(e) {
            tabClicks.push('Error: ' + e.message);
          }
        });
        
        // Trigger all inputs in this chapter
        const inputs = Array.from(view.querySelectorAll('input, select'));
        inputs.forEach(inp => {
          try {
            inp.dispatchEvent(new Event('input', { bubbles: true }));
            inp.dispatchEvent(new Event('change', { bubbles: true }));
          } catch(e) {}
        });
        
        // Check images in view
        const imgs = Array.from(view.querySelectorAll('img'));
        const brokenImgs = imgs.filter(img => !img.complete || img.naturalWidth === 0).map(img => img.src);

        return {
          ch: ${ch},
          sidebarFound: !!sideBtn,
          viewVisible: isVisible,
          othersHidden: othersHidden,
          tabsCount: tabButtons.length,
          inputsCount: inputs.length,
          brokenImagesCount: brokenImgs.length,
          brokenImages: brokenImgs
        };
      })()`,
      returnByValue: true
    });
    chAudit.push(res.result.value);
  }

  console.table(chAudit.map(c => ({
    Ch: c.ch,
    Sidebar: c.sidebarFound,
    Visible: c.viewVisible,
    OthersHidden: c.othersHidden,
    Tabs: c.tabsCount,
    Inputs: c.inputsCount,
    BrokenImgs: c.brokenImagesCount
  })));

  // Step 4: Check Broken images in entire document
  console.log('\n[4/5] Checking Document Images and Links...');
  const imgAudit = await send('Runtime.evaluate', {
    expression: `(function() {
      const allImgs = Array.from(document.querySelectorAll('img'));
      const broken = allImgs.filter(i => {
        // if completed but naturalWidth === 0 and src is not empty
        return i.src && i.complete && i.naturalWidth === 0;
      }).map(i => ({ src: i.src, alt: i.alt }));
      return { totalImgs: allImgs.length, broken };
    })()`,
    returnByValue: true
  });
  console.log('Image audit result:', imgAudit.result.value);

  // Step 5: Report Console Errors and Exceptions
  console.log('\n[5/5] Console Errors & Exceptions Audit...');
  console.log('Console Errors count:', consoleErrors.length);
  if (consoleErrors.length > 0) {
    console.error('Console errors:', consoleErrors);
  }
  console.log('Runtime Exceptions count:', runtimeExceptions.length);
  if (runtimeExceptions.length > 0) {
    console.error('Runtime exceptions:', runtimeExceptions);
  }

  cleanup();
  process.exit(0);
}

runFullAudit().catch(e => {
  console.error('Audit fatal error:', e);
  process.exit(1);
});
