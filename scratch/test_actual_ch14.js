const { spawn } = require('child_process');

async function testActualCh14() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_actual_ch14_' + Date.now(),
    'file://' + process.cwd() + '/index.html?ch=14'
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

  const res = await send('Runtime.evaluate', {
    expression: `(function() {
      const results = {};
      const fns = [
        'setTabCh14', 'setExerciseCh14', 'setCh14LabMode',
        'setCh14Angle', 'prevCh14Step', 'nextCh14Step',
        'resetCh14Construct', 'runCh14Lab', 'checkQuizCh14', 'resetQuizCh14'
      ];
      for (const fn of fns) {
        results[fn] = typeof window[fn];
      }

      // Test calling lab
      try {
        setCh14LabMode('types');
        setCh14Angle(60);
        results.setCh14Angle_60 = 'OK';
      } catch(e) {
        results.setCh14Angle_60 = 'ERROR: ' + e.message;
      }

      // Test calling relations
      try {
        setCh14LabMode('relations');
        results.setCh14LabMode_relations = 'OK';
      } catch(e) {
        results.setCh14LabMode_relations = 'ERROR: ' + e.message;
      }

      // Test calling parallel
      try {
        setCh14LabMode('parallel');
        results.setCh14LabMode_parallel = 'OK';
      } catch(e) {
        results.setCh14LabMode_parallel = 'ERROR: ' + e.message;
      }

      // Test calling construction
      try {
        setCh14LabMode('construction');
        nextCh14Step();
        prevCh14Step();
        resetCh14Construct();
        results.construction_steps = 'OK';
      } catch(e) {
        results.construction_steps = 'ERROR: ' + e.message;
      }

      // Test quiz
      try {
        checkQuizCh14(0, 0);
        resetQuizCh14();
        results.quiz = 'OK';
      } catch(e) {
        results.quiz = 'ERROR: ' + e.message;
      }

      // Test exercise tabs
      try {
        ['all', '14.1', '14.2', '14.3', '14.4', '14.5', 'project'].forEach(sec => setExerciseCh14(sec));
        results.exercises = 'OK';
      } catch(e) {
        results.exercises = 'ERROR: ' + e.message;
      }

      return results;
    })()`,
    returnByValue: true
  });

  console.log('Chapter 14 tests:', res.result.value);
  cleanup();
  process.exit(0);
}

testActualCh14().catch(e => { console.error(e); process.exit(1); });
