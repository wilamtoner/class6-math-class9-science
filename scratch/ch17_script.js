// ==================== CHAPTER 17 INTERACTIVE ENGINE ====================

// --- Tab Switcher ---
function setTabCh17(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById('ch17-tab-' + t);
    const view = document.getElementById('ch17-view-' + t);
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
    renderCh17Quiz();
  }

  try {
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('chapter-view-17'), {
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
function switchCh17Lab(mode) {
  const polyLab = document.getElementById('ch17-sublab-poly');
  const curvedLab = document.getElementById('ch17-sublab-curved');
  const netLab = document.getElementById('ch17-sublab-net');
  const btnPoly = document.getElementById('btn-lab-poly');
  const btnCurved = document.getElementById('btn-lab-curved');
  const btnNet = document.getElementById('btn-lab-net');

  const activeCls = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-sm transition cursor-pointer';
  const inactiveCls = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';

  if (mode === 'poly') {
    if (polyLab) polyLab.classList.remove('hidden');
    if (curvedLab) curvedLab.classList.add('hidden');
    if (netLab) netLab.classList.add('hidden');
    if (btnPoly) btnPoly.className = activeCls;
    if (btnCurved) btnCurved.className = inactiveCls;
    if (btnNet) btnNet.className = inactiveCls;
    updatePolyLab();
  } else if (mode === 'curved') {
    if (polyLab) polyLab.classList.add('hidden');
    if (curvedLab) curvedLab.classList.remove('hidden');
    if (netLab) netLab.classList.add('hidden');
    if (btnCurved) btnCurved.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-cyan-600 text-white shadow-sm transition cursor-pointer';
    if (btnPoly) btnPoly.className = inactiveCls;
    if (btnNet) btnNet.className = inactiveCls;
    updateCurvedLab();
  } else if (mode === 'net') {
    if (polyLab) polyLab.classList.add('hidden');
    if (curvedLab) curvedLab.classList.add('hidden');
    if (netLab) netLab.classList.remove('hidden');
    if (btnNet) btnNet.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-purple-600 text-white shadow-sm transition cursor-pointer';
    if (btnPoly) btnPoly.className = inactiveCls;
    if (btnCurved) btnCurved.className = inactiveCls;
    updateNetLab();
  }
}

// --- SUB-LAB 1: POLYHEDRA & EULER EXPLORER STATE ---
let currentPolyShape = 'cube';
let currentPolyHighlight = 'all';

const polyShapeData = {
  cube: {
    title: 'घन (Cube)',
    F: 6,
    V: 8,
    E: 12,
    desc: 'घनमा ६ वटा बराबर वर्गहरू, १२ वटा बराबर सिधा किनारा र ८ वटा शीर्षबिन्दु हुन्छन् । यसका तीनवटै आयामहरू बराबर हुन्छन् (l = b = h) ।'
  },
  cuboid: {
    title: 'षड्मुखा (Cuboid)',
    F: 6,
    V: 8,
    E: 12,
    desc: 'षड्मुखामा ६ वटा आयताकार सतहहरू (३ जोडी समानान्तर आयतहरू), १२ वटा किनारा र ८ वटा शीर्षबिन्दु हुन्छन् ।'
  },
  prism: {
    title: 'त्रिकोणात्मक प्रिज्मा (Triangular Prism)',
    F: 5,
    V: 6,
    E: 9,
    desc: 'प्रिज्मामा २ वटा त्रिभुजाकार आधार र ३ वटा आयताकार सतहहरू गरी जम्मा ५ सतह, ९ किनारा र ६ शीर्षबिन्दु हुन्छन् ।'
  },
  pyramid: {
    title: 'वर्गाकार पिरामिड (Square Pyramid)',
    F: 5,
    V: 5,
    E: 8,
    desc: 'पिरामिडमा १ वटा वर्गाकार आधार र ४ वटा त्रिभुजाकार छड्के सतहहरू हुन्छन् । जम्मा ५ सतह, ८ किनारा र ५ शीर्षबिन्दु हुन्छन् ।'
  },
  tetra: {
    title: 'टेट्राहेड्रन / त्रिभुजाकार पिरामिड',
    F: 4,
    V: 4,
    E: 6,
    desc: 'टेट्राहेड्रनमा ४ वटा त्रिभुजाकार सतहहरू, ६ वटा किनारा र ४ वटा शीर्षबिन्दु हुन्छन् । यो सबैभन्दा सरल बहुफलक हो ।'
  }
};

function setPolyShape(shape) {
  currentPolyShape = shape;
  ['cube', 'cuboid', 'prism', 'pyramid', 'tetra'].forEach(s => {
    const btn = document.getElementById('btn-shape-' + s);
    if (btn) {
      if (s === shape) {
        btn.className = 'px-3 py-2 rounded-xl bg-blue-600 text-white font-bold text-xs shadow-sm transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updatePolyLab();
}

function setPolyHighlight(mode) {
  currentPolyHighlight = mode;
  ['all', 'faces', 'edges', 'vertices'].forEach(m => {
    const btn = document.getElementById('btn-high-' + m);
    if (btn) {
      if (m === mode) {
        btn.className = 'px-3 py-2 rounded-xl bg-indigo-600 text-white font-bold text-xs transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updatePolyLab();
}

function updatePolyLab() {
  const data = polyShapeData[currentPolyShape] || polyShapeData.cube;

  // Update counters
  const fEl = document.getElementById('live-f-val');
  const vEl = document.getElementById('live-v-val');
  const eEl = document.getElementById('live-e-val');
  const eulerEl = document.getElementById('live-euler-val');
  const badgeEl = document.getElementById('poly-part-badge');
  const titleEl = document.getElementById('poly-shape-title');
  const descEl = document.getElementById('poly-desc-box');
  const calcEl = document.getElementById('poly-euler-calc');

  if (fEl) fEl.textContent = data.F;
  if (vEl) vEl.textContent = data.V;
  if (eEl) eEl.textContent = data.E;
  if (eulerEl) eulerEl.textContent = (data.F + data.V - data.E) + ' ✓';
  if (badgeEl) badgeEl.textContent = data.title;
  if (titleEl) titleEl.textContent = data.title;
  if (descEl) descEl.textContent = data.desc;
  if (calcEl) calcEl.textContent = `F + V - E = ${data.F} + ${data.V} - ${data.E} = 2`;

  // Sync inputs
  const inF = document.getElementById('calc-f-input');
  const inV = document.getElementById('calc-v-input');
  const inE = document.getElementById('calc-e-input');
  if (inF) inF.value = data.F;
  if (inV) inV.value = data.V;
  if (inE) inE.value = data.E;
  const solverRes = document.getElementById('calc-solver-result');
  if (solverRes) {
    solverRes.textContent = `E = F + V - 2 = ${data.F} + ${data.V} - 2 = ${data.E}`;
  }

  // Render 3D SVG
  renderPolySvg(currentPolyShape, currentPolyHighlight);
}

function renderPolySvg(shape, highlight) {
  const container = document.getElementById('poly-svg-shapes');
  if (!container) return;

  const showFaces = highlight === 'all' || highlight === 'faces';
  const showEdges = highlight === 'all' || highlight === 'edges';
  const showVerts = highlight === 'all' || highlight === 'vertices';

  const faceFill = showFaces ? 'rgba(99, 102, 241, 0.35)' : 'rgba(99, 102, 241, 0.12)';
  const faceStroke = showFaces ? '#818cf8' : 'rgba(129, 140, 248, 0.4)';
  const edgeColor = showEdges ? '#f59e0b' : '#38bdf8';
  const edgeWidth = showEdges ? 3.5 : 2;
  const vertFill = showVerts ? '#f43f5e' : '#3b82f6';
  const vertR = showVerts ? 6.5 : 4.5;

  let html = '';

  if (shape === 'cube' || shape === 'cuboid') {
    const isCube = shape === 'cube';
    const w = isCube ? 150 : 200;
    const h = isCube ? 150 : 120;
    const dx = isCube ? 55 : 60;
    const dy = isCube ? 55 : 45;
    const ox = 70;
    const oy = 160;

    const A = { x: ox + dx, y: oy - h - dy, name: 'A' };
    const B = { x: ox + w + dx, y: oy - h - dy, name: 'B' };
    const C = { x: ox + w, y: oy - h, name: 'C' };
    const D = { x: ox, y: oy - h, name: 'D' };
    const E = { x: ox + dx, y: oy - dy, name: 'E' };
    const F = { x: ox + w + dx, y: oy - dy, name: 'F' };
    const G = { x: ox + w, y: oy, name: 'G' };
    const H = { x: ox, y: oy, name: 'H' };

    // Dashed back edges
    html += `
      <line x1="${E.x}" y1="${E.y}" x2="${A.x}" y2="${A.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${E.x}" y1="${E.y}" x2="${F.x}" y2="${F.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${H.x}" y1="${H.y}" x2="${E.x}" y2="${E.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
    `;

    // Shaded Faces
    html += `
      <!-- Top Face ABCD -->
      <polygon points="${A.x},${A.y} ${B.x},${B.y} ${C.x},${C.y} ${D.x},${D.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Right Face BCGF -->
      <polygon points="${B.x},${B.y} ${C.x},${C.y} ${G.x},${G.y} ${F.x},${F.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Front Face DCGH -->
      <polygon points="${D.x},${D.y} ${C.x},${C.y} ${G.x},${G.y} ${H.x},${H.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Visible Edges
    const edges = [
      [A, B], [B, C], [C, D], [D, A],
      [B, F], [C, G], [D, H],
      [F, G], [G, H]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    // Vertices
    const verts = [A, B, C, D, E, F, G, H];
    verts.forEach(p => {
      const isBack = p === E;
      const fill = isBack ? '#94a3b8' : vertFill;
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${fill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  } else if (shape === 'prism') {
    // Triangular Prism
    const A = { x: 90, y: 110, name: 'A' };
    const B = { x: 190, y: 190, name: 'B' };
    const C = { x: 50, y: 220, name: 'C' };

    const D = { x: 260, y: 110, name: 'D' };
    const E = { x: 360, y: 190, name: 'E' };
    const F = { x: 220, y: 220, name: 'F' };

    // Back dashed edge
    html += `<line x1="${A.x}" y1="${A.y}" x2="${D.x}" y2="${D.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />`;

    // Faces
    html += `
      <!-- Front Triangle ABC -->
      <polygon points="${A.x},${A.y} ${B.x},${B.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Back Triangle DEF -->
      <polygon points="${D.x},${D.y} ${E.x},${E.y} ${F.x},${F.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Lateral Face ABED -->
      <polygon points="${A.x},${A.y} ${B.x},${B.y} ${E.x},${E.y} ${D.x},${D.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Lateral Face BCFE -->
      <polygon points="${B.x},${B.y} ${C.x},${C.y} ${F.x},${F.y} ${E.x},${E.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Edges
    const edges = [
      [A, B], [B, C], [C, A],
      [D, E], [E, F], [F, D],
      [B, E], [C, F]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    // Vertices
    [A, B, C, D, E, F].forEach(p => {
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${vertFill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  } else if (shape === 'pyramid') {
    // Square Pyramid
    const Apex = { x: 200, y: 70, name: 'V' };
    const A = { x: 120, y: 220, name: 'A' };
    const B = { x: 280, y: 220, name: 'B' };
    const C = { x: 330, y: 270, name: 'C' };
    const D = { x: 70, y: 270, name: 'D' };

    // Dashed back lines
    html += `
      <line x1="${A.x}" y1="${A.y}" x2="${Apex.x}" y2="${Apex.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${A.x}" y1="${A.y}" x2="${B.x}" y2="${B.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${D.x}" y1="${D.y}" x2="${A.x}" y2="${A.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
    `;

    // Faces
    html += `
      <polygon points="${Apex.x},${Apex.y} ${B.x},${B.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <polygon points="${Apex.x},${Apex.y} ${D.x},${D.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Edges
    const edges = [
      [Apex, B], [Apex, C], [Apex, D],
      [B, C], [C, D]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    [Apex, A, B, C, D].forEach(p => {
      const isBack = p === A;
      const fill = isBack ? '#94a3b8' : vertFill;
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${fill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  } else if (shape === 'tetra') {
    // Tetrahedron (Triangular Pyramid)
    const Apex = { x: 200, y: 70, name: 'V' };
    const A = { x: 170, y: 220, name: 'A' };
    const B = { x: 310, y: 250, name: 'B' };
    const C = { x: 90, y: 260, name: 'C' };

    // Dashed back edge
    html += `
      <line x1="${A.x}" y1="${A.y}" x2="${Apex.x}" y2="${Apex.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${C.x}" y1="${C.y}" x2="${A.x}" y2="${A.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${A.x}" y1="${A.y}" x2="${B.x}" y2="${B.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
    `;

    // Front Faces
    html += `
      <polygon points="${Apex.x},${Apex.y} ${B.x},${B.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Edges
    const edges = [
      [Apex, B], [Apex, C],
      [C, B]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    [Apex, A, B, C].forEach(p => {
      const isBack = p === A;
      const fill = isBack ? '#94a3b8' : vertFill;
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${fill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  }

  container.innerHTML = html;
}

function solveEulerUnknown(changed) {
  const fIn = document.getElementById('calc-f-input');
  const vIn = document.getElementById('calc-v-input');
  const eIn = document.getElementById('calc-e-input');
  const resEl = document.getElementById('calc-solver-result');
  if (!fIn || !vIn || !eIn || !resEl) return;

  let F = parseInt(fIn.value) || 0;
  let V = parseInt(vIn.value) || 0;
  let E = parseInt(eIn.value) || 0;

  if (changed === 'E') {
    // If user changed E, solve for V or check formula
    V = 2 + E - F;
    vIn.value = V;
    resEl.textContent = `कुना V = 2 + E - F = 2 + ${E} - ${F} = ${V}`;
  } else {
    // Calculate E
    E = F + V - 2;
    eIn.value = E;
    resEl.textContent = `किनारा E = F + V - 2 = ${F} + ${V} - 2 = ${E}`;
  }
}

// --- SUB-LAB 2: CURVED SOLIDS EXPLORER STATE ---
let currentCurvedShape = 'cylinder';

const curvedShapeData = {
  cylinder: {
    title: 'बेलना (Cylinder)',
    surfaces: '२ समतल (वृत्ताकार आधार) + १ वक्र सतह',
    vertices: '०',
    desc: 'बेलनामा माथि र तल २ ओटा बराबर वृत्ताकार समतलीय आधारहरू हुन्छन् र वरिपरि एउटा वक्र सतह हुन्छ । यसमा २ ओटा घुमाउरा किनारा हुन्छन् तर कुनै कुना हुँदैन ($V=0$) ।'
  },
  cone: {
    title: 'सोली (Cone)',
    surfaces: '१ समतलीय वृत्ताकार आधार + १ वक्र सतह',
    vertices: '१ (शीर्षबिन्दु / Apex)',
    desc: 'सोलीमा तल १ वटा समतलीय वृत्ताकार आधार र वरिपरि घुमेको वक्र सतह हुन्छ । यसको माथिल्लो टुप्पोमा ठ्याक्कै १ वटा शीर्षबिन्दु (Vertex) हुन्छ र १ घुमाउरो किनारा हुन्छ ।'
  },
  sphere: {
    title: 'गोला (Sphere)',
    surfaces: '१ पूर्ण वक्र सतह (समतल सतह शून्य)',
    vertices: '०',
    desc: 'गोला केन्द्रबिन्दुबाट सतहका सबै बिन्दुहरू बराबर दूरीमा भएको पूर्ण वक्र ठोस वस्तु हो । यसमा कुनै समतल सतह, किनारा वा शीर्षबिन्दु हुँदैन ।'
  }
};

function setCurvedShape(shape) {
  currentCurvedShape = shape;
  ['cyl', 'cone', 'sph'].forEach(s => {
    const btn = document.getElementById('btn-curved-' + s);
    const map = { cyl: 'cylinder', cone: 'cone', sph: 'sphere' };
    if (btn) {
      if (map[s] === shape) {
        btn.className = 'px-3 py-2 rounded-xl bg-cyan-600 text-white font-bold text-xs shadow-sm transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updateCurvedLab();
}

function updateCurvedLab() {
  const data = curvedShapeData[currentCurvedShape] || curvedShapeData.cylinder;

  const badgeEl = document.getElementById('curved-part-badge');
  const surEl = document.getElementById('curved-surface-types');
  const vEl = document.getElementById('curved-v-count');
  const descEl = document.getElementById('curved-desc-box');

  if (badgeEl) badgeEl.textContent = data.title;
  if (surEl) surEl.textContent = data.surfaces;
  if (vEl) vEl.textContent = data.vertices;
  if (descEl) descEl.textContent = data.desc;

  renderCurvedSvg(currentCurvedShape);
}

function renderCurvedSvg(shape) {
  const container = document.getElementById('curved-svg-shapes');
  if (!container) return;

  let html = '';

  if (shape === 'cylinder') {
    // Cylinder SVG
    html = `
      <!-- Lower Base Dashed Back Arc -->
      <path d="M 120 280 A 80 30 0 0 1 280 280" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <!-- Lower Base Visible Front Arc -->
      <path d="M 120 280 A 80 30 0 0 0 280 280" fill="none" stroke="#38bdf8" stroke-width="3" />
      
      <!-- Body Shading -->
      <path d="M 120 120 L 120 280 A 80 30 0 0 0 280 280 L 280 120 Z" fill="rgba(56, 189, 248, 0.15)" stroke="none" />
      
      <!-- Side Generators -->
      <line x1="120" y1="120" x2="120" y2="280" stroke="#38bdf8" stroke-width="3" />
      <line x1="280" y1="120" x2="280" y2="280" stroke="#38bdf8" stroke-width="3" />
      
      <!-- Top Elliptical Flat Face -->
      <ellipse cx="200" cy="120" rx="80" ry="30" fill="rgba(56, 189, 248, 0.35)" stroke="#38bdf8" stroke-width="3" />
      
      <!-- Center and Radius in Top Base -->
      <circle cx="200" cy="120" r="4" fill="#f43f5e" />
      <line x1="200" y1="120" x2="280" y2="120" stroke="#f43f5e" stroke-width="2" />
      <text x="235" y="112" fill="#f43f5e" font-size="11" font-weight="bold">r</text>
      
      <!-- Height Dimension Arrow -->
      <line x1="90" y1="120" x2="90" y2="280" stroke="#eab308" stroke-width="1.5" />
      <polygon points="90,115 86,125 94,125" fill="#eab308" />
      <polygon points="90,285 86,275 94,275" fill="#eab308" />
      <text x="75" y="205" fill="#eab308" font-size="12" font-weight="bold">h</text>
    `;
  } else if (shape === 'cone') {
    // Cone SVG
    html = `
      <!-- Base Dashed Back Arc -->
      <path d="M 110 280 A 90 32 0 0 1 290 280" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <!-- Base Visible Front Arc -->
      <path d="M 110 280 A 90 32 0 0 0 290 280" fill="none" stroke="#f59e0b" stroke-width="3" />
      
      <!-- Cone Curved Body Fill -->
      <path d="M 200 80 L 110 280 A 90 32 0 0 0 290 280 Z" fill="rgba(245, 158, 11, 0.2)" stroke="none" />
      
      <!-- Slant Sides -->
      <line x1="200" y1="80" x2="110" y2="280" stroke="#f59e0b" stroke-width="3" />
      <line x1="200" y1="80" x2="290" y2="280" stroke="#f59e0b" stroke-width="3" />
      
      <!-- Apex Vertex -->
      <circle cx="200" cy="80" r="6" fill="#f43f5e" stroke="#ffffff" stroke-width="2" />
      <text x="212" y="78" fill="#f43f5e" font-size="13" font-weight="extrabold">शीर्षबिन्दु (Vertex)</text>
      
      <!-- Base Radius -->
      <circle cx="200" cy="280" r="4" fill="#38bdf8" />
      <line x1="200" y1="280" x2="290" y2="280" stroke="#38bdf8" stroke-width="2" />
      <text x="245" y="272" fill="#38bdf8" font-size="11" font-weight="bold">r</text>
    `;
  } else if (shape === 'sphere') {
    // Sphere SVG
    html = `
      <!-- Sphere Outer Boundary Circle -->
      <circle cx="200" cy="200" r="100" fill="rgba(168, 85, 247, 0.2)" stroke="#a855f7" stroke-width="3.5" />
      
      <!-- Equatorial Ellipse (Dashed back) -->
      <path d="M 100 200 A 100 35 0 0 1 300 200" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <!-- Equatorial Ellipse (Front) -->
      <path d="M 100 200 A 100 35 0 0 0 300 200" fill="none" stroke="#c084fc" stroke-width="2.5" />
      
      <!-- Polar Meridian Ellipse (Vertical) -->
      <ellipse cx="200" cy="200" rx="35" ry="100" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="2,2" />
      
      <!-- Centre O -->
      <circle cx="200" cy="200" r="5" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
      <text x="185" y="195" fill="#ffffff" font-size="12" font-weight="bold">O</text>
      
      <!-- Radius Line -->
      <line x1="200" y1="200" x2="300" y2="200" stroke="#f43f5e" stroke-width="2.5" />
      <text x="245" y="190" fill="#f43f5e" font-size="12" font-weight="bold">r</text>
    `;
  }

  container.innerHTML = html;
}

// --- SUB-LAB 3: 3D NET / UNPOLDING LAB STATE ---
let currentNetShape = 'cube';

const netShapeData = {
  cube: {
    title: 'घनको नेट (Cube Net)',
    desc: '६ वटा बराबर वर्गहरू मिलेर बनेको क्रस (Cross / T) ढाँचा । यसलाई पट्याउँदा ठ्याक्कै घन बन्दछ ।',
    faces: 6,
    tip: '💡 <strong>घनको नेट:</strong> ६ वटा वर्गहरूलाई विभिन्न ११ प्रकारका वैध ढाँचामा फैलाउन सकिन्छ । ती सबैबाट पट्याएर घन बनाउन सकिन्छ ।'
  },
  cuboid: {
    title: 'षड्मुखाको नेट (Cuboid Net)',
    desc: '६ वटा आयताकार सतहहरू (३ जोडी फरक आयतहरू) मिलेर बनेको ढाँचा ।',
    faces: 6,
    tip: '💡 <strong>षड्मुखाको नेट:</strong> विपरीत आयताकार सतहहरू एकअर्काको सिधा समानान्तर हुने गरी पट्याइन्छ ।'
  },
  cylinder: {
    title: 'बेलनाको नेट (Cylinder Net)',
    desc: '१ वटा लामो आयत (वक्र सतह खोल्दा) र २ वटा बराबर वृत्तहरू (माथिल्लो र तल्लो आधार) ।',
    faces: 3,
    tip: '💡 <strong>बेलनाको वक्र सतह:</strong> आयतको लम्बाइ ठ्याक्कै वृत्तको परिधि ($2\\pi r$) बराबर हुन्छ र चौडाइ बेलनाको उचाइ ($h$) बराबर हुन्छ ।'
  },
  cone: {
    title: 'सोलीको नेट (Cone Net)',
    desc: '१ वटा वृत्तखण्ड वा क्षेत्रक (वक्र सतह खोल्दा) र १ वटा वृत्ताकार समतल आधार ।',
    faces: 2,
    tip: '💡 <strong>सोलीको जाली:</strong> क्षेत्रकको चापको लम्बाइ आधार वृत्तको परिधि बराबर हुन्छ ।'
  }
};

function setNetShape(shape) {
  currentNetShape = shape;
  ['cube', 'cuboid', 'cylinder', 'cone'].forEach(s => {
    const btn = document.getElementById('btn-net-' + s);
    if (btn) {
      if (s === shape) {
        btn.className = 'px-3 py-2 rounded-xl bg-purple-600 text-white font-bold text-xs shadow-sm transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updateNetLab();
}

function updateNetLab() {
  const data = netShapeData[currentNetShape] || netShapeData.cube;

  const badgeEl = document.getElementById('net-part-badge');
  const descEl = document.getElementById('net-desc-summary');
  const fEl = document.getElementById('net-faces-count');
  const tipEl = document.getElementById('net-tip-box');

  if (badgeEl) badgeEl.textContent = data.title;
  if (descEl) descEl.textContent = data.desc;
  if (fEl) fEl.textContent = data.faces;
  if (tipEl) tipEl.innerHTML = data.tip;

  renderNetSvg(currentNetShape);
}

function renderNetSvg(shape) {
  const container = document.getElementById('net-svg-shapes');
  if (!container) return;

  let html = '';

  if (shape === 'cube') {
    // Cross-shaped Cube Net (4 in row, 1 top, 1 bottom)
    const s = 50;
    const ox = 75;
    const oy = 100;
    const squares = [
      { x: ox + s, y: oy, label: '१' },      // Top
      { x: ox, y: oy + s, label: '२' },      // Left
      { x: ox + s, y: oy + s, label: '३' },  // Middle
      { x: ox + 2 * s, y: oy + s, label: '४' }, // Right
      { x: ox + 3 * s, y: oy + s, label: '५' }, // Far Right
      { x: ox + s, y: oy + 2 * s, label: '६' }  // Bottom
    ];

    squares.forEach(sq => {
      html += `
        <rect x="${sq.x}" y="${sq.y}" width="${s}" height="${s}" fill="rgba(168, 85, 247, 0.3)" stroke="#c084fc" stroke-width="2" rx="2" />
        <text x="${sq.x + s/2}" y="${sq.y + s/2 + 5}" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">${sq.label}</text>
      `;
    });
  } else if (shape === 'cuboid') {
    // Cuboid Net
    const ox = 70;
    const oy = 90;
    const l = 60;
    const b = 45;
    const h = 50;

    // 6 Rectangles
    html = `
      <!-- Top -->
      <rect x="${ox + b}" y="${oy}" width="${l}" height="${b}" fill="rgba(99, 102, 241, 0.3)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l/2}" y="${oy + b/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">माथि</text>
      
      <!-- Side Left -->
      <rect x="${ox}" y="${oy + b}" width="${b}" height="${h}" fill="rgba(99, 102, 241, 0.25)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">बायाँ</text>
      
      <!-- Front -->
      <rect x="${ox + b}" y="${oy + b}" width="${l}" height="${h}" fill="rgba(99, 102, 241, 0.35)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">अगाडि</text>
      
      <!-- Side Right -->
      <rect x="${ox + b + l}" y="${oy + b}" width="${b}" height="${h}" fill="rgba(99, 102, 241, 0.25)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l + b/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">दायाँ</text>
      
      <!-- Back -->
      <rect x="${ox + 2*b + l}" y="${oy + b}" width="${l}" height="${h}" fill="rgba(99, 102, 241, 0.35)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + 2*b + 3*l/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">पछाडि</text>
      
      <!-- Bottom -->
      <rect x="${ox + b}" y="${oy + b + h}" width="${l}" height="${b}" fill="rgba(99, 102, 241, 0.3)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l/2}" y="${oy + b + h + b/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">तल</text>
    `;
  } else if (shape === 'cylinder') {
    // Cylinder Net (1 Rectangle + 2 Circles)
    html = `
      <!-- Top Circle -->
      <circle cx="200" cy="90" r="35" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="2" />
      <text x="200" y="94" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">माथिल्लो वृत्त</text>
      
      <!-- Lateral Rectangle -->
      <rect x="90" y="135" width="220" height="90" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2" rx="3" />
      <text x="200" y="175" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">वक्र सतह (Rectangle: 2πr × h)</text>
      <text x="200" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">लम्बाइ = परिधि (2πr), चौडाइ = उचाइ (h)</text>
      
      <!-- Bottom Circle -->
      <circle cx="200" cy="270" r="35" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="2" />
      <text x="200" y="274" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">तल्लो वृत्त</text>
    `;
  } else if (shape === 'cone') {
    // Cone Net (1 Sector + 1 Circle)
    html = `
      <!-- Sector (Curved Surface) -->
      <path d="M 200 80 L 110 220 A 160 160 0 0 0 290 220 Z" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2.5" />
      <text x="200" y="160" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">वक्र सतह (Sector)</text>
      
      <!-- Base Circle -->
      <circle cx="200" cy="280" r="40" fill="rgba(245, 158, 11, 0.35)" stroke="#f59e0b" stroke-width="2" />
      <text x="200" y="284" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">वृत्ताकार आधार</text>
    `;
  }

  container.innerHTML = html;
}

// ==================== CHAPTER 17 QUIZ ENGINE ====================
const ch17QuizData = [
  {
    q: '१. ६ वटा बराबर वर्गाकार सतहहरू मिलेर बनेको ठोस वस्तु कुन हो ?',
    opts: ['षड्मुखा (Cuboid)', 'घन (Cube)', 'बेलना (Cylinder)', 'पिरामिड'],
    ans: 1,
    exp: 'छओटा बराबर वर्गाकार समतलीय सतहहरू मिलेर बनेको बन्द ठोस वस्तुलाई घन (Cube) भनिन्छ ।'
  },
  {
    q: '२. बहुफलकमा सतह (F), शीर्षबिन्दु (V) र किनारा (E) बीचको यूलरको सही सूत्र कुन हो ?',
    opts: ['V + E + F = 2', 'V - E + F = 2', 'F - V + E = 2', 'E - V - F = 2'],
    ans: 1,
    exp: 'यूलरको सूत्र अनुसार V - E + F = 2 वा F + V = E + 2 हुन्छ ।'
  },
  {
    q: '३. एउटा षड्मुखा (Cuboid) मा कतिवटा किनाराहरू (Edges) हुन्छन् ?',
    opts: ['६ ओटा', '८ ओटा', '१० ओटा', '१२ ओटा'],
    ans: 3,
    exp: 'षड्मुखामा ४ लम्बाइ, ४ चौडाइ र ४ उचाइ गरी जम्मा १२ ओटा किनाराहरू हुन्छन् ।'
  },
  {
    q: '४. कुनै ठोस वस्तुमा सतह F = 5 र शीर्षबिन्दु V = 6 भए किनारा E को मान कति हुन्छ ?',
    opts: ['७ ओटा', '८ ओटा', '९ ओटा', '११ ओटा'],
    ans: 2,
    exp: 'यूलर सूत्र अनुसार: E = F + V - 2 = 5 + 6 - 2 = 9 ओटा किनारा हुन्छन् (यो त्रिकोणात्मक प्रिज्मा हो) ।'
  },
  {
    q: '५. तलका मध्ये कुन ठोस वस्तुमा ठ्याक्कै एउटा मात्र शीर्षबिन्दु (Vertex) हुन्छ ?',
    opts: ['बेलना (Cylinder)', 'सोली (Cone)', 'गोला (Sphere)', 'घन (Cube)'],
    ans: 1,
    exp: 'सोली (Cone) मा तल १ वृत्ताकार आधार र माथिल्लो टुप्पोमा ठ्याक्कै १ वटा शीर्षबिन्दु हुन्छ ।'
  },
  {
    q: '६. बेलना (Cylinder) मा कतिवटा समतलीय र कतिवटा वक्र सतह हुन्छन् ?',
    opts: ['२ समतलीय र १ वक्र सतह', '१ समतलीय र २ वक्र सतह', '३ समतलीय सतह', '१ वक्र सतह मात्र'],
    ans: 0,
    exp: 'बेलनामा माथि र तल २ ओटा समतलीय वृत्ताकार सतह र १ वटा वक्र सतह गरी जम्मा ३ सतह हुन्छन् ।'
  },
  {
    q: '७. फुटबल, गुच्चा र सुन्तला कुन ठोस ज्यामितीय आकृतिका उदाहरण हुन् ?',
    opts: ['बेलना (Cylinder)', 'सोली (Cone)', 'गोला (Sphere)', 'पिरामिड'],
    ans: 2,
    exp: 'फुटबल र गुच्चा पूर्ण रूपमा गोलाकार वक्र सतह भएकाले यी गोला (Sphere) का उदाहरण हुन् ।'
  },
  {
    q: '८. एउटा षड्मुखाको लम्बाइ, चौडाइ र उचाइ तीनवटै बराबर भएमा उक्त आकृति के बन्दछ ?',
    opts: ['बेलना', 'सोली', 'घन (Cube)', 'प्रिज्मा'],
    ans: 2,
    exp: 'जब षड्मुखामा l = b = h हुन्छ, सबै ६ सतहहरू वर्ग बन्दछन् र त्यो आकृति घन बन्दछ ।'
  },
  {
    q: '९. वर्गाकार आधार भएको पिरामिड (Square Pyramid) मा जम्मा कतिवटा सतहहरू हुन्छन् ?',
    opts: ['४ ओटा', '५ ओटा', '६ ओटा', '८ ओटा'],
    ans: 1,
    exp: 'वर्गाकार पिरामिडमा १ वटा वर्गाकार आधार र ४ वटा त्रिभुजाकार सतह गरी जम्मा ५ ओटा सतह हुन्छन् ।'
  },
  {
    q: '१०. तलका मध्ये कुन ठोस वस्तुमा कुनै पनि कुना (शीर्षबिन्दु) र समतलीय सतह हुँदैन ?',
    opts: ['घन', 'षड्मुखा', 'बेलना', 'गोला (Sphere)'],
    ans: 3,
    exp: 'गोला (Sphere) मा एउटा मात्र पूर्ण वक्र सतह हुन्छ; यसमा कुनै समतल सतह, किनारा वा शीर्षबिन्दु हुँदैन ।'
  }
];

let ch17QuizAnswers = {};

function renderCh17Quiz() {
  const container = document.getElementById('ch17-quiz-container');
  if (!container) return;

  container.innerHTML = ch17QuizData
    .map((item, qIdx) => {
      const isAnswered = ch17QuizAnswers.hasOwnProperty(qIdx);
      const selAns = ch17QuizAnswers[qIdx];
      const isCorrect = isAnswered && selAns === item.ans;

      const optsHtml = item.opts
        .map((opt, optIdx) => {
          let btnClass = 'p-3 rounded-xl border text-left text-xs md:text-sm transition cursor-pointer ';
          if (!isAnswered) {
            btnClass += 'bg-slate-50 border-slate-200 hover:bg-blue-50 hover:border-blue-300 text-slate-800';
          } else {
            if (optIdx === item.ans) {
              btnClass += 'bg-emerald-100 border-emerald-500 text-emerald-900 font-bold';
            } else if (optIdx === selAns) {
              btnClass += 'bg-rose-100 border-rose-500 text-rose-900 font-bold';
            } else {
              btnClass += 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
            }
          }

          return `
            <button onclick="handleCh17QuizAnswer(${qIdx}, ${optIdx})" class="${btnClass}">
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

  updateCh17QuizScore();
}

function handleCh17QuizAnswer(qIdx, optIdx) {
  if (ch17QuizAnswers.hasOwnProperty(qIdx)) return;
  ch17QuizAnswers[qIdx] = optIdx;
  renderCh17Quiz();
}

function updateCh17QuizScore() {
  let score = 0;
  Object.keys(ch17QuizAnswers).forEach(qIdx => {
    if (ch17QuizAnswers[qIdx] === ch17QuizData[qIdx].ans) {
      score++;
    }
  });
  const el = document.getElementById('ch17-quiz-score');
  if (el) el.textContent = score;
}

function resetCh17Quiz() {
  ch17QuizAnswers = {};
  renderCh17Quiz();
}

// Initialise Chapter 17 Lab on load
document.addEventListener('DOMContentLoaded', () => {
  updatePolyLab();
});