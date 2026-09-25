const { spawn } = require('child_process');
const fs = require('fs');

async function shot() {
  const chrome = spawn('chromium', [
    '--headless', '--no-sandbox', '--disable-gpu',
    '--window-size=1280,950',
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

  await send('Runtime.evaluate', {
    expression: `(function() {
      selectGrade(9);
      switchGrade9Unit(1);
      setTabC9U1('quiz');
      c9u1QuizData.forEach((item, idx) => {
        checkC9U1Quiz(idx, item.ans);
      });
      document.getElementById('c9u1-quiz-container').scrollIntoView({ behavior: 'instant', block: 'start' });
    })()`
  });
  await new Promise(r => setTimeout(r, 600));

  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('scratch/shot_c9u1_quiz_questions.png', Buffer.from(shot.data, 'base64'));

  cleanup();
  process.exit(0);
}
shot().catch(e => { console.error(e); process.exit(1); });
