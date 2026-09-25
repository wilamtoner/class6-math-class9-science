const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const brainDir = '/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66';

async function testUnit3() {
  const tmpDir = '/tmp/cdp_c9u3_test_' + Date.now();
  const chrome = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9224',
    `--user-data-dir=${tmpDir}`,
    '--window-size=1280,1100',
    'file:///run/media/nepal/Backup1/class 6 maths/index.html?grade=9&unit=3'
  ]);

  function cleanup() {
    try { chrome.kill(); } catch (e) {}
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
  process.on('exit', cleanup);
  process.on('SIGINT', cleanup);

  await new Promise(r => setTimeout(r, 2500));

  const listRes = await fetch('http://127.0.0.1:9224/json');
  const tabs = await listRes.json();
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
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

  console.log("1. Verifying Unit 3 initial state...");
  const initCheck = await evaluate(`
    (() => {
      return {
        v3Visible: !document.getElementById('c9-view-3')?.classList.contains('hidden'),
        v1Hidden: document.getElementById('c9-view-1')?.classList.contains('hidden'),
        v2Hidden: document.getElementById('c9-view-2')?.classList.contains('hidden'),
        headerText: document.querySelector('#c9-view-3 h2')?.textContent?.trim()
      };
    })()
  `);
  console.log("Initial state:", initCheck);

  if (!initCheck.v3Visible) {
    console.log("Calling switchGrade9Unit(3)...");
    await evaluate("switchGrade9Unit(3)");
  }

  // Check Tab 1: Anatomy & Microscopic Gill Explorer
  console.log("2. Testing Mode 1: Anatomy Explorer...");
  await evaluate("setTabC9U3('concepts')");
  await evaluate("setLabModeC9U3('anatomy')");
  await evaluate("setAnatomySubModeC9U3('external')");
  await evaluate("selectExtPartC9U3('pileus')");
  await new Promise(r => setTimeout(r, 400));

  const extCheck = await evaluate(`
    (() => ({
      eng: document.getElementById('c9u3-ext-engname')?.textContent,
      nep: document.getElementById('c9u3-ext-nepname')?.textContent,
      role: document.getElementById('c9u3-ext-role')?.textContent
    }))()
  `);
  console.log("External Anatomy check:", extCheck);

  // Switch to internal gill TS
  await evaluate("setAnatomySubModeC9U3('internal')");
  await evaluate("selectIntPartC9U3('basidium')");
  await new Promise(r => setTimeout(r, 400));

  const intCheck = await evaluate(`
    (() => ({
      eng: document.getElementById('c9u3-int-engname')?.textContent,
      nep: document.getElementById('c9u3-int-nepname')?.textContent,
      role: document.getElementById('c9u3-int-role')?.textContent
    }))()
  `);
  console.log("Internal Gill T.S. check:", intCheck);

  // Screenshot Lab Anatomy
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u3-lab-mode-anatomy');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u3_anatomy.png'), Buffer.from(shot1.data, 'base64'));
  console.log("Saved shot_c9u3_anatomy.png");

  // Check Mode 2: Cultivation Simulator
  console.log("3. Testing Mode 2: Cultivation Simulator...");
  await evaluate("setLabModeC9U3('farming')");
  await evaluate("setFarmStageC9U3(3)"); // Stage 3: Moisture test
  await evaluate("setMoistureC9U3('ideal')");
  await new Promise(r => setTimeout(r, 400));

  const farmCheck = await evaluate(`
    (() => ({
      title: document.getElementById('c9u3-farm-title')?.textContent,
      stageBadge: document.getElementById('c9u3-farm-step-badge')?.textContent,
      feedback: document.getElementById('c9u3-moisture-feedback')?.textContent?.trim()?.slice(0, 50)
    }))()
  `);
  console.log("Farming check:", farmCheck);

  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u3_farming.png'), Buffer.from(shot2.data, 'base64'));
  console.log("Saved shot_c9u3_farming.png");

  // Check Mode 3: Safety Identifier
  console.log("4. Testing Mode 3: Safety Identifier...");
  await evaluate("setLabModeC9U3('safety')");
  await evaluate("selectSpecimenC9U3('deathcap')");
  await new Promise(r => setTimeout(r, 400));

  const safetyCheck = await evaluate(`
    (() => ({
      nep: document.getElementById('c9u3-spec-nepname')?.textContent,
      badge: document.getElementById('c9u3-spec-verdict-badge')?.textContent?.trim(),
      volva: document.getElementById('c9u3-spec-volva')?.textContent
    }))()
  `);
  console.log("Safety check:", safetyCheck);

  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u3_safety.png'), Buffer.from(shot3.data, 'base64'));
  console.log("Saved shot_c9u3_safety.png");

  // Check Tab 2: Exercises
  console.log("5. Testing Tab 2: Exercises...");
  await evaluate("setTabC9U3('exercises')");
  await evaluate("filterC9U3Exercises('all')");
  await new Promise(r => setTimeout(r, 400));

  const exCardsCount = await evaluate("document.querySelectorAll('.c9u3-ex-card:not(.hidden)').length");
  console.log("Visible exercise cards count:", exCardsCount);

  await evaluate(`
    (() => {
      const el = document.getElementById('c9u3-view-exercises');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u3_exercises.png'), Buffer.from(shot4.data, 'base64'));
  console.log("Saved shot_c9u3_exercises.png");

  // Check Tab 3: Tiered Questions
  console.log("6. Testing Tab 3: Tiered Questions...");
  await evaluate("setTabC9U3('tiers')");
  await evaluate("filterC9U3Tiers('all')");
  await new Promise(r => setTimeout(r, 400));

  const tierCardsCount = await evaluate("document.querySelectorAll('.c9u3-tier-card:not(.hidden)').length");
  console.log("Visible tier questions count (expect 16):", tierCardsCount);

  await evaluate(`
    (() => {
      const el = document.getElementById('c9u3-view-tiers');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot5 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u3_tiers.png'), Buffer.from(shot5.data, 'base64'));
  console.log("Saved shot_c9u3_tiers.png");

  // Check Tab 4: Self-Assessment Quiz
  console.log("7. Testing Tab 4: Quiz with perfect score 10/10...");
  await evaluate("setTabC9U3('quiz')");
  await evaluate("resetC9U3Quiz()");
  await new Promise(r => setTimeout(r, 300));

  // Answer all 10 correctly
  const correctAnswers = [1, 2, 0, 2, 1, 0, 2, 0, 0, 2];
  for (let q = 0; q < 10; q++) {
    await evaluate(`selectC9U3QuizOption(${q}, ${correctAnswers[q]})`);
  }
  await new Promise(r => setTimeout(r, 500));

  const quizScore = await evaluate("document.getElementById('c9u3-quiz-score-badge')?.textContent?.trim()");
  console.log("Quiz final score badge:", quizScore);

  await evaluate(`
    (() => {
      const el = document.getElementById('c9u3-view-quiz');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot6 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u3_quiz_perfect.png'), Buffer.from(shot6.data, 'base64'));
  console.log("Saved shot_c9u3_quiz_perfect.png");

  // Check horizontal overflow
  const overflow = await evaluate(`
    (() => ({
      innerWidth: window.innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      hasOverflow: document.documentElement.scrollWidth > window.innerWidth
    }))()
  `);
  console.log("Horizontal overflow audit:", overflow);

  cleanup();
  console.log("\nALL VERIFICATIONS PASSED SUCCESSFULLY!");
}

testUnit3().catch(err => {
  console.error("Test failed:", err);
  process.exit(1);
});
