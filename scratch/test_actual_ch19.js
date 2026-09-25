const { spawn } = require('child_process');
const fs = require('fs');

async function testActualCh19() {
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,1050',
    '--remote-debugging-port=9224',
    '--user-data-dir=/tmp/cdp_actual_ch19_' + Date.now(),
    'file://' + process.cwd() + '/index.html?ch=19'
  ]);
  function cleanup() { try { chrome.kill(); } catch(e) {} }
  process.on('exit', cleanup);

  await new Promise(r => setTimeout(r, 2500));
  const listRes = await fetch('http://127.0.0.1:9224/json');
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

  console.log('Testing Mode 1 (Symmetry Explorer)...');
  await send('Runtime.evaluate', {
    expression: `(function() {
      window.selectSymmetryShape('square');
      document.getElementById('ch19-lab-mode-symmetry').scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  let shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_symmetry_lab.png', Buffer.from(shot1.data, 'base64'));
  console.log('Screenshot 1 saved: scratch/shot_ch19_symmetry_lab.png');

  console.log('Testing Mode 2 (Tessellation Studio)...');
  await send('Runtime.evaluate', {
    expression: `(function() {
      window.switchCh19Lab('tessellation');
      window.selectTessShape('hexagon');
      document.getElementById('ch19-lab-mode-tessellation').scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  let shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_tess_lab.png', Buffer.from(shot2.data, 'base64'));
  console.log('Screenshot 2 saved: scratch/shot_ch19_tess_lab.png');

  console.log('Testing Mode 3 (Mirror Grid Challenge)...');
  await send('Runtime.evaluate', {
    expression: `(function() {
      window.switchCh19Lab('mirror');
      window.loadMirrorPreset('rocket');
      window.autoCompleteMirror();
      window.checkMirrorSymmetry();
      document.getElementById('ch19-lab-mode-mirror').scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  let shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_mirror_lab.png', Buffer.from(shot3.data, 'base64'));
  console.log('Screenshot 3 saved: scratch/shot_ch19_mirror_lab.png');

  console.log('Testing Tab 2 (Exercises & Mixed Review)...');
  await send('Runtime.evaluate', {
    expression: `(function() {
      window.setTabCh19('exercises');
      window.filterCh19Exercises('all');
      document.getElementById('sec-ch19-ex19_1').scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  let shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_exercises.png', Buffer.from(shot4.data, 'base64'));
  console.log('Screenshot 4 saved: scratch/shot_ch19_exercises.png');

  console.log('Testing Tab 3 (Tiered Questions)...');
  await send('Runtime.evaluate', {
    expression: `(function() {
      window.setTabCh19('tiers');
      window.scrollTo(0, 0);
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  let shot5 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_tiers.png', Buffer.from(shot5.data, 'base64'));
  console.log('Screenshot 5 saved: scratch/shot_ch19_tiers.png');

  console.log('Testing Tab 4 (Quiz with Answers)...');
  await send('Runtime.evaluate', {
    expression: `(function() {
      window.setTabCh19('quiz');
      window.handleCh19QuizAnswer('q1', 2);
      window.handleCh19QuizAnswer('q2', 2);
      window.handleCh19QuizAnswer('q3', 1);
      window.handleCh19QuizAnswer('q4', 2);
      window.handleCh19QuizAnswer('q5', 2);
      document.getElementById('ch19-quiz-container').scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await new Promise(r => setTimeout(r, 400));
  let shot6 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_ch19_quiz.png', Buffer.from(shot6.data, 'base64'));
  console.log('Screenshot 6 saved: scratch/shot_ch19_quiz.png');

  console.log('Exceptions thrown:', errors.length);
  cleanup();
  console.log('ALL SCREENSHOTS CAPTURED PERFECTLY!');
}

testActualCh19().catch(err => {
  console.error('Test failed:', err);
  process.exit(1);
});
