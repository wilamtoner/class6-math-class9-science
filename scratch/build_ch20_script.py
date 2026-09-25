# -*- coding: utf-8 -*-
import os

script_code = r'''
// ================= CHAPTER 20: STATISTICS JAVASCRIPT ENGINE =================

// 1. Tab Navigation
function setTabCh20(tabName) {
  ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
    const view = document.getElementById('ch20-view-' + t);
    const btn = document.getElementById('ch20-tab-' + t);
    if (view) view.classList.add('hidden');
    if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
  });
  const activeView = document.getElementById('ch20-view-' + tabName);
  const activeBtn = document.getElementById('ch20-tab-' + tabName);
  if (activeView) activeView.classList.remove('hidden');
  if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';

  if (tabName === 'concepts') {
    renderBarStudio();
  } else if (tabName === 'quiz') {
    renderCh20Quiz();
  }

  if (window.MathJax && window.MathJax.Hub && activeView) {
    window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
  } else if (window.renderOfflineMath) {
    window.renderOfflineMath(activeView);
  }
}

// 2. Exercise Sub-section Filter
function filterCh20Exercises(sec) {
  const allSecs = ['ex20_1', 'ex20_2', 'unit6_mixed'];
  const btns = {
    'all': document.getElementById('btn-sub20-all'),
    'ex20_1': document.getElementById('btn-sub20-ex20_1'),
    'ex20_2': document.getElementById('btn-sub20-ex20_2'),
    'unit6_mixed': document.getElementById('btn-sub20-mixed')
  };

  Object.keys(btns).forEach(k => {
    if (btns[k]) {
      btns[k].className = (k === sec) 
        ? 'ch20-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-sm transition'
        : 'ch20-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-200 transition';
    }
  });

  allSecs.forEach(s => {
    const el = document.getElementById('sec-ch20-' + s);
    if (el) {
      el.classList.toggle('hidden', sec !== 'all' && sec !== s);
    }
  });
}

// 3. Interactive Lab Mode Switcher
function switchCh20Lab(mode) {
  const modes = ['barStudio', 'tallyLab', 'readerLab'];
  modes.forEach(m => {
    const el = document.getElementById('ch20-lab-mode-' + m);
    const btn = document.getElementById('ch20-lab-btn-' + m);
    if (el) el.classList.toggle('hidden', m !== mode);
    if (btn) {
      btn.className = (m === mode)
        ? 'px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-md transition'
        : 'px-4 py-2 rounded-xl text-xs font-bold text-slate-300 hover:text-white transition';
    }
  });

  if (mode === 'barStudio') {
    renderBarStudio();
  } else if (mode === 'tallyLab') {
    initTallyLab();
  } else if (mode === 'readerLab') {
    initReaderLab();
  }
}

// ================= MODE 1: DYNAMIC BAR CHART STUDIO =================
let currentBarPreset = 'absent';

const barDatasets = {
  absent: {
    title: 'हप्ताका ६ दिनमा अनुपस्थित विद्यार्थी सङ्ख्या सम्बन्धी साधारण स्तम्भ चित्र',
    xAxisLabel: 'दिनहरू (Days)',
    yAxisLabel: 'विद्यार्थी सङ्ख्या',
    scaleText: 'Y-अक्ष: १ से.मि. = ५ जना',
    data: [
      { label: 'आइतबार', val: 5 },
      { label: 'सोमबार', val: 10 },
      { label: 'मङ्गलबार', val: 25 },
      { label: 'बुधबार', val: 10 },
      { label: 'बिहीबार', val: 5 },
      { label: 'शुक्रबार', val: 5 }
    ]
  },
  subjects: {
    title: 'सौरभको पहिलो त्रैमासिक परीक्षा प्राप्ताङ्क सम्बन्धी स्तम्भ चित्र',
    xAxisLabel: 'विषयहरू (Subjects)',
    yAxisLabel: 'प्राप्ताङ्क (अङ्क)',
    scaleText: 'Y-अक्ष: १ से.मि. = १० अङ्क',
    data: [
      { label: 'नेपाली', val: 65 },
      { label: 'गणित', val: 90 },
      { label: 'अङ्ग्रेजी', val: 75 },
      { label: 'विज्ञान', val: 80 },
      { label: 'सामाजिक', val: 55 }
    ]
  },
  population: {
    title: 'सहरको ६ वर्षको जनसङ्ख्या (लाखमा) स्तम्भ चित्र',
    xAxisLabel: 'वर्ष (वि.सं.)',
    yAxisLabel: 'जनसङ्ख्या (लाखमा)',
    scaleText: 'Y-अक्ष: १ से.मि. = १० लाख',
    data: [
      { label: '२०७०', val: 35 },
      { label: '२०७१', val: 40 },
      { label: '२०७२', val: 50 },
      { label: '२०७३', val: 65 },
      { label: '२०७४', val: 90 },
      { label: '२०७५', val: 100 }
    ]
  },
  expenses: {
    title: 'परिवारको वार्षिक खर्च (रू. हजारमा) सम्बन्धी स्तम्भ चित्र',
    xAxisLabel: 'खर्च शीर्षकहरू',
    yAxisLabel: 'रकम (रू. हजारमा)',
    scaleText: 'Y-अक्ष: १ से.मि. = १० हजार',
    data: [
      { label: 'खाना', val: 50 },
      { label: 'कपडा', val: 15 },
      { label: 'स्वास्थ्य', val: 15 },
      { label: 'शिक्षा', val: 20 },
      { label: 'घरभाडा', val: 30 },
      { label: 'अन्य', val: 15 }
    ]
  },
  animals: {
    title: 'पशु फार्ममा भएका पशुहरूको सङ्ख्या सम्बन्धी स्तम्भ चित्र',
    xAxisLabel: 'पशुका नाम',
    yAxisLabel: 'पशु सङ्ख्या',
    scaleText: 'Y-अक्ष: १ से.मि. = ५ वटा',
    data: [
      { label: 'गाई', val: 15 },
      { label: 'भैंसी', val: 10 },
      { label: 'भेडा', val: 35 },
      { label: 'बाख्रा', val: 40 },
      { label: 'सुँगुर', val: 25 }
    ]
  }
};

const barThemes = {
  indigo: ['#3b82f6', '#2563eb', '#1d4ed8', '#4f46e5', '#6366f1', '#818cf8'],
  emerald: ['#10b981', '#059669', '#047857', '#14b8a6', '#0d9488', '#2dd4bf'],
  amber: ['#f59e0b', '#d97706', '#b45309', '#f97316', '#ea580c', '#fbbf24'],
  multi: ['#f43f5e', '#f59e0b', '#10b981', '#06b6d4', '#6366f1', '#ec4899']
};

function loadBarPreset(key) {
  currentBarPreset = key;
  document.querySelectorAll('.bar-preset-btn').forEach(b => {
    b.className = 'bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600 transition';
  });
  const btn = document.getElementById('btn-bar-' + key);
  if (btn) btn.className = 'bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white transition';
  renderBarStudio();
}

function renderBarStudio() {
  const gGrid = document.getElementById('bar-grid-group');
  const gBars = document.getElementById('bar-elements-group');
  const gAxes = document.getElementById('bar-axes-group');
  const gLabels = document.getElementById('bar-labels-group');
  if (!gGrid || !gBars || !gAxes || !gLabels) return;

  gGrid.innerHTML = '';
  gBars.innerHTML = '';
  gAxes.innerHTML = '';
  gLabels.innerHTML = '';

  const ds = barDatasets[currentBarPreset] || barDatasets['absent'];
  const titleEl = document.getElementById('bar-chart-title');
  const scaleEl = document.getElementById('bar-scale-text');
  if (titleEl) titleEl.textContent = ds.title;
  if (scaleEl) scaleEl.textContent = ds.scaleText;

  const themeKey = (document.getElementById('ch20-bar-theme') || {}).value || 'indigo';
  const colors = barThemes[themeKey] || barThemes['indigo'];

  // Dimensions
  const svgW = 540, svgH = 340;
  const padLeft = 65, padBottom = 60, padTop = 35, padRight = 30;
  const plotW = svgW - padLeft - padRight;
  const plotH = svgH - padTop - padBottom;

  const values = ds.data.map(d => d.val);
  const maxVal = Math.max(...values);
  const minVal = Math.min(...values);
  const sumVal = values.reduce((a, b) => a + b, 0);
  const avgVal = (sumVal / values.length).toFixed(2);

  // Update metrics cards
  const mMax = document.getElementById('bar-metric-max');
  const mMin = document.getElementById('bar-metric-min');
  const mSum = document.getElementById('bar-metric-sum');
  const mAvg = document.getElementById('bar-metric-avg');
  const mCount = document.getElementById('bar-items-count');
  if (mMax) mMax.textContent = maxVal;
  if (mMin) mMin.textContent = minVal;
  if (mSum) mSum.textContent = sumVal;
  if (mAvg) mAvg.textContent = avgVal;
  if (mCount) mCount.textContent = `${values.length} वटा स्तम्भ`;

  // Scale Y
  let yAxisMax = Math.ceil(maxVal * 1.15 / 5) * 5;
  if (yAxisMax < 10) yAxisMax = 10;
  const numGridLines = 5;

  // Draw Grid Lines & Y ticks
  let gridHtml = '';
  for (let i = 0; i <= numGridLines; i++) {
    let tickVal = Math.round((yAxisMax / numGridLines) * i);
    let y = padTop + plotH - (tickVal / yAxisMax) * plotH;
    gridHtml += `<line x1="${padLeft}" y1="${y}" x2="${padLeft + plotW}" y2="${y}" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>`;
    gridHtml += `<text x="${padLeft - 8}" y="${y + 4}" fill="#94a3b8" font-size="11" text-anchor="end" font-family="monospace">${tickVal}</text>`;
  }
  gGrid.innerHTML = gridHtml;

  // Axes lines
  const originX = padLeft, originY = padTop + plotH;
  let axesHtml = `
    <!-- X-Axis -->
    <line x1="${originX}" y1="${originY}" x2="${originX + plotW + 15}" y2="${originY}" stroke="#e2e8f0" stroke-width="2.5"/>
    <polygon points="${originX + plotW + 18},${originY} ${originX + plotW + 10},${originY - 4} ${originX + plotW + 10},${originY + 4}" fill="#e2e8f0"/>
    <text x="${originX + plotW + 22}" y="${originY + 4}" fill="#38bdf8" font-size="12" font-weight="black">X</text>

    <!-- Y-Axis -->
    <line x1="${originX}" y1="${originY}" x2="${originX}" y2="${padTop - 15}" stroke="#e2e8f0" stroke-width="2.5"/>
    <polygon points="${originX},${padTop - 18} ${originX - 4},${padTop - 10} ${originX + 4},${padTop - 10}" fill="#e2e8f0"/>
    <text x="${originX}" y="${padTop - 22}" fill="#38bdf8" font-size="12" font-weight="black" text-anchor="middle">Y</text>
    <text x="${originX - 10}" y="${originY + 18}" fill="#94a3b8" font-size="11" font-weight="bold">O</text>
  `;
  gAxes.innerHTML = axesHtml;

  // Draw Bars & Labels
  const n = ds.data.length;
  const slotW = plotW / n;
  const barW = Math.min(slotW * 0.58, 48); // Equal width rule!
  let barsHtml = '';
  let labelsHtml = '';

  ds.data.forEach((item, idx) => {
    const cx = originX + idx * slotW + slotW / 2;
    const x = cx - barW / 2;
    const bHeight = (item.val / yAxisMax) * plotH;
    const y = originY - bHeight;
    const barCol = colors[idx % colors.length];

    barsHtml += `
      <rect x="${x}" y="${y}" width="${barW}" height="${bHeight}" fill="${barCol}" rx="5" stroke="rgba(255,255,255,0.2)" stroke-width="1.5">
        <title>${item.label}: ${item.val}</title>
      </rect>
    `;

    // Top value on bar
    labelsHtml += `<text x="${cx}" y="${y - 6}" fill="#f8fafc" font-size="11" font-weight="black" text-anchor="middle">${item.val}</text>`;

    // X-Axis category label below bar
    labelsHtml += `<text x="${cx}" y="${originY + 18}" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">${item.label}</text>`;
  });

  gBars.innerHTML = barsHtml;
  gLabels.innerHTML = labelsHtml;
}

// ================= MODE 2: TALLY MARKS & FREQUENCY GENERATOR =================
let currentTallyPreset = 'scores';
let tallyFreqMap = {}; // item -> count

const tallyPresets = {
  scores: {
    title: 'कक्षा ६ का ३० जना विद्यार्थीहरूको २० पूर्णाङ्कको गणित प्राप्ताङ्क',
    items: [
      2, 14, 9, 6, 13, 7, 8, 11, 12, 9,
      5, 4, 15, 19, 20, 17, 16, 13, 20, 19,
      15, 9, 15, 12, 17, 13, 18, 19, 16, 15
    ]
  },
  heights: {
    title: 'कक्षा १० का ३२ जना विद्यार्थीहरूको उचाइ (से.मि. मा)',
    items: [
      123, 122, 121, 120, 124, 120, 122, 121, 120, 123, 120, 122,
      124, 123, 121, 124, 120, 124, 122, 121, 123, 122, 123, 123,
      122, 121, 120, 124, 120, 121, 123, 122
    ]
  },
  transport: {
    title: 'विद्यालय आउने यातायातका साधनहरू (४० जना)',
    items: [
      'बस', 'साइकल', 'साइकल', 'ट्याक्सी', 'मोटरसाइकल', 'पैदल', 'बस',
      'पैदल', 'ट्याक्सी', 'पैदल', 'बस', 'पैदल', 'ट्याक्सी', 'पैदल',
      'पैदल', 'साइकल', 'मोटरसाइकल', 'पैदल', 'साइकल', 'साइकल', 'ट्याक्सी',
      'ट्याक्सी', 'बस', 'साइकल', 'बस', 'ट्याक्सी', 'पैदल', 'पैदल',
      'बस', 'मोटरसाइकल', 'पैदल', 'बस', 'मोटरसाइकल', 'मोटरसाइकल', 'बस',
      'पैदल', 'ट्याक्सी', 'बस', 'साइकल', 'पैदल'
    ]
  },
  dice: {
    title: 'पासा (Dice) २५ पटक फ्याँक्दा प्राप्त सङ्ख्याहरू',
    items: [
      3, 5, 2, 6, 1, 4, 3, 2, 6, 5,
      1, 4, 3, 6, 2, 5, 4, 1, 6, 3,
      2, 5, 6, 4, 3
    ]
  }
};

function initTallyLab() {
  loadTallyPreset('scores');
}

function loadTallyPreset(key) {
  currentTallyPreset = key;
  const ds = tallyPresets[key] || tallyPresets['scores'];
  tallyFreqMap = {};
  ds.items.forEach(val => {
    tallyFreqMap[val] = (tallyFreqMap[val] || 0) + 1;
  });

  const tEl = document.getElementById('tally-dataset-title');
  if (tEl) tEl.textContent = ds.title;
  renderTallyTableDom();
}

function addTallyItem() {
  const input = document.getElementById('tally-custom-item');
  if (!input) return;
  const val = input.value.trim();
  if (!val) return;
  tallyFreqMap[val] = (tallyFreqMap[val] || 0) + 1;
  input.value = '';
  renderTallyTableDom();
}

function renderTallyMarkString(count) {
  const fullBundles = Math.floor(count / 5);
  const remainder = count % 5;
  let str = '';
  for (let i = 0; i < fullBundles; i++) {
    str += '<span class="text-emerald-400 font-mono font-bold mr-2"><s>||||</s></span>';
  }
  if (remainder > 0) {
    str += `<span class="text-blue-400 font-mono font-bold">${'|'.repeat(remainder)}</span>`;
  }
  return str || '<span class="text-slate-500 font-mono">-</span>';
}

function renderTallyTableDom() {
  const tbody = document.getElementById('tally-table-body');
  const countBadge = document.getElementById('tally-total-count');
  if (!tbody) return;
  tbody.innerHTML = '';

  let keys = Object.keys(tallyFreqMap);
  // Sort numerically if all keys are numbers, else alphabetically
  const isAllNumeric = keys.every(k => !isNaN(k));
  if (isAllNumeric) {
    keys.sort((a, b) => Number(a) - Number(b));
  } else {
    keys.sort();
  }

  let totalN = 0;
  keys.forEach((key, idx) => {
    const count = tallyFreqMap[key];
    totalN += count;
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-slate-900 transition';
    tr.innerHTML = `
      <td class="p-3 text-center text-slate-500 font-mono">${idx + 1}</td>
      <td class="p-3 font-bold text-slate-200">${key}</td>
      <td class="p-3">${renderTallyMarkString(count)}</td>
      <td class="p-3 text-center font-black text-cyan-300 text-sm">${count}</td>
    `;
    tbody.appendChild(tr);
  });

  if (countBadge) {
    countBadge.textContent = `कुल सङ्ख्या N = ${totalN}`;
  }
}

// ================= MODE 3: BAR CHART READER LAB =================
const readerQuestions = [
  {
    q: 'कुन कक्षामा सबैभन्दा धेरै विद्यार्थीहरू अध्ययनरत छन्?',
    options: ['कक्षा ६', 'कक्षा ७', 'कक्षा ८ (१०० जना)', 'कक्षा १२'],
    correct: 2,
    explanation: 'कक्षा ८ को स्तम्भ १०० जना (सबैभन्दा अग्लो) छ।'
  },
  {
    q: 'सबैभन्दा थोरै विद्यार्थी भएको कक्षा कुन हो र कति जना छन्?',
    options: ['कक्षा १० (७० जना)', 'कक्षा ११ (७५ जना)', 'कक्षा ६ (८० जना)', 'कक्षा ७ (८५ जना)'],
    correct: 0,
    explanation: 'कक्षा १० को स्तम्भ ७० जनामा सीमित छ (सबैभन्दा होचो)।'
  },
  {
    q: 'कक्षा ६ देखि १२ सम्मका कुल विद्यार्थी सङ्ख्या कति हो?',
    options: ['५०० जना', '५९० जना', '६०० जना', '५५० जना'],
    correct: 1,
    explanation: '८० + ८५ + १०० + ९० + ७० + ७५ + ९० = ५९० जना।'
  },
  {
    q: 'कक्षा ८ र कक्षा १० का विद्यार्थी सङ्ख्या बीचको अन्तर (Difference) कति छ?',
    options: ['२० जना', '३० जना', '२५ जना', '१५ जना'],
    correct: 1,
    explanation: 'कक्षा ८ (१००) - कक्षा १० (७०) = ३० जना।'
  },
  {
    q: 'कुन दुई कक्षाहरूमा बराबर ९०-९० जना विद्यार्थी छन्?',
    options: ['कक्षा ६ र ७', 'कक्षा ९ र १२', 'कक्षा ७ र ११', 'कक्षा ८ र ९'],
    correct: 1,
    explanation: 'कक्षा ९ र कक्षा १२ दुवैमा ९०-९० जना विद्यार्थी छन्।'
  }
];

let readerCurrentQIndex = 0;
let readerUserScore = 0;
let readerAnswered = false;

function initReaderLab() {
  readerCurrentQIndex = 0;
  readerUserScore = 0;
  readerAnswered = false;
  renderReaderSvg();
  renderReaderQuestion();
}

function renderReaderSvg() {
  const g = document.getElementById('reader-svg-elements');
  if (!g) return;

  const data = [
    { label: '६', val: 80, col: '#f59e0b' },
    { label: '७', val: 85, col: '#10b981' },
    { label: '८', val: 100, col: '#38bdf8' },
    { label: '९', val: 90, col: '#6366f1' },
    { label: '१०', val: 70, col: '#ec4899' },
    { label: '११', val: 75, col: '#84cc16' },
    { label: '१२', val: 90, col: '#14b8a6' }
  ];

  const padLeft = 45, padBottom = 45, padTop = 25, padRight = 20;
  const w = 460 - padLeft - padRight;
  const h = 300 - padTop - padBottom;
  const originX = padLeft, originY = padTop + h;
  const yMax = 120;

  let html = `
    <!-- Axes -->
    <line x1="${originX}" y1="${originY}" x2="${originX + w + 10}" y2="${originY}" stroke="#94a3b8" stroke-width="2"/>
    <line x1="${originX}" y1="${originY}" x2="${originX}" y2="${padTop - 10}" stroke="#94a3b8" stroke-width="2"/>
    <text x="${originX + w + 12}" y="${originY + 4}" fill="#38bdf8" font-size="11" font-weight="bold">X</text>
    <text x="${originX}" y="${padTop - 14}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Y</text>
  `;

  // Grid lines
  for (let val = 20; val <= 100; val += 20) {
    let y = originY - (val / yMax) * h;
    html += `
      <line x1="${originX}" y1="${y}" x2="${originX + w}" y2="${y}" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
      <text x="${originX - 6}" y="${y + 4}" fill="#64748b" font-size="10" text-anchor="end" font-family="monospace">${val}</text>
    `;
  }

  // Bars
  const slotW = w / data.length;
  const barW = slotW * 0.65;
  data.forEach((d, i) => {
    let cx = originX + i * slotW + slotW / 2;
    let bx = cx - barW / 2;
    let bH = (d.val / yMax) * h;
    let by = originY - bH;

    html += `
      <rect x="${bx}" y="${by}" width="${barW}" height="${bH}" fill="${d.col}" rx="4" opacity="0.9"/>
      <text x="${cx}" y="${by - 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">${d.val}</text>
      <text x="${cx}" y="${originY + 16}" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">कक्षा ${d.label}</text>
    `;
  });

  g.innerHTML = html;
}

function renderReaderQuestion() {
  const qObj = readerQuestions[readerCurrentQIndex];
  if (!qObj) return;

  readerAnswered = false;
  const qNum = document.getElementById('reader-q-num');
  const qText = document.getElementById('reader-q-text');
  const optContainer = document.getElementById('reader-options-container');
  const fb = document.getElementById('reader-feedback');
  const scoreBadge = document.getElementById('reader-score-badge');

  if (qNum) qNum.textContent = `प्रश्न ${readerCurrentQIndex + 1} / ${readerQuestions.length}`;
  if (qText) qText.textContent = qObj.q;
  if (scoreBadge) scoreBadge.textContent = `अङ्क: ${readerUserScore} / ${readerQuestions.length}`;
  if (fb) {
    fb.textContent = 'विकल्प छानेर आफ्नो उत्तर परीक्षण गर्नुहोस्!';
    fb.className = 'p-3 rounded-xl bg-slate-900/80 border border-slate-800 text-xs font-semibold text-slate-400 min-h-[36px]';
  }

  if (optContainer) {
    optContainer.innerHTML = '';
    qObj.options.forEach((opt, idx) => {
      const btn = document.createElement('button');
      btn.className = 'w-full text-left p-2.5 rounded-xl border border-slate-700 bg-slate-900/60 hover:bg-slate-800 text-slate-200 text-xs font-semibold transition cursor-pointer flex justify-between items-center';
      btn.innerHTML = `<span>${String.fromCharCode(65 + idx)}. ${opt}</span>`;
      btn.onclick = () => handleReaderAnswer(idx);
      optContainer.appendChild(btn);
    });
  }
}

function handleReaderAnswer(selectedIdx) {
  if (readerAnswered) return;
  readerAnswered = true;
  const qObj = readerQuestions[readerCurrentQIndex];
  const fb = document.getElementById('reader-feedback');
  const optContainer = document.getElementById('reader-options-container');
  const scoreBadge = document.getElementById('reader-score-badge');

  const btns = optContainer.querySelectorAll('button');
  btns.forEach((b, idx) => {
    b.disabled = true;
    if (idx === qObj.correct) {
      b.className = 'w-full text-left p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/60 text-emerald-200 text-xs font-bold flex justify-between items-center';
      b.innerHTML += '<span class="text-emerald-400">✓ सही</span>';
    } else if (idx === selectedIdx) {
      b.className = 'w-full text-left p-2.5 rounded-xl border border-rose-500 bg-rose-950/60 text-rose-200 text-xs font-bold flex justify-between items-center';
      b.innerHTML += '<span class="text-rose-400">✗ गलत</span>';
    } else {
      b.className += ' opacity-50';
    }
  });

  if (selectedIdx === qObj.correct) {
    readerUserScore++;
    if (scoreBadge) scoreBadge.textContent = `अङ्क: ${readerUserScore} / ${readerQuestions.length}`;
    if (fb) {
      fb.innerHTML = `<span class="text-emerald-400 font-bold">🎉 सही उत्तर!</span> <span class="text-slate-300">${qObj.explanation}</span>`;
      fb.className = 'p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/60 text-xs';
    }
  } else {
    if (fb) {
      fb.innerHTML = `<span class="text-rose-400 font-bold">⚠️ गलत उत्तर!</span> <span class="text-slate-300">${qObj.explanation}</span>`;
      fb.className = 'p-3 rounded-xl bg-rose-950/40 border border-rose-800/60 text-xs';
    }
  }
}

function nextReaderQuestion() {
  readerCurrentQIndex = (readerCurrentQIndex + 1) % readerQuestions.length;
  renderReaderQuestion();
}

// ================= 4. SELF-ASSESSMENT QUIZ ENGINE =================
const ch20QuizQuestions = [
  {
    id: 'q1',
    question: 'कुनै तथ्याङ्कमा कुनै मान दोहोरिने सङ्ख्यालाई के भनिन्छ?',
    options: ['परास (Range)', 'बारम्बारता (Frequency)', 'मध्यक (Mean)', 'कोरा तथ्याङ्क'],
    correct: 1,
    explanation: 'कुनै विशेष मान तथ्याङ्कमा कति पटक दोहोरिएको छ, त्यो सङ्ख्या नै उक्त मानको बारम्बारता (Frequency) हो।'
  },
  {
    id: 'q2',
    question: 'मिलान चिह्न (Tally marks) मा ५ को मान देखाउन कस्तो सङ्केत कोरिन्छ?',
    options: ['५ वटा ठाडो धर्सा', '४ वटा ठाडो र १ वटा छड्के धर्सा (<s>||||</s>)', '३ वटा ठाडो र २ छड्के', '१ वटा तेर्सो धर्सा'],
    correct: 1,
    explanation: 'चारवटा ठाडो धर्सा तानेपछि पाँचौँ गणनाले छड्के काटेर ५ को बण्डल बनाइन्छ।'
  },
  {
    id: 'q3',
    question: 'साधारण स्तम्भ चित्र बनाउँदा तेर्सो X-अक्षमा सामान्यतया के राखिन्छ?',
    options: ['बारम्बारता वा सङ्ख्या', 'अध्ययन गरिने विषय वा शीर्षकहरू', 'स्केल (Scale)', 'कुल योगफल'],
    correct: 1,
    explanation: 'तेर्सो X-अक्षमा अध्ययन गरिने चर/शीर्षक (जस्तै दिन, विषय, कक्षा) राखिन्छ र ठाडो Y-अक्षमा बारम्बारता राखिन्छ।'
  },
  {
    id: 'q4',
    question: 'साधारण स्तम्भ चित्रमा सबै स्तम्भहरूको के अनिवार्य रूपमा बराबर हुनुपर्छ?',
    options: ['स्तम्भको उचाइ', 'स्तम्भको चौडाइ', 'स्तम्भको रङ', 'स्तम्भको क्षेत्रफल'],
    correct: 1,
    explanation: 'स्तम्भको मान उचाइले मात्र जनाउने हुनाले तुलनामा भ्रम नहोस् भन्न सबै स्तम्भको चौडाइ ठ्याक्कै बराबर हुनुपर्छ।'
  },
  {
    id: 'q5',
    question: 'स्तम्भ चित्रमा दुईवटा स्तम्भहरू बिचको दूरी कस्तो हुनुपर्दछ?',
    options: ['असमान हुनुपर्छ', 'जति राखे पनि हुन्छ', 'सधैँ समान हुनुपर्छ', 'शून्य (खप्टिएको) हुनुपर्छ'],
    correct: 2,
    explanation: 'साधारण स्तम्भ चित्रमा कुनै पनि दुई स्तम्भहरूको बिचको खाली दूरी सधैँ समान हुनुपर्छ।'
  },
  {
    id: 'q6',
    question: 'यदि Y-अक्षमा १ से.मि. = ५ जना मानिएको छ र एउटा स्तम्भको उचाइ ६ से.मि. छ भने सो स्तम्भले कति विद्यार्थी जनाउँछ?',
    options: ['११ जना', '३० जना', '२५ जना', '३६ जना'],
    correct: 1,
    explanation: 'मान = उचाइ × स्केल = ६ × ५ = ३० जना।'
  },
  {
    id: 'q7',
    question: '३० जना विद्यार्थीको परीक्षामा १५ अङ्क पाउने ४ जना छन् भने १५ अङ्कको बारम्बारता कति हुन्छ?',
    options: ['१५', '३०', '४', '२'],
    correct: 2,
    explanation: '१५ अङ्क पाउने विद्यार्थी ४ जना भएकाले यसको बारम्बारता ४ हुन्छ।'
  },
  {
    id: 'q8',
    question: 'सुरुवाती अवस्थामा सङ्कलन गरिएको तर कुनै तालिका वा समूहमा नराखिएको तथ्याङ्कलाई के भनिन्छ?',
    options: ['माध्यमिक तथ्याङ्क', 'कोरा तथ्याङ्क (Raw Data)', 'बारम्बारता', 'स्तम्भ'],
    correct: 1,
    explanation: 'सुरुमा सङ्कलन गरिएको अव्यवस्थित सुरुवाती तथ्याङ्कलाई कोरा तथ्याङ्क भनिन्छ।'
  },
  {
    id: 'q9',
    question: 'परिवारको कुल खर्च १ लाख ४० हजारमा खानामा ५० हजार खर्च हुन्छ भने खानामा भएको खर्च प्रतिशत कति हो?',
    options: ['२५%', '५०%', '३५.७१%', '४०%'],
    correct: 2,
    explanation: '(५० / १४०) × १००% = ३५.७१%।'
  },
  {
    id: 'q10',
    question: 'अनुसन्धानकर्ता आफैँले स्थलगत रूपमा प्रत्यक्ष सोधपुछ वा अवलोकन गरी सङ्कलन गरेको तथ्याङ्कलाई के भनिन्छ?',
    options: ['प्राथमिक तथ्याङ्क (Primary Data)', 'द्वितीयक तथ्याङ्क', 'अनुमानित तथ्याङ्क', 'समूहकृत तथ्याङ्क'],
    correct: 0,
    explanation: 'आफैँले प्रत्यक्ष सङ्कलन गरेको मौलिक तथ्याङ्क प्राथमिक तथ्याङ्क हो।'
  }
];

let ch20UserAnswers = {};

function renderCh20Quiz() {
  const container = document.getElementById('ch20-quiz-container');
  if (!container) return;
  container.innerHTML = '';

  ch20QuizQuestions.forEach((q, idx) => {
    const answered = ch20UserAnswers.hasOwnProperty(q.id);
    const selectedOpt = ch20UserAnswers[q.id];

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
        <button onclick="handleCh20QuizAnswer('${q.id}', ${oIdx})" ${answered ? 'disabled' : ''} class="${optClass}">
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
        <span class="text-xs font-bold text-blue-600">प्रश्न ${idx + 1} / ${ch20QuizQuestions.length}</span>
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

function handleCh20QuizAnswer(qId, optIdx) {
  if (ch20UserAnswers.hasOwnProperty(qId)) return;
  ch20UserAnswers[qId] = optIdx;

  let score = 0;
  ch20QuizQuestions.forEach(q => {
    if (ch20UserAnswers[q.id] === q.correct) {
      score++;
    }
  });

  const scoreEl = document.getElementById('ch20-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `${score} / ${ch20QuizQuestions.length}`;
  }

  renderCh20Quiz();
}

function resetCh20Quiz() {
  ch20UserAnswers = {};
  const scoreEl = document.getElementById('ch20-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `० / ${ch20QuizQuestions.length}`;
  }
  renderCh20Quiz();
}

// Expose to window for global access
window.setTabCh20 = setTabCh20;
window.filterCh20Exercises = filterCh20Exercises;
window.switchCh20Lab = switchCh20Lab;
window.loadBarPreset = loadBarPreset;
window.renderBarStudio = renderBarStudio;
window.initTallyLab = initTallyLab;
window.loadTallyPreset = loadTallyPreset;
window.addTallyItem = addTallyItem;
window.renderTallyTableDom = renderTallyTableDom;
window.initReaderLab = initReaderLab;
window.renderReaderSvg = renderReaderSvg;
window.renderReaderQuestion = renderReaderQuestion;
window.handleReaderAnswer = handleReaderAnswer;
window.nextReaderQuestion = nextReaderQuestion;
window.renderCh20Quiz = renderCh20Quiz;
window.handleCh20QuizAnswer = handleCh20QuizAnswer;
window.resetCh20Quiz = resetCh20Quiz;
'''

with open('scratch/ch20_script.js', 'w', encoding='utf-8') as f:
    f.write(script_code.strip() + '\n')

print("scratch/ch20_script.js created successfully!")
