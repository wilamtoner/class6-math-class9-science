const { execSync } = require('child_process');
const http = require('http');
const fs = require('fs');

async function main() {
  const browserProc = require('child_process').spawn('chromium', [
    '--headless=new',
    '--remote-debugging-port=9223',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1280,1000'
  ]);

  await new Promise(r => setTimeout(r, 1500));

  function getVersion() {
    return new Promise((resolve, reject) => {
      http.get('http://127.0.0.1:9223/json/version', res => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => resolve(JSON.parse(data)));
      }).on('error', reject);
    });
  }

  const ver = await getVersion();
  const wsUrl = ver.webSocketDebuggerUrl;
  const WebSocket = require('ws');
  const ws = new WebSocket(wsUrl);

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
  await new Promise(r => setTimeout(r, 2500));

  // Switch to exercises tab & structured
  await send('Runtime.evaluate', {
    expression: `
      if (typeof switchC9U7Tab === 'function') switchC9U7Tab('exercises');
      if (typeof filterC9U7Exercise === 'function') filterC9U7Exercise('structured');
    `
  });
  await new Promise(r => setTimeout(r, 1000));

  // 1. Scroll to Derivations 2 & 3
  await send('Runtime.evaluate', {
    expression: `
      const el = document.getElementById('c9u7-struct-card-struct-2');
      if (el) {
        const divs = el.querySelectorAll('div.shadow-xs');
        if (divs.length >= 2) divs[1].scrollIntoView({ behavior: 'instant', block: 'start' });
      }
    `
  });
  await new Promise(r => setTimeout(r, 500));
  let shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66/shot_c9u7_derivations_2_3.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved shot_c9u7_derivations_2_3.png');

  // 2. Scroll to F = ma (struct-11)
  await send('Runtime.evaluate', {
    expression: `
      const el = document.getElementById('c9u7-struct-card-struct-11');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
    `
  });
  await new Promise(r => setTimeout(r, 500));
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66/shot_c9u7_f_ma.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved shot_c9u7_f_ma.png');

  // 3. Scroll to struct-4 (Slope calculation)
  await send('Runtime.evaluate', {
    expression: `
      const el = document.getElementById('c9u7-struct-card-struct-4');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
    `
  });
  await new Promise(r => setTimeout(r, 500));
  shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66/shot_c9u7_slope_graph.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved shot_c9u7_slope_graph.png');

  browserProc.kill();
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
