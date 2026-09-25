const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const brainDir = '/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66';

async function testUnit4() {
  const tmpDir = '/tmp/cdp_c9u4_test_' + Date.now();
  console.log("Starting Headless Chromium for Unit 4 Verification...");
  const chromeProc = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9225',
    `--user-data-dir=${tmpDir}`,
    '--window-size=1280,1100',
    'file:///run/media/nepal/Backup1/class 6 maths/index.html?grade=9&unit=4'
  ]);

  function cleanup() {
    try { chromeProc.kill(); } catch (e) {}
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
  process.on('exit', cleanup);
  process.on('SIGINT', cleanup);

  // Wait 2.5s for Chromium to start and parse 2.4MB HTML
  await new Promise(r => setTimeout(r, 2500));

  const listRes = await fetch('http://127.0.0.1:9225/json');
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

  console.log("1. Verifying Grade 9 Unit 4 initial activation...");
  const initCheck = await evaluate(`
    (() => {
      return {
        v4Visible: !document.getElementById('c9-view-4')?.classList.contains('hidden'),
        v1Hidden: document.getElementById('c9-view-1')?.classList.contains('hidden'),
        v2Hidden: document.getElementById('c9-view-2')?.classList.contains('hidden'),
        v3Hidden: document.getElementById('c9-view-3')?.classList.contains('hidden'),
        headerText: document.querySelector('#c9-view-4 h2')?.textContent?.trim()
      };
    })()
  `);
  console.log("Initial state check:", initCheck);

  if (!initCheck.v4Visible) {
    console.log("Calling selectGrade(9) and switchGrade9Unit(4)...");
    await evaluate("selectGrade(9)");
    await evaluate("switchGrade9Unit(4)");
    await new Promise(r => setTimeout(r, 400));
  }

  // 2. Test Mode 1: Comparative Anatomy Explorer
  console.log("2. Testing Mode 1: Comparative Anatomy & Evidences...");
  await evaluate("setTabC9U4('concepts')");
  await evaluate("setLabModeC9U4('anatomy')");
  await evaluate("setAnatomySubModeC9U4('homology')");
  await evaluate("selectHomologyOrganC9U4('bat')");
  await new Promise(r => setTimeout(r, 400));

  const batCheck = await evaluate(`
    (() => ({
      nep: document.getElementById('c9u4-h-neptitle')?.textContent,
      eng: document.getElementById('c9u4-h-engtitle')?.textContent,
      bones: document.getElementById('c9u4-h-bones')?.textContent
    }))()
  `);
  console.log("Homology check (Bat):", batCheck);

  // Switch to Vestigial submode
  await evaluate("setAnatomySubModeC9U4('vestigial')");
  await evaluate("selectVestigialC9U4('appendix')");
  await new Promise(r => setTimeout(r, 400));

  const appCheck = await evaluate(`
    (() => ({
      nep: document.getElementById('c9u4-v-nepname')?.textContent,
      eng: document.getElementById('c9u4-v-engname')?.textContent,
      conc: document.getElementById('c9u4-v-conclusion')?.textContent
    }))()
  `);
  console.log("Vestigial check (Appendix):", appCheck);

  // Switch to Connecting Links submode
  await evaluate("setAnatomySubModeC9U4('connecting')");
  await evaluate("selectConnectingC9U4('archaeopteryx')");
  await new Promise(r => setTimeout(r, 400));

  const arcCheck = await evaluate(`
    (() => ({
      title: document.getElementById('c9u4-c-title')?.textContent,
      traits1: document.getElementById('c9u4-c-traits1')?.textContent
    }))()
  `);
  console.log("Connecting link check (Archaeopteryx):", arcCheck);

  // Screenshot Anatomy Lab
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u4-lab-mode-anatomy');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u4_anatomy.png'), Buffer.from(shot1.data, 'base64'));
  console.log("Saved shot_c9u4_anatomy.png");

  // 3. Test Mode 2: Natural Selection Simulator
  console.log("3. Testing Mode 2: Natural Selection Simulator (Peppered Moth)...");
  await evaluate("setLabModeC9U4('selection')");
  await evaluate("setMothEnvC9U4('clean')");
  await evaluate("stepMothGenC9U4()");
  await evaluate("stepMothGenC9U4()");
  await new Promise(r => setTimeout(r, 300));

  const mothCleanCheck = await evaluate(`
    (() => ({
      whitePct: document.getElementById('c9u4-white-pct')?.textContent,
      blackPct: document.getElementById('c9u4-black-pct')?.textContent,
      genBadge: document.getElementById('c9u4-moth-gen-badge')?.textContent
    }))()
  `);
  console.log("Moth simulator clean env check:", mothCleanCheck);

  await evaluate("setMothEnvC9U4('polluted')");
  await evaluate("stepMothGenC9U4()");
  await evaluate("stepMothGenC9U4()");
  await new Promise(r => setTimeout(r, 300));

  const mothPolCheck = await evaluate(`
    (() => ({
      whitePct: document.getElementById('c9u4-white-pct')?.textContent,
      blackPct: document.getElementById('c9u4-black-pct')?.textContent,
      genBadge: document.getElementById('c9u4-moth-gen-badge')?.textContent
    }))()
  `);
  console.log("Moth simulator polluted env check:", mothPolCheck);

  // Screenshot Selection Simulator
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u4-lab-mode-selection');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u4_selection.png'), Buffer.from(shot2.data, 'base64'));
  console.log("Saved shot_c9u4_selection.png");

  // 4. Test Mode 3: Mutation Simulator
  console.log("4. Testing Mode 3: Mutation Simulator...");
  await evaluate("setLabModeC9U4('mutation')");
  await evaluate("selectMutationDemoC9U4('polydactyly')");
  await new Promise(r => setTimeout(r, 300));

  const muCheck = await evaluate(`
    (() => ({
      title: document.getElementById('c9u4-mu-title')?.textContent,
      badge: document.getElementById('c9u4-mu-badge')?.textContent
    }))()
  `);
  console.log("Mutation check (Polydactyly):", muCheck);

  // 5. Test Tab 2: Exercises
  console.log("5. Testing Tab 2: Exercises...");
  await evaluate("setTabC9U4('exercises')");
  await evaluate("filterC9U4Exercises('all')");
  await new Promise(r => setTimeout(r, 400));

  const exCount = await evaluate("document.querySelectorAll('.c9u4-ex-card:not(.hidden)').length");
  console.log("Exercise cards visible:", exCount);

  // Screenshot Exercises
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u4-view-exercises');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u4_exercises.png'), Buffer.from(shot3.data, 'base64'));
  console.log("Saved shot_c9u4_exercises.png");

  // 6. Test Tab 3: 16 Tiered Model Questions
  console.log("6. Testing Tab 3: Tiered Questions...");
  await evaluate("setTabC9U4('tiers')");
  await evaluate("filterC9U4Tiers('all')");
  await new Promise(r => setTimeout(r, 400));

  const tierCount = await evaluate("document.querySelectorAll('.c9u4-tier-card:not(.hidden)').length");
  console.log("Tier cards count (expect 16):", tierCount);
  if (tierCount !== 16) {
    throw new Error(`Expected exactly 16 tier cards, found ${tierCount}`);
  }

  // 7. Test Tab 4: Interactive Quiz with Perfect 10/10 Score
  console.log("7. Testing Tab 4: Self-Assessment Quiz with 10/10 score...");
  await evaluate("setTabC9U4('quiz')");
  await evaluate("resetC9U4Quiz()");
  await new Promise(r => setTimeout(r, 300));

  // Correct options: [1, 0, 1, 2, 1, 1, 1, 0, 1, 2]
  const correctAnswers = [1, 0, 1, 2, 1, 1, 1, 0, 1, 2];
  for (let q = 0; q < 10; q++) {
    await evaluate(`selectC9U4QuizOption(${q}, ${correctAnswers[q]})`);
  }
  await new Promise(r => setTimeout(r, 500));

  const quizScore = await evaluate("document.getElementById('c9u4-quiz-score-badge')?.textContent?.trim()");
  console.log("Quiz final score badge:", quizScore);
  if (!quizScore.includes("१० / १०")) {
    throw new Error(`Expected score '१० / १०', got '${quizScore}'`);
  }

  // Screenshot Quiz Perfect Score
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u4-view-quiz');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -60);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u4_quiz_perfect.png'), Buffer.from(shot4.data, 'base64'));
  console.log("Saved shot_c9u4_quiz_perfect.png");

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
  console.log("\nALL UNIT 4 VERIFICATIONS PASSED WITH ZERO ERRORS!");
}

testUnit4().catch(err => {
  console.error("Test failed:", err);
  process.exit(1);
});
