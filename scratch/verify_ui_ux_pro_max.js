const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

async function main() {
  const brainDir = '/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66';
  const chrome = spawn('chromium', [
    '--headless=new',
    '--remote-debugging-port=9240',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,1000'
  ]);

  await new Promise(r => setTimeout(r, 1500));

  function getVersion() {
    return new Promise((resolve, reject) => {
      http.get('http://127.0.0.1:9240/json', res => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => resolve(JSON.parse(data)));
      }).on('error', reject);
    });
  }

  const targets = await getVersion();
  const WebSocket = require('ws');
  const ws = new WebSocket(targets[0].webSocketDebuggerUrl);

  let id = 1;
  const pending = {};
  ws.on('message', data => {
    const msg = JSON.parse(data);
    if (msg.id && pending[msg.id]) {
      pending[msg.id](msg.result);
      delete pending[msg.id];
    }
  });

  function send(method, params = {}) {
    return new Promise(resolve => {
      const msgId = id++;
      pending[msgId] = resolve;
      ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  await new Promise(r => ws.on('open', r));
  await send('Page.enable');
  await send('Runtime.enable');

  const fileUrl = 'file:///run/media/nepal/Backup1/class%206%20maths/index.html?grade=9&unit=7';
  await send('Page.navigate', { url: fileUrl });
  await new Promise(r => setTimeout(r, 2000));

  // 1. Desktop Screenshot of Header and Tabs
  console.log("1. Capturing Desktop Header and Tabs...");
  const metricsDesktop = await send('Runtime.evaluate', {
    expression: '({ innerWidth: window.innerWidth, scrollWidth: document.documentElement.scrollWidth })',
    returnByValue: true
  });
  console.log("Desktop Viewport Metrics:", metricsDesktop.result.value);

  let shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_ui_ux_desktop_header.png'), Buffer.from(shot.data, 'base64'));
  console.log("Saved: shot_ui_ux_desktop_header.png");

  // 2. Switch to Grade 6 to test switcher
  console.log("2. Testing Grade 6 Switch...");
  await send('Runtime.evaluate', { expression: 'selectGrade(6);' });
  await new Promise(r => setTimeout(r, 800));

  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_ui_ux_grade6_view.png'), Buffer.from(shot.data, 'base64'));
  console.log("Saved: shot_ui_ux_grade6_view.png");

  // 3. Switch back to Grade 9 Unit 7
  await send('Runtime.evaluate', { expression: 'selectGrade(9); switchGrade9Unit(7);' });
  await new Promise(r => setTimeout(r, 800));

  // 4. Test Mobile Viewport 375x812
  console.log("4. Resizing to Mobile 375x812...");
  await send('Emulation.setDeviceMetricsOverride', {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });
  await new Promise(r => setTimeout(r, 800));

  const metricsMobile = await send('Runtime.evaluate', {
    expression: '({ innerWidth: window.innerWidth, scrollWidth: document.documentElement.scrollWidth })',
    returnByValue: true
  });
  console.log("Mobile Viewport Metrics:", metricsMobile.result.value);

  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(brainDir, 'shot_ui_ux_mobile_view.png'), Buffer.from(shot.data, 'base64'));
  console.log("Saved: shot_ui_ux_mobile_view.png");

  chrome.kill();
  console.log("Verification finished successfully!");
  process.exit(0);
}

main().catch(err => {
  console.error("Verification error:", err);
  process.exit(1);
});
