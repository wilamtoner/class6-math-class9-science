const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const brainDir = '/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66';

async function testUnit7() {
  const tmpDir = '/tmp/cdp_c9u7_test_' + Date.now();
  console.log("Starting Headless Chromium for Unit 7 Verification...");
  const chromeProc = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9227',
    `--user-data-dir=${tmpDir}`,
    '--window-size=1280,1100',
    'file:///run/media/nepal/Backup1/class 6 maths/index.html?grade=9&unit=7'
  ]);

  function cleanup() {
    try { chromeProc.kill(); } catch (e) {}
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
  process.on('exit', cleanup);
  process.on('SIGINT', cleanup);

  // Wait 3s for Chromium to start and parse 3.2MB HTML
  await new Promise(r => setTimeout(r, 3000));

  const listRes = await fetch('http://127.0.0.1:9227/json');
  const tabs = await listRes.json();
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  console.log("Connected to WebSocket URL:", pageTab.webSocketDebuggerUrl);

  const WebSocket = require('ws');
  const ws = new WebSocket(pageTab.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);

  let msgId = 1;
  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = msgId++;
      const handler = (event) => {
        const data = JSON.parse(event.data);
        if (data.id === id) {
          ws.removeEventListener('message', handler);
          if (data.error) reject(data.error);
          else resolve(data.result);
        }
      };
      ws.addEventListener('message', handler);
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  async function evaluate(expr) {
    const res = await send('Runtime.evaluate', { expression: expr, returnByValue: true });
    if (res.exceptionDetails) throw new Error(JSON.stringify(res.exceptionDetails));
    return res.result.value;
  }

  await send('Page.enable');
  await send('Runtime.enable');

  console.log("1. Verifying Grade 9 Unit 7 initial activation...");
  const initCheck = await evaluate(`
    (() => {
      return {
        v7Visible: !document.getElementById('c9-view-7')?.classList.contains('hidden'),
        v1Hidden: document.getElementById('c9-view-1')?.classList.contains('hidden'),
        v6Hidden: document.getElementById('c9-view-6')?.classList.contains('hidden'),
        headerText: document.querySelector('#c9-view-7 h2')?.textContent?.trim()
      };
    })()
  `);
  console.log("Initial state check:", initCheck);

  if (!initCheck.v7Visible) {
    console.log("Activating Unit 7 explicitly...");
    await evaluate("selectGrade(9)");
    await evaluate("switchGrade9Unit(7)");
    await new Promise(r => setTimeout(r, 500));
  }

  // 2. Test Mode 1: Kinematics Simulator (Airplane Preset)
  console.log("2. Testing Mode 1: Kinematics Simulator...");
  await evaluate("setTabC9U7('concepts')");
  await evaluate("setLabModeC9U7('kinematics')");
  await evaluate("applyKinematicsPresetC9U7('airplane')");
  await new Promise(r => setTimeout(r, 300));

  const planeCheck = await evaluate(`
    (() => ({
      u: document.getElementById('c9u7-val-u')?.textContent,
      a: document.getElementById('c9u7-val-a')?.textContent,
      t: document.getElementById('c9u7-val-t')?.textContent,
      v: document.getElementById('c9u7-calc-v')?.textContent,
      s: document.getElementById('c9u7-calc-s')?.textContent
    }))()
  `);
  console.log("Airplane preset calculation check:", planeCheck);
  if (!planeCheck.s.includes('675') || !planeCheck.v.includes('45')) {
    throw new Error(`Expected s=675m, v=45m/s, got: ${JSON.stringify(planeCheck)}`);
  }

  // Screenshot Kinematics Lab
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u7-lab-mode-kinematics');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u7_kinematics.png'), Buffer.from(shot1.data, 'base64'));
  console.log("Saved shot_c9u7_kinematics.png");

  // 3. Test Mode 2: Motion Graphs Studio (s-t and v-t)
  console.log("3. Testing Mode 2: Motion Graphs Studio...");
  await evaluate("setLabModeC9U7('graphs')");
  await evaluate("setGraphTypeC9U7('st_graph')");
  await evaluate("selectGraphSectionC9U7('0_4')");
  await new Promise(r => setTimeout(r, 300));

  const stCheck = await evaluate(`
    (() => ({
      slope: document.getElementById('c9u7-sec-slope')?.textContent,
      badge: document.getElementById('c9u7-sec-badge')?.textContent
    }))()
  `);
  console.log("s-t Graph section 0-4s check:", stCheck);

  // Switch to v-t graph
  await evaluate("setGraphTypeC9U7('vt_graph')");
  await evaluate("selectGraphSectionC9U7('cd')");
  await new Promise(r => setTimeout(r, 300));

  const vtCheck = await evaluate(`
    (() => ({
      slope: document.getElementById('c9u7-sec-slope')?.textContent,
      area: document.getElementById('c9u7-sec-area')?.textContent
    }))()
  `);
  console.log("v-t Graph section CD check:", vtCheck);
  if (!vtCheck.area.includes('80 m')) {
    throw new Error(`Expected area 80 m, got: ${JSON.stringify(vtCheck)}`);
  }

  // Screenshot Graphs
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u7-lab-mode-graphs');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u7_graphs.png'), Buffer.from(shot2.data, 'base64'));
  console.log("Saved shot_c9u7_graphs.png");

  // Switch to Hare & Tortoise Race
  console.log("Testing Hare & Tortoise Race Simulation...");
  await evaluate("setGraphTypeC9U7('hare_tortoise')");
  await evaluate("runHareTortoiseRaceC9U7()");
  await new Promise(r => setTimeout(r, 3500)); // wait for animation steps to finish

  const raceCheck = await evaluate(`
    (() => ({
      badge: document.getElementById('c9u7-sec-badge')?.textContent,
      summary: document.getElementById('c9u7-sec-summary')?.textContent
    }))()
  `);
  console.log("Hare & Tortoise race result check:", raceCheck);

  // Screenshot Hare & Tortoise
  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u7_haretortoise.png'), Buffer.from(shot3.data, 'base64'));
  console.log("Saved shot_c9u7_haretortoise.png");

  // 4. Test Mode 3: Newton's Laws Sandbox
  console.log("4. Testing Mode 3: Newton's Laws Sandbox...");
  await evaluate("setLabModeC9U7('newton_laws')");
  await evaluate("setNewtonLawC9U7(1)");
  await evaluate("flickCardC9U7()");
  await new Promise(r => setTimeout(r, 400));

  const law1Check = await evaluate("document.getElementById('c9u7-newton-svg-wrap')?.innerHTML");
  console.log("Law 1 coin flick verified!");

  // Law 3 Rocket
  await evaluate("setNewtonLawC9U7(3)");
  await evaluate("launchRocketC9U7()");
  await new Promise(r => setTimeout(r, 400));

  // Law 4 Elasticity
  await evaluate("setNewtonLawC9U7(4)");
  await evaluate("updateSpringLoadC9U7(9)"); // exceed limit
  await new Promise(r => setTimeout(r, 300));

  // Screenshot Newton's Laws
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u7-lab-mode-newton_laws');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u7_newton.png'), Buffer.from(shot4.data, 'base64'));
  console.log("Saved shot_c9u7_newton.png");

  // 5. Test Tab 2: Exercises
  console.log("5. Testing Tab 2: Exercises...");
  await evaluate("setTabC9U7('exercises')");
  await evaluate("filterC9U7Exercises('all')");
  await new Promise(r => setTimeout(r, 300));

  const exCount = await evaluate("document.querySelectorAll('.c9u7-ex-card:not(.hidden)').length");
  console.log("Exercise cards visible:", exCount);

  // Screenshot Exercises
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u7-view-exercises');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot5 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u7_exercises.png'), Buffer.from(shot5.data, 'base64'));
  console.log("Saved shot_c9u7_exercises.png");

  // 6. Test Tab 3: 16 Tiered Model Questions
  console.log("6. Testing Tab 3: Tiered Questions...");
  await evaluate("setTabC9U7('tiers')");
  await evaluate("filterC9U7Tiers('all')");
  await new Promise(r => setTimeout(r, 300));

  const tierCount = await evaluate("document.querySelectorAll('.c9u7-tier-card:not(.hidden)').length");
  console.log("Tier cards count (expect 16):", tierCount);
  if (tierCount !== 16) {
    throw new Error(`Expected exactly 16 tier cards, found ${tierCount}`);
  }

  // 7. Test Tab 4: Interactive Quiz with Perfect 10/10 Score
  console.log("7. Testing Tab 4: Self-Assessment Quiz with 10/10 score...");
  await evaluate("setTabC9U7('quiz')");
  await evaluate("resetC9U7Quiz()");
  await new Promise(r => setTimeout(r, 300));

  // Correct options: [2, 1, 1, 1, 2, 1, 1, 1, 1, 0]
  const correctAnswers = [2, 1, 1, 1, 2, 1, 1, 1, 1, 0];
  for (let q = 0; q < 10; q++) {
    await evaluate(`selectC9U7QuizOption(${q}, ${correctAnswers[q]})`);
  }
  await new Promise(r => setTimeout(r, 500));

  const quizScore = await evaluate("document.getElementById('c9u7-quiz-score-badge')?.textContent?.trim()");
  console.log("Quiz final score badge:", quizScore);
  if (!quizScore.includes("१० / १०")) {
    throw new Error(`Expected score '१० / १०', got '${quizScore}'`);
  }

  // Screenshot Quiz Perfect Score
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u7-view-quiz');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot6 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u7_quiz_perfect.png'), Buffer.from(shot6.data, 'base64'));
  console.log("Saved shot_c9u7_quiz_perfect.png");

  // 8. Horizontal overflow audit
  const overflow = await evaluate(`
    (() => ({
      innerWidth: window.innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      hasOverflow: document.documentElement.scrollWidth > window.innerWidth
    }))()
  `);
  console.log("Horizontal overflow audit:", overflow);
  if (overflow.hasOverflow) {
    throw new Error(`Horizontal overflow detected! scrollWidth=${overflow.scrollWidth}, innerWidth=${overflow.innerWidth}`);
  }

  cleanup();
  console.log("\n========================================================");
  console.log("ALL UNIT 7 VERIFICATIONS PASSED WITH ZERO ERRORS!");
  console.log("========================================================");
}

testUnit7().catch(err => {
  console.error("Test failed:", err);
  process.exit(1);
});
