const { spawn } = require('child_process');
const fs = require('fs');

async function testPortal() {
  const chrome = spawn('chromium', [
    '--headless', '--no-sandbox', '--disable-gpu',
    '--window-size=1280,850',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/cdp_portal_test_' + Date.now(),
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

  await send('Page.enable');
  await send('Runtime.enable');

  const testResults = await send('Runtime.evaluate', {
    expression: `(function() {
      const log = [];
      const docW = document.documentElement.clientWidth;

      // 1. Initial State (Grade 6)
      log.push({
        step: 'Init Grade 6',
        grade: currentGrade,
        title: document.getElementById('portal-title').textContent,
        bsw: document.body.scrollWidth,
        overflow: document.body.scrollWidth > docW
      });

      // 2. Switch to Grade 9
      selectGrade(9);
      log.push({
        step: 'Switched to Grade 9',
        grade: currentGrade,
        badge: document.getElementById('portal-grade-badge').textContent,
        title: document.getElementById('portal-title').textContent,
        sideHeading: document.getElementById('sidebar-list-heading').textContent,
        sideCount: document.getElementById('sidebar-count-badge').textContent,
        unit1Visible: !document.getElementById('c9-view-1').classList.contains('hidden'),
        bsw: document.body.scrollWidth,
        overflow: document.body.scrollWidth > docW
      });

      // 3. Test Mode 1 (Scientific Notation)
      setC9U1Preset('0.00042');
      const notation1 = document.getElementById('c9u1-res-notation').textContent.trim();
      const n1 = document.getElementById('c9u1-res-n').textContent.trim();

      setC9U1Preset('300000000');
      const notation2 = document.getElementById('c9u1-res-notation').textContent.trim();
      log.push({
        step: 'Scientific Notation Test',
        preset1: { notation: notation1, n: n1 },
        preset2: { notation: notation2 }
      });

      // 4. Test Mode 2 (Least Count Lab)
      switchC9U1Lab('leastcount');
      selectC9U1Instrument('stopwatch');
      const stopReading = document.getElementById('c9u1-inst-reading').textContent;
      selectC9U1Instrument('ammeter');
      const ammeterReading = document.getElementById('c9u1-inst-reading').textContent;
      log.push({
        step: 'Least Count Test',
        stopReading,
        ammeterReading
      });

      // 5. Test Mode 3 (Inquiry Simulator)
      switchC9U1Lab('inquiry');
      runC9U1InquiryTrial();
      const trial1 = document.getElementById('c9u1-trial-1').textContent;
      log.push({
        step: 'Inquiry Simulator Test',
        trial1
      });

      // 6. Test Tab 2 (Exercises)
      setTabC9U1('exercises');
      filterC9U1Ex('mcq');
      const mcqGroupDisplay = document.querySelector('.c9u1-ex-group[data-group="mcq"]').style.display;
      log.push({
        step: 'Exercises Tab Test',
        mcqGroupDisplay
      });

      // 7. Test Tab 3 (Tiered Questions)
      setTabC9U1('tiers');
      filterC9U1Tiers('k');
      const kTierDisplay = document.querySelector('.c9u1-tier-section[data-tier="k"]').style.display;
      log.push({
        step: 'Tiers Tab Test',
        kTierDisplay
      });

      // 8. Test Tab 4 (Quiz)
      setTabC9U1('quiz');
      // answer all 10 questions correctly
      c9u1QuizData.forEach((item, idx) => {
        checkC9U1Quiz(idx, item.ans);
      });
      const quizScore = document.getElementById('c9u1-quiz-score-badge').textContent;
      log.push({
        step: 'Quiz Test',
        quizScore
      });

      // 9. Test Unit 2 Placeholder & Back to Unit 1
      switchGrade9Unit(2);
      const isPlaceholderVisible = !document.getElementById('c9-placeholder-view').classList.contains('hidden');
      switchGrade9Unit(1);
      const isU1Back = !document.getElementById('c9-view-1').classList.contains('hidden');
      log.push({
        step: 'Unit Navigation Test',
        isPlaceholderVisible,
        isU1Back
      });

      // 10. Switch back to Grade 6
      selectGrade(6);
      log.push({
        step: 'Back to Grade 6',
        grade: currentGrade,
        title: document.getElementById('portal-title').textContent,
        ch1Visible: !document.getElementById('chapter-view-1').classList.contains('hidden'),
        bsw: document.body.scrollWidth,
        overflow: document.body.scrollWidth > docW
      });

      return log;
    })()`,
    returnByValue: true
  });

  console.log('Automated Test Report:');
  console.log(JSON.stringify(testResults.result.value, null, 2));

  // Capture screenshot of Grade 9 Unit 1
  await send('Runtime.evaluate', {
    expression: `(function() {
      selectGrade(9);
      switchGrade9Unit(1);
      setTabC9U1('concepts');
      switchC9U1Lab('notation');
    })()`
  });
  await new Promise(r => setTimeout(r, 600));

  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_notation_lab.png', Buffer.from(shot1.data, 'base64'));
  console.log('Captured scratch/shot_c9u1_notation_lab.png');

  // Capture screenshot of Least count lab
  await send('Runtime.evaluate', {
    expression: `(function() {
      switchC9U1Lab('leastcount');
      selectC9U1Instrument('ruler');
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_leastcount_lab.png', Buffer.from(shot2.data, 'base64'));
  console.log('Captured scratch/shot_c9u1_leastcount_lab.png');

  // Capture screenshot of Tab 2 Exercises
  await send('Runtime.evaluate', {
    expression: `(function() {
      setTabC9U1('exercises');
      filterC9U1Ex('all');
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_exercises.png', Buffer.from(shot3.data, 'base64'));
  console.log('Captured scratch/shot_c9u1_exercises.png');

  // Capture screenshot of Tab 4 Quiz
  await send('Runtime.evaluate', {
    expression: `(function() {
      setTabC9U1('quiz');
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  const shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_quiz.png', Buffer.from(shot4.data, 'base64'));
  console.log('Captured scratch/shot_c9u1_quiz.png');

  cleanup();
  process.exit(0);
}
testPortal().catch(e => { console.error(e); process.exit(1); });
