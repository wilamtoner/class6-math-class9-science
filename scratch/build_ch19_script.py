# -*- coding: utf-8 -*-
import os

script_code = r'''
// ================= CHAPTER 19: SYMMETRY & TESSELLATION JAVASCRIPT ENGINE =================

// 1. Tab Navigation
function setTabCh19(tabName) {
  ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
    const view = document.getElementById('ch19-view-' + t);
    const btn = document.getElementById('ch19-tab-' + t);
    if (view) view.classList.add('hidden');
    if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
  });
  const activeView = document.getElementById('ch19-view-' + tabName);
  const activeBtn = document.getElementById('ch19-tab-' + tabName);
  if (activeView) activeView.classList.remove('hidden');
  if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';

  if (tabName === 'concepts') {
    renderSymmetryShape();
  } else if (tabName === 'quiz') {
    renderCh19Quiz();
  }

  if (window.MathJax && window.MathJax.Hub && activeView) {
    window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
  } else if (window.renderOfflineMath) {
    window.renderOfflineMath(activeView);
  }
}

// 2. Exercise Sub-section Filter
function filterCh19Exercises(sec) {
  const allSecs = ['ex19_1', 'ex19_2', 'unit5_mixed'];
  const btns = {
    'all': document.getElementById('btn-sub-all'),
    'ex19_1': document.getElementById('btn-sub-ex19_1'),
    'ex19_2': document.getElementById('btn-sub-ex19_2'),
    'unit5_mixed': document.getElementById('btn-sub-mixed')
  };

  Object.keys(btns).forEach(k => {
    if (btns[k]) {
      btns[k].className = (k === sec) 
        ? 'ch19-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-sm transition'
        : 'ch19-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-200 transition';
    }
  });

  allSecs.forEach(s => {
    const el = document.getElementById('sec-ch19-' + s);
    if (el) {
      el.classList.toggle('hidden', sec !== 'all' && sec !== s);
    }
  });
}

// 3. Interactive Lab Mode Switcher
function switchCh19Lab(mode) {
  const modes = ['symmetry', 'tessellation', 'mirror'];
  modes.forEach(m => {
    const el = document.getElementById('ch19-lab-mode-' + m);
    const btn = document.getElementById('ch19-lab-btn-' + m);
    if (el) el.classList.toggle('hidden', m !== mode);
    if (btn) {
      btn.className = (m === mode)
        ? 'px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-md transition'
        : 'px-4 py-2 rounded-xl text-xs font-bold text-slate-300 hover:text-white transition';
    }
  });

  if (mode === 'symmetry') {
    renderSymmetryShape();
  } else if (mode === 'tessellation') {
    renderTessellation();
  } else if (mode === 'mirror') {
    initMirrorGrid();
  }
}

// ================= MODE 1: SYMMETRY EXPLORER =================
let currentSymShape = 'equilateral';
let showAllSymLines = true;

const symShapeData = {
  equilateral: {
    name: 'समबाहु त्रिभुज (Equilateral Triangle)',
    badge: '३ वटा अक्ष',
    desc: 'यसका तीनवटै भुजाहरू बराबर हुन्छन्। प्रत्येक शीर्षबिन्दुबाट विपरीत भुजाको मध्यबिन्दुमा खिचेको रेखाले त्रिभुजलाई दुई समान भागमा विभाजन गर्छ।',
    vert: '१ वटा (ठाडो)',
    diag: '२ वटा (छड्के)',
    rot: '३ ($120^\\circ$)',
    tip: '💡 नियमित बहुभुज (Regular Polygon) का जतिवटा भुजा हुन्छन्, त्यति नै वटा सममिति रेखा हुन्छन्!',
    lines: 3,
    render: function(gShape, gLines) {
      // Triangle path
      const p1 = [200, 50], p2 = [70, 275], p3 = [330, 275];
      gShape.innerHTML = `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]}" fill="rgba(59, 130, 246, 0.25)" stroke="#38bdf8" stroke-width="3" stroke-linejoin="round"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Line 1: Top to base midpoint -->
          <line x1="200" y1="20" x2="200" y2="305" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Line 2: P2 to opposite mid (265, 162.5) -->
          <line x1="45" y1="290" x2="285" y2="145" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Line 3: P3 to opposite mid (135, 162.5) -->
          <line x1="355" y1="290" x2="115" y2="145" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Center point -->
          <circle cx="200" cy="200" r="4" fill="#fbbf24"/>
        `;
      }
    }
  },
  isosceles: {
    name: 'समद्विबाहु त्रिभुज (Isosceles Triangle)',
    badge: '१ वटा अक्ष',
    desc: 'दुई बराबर भुजाहरूको साझा शीर्षबिन्दुबाट आधारको मध्यबिन्दु जोड्ने लम्ब रेखा नै यसको एकमात्र सममिति अक्ष हो।',
    vert: '१ वटा (ठाडो)',
    diag: '० वटा',
    rot: '१ ($360^\\circ$)',
    tip: '💡 केवल दुई भुजा बराबर भएकाले अन्य शीर्षबिन्दुबाट खिचेका रेखाहरूले सममिति दिँदैनन्।',
    lines: 1,
    render: function(gShape, gLines) {
      const p1 = [200, 45], p2 = [100, 280], p3 = [300, 280];
      gShape.innerHTML = `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]}" fill="rgba(14, 165, 233, 0.25)" stroke="#38bdf8" stroke-width="3" stroke-linejoin="round"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <line x1="200" y1="20" x2="200" y2="310" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
        `;
      }
    }
  },
  scalene: {
    name: 'विषमबाहु त्रिभुज (Scalene Triangle)',
    badge: '० वटा (कुनै छैन)',
    desc: 'कुनै पनि भुजा वा कोण बराबर हुँदैनन्। यसलाई कुनै पनि रेखाबाट दोब्य्राउँदा दुवै भागहरू खप्टिँदैनन्।',
    vert: '० वटा',
    diag: '० वटा',
    rot: '१ ($360^\\circ$)',
    tip: '💡 विषमबाहु त्रिभुजमा रेखीय सममिति रेखा हुँदैन!',
    lines: 0,
    render: function(gShape, gLines) {
      const p1 = [160, 55], p2 = [60, 275], p3 = [340, 240];
      gShape.innerHTML = `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]}" fill="rgba(244, 63, 94, 0.2)" stroke="#fb7185" stroke-width="3" stroke-linejoin="round"/>`;
      gLines.innerHTML = `
        <text x="200" y="170" fill="#f43f5e" font-size="14" font-weight="bold" text-anchor="middle">❌ कुनै सममिति रेखा छैन</text>
      `;
    }
  },
  square: {
    name: 'वर्ग (Square)',
    badge: '४ वटा अक्ष',
    desc: 'वर्गका चारवटै भुजा र चारवटै कोण बराबर हुन्छन्। विपरीत भुजाका मध्यबिन्दु जोड्ने २ रेखा र २ वटा विकर्ण गरी जम्मा ४ वटा सममिति अक्ष हुन्छन्।',
    vert: '१ ठाडो + १ तेर्सो (२ अक्षीय)',
    diag: '२ वटा (विकर्ण)',
    rot: '४ ($90^\\circ$)',
    tip: '💡 वर्गमा अक्षीय र विकर्ण दुवै गरी कुल ४ वटा सममिति रेखा हुन्छन्!',
    lines: 4,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<rect x="90" y="60" width="220" height="220" rx="4" fill="rgba(16, 185, 129, 0.25)" stroke="#34d399" stroke-width="3"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Vertical -->
          <line x1="200" y1="30" x2="200" y2="310" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Horizontal -->
          <line x1="60" y1="170" x2="340" y2="170" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Diagonal 1 -->
          <line x1="70" y1="40" x2="330" y2="300" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Diagonal 2 -->
          <line x1="70" y1="300" x2="330" y2="40" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
        `;
      }
    }
  },
  rectangle: {
    name: 'आयत (Rectangle)',
    badge: '२ वटा अक्ष',
    desc: 'विपरीत भुजाहरूका मध्यबिन्दु जोड्ने १ ठाडो र १ तेर्सो रेखा मात्र सममिति रेखा हुन्। विकर्णबाट पट्याउँदा कुनाहरू बाहिर निस्कने हुँदा विकर्ण सममिति रेखा बन्दैन!',
    vert: '१ ठाडो + १ तेर्सो',
    diag: '० वटा (विकर्ण सममिति होइन)',
    rot: '२ ($180^\\circ$)',
    tip: '⚠️ ध्यान दिनुहोस्: आयतलाई विकर्णबाट पट्याउँदा कुनाहरू ठ्याक्कै खप्टिँदैनन्!',
    lines: 2,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<rect x="60" y="85" width="280" height="170" rx="4" fill="rgba(168, 85, 247, 0.25)" stroke="#c084fc" stroke-width="3"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Vertical -->
          <line x1="200" y1="45" x2="200" y2="295" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Horizontal -->
          <line x1="30" y1="170" x2="370" y2="170" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Failed Diagonal indicator -->
          <line x1="60" y1="85" x2="340" y2="255" stroke="rgba(244, 63, 94, 0.3)" stroke-width="1.5" stroke-dasharray="3,3"/>
          <text x="300" y="110" fill="#fb7185" font-size="10">विकर्ण ≠ अक्ष</text>
        `;
      }
    }
  },
  rhombus: {
    name: 'समचतुर्भुज (Rhombus)',
    badge: '२ वटा अक्ष',
    desc: 'समचतुर्भुजका चारवटै भुजाहरू बराबर हुन्छन्। यसका दुईवटा विकर्णहरू नै यसका २ वटा सममिति रेखा हुन्। भुजाहरूका मध्यबिन्दु जोड्ने रेखा सममिति हुँदैन।',
    vert: '१ वटा (ठाडो विकर्ण)',
    diag: '१ वटा (तेर्सो विकर्ण)',
    rot: '२ ($180^\\circ$)',
    tip: '💡 समचतुर्भुजमा विकर्णहरू सममिति रेखा हुन्छन् तर मध्यबिन्दु जोड्ने रेखा हुँदैनन् (आयतको उल्टो)!',
    lines: 2,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<polygon points="200,45 330,170 200,295 70,170" fill="rgba(245, 158, 11, 0.25)" stroke="#fbbf24" stroke-width="3"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Vertical diagonal -->
          <line x1="200" y1="20" x2="200" y2="320" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Horizontal diagonal -->
          <line x1="45" y1="170" x2="355" y2="170" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
        `;
      }
    }
  },
  hexagon: {
    name: 'नियमित षट्कोण (Regular Hexagon)',
    badge: '६ वटा अक्ष',
    desc: 'यसका ६ वटा बराबर भुजाहरू हुन्छन्। ३ वटा विपरीत शीर्षबिन्दु जोड्ने विकर्णहरू र ३ वटा विपरीत भुजाका मध्यबिन्दु जोड्ने लम्ब रेखाहरू गरी कुल ६ वटा अक्ष हुन्छन्।',
    vert: '३ विकर्ण',
    diag: '३ मध्यबिन्दु लम्ब',
    rot: '६ ($60^\\circ$)',
    tip: '💡 नियमित षट्कोणले मौरीको घारजस्तै बिना कुनै खाली ठाउँ टेसेलेसन बनाउँछ!',
    lines: 6,
    render: function(gShape, gLines) {
      const cx = 200, cy = 170, r = 115;
      let pts = [];
      for (let i = 0; i < 6; i++) {
        let ang = (i * 60 - 30) * Math.PI / 180;
        pts.push(`${cx + r * Math.cos(ang)},${cy + r * Math.sin(ang)}`);
      }
      gShape.innerHTML = `<polygon points="${pts.join(' ')}" fill="rgba(99, 102, 241, 0.25)" stroke="#818cf8" stroke-width="3"/>`;
      if (showAllSymLines) {
        let linesHtml = '';
        for (let i = 0; i < 6; i++) {
          let ang = (i * 30) * Math.PI / 180;
          let x1 = cx - 145 * Math.cos(ang), y1 = cy - 145 * Math.sin(ang);
          let x2 = cx + 145 * Math.cos(ang), y2 = cy + 145 * Math.sin(ang);
          linesHtml += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f43f5e" stroke-width="2" stroke-dasharray="6,4"/>`;
        }
        gLines.innerHTML = linesHtml;
      }
    }
  },
  circle: {
    name: 'वृत्त (Circle)',
    badge: 'अनन्त (∞) अक्ष',
    desc: 'केन्द्रबिन्दु भएर जाने जुनसुकै सीधा रेखा (व्यास) ले वृत्तलाई दुई बराबर अर्धवृत्तमा बाँड्दछ। त्यसैले वृत्तमा अनन्त सममिति रेखाहरू हुन्छन्।',
    vert: 'अनन्त (ठाडो)',
    diag: 'अनन्त (छड्के)',
    rot: 'अनन्त (कुनै पनि कोण)',
    tip: '💡 वृत्त संसारको सबैभन्दा पूर्ण सममितीय २D ज्यामितीय आकृति हो!',
    lines: 999,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<circle cx="200" cy="170" r="110" fill="rgba(20, 184, 166, 0.25)" stroke="#2dd4bf" stroke-width="3"/>`;
      if (showAllSymLines) {
        let linesHtml = '';
        for (let i = 0; i < 8; i++) {
          let ang = (i * 22.5) * Math.PI / 180;
          let x1 = 200 - 135 * Math.cos(ang), y1 = 170 - 135 * Math.sin(ang);
          let x2 = 200 + 135 * Math.cos(ang), y2 = 170 + 135 * Math.sin(ang);
          linesHtml += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="5,4" opacity="0.85"/>`;
        }
        linesHtml += `<circle cx="200" cy="170" r="5" fill="#fbbf24"/>`;
        gLines.innerHTML = linesHtml;
      }
    }
  }
};

function selectSymmetryShape(key) {
  currentSymShape = key;
  document.querySelectorAll('.sym-shape-btn').forEach(b => {
    b.className = 'sym-shape-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600 transition';
  });
  const btn = document.getElementById('btn-sym-' + key);
  if (btn) btn.className = 'sym-shape-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white transition';
  renderSymmetryShape();
}

function toggleSymmetryLine() {
  showAllSymLines = !showAllSymLines;
  renderSymmetryShape();
}

function renderSymmetryShape() {
  const gShape = document.getElementById('sym-shape-container');
  const gLines = document.getElementById('sym-lines-container');
  if (!gShape || !gLines) return;
  gShape.innerHTML = '';
  gLines.innerHTML = '';

  const data = symShapeData[currentSymShape] || symShapeData['equilateral'];
  data.render(gShape, gLines);

  const tEl = document.getElementById('sym-info-title');
  const bEl = document.getElementById('sym-info-badge');
  const dEl = document.getElementById('sym-info-desc');
  const vEl = document.getElementById('sym-val-vert');
  const dgEl = document.getElementById('sym-val-diag');
  const rEl = document.getElementById('sym-val-rot');
  const tipEl = document.getElementById('sym-info-tip');

  if (tEl) tEl.textContent = data.name;
  if (bEl) bEl.textContent = data.badge;
  if (dEl) dEl.textContent = data.desc;
  if (vEl) vEl.textContent = data.vert;
  if (dgEl) dgEl.textContent = data.diag;
  if (rEl) rEl.textContent = data.rot;
  if (tipEl) tipEl.innerHTML = `<span>💡</span><span>${data.tip.replace('💡 ', '')}</span>`;

  if (window.MathJax && window.MathJax.Hub) {
    const card = document.getElementById('sym-info-card');
    if (card) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, card]);
  }
}

// ================= MODE 2: TESSELLATION STUDIO =================
let currentTessShape = 'square';

const tessThemes = {
  emerald: { bg1: '#047857', bg2: '#059669', bg3: '#10b981', stroke: '#a7f3d0' },
  cyber:   { bg1: '#1d4ed8', bg2: '#2563eb', bg3: '#3b82f6', stroke: '#93c5fd' },
  warm:    { bg1: '#b45309', bg2: '#d97706', bg3: '#f59e0b', stroke: '#fde68a' },
  duo:     { bg1: '#0f172a', bg2: '#334155', bg3: '#64748b', stroke: '#e2e8f0' }
};

function selectTessShape(key) {
  currentTessShape = key;
  document.querySelectorAll('.tess-btn').forEach(b => {
    b.className = 'tess-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600 transition';
  });
  const btn = document.getElementById('btn-tess-' + key);
  if (btn) {
    if (key === 'pentagon') {
      btn.className = 'tess-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-600 text-white transition';
    } else {
      btn.className = 'tess-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-teal-600 text-white transition';
    }
  }
  renderTessellation();
}

function renderTessellation() {
  const gTiles = document.getElementById('tess-tiles-group');
  const gOverlay = document.getElementById('tess-overlay-group');
  if (!gTiles || !gOverlay) return;
  gTiles.innerHTML = '';
  gOverlay.innerHTML = '';

  const themeKey = (document.getElementById('ch19-tess-theme') || {}).value || 'emerald';
  const theme = tessThemes[themeKey] || tessThemes['emerald'];

  const tTitle = document.getElementById('tess-info-title');
  const tBadge = document.getElementById('tess-status-badge');
  const tDesc = document.getElementById('tess-info-desc');
  const tAngle = document.getElementById('tess-angle-each');
  const tCount = document.getElementById('tess-tile-count');
  const tSum = document.getElementById('tess-angle-sum');
  const tReason = document.getElementById('tess-reason-box');

  if (currentTessShape === 'square') {
    if (tTitle) tTitle.textContent = 'वर्गाकार टेसेलेसन (Square Tiling)';
    if (tBadge) {
      tBadge.textContent = 'सफल टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }
    if (tDesc) tDesc.textContent = 'वर्गका चारवटै कोणहरू ९०° हुन्छन्। एउटा साझा शीर्षबिन्दुमा ४ वटा वर्गहरू जोडिँदा कोणहरूको कुल योग ठ्याक्कै ३६०° हुन्छ।';
    if (tAngle) tAngle.textContent = '९०°';
    if (tCount) tCount.textContent = '४ वटा';
    if (tSum) tSum.textContent = '४ × ९०° = ३६०°';
    if (tReason) tReason.textContent = 'कुनै खाली ठाउँ नछाडी र नखप्टाई सम्पूर्ण समतल सतह पूर्ण रूपमा ढाकिएको छ।';

    // Render 7x5 square grid
    const size = 50;
    let tilesHtml = '';
    for (let r = 0; r < 7; r++) {
      for (let c = 0; c < 9; c++) {
        let x = c * size - 15;
        let y = r * size - 5;
        let col = ((r + c) % 2 === 0) ? theme.bg1 : theme.bg2;
        tilesHtml += `<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="${col}" stroke="${theme.stroke}" stroke-width="1.5"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

    // Highlight one shared vertex
    gOverlay.innerHTML = `
      <circle cx="185" cy="145" r="7" fill="#f43f5e"/>
      <circle cx="185" cy="145" r="14" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="185" y="125" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">साझा शीर्षबिन्दु (३६०°)</text>
    `;

  } else if (currentTessShape === 'triangle') {
    if (tTitle) tTitle.textContent = 'समबाहु त्रिभुजाकार टेसेलेसन (Equilateral Triangle Tiling)';
    if (tBadge) {
      tBadge.textContent = 'सफल टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }
    if (tDesc) tDesc.textContent = 'समबाहु त्रिभुजको प्रत्येक भित्री कोण ६०° हुन्छ। साझा शीर्षबिन्दुमा ६ वटा त्रिभुजहरू मिल्दा ६ × ६०° = ३६०° भई सतह भरिन्छ।';
    if (tAngle) tAngle.textContent = '६०°';
    if (tCount) tCount.textContent = '६ वटा';
    if (tSum) tSum.textContent = '६ × ६०° = ३६०°';
    if (tReason) tReason.textContent = 'सुल्टो र उल्टो त्रिभुजहरू पालैपालो जोडेर आकर्षक नियमित टेसेलेसन बन्दछ।';

    const s = 60, h = s * Math.sqrt(3) / 2;
    let tilesHtml = '';
    for (let row = -1; row < 7; row++) {
      let y0 = row * h;
      let y1 = (row + 1) * h;
      for (let col = -1; col < 9; col++) {
        let x0 = col * s + (row % 2) * (s / 2);
        let x1 = x0 + s;
        let xMid = x0 + s / 2;
        // Upward triangle
        let col1 = ((row + col) % 3 === 0) ? theme.bg1 : ((row + col) % 3 === 1) ? theme.bg2 : theme.bg3;
        tilesHtml += `<polygon points="${x0},${y1} ${x1},${y1} ${xMid},${y0}" fill="${col1}" stroke="${theme.stroke}" stroke-width="1.2"/>`;
        // Downward triangle
        let col2 = ((row + col + 1) % 3 === 0) ? theme.bg1 : theme.bg2;
        tilesHtml += `<polygon points="${x0},${y1} ${xMid},${y0} ${x0 - s/2},${y0}" fill="${col2}" stroke="${theme.stroke}" stroke-width="1.2"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

    // Highlight shared vertex with 6 triangles
    gOverlay.innerHTML = `
      <circle cx="210" cy="156" r="6" fill="#fbbf24"/>
      <text x="210" y="140" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">६ वटा त्रिभुजको भेट (३६०°)</text>
    `;

  } else if (currentTessShape === 'hexagon') {
    if (tTitle) tTitle.textContent = 'नियमित षट्कोणीय टेसेलेसन (Honeycomb Hexagon)';
    if (tBadge) {
      tBadge.textContent = 'सफल टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }
    if (tDesc) tDesc.textContent = 'नियमित षट्कोणको प्रत्येक भित्री कोण १२०° हुन्छ। साझा शीर्षबिन्दुमा ३ वटा षट्कोण मिल्दा ३ × १२०° = ३६०° पुग्छ। मौरीको घार यसको प्राकृतिक उदाहरण हो।';
    if (tAngle) tAngle.textContent = '१२०°';
    if (tCount) tCount.textContent = '३ वटा';
    if (tSum) tSum.textContent = '३ × १२०° = ३६०°';
    if (tReason) tReason.textContent = 'न्यूनतम परिधिमा अधिकतम क्षेत्रफल घेर्ने भएकाले प्रकृतिमा मौरीले यही ढाँचा प्रयोग गर्छ।';

    const r = 38;
    const w = Math.sqrt(3) * r;
    const h = 2 * r * 0.75;
    let tilesHtml = '';
    for (let row = -1; row < 7; row++) {
      for (let col = -1; col < 8; col++) {
        let cx = col * w + ((row % 2) * (w / 2));
        let cy = row * h;
        let pts = [];
        for (let i = 0; i < 6; i++) {
          let ang = (i * 60 + 30) * Math.PI / 180;
          pts.push(`${cx + r * Math.cos(ang)},${cy + r * Math.sin(ang)}`);
        }
        let colShade = ((row + col) % 3 === 0) ? theme.bg1 : ((row + col) % 3 === 1) ? theme.bg2 : theme.bg3;
        tilesHtml += `<polygon points="${pts.join(' ')}" fill="${colShade}" stroke="${theme.stroke}" stroke-width="1.8"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

    // Highlight shared vertex of 3 hexagons
    gOverlay.innerHTML = `
      <circle cx="214" cy="142" r="6" fill="#f43f5e"/>
      <text x="214" y="125" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">३ वटा षट्कोण (३ × १२०° = ३६०°)</text>
    `;

  } else if (currentTessShape === 'brick') {
    if (tTitle) tTitle.textContent = 'आयताकार इँटाको टेसेलेसन (Brick Running Bond)';
    if (tBadge) {
      tBadge.textContent = 'व्यावहारिक टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-blue-500/20 text-blue-300 border border-blue-500/30';
    }
    if (tDesc) tDesc.textContent = 'घरको पर्खाल लगाउँदा आयताकार इँटाहरूलाई आधा-आधा खप्टाएर (Running bond) बिछ्याइन्छ। यसले पर्खाललाई बलियो बनाउँछ र खाली ठाउँ छोड्दैन।';
    if (tAngle) tAngle.textContent = '९०°';
    if (tCount) tCount.textContent = '४ वा ३ वटा';
    if (tSum) tSum.textContent = '२ × ९०° + १८०° = ३६०°';
    if (tReason) tReason.textContent = 'इँटाको पर्खाल निर्माणमा प्रयोग हुने विश्वप्रसिद्ध इन्जिनियरिङ टेसेलेसन।';

    const bw = 70, bh = 32;
    let tilesHtml = '';
    for (let r = 0; r < 11; r++) {
      let offset = (r % 2 === 0) ? 0 : -bw / 2;
      for (let c = -1; c < 8; c++) {
        let x = c * bw + offset;
        let y = r * bh;
        let col = ((r + c) % 2 === 0) ? '#b45309' : '#d97706';
        tilesHtml += `<rect x="${x}" y="${y}" width="${bw}" height="${bh}" fill="${col}" stroke="#fde68a" stroke-width="1.5"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

  } else if (currentTessShape === 'pentagon') {
    if (tTitle) tTitle.textContent = 'नियमित पञ्चकोण (Regular Pentagon Test)';
    if (tBadge) {
      tBadge.textContent = 'टेसेलेसन असम्भव ❌';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-rose-500/20 text-rose-300 border border-rose-500/30';
    }
    if (tDesc) tDesc.textContent = 'नियमित पञ्चकोणको भित्री कोण १०८° हुन्छ। ३ वटा जोड्दा ३२४° मात्र हुन्छ (३६° खाली ठाउँ बाँकी रहन्छ)। ४ वटा जोड्दा ४३२° भई खप्टिन्छ!';
    if (tAngle) tAngle.textContent = '१०८°';
    if (tCount) tCount.textContent = '३ वटा जोड्दा';
    if (tSum) tSum.textContent = '३ × १०८° = ३२४° (< ३६०°)';
    if (tReason) tReason.textContent = '३६०° लाई १०८° ले भाग गर्दा ३.३३ आउँछ (पूर्ण सङ्ख्या नहुने)। तसर्थ पञ्चकोणले टेसेलेसन बनाउन सक्दैन!';

    // Render 3 regular pentagons meeting at center with a visible gap
    const cx = 210, cy = 175, r = 75;
    let tilesHtml = '';
    const angles = [0, 108, 216];
    angles.forEach((startDeg, idx) => {
      let pts = [];
      for (let i = 0; i < 5; i++) {
        let a = (startDeg + i * 72 - 54) * Math.PI / 180;
        pts.push(`${cx + r * Math.cos(a)},${cy + r * Math.sin(a)}`);
      }
      tilesHtml += `<polygon points="${pts.join(' ')}" fill="rgba(244, 63, 94, 0.4)" stroke="#fb7185" stroke-width="2.5"/>`;
    });

    // Render GAP sector
    tilesHtml += `
      <!-- Gap arc -->
      <path d="M 210 175 L 285 175 A 75 75 0 0 1 270 235 Z" fill="rgba(251, 191, 36, 0.4)" stroke="#f59e0b" stroke-width="2"/>
    `;
    gTiles.innerHTML = tilesHtml;

    gOverlay.innerHTML = `
      <circle cx="210" cy="175" r="7" fill="#f43f5e"/>
      <text x="210" y="80" fill="#fb7185" font-size="13" font-weight="black" text-anchor="middle">❌ खाली ठाउँ (३६° Gap)</text>
      <text x="210" y="98" fill="#cbd5e1" font-size="11" text-anchor="middle">३ वटा पञ्चकोण = ३२४° (३६०° पुगेन)</text>
    `;
  }
}

// ================= MODE 3: MIRROR REFLECTION GRID =================
const GRID_ROWS = 8;
const GRID_COLS = 8; // 0..3 Left, 4..7 Right
let mirrorGridState = []; // 8x8 boolean

function initMirrorGrid() {
  loadMirrorPreset('rocket');
}

function clearMirrorGrid() {
  mirrorGridState = Array(GRID_ROWS).fill(null).map(() => Array(GRID_COLS).fill(false));
  renderMirrorGridDom();
  setMirrorFeedback('ग्रिड खाली गरियो। नयाँ आकृति कोर्नुहोस् वा नमुना छान्नुहोस्।', 'text-slate-300');
}

function loadMirrorPreset(name) {
  mirrorGridState = Array(GRID_ROWS).fill(null).map(() => Array(GRID_COLS).fill(false));

  if (name === 'rocket') {
    // Left side rocket
    mirrorGridState[0][3] = true;
    mirrorGridState[1][3] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true; mirrorGridState[5][1] = true;
    mirrorGridState[6][3] = true; mirrorGridState[6][2] = true; mirrorGridState[6][0] = true;
    mirrorGridState[7][3] = true; mirrorGridState[7][1] = true;
  } else if (name === 'heart') {
    mirrorGridState[1][2] = true; mirrorGridState[1][1] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true; mirrorGridState[2][1] = true; mirrorGridState[2][0] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true; mirrorGridState[3][1] = true; mirrorGridState[3][0] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true; mirrorGridState[4][1] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true;
    mirrorGridState[6][3] = true;
  } else if (name === 'tree') {
    mirrorGridState[0][3] = true;
    mirrorGridState[1][3] = true; mirrorGridState[1][2] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true; mirrorGridState[3][1] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true; mirrorGridState[4][1] = true; mirrorGridState[4][0] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true;
    mirrorGridState[6][3] = true;
    mirrorGridState[7][3] = true;
  } else if (name === 'arrow') {
    mirrorGridState[1][3] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true; mirrorGridState[3][1] = true; mirrorGridState[3][0] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true; mirrorGridState[4][1] = true; mirrorGridState[4][0] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true;
    mirrorGridState[6][3] = true;
  }

  renderMirrorGridDom();
  setMirrorFeedback('बायाँ भाग तयार छ। दायाँतर्फ क्लिक गरी ऐना प्रतिबिम्ब पूरा गर्नुहोस्!', 'text-cyan-300');
}

function renderMirrorGridDom() {
  const container = document.getElementById('ch19-mirror-grid');
  if (!container) return;
  container.innerHTML = '';
  container.style.gridTemplateColumns = `repeat(${GRID_COLS}, 32px)`;

  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < GRID_COLS; c++) {
      const cell = document.createElement('button');
      cell.className = 'w-8 h-8 rounded text-xs font-bold transition flex items-center justify-center cursor-pointer ';
      
      const isLeft = c < 4;
      const isFilled = mirrorGridState[r][c];

      // Mirror line border indicator between col 3 and col 4
      if (c === 3) {
        cell.classList.add('border-r-2', 'border-rose-500');
      } else {
        cell.classList.add('border', 'border-slate-800');
      }

      if (isLeft) {
        cell.className += isFilled ? 'bg-blue-600 text-white' : 'bg-slate-900/60 hover:bg-slate-800 text-transparent';
        cell.onclick = () => toggleGridTile(r, c);
      } else {
        cell.className += isFilled ? 'bg-emerald-500 text-white shadow' : 'bg-slate-900/80 hover:bg-slate-700 text-transparent';
        cell.onclick = () => toggleGridTile(r, c);
      }

      container.appendChild(cell);
    }
  }
}

function toggleGridTile(r, c) {
  mirrorGridState[r][c] = !mirrorGridState[r][c];
  renderMirrorGridDom();
}

function autoCompleteMirror() {
  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < 4; c++) {
      const mirrorCol = 7 - c;
      mirrorGridState[r][mirrorCol] = mirrorGridState[r][c];
    }
  }
  renderMirrorGridDom();
  setMirrorFeedback('✨ ऐना प्रतिबिम्ब स्वतः पूरा भयो! दुवै भाग दुरुस्त सममितीय छन्।', 'text-emerald-400');
}

function checkMirrorSymmetry() {
  let errors = 0;
  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < 4; c++) {
      const mirrorCol = 7 - c;
      if (mirrorGridState[r][c] !== mirrorGridState[r][mirrorCol]) {
        errors++;
      }
    }
  }

  if (errors === 0) {
    setMirrorFeedback('🎉 उत्कृष्ट! तपाईंको चित्र पूर्ण रूपमा सममितीय छ (Symmetric Match)!', 'text-emerald-400 font-extrabold text-sm');
  } else {
    setMirrorFeedback(`⚠️ अझै ${errors} ठाउँमा मिलेको छैन। डट रेखाबाट दायाँ र बायाँको दूरी पुनः गन्नुहोस्!`, 'text-amber-400 font-bold');
  }
}

function setMirrorFeedback(msg, colorClass) {
  const fb = document.getElementById('mirror-feedback');
  if (fb) {
    fb.textContent = msg;
    fb.className = `mt-3 text-xs font-bold ${colorClass} min-h-[20px] text-center transition`;
  }
}

// ================= 4. SELF-ASSESSMENT QUIZ ENGINE =================
const ch19QuizQuestions = [
  {
    id: 'q1',
    question: 'समबाहु त्रिभुज (Equilateral Triangle) मा कतिवटा सममिति रेखा हुन्छन्?',
    options: ['१ वटा', '२ वटा', '३ वटा', '४ वटा'],
    correct: 2,
    explanation: 'समबाहु त्रिभुजका तीनवटै भुजाहरू बराबर हुने भएकाले यसका प्रत्येक शीर्षबिन्दुबाट विपरीत भुजाको मध्यबिन्दुमा ३ वटा सममिति रेखा खिच्न सकिन्छ।'
  },
  {
    id: 'q2',
    question: 'तलका मध्ये कुन अङ्ग्रेजी क्यापिटल अक्षरमा ठाडो र तेर्सो दुवै सममिति रेखा हुन्छ?',
    options: ['अक्षर A', 'अक्षर M', 'अक्षर H', 'अक्षर E'],
    correct: 2,
    explanation: 'अक्षर H लाई ठाडो र तेर्सो दुवै रेखाबाट पट्याउँदा दुरुस्त खप्टिन्छ। अक्षर A र M मा ठाडो मात्र र E मा तेर्सो मात्र हुन्छ।'
  },
  {
    id: 'q3',
    question: 'आयत (Rectangle) मा कतिवटा सममिति रेखा हुन्छन्?',
    options: ['४ वटा', '२ वटा', '१ वटा', 'शून्य (हुँदैन)'],
    correct: 1,
    explanation: 'आयतका विपरीत भुजाहरूका मध्यबिन्दु जोड्ने १ ठाडो र १ तेर्सो गरी २ वटा मात्र अक्ष हुन्छन्। विकर्णबाट पट्याउँदा कुनाहरू नखप्टिने भएकाले विकर्ण सममिति रेखा हुँदैन।'
  },
  {
    id: 'q4',
    question: 'टेसेलेसन हुनका लागि साझा शीर्षबिन्दु (Vertex) मा बन्ने कोणहरूको योगफल कति हुनुपर्दछ?',
    options: ['१८०°', '२७०°', '३६०°', '५४०°'],
    correct: 2,
    explanation: 'समतल सतहलाई बिना खाली ठाउँ र नखप्टाई पूर्ण रूपमा ढाक्न शीर्षबिन्दु वरिपरिका भित्री कोणहरूको योग ठ्याक्कै ३६०° हुनुपर्छ।'
  },
  {
    id: 'q5',
    question: 'तलका मध्ये कुन नियमित बहुभुजले एक्लै नियमित टेसेलेसन बनाउन सक्दैन?',
    options: ['समबाहु त्रिभुज', 'वर्ग', 'नियमित पञ्चकोण', 'नियमित षट्कोण'],
    correct: 2,
    explanation: 'नियमित पञ्चकोणको प्रत्येक भित्री कोण १०८° हुन्छ र ३६०° लाई १०८° ले निःशेष भाग जाँदैन (३.३३ आउँछ)। त्यसैले पञ्चकोणले टेसेलेसन बनाउन सक्दैन।'
  },
  {
    id: 'q6',
    question: 'नियमित षट्कोणको प्रत्येक भित्री कोण १२०° हुन्छ। यसको टेसेलेसनमा एउटा शीर्षबिन्दुमा कतिवटा षट्कोण भेटिन्छन्?',
    options: ['२ वटा', '३ वटा', '४ वटा', '६ वटा'],
    correct: 1,
    explanation: '३ × १२०° = ३६०° हुने भएकाले प्रत्येक साझा शीर्षबिन्दुमा ३ वटा नियमित षट्कोणहरू आपसमा जोडिन्छन्।'
  },
  {
    id: 'q7',
    question: 'वृत्त (Circle) मा कतिवटा सममिति रेखाहरू हुन्छन्?',
    options: ['४ वटा', '३६० वटा', '१ वटा', 'अनन्त (Infinite)'],
    correct: 3,
    explanation: 'केन्द्रबिन्दु भएर जाने जुनसुकै सीधा रेखा (व्यास) ले वृत्तलाई दुई दुरुस्त आधा भागमा बाँड्ने भएकाले वृत्तमा अनन्त सममिति रेखाहरू हुन्छन्।'
  },
  {
    id: 'q8',
    question: 'नियमित अष्टकोण (१३५°) र वर्ग (९०°) मिलेर भुइँमा टेसेलेसन बन्दा साझा शीर्षबिन्दुमा कोणहरूको योग कति हुन्छ?',
    options: ['३६०° (२ अष्टकोण + १ वर्ग)', '२७०°', '४००°', '३००°'],
    correct: 0,
    explanation: 'दुईवटा अष्टकोण (२ × १३५° = २७०°) र एउटा वर्ग (९०°) जोड्दा कुल २७०° + ९०° = ३६०° पुग्ने भएकाले यिनीहरूले अर्ध-नियमित टेसेलेसन बनाउँछन्।'
  },
  {
    id: 'q9',
    question: 'कुन चतुर्भुजमा रेखीय सममिति रेखा हुँदैन (० वटा हुन्छ)?',
    options: ['वर्ग', 'आयत', 'समचतुर्भुज', 'साधारण समानान्तर चतुर्भुज'],
    correct: 3,
    explanation: 'साधारण समानान्तर चतुर्भुज (Parallelogram) लाई कुनै पनि ठाडो, तेर्सो वा विकर्ण रेखाबाट दोब्य्राउँदा भुजाहरू ठ्याक्कै खप्टिँदैनन्। त्यसैले यसमा रेखीय सममिति हुँदैन।'
  },
  {
    id: 'q10',
    question: 'कुनै पनि n-भुजा भएको नियमित बहुभुजमा सममिति रेखाको सङ्ख्या कति हुन्छ?',
    options: ['n - २', 'n वटा', '२n वटा', 'n / २'],
    correct: 1,
    explanation: 'नियमित बहुभुज (जस्तै समबाहु त्रिभुजमा ३, वर्गमा ४, पञ्चकोणमा ५, षट्कोणमा ६) मा सममिति रेखाको सङ्ख्या भुजाहरूको सङ्ख्या n बराबर हुन्छ।'
  }
];

let ch19UserAnswers = {};

function renderCh19Quiz() {
  const container = document.getElementById('ch19-quiz-container');
  if (!container) return;
  container.innerHTML = '';

  ch19QuizQuestions.forEach((q, idx) => {
    const answered = ch19UserAnswers.hasOwnProperty(q.id);
    const selectedOpt = ch19UserAnswers[q.id];

    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3';

    let optionsHtml = '';
    q.options.forEach((opt, oIdx) => {
      let optClass = 'w-full text-left p-3 rounded-xl border text-xs md:text-sm font-semibold transition flex items-center justify-between ';
      if (!answered) {
        optClass += 'border-slate-200 hover:bg-slate-50 text-slate-700 cursor-pointer';
      } else {
        if (oIdx === q.correct) {
          optClass += 'border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
        } else if (oIdx === selectedOpt) {
          optClass += 'border-rose-500 bg-rose-50 text-rose-900 font-bold';
        } else {
          optClass += 'border-slate-200 text-slate-400 opacity-60';
        }
      }

      optionsHtml += `
        <button onclick="handleCh19QuizAnswer('${q.id}', ${oIdx})" ${answered ? 'disabled' : ''} class="${optClass}">
          <span>${String.fromCharCode(65 + oIdx)}. ${opt}</span>
          ${answered && oIdx === q.correct ? '<span class="text-emerald-600 font-black">✓ सही</span>' : ''}
          ${answered && oIdx === selectedOpt && oIdx !== q.correct ? '<span class="text-rose-600 font-black">✗ गलत</span>' : ''}
        </button>
      `;
    });

    let explanationHtml = '';
    if (answered) {
      explanationHtml = `
        <div class="mt-3 p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-600 space-y-1">
          <strong class="text-slate-800">💡 व्याख्या:</strong> ${q.explanation}
        </div>
      `;
    }

    card.innerHTML = `
      <div class="flex items-center justify-between border-b border-slate-100 pb-2">
        <span class="text-xs font-bold text-blue-600">प्रश्न ${idx + 1} / ${ch19QuizQuestions.length}</span>
        <span class="text-[11px] font-mono text-slate-400">१ अङ्क</span>
      </div>
      <p class="font-extrabold text-sm md:text-base text-slate-800">${q.question}</p>
      <div class="space-y-2 pt-1">
        ${optionsHtml}
      </div>
      ${explanationHtml}
    `;

    container.appendChild(card);
  });
}

function handleCh19QuizAnswer(qId, optIdx) {
  if (ch19UserAnswers.hasOwnProperty(qId)) return;
  ch19UserAnswers[qId] = optIdx;

  // Calculate score
  let score = 0;
  ch19QuizQuestions.forEach(q => {
    if (ch19UserAnswers[q.id] === q.correct) {
      score++;
    }
  });

  const scoreEl = document.getElementById('ch19-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `${score} / ${ch19QuizQuestions.length}`;
  }

  renderCh19Quiz();
}

function resetCh19Quiz() {
  ch19UserAnswers = {};
  const scoreEl = document.getElementById('ch19-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `० / ${ch19QuizQuestions.length}`;
  }
  renderCh19Quiz();
}

// Expose to window for global access
window.setTabCh19 = setTabCh19;
window.filterCh19Exercises = filterCh19Exercises;
window.switchCh19Lab = switchCh19Lab;
window.selectSymmetryShape = selectSymmetryShape;
window.toggleSymmetryLine = toggleSymmetryLine;
window.renderSymmetryShape = renderSymmetryShape;
window.selectTessShape = selectTessShape;
window.renderTessellation = renderTessellation;
window.toggleGridTile = toggleGridTile;
window.clearMirrorGrid = clearMirrorGrid;
window.loadMirrorPreset = loadMirrorPreset;
window.autoCompleteMirror = autoCompleteMirror;
window.checkMirrorSymmetry = checkMirrorSymmetry;
window.initMirrorGrid = initMirrorGrid;
window.renderCh19Quiz = renderCh19Quiz;
window.handleCh19QuizAnswer = handleCh19QuizAnswer;
window.resetCh19Quiz = resetCh19Quiz;
'''

with open('scratch/ch19_script.js', 'w', encoding='utf-8') as f:
    f.write(script_code.strip() + '\n')

print("scratch/ch19_script.js created successfully!")
