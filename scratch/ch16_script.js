
// ==================== CHAPTER 16 INTERACTIVE ENGINE ====================

// --- Tab Switcher ---
function setTabCh16(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById('ch16-tab-' + t);
    const view = document.getElementById('ch16-view-' + t);
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
    renderCh16Quiz();
  }

  // Render MathJax / KaTeX if available
  try {
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('chapter-view-16'), {
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
function switchCh16Lab(mode) {
  const circLab = document.getElementById('ch16-sublab-circle');
  const wheelLab = document.getElementById('ch16-sublab-wheel');
  const btnCirc = document.getElementById('btn-lab-circle');
  const btnWheel = document.getElementById('btn-lab-wheel');

  if (mode === 'circle') {
    if (circLab) circLab.classList.remove('hidden');
    if (wheelLab) wheelLab.classList.add('hidden');
    if (btnCirc) btnCirc.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-sm transition cursor-pointer';
    if (btnWheel) btnWheel.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
  } else {
    if (circLab) circLab.classList.add('hidden');
    if (wheelLab) wheelLab.classList.remove('hidden');
    if (btnWheel) btnWheel.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-cyan-600 text-white shadow-sm transition cursor-pointer';
    if (btnCirc) btnCirc.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
    onWheelChange();
  }
}

// --- DYNAMIC CIRCLE LAB ---
let circleCurrentRadius = 7.0; // in cm
let circleCurrentPart = 'radius';

const circlePartDetails = {
  centre: {
    title: 'केन्द्रबिन्दु (Centre - O)',
    badge: 'केन्द्रबिन्दु (Centre)',
    desc: 'वृत्तको ठीक बीचमा रहने निश्चित स्थिर बिन्दुलाई केन्द्रबिन्दु भनिन्छ । परिधिका सबै बिन्दुहरू यसबाट सधैँ समान दूरीमा रहन्छन् ।',
    formula: 'केन्द्रबिन्दु O बाट परिधिसम्मको दूरी = अर्धव्यास (r)',
    color: '#f43f5e'
  },
  radius: {
    title: 'अर्धव्यास (Radius - r)',
    badge: 'अर्धव्यास (Radius)',
    desc: 'वृत्तको केन्द्रबिन्दु O बाट परिधिको कुनै पनि बिन्दुसम्म जोड्ने सीधा रेखाखण्डलाई अर्धव्यास भनिन्छ । यो व्यासको आधा हुन्छ ।',
    formula: 'अर्धव्यास r = d ÷ २',
    color: '#10b981'
  },
  diameter: {
    title: 'व्यास (Diameter - d)',
    badge: 'व्यास (Diameter)',
    desc: 'केन्द्रबिन्दु O भएर जाने र दुवै छेउ परिधिमा छुने सीधा रेखाखण्ड व्यास हो । यो वृत्तको सबैभन्दा लामो जीवा हो र अर्धव्यासको दोब्बर हुन्छ ।',
    formula: 'व्यास d = २ × r',
    color: '#f59e0b'
  },
  chord: {
    title: 'जीवा (Chord - EF)',
    badge: 'जीवा (Chord)',
    desc: 'वृत्तको परिधिका कुनै दुई बिन्दुहरूलाई जोड्ने सीधा रेखाखण्डलाई जीवा भनिन्छ । व्यास केन्द्रबिन्दु भएर जाने सबैभन्दा ठूलो जीवा हो ।',
    formula: 'जीवाको लम्बाइ सधैँ व्यासभन्दा सानो वा बराबर हुन्छ (Chord ≤ d)',
    color: '#ec4899'
  },
  sector: {
    title: 'क्षेत्रक (Sector - AOB)',
    badge: 'क्षेत्रक (Sector)',
    desc: 'वृत्तका दुईवटा अर्धव्यासहरू (OA र OB) र तिनीहरूबीचको परिधिको चापले घेरिएको भित्री समतलीय भागलाई क्षेत्रक भनिन्छ (पिज्जाको टुक्रा जस्तो) ।',
    formula: 'क्षेत्रक = दुई अर्धव्यास + १ चाप बीचको क्षेत्र',
    color: '#f43f5e'
  },
  semicircle: {
    title: 'अर्धवृत्त (Semi-circle)',
    badge: 'अर्धवृत्त (Semi-circle)',
    desc: 'व्यासले वृत्तलाई दुई बराबर भागमा विभाजन गर्दा बन्ने आधा वृत्तलाई अर्धवृत्त भनिन्छ । एउटा वृत्तमा २ वटा अर्धवृत्तहरू हुन्छन् ।',
    formula: 'अर्धवृत्तको कोण = १८०°, परिधिको आधा = πr',
    color: '#10b981'
  },
  arc: {
    title: 'चाप (Arc - AB)',
    badge: 'चाप (Arc)',
    desc: 'वृत्तको बाहिरी परिधिको कुनै एउटा परिमित खण्ड वा टुक्रालाई चाप भनिन्छ । सानो भागलाई लघुचाप र ठूलो भागलाई वृहत् चाप भनिन्छ ।',
    formula: 'चाप = परिधिको एक टुक्रा (भाग)',
    color: '#a855f7'
  },
  circumference: {
    title: 'परिधि (Circumference - C)',
    badge: 'परिधि (Circumference)',
    desc: 'वृत्तको वरिपरिको कुल घेरा वा वक्ररेखाको लम्बाइलाई परिधि भनिन्छ ।',
    formula: 'परिधि C = २πr = πd (जहाँ π ≈ २२/७)',
    color: '#38bdf8'
  }
};

function updateCircleLab() {
  const r = circleCurrentRadius;
  // Visual scaling: 7 cm = 120 SVG units -> scale = 120 / 7 ≈ 17.14
  const scale = 17.14;
  const svgR = Math.round(r * scale);
  const cx = 200, cy = 200;

  // Update SVG elements
  const boundary = document.getElementById('circ-boundary');
  if (boundary) boundary.setAttribute('r', svgR);

  // Measurements
  const diam = r * 2;
  const circum = 2 * (22 / 7) * r;
  const area = (22 / 7) * r * r;

  // Live values in UI
  const elR = document.getElementById('live-r-val');
  const elD = document.getElementById('live-d-val');
  const elC = document.getElementById('live-c-val');
  const elA = document.getElementById('live-a-val');
  const sliderLabel = document.getElementById('slider-r-label');
  const measLabel = document.getElementById('circ-meas-label');

  if (elR) elR.textContent = `${r.toFixed(1)} cm`;
  if (elD) elD.textContent = `${diam.toFixed(1)} cm`;
  if (elC) elC.textContent = `${circum.toFixed(1)} cm`;
  if (elA) elA.textContent = `${area.toFixed(1)} cm²`;
  if (sliderLabel) sliderLabel.textContent = `${r.toFixed(1)} cm`;

  // Radius Line OA
  const radLine = document.getElementById('circ-radius-line');
  const nodeA = document.getElementById('circ-node-A');
  const textA = document.getElementById('circ-text-A');
  if (radLine) {
    radLine.setAttribute('x1', cx);
    radLine.setAttribute('y1', cy);
    radLine.setAttribute('x2', cx + svgR);
    radLine.setAttribute('y2', cy);
  }
  if (nodeA) {
    nodeA.setAttribute('cx', cx + svgR);
    nodeA.setAttribute('cy', cy);
  }
  if (textA) {
    textA.setAttribute('x', cx + svgR + 12);
    textA.setAttribute('y', cy + 5);
  }
  if (measLabel) {
    measLabel.setAttribute('x', cx + svgR / 2);
    measLabel.setAttribute('y', cy - 10);
    measLabel.textContent = `r = ${r.toFixed(1)} cm`;
  }

  // Diameter Line CD
  const diamLine = document.getElementById('circ-diam-line');
  const nodeC = document.getElementById('circ-node-C');
  const textC = document.getElementById('circ-text-C');
  const textD = document.getElementById('circ-text-D');
  if (diamLine) {
    diamLine.setAttribute('x1', cx - svgR);
    diamLine.setAttribute('y1', cy);
    diamLine.setAttribute('x2', cx + svgR);
    diamLine.setAttribute('y2', cy);
  }
  if (nodeC) {
    nodeC.setAttribute('cx', cx - svgR);
    nodeC.setAttribute('cy', cy);
  }
  if (textC) {
    textC.setAttribute('x', cx - svgR - 15);
    textC.setAttribute('y', cy + 5);
  }
  if (textD) {
    textD.setAttribute('x', cx + svgR + 12);
    textD.setAttribute('y', cy + 5);
  }

  // Radius OB (for sector, 60 deg angle)
  // angle 60 deg: x = cx + r*cos(-60) = cx + r*0.5, y = cy + r*sin(-60) = cy - r*0.866
  const obX = Math.round(cx + svgR * 0.5);
  const obY = Math.round(cy - svgR * 0.866);
  const radOB = document.getElementById('circ-radius-ob');
  const nodeB = document.getElementById('circ-node-B');
  const textB = document.getElementById('circ-text-B');
  if (radOB) {
    radOB.setAttribute('x1', cx);
    radOB.setAttribute('y1', cy);
    radOB.setAttribute('x2', obX);
    radOB.setAttribute('y2', obY);
  }
  if (nodeB) {
    nodeB.setAttribute('cx', obX);
    nodeB.setAttribute('cy', obY);
  }
  if (textB) {
    textB.setAttribute('x', obX + 10);
    textB.setAttribute('y', obY - 5);
  }

  // Sector Path (from OA to OB)
  const sector = document.getElementById('circ-sector');
  if (sector) {
    sector.setAttribute('d', `M ${cx} ${cy} L ${cx + svgR} ${cy} A ${svgR} ${svgR} 0 0 0 ${obX} ${obY} Z`);
  }

  // Arc Path (from OA to OB)
  const arcPath = document.getElementById('circ-arc-path');
  if (arcPath) {
    arcPath.setAttribute('d', `M ${cx + svgR} ${cy} A ${svgR} ${svgR} 0 0 0 ${obX} ${obY}`);
  }

  // Semicircle Path (from -svgR to +svgR)
  const semi = document.getElementById('circ-semicircle');
  if (semi) {
    semi.setAttribute('d', `M ${cx - svgR} ${cy} A ${svgR} ${svgR} 0 0 1 ${cx + svgR} ${cy} Z`);
  }

  // Chord EF (horizontal chord at cy + svgR*0.6)
  const chordLine = document.getElementById('circ-chord-line');
  const nodeE = document.getElementById('circ-node-E');
  const textE = document.getElementById('circ-text-E');
  const nodeF = document.getElementById('circ-node-F');
  const textF = document.getElementById('circ-text-F');
  const chordY = cy + Math.round(svgR * 0.6);
  const chordHalfW = Math.round(Math.sqrt(svgR * svgR - (chordY - cy) * (chordY - cy)));
  if (chordLine) {
    chordLine.setAttribute('x1', cx - chordHalfW);
    chordLine.setAttribute('y1', chordY);
    chordLine.setAttribute('x2', cx + chordHalfW);
    chordLine.setAttribute('y2', chordY);
  }
  if (nodeE) {
    nodeE.setAttribute('cx', cx - chordHalfW);
    nodeE.setAttribute('cy', chordY);
  }
  if (textE) {
    textE.setAttribute('x', cx - chordHalfW - 15);
    textE.setAttribute('y', chordY + 10);
  }
  if (nodeF) {
    nodeF.setAttribute('cx', cx + chordHalfW);
    nodeF.setAttribute('cy', chordY);
  }
  if (textF) {
    textF.setAttribute('x', cx + chordHalfW + 12);
    textF.setAttribute('y', chordY + 10);
  }

  // Update info card formula
  const infoFormula = document.getElementById('part-info-formula');
  if (infoFormula) {
    if (circleCurrentPart === 'radius') {
      infoFormula.textContent = `अर्धव्यास r = ${r.toFixed(1)} cm ⟹ व्यास d = ${diam.toFixed(1)} cm`;
    } else if (circleCurrentPart === 'diameter') {
      infoFormula.textContent = `व्यास d = ${diam.toFixed(1)} cm ⟹ अर्धव्यास r = ${r.toFixed(1)} cm`;
    } else if (circleCurrentPart === 'circumference') {
      infoFormula.textContent = `परिधि C = २ × (२२/७) × ${r.toFixed(1)} = ${circum.toFixed(1)} cm`;
    }
  }
}

function highlightCirclePart(part) {
  circleCurrentPart = part;
  const conf = circlePartDetails[part];
  if (!conf) return;

  // Update badge and info card
  const badge = document.getElementById('circle-part-badge');
  const title = document.getElementById('part-info-title');
  const desc = document.getElementById('part-info-desc');
  if (badge) badge.textContent = conf.badge;
  if (title) title.textContent = conf.title;
  if (desc) desc.textContent = conf.desc;

  // Update button highlights
  const parts = ['centre', 'radius', 'diameter', 'chord', 'sector', 'semicircle', 'arc', 'circumference'];
  parts.forEach(p => {
    const btn = document.getElementById('pbtn-' + p);
    if (btn) {
      if (p === part) {
        btn.className = 'p-2 rounded-xl bg-blue-600 text-white transition text-left font-semibold border border-blue-500 shadow-sm';
      } else {
        btn.className = 'p-2 rounded-xl bg-slate-800 hover:bg-slate-700 transition text-left font-semibold border border-slate-700 text-slate-300';
      }
    }
  });

  // Toggle visibility of SVG elements
  const elBoundary = document.getElementById('circ-boundary');
  const elDiam = document.getElementById('circ-diam-line');
  const elRad = document.getElementById('circ-radius-line');
  const elRadOB = document.getElementById('circ-radius-ob');
  const elChord = document.getElementById('circ-chord-line');
  const elSector = document.getElementById('circ-sector');
  const elSemi = document.getElementById('circ-semicircle');
  const elArc = document.getElementById('circ-arc-path');
  const nodeB = document.getElementById('circ-node-B');
  const textB = document.getElementById('circ-text-B');
  const nodeC = document.getElementById('circ-node-C');
  const textC = document.getElementById('circ-text-C');
  const textD = document.getElementById('circ-text-D');
  const nodeE = document.getElementById('circ-node-E');
  const textE = document.getElementById('circ-text-E');
  const nodeF = document.getElementById('circ-node-F');
  const textF = document.getElementById('circ-text-F');
  const measLabel = document.getElementById('circ-meas-label');

  // Reset styles
  if (elDiam) elDiam.style.display = 'none';
  if (elRad) elRad.style.display = 'none';
  if (elRadOB) elRadOB.style.display = 'none';
  if (elChord) elChord.style.display = 'none';
  if (elSector) elSector.style.display = 'none';
  if (elSemi) elSemi.style.display = 'none';
  if (elArc) elArc.style.display = 'none';
  if (nodeB) nodeB.style.display = 'none';
  if (textB) textB.style.display = 'none';
  if (nodeC) nodeC.style.display = 'none';
  if (textC) textC.style.display = 'none';
  if (textD) textD.style.display = 'none';
  if (nodeE) nodeE.style.display = 'none';
  if (textE) textE.style.display = 'none';
  if (nodeF) nodeF.style.display = 'none';
  if (textF) textF.style.display = 'none';

  if (part === 'centre') {
    if (elBoundary) elBoundary.setAttribute('stroke', '#38bdf8');
  } else if (part === 'radius') {
    if (elRad) elRad.style.display = 'block';
  } else if (part === 'diameter') {
    if (elDiam) elDiam.style.display = 'block';
    if (nodeC) nodeC.style.display = 'block';
    if (textC) textC.style.display = 'block';
    if (textD) textD.style.display = 'block';
  } else if (part === 'chord') {
    if (elChord) elChord.style.display = 'block';
    if (nodeE) nodeE.style.display = 'block';
    if (textE) textE.style.display = 'block';
    if (nodeF) nodeF.style.display = 'block';
    if (textF) textF.style.display = 'block';
  } else if (part === 'sector') {
    if (elSector) elSector.style.display = 'block';
    if (elRad) elRad.style.display = 'block';
    if (elRadOB) elRadOB.style.display = 'block';
    if (nodeB) nodeB.style.display = 'block';
    if (textB) textB.style.display = 'block';
  } else if (part === 'semicircle') {
    if (elSemi) elSemi.style.display = 'block';
    if (elDiam) elDiam.style.display = 'block';
  } else if (part === 'arc') {
    if (elArc) elArc.style.display = 'block';
    if (nodeB) nodeB.style.display = 'block';
    if (textB) textB.style.display = 'block';
  } else if (part === 'circumference') {
    if (elBoundary) elBoundary.setAttribute('stroke', '#ec4899');
  }

  updateCircleLab();
}

function onCircleRadiusSliderChange() {
  const slider = document.getElementById('slider-circle-r');
  if (slider) {
    circleCurrentRadius = parseFloat(slider.value);
    updateCircleLab();
  }
}

function setCircleRadiusPreset(r) {
  circleCurrentRadius = r;
  const slider = document.getElementById('slider-circle-r');
  if (slider) slider.value = r;
  updateCircleLab();
}

// --- SUB-LAB 2: WHEEL ROTATION LAB ---
function onWheelChange() {
  const sel = document.getElementById('wheel-radius-select');
  const inp = document.getElementById('wheel-rot-input');
  if (!sel || !inp) return;

  const r = parseFloat(sel.value);
  const n = Math.max(1, parseInt(inp.value) || 1);

  // Circumference
  const c = Math.round(2 * (22 / 7) * r);
  const totalDistCm = n * c;
  const totalDistM = (totalDistCm / 100).toFixed(2);

  const statC = document.getElementById('wheel-stat-c');
  const statCm = document.getElementById('wheel-stat-dist-cm');
  const statM = document.getElementById('wheel-stat-dist-m');
  const calcTotal = document.getElementById('wheel-calc-total');
  const badge = document.getElementById('wheel-rot-badge');
  const distLabel = document.getElementById('wheel-dist-label');

  if (statC) statC.textContent = `${c} cm`;
  if (statCm) statCm.textContent = `${totalDistCm} cm`;
  if (statM) statM.textContent = `${totalDistM} m`;
  if (calcTotal) calcTotal.textContent = `${totalDistCm} cm (${totalDistM} m)`;
  if (badge) badge.textContent = `${n} फन्को (${n} Rotation${n > 1 ? 's' : ''})`;
  if (distLabel) distLabel.textContent = `दूरी = ${totalDistCm} cm`;
}

function setWheelRotations(n) {
  const inp = document.getElementById('wheel-rot-input');
  if (inp) {
    inp.value = n;
    onWheelChange();
  }
}

// --- CHAPTER 16 QUIZ DATA & ENGINE ---
const ch16QuizData = [
  {
    q: '१. वृत्तको सबैभन्दा लामो जीवा कुन हो ?',
    opts: ['अर्धव्यास', 'व्यास', 'चाप', 'स्पर्शरेखा'],
    ans: 1,
    exp: 'केन्द्रबिन्दु भएर जाने जीवा नै वृत्तको सबैभन्दा लामो जीवा हो, जसलाई व्यास (Diameter) भनिन्छ ।'
  },
  {
    q: '२. एउटा वृत्तमा कतिवटा केन्द्रबिन्दु हुन्छन् ?',
    opts: ['१ वटा', '२ वटा', '४ वटा', 'अनगिन्ती'],
    ans: 0,
    exp: 'वृत्तको ठीक बीचमा एउटा मात्र निश्चित केन्द्रबिन्दु हुन्छ ।'
  },
  {
    q: '३. व्यास (d) र अर्धव्यास (r) बीचको सम्बन्ध कुन सही हो ?',
    opts: ['d = r', 'd = 2r', 'r = 2d', 'd = r ÷ 2'],
    ans: 1,
    exp: 'व्यास अर्धव्यासको ठ्याक्कै दोब्बर हुन्छ: d = 2r वा r = d/2 ।'
  },
  {
    q: '४. वृत्तका दुई अर्धव्यास र चापले घेरिएको भागलाई के भनिन्छ ?',
    opts: ['जीवा', 'वृत्तखण्ड', 'क्षेत्रक (Sector)', 'अर्धवृत्त'],
    ans: 2,
    exp: 'दुईवटा अर्धव्यासहरू र तिनीहरूबीचको चापले घेरिएको भित्री क्षेत्रलाई क्षेत्रक भनिन्छ ।'
  },
  {
    q: '५. वृत्तको वरिपरिको कुल घेरा वा वक्ररेखाको लम्बाइलाई के भनिन्छ ?',
    opts: ['व्यास', 'अर्धव्यास', 'परिधि (Circumference)', 'चाप'],
    ans: 2,
    exp: 'वृत्तको वरिपरिको घेराको लम्बाइ परिधि (Circumference) हो ।'
  },
  {
    q: '६. अर्धव्यास ७ से.मी. भएको वृत्तको परिधि कति हुन्छ ? (π = २२/७)',
    opts: ['२२ से.मी.', '४४ से.मी.', '८८ से.मी.', '१५४ से.मी.'],
    ans: 1,
    exp: 'C = 2πr = 2 × (22/7) × 7 = 44 cm हुन्छ ।'
  },
  {
    q: '७. व्यास १४ से.मी. भएको वृत्तको अर्धव्यास कति हुन्छ ?',
    opts: ['७ से.मी.', '१४ से.मी.', '२८ से.मी.', '४४ से.मी.'],
    ans: 0,
    exp: 'अर्धव्यास r = d ÷ 2 = 14 ÷ 2 = 7 cm हुन्छ ।'
  },
  {
    q: '८. वृत्तको परिधि र त्यसको व्यासको अनुपातलाई के भनिन्छ ?',
    opts: ['क्षेत्रफल', 'π (पाइ)', 'अर्धव्यास', 'जीवा'],
    ans: 1,
    exp: 'परिधि र व्यासको अनुपात स्थिर सङ्ख्या π (पाइ ≈ २२/७) हुन्छ ।'
  },
  {
    q: '९. एउटा व्यासले वृत्तलाई कतिवटा अर्धवृत्तमा विभाजन गर्दछ ?',
    opts: ['१ वटा', '२ वटा', '३ वटा', '४ वटा'],
    ans: 1,
    exp: 'व्यासले वृत्तलाई ठ्याक्कै दुई बराबर भाग (अर्धवृत्तहरू) मा विभाजन गर्दछ ।'
  },
  {
    q: '१०. साइकलको पाङ्ग्रा १ फन्को घुम्दा पार गर्ने दूरी कुन नापसँग बराबर हुन्छ ?',
    opts: ['व्यास', 'अर्धव्यास', 'पाङ्ग्राको परिधि', 'पाङ्ग्राको क्षेत्रफल'],
    ans: 2,
    exp: 'पाङ्ग्रा १ पटक पूरा घुम्दा त्यसको बाहिरी घेरा अर्थात् परिधि (2πr) बराबर दूरी पार गर्दछ ।'
  }
];

let ch16QuizAnswers = {};

function renderCh16Quiz() {
  const container = document.getElementById('ch16-quiz-container');
  if (!container) return;

  container.innerHTML = ch16QuizData
    .map((item, qIdx) => {
      const isAnswered = ch16QuizAnswers.hasOwnProperty(qIdx);
      const selected = ch16QuizAnswers[qIdx];
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
            <button onclick="handleCh16QuizAnswer(${qIdx}, ${optIdx})" class="${btnClass}">
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

  updateCh16QuizScore();
}

function handleCh16QuizAnswer(qIdx, optIdx) {
  if (ch16QuizAnswers.hasOwnProperty(qIdx)) return;
  ch16QuizAnswers[qIdx] = optIdx;
  renderCh16Quiz();
}

function updateCh16QuizScore() {
  let score = 0;
  Object.keys(ch16QuizAnswers).forEach(qIdx => {
    if (ch16QuizAnswers[qIdx] === ch16QuizData[qIdx].ans) {
      score++;
    }
  });
  const el = document.getElementById('ch16-quiz-score');
  if (el) el.textContent = score;
}

function resetCh16Quiz() {
  ch16QuizAnswers = {};
  renderCh16Quiz();
}

// Initialise Chapter 16 when DOM loads
document.addEventListener('DOMContentLoaded', () => {
  updateCircleLab();
});
