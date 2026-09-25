// ==========================================
// UNIT 6: Nature and Environment - Logic
// ==========================================

let c9u6AudioCtx = null;
function playAudioC9U6(type) {
  try {
    if (!c9u6AudioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) c9u6AudioCtx = new AudioContext();
    }
    if (!c9u6AudioCtx) return;
    if (c9u6AudioCtx.state === 'suspended') c9u6AudioCtx.resume();

    const t = c9u6AudioCtx.currentTime;
    const osc = c9u6AudioCtx.createOscillator();
    const gain = c9u6AudioCtx.createGain();
    osc.connect(gain);
    gain.connect(c9u6AudioCtx.destination);

    if (type === 'click') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, t);
      osc.frequency.exponentialRampToValueAtTime(800, t + 0.05);
      gain.gain.setValueAtTime(0.1, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.06);
      osc.start(t);
      osc.stop(t + 0.06);
    } else if (type === 'energy_transfer') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(300, t);
      osc.frequency.linearRampToValueAtTime(500, t + 0.2);
      gain.gain.setValueAtTime(0.1, t);
      gain.gain.linearRampToValueAtTime(0, t + 0.3);
      osc.start(t);
      osc.stop(t + 0.3);
    } else if (type === 'cascade_alert') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(150, t);
      osc.frequency.linearRampToValueAtTime(100, t + 0.4);
      gain.gain.setValueAtTime(0.15, t);
      gain.gain.linearRampToValueAtTime(0, t + 0.5);
      osc.start(t);
      osc.stop(t + 0.5);
    } else if (type === 'correct') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(400, t);
      osc.frequency.setValueAtTime(600, t + 0.1);
      gain.gain.setValueAtTime(0.1, t);
      gain.gain.linearRampToValueAtTime(0, t + 0.3);
      osc.start(t);
      osc.stop(t + 0.3);
    } else if (type === 'wrong') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(200, t);
      osc.frequency.exponentialRampToValueAtTime(100, t + 0.2);
      gain.gain.setValueAtTime(0.1, t);
      gain.gain.linearRampToValueAtTime(0, t + 0.2);
      osc.start(t);
      osc.stop(t + 0.2);
    }
  } catch (e) {}
}

function toNepaliNumC9U6(num) {
  const nepaliDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
  return num.toString().split('').map(d => nepaliDigits[d] || d).join('');
}

// ------------------------------------------
// Tab Logic
// ------------------------------------------
function switchTabC9U6(tab) {
  playAudioC9U6('click');
  const tabs = ['theory', 'exercise', 'qa', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById(`c9u6-tab-${t}`);
    const content = document.getElementById(`c9u6-content-${t}`);
    if (!btn || !content) return;

    if (t === tab) {
      content.classList.remove('hidden');
      if (t === 'theory') {
        btn.className = "flex-1 min-w-[120px] py-2.5 px-3 text-sm font-semibold rounded-lg bg-emerald-50 text-emerald-700 border border-emerald-200 transition-all";
      } else {
        btn.className = "flex-1 min-w-[120px] py-2.5 px-3 text-sm font-semibold rounded-lg bg-slate-100 text-emerald-700 border border-slate-300 transition-all";
      }
    } else {
      content.classList.add('hidden');
      btn.className = "flex-1 min-w-[120px] py-2.5 px-3 text-sm font-medium rounded-lg text-slate-600 hover:bg-slate-50 transition-all";
    }
  });

  // Lazy load markdown if needed
  if (tab === 'exercise' || tab === 'qa') {
      const container = document.getElementById(`c9u6-content-${tab}`);
      if (container && container.getAttribute('data-markdown-src') && !container.hasAttribute('data-loaded')) {
          const src = container.getAttribute('data-markdown-src');
          fetch(src).then(r => r.text()).then(text => {
              if (window.marked) {
                 container.innerHTML = `<div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 markdown-body">${window.marked.parse(text)}</div>`;
              } else {
                 container.innerHTML = `<pre class="whitespace-pre-wrap p-4 text-sm font-mukta">${text}</pre>`;
              }
              container.setAttribute('data-loaded', 'true');
          }).catch(e => {
              container.innerHTML = `<div class="p-4 text-red-500">सामग्री लोड गर्न समस्या भयो।</div>`;
          });
      }
  }
}

// ------------------------------------------
// Lab Mode 1: Ecosystem Simulator
// ------------------------------------------
let currentEcoMode = 'grassland';

function setLabModeC9U6(mode) {
  playAudioC9U6('click');
  const modes = ['ecosystem', 'energy_web', 'interactions'];
  modes.forEach(m => {
    const btn = document.getElementById(`c9u6-mode-btn-${m}`);
    const div = document.getElementById(`c9u6-lab-${m}`);
    if (!btn || !div) return;
    if (m === mode) {
      div.classList.remove('hidden');
      btn.className = "flex-1 py-2 px-3 text-sm font-semibold rounded-lg bg-white shadow text-emerald-700";
    } else {
      div.classList.add('hidden');
      btn.className = "flex-1 py-2 px-3 text-sm font-medium rounded-lg text-slate-600 hover:bg-slate-200 transition-colors";
    }
  });

  if (mode === 'ecosystem') selectEcosystemTypeC9U6(currentEcoMode);
  if (mode === 'energy_web') calculateEnergyFlowC9U6();
  if (mode === 'interactions') selectInteractionC9U6('mutualism');
}

function selectEcosystemTypeC9U6(type) {
  currentEcoMode = type;
  playAudioC9U6('click');
  const btnG = document.getElementById('c9u6-eco-btn-grassland');
  const btnP = document.getElementById('c9u6-eco-btn-pond');
  if(btnG && btnP) {
      if (type === 'grassland') {
        btnG.className = "px-4 py-1.5 rounded-full text-sm font-semibold bg-emerald-100 text-emerald-800 border border-emerald-300";
        btnP.className = "px-4 py-1.5 rounded-full text-sm bg-blue-50 text-blue-600 border border-blue-200 hover:bg-blue-100 transition-colors";
        renderEcosystemSVG('grassland');
      } else {
        btnG.className = "px-4 py-1.5 rounded-full text-sm bg-emerald-50 text-emerald-600 border border-emerald-200 hover:bg-emerald-100 transition-colors";
        btnP.className = "px-4 py-1.5 rounded-full text-sm font-semibold bg-blue-100 text-blue-800 border border-blue-300";
        renderEcosystemSVG('pond');
      }
  }
}

function renderEcosystemSVG(type) {
  const svg = document.getElementById('c9u6-ecosystem-svg');
  if(!svg) return;

  const width = 800;
  const height = 450;

  if (type === 'grassland') {
    svg.innerHTML = `
      <rect width="100%" height="100%" fill="#87CEEB"/> <!-- Sky -->
      <circle cx="100" cy="80" r="40" fill="#FFD700" onclick="selectOrganismC9U6('sun')"/> <!-- Sun -->
      <path d="M0,300 Q400,280 800,320 L800,450 L0,450 Z" fill="#7CFC00"/> <!-- Grass -->
      <path d="M0,350 Q400,330 800,370 L800,450 L0,450 Z" fill="#228B22"/> <!-- Darker Grass -->

      <!-- Grasshopper -->
      <g transform="translate(200, 380)" cursor="pointer" onclick="selectOrganismC9U6('grasshopper')">
         <ellipse cx="20" cy="10" rx="15" ry="8" fill="#556B2F"/>
         <path d="M20,10 L30,-5 L35,15" stroke="#556B2F" stroke-width="2" fill="none"/>
      </g>

      <!-- Frog -->
      <g transform="translate(400, 360)" cursor="pointer" onclick="selectOrganismC9U6('frog')">
         <ellipse cx="20" cy="15" rx="20" ry="15" fill="#32CD32"/>
         <circle cx="10" cy="5" r="4" fill="white"/><circle cx="10" cy="5" r="2" fill="black"/>
      </g>

      <!-- Snake -->
      <g transform="translate(600, 390)" cursor="pointer" onclick="selectOrganismC9U6('snake')">
         <path d="M0,10 Q20,-10 40,10 T80,10" stroke="#8B4513" stroke-width="8" fill="none" stroke-linecap="round"/>
         <circle cx="5" cy="8" r="2" fill="yellow"/>
      </g>

      <!-- Eagle -->
      <g transform="translate(500, 100)" cursor="pointer" onclick="selectOrganismC9U6('eagle')">
         <path d="M0,0 Q30,-20 60,0 Q30,20 0,0" fill="#654321"/>
         <circle cx="30" cy="0" r="10" fill="white"/>
      </g>
    `;
  } else {
    svg.innerHTML = `
      <rect width="100%" height="100%" fill="#87CEEB"/> <!-- Sky -->
      <circle cx="700" cy="80" r="40" fill="#FFD700" onclick="selectOrganismC9U6('sun')"/>
      <rect x="0" y="250" width="800" height="200" fill="#4682B4"/> <!-- Water -->
      <path d="M0,250 Q400,270 800,250 L800,450 L0,450 Z" fill="#4169E1" opacity="0.5"/>

      <!-- Algae -->
      <g transform="translate(100, 300)" cursor="pointer" onclick="selectOrganismC9U6('algae')">
         <circle cx="0" cy="0" r="20" fill="#2E8B57" opacity="0.8"/>
         <circle cx="30" cy="10" r="15" fill="#2E8B57" opacity="0.8"/>
         <circle cx="15" cy="20" r="25" fill="#2E8B57" opacity="0.8"/>
      </g>

      <!-- Small Fish -->
      <g transform="translate(300, 320)" cursor="pointer" onclick="selectOrganismC9U6('small_fish')">
         <ellipse cx="20" cy="10" rx="15" ry="8" fill="#FFA500"/>
         <polygon points="5,10 -5,5 -5,15" fill="#FFA500"/>
      </g>

      <!-- Big Fish -->
      <g transform="translate(550, 350)" cursor="pointer" onclick="selectOrganismC9U6('big_fish')">
         <ellipse cx="40" cy="20" rx="40" ry="20" fill="#708090"/>
         <polygon points="0,20 -20,0 -20,40" fill="#708090"/>
      </g>

      <!-- Heron -->
      <g transform="translate(700, 200)" cursor="pointer" onclick="selectOrganismC9U6('heron')">
         <path d="M20,50 L20,100 M25,50 L25,100" stroke="orange" stroke-width="2"/> <!-- legs -->
         <ellipse cx="22" cy="40" rx="15" ry="25" fill="white"/> <!-- body -->
         <circle cx="22" cy="10" r="8" fill="white"/> <!-- head -->
         <polygon points="15,10 0,15 15,12" fill="orange"/> <!-- beak -->
      </g>
    `;
  }
}

const c9u6OrgData = {
  'sun': '<b>सूर्य (Sun):</b> सम्पूर्ण इकोसिस्टमको प्राथमिक ऊर्जा स्रोत। अजैविक अवयव।',
  'grasshopper': '<b>फट्याङ्ग्रो (Grasshopper):</b> प्राथमिक उपभोक्ता (शाकाहारी)। यसले घाँस खाएर बाँच्छ।',
  'frog': '<b>भ्यागुता (Frog):</b> द्वितीय उपभोक्ता (मांसाहारी)। यसले कीराफट्याङ्ग्रा खान्छ।',
  'snake': '<b>सर्प (Snake):</b> तृतीय उपभोक्ता। यसले भ्यागुता र मुसा खान्छ।',
  'eagle': '<b>चिल (Eagle):</b> शीर्ष उपभोक्ता (Top Predator)। यसले सर्प लगायत अन्य जनावर खान्छ।',
  'algae': '<b>लेउ (Algae):</b> उत्पादक (Producer)। पानीमा प्रकाश संश्लेषण गरी खाना बनाउँछ।',
  'small_fish': '<b>सानो माछा (Small Fish):</b> प्राथमिक उपभोक्ता। यसले लेउ र साना कीरा खान्छ।',
  'big_fish': '<b>ठूलो माछा (Big Fish):</b> द्वितीय उपभोक्ता। यसले साना माछा खान्छ।',
  'heron': '<b>बकुल्ला (Heron):</b> शीर्ष उपभोक्ता। यसले पोखरीका माछाहरू खान्छ।'
};

window.selectOrganismC9U6 = function(key) {
  playAudioC9U6('click');
  const div = document.getElementById('c9u6-organism-details');
  if(div) {
    div.innerHTML = c9u6OrgData[key] || "विवरण उपलब्ध छैन।";
    div.classList.add('bg-emerald-100');
    setTimeout(() => div.classList.remove('bg-emerald-100'), 300);
  }
}

// ------------------------------------------
// Lab Mode 2: Energy Flow & Cascade
// ------------------------------------------
window.calculateEnergyFlowC9U6 = function() {
  const inputEl = document.getElementById('c9u6-energy-input');
  if(!inputEl) return;
  let energy = parseFloat(inputEl.value) || 100000;

  const e1 = energy;
  const e2 = energy * 0.1;
  const e3 = energy * 0.01;
  const e4 = energy * 0.001;

  const svg = document.getElementById('c9u6-energy-svg');
  if(svg) {
    svg.innerHTML = `
      <polygon points="150,20 280,230 20,230" fill="#fde047" stroke="#eab308" stroke-width="2"/>
      <line x1="60" y1="160" x2="240" y2="160" stroke="#eab308" stroke-width="2"/>
      <line x1="100" y1="90" x2="200" y2="90" stroke="#eab308" stroke-width="2"/>

      <text x="150" y="210" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">उत्पादक (घाँस)</text>
      <text x="150" y="225" text-anchor="middle" font-size="10" fill="#a16207">${toNepaliNumC9U6(e1)} J (१००%)</text>

      <text x="150" y="140" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">प्राथमिक उपभोक्ता</text>
      <text x="150" y="155" text-anchor="middle" font-size="10" fill="#a16207">${toNepaliNumC9U6(e2)} J (१०%)</text>

      <text x="150" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">द्वितीय/तृतीय उपभोक्ता</text>
      <text x="150" y="80" text-anchor="middle" font-size="10" fill="#a16207">${toNepaliNumC9U6(e3)} J (१%)</text>

      <text x="150" y="35" text-anchor="middle" font-size="10" font-weight="bold" fill="#854d0e">शीर्ष</text>
    `;
  }
  playAudioC9U6('energy_transfer');
}

window.triggerCascadeEventC9U6 = function(event) {
  const alertDiv = document.getElementById('c9u6-cascade-alert');
  if(!alertDiv) return;

  if (event === 'rats_killed') {
    playAudioC9U6('cascade_alert');
    alertDiv.innerHTML = `<b>असर:</b> सर्प र चिलको खाना अभाव हुन्छ, उनीहरूको सङ्ख्या घट्छ। मुसा नभएपछि कीराफट्याङ्ग्रा अनियन्त्रित रूपमा बढ्छन् र बाली उल्टै सखाप हुन्छ। यसलाई <i>Trophic Cascade</i> भनिन्छ।`;
    alertDiv.className = "mt-4 p-3 rounded text-sm font-medium min-h-[60px] bg-rose-100 text-rose-900 border border-rose-300";
  } else if (event === 'frogs_extinct') {
    playAudioC9U6('cascade_alert');
    alertDiv.innerHTML = `<b>असर:</b> भ्यागुता लोप हुँदा कीराहरूको सङ्ख्या ह्वात्तै बढ्छ। सर्पहरू भोकै पर्छन्। पारिस्थितिक सन्तुलन पूर्ण रूपमा बिग्रन्छ।`;
    alertDiv.className = "mt-4 p-3 rounded text-sm font-medium min-h-[60px] bg-rose-100 text-rose-900 border border-rose-300";
  } else {
    playAudioC9U6('click');
    alertDiv.innerHTML = `खाद्यजाल सामान्य अवस्थामा छ। सन्तुलन कायम छ।`;
    alertDiv.className = "mt-4 p-3 rounded text-sm font-medium min-h-[60px] bg-emerald-100 text-emerald-900 border border-emerald-300";
  }
}

// ------------------------------------------
// Lab Mode 3: Biotic Interactions
// ------------------------------------------
window.selectInteractionC9U6 = function(key) {
  playAudioC9U6('click');
  const interactions = ['mutualism', 'commensalism', 'parasitism', 'predation', 'competition'];
  interactions.forEach(i => {
    const btn = document.getElementById(`c9u6-int-btn-${i}`);
    if(!btn) return;
    if(i === key) {
       btn.classList.add('bg-indigo-100', 'text-indigo-800', 'border-indigo-300', 'font-semibold');
       btn.classList.remove('bg-slate-100', 'text-slate-700', 'border-slate-300');
    } else {
       btn.classList.remove('bg-indigo-100', 'text-indigo-800', 'border-indigo-300', 'font-semibold');
       btn.classList.add('bg-slate-100', 'text-slate-700', 'border-slate-300');
    }
  });

  const svg = document.getElementById('c9u6-interaction-svg');
  const desc = document.getElementById('c9u6-interaction-desc');

  if (key === 'mutualism') {
    svg.innerHTML = `
      <circle cx="200" cy="150" r="50" fill="#f472b6"/> <!-- Flower -->
      <circle cx="200" cy="150" r="20" fill="#fde047"/>
      <path d="M250,100 Q280,80 300,100 T320,120" fill="none" stroke="#eab308" stroke-width="10" stroke-dasharray="10 5"/> <!-- Bee path -->
      <ellipse cx="300" cy="100" rx="15" ry="10" fill="#eab308"/>
      <ellipse cx="305" cy="95" rx="5" ry="8" fill="white" opacity="0.8"/>
    `;
    desc.innerHTML = `<b>पारस्परिकता (+,+)</b>: दुवै जीवलाई फाइदा हुन्छ। जस्तै: मौरी (मह पाउँछ) र फूल (परागसेचन हुन्छ)।`;
  } else if (key === 'commensalism') {
    svg.innerHTML = `
      <ellipse cx="200" cy="150" rx="120" ry="40" fill="#94a3b8"/> <!-- Shark -->
      <polygon points="120,150 80,120 100,150 80,180" fill="#94a3b8"/>
      <ellipse cx="220" cy="190" rx="30" ry="8" fill="#64748b"/> <!-- Remora -->
    `;
    desc.innerHTML = `<b>सहभोजिता (+,0)</b>: एउटालाई फाइदा, अर्कोलाई असर नपर्ने। जस्तै: शार्क र रेमोरा माछा।`;
  } else if (key === 'parasitism') {
    svg.innerHTML = `
      <rect x="150" y="100" width="100" height="150" rx="20" fill="#fca5a5"/> <!-- Human Arm -->
      <path d="M180,130 Q170,100 220,120 T210,160" fill="none" stroke="#7f1d1d" stroke-width="6"/> <!-- Leech/Worm -->
    `;
    desc.innerHTML = `<b>परजीविता (+,-)</b>: एउटालाई फाइदा, आश्रयदातालाई हानि। जस्तै: मानिस र जुका/किर्ना।`;
  } else if (key === 'predation') {
    svg.innerHTML = `
      <ellipse cx="120" cy="200" rx="40" ry="20" fill="#fb923c"/> <!-- Predator (Tiger) -->
      <ellipse cx="280" cy="200" rx="30" ry="15" fill="#a8a29e"/> <!-- Prey (Deer) -->
      <path d="M160,200 L240,200" stroke="red" stroke-width="4" stroke-dasharray="5 5" fill="none"/>
    `;
    desc.innerHTML = `<b>सिकारिता (+,-)</b>: एउटाले अर्कोलाई मारेर खाने। जस्तै: बाघ र जरायो।`;
  } else if (key === 'competition') {
    svg.innerHTML = `
      <path d="M150,250 L150,50 M140,250 L160,250" stroke="#166534" stroke-width="15"/> <!-- Tree 1 -->
      <circle cx="150" cy="80" r="50" fill="#22c55e" opacity="0.8"/>

      <path d="M250,250 L250,100 M240,250 L260,250" stroke="#166534" stroke-width="10"/> <!-- Tree 2 -->
      <circle cx="250" cy="120" r="40" fill="#4ade80" opacity="0.8"/>

      <circle cx="200" cy="30" r="30" fill="#fef08a"/> <!-- Sun -->
      <path d="M200,60 L150,100 M200,60 L250,120" stroke="#fde047" stroke-width="2" stroke-dasharray="5 5" fill="none"/>
    `;
    desc.innerHTML = `<b>प्रतिस्पर्धा (-,-)</b>: स्रोत (जस्तै घाम, पानी) को लागि सङ्घर्ष। दुवैलाई शक्ति खर्च हुन्छ। जस्तै: जङ्गलका रुखहरू।`;
  }
}

// ------------------------------------------
// Quiz Engine
// ------------------------------------------
const c9u6QuizData = [
  { q: "पारिस्थिक पद्धतिका उत्पादक कुन हुन्?", options: ["विच्छेदक", "हरिया बिरुवा", "जनावर", "माटो"], ans: 1 },
  { q: "कुन नियमले एक तहबाट अर्को तहमा १०% ऊर्जा मात्र सर्छ भन्छ?", options: ["न्युटनको नियम", "लिन्डम्यानको नियम", "पास्कलको नियम", "चार्ल्सको नियम"], ans: 1 },
  { q: "कुन सम्बन्धमा दुवै जीवलाई फाइदा हुन्छ?", options: ["पारस्परिकता", "परजीविता", "प्रतिस्पर्धा", "सहभोजिता"], ans: 0 },
  { q: "खाद्य शृङ्खलाहरू जोडिएर के बन्छ?", options: ["खाद्य चक्र", "खाद्य पिरामिड", "खाद्यजाल", "इकोसिस्टम"], ans: 2 },
  { q: "जुका र मानिसबीचको सम्बन्ध कुन हो?", options: ["पारस्परिकता", "परजीविता", "सिकारिता", "सहभोजिता"], ans: 1 },
  { q: "ऊर्जाको पिरामिड कस्तो हुन्छ?", options: ["सधैँ उल्टो", "सधैँ ठाडो", "गोलाकार", "तेर्सो"], ans: 1 },
  { q: "ढुसी र ब्याक्टेरियालाई के भनिन्छ?", options: ["उत्पादक", "प्राथमिक उपभोक्ता", "शीर्ष उपभोक्ता", "विच्छेदक"], ans: 3 },
  { q: "चउरको इकोसिस्टममा मुख्य उत्पादक को हो?", options: ["भ्यागुता", "घाँस", "सर्प", "चिल"], ans: 1 },
  { q: "शार्क र रेमोरा माछाको सम्बन्धलाई के भनिन्छ?", options: ["सहभोजिता", "प्रतिस्पर्धा", "पारस्परिकता", "परजीविता"], ans: 0 },
  { q: "किसानले सबै मुसा मारेमा के हुन्छ?", options: ["बाली राम्रो हुन्छ", "सर्प र चिल बढ्छन्", "खाद्यजाल भत्कन्छ", "माटो मलिलो हुन्छ"], ans: 2 }
];

let c9u6UserAnswers = new Array(10).fill(null);

function renderQuizC9U6() {
  const container = document.getElementById('c9u6-quiz-questions');
  if(!container) return;

  let html = '';
  c9u6QuizData.forEach((q, i) => {
    html += `
      <div class="bg-slate-50 rounded-xl p-5 border border-slate-200" id="c9u6-q-box-${i}">
        <p class="font-semibold text-slate-800 mb-3">${toNepaliNumC9U6(i + 1)}. ${q.q}</p>
        <div class="space-y-2">
    `;
    q.options.forEach((opt, j) => {
      html += `
        <label class="flex items-center gap-3 p-3 rounded-lg border cursor-pointer transition-colors ${c9u6UserAnswers[i] === j ? 'border-emerald-500 bg-emerald-50' : 'border-slate-200 hover:bg-slate-100'}">
          <input type="radio" name="c9u6-q${i}" value="${j}" onchange="selectQuizOptionC9U6(${i}, ${j})" class="w-4 h-4 text-emerald-600 focus:ring-emerald-500">
          <span class="text-slate-700">${opt}</span>
        </label>
      `;
    });
    html += `</div><div id="c9u6-q-feedback-${i}" class="mt-3 text-sm hidden font-medium"></div></div>`;
  });
  container.innerHTML = html;
}

window.selectQuizOptionC9U6 = function(qIdx, optIdx) {
  playAudioC9U6('click');
  c9u6UserAnswers[qIdx] = optIdx;
  // Visual update handled by re-render for simplicity
  renderQuizC9U6();
  // Reselect the radio visually
  const radios = document.getElementsByName(`c9u6-q${qIdx}`);
  if(radios[optIdx]) radios[optIdx].checked = true;
}

window.submitQuizC9U6 = function() {
  let score = 0;
  let allAnswered = true;

  for(let i=0; i<10; i++) {
    if(c9u6UserAnswers[i] === null) {
      allAnswered = false;
      break;
    }
    const fb = document.getElementById(`c9u6-q-feedback-${i}`);
    const box = document.getElementById(`c9u6-q-box-${i}`);
    if (c9u6UserAnswers[i] === c9u6QuizData[i].ans) {
      score++;
      if(fb) { fb.innerHTML = '✅ सही उत्तर!'; fb.className = "mt-3 text-sm text-emerald-600 font-medium block"; }
      if(box) box.classList.add('border-emerald-300', 'bg-emerald-50/50');
    } else {
      if(fb) { fb.innerHTML = `❌ गलत। सही उत्तर: <b>${c9u6QuizData[i].options[c9u6QuizData[i].ans]}</b>`; fb.className = "mt-3 text-sm text-rose-600 font-medium block"; }
      if(box) box.classList.add('border-rose-300', 'bg-rose-50/50');
    }
  }

  if(!allAnswered) {
    alert("कृपया सबै प्रश्नहरूको उत्तर दिनुहोस्।");
    return;
  }

  const scoreContainer = document.getElementById('c9u6-quiz-score-container');
  const scoreVal = document.getElementById('c9u6-quiz-score-val');

  if(scoreContainer && scoreVal) {
    scoreVal.textContent = toNepaliNumC9U6(score);
    scoreContainer.classList.remove('hidden');
    if(score >= 8) {
      playAudioC9U6('correct');
      scoreContainer.className = "mt-4 inline-block bg-emerald-100 border border-emerald-300 text-emerald-800 px-6 py-3 rounded-xl font-bold text-lg";
    } else {
      playAudioC9U6('wrong');
      scoreContainer.className = "mt-4 inline-block bg-amber-100 border border-amber-300 text-amber-800 px-6 py-3 rounded-xl font-bold text-lg";
    }
  }

  const btn = document.getElementById('c9u6-quiz-submit-btn');
  if(btn) btn.classList.add('hidden');
}

// ------------------------------------------
// Initialization
// ------------------------------------------
window.initC9U6 = function() {
  switchTabC9U6('theory');
  setLabModeC9U6('ecosystem');
  renderQuizC9U6();
};
