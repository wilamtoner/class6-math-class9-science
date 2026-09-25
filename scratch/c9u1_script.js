// ================= CLASS 9 UNIT 1: SCIENTIFIC STUDY SCRIPT =================

// Tab Switching
function setTabC9U1(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const view = document.getElementById(`c9u1-view-${t}`);
    const btn = document.getElementById(`c9u1-tab-${t}`);
    if (view) {
      if (t === tab) {
        view.classList.remove('hidden');
      } else {
        view.classList.add('hidden');
      }
    }
    if (btn) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-cyan-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
      }
    }
  });
  if (tab === 'quiz') {
    renderC9U1Quiz();
  }
}

// Virtual Lab Mode Switcher
function switchC9U1Lab(mode) {
  const modes = ['notation', 'leastcount', 'inquiry'];
  modes.forEach(m => {
    const container = document.getElementById(`c9u1-lab-mode-${m}`);
    const btn = document.getElementById(`c9u1-lab-btn-${m}`);
    if (container) {
      if (m === mode) {
        container.classList.remove('hidden');
      } else {
        container.classList.add('hidden');
      }
    }
    if (btn) {
      if (m === mode) {
        btn.className = 'px-3.5 py-2 rounded-xl text-xs font-black transition bg-cyan-600 text-white shadow-sm cursor-pointer';
      } else {
        btn.className = 'px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-300 hover:text-white cursor-pointer';
      }
    }
  });
  if (mode === 'leastcount') {
    selectC9U1Instrument('ruler');
  }
}

// Convert English numbers to Nepali numerals
function toNepaliNumC9(numStr) {
  const nep = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
  return String(numStr).replace(/[0-9]/g, d => nep[parseInt(d, 10)]);
}

// Mode 1: Scientific Notation Converter
function calculateScientificNotation() {
  const inputEl = document.getElementById('c9u1-num-input');
  if (!inputEl) return;
  let raw = inputEl.value.trim().replace(/,/g, '');
  if (!raw || isNaN(raw) || Number(raw) === 0) {
    document.getElementById('c9u1-res-notation').textContent = 'अमान्य वा शून्य';
    document.getElementById('c9u1-res-eng').textContent = 'Enter valid non-zero number';
    return;
  }

  const num = parseFloat(raw);
  const expStr = num.toExponential();
  const parts = expStr.split('e');
  let m = parseFloat(parts[0]);
  let n = parseInt(parts[1], 10);

  // Format M to reasonable decimals
  let mStr = m.toString();
  if (mStr.length > 7) {
    mStr = m.toFixed(4).replace(/\.?0+$/, '');
  }

  const nepM = toNepaliNumC9(mStr);
  const nepN = toNepaliNumC9(Math.abs(n));
  const signSymbol = n >= 0 ? '' : '-';
  const nepSign = n >= 0 ? '' : '-';

  const resNotation = document.getElementById('c9u1-res-notation');
  const resEng = document.getElementById('c9u1-res-eng');
  const resM = document.getElementById('c9u1-res-m');
  const resN = document.getElementById('c9u1-res-n');
  const resShift = document.getElementById('c9u1-res-shift');
  const resSig = document.getElementById('c9u1-res-sig');

  if (resNotation) resNotation.textContent = `${nepM} × १०^${nepSign}${nepN}`;
  if (resEng) resEng.textContent = `${mStr} × 10^(${signSymbol}${Math.abs(n)})`;
  if (resM) resM.textContent = `${mStr} (${nepM})`;
  if (resN) resN.textContent = (n >= 0 ? `+${n}` : `${n}`) + ` (${toNepaliNumC9(n)})`;

  if (resShift) {
    if (n > 0) {
      resShift.textContent = `बायाँतर्फ ${toNepaliNumC9(n)} स्थान (धनात्मक घाताङ्क)`;
    } else if (n < 0) {
      resShift.textContent = `दायाँतर्फ ${toNepaliNumC9(Math.abs(n))} स्थान (ऋणात्मक घाताङ्क)`;
    } else {
      resShift.textContent = `दशमलव सार्न नपर्ने (घाताङ्क ०)`;
    }
  }

  if (resSig) {
    // Count significant figures in mStr
    const cleanDigits = mStr.replace('.', '');
    resSig.textContent = `${toNepaliNumC9(cleanDigits.length)} वटा (${cleanDigits.split('').join(', ')})`;
  }
}

function setC9U1Preset(val) {
  const inputEl = document.getElementById('c9u1-num-input');
  if (inputEl) {
    inputEl.value = val;
    calculateScientificNotation();
  }
}

// Mode 2: Least Count Lab
const c9u1Instruments = {
  ruler: {
    title: 'साधारण मिटर स्केल (Meter Scale)',
    badge: 'LC = 1 mm (0.1 cm)',
    reading: '३.७ cm (३७ mm)',
    desc: '१ सेन्टिमिटरलाई १० बराबर साना भागहरूमा बाँडिएको हुन्छ। १ सानो भाग = ०.१ cm = १ mm। १ mm भन्दा सानो नाप यसले सिधै लिन सक्दैन।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="20" y="30" width="460" height="70" fill="#fef08a" stroke="#ca8a04" stroke-width="2" rx="6"/>
        <!-- Main markings: 0 to 5 cm -->
        ${Array.from({length: 6}).map((_, i) => `
          <line x1="${50 + i * 75}" y1="30" x2="${50 + i * 75}" y2="70" stroke="#713f12" stroke-width="2"/>
          <text x="${50 + i * 75}" y="92" fill="#713f12" font-size="14" font-weight="bold" text-anchor="middle">${i}</text>
          <!-- 10 mm subdivisions -->
          ${i < 5 ? Array.from({length: 9}).map((_, j) => `
            <line x1="${50 + i * 75 + (j + 1) * 7.5}" y1="30" x2="${50 + i * 75 + (j + 1) * 7.5}" y2="${j === 4 ? 58 : 46}" stroke="#854d0e" stroke-width="${j === 4 ? 1.5 : 1}"/>
          `).join('') : ''}
        `).join('')}
        <!-- Reading Indicator arrow at 3.7 cm = 50 + 3*75 + 7*7.5 = 327.5 -->
        <polygon points="327.5,10 322,0 333,0" fill="#ef4444"/>
        <line x1="327.5" y1="10" x2="327.5" y2="75" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>
        <text x="327.5" y="125" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">३.७ cm (न्यूनतम नाप १ mm)</text>
      `;
    }
  },
  stopwatch: {
    title: 'डिजिटल स्टपवाच (Digital Stopwatch)',
    badge: 'LC = 0.01 s (१ सेन्टीसेकेन्ड)',
    reading: '०.६३ s (१०० भागको ६३ भाग)',
    desc: 'डिजिटल स्टपवाचले १ सेकेन्डलाई १०० बराबर भागमा विभाजन गर्छ। यसको न्यूनतम नाप ०.०१ सेकेन्ड (१/१०० s) हुन्छ।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="140" y="20" width="220" height="110" rx="20" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
        <rect x="160" y="40" width="180" height="50" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
        <text x="250" y="75" fill="#38bdf8" font-size="28" font-weight="bold" font-family="monospace" text-anchor="middle">00 : 00 . 63</text>
        <text x="250" y="115" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">न्यूनतम नाप = ०.०१ सेकेन्ड</text>
        <!-- Buttons on top -->
        <rect x="180" y="8" width="30" height="12" rx="4" fill="#64748b"/>
        <rect x="290" y="8" width="30" height="12" rx="4" fill="#64748b"/>
      `;
    }
  },
  ammeter: {
    title: 'माइक्रो-एमिटर (Microammeter - क्रियाकलाप १.५)',
    badge: 'LC = 1 μA',
    reading: '२४ μA',
    desc: '० देखि ५० μA नाप्ने मिटरमा ० देखि १० सम्म १० वटा साना खण्ड हुन्छन्। त्यसैले १ सानो खण्ड = १०/१० = १ μA हुन्छ।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="100" y="15" width="300" height="125" rx="16" fill="#18181b" stroke="#71717a" stroke-width="2"/>
        <path d="M 130 90 A 120 120 0 0 1 370 90" fill="none" stroke="#e4e4e7" stroke-width="2"/>
        <!-- Ticks for 0, 10, 20, 30, 40, 50 -->
        <text x="140" y="105" fill="#e4e4e7" font-size="11" font-weight="bold">0</text>
        <text x="180" y="65" fill="#e4e4e7" font-size="11" font-weight="bold">10</text>
        <text x="245" y="48" fill="#e4e4e7" font-size="11" font-weight="bold">25</text>
        <text x="310" y="65" fill="#e4e4e7" font-size="11" font-weight="bold">40</text>
        <text x="350" y="105" fill="#e4e4e7" font-size="11" font-weight="bold">50</text>
        <text x="250" y="90" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">μA</text>
        <!-- Needle pointing to 24 -->
        <line x1="250" y1="120" x2="242" y2="45" stroke="#ef4444" stroke-width="2"/>
        <circle cx="250" cy="120" r="5" fill="#ef4444"/>
      `;
    }
  },
  cylinder: {
    title: 'मेजरिङ सिलिन्डर (Measuring Cylinder - क्रियाकलाप १.५)',
    badge: 'LC = 1 mL',
    reading: '३२ mL',
    desc: '० देखि ५० mL सिलिन्डरमा प्रत्येक १० mL बीचमा १० वटा साना खण्डहरू हुन्छन्। १ खण्ड = १०/१० = १ mL हुन्छ।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="210" y="20" width="80" height="120" fill="none" stroke="#67e8f9" stroke-width="2" rx="4"/>
        <!-- Water level at 32 ml (height ~ 70px) -->
        <rect x="212" y="60" width="76" height="78" fill="rgba(6, 182, 212, 0.35)"/>
        <!-- Graduation lines -->
        ${Array.from({length: 6}).map((_, i) => `
          <line x1="210" y1="${135 - i * 22}" x2="235" y2="${135 - i * 22}" stroke="#67e8f9" stroke-width="2"/>
          <text x="242" y="${139 - i * 22}" fill="#67e8f9" font-size="10" font-weight="bold">${i * 10}</text>
        `).join('')}
        <text x="310" y="70" fill="#38bdf8" font-size="12" font-weight="bold">तरलको सतह = ३२ mL</text>
      `;
    }
  }
};

function selectC9U1Instrument(type) {
  const conf = c9u1Instruments[type];
  if (!conf) return;

  const btns = ['ruler', 'stopwatch', 'ammeter', 'cylinder'];
  btns.forEach(b => {
    const btn = document.getElementById(`btn-inst-${b}`);
    if (btn) {
      if (b === type) {
        btn.className = 'w-full text-left p-3.5 rounded-2xl transition border border-cyan-500 bg-cyan-950/40 text-cyan-200 font-bold text-xs flex justify-between items-center cursor-pointer';
      } else {
        btn.className = 'w-full text-left p-3.5 rounded-2xl transition border border-slate-700 bg-slate-800 text-slate-300 hover:text-white font-bold text-xs flex justify-between items-center cursor-pointer';
      }
    }
  });

  const svg = document.getElementById('c9u1-inst-svg');
  if (svg) conf.render(svg);

  const readingEl = document.getElementById('c9u1-inst-reading');
  const titleEl = document.getElementById('c9u1-inst-title');
  const badgeEl = document.getElementById('c9u1-inst-badge');
  const descEl = document.getElementById('c9u1-inst-desc');

  if (readingEl) readingEl.textContent = conf.reading;
  if (titleEl) titleEl.textContent = conf.title;
  if (badgeEl) badgeEl.textContent = conf.badge;
  if (descEl) descEl.textContent = conf.desc;
}

// Mode 3: Simulation Trial
function runC9U1InquiryTrial() {
  const t1 = (0.61 + Math.random() * 0.05).toFixed(2);
  const t2 = (0.63 + Math.random() * 0.05).toFixed(2);
  const t3 = (0.61 + Math.random() * 0.04).toFixed(2);
  const avg = ((parseFloat(t1) + parseFloat(t2) + parseFloat(t3)) / 3).toFixed(2);

  const el1 = document.getElementById('c9u1-trial-1');
  const el2 = document.getElementById('c9u1-trial-2');
  const el3 = document.getElementById('c9u1-trial-3');

  if (el1) el1.textContent = `${toNepaliNumC9(t1)} s`;
  if (el2) el2.textContent = `${toNepaliNumC9(t2)} s`;
  if (el3) el3.textContent = `${toNepaliNumC9(t3)} s`;
}

// Exercise Sub-filter
function filterC9U1Ex(group) {
  const groups = ['all', 'mcq', 'theory', 'math', 'activity'];
  groups.forEach(g => {
    const btn = document.getElementById(`btn-c9u1-filter-${g}`);
    if (btn) {
      if (g === group) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-xs cursor-pointer';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-600 hover:bg-slate-100 border border-slate-200 cursor-pointer';
      }
    }
  });

  const cards = document.querySelectorAll('.c9u1-ex-group');
  cards.forEach(c => {
    const cGroup = c.getAttribute('data-group');
    if (group === 'all' || cGroup === group) {
      c.style.display = '';
    } else {
      c.style.display = 'none';
    }
  });
}

// Tiered Questions Filter
function filterC9U1Tiers(tier) {
  const tiers = ['all', 'k', 'u', 'ha'];
  tiers.forEach(t => {
    const btn = document.getElementById(`btn-c9u1-tier-${t}`);
    if (btn) {
      if (t === tier) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-xs cursor-pointer';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-600 hover:bg-slate-100 border border-slate-200 cursor-pointer';
      }
    }
  });

  const sections = document.querySelectorAll('.c9u1-tier-section');
  sections.forEach(s => {
    const sTier = s.getAttribute('data-tier');
    if (tier === 'all' || sTier === tier) {
      s.style.display = '';
    } else {
      s.style.display = 'none';
    }
  });
}

// Quiz Questions Data (10 Questions)
const c9u1QuizData = [
  {
    q: '१. भेटेनरी पेसा विज्ञानको कुन शाखासँग प्रत्यक्ष सम्बन्धित छ?',
    options: ['भौतिक विज्ञान', 'जीव विज्ञान', 'रसायन विज्ञान', 'भू विज्ञान'],
    ans: 1,
    exp: 'भेटेनरी पेसा जनावर तथा पशुपक्षीहरूको स्वास्थ्य, रोग निदान र उपचारसँग सम्बन्धित भएकाले जीव विज्ञानअन्तर्गत पर्छ।'
  },
  {
    q: '२. आनुवंशिकी वा वंशाणुशास्त्रका पिता (Father of Genetics) कसलाई मानिन्छ?',
    options: ['सर आइज्याक न्युटन', 'जोन डाल्टन', 'ग्रेगर जोन मेन्डेल', 'दिमित्रि मेन्डेलिभ'],
    ans: 2,
    exp: 'ग्रेगर मेन्डेलले केराउको बोटमा अध्ययन गरी वंशाणुगत गुण सर्ने नियमहरू प्रतिपादन गरेका थिए।'
  },
  {
    q: '३. साधारण मिटर स्केलको प्रयोग गरी नाप्दा लिइने न्यूनतम नाप (Least Count) कति हुन्छ?',
    options: ['१ सेन्टिमिटर (१ cm)', '१ मिलिमिटर (०.१ cm)', '०.०१ मिलिमिटर', '१ मिटर'],
    ans: 1,
    exp: 'साधारण स्केलको १ सानो खण्ड = १/१० cm = ०.१ cm = १ mm हुन्छ।'
  },
  {
    q: '४. 0.000024 अङ्कलाई वैज्ञानिक सङ्केतन (Scientific Notation) मा कसरी लेखिन्छ?',
    options: ['२.४ × १०⁻⁵', '२४ × १०⁻⁵', '०.२४ × १०⁻⁶', '२ × १०⁻⁵'],
    ans: 0,
    exp: 'दशमलव ५ स्थान दायाँ सार्दा पहिलो गैर-शून्य अङ्कपछि २.४ बन्छ र १० को घाताङ्क -५ हुन्छ।'
  },
  {
    q: '५. गिगा (Giga) मेट्रिक उपसर्गको गुणक मान कति हुन्छ?',
    options: ['१०⁶', '१०⁹', '१०¹²', '१०⁻⁹'],
    ans: 1,
    exp: 'गिगा (Giga - G) = १०⁹ (अर्थात् १ अर्ब) हुन्छ।'
  },
  {
    q: '६. डा. सन्दुक रुइतले विकास गरेको इन्ट्राअकुलर लेन्स (IOL) कुन दुई क्षेत्रको अन्तरसम्बन्ध हो?',
    options: ['जीव विज्ञान र भौतिक विज्ञान (बायोफिजिक्स)', 'रसायन र भू-विज्ञान', 'भौतिक र खगोल विज्ञान', 'जीव विज्ञान र वातावरण विज्ञान'],
    ans: 0,
    exp: 'भौतिक विज्ञानको प्रकाश/लेन्सको सिद्धान्त र जीव विज्ञानको आँखाको शल्यक्रिया मिलेर बायोफिजिक्स/चिकित्सा विज्ञान बनेको छ।'
  },
  {
    q: '७. कुनै उपकरणले सही रूपमा नाप्न सक्ने सबैभन्दा सानो परिमाणलाई के भनिन्छ?',
    options: ['अधिकतम नाप', 'औसत नाप', 'न्यूनतम नाप (Least Count)', 'सार्थक अङ्क'],
    ans: 2,
    exp: 'कुनै पनि यन्त्रले सही रूपमा मापन गर्न सक्ने लघुतम परिमाणलाई त्यसको न्यूनतम नाप (Least Count) भनिन्छ।'
  },
  {
    q: '८. १ माइक्रोमिटर (1 μm) कति मिटर बराबर हुन्छ?',
    options: ['१०⁻³ मिटर', '१०⁻⁶ मिटर', '१०⁻⁹ मिटर', '१०⁻¹² मिटर'],
    ans: 1,
    exp: 'माइक्रो (Micro - μ) = १०⁻⁶ (मिटरको दश लाखौं भाग) हुन्छ।'
  },
  {
    q: '९. वैज्ञानिक पद्धतिमा कुनै परिकल्पना (Hypothesis) को सत्यता प्रमाणित गर्ने मुख्य आधार के हो?',
    options: ['अनुमान', 'प्रयोग (Experiment)', 'छलफल', 'पुस्तक अध्ययन'],
    ans: 1,
    exp: 'वैज्ञानिक पद्धतिमा प्रयोगबिना कुनै पनि परिकल्पना प्रमाणित मानिँदैन।'
  },
  {
    q: '१०. रासायनिक प्रयोगशालामा कडा अम्ल वा क्षारको बोतलमा कुन खतराको सङ्केत (Hazard Symbol) हुन्छ?',
    options: ['ज्वलनशील (Flammable)', 'संक्षारक (Corrosive)', 'विस्फोटक (Explosive)', 'जैविक जोखिम (Biohazard)'],
    ans: 1,
    exp: 'कडा अम्ल वा क्षारले छाला र धातु जलाउने/खियाउने हुँदा संक्षारक (Corrosive) सङ्केत राखिन्छ।'
  }
];

let c9u1QuizAnswers = {};

function renderC9U1Quiz() {
  const container = document.getElementById('c9u1-quiz-container');
  if (!container) return;

  container.innerHTML = c9u1QuizData.map((item, qIdx) => {
    const selected = c9u1QuizAnswers[qIdx];
    return `
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3">
        <div class="font-bold text-slate-800 text-sm md:text-base">${item.q}</div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
          ${item.options.map((opt, optIdx) => {
            let btnClass = 'p-3 rounded-xl border border-slate-200 text-left font-medium transition cursor-pointer hover:bg-slate-50';
            let icon = '';
            if (selected !== undefined) {
              if (optIdx === item.ans) {
                btnClass = 'p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
                icon = ' ✓';
              } else if (optIdx === selected) {
                btnClass = 'p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900 font-bold';
                icon = ' ✗';
              } else {
                btnClass = 'p-3 rounded-xl border border-slate-200 text-slate-400 opacity-60';
              }
            }
            return `
              <button onclick="checkC9U1Quiz(${qIdx}, ${optIdx})" class="${btnClass}" ${selected !== undefined ? 'disabled' : ''}>
                ${opt}${icon}
              </button>
            `;
          }).join('')}
        </div>
        ${selected !== undefined ? `
          <div class="text-xs p-3 rounded-xl ${selected === item.ans ? 'bg-emerald-50 text-emerald-800 border border-emerald-200' : 'bg-rose-50 text-rose-800 border border-rose-200'}">
            <strong>${selected === item.ans ? 'सबास! सही उत्तर।' : 'गलत उत्तर।'}</strong> ${item.exp}
          </div>
        ` : ''}
      </div>
    `;
  }).join('');

  // Update Score
  let score = 0;
  Object.keys(c9u1QuizAnswers).forEach(k => {
    if (c9u1QuizAnswers[k] === c9u1QuizData[k].ans) score++;
  });
  const scoreBadge = document.getElementById('c9u1-quiz-score-badge');
  if (scoreBadge) {
    scoreBadge.textContent = `${toNepaliNumC9(score)} / १०`;
  }
}

function checkC9U1Quiz(qIdx, optIdx) {
  if (c9u1QuizAnswers[qIdx] !== undefined) return;
  c9u1QuizAnswers[qIdx] = optIdx;
  renderC9U1Quiz();
}

function resetC9U1Quiz() {
  c9u1QuizAnswers = {};
  renderC9U1Quiz();
}
