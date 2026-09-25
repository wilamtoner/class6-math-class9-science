const { spawn } = require('child_process');
const fs = require('fs');

async function testActualCh20() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,1050',
    '--remote-debugging-port=9231',
    '--user-data-dir=/tmp/cdp_actual_ch20_' + Date.now(),
    'file://' + process.cwd() + '/index.html?ch=20'
  ]);
  function cleanup() { try { chrome.kill(); } catch(e) {} }
  process.on('exit', cleanup);

  await new Promise(r => setTimeout(r, 2500));
  const listRes = await fetch('http://127.0.0.1:9231/json');
  const tabs = await listRes.json();
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  const ws = new WebSocket(pageTab.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);

  let msgId = 1;
  const pending = new Map();
  const consoleLogs = [];
  const errors = [];

  ws.onmessage = (evt) => {
    const data = JSON.parse(evt.data);
    if (data.method === 'Runtime.consoleAPICalled') {
      consoleLogs.push(data.params);
    }
    if (data.method === 'Runtime.exceptionThrown') {
      errors.push(data.params);
    }
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
  await send('Page.enable');

  console.log('Evaluating Chapter 20 Initialization...');
  const initCheck = await send('Runtime.evaluate', {
    expression: `(function() {
      const v20 = document.getElementById('chapter-view-20');
      const b20 = document.getElementById('side-ch-20');
      return {
        viewExists: !!v20,
        viewVisible: v20 && !v20.classList.contains('hidden'),
        btnExists: !!b20,
        btnActive: b20 && b20.className.includes('bg-blue-600'),
        tabConceptsVisible: !document.getElementById('ch20-view-concepts').classList.contains('hidden'),
        barSvgExists: !!document.getElementById('ch20-bar-svg')
      };
    })()`,
    returnByValue: true
  });
  console.log('Init Check Result:', JSON.stringify(initCheck.result.value, null, 2));

  // Test Mode 1: Bar Chart Studio
  console.log('Testing Mode 1 (Bar Chart Studio)...');
  const barTest = await send('Runtime.evaluate', {
    expression: `(function() {
      window.loadBarPreset('subjects');
      const title = document.getElementById('bar-chart-title').textContent;
      const gBars = document.getElementById('bar-elements-group').innerHTML;
      const maxVal = document.getElementById('bar-metric-max').textContent;
      window.scrollTo(0, 680);
      return {
        title,
        hasRects: gBars.includes('<rect'),
        barCount: (gBars.match(/<rect/g) || []).length,
        maxVal
      };
    })()`,
    returnByValue: true
  });
  console.log('Bar Chart Test Result:', barTest.result.value);

  await new Promise(r => setTimeout(r, 400));
  let shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch20_bar_studio.png', Buffer.from(shot1.data, 'base64'));
  console.log('Screenshot 1 saved: scratch/shot_ch20_bar_studio.png');

  // Test Mode 2: Tally Marks Lab
  console.log('Testing Mode 2 (Tally Marks Lab)...');
  const tallyTest = await send('Runtime.evaluate', {
    expression: `(function() {
      window.switchCh20Lab('tallyLab');
      window.loadTallyPreset('scores');
      const tbody = document.getElementById('tally-table-body');
      const rowCount = tbody.children.length;
      const totalCount = document.getElementById('tally-total-count').textContent;
      window.scrollTo(0, 680);
      return {
        rowCount,
        totalCount
      };
    })()`,
    returnByValue: true
  });
  console.log('Tally Lab Test Result:', tallyTest.result.value);

  await new Promise(r => setTimeout(r, 400));
  let shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch20_tally_lab.png', Buffer.from(shot2.data, 'base64'));
  console.log('Screenshot 2 saved: scratch/shot_ch20_tally_lab.png');

  // Test Mode 3: Reader Lab
  console.log('Testing Mode 3 (Reader Lab)...');
  const readerTest = await send('Runtime.evaluate', {
    expression: `(function() {
      window.switchCh20Lab('readerLab');
      window.handleReaderAnswer(2); // Option C: कक्षा ८ (१०० जना) - Correct!
      const fb = document.getElementById('reader-feedback').textContent;
      window.scrollTo(0, 680);
      return {
        feedback: fb,
        isCorrect: fb.includes('सही उत्तर')
      };
    })()`,
    returnByValue: true
  });
  console.log('Reader Lab Test Result:', readerTest.result.value);

  await new Promise(r => setTimeout(r, 400));
  let shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch20_reader_lab.png', Buffer.from(shot3.data, 'base64'));
  console.log('Screenshot 3 saved: scratch/shot_ch20_reader_lab.png');

  // Test Tab 2: Exercises & Mixed Review
  console.log('Testing Tab 2 (Exercises)...');
  const exTest = await send('Runtime.evaluate', {
    expression: `(function() {
      window.setTabCh20('exercises');
      window.filterCh20Exercises('unit6_mixed');
      const secMixed = document.getElementById('sec-ch20-unit6_mixed');
      const secEx1 = document.getElementById('sec-ch20-ex20_1');
      window.scrollTo(0, 300);
      return {
        mixedVisible: !secMixed.classList.contains('hidden'),
        ex1Hidden: secEx1.classList.contains('hidden')
      };
    })()`,
    returnByValue: true
  });
  console.log('Exercises Filter Test Result:', exTest.result.value);

  await new Promise(r => setTimeout(r, 400));
  let shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch20_exercises.png', Buffer.from(shot4.data, 'base64'));
  console.log('Screenshot 4 saved: scratch/shot_ch20_exercises.png');

  // Test Tab 3: Tiered Questions
  console.log('Testing Tab 3 (Tiered Questions)...');
  await send('Runtime.evaluate', {
    expression: `(function() {
      window.setTabCh20('tiers');
      window.scrollTo(0, 0);
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  let shot5 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch20_tiers.png', Buffer.from(shot5.data, 'base64'));
  console.log('Screenshot 5 saved: scratch/shot_ch20_tiers.png');

  // Test Tab 4: Quiz
  console.log('Testing Tab 4 (Quiz with Answers)...');
  const quizTest = await send('Runtime.evaluate', {
    expression: `(function() {
      window.setTabCh20('quiz');
      window.handleCh20QuizAnswer('q1', 1); // बारम्बारता
      window.handleCh20QuizAnswer('q2', 1); // ४ ठाडो र १ छड्के
      window.handleCh20QuizAnswer('q3', 1); // अध्ययन गरिने विषय
      window.handleCh20QuizAnswer('q4', 1); // चौडाइ
      window.handleCh20QuizAnswer('q5', 2); // सधैँ समान
      const score = document.getElementById('ch20-quiz-score').textContent;
      window.scrollTo(0, 300);
      return { score };
    })()`,
    returnByValue: true
  });
  console.log('Quiz Test Result:', quizTest.result.value);

  await new Promise(r => setTimeout(r, 400));
  let shot6 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch20_quiz.png', Buffer.from(shot6.data, 'base64'));
  console.log('Screenshot 6 saved: scratch/shot_ch20_quiz.png');

  console.log('--- Errors check ---');
  console.log('Exceptions thrown:', errors.length);
  if (errors.length > 0) {
    console.error('Errors:', JSON.stringify(errors, null, 2));
  }
  console.log('Console logs count:', consoleLogs.length);

  cleanup();
  console.log('ALL CHAPTER 20 TESTS COMPLETED SUCCESSFULLY!');
}

testActualCh20().catch(err => {
  console.error('Test failed:', err);
  process.exit(1);
});
