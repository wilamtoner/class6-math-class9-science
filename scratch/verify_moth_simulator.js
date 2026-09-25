const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const brainDir = '/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66';

async function verifyMothSimulator() {
  const tmpDir = '/tmp/cdp_moth_test_' + Date.now();
  console.log("Starting Headless Chromium for Peppered Moth Simulator Verification...");
  const chromeProc = spawn('chromium', [
    '--headless',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9227',
    `--user-data-dir=${tmpDir}`,
    '--window-size=1280,1050',
    'file:///run/media/nepal/Backup1/class 6 maths/index.html?grade=9&unit=4'
  ]);

  function cleanup() {
    try { chromeProc.kill(); } catch (e) {}
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
  process.on('exit', cleanup);
  process.on('SIGINT', cleanup);

  await new Promise(r => setTimeout(r, 2500));

  const listRes = await fetch('http://127.0.0.1:9227/json');
  const tabs = await listRes.json();
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  console.log("Connected to WebSocket:", pageTab.webSocketDebuggerUrl);

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

  // Activate Unit 4 and Simulator Mode
  console.log("1. Activating Unit 4 and Natural Selection Mode...");
  await evaluate("selectGrade(9)");
  await evaluate("switchGrade9Unit(4)");
  await evaluate("setTabC9U4('concepts')");
  await evaluate("setLabModeC9U4('selection')");
  await new Promise(r => setTimeout(r, 400));

  // Check Bark View and Moth Items
  console.log("2. Checking Moth population and SVG elements...");
  const mothState1 = await evaluate(`
    (() => {
      const barkSvg = document.getElementById('c9u4-bark-svg');
      const moths = document.querySelectorAll('#c9u4-bark-view .moth-item');
      const whiteCount = document.getElementById('c9u4-white-count')?.textContent;
      const blackCount = document.getElementById('c9u4-black-count')?.textContent;
      const whitePct = document.getElementById('c9u4-white-pct')?.textContent;
      const blackPct = document.getElementById('c9u4-black-pct')?.textContent;
      const genBadge = document.getElementById('c9u4-moth-gen-badge')?.textContent;
      const timelineDots = document.querySelectorAll('#c9u4-gen-timeline span').length;

      return {
        hasBarkSvg: !!barkSvg,
        mothCount: moths.length,
        whiteCount,
        blackCount,
        whitePct,
        blackPct,
        genBadge,
        timelineDots
      };
    })()
  `);
  console.log("Initial Simulator State:", mothState1);

  if (!mothState1.hasBarkSvg || mothState1.mothCount !== 12) {
    throw new Error(`Expected SVG bark with 12 moths! Found hasBarkSvg=${mothState1.hasBarkSvg}, mothCount=${mothState1.mothCount}`);
  }

  // Test Hunting a Moth by click
  console.log("3. Testing Moth Hunt click interaction...");
  const huntRes = await evaluate(`
    (() => {
      const firstMoth = document.querySelector('#c9u4-bark-view .moth-item');
      if (firstMoth) {
        firstMoth.dispatchEvent(new MouseEvent('click', { bubbles: true }));
      }
      return {
        scoreText: document.getElementById('c9u4-hunt-live-score')?.textContent
      };
    })()
  `);
  console.log("Post-click hunt score:", huntRes);
  await new Promise(r => setTimeout(r, 400));

  // Test Next Generation Step
  console.log("4. Testing Next Generation Step (Bird Swoop & Population Evolution)...");
  await evaluate("stepMothGenC9U4()");
  await new Promise(r => setTimeout(r, 700));

  const mothStateGen2 = await evaluate(`
    (() => ({
      genBadge: document.getElementById('c9u4-moth-gen-badge')?.textContent,
      whitePct: document.getElementById('c9u4-white-pct')?.textContent,
      blackPct: document.getElementById('c9u4-black-pct')?.textContent,
      whiteBarW: document.getElementById('c9u4-white-bar')?.style.width,
      blackBarW: document.getElementById('c9u4-black-bar')?.style.width,
      mothCount: document.querySelectorAll('#c9u4-bark-view .moth-item').length
    }))()
  `);
  console.log("Generation 2 State:", mothStateGen2);

  if (!mothStateGen2.genBadge.includes('पुस्ता २')) {
    throw new Error(`Expected Generation 2, got: ${mothStateGen2.genBadge}`);
  }

  // Test Switching to Polluted Environment
  console.log("5. Testing Switch to Polluted Sooty Environment...");
  await evaluate("setMothEnvC9U4('polluted')");
  await new Promise(r => setTimeout(r, 500));

  const polState = await evaluate(`
    (() => ({
      envLabel: document.getElementById('c9u4-moth-env-label')?.textContent,
      whitePct: document.getElementById('c9u4-white-pct')?.textContent,
      blackPct: document.getElementById('c9u4-black-pct')?.textContent,
      whiteCount: document.getElementById('c9u4-white-count')?.textContent,
      blackCount: document.getElementById('c9u4-black-count')?.textContent,
      advBadge: document.getElementById('c9u4-advantage-badge')?.textContent,
      mothCount: document.querySelectorAll('#c9u4-bark-view .moth-item').length
    }))()
  `);
  console.log("Polluted Environment State:", polState);

  // Take High-Res Screenshot of Working Simulator
  console.log("6. Taking High-Resolution Screenshot of Working Peppered Moth Simulator...");
  await evaluate(`
    (() => {
      const el = document.getElementById('c9u4-lab-mode-selection');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      window.scrollBy(0, -50);
    })()
  `);
  await new Promise(r => setTimeout(r, 400));
  const shot1 = await send('Page.captureScreenshot', { format: 'png' });
  const shotPath = path.join(brainDir, 'shot_c9u4_selection_working.png');
  fs.writeFileSync(shotPath, Buffer.from(shot1.data, 'base64'));
  console.log("Saved screenshot to:", shotPath);

  // Also test Clean environment screenshot
  await evaluate("setMothEnvC9U4('clean')");
  await new Promise(r => setTimeout(r, 400));
  const shotClean = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_c9u4_selection.png'), Buffer.from(shotClean.data, 'base64'));
  console.log("Updated shot_c9u4_selection.png with clean bark & moths");

  // Verify Homology and Mutation SVGs
  console.log("7. Verifying Homology & Mutation SVGs...");
  await evaluate("setLabModeC9U4('anatomy')");
  await evaluate("selectHomologyOrganC9U4('bat')");
  const batSvgCheck = await evaluate("!!document.querySelector('#c9u4-homology-svg-wrap svg')");

  await evaluate("setLabModeC9U4('mutation')");
  await evaluate("selectMutationDemoC9U4('polydactyly')");
  const muSvgCheck = await evaluate("!!document.querySelector('#c9u4-mutation-svg-wrap svg')");

  console.log("Homology SVG present?", batSvgCheck, "Mutation SVG present?", muSvgCheck);
  if (!batSvgCheck || !muSvgCheck) {
    throw new Error("Missing dynamic SVGs in Anatomy or Mutation modes!");
  }

  // Horizontal Overflow Check
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
  console.log("\nALL PEPPERED MOTH SIMULATOR TESTS PASSED WITH 100% SUCCESS!");
}

verifyMothSimulator().catch(err => {
  console.error("Verification failed:", err);
  process.exit(1);
});
