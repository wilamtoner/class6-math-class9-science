
// ==================== CHAPTER 15 INTERACTIVE ENGINE ====================

// --- Tab Switcher ---
function setTabCh15(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById('ch15-tab-' + t);
    const view = document.getElementById('ch15-view-' + t);
    if (btn && view) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
        view.classList.remove('hidden');
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
        view.classList.add('hidden');
      }
    }
  });

  if (tab === 'quiz') {
    renderCh15Quiz();
  }

  // Render MathJax / KaTeX if available
  try {
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('chapter-view-15'), {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  } catch (e) {}
}

// --- Lab Mode Switcher ---
function switchCh15Lab(mode) {
  const triLab = document.getElementById('ch15-sublab-triangle');
  const quadLab = document.getElementById('ch15-sublab-quad');
  const btnTri = document.getElementById('btn-lab-triangle');
  const btnQuad = document.getElementById('btn-lab-quad');

  if (mode === 'triangle') {
    if (triLab) triLab.classList.remove('hidden');
    if (quadLab) quadLab.classList.add('hidden');
    if (btnTri) btnTri.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-sm transition cursor-pointer';
    if (btnQuad) btnQuad.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
  } else {
    if (triLab) triLab.classList.add('hidden');
    if (quadLab) quadLab.classList.remove('hidden');
    if (btnQuad) btnQuad.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-purple-600 text-white shadow-sm transition cursor-pointer';
    if (btnTri) btnTri.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
  }
}

// --- DYNAMIC TRIANGLE LAB ---
const triState = {
  Ax: 200,
  Ay: 60,
  Bx: 80,
  By: 240,
  Cx: 320,
  Cy: 240
};

function updateTriangleLab() {
  const poly = document.getElementById('tri-polygon');
  const nodeA = document.getElementById('node-A');
  const textA = document.getElementById('text-A');
  const labelA = document.getElementById('label-side-a');
  const labelB = document.getElementById('label-side-b');
  const labelC = document.getElementById('label-side-c');

  if (!poly || !nodeA) return;

  const Ax = triState.Ax;
  const Ay = triState.Ay;
  const Bx = triState.Bx;
  const By = triState.By;
  const Cx = triState.Cx;
  const Cy = triState.Cy;

  // Update polygon & node
  poly.setAttribute('points', `${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}`);
  nodeA.setAttribute('cx', Ax);
  nodeA.setAttribute('cy', Ay);
  textA.setAttribute('x', Ax);
  textA.setAttribute('y', Ay - 12);

  // Side lengths (Euclidean distance, scaled: 10px = 1 cm)
  const a = Math.hypot(Cx - Bx, Cy - By) / 10;
  const b = Math.hypot(Ax - Cx, Ay - Cy) / 10;
  const c = Math.hypot(Ax - Bx, Ay - By) / 10;

  // Labels position at midpoints
  if (labelC) {
    labelC.setAttribute('x', (Ax + Bx) / 2 - 15);
    labelC.setAttribute('y', (Ay + By) / 2);
    labelC.textContent = `c=${c.toFixed(1)}`;
  }
  if (labelB) {
    labelB.setAttribute('x', (Ax + Cx) / 2 + 15);
    labelB.setAttribute('y', (Ay + Cy) / 2);
    labelB.textContent = `b=${b.toFixed(1)}`;
  }
  if (labelA) {
    labelA.setAttribute('x', (Bx + Cx) / 2);
    labelA.setAttribute('y', By + 22);
    labelA.textContent = `a=${a.toFixed(1)}`;
  }

  // Calculate angles via Law of Cosines
  // cos A = (b^2 + c^2 - a^2) / (2bc)
  function getAngleDeg(opp, adj1, adj2) {
    const cosVal = Math.max(-1, Math.min(1, (adj1 * adj1 + adj2 * adj2 - opp * opp) / (2 * adj1 * adj2)));
    return (Math.acos(cosVal) * 180) / Math.PI;
  }

  const angA = getAngleDeg(a, b, c);
  const angB = getAngleDeg(b, a, c);
  const angC = Math.max(0, 180 - (angA + angB));

  // Display angles in UI
  const elA = document.getElementById('val-ang-A');
  const elB = document.getElementById('val-ang-B');
  const elC = document.getElementById('val-ang-C');
  const elSum = document.getElementById('val-ang-sum');
  if (elA) elA.textContent = `${Math.round(angA)}°`;
  if (elB) elB.textContent = `${Math.round(angB)}°`;
  if (elC) elC.textContent = `${Math.round(angC)}°`;
  if (elSum) elSum.textContent = `180°`;

  // Draw angle arcs
  drawAngleArc('arc-A', Ax, Ay, Bx, By, Cx, Cy, 25);
  drawAngleArc('arc-B', Bx, By, Cx, Cy, Ax, Ay, 25);
  drawAngleArc('arc-C', Cx, Cy, Ax, Ay, Bx, By, 25);

  // Statistics & Classification
  const elStatA = document.getElementById('stat-side-a');
  const elStatB = document.getElementById('stat-side-b');
  const elStatC = document.getElementById('stat-side-c');
  const elSideType = document.getElementById('stat-side-type');
  const elAngType = document.getElementById('stat-angle-type');
  const elBadge = document.getElementById('tri-type-badge');

  if (elStatA) elStatA.textContent = `${a.toFixed(1)} cm`;
  if (elStatB) elStatB.textContent = `${b.toFixed(1)} cm`;
  if (elStatC) elStatC.textContent = `${c.toFixed(1)} cm`;

  // Side classification
  let sideType = 'विषमबाहु (Scalene)';
  const diffAB = Math.abs(c - b);
  const diffBC = Math.abs(a - b);
  const diffCA = Math.abs(a - c);
  if (diffAB < 0.6 && diffBC < 0.6 && diffCA < 0.6) {
    sideType = 'समबाहु (Equilateral)';
  } else if (diffAB < 0.6 || diffBC < 0.6 || diffCA < 0.6) {
    sideType = 'समद्विबाहु (Isosceles)';
  }
  if (elSideType) elSideType.textContent = sideType;

  // Angle classification
  let angType = 'न्यूनकोणी त्रिभुज (Acute)';
  const maxAng = Math.max(angA, angB, angC);
  if (Math.abs(maxAng - 90) <= 2) {
    angType = 'समकोणी त्रिभुज (Right-angled)';
  } else if (maxAng > 92) {
    angType = 'अधिककोणी त्रिभुज (Obtuse-angled)';
  }
  if (elAngType) elAngType.textContent = angType;
  if (elBadge) elBadge.textContent = `${sideType} | ${angType}`;
}

function drawAngleArc(arcId, vx, vy, p1x, p1y, p2x, p2y, r) {
  const arc = document.getElementById(arcId);
  if (!arc) return;
  const a1 = Math.atan2(p1y - vy, p1x - vx);
  const a2 = Math.atan2(p2y - vy, p2x - vx);
  let start = a1;
  let end = a2;
  let diff = end - start;
  while (diff < 0) diff += 2 * Math.PI;
  while (diff > 2 * Math.PI) diff -= 2 * Math.PI;
  if (diff > Math.PI) {
    start = a2;
    end = a1;
    diff = 2 * Math.PI - diff;
  }
  const x1 = vx + r * Math.cos(start);
  const y1 = vy + r * Math.sin(start);
  const x2 = vx + r * Math.cos(end);
  const y2 = vy + r * Math.sin(end);
  const largeArc = diff > Math.PI ? 1 : 0;
  arc.setAttribute('d', `M ${vx} ${vy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`);
}

function onTriSliderChange() {
  const sx = document.getElementById('slider-tri-x');
  const sy = document.getElementById('slider-tri-y');
  const lx = document.getElementById('slider-x-val');
  const ly = document.getElementById('slider-y-val');
  if (sx && sy) {
    triState.Ax = parseInt(sx.value);
    triState.Ay = parseInt(sy.value);
    if (lx) lx.textContent = `${triState.Ax} px`;
    if (ly) ly.textContent = `${triState.Ay} px`;
    updateTriangleLab();
  }
}

function setTriPreset(preset) {
  const sx = document.getElementById('slider-tri-x');
  const sy = document.getElementById('slider-tri-y');
  const lx = document.getElementById('slider-x-val');
  const ly = document.getElementById('slider-y-val');

  if (preset === 'equilateral') {
    // Equilateral: base 240, height = 240 * sqrt(3)/2 = 207.8 -> y = 240 - 208 = 32
    triState.Ax = 200;
    triState.Ay = 32;
  } else if (preset === 'isosceles') {
    triState.Ax = 200;
    triState.Ay = 90;
  } else if (preset === 'right') {
    triState.Ax = 80;
    triState.Ay = 60;
  } else if (preset === 'obtuse') {
    triState.Ax = 280;
    triState.Ay = 175;
  } else if (preset === 'acute_scalene') {
    triState.Ax = 160;
    triState.Ay = 60;
  }

  if (sx) sx.value = triState.Ax;
  if (sy) sy.value = triState.Ay;
  if (lx) lx.textContent = `${triState.Ax} px`;
  if (ly) ly.textContent = `${triState.Ay} px`;
  updateTriangleLab();
}

// --- DYNAMIC QUADRILATERAL LAB ---
const quadConfigs = {
  rectangle: {
    title: 'आयतका प्रमाणित ज्यामितीय गुणहरू',
    badge: 'आयत (Rectangle)',
    points: '80,80 320,80 320,220 80,220',
    diag1: { x1: 80, y1: 80, x2: 320, y2: 220 },
    diag2: { x1: 320, y1: 80, x2: 80, y2: 220 },
    nodes: [
      { id: 'qnode-A', cx: 80, cy: 80 },
      { id: 'qnode-B', cx: 320, cy: 80 },
      { id: 'qnode-C', cx: 320, cy: 220 },
      { id: 'qnode-D', cx: 80, cy: 220 }
    ],
    labels: [
      { id: 'qtext-A', x: 65, y: 75 },
      { id: 'qtext-B', x: 335, y: 75 },
      { id: 'qtext-C', x: 335, y: 240 },
      { id: 'qtext-D', x: 65, y: 240 },
      { id: 'qlabel-AB', x: 200, y: 70, text: 'AB = 6 cm' },
      { id: 'qlabel-CD', x: 200, y: 240, text: 'CD = 6 cm' },
      { id: 'qlabel-AD', x: 50, y: 155, text: 'AD = 3.5 cm' },
      { id: 'qlabel-BC', x: 350, y: 155, text: 'BC = 3.5 cm' }
    ],
    angles: { A: '90°', B: '90°', C: '90°', D: '90°', sum: '360°' },
    squaresVisible: true,
    sqPaths: {
      A: 'M 80 100 L 100 100 L 100 80',
      B: 'M 300 80 L 300 100 L 320 100',
      C: 'M 320 200 L 300 200 L 300 220',
      D: 'M 100 220 L 100 200 L 80 200'
    },
    props: [
      '✓ सम्मुख भुजाहरू बराबर र समानान्तर (AB = CD, AD = BC)',
      '✓ चारवटै कोणहरू ९०° (समकोण) छन्',
      '✓ दुवै विकर्णहरू (AC = BD) लम्बाइमा बराबर छन्',
      '✓ विकर्णहरू परस्पर समद्विभाजित हुन्छन्'
    ]
  },
  square: {
    title: 'वर्गका प्रमाणित ज्यामितीय गुणहरू',
    badge: 'वर्ग (Square)',
    points: '120,70 280,70 280,230 120,230',
    diag1: { x1: 120, y1: 70, x2: 280, y2: 230 },
    diag2: { x1: 280, y1: 70, x2: 120, y2: 230 },
    nodes: [
      { id: 'qnode-A', cx: 120, cy: 70 },
      { id: 'qnode-B', cx: 280, cy: 70 },
      { id: 'qnode-C', cx: 280, cy: 230 },
      { id: 'qnode-D', cx: 120, cy: 230 }
    ],
    labels: [
      { id: 'qtext-A', x: 105, y: 65 },
      { id: 'qtext-B', x: 295, y: 65 },
      { id: 'qtext-C', x: 295, y: 245 },
      { id: 'qtext-D', x: 105, y: 245 },
      { id: 'qlabel-AB', x: 200, y: 60, text: 'AB = 4 cm' },
      { id: 'qlabel-CD', x: 200, y: 250, text: 'CD = 4 cm' },
      { id: 'qlabel-AD', x: 90, y: 155, text: 'AD = 4 cm' },
      { id: 'qlabel-BC', x: 310, y: 155, text: 'BC = 4 cm' }
    ],
    angles: { A: '90°', B: '90°', C: '90°', D: '90°', sum: '360°' },
    squaresVisible: true,
    sqPaths: {
      A: 'M 120 90 L 140 90 L 140 70',
      B: 'M 260 70 L 260 90 L 280 90',
      C: 'M 280 210 L 260 210 L 260 230',
      D: 'M 140 230 L 140 210 L 120 210'
    },
    props: [
      '✓ चारवटै भुजाहरू समान लम्बाइका छन् (AB = BC = CD = DA)',
      '✓ चारवटै कोणहरू ठीक ९०° का समकोण छन्',
      '✓ दुवै विकर्णहरू बराबर छन् (AC = BD)',
      '✓ विकर्णहरू परस्पर ९०° मा समद्विभाजित हुन्छन्'
    ]
  },
  parallelogram: {
    title: 'समानान्तर चतुर्भुजका प्रमाणित गुणहरू',
    badge: 'समानान्तर चतुर्भुज (Parallelogram)',
    points: '120,80 340,80 280,220 60,220',
    diag1: { x1: 120, y1: 80, x2: 280, y2: 220 },
    diag2: { x1: 340, y1: 80, x2: 60, y2: 220 },
    nodes: [
      { id: 'qnode-A', cx: 120, cy: 80 },
      { id: 'qnode-B', cx: 340, cy: 80 },
      { id: 'qnode-C', cx: 280, cy: 220 },
      { id: 'qnode-D', cx: 60, cy: 220 }
    ],
    labels: [
      { id: 'qtext-A', x: 110, y: 70 },
      { id: 'qtext-B', x: 355, y: 80 },
      { id: 'qtext-C', x: 295, y: 235 },
      { id: 'qtext-D', x: 45, y: 230 },
      { id: 'qlabel-AB', x: 230, y: 70, text: 'AB = 6 cm' },
      { id: 'qlabel-CD', x: 170, y: 240, text: 'CD = 6 cm' },
      { id: 'qlabel-AD', x: 70, y: 145, text: 'AD = 4 cm' },
      { id: 'qlabel-BC', x: 330, y: 155, text: 'BC = 4 cm' }
    ],
    angles: { A: '115°', B: '65°', C: '115°', D: '65°', sum: '360°' },
    squaresVisible: false,
    sqPaths: {},
    props: [
      '✓ सम्मुख भुजाहरू समानान्तर र बराबर छन् (AB ∥ CD, AD ∥ BC)',
      '✓ सम्मुख कोणहरू बराबर छन् (∠A = ∠C = 115°, ∠B = ∠D = 65°)',
      '✓ क्रमागत भित्री कोणहरूको योग १८०° हुन्छ (115° + 65° = 180°)',
      '✓ विकर्णहरूले एक-अर्कालाई समद्विभाजित गर्दछन्'
    ]
  },
  rhombus: {
    title: 'समबाहु चतुर्भुजका प्रमाणित गुणहरू',
    badge: 'समबाहु चतुर्भुज (Rhombus)',
    points: '200,60 310,150 200,240 90,150',
    diag1: { x1: 200, y1: 60, x2: 200, y2: 240 },
    diag2: { x1: 90, y1: 150, x2: 310, y2: 150 },
    nodes: [
      { id: 'qnode-A', cx: 200, cy: 60 },
      { id: 'qnode-B', cx: 310, cy: 150 },
      { id: 'qnode-C', cx: 200, cy: 240 },
      { id: 'qnode-D', cx: 90, cy: 150 }
    ],
    labels: [
      { id: 'qtext-A', x: 200, y: 48 },
      { id: 'qtext-B', x: 325, y: 155 },
      { id: 'qtext-C', x: 200, y: 258 },
      { id: 'qtext-D', x: 75, y: 155 },
      { id: 'qlabel-AB', x: 265, y: 100, text: 'AB = 4.5 cm' },
      { id: 'qlabel-CD', x: 135, y: 200, text: 'CD = 4.5 cm' },
      { id: 'qlabel-AD', x: 135, y: 100, text: 'AD = 4.5 cm' },
      { id: 'qlabel-BC', x: 265, y: 200, text: 'BC = 4.5 cm' }
    ],
    angles: { A: '78°', B: '102°', C: '78°', D: '102°', sum: '360°' },
    squaresVisible: false,
    sqPaths: {},
    props: [
      '✓ चारवटै भुजाहरू समान लम्बाइका छन् (AB = BC = CD = DA)',
      '✓ सम्मुख भुजाहरू समानान्तर छन् (AB ∥ CD, AD ∥ BC)',
      '✓ सम्मुख कोणहरू बराबर छन् (∠A = ∠C, ∠B = ∠D)',
      '✓ विकर्णहरू परस्पर ९०° मा लम्ब भई समद्विभाजित हुन्छन्'
    ]
  },
  trapezium: {
    title: 'समलम्ब चतुर्भुजका प्रमाणित गुणहरू',
    badge: 'समलम्ब चतुर्भुज (Trapezium)',
    points: '120,80 280,80 340,220 60,220',
    diag1: { x1: 120, y1: 80, x2: 340, y2: 220 },
    diag2: { x1: 280, y1: 80, x2: 60, y2: 220 },
    nodes: [
      { id: 'qnode-A', cx: 120, cy: 80 },
      { id: 'qnode-B', cx: 280, cy: 80 },
      { id: 'qnode-C', cx: 340, cy: 220 },
      { id: 'qnode-D', cx: 60, cy: 220 }
    ],
    labels: [
      { id: 'qtext-A', x: 110, y: 70 },
      { id: 'qtext-B', x: 290, y: 70 },
      { id: 'qtext-C', x: 355, y: 235 },
      { id: 'qtext-D', x: 45, y: 235 },
      { id: 'qlabel-AB', x: 200, y: 70, text: 'AB = 4 cm (∥)' },
      { id: 'qlabel-CD', x: 200, y: 240, text: 'DC = 7 cm (∥)' },
      { id: 'qlabel-AD', x: 75, y: 150, text: 'AD = 4.2 cm' },
      { id: 'qlabel-BC', x: 325, y: 150, text: 'BC = 4.2 cm' }
    ],
    angles: { A: '113°', B: '113°', C: '67°', D: '67°', sum: '360°' },
    squaresVisible: false,
    sqPaths: {},
    props: [
      '✓ केवल एक जोडा सम्मुख भुजाहरू मात्र समानान्तर छन् (AB ∥ DC)',
      '✓ असमानान्तर भुजाहरू (AD र BC) बराबर भए समद्विबाहु समलम्ब हुन्छ',
      '✓ समानान्तर भुजाबीचको लम्ब दूरी सधैँ स्थिर रहन्छ',
      '✓ चारवटै कोणहरूको कुल योग सधैँ ३६०° हुन्छ'
    ]
  }
};

function setQuadType(type) {
  const conf = quadConfigs[type];
  if (!conf) return;

  const poly = document.getElementById('quad-polygon');
  const d1 = document.getElementById('quad-diag-1');
  const d2 = document.getElementById('quad-diag-2');
  const title = document.getElementById('quad-prop-title');
  const badge = document.getElementById('quad-type-badge');
  const propList = document.getElementById('quad-prop-list');

  if (poly) poly.setAttribute('points', conf.points);
  if (d1) {
    d1.setAttribute('x1', conf.diag1.x1);
    d1.setAttribute('y1', conf.diag1.y1);
    d1.setAttribute('x2', conf.diag1.x2);
    d1.setAttribute('y2', conf.diag1.y2);
  }
  if (d2) {
    d2.setAttribute('x1', conf.diag2.x1);
    d2.setAttribute('y1', conf.diag2.y1);
    d2.setAttribute('x2', conf.diag2.x2);
    d2.setAttribute('y2', conf.diag2.y2);
  }

  conf.nodes.forEach(n => {
    const el = document.getElementById(n.id);
    if (el) {
      el.setAttribute('cx', n.cx);
      el.setAttribute('cy', n.cy);
    }
  });

  conf.labels.forEach(l => {
    const el = document.getElementById(l.id);
    if (el) {
      el.setAttribute('x', l.x);
      el.setAttribute('y', l.y);
      if (l.text) el.textContent = l.text;
    }
  });

  // Angles readout
  const qA = document.getElementById('qval-ang-A');
  const qB = document.getElementById('qval-ang-B');
  const qC = document.getElementById('qval-ang-C');
  const qD = document.getElementById('qval-ang-D');
  const qSum = document.getElementById('qval-ang-sum');
  if (qA) qA.textContent = conf.angles.A;
  if (qB) qB.textContent = conf.angles.B;
  if (qC) qC.textContent = conf.angles.C;
  if (qD) qD.textContent = conf.angles.D;
  if (qSum) qSum.textContent = conf.angles.sum;

  // Right angle markers
  const sqA = document.getElementById('quad-sq-A');
  const sqB = document.getElementById('quad-sq-B');
  const sqC = document.getElementById('quad-sq-C');
  const sqD = document.getElementById('quad-sq-D');
  if (conf.squaresVisible) {
    if (sqA) { sqA.style.display = 'block'; sqA.setAttribute('d', conf.sqPaths.A); }
    if (sqB) { sqB.style.display = 'block'; sqB.setAttribute('d', conf.sqPaths.B); }
    if (sqC) { sqC.style.display = 'block'; sqC.setAttribute('d', conf.sqPaths.C); }
    if (sqD) { sqD.style.display = 'block'; sqD.setAttribute('d', conf.sqPaths.D); }
  } else {
    if (sqA) sqA.style.display = 'none';
    if (sqB) sqB.style.display = 'none';
    if (sqC) sqC.style.display = 'none';
    if (sqD) sqD.style.display = 'none';
  }

  if (title) title.textContent = conf.title;
  if (badge) badge.textContent = conf.badge;

  if (propList) {
    propList.innerHTML = conf.props
      .map(p => `<div class="flex items-center gap-2 text-emerald-400">${p}</div>`)
      .join('');
  }
}

// --- CHAPTER 15 QUIZ ENGINE ---
const ch15QuizData = [
  {
    q: '१. समबाहु त्रिभुज (Equilateral Triangle) का प्रत्येक कोणको नाप कति हुन्छ ?',
    opts: ['४५°', '६०°', '९०°', '१२०°'],
    ans: 1,
    exp: 'समबाहु त्रिभुजका तीनवटै भुजाहरू र तीनवटै कोणहरू बराबर हुन्छन्: १८०° ÷ ३ = ६०° ।'
  },
  {
    q: '२. त्रिभुजका तीनवटै भित्री कोणहरूको योगफल सधैँ कति डिग्री हुन्छ ?',
    opts: ['९०°', '१८०°', '२७०°', '३६०°'],
    ans: 1,
    exp: 'ज्यामितिको आधारभूत साध्य अनुसार जुनसुकै त्रिभुजका तीन भित्री कोणको योग १८०° (२ समकोण) हुन्छ ।'
  },
  {
    q: '३. कुनै एउटा कोण ९०° भन्दा ठूलो भएको त्रिभुजलाई के भनिन्छ ?',
    opts: ['न्यूनकोणी', 'समकोणी', 'अधिककोणी', 'समबाहु'],
    ans: 2,
    exp: 'एउटा कोण ९०° भन्दा बढी (अधिककोण) भएको त्रिभुज अधिककोणी त्रिभुज हो ।'
  },
  {
    q: '४. कुनै दुईवटा भुजाहरू मात्र बराबर भएको त्रिभुज कुन हो ?',
    opts: ['समबाहु', 'समद्विबाहु', 'विषमबाहु', 'अधिककोणी'],
    ans: 1,
    exp: 'दुई भुजा बराबर भएको त्रिभुजलाई समद्विबाहु त्रिभुज (Isosceles Triangle) भनिन्छ ।'
  },
  {
    q: '५. चतुर्भुजका चारवटै भित्री कोणहरूको योगफल कति डिग्री हुन्छ ?',
    opts: ['१८०°', '२७०°', '३६०°', '५४०°'],
    ans: 2,
    exp: 'चतुर्भुजमा २ वटा त्रिभुज बन्ने भएकाले कुल कोण योगफल १८०° × २ = ३६०° हुन्छ ।'
  },
  {
    q: '६. चारवटै भुजा बराबर र चारवटै कोण ९०° भएको चतुर्भुजलाई के भनिन्छ ?',
    opts: ['आयत', 'समानान्तर चतुर्भुज', 'वर्ग', 'समलम्ब चतुर्भुज'],
    ans: 2,
    exp: 'चारै भुजा बराबर र चारै कोण ९०° भएको चतुर्भुज वर्ग (Square) हो ।'
  },
  {
    q: '७. केवल एक जोडा सम्मुख भुजाहरू मात्र समानान्तर भएको चतुर्भुज कुन हो ?',
    opts: ['समलम्ब चतुर्भुज (Trapezium)', 'आयत', 'समबाहु चतुर्भुज', 'समानान्तर चतुर्भुज'],
    ans: 0,
    exp: 'जुन चतुर्भुजका केवल १ जोडा सम्मुख भुजाहरू समानान्तर हुन्छन्, त्यसलाई समलम्ब चतुर्भुज भनिन्छ ।'
  },
  {
    q: '८. एउटा समद्विबाहु त्रिभुजको शीर्षकोण ४०° छ भने त्यसका समान आधारकोणहरू कति-कति हुन्छन् ?',
    opts: ['४०° र ४०°', '५०° र ५०°', '७०° र ७०°', '८०° र ८०°'],
    ans: 2,
    exp: '१८०° - ४०° = १४०° । दुई आधारकोण बराबर हुने भएकाले १४०° ÷ २ = ७०° र ७०° हुन्छ ।'
  },
  {
    q: '९. त्रिभुजको बाहिरी कोण ११०° र एउटा अनासन्न भित्री कोण ५०° छ भने अर्को भित्री कोण कति हुन्छ ?',
    opts: ['५०°', '६०°', '७०°', '११०°'],
    ans: 1,
    exp: 'बाहिरी कोण साध्य अनुसार: ११०° - ५०° = ६०° ।'
  },
  {
    q: '१०. समानान्तर चतुर्भुजको एउटा कोण ८०° छ भने त्यसको सम्मुख कोणको नाप कति हुन्छ ?',
    opts: ['८०°', '१००°', '९०°', '१६०°'],
    ans: 0,
    exp: 'समानान्तर चतुर्भुजका सम्मुख कोणहरू सधैँ लम्बाइ र नापमा बराबर हुन्छन्: सम्मुख कोण = ८०° ।'
  }
];

let ch15QuizAnswers = {};

function renderCh15Quiz() {
  const container = document.getElementById('ch15-quiz-container');
  if (!container) return;

  container.innerHTML = ch15QuizData
    .map((item, qIdx) => {
      const isAnswered = ch15QuizAnswers.hasOwnProperty(qIdx);
      const selected = ch15QuizAnswers[qIdx];
      const isCorrect = isAnswered && selected === item.ans;

      const optsHtml = item.opts
        .map((opt, optIdx) => {
          let btnClass = 'p-3 rounded-xl border text-xs md:text-sm text-left transition font-semibold ';
          if (!isAnswered) {
            btnClass += 'bg-slate-50 hover:bg-blue-50 border-slate-200 text-slate-700 cursor-pointer';
          } else {
            if (optIdx === item.ans) {
              btnClass += 'bg-emerald-100 border-emerald-500 text-emerald-900 font-bold';
            } else if (optIdx === selected) {
              btnClass += 'bg-rose-100 border-rose-500 text-rose-900 font-bold';
            } else {
              btnClass += 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
            }
          }

          return `
            <button onclick="handleCh15QuizAnswer(${qIdx}, ${optIdx})" class="${btnClass}">
              ${opt}
            </button>
          `;
        })
        .join('');

      let feedbackHtml = '';
      if (isAnswered) {
        feedbackHtml = `
          <div class="mt-2.5 p-3 rounded-xl text-xs ${isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-rose-50 border border-rose-200 text-rose-900'}">
            <span class="font-bold">${isCorrect ? '✓ सही उत्तर!' : '✗ गलत उत्तर!'}</span> ${item.exp}
          </div>
        `;
      }

      return `
        <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
          <div class="font-bold text-slate-800 text-sm md:text-base">${item.q}</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            ${optsHtml}
          </div>
          ${feedbackHtml}
        </div>
      `;
    })
    .join('');

  updateCh15QuizScore();
}

function handleCh15QuizAnswer(qIdx, optIdx) {
  if (ch15QuizAnswers.hasOwnProperty(qIdx)) return;
  ch15QuizAnswers[qIdx] = optIdx;
  renderCh15Quiz();
}

function updateCh15QuizScore() {
  let score = 0;
  Object.keys(ch15QuizAnswers).forEach(qIdx => {
    if (ch15QuizAnswers[qIdx] === ch15QuizData[qIdx].ans) {
      score++;
    }
  });
  const el = document.getElementById('ch15-quiz-score');
  if (el) el.textContent = score;
}

function resetCh15Quiz() {
  ch15QuizAnswers = {};
  renderCh15Quiz();
}

// Initialize when view loads
document.addEventListener('DOMContentLoaded', () => {
  updateTriangleLab();
  setQuadType('rectangle');
});
