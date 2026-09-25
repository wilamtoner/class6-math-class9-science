
// =========================================================================
// GRADE 9 UNIT 4: EVOLUTION (क्रम विकास) INTERACTIVE CONTROLLER
// =========================================================================

let activeC9U4Tab = 'concepts';
let activeC9U4LabMode = 'anatomy';
let activeC9U4AnatSub = 'homology';
let activeC9U4HomologyOrgan = 'human';
let activeC9U4VestigialOrgan = 'appendix';
let activeC9U4ConnectingOrgan = 'archaeopteryx';

// Mode 2 Simulator State
let c9u4MothEnv = 'clean';
let c9u4MothGen = 1;
let c9u4WhitePct = 85;
let c9u4BlackPct = 15;
let c9u4LiveHunts = 0;
let c9u4MothsData = [];
let c9u4HuntTimerId = null;
let c9u4HuntTimeLeft = 10;
let c9u4PredatorActive = false;
let c9u4PredatorCaughtConspicuous = 0;
let c9u4PredatorCaughtCamouflaged = 0;

// Mode 3 Simulator State
let activeC9U4Mutation = 'polydactyly';

// Quiz State
let c9u4QuizAnswers = {};

// -------------------------------------------------------------------------
// Web Audio Synthesizer (Zero External Dependencies)
// -------------------------------------------------------------------------
let c9u4AudioCtx = null;
function playMothAudioC9U4(type) {
  try {
    if (!c9u4AudioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) c9u4AudioCtx = new AudioContext();
    }
    if (!c9u4AudioCtx) return;
    if (c9u4AudioCtx.state === 'suspended') {
      c9u4AudioCtx.resume();
    }
    const t = c9u4AudioCtx.currentTime;
    const osc = c9u4AudioCtx.createOscillator();
    const gain = c9u4AudioCtx.createGain();
    osc.connect(gain);
    gain.connect(c9u4AudioCtx.destination);

    if (type === 'catch') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(440, t);
      osc.frequency.exponentialRampToValueAtTime(880, t + 0.12);
      gain.gain.setValueAtTime(0.3, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.15);
      osc.start(t);
      osc.stop(t + 0.15);
    } else if (type === 'swoop') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(340, t);
      osc.frequency.exponentialRampToValueAtTime(120, t + 0.28);
      gain.gain.setValueAtTime(0.22, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.3);
      osc.start(t);
      osc.stop(t + 0.3);
    } else if (type === 'win') {
      [523.25, 659.25, 783.99].forEach((freq, idx) => {
        const o = c9u4AudioCtx.createOscillator();
        const g = c9u4AudioCtx.createGain();
        o.connect(g);
        g.connect(c9u4AudioCtx.destination);
        o.type = 'sine';
        o.frequency.setValueAtTime(freq, t + idx * 0.1);
        g.gain.setValueAtTime(0.2, t + idx * 0.1);
        g.gain.exponentialRampToValueAtTime(0.01, t + idx * 0.1 + 0.2);
        o.start(t + idx * 0.1);
        o.stop(t + idx * 0.1 + 0.2);
      });
    }
  } catch (e) {
    // Silently continue if audio context is blocked
  }
}

// -------------------------------------------------------------------------
// Tab Switching
// -------------------------------------------------------------------------
function setTabC9U4(tab) {
  activeC9U4Tab = tab;
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const view = document.getElementById(`c9u4-view-${t}`);
    const btn = document.getElementById(`c9u4-tab-${t}`);
    if (view) {
      if (t === tab) view.classList.remove('hidden');
      else view.classList.add('hidden');
    }
    if (btn) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-purple-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer font-bold';
      }
    }
  });

  if (tab === 'quiz') {
    renderC9U4Quiz();
  }
}

// -------------------------------------------------------------------------
// Lab Mode Switching
// -------------------------------------------------------------------------
function setLabModeC9U4(mode) {
  activeC9U4LabMode = mode;
  const modes = ['anatomy', 'selection', 'mutation'];
  modes.forEach(m => {
    const container = document.getElementById(`c9u4-lab-mode-${m}`);
    const btn = document.getElementById(`c9u4-btn-mode-${m}`);
    if (container) {
      if (m === mode) container.classList.remove('hidden');
      else container.classList.add('hidden');
    }
    if (btn) {
      if (m === mode) {
        btn.className = 'flex-1 py-3 px-4 rounded-2xl bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-black text-xs md:text-sm shadow-md transition';
      } else {
        btn.className = 'flex-1 py-3 px-4 rounded-2xl bg-slate-800 text-slate-400 hover:text-white font-bold text-xs md:text-sm transition';
      }
    }
  });

  if (mode === 'anatomy') {
    renderHomologySVGC9U4(activeC9U4HomologyOrgan);
  } else if (mode === 'selection') {
    renderMothsC9U4();
    updateMothUI();
  } else if (mode === 'mutation') {
    renderMutationSVGC9U4(activeC9U4Mutation);
  }
}

// -------------------------------------------------------------------------
// Anatomy Submode Switching
// -------------------------------------------------------------------------
function setAnatomySubModeC9U4(sub) {
  activeC9U4AnatSub = sub;
  const subs = ['homology', 'vestigial', 'connecting'];
  subs.forEach(s => {
    const p = document.getElementById(`c9u4-anat-panel-${s}`);
    const btn = document.getElementById(`c9u4-subbtn-${s}`);
    if (p) {
      if (s === sub) p.classList.remove('hidden');
      else p.classList.add('hidden');
    }
    if (btn) {
      if (s === sub) {
        btn.className = 'px-3.5 py-1.5 rounded-xl bg-purple-500/20 border border-purple-500 text-purple-300 font-bold transition whitespace-nowrap cursor-pointer text-xs';
      } else {
        btn.className = 'px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition whitespace-nowrap cursor-pointer text-xs';
      }
    }
  });

  if (sub === 'homology') {
    renderHomologySVGC9U4(activeC9U4HomologyOrgan);
  }
}

// -------------------------------------------------------------------------
// Homology Organ Explorer
// -------------------------------------------------------------------------
const C9U4_HOMOLOGY_DATA = {
  human: {
    nep: 'मानिसको हात (Human Hand)',
    eng: 'HUMAN HAND (HOMOLOGOUS)',
    func: 'विभिन्न वस्तुहरू समात्न, लेख्न र औजार चलाउनका लागि विपरित दिशामा चल्ने बुढी औँला (Opposable thumb) सहित अनुकूलित।',
    bones: 'Humerus, Radius, Ulna, Carpals (८ वटा), Metacarpals (५ वटा), र Phalanges (१४ वटा) मिलेर पूर्ण लचिलोपन दिन्छन्।',
    meaning: 'घोडा, चमेरो र ह्वेलसँग हाडको ढाँचा ठ्याक्कै मिल्नुले यी सबै स्तनधारीहरू एउटै साझा चौपाया पुर्खाबाट विकसित भएका हुन् (Divergent Evolution) भन्ने पुष्टि गर्छ।'
  },
  cat: {
    nep: 'बिरालो वा चीताको अगाडिको खुट्टा',
    eng: 'CAT / CHEETAH FORELIMB',
    func: 'शिकार पक्रन, रुख चढ्न र तीव्र गतिमा फड्को मार्नका लागि कडा पञ्जा र बलियो कुहिनाको जोड।',
    bones: 'Humerus, Radius-Ulna, Carpals, Metacarpals र Phalanges मा लुकाउन मिल्ने तीखा नङ्ग्राहरू (Retractile claws)।',
    meaning: 'शिकारी जीवनशैलीका लागि रूपान्तरित भए तापनि आन्तरिक कंकाल मानिसको हातसँग शतप्रतिशत समधर्मी छ।'
  },
  whale: {
    nep: 'ह्वेलको फ्लिपर (Whale Flipper)',
    eng: 'WHALE FLIPPER (PADDLE)',
    func: 'पानीमा सन्तुलन कायम राख्न र दिशा परिवर्तन गर्दै पौडी खेल्न (Oar-like paddle) रूपान्तरित।',
    bones: 'बाक्लो छाला र बोसोभित्र ह्युमरस, छोटा रेडियस-अल्ना र लाम्चिएका फ्यालेन्जेजहरू प्याडलको आकारमा सजिएका।',
    meaning: 'जलचर स्तनधारी भए तापनि चौपाया जमिनका पुर्खाबाटै विकसित भएको अकाट्य शारीरिक प्रमाण।'
  },
  bat: {
    nep: 'चमेराको पखेटा (Bat Wing)',
    eng: 'BAT WING (PATAGIUM)',
    func: 'हावामा उड्न र तीव्र गतिमा किटपतंग शिकार गर्नका लागि छालाको पातलो झिल्ली (Patagium) फैलाउने।',
    bones: 'अत्यधिक लाम्चिएका ४ ओटा फ्यालेन्जेज (औँलाहरू) जसले पखेटाको छालालाई छाताको तार जस्तै फैलाई राख्छन्।',
    meaning: 'उड्नका लागि अनुकूलित भए तापनि हाडको ढाँचा मानिसकै हातको परिमार्जित रूप (Homologous organ) हो।'
  },
  horse: {
    nep: 'घोडाको अगाडिको खुट्टा (Horse Forelimb)',
    eng: 'HORSE FORELIMB (RUNNING)',
    func: 'कडा जमिनमा तीव्र गतिमा दौडन (Cursorial locomotion) र शरीरको सम्पूर्ण भार थाम्न अनुकूलित।',
    bones: 'तेस्रो औँला (3rd digit) मात्र लामो र बलियो भई खुर (Hoof) मा परिणत भएको, बाँकी औँलाहरू अवशेषी हाड (Splint bones) का रूपमा रहेका।',
    meaning: 'दौडनका लागि औँलाहरू घटेर एउटा मात्र खुर बने तापनि यसको ह्युमरस र रेडियस-अल्ना मानिसको जस्तै हुन्छ।'
  }
};

function renderHomologySVGC9U4(organ) {
  const wrap = document.getElementById('c9u4-homology-svg-wrap');
  if (!wrap) return;

  if (organ === 'bat') {
    wrap.innerHTML = `
      <svg viewBox="0 0 420 150" class="w-full max-w-[390px] h-auto select-none">
        <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🦇 चमेराको पखेटा (Bat Wing - Flying)</text>
        <path d="M 60,65 Q 160,-10 390,20 Q 380,130 180,120 Q 80,100 60,65 Z" fill="#9333ea" fill-opacity="0.18" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="3,3"/>
        <rect x="30" y="58" width="55" height="14" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
        <text x="57" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
        <rect x="95" y="55" width="80" height="10" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
        <text x="135" y="63" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Radius (Long)</text>
        <circle cx="185" cy="60" r="8" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
        <text x="185" y="63" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Carpals</text>
        <path d="M 185,52 L 195,35 L 205,32" stroke="#34d399" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M 188,56 Q 260,35 375,25" stroke="#34d399" stroke-width="2.2" fill="none"/>
        <path d="M 190,60 Q 280,65 390,70" stroke="#34d399" stroke-width="2.2" fill="none"/>
        <path d="M 188,64 Q 270,95 365,115" stroke="#34d399" stroke-width="2" fill="none"/>
        <path d="M 185,68 Q 230,110 280,125" stroke="#34d399" stroke-width="2" fill="none"/>
        <text x="310" y="140" fill="#34d399" font-size="9" font-weight="bold">अत्यधिक लामा ४ औँलाहरू (Phalanges)</text>
      </svg>
      <span class="text-[11px] text-slate-400 mt-2 font-mono">उड्नका लागि अनुकूलित पातलो छालाको झिल्ली (Patagium) र लामा औँलाहरू</span>
    `;
  } else if (organ === 'whale') {
    wrap.innerHTML = `
      <svg viewBox="0 0 420 150" class="w-full max-w-[390px] h-auto select-none">
        <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🐋 ह्वेलको फ्लिपर (Whale Flipper - Swimming Paddle)</text>
        <path d="M 40,65 Q 120,25 320,50 Q 380,85 310,115 Q 130,115 40,65 Z" fill="#0284c7" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,3"/>
        <rect x="50" y="52" width="45" height="28" rx="6" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
        <text x="72" y="70" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
        <rect x="105" y="44" width="45" height="18" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
        <rect x="105" y="68" width="45" height="18" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
        <text x="127" y="56" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Radius</text>
        <text x="127" y="80" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Ulna</text>
        <rect x="158" y="48" width="22" height="36" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
        <g stroke="#34d399" stroke-width="4" stroke-linecap="round" fill="none">
          <line x1="188" y1="52" x2="270" y2="52"/>
          <line x1="188" y1="62" x2="330" y2="68"/>
          <line x1="188" y1="72" x2="320" y2="84"/>
          <line x1="188" y1="80" x2="280" y2="98"/>
          <line x1="188" y1="88" x2="240" y2="108"/>
        </g>
        <text x="260" y="135" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">पौडी खेल्ने फ्लिपर प्याडल (Flattened Phalanges)</text>
      </svg>
      <span class="text-[11px] text-slate-400 mt-2 font-mono">पानीमा दिशा मोड्न बाक्लो छालाभित्र प्याडल आकारमा सजिएका हाडहरू</span>
    `;
  } else if (organ === 'horse') {
    wrap.innerHTML = `
      <svg viewBox="0 0 420 150" class="w-full max-w-[390px] h-auto select-none">
        <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🐎 घोडाको अगाडिको खुट्टा (Horse Forelimb - Running)</text>
        <rect x="40" y="55" width="60" height="22" rx="5" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
        <text x="70" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
        <rect x="110" y="58" width="95" height="16" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
        <text x="155" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Radius-Ulna (Fused)</text>
        <rect x="215" y="56" width="22" height="20" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
        <text x="226" y="69" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Carpals</text>
        <rect x="245" y="60" width="75" height="12" rx="3" fill="#34d399" stroke="#059669" stroke-width="1.5"/>
        <text x="282" y="70" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">3rd Metacarpal</text>
        <rect x="328" y="58" width="30" height="16" rx="3" fill="#34d399" stroke="#059669" stroke-width="1.5"/>
        <path d="M 364,52 L 388,52 L 392,80 L 364,80 Z" fill="#475569" stroke="#1e293b" stroke-width="2"/>
        <text x="378" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">खुर (Hoof)</text>
        <text x="280" y="135" fill="#94a3b8" font-size="9" text-anchor="middle">तेस्रो औँला मात्र बलियो भई खुर बनेको (Digit 3)</text>
      </svg>
      <span class="text-[11px] text-slate-400 mt-2 font-mono">तीव्र गतिमा दौडनका लागि विकसित एउटै बलियो खुर र जोडिएका हाडहरू</span>
    `;
  } else if (organ === 'cat') {
    wrap.innerHTML = `
      <svg viewBox="0 0 420 150" class="w-full max-w-[390px] h-auto select-none">
        <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🐆 चीता वा बिरालोको अगाडिको खुट्टा (Cat Forelimb - Hunting)</text>
        <rect x="40" y="52" width="65" height="20" rx="5" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
        <text x="72" y="65" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
        <rect x="115" y="47" width="80" height="13" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
        <rect x="115" y="67" width="80" height="13" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
        <text x="155" y="57" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Radius</text>
        <text x="155" y="77" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Ulna</text>
        <rect x="205" y="52" width="22" height="24" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
        <g stroke="#34d399" stroke-width="3" stroke-linecap="round" fill="none">
          <line x1="235" y1="52" x2="300" y2="42"/>
          <line x1="235" y1="58" x2="315" y2="52"/>
          <line x1="235" y1="65" x2="320" y2="66"/>
          <line x1="235" y1="72" x2="310" y2="80"/>
          <line x1="235" y1="78" x2="280" y2="92"/>
        </g>
        <path d="M 300,42 Q 315,38 312,32 M 315,52 Q 330,48 327,42 M 320,66 Q 335,66 332,60 M 310,80 Q 325,84 322,90" stroke="#f43f5e" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <text x="270" y="135" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">शिकार समात्ने तीखा नङ्ग्राहरू (Retractile Claws)</text>
      </svg>
      <span class="text-[11px] text-slate-400 mt-2 font-mono">शिकार समात्न र फड्को मार्न लचिलो कुहिना र लुक्ने तीखा नङ्ग्राहरू</span>
    `;
  } else {
    // human
    wrap.innerHTML = `
      <svg viewBox="0 0 420 150" class="w-full max-w-[390px] h-auto select-none">
        <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🖐️ मानिसको हात (Human Hand - Grasping/Tools)</text>
        <rect x="30" y="52" width="75" height="22" rx="5" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
        <text x="67" y="66" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Humerus (बाहु)</text>
        <circle cx="115" cy="63" r="5" fill="#cbd5e1"/>
        <rect x="128" y="45" width="75" height="15" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
        <rect x="128" y="66" width="75" height="15" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
        <text x="165" y="56" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Radius (रेडियस)</text>
        <text x="165" y="77" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Ulna (अल्ना)</text>
        <rect x="212" y="47" width="24" height="34" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
        <text x="224" y="67" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Carpals</text>
        <path d="M 238,48 L 265,30 L 290,26" stroke="#34d399" stroke-width="3" fill="none" stroke-linecap="round"/>
        <text x="295" y="24" fill="#34d399" font-size="8" font-weight="bold">बुढी औँला (Thumb)</text>
        <g stroke="#34d399" stroke-width="2.5" stroke-linecap="round" fill="none">
          <path d="M 238,55 L 295,48 L 335,46"/>
          <path d="M 238,62 L 310,60 L 350,60"/>
          <path d="M 238,69 L 305,72 L 340,75"/>
          <path d="M 238,76 L 285,85 L 320,90"/>
        </g>
        <text x="280" y="135" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">५ ओटा औँलाहरू (Metacarpals & 14 Phalanges)</text>
      </svg>
      <span class="text-[11px] text-slate-400 mt-2 font-mono">आधारभूत अस्थिपञ्जर ढाँचा: Humerus ➔ Radius/Ulna ➔ Carpals ➔ Phalanges</span>
    `;
  }
}

function selectHomologyOrganC9U4(organ) {
  activeC9U4HomologyOrgan = organ;
  const d = C9U4_HOMOLOGY_DATA[organ];
  if (!d) return;

  const nepEl = document.getElementById('c9u4-h-neptitle');
  const engEl = document.getElementById('c9u4-h-engtitle');
  const funcEl = document.getElementById('c9u4-h-function');
  const bonesEl = document.getElementById('c9u4-h-bones');
  const meaningEl = document.getElementById('c9u4-h-meaning');

  if (nepEl) nepEl.textContent = d.nep;
  if (engEl) engEl.textContent = d.eng;
  if (funcEl) funcEl.textContent = d.func;
  if (bonesEl) bonesEl.textContent = d.bones;
  if (meaningEl) meaningEl.textContent = d.meaning;

  const organs = ['human', 'cat', 'whale', 'bat', 'horse'];
  organs.forEach(o => {
    const btn = document.getElementById(`c9u4-hbtn-${o}`);
    if (btn) {
      if (o === organ) {
        btn.className = 'p-3 rounded-2xl border bg-purple-600/30 border-purple-500 text-purple-300 text-left transition cursor-pointer';
      } else {
        btn.className = 'p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer';
      }
    }
  });

  renderHomologySVGC9U4(organ);
}

// -------------------------------------------------------------------------
// Vestigial Organs Explorer
// -------------------------------------------------------------------------
const C9U4_VESTIGIAL_DATA = {
  appendix: {
    nep: 'भर्मिफर्म एपेन्डिक्स (Appendix)',
    eng: 'VERMIFORM APPENDIX',
    anc: 'हाम्रा प्राचीन शाकाहारी पूर्वजहरूमा काँचो घाँस-पात र रुखका बोक्रामा भएको सेलुलोज (Cellulose) पचाउने ब्याक्टेरिया भण्डारण गर्न यो निकै लामो र पूर्ण कार्यशील थियो।',
    pres: 'मानिसले खाना पकाएर खान थालेपछि सेलुलोज पचाउने आवश्यकता परेन र यो खुम्चिएर काम नलाग्ने अवशेषाङ्ग बन्यो। कहिलेकाहीँ यसमा संक्रमण भई एपेन्डिसाइटिस (Appendicitis) हुन्छ।',
    conc: 'यसले मानिस शाकाहारी चौपाया पूर्वजबाट विकसित भएको अकाट्य प्रमाण दिन्छ।'
  },
  coccyx: {
    nep: 'पुच्छ्रे हाड (Coccyx / Tailbone)',
    eng: 'COCCYX (VESTIGIAL TAIL)',
    anc: 'रुखमा बस्ने पुर्खाहरूमा हाँगा समात्न र उफ्रँदा शरीरको सन्तुलन कायम राख्न लामो पुच्छर थियो।',
    pres: 'मानिस सिधा दुई खुट्टाले हिँड्न थालेपछि पुच्छरको आवश्यकता हरायो र मेरुदण्डको फेदमा ४ ओटा हाडहरू आपसमा टाँसिएर सानो अवशेषी हाड (Coccyx) मात्र बाँकी रह्यो।',
    conc: 'यसले मानव पुर्खामा लामो पुच्छर थियो भन्ने प्रत्यक्ष कंकाल प्रमाण प्रस्तुत गर्दछ।'
  },
  plica: {
    nep: 'प्लीका सेमिल्युनारिस (Plica Semilunaris)',
    eng: 'NICTITATING MEMBRANE REMNANT',
    anc: 'उभयचर, सरीसृप र चराहरूमा आँखालाई पानीमुनि वा हावामा धुलोबाट जोगाउन आँखा छोप्ने तेस्रो पारदर्शी ढकनी (Nictitating membrane) पूर्ण सक्रिय हुन्छ।',
    pres: 'मानिसको आँखाको भित्री कुनामा सानो गुलाबी मासुको पत्र (Plica semilunaris) का रूपमा मात्र यो बाँकी छ, जसको कुनै दृष्टि कार्य छैन।',
    conc: 'यसले मानव पूर्वजहरूको आँखामा पनि तेस्रो आँखाको ढकनी थियो भन्ने प्रमाण देखाउँछ।'
  },
  ear: {
    nep: 'कानको बाह्य मांसपेशी (Auricular Muscles)',
    eng: 'AURICULAR EAR MUSCLES',
    anc: 'कुकुर, घोडा र गाईभैँसीले आवाज आएको दिशातर्फ कानको लोती (Pinna) स्वतन्त्र रूपमा घुमाउन सक्छन् जसले गर्दा शिकारी शत्रुबाट बच्न मद्दत पुग्छ।',
    pres: 'मानिसको कान वरिपरिका मांसपेशीहरू निष्क्रिय छन्। धेरैजसो मानिसले कान हल्लाउन सक्दैनन्, केहीले सामान्य हल्लाउन सके तापनि यसको कुनै सुरक्षा उपयोग छैन।',
    conc: 'मानिसका पूर्वजहरूमा कानको दिशा घुमाउने क्षमता थियो भन्ने अवशेषाङ्गीय प्रमाण।'
  },
  wisdom: {
    nep: 'अक्कल दाँत (Wisdom Teeth)',
    eng: 'THIRD MOLARS',
    anc: 'प्राचीन मानव पूर्वजहरूले काँचो, कडा मासु, जरा र कन्दमूल चपाउनु पर्ने हुनाले च्यापु चौडा हुन्थ्यो र तेस्रो बङ्गरा (Wisdom tooth) पूर्ण उपयोगी थियो।',
    pres: 'खाना पकाएर नरम बनाएर खान थालेपछि च्यापु सानो हुँदै गयो। हाल धेरै मानिसमा अक्कल दाँत पलाउन ठाउँ नपुगेर दुखाइ हुने वा नपलाउने समस्या देखिन्छ।',
    conc: 'आहार र आहार-शैलीमा आएको परिवर्तनसँगै अङ्गहरू कसरी अवशेषी बन्दै जान्छन् भन्ने प्रमाण।'
  }
};

function selectVestigialC9U4(organ) {
  activeC9U4VestigialOrgan = organ;
  const d = C9U4_VESTIGIAL_DATA[organ];
  if (!d) return;

  const nepEl = document.getElementById('c9u4-v-nepname');
  const engEl = document.getElementById('c9u4-v-engname');
  const ancEl = document.getElementById('c9u4-v-ancestor');
  const presEl = document.getElementById('c9u4-v-present');
  const concEl = document.getElementById('c9u4-v-conclusion');

  if (nepEl) nepEl.textContent = d.nep;
  if (engEl) engEl.textContent = d.eng;
  if (ancEl) ancEl.textContent = d.anc;
  if (presEl) presEl.textContent = d.pres;
  if (concEl) concEl.textContent = d.conc;

  const organs = ['appendix', 'coccyx', 'plica', 'ear', 'wisdom'];
  organs.forEach(o => {
    const btn = document.getElementById(`c9u4-vbtn-${o}`);
    if (btn) {
      if (o === organ) {
        btn.className = 'p-3 rounded-2xl border bg-cyan-600/30 border-cyan-500 text-cyan-300 text-left transition cursor-pointer' + (o === 'wisdom' ? ' sm:col-span-2' : '');
      } else {
        btn.className = 'p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer' + (o === 'wisdom' ? ' sm:col-span-2' : '');
      }
    }
  });
}

// -------------------------------------------------------------------------
// Connecting Links Explorer
// -------------------------------------------------------------------------
const C9U4_CONNECTING_DATA = {
  archaeopteryx: {
    title: 'आर्कियोप्टेरिक्स (Archaeopteryx lithographica)',
    sci: 'JURASSIC CONNECTING LINK: REPTILIA + AVES',
    desc: 'जुरासिक कालको पत्रे चट्टानमा फेला परेको यो जीवावशेषले सरीसृप र चरा दुवैका लक्षण देखाउँछ।',
    class1: '१. सरीसृप (Reptiles) का लक्षणहरू:',
    traits1: 'जबडामा तीखा दाँत, लामो हाड भएको पुच्छर (२० कशेरुका), पखेटामा नङ्ग्रा भएका तीन औँलाहरू, कडा गैर-वायवीय हाडहरू।',
    class2: '२. चरा (Aves) का लक्षणहरू:',
    traits2: 'शरीरभरि प्वाँख (Feathers), अग्रअङ्ग पखेटामा रूपान्तरित, चुच्चो (Beak), दुई खुट्टाले टेक्न सक्ने बनावट।'
  },
  platypus: {
    title: 'डक-बिल्ड प्लाटिपस (Ornithorhynchus anatinus)',
    sci: 'LIVING CONNECTING LINK: REPTILIA + MAMMALIA',
    desc: 'अस्ट्रेलियामा पाइने यो विचित्र अर्ध-जलचर स्तनधारी जीवित संयोजक कडी हो।',
    class1: '१. सरीसृप (Reptiles) का लक्षणहरू:',
    traits1: 'अण्डा पार्ने (Oviparous), क्लोआका (Cloaca) हुनु, शरीरको तापक्रम पूर्ण स्थिर नहुनु, विषालु खुट्टाको काँडा (spur)।',
    class2: '२. स्तनधारी (Mammalia) का लक्षणहरू:',
    traits2: 'शरीरमा रौं हुनु, स्तन ग्रन्थि (Mammary glands) हुनु जसबाट बच्चालाई दूध चुसाउने, मध्य कानमा ३ हाडहरू।'
  }
};

function selectConnectingC9U4(organ) {
  activeC9U4ConnectingOrgan = organ;
  const d = C9U4_CONNECTING_DATA[organ];
  if (!d) return;

  const tEl = document.getElementById('c9u4-c-title');
  const sciEl = document.getElementById('c9u4-c-sci');
  const descEl = document.getElementById('c9u4-c-desc');
  const c1El = document.getElementById('c9u4-c-class1');
  const t1El = document.getElementById('c9u4-c-traits1');
  const c2El = document.getElementById('c9u4-c-class2');
  const t2El = document.getElementById('c9u4-c-traits2');

  if (tEl) tEl.textContent = d.title;
  if (sciEl) sciEl.textContent = d.sci;
  if (descEl) descEl.textContent = d.desc;
  if (c1El) c1El.textContent = d.class1;
  if (t1El) t1El.textContent = d.traits1;
  if (c2El) c2El.textContent = d.class2;
  if (t2El) t2El.textContent = d.traits2;

  const bAr = document.getElementById('c9u4-cbtn-archaeo');
  const bPl = document.getElementById('c9u4-cbtn-platypus');
  if (bAr) {
    bAr.className = organ === 'archaeopteryx' ?
      'p-3 rounded-2xl border bg-amber-600/30 border-amber-500 text-amber-300 text-left transition cursor-pointer' :
      'p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer';
  }
  if (bPl) {
    bPl.className = organ === 'platypus' ?
      'p-3 rounded-2xl border bg-amber-600/30 border-amber-500 text-amber-300 text-left transition cursor-pointer' :
      'p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer';
  }
}

// -------------------------------------------------------------------------
// Mode 2: Natural Selection Simulator (Peppered Moth / Industrial Melanism)
// -------------------------------------------------------------------------
const C9U4_MOTH_POSITIONS = [
  { x: 55, y: 50, rot: -14, scale: 0.82 },
  { x: 130, y: 130, rot: 18, scale: 0.85 },
  { x: 75, y: 195, rot: -8, scale: 0.8 },
  { x: 205, y: 60, rot: 15, scale: 0.84 },
  { x: 245, y: 160, rot: -20, scale: 0.88 },
  { x: 170, y: 205, rot: 32, scale: 0.78 },
  { x: 335, y: 65, rot: -10, scale: 0.85 },
  { x: 375, y: 170, rot: 14, scale: 0.82 },
  { x: 440, y: 80, rot: -26, scale: 0.8 },
  { x: 490, y: 185, rot: 12, scale: 0.85 },
  { x: 545, y: 60, rot: -14, scale: 0.82 },
  { x: 580, y: 150, rot: 25, scale: 0.78 }
];

function buildMothSVGMarkup(id, isBlack, x, y, rot, scale) {
  const bodyFill = isBlack ? '#09090b' : '#64748b';
  const wingFill = isBlack ? '#18181b' : '#f8fafc';
  const wingStroke = isBlack ? '#09090b' : '#cbd5e1';
  const speckle = isBlack ? '#27272a' : '#475569';
  const shadow = isBlack ? 'filter: drop-shadow(0 2px 5px rgba(0,0,0,0.7));' : 'filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));';

  return `
    <g id="c9u4-moth-g-${id}" class="moth-item cursor-pointer transition-all duration-300 hover:scale-110"
       transform="translate(${x}, ${y}) rotate(${rot}) scale(${scale})"
       onclick="huntMothC9U4(${id}, ${isBlack})"
       style="${shadow}">
      <!-- Left Forewing -->
      <path d="M 0,-4 Q -35,-32 -48,-12 Q -42,16 -6,8 Z" fill="${wingFill}" stroke="${wingStroke}" stroke-width="1.2"/>
      <!-- Right Forewing -->
      <path d="M 0,-4 Q 35,-32 48,-12 Q 42,16 6,8 Z" fill="${wingFill}" stroke="${wingStroke}" stroke-width="1.2"/>
      <!-- Left Hindwing -->
      <path d="M 0,2 Q -24,4 -30,22 Q -16,28 0,16 Z" fill="${wingFill}" stroke="${wingStroke}" stroke-width="0.8" opacity="0.95"/>
      <!-- Right Hindwing -->
      <path d="M 0,2 Q 24,4 30,22 Q 16,28 0,16 Z" fill="${wingFill}" stroke="${wingStroke}" stroke-width="0.8" opacity="0.95"/>
      <!-- Peppered Speckles -->
      <circle cx="-16" cy="-8" r="2.2" fill="${speckle}" opacity="0.75"/>
      <circle cx="-30" cy="-2" r="1.8" fill="${speckle}" opacity="0.75"/>
      <circle cx="-10" cy="10" r="2" fill="${speckle}" opacity="0.75"/>
      <circle cx="16" cy="-8" r="2.2" fill="${speckle}" opacity="0.75"/>
      <circle cx="30" cy="-2" r="1.8" fill="${speckle}" opacity="0.75"/>
      <circle cx="10" cy="10" r="2" fill="${speckle}" opacity="0.75"/>
      <path d="M -22,-14 Q -15,-6 -8,-12" stroke="${speckle}" stroke-width="1.2" fill="none" opacity="0.65"/>
      <path d="M 22,-14 Q 15,-6 8,-12" stroke="${speckle}" stroke-width="1.2" fill="none" opacity="0.65"/>
      <!-- Thorax & Abdomen -->
      <ellipse cx="0" cy="6" rx="4.2" ry="14" fill="${bodyFill}"/>
      <circle cx="0" cy="-7" r="3.5" fill="${bodyFill}"/>
      <!-- Antennae -->
      <path d="M -2,-9 Q -8,-20 -15,-22" stroke="${bodyFill}" stroke-width="1.3" fill="none" stroke-linecap="round"/>
      <path d="M 2,-9 Q 8,-20 15,-22" stroke="${bodyFill}" stroke-width="1.3" fill="none" stroke-linecap="round"/>
      <!-- Floating Label on hover -->
      <title>${isBlack ? 'कालो मथ (Carbonaria)' : 'सेतो मथ (Typica)'}</title>
    </g>
  `;
}

function renderMothsC9U4() {
  const barkView = document.getElementById('c9u4-bark-view');
  if (!barkView) return;

  // Determine moth counts (total 12)
  let blackCount = Math.round(12 * (c9u4BlackPct / 100));
  if (c9u4BlackPct > 0 && blackCount === 0) blackCount = 1;
  if (c9u4WhitePct > 0 && (12 - blackCount) === 0) blackCount = 11;
  let whiteCount = 12 - blackCount;

  // Distribute black moths nicely across 12 positions
  // Evenly spread black indices
  const blackIndices = new Set();
  const step = 12 / (blackCount || 1);
  for (let i = 0; i < blackCount; i++) {
    const idx = Math.min(11, Math.floor(i * step + (step / 2)));
    blackIndices.add(idx);
  }
  // Fill in if set size < blackCount
  for (let i = 0; i < 12 && blackIndices.size < blackCount; i++) {
    blackIndices.add(i);
  }

  c9u4MothsData = [];
  for (let i = 0; i < 12; i++) {
    const isBlack = blackIndices.has(i);
    c9u4MothsData.push({ id: i, isBlack: isBlack, alive: true });
  }

  // Bark Background SVG
  let barkSvgBg = '';
  if (c9u4MothEnv === 'clean') {
    // Pale Lichen Bark
    barkSvgBg = `
      <defs>
        <linearGradient id="cleanBarkGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#41523a"/>
          <stop offset="25%" stop-color="#546b4c"/>
          <stop offset="60%" stop-color="#4d6245"/>
          <stop offset="100%" stop-color="#374531"/>
        </linearGradient>
        <filter id="lichenGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
      </defs>
      <!-- Base Trunk -->
      <rect width="640" height="240" fill="url(#cleanBarkGrad)"/>
      <!-- Vertical Grain lines -->
      <g stroke="#2d3725" stroke-width="1.5" opacity="0.4">
        <path d="M 40,0 Q 45,120 35,240"/>
        <path d="M 110,0 Q 115,100 105,240"/>
        <path d="M 190,0 Q 185,140 195,240"/>
        <path d="M 280,0 Q 285,110 275,240"/>
        <path d="M 370,0 Q 365,130 375,240"/>
        <path d="M 460,0 Q 465,100 455,240"/>
        <path d="M 550,0 Q 545,150 555,240"/>
      </g>
      <!-- Lichen Patches (Pale Cream/Green covering ~65% for white moth camouflage) -->
      <g fill="#d8e2dc" opacity="0.88">
        <path d="M 20,20 Q 90,10 120,60 Q 80,110 30,90 Z"/>
        <path d="M 100,100 Q 170,80 200,140 Q 150,190 90,170 Z"/>
        <path d="M 180,30 Q 260,20 280,80 Q 220,130 170,90 Z"/>
        <path d="M 270,120 Q 350,110 380,170 Q 320,220 260,190 Z"/>
        <path d="M 360,30 Q 440,20 470,80 Q 420,130 350,90 Z"/>
        <path d="M 450,120 Q 530,100 560,160 Q 510,220 440,190 Z"/>
        <path d="M 540,20 Q 610,15 630,70 Q 590,120 530,90 Z"/>
      </g>
      <g fill="#f1faee" opacity="0.75">
        <circle cx="65" cy="55" r="32"/>
        <circle cx="140" cy="130" r="36"/>
        <circle cx="215" cy="65" r="34"/>
        <circle cx="255" cy="165" r="38"/>
        <circle cx="345" cy="70" r="35"/>
        <circle cx="385" cy="175" r="38"/>
        <circle cx="450" cy="85" r="34"/>
        <circle cx="500" cy="185" r="36"/>
        <circle cx="555" cy="65" r="35"/>
        <circle cx="590" cy="150" r="32"/>
      </g>
      <g fill="#a3b18a" opacity="0.5">
        <circle cx="85" cy="75" r="16"/>
        <circle cx="160" cy="150" r="18"/>
        <circle cx="230" cy="85" r="18"/>
        <circle cx="270" cy="185" r="20"/>
        <circle cx="360" cy="90" r="18"/>
        <circle cx="400" cy="195" r="20"/>
        <circle cx="470" cy="105" r="18"/>
        <circle cx="520" cy="205" r="20"/>
      </g>
    `;
  } else {
    // Sooty Polluted Bark
    barkSvgBg = `
      <defs>
        <linearGradient id="sootBarkGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#18181b"/>
          <stop offset="30%" stop-color="#27272a"/>
          <stop offset="70%" stop-color="#18181b"/>
          <stop offset="100%" stop-color="#09090b"/>
        </linearGradient>
      </defs>
      <!-- Base Trunk -->
      <rect width="640" height="240" fill="url(#sootBarkGrad)"/>
      <!-- Deep Charred Grain lines -->
      <g stroke="#09090b" stroke-width="2" opacity="0.8">
        <path d="M 50,0 Q 40,110 55,240"/>
        <path d="M 130,0 Q 140,120 125,240"/>
        <path d="M 210,0 Q 200,100 215,240"/>
        <path d="M 300,0 Q 310,130 295,240"/>
        <path d="M 390,0 Q 380,110 395,240"/>
        <path d="M 480,0 Q 490,140 475,240"/>
        <path d="M 570,0 Q 560,110 575,240"/>
      </g>
      <!-- Soot Stains and Smog Patches (Dark charcoal covering 85% for black moth camouflage) -->
      <g fill="#09090b" opacity="0.9">
        <circle cx="65" cy="55" r="42"/>
        <circle cx="140" cy="130" r="45"/>
        <circle cx="215" cy="65" r="44"/>
        <circle cx="255" cy="165" r="46"/>
        <circle cx="345" cy="70" r="45"/>
        <circle cx="385" cy="175" r="46"/>
        <circle cx="450" cy="85" r="44"/>
        <circle cx="500" cy="185" r="46"/>
        <circle cx="555" cy="65" r="44"/>
        <circle cx="590" cy="150" r="42"/>
      </g>
      <g fill="#3f3f46" opacity="0.25">
        <circle cx="90" cy="80" r="22"/>
        <circle cx="170" cy="155" r="25"/>
        <circle cx="240" cy="90" r="25"/>
        <circle cx="280" cy="190" r="26"/>
        <circle cx="370" cy="95" r="25"/>
        <circle cx="410" cy="200" r="26"/>
      </g>
    `;
  }

  // Render Moths
  const mothsMarkup = c9u4MothsData.map((m, i) => {
    const pos = C9U4_MOTH_POSITIONS[i];
    return buildMothSVGMarkup(m.id, m.isBlack, pos.x, pos.y, pos.rot, pos.scale);
  }).join('');

  // Assemble full SVG inside bark view
  barkView.innerHTML = `
    <svg id="c9u4-bark-svg" viewBox="0 0 640 240" class="w-full h-full select-none rounded-2xl">
      ${barkSvgBg}
      <!-- Moths Layer -->
      <g id="c9u4-moths-layer">
        ${mothsMarkup}
      </g>
      <!-- Dynamic Strike / Crosshair Effects Layer -->
      <g id="c9u4-effects-layer" pointer-events="none"></g>
      <!-- Swooping Bird Layer -->
      <g id="c9u4-bird-layer" pointer-events="none"></g>
    </svg>
  `;

  // Update counts badge
  const wCountEl = document.getElementById('c9u4-white-count');
  const bCountEl = document.getElementById('c9u4-black-count');
  if (wCountEl) wCountEl.textContent = `${whiteCount} ओटा`;
  if (bCountEl) bCountEl.textContent = `${blackCount} ओटा`;

  renderMothTimelineC9U4();
}

// -------------------------------------------------------------------------
// Moth Hunt (Predation Handler)
// -------------------------------------------------------------------------
function huntMothC9U4(id, isBlack) {
  const mothObj = c9u4MothsData.find(m => m.id === id);
  if (!mothObj || !mothObj.alive) return;

  mothObj.alive = false;
  c9u4LiveHunts++;

  const scoreEl = document.getElementById('c9u4-hunt-live-score');
  if (scoreEl) scoreEl.textContent = `शिकार: ${c9u4LiveHunts}`;

  // Audio trigger
  playMothAudioC9U4('catch');

  // Track Conspicuous vs Camouflaged
  const isConspicuous = (c9u4MothEnv === 'clean' && isBlack) || (c9u4MothEnv === 'polluted' && !isBlack);
  if (isConspicuous) {
    c9u4PredatorCaughtConspicuous++;
  } else {
    c9u4PredatorCaughtCamouflaged++;
  }

  // Visual strike effect on SVG
  const pos = C9U4_MOTH_POSITIONS[id];
  const fxLayer = document.getElementById('c9u4-effects-layer');
  if (fxLayer) {
    const strike = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    strike.innerHTML = `
      <circle cx="${pos.x}" cy="${pos.y}" r="22" stroke="#ef4444" stroke-width="2.5" fill="none" opacity="0.9">
        <animate attributeName="r" from="10" to="28" dur="0.25s" fill="freeze"/>
        <animate attributeName="opacity" from="1" to="0" dur="0.3s" fill="freeze"/>
      </circle>
      <text x="${pos.x}" y="${pos.y - 15}" fill="#ef4444" font-size="12" font-weight="900" text-anchor="middle">
        +१ शिकार!
        <animate attributeName="y" from="${pos.y - 10}" to="${pos.y - 25}" dur="0.35s" fill="freeze"/>
        <animate attributeName="opacity" from="1" to="0" dur="0.35s" fill="freeze"/>
      </text>
    `;
    fxLayer.appendChild(strike);
    setTimeout(() => {
      if (strike.parentNode) strike.parentNode.removeChild(strike);
    }, 400);
  }

  // Animate moth disappearance
  const mothEl = document.getElementById(`c9u4-moth-g-${id}`);
  if (mothEl) {
    mothEl.style.transition = 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)';
    mothEl.style.transform = `translate(${pos.x}px, ${pos.y}px) scale(0)`;
    mothEl.style.opacity = '0';
    setTimeout(() => {
      if (mothEl.parentNode) mothEl.parentNode.removeChild(mothEl);
    }, 280);
  }

  // Update live counts
  const aliveWhite = c9u4MothsData.filter(m => !m.isBlack && m.alive).length;
  const aliveBlack = c9u4MothsData.filter(m => m.isBlack && m.alive).length;
  const wCountEl = document.getElementById('c9u4-white-count');
  const bCountEl = document.getElementById('c9u4-black-count');
  if (wCountEl) wCountEl.textContent = `${aliveWhite} ओटा`;
  if (bCountEl) bCountEl.textContent = `${aliveBlack} ओटा`;
}

// -------------------------------------------------------------------------
// Next Generation Step (Bird Swoop & Natural Selection)
// -------------------------------------------------------------------------
function stepMothGenC9U4() {
  if (c9u4MothGen >= 10) return;

  c9u4MothGen++;
  playMothAudioC9U4('swoop');

  // Swooping bird silhouette
  const birdLayer = document.getElementById('c9u4-bird-layer');
  if (birdLayer) {
    birdLayer.innerHTML = `
      <g>
        <path d="M 0,0 Q 25,-18 50,0 Q 75,-18 100,0 Q 50,15 0,0 Z" fill="#09090b" opacity="0.65">
          <animateTransform attributeName="transform" type="translate" from="-120, 90" to="720, 60" dur="0.65s" fill="freeze"/>
          <animateTransform attributeName="transform" type="scale" from="0.7" to="1.2" additive="sum" dur="0.65s" fill="freeze"/>
        </path>
      </g>
    `;
    setTimeout(() => {
      if (birdLayer) birdLayer.innerHTML = '';
    }, 700);
  }

  // Natural selection population shift
  if (c9u4MothEnv === 'clean') {
    // White moths favored, black moths predated
    c9u4BlackPct = Math.max(2, c9u4BlackPct - 3);
    c9u4WhitePct = 100 - c9u4BlackPct;
  } else {
    // Black moths favored, white moths predated
    c9u4WhitePct = Math.max(2, c9u4WhitePct - 3);
    c9u4BlackPct = 100 - c9u4WhitePct;
  }

  setTimeout(() => {
    updateMothUI();
    renderMothsC9U4();
  }, 400);
}

// -------------------------------------------------------------------------
// Reset Moth Simulator
// -------------------------------------------------------------------------
function resetMothSimC9U4() {
  c9u4MothGen = 1;
  c9u4LiveHunts = 0;
  if (c9u4HuntTimerId) {
    clearInterval(c9u4HuntTimerId);
    c9u4HuntTimerId = null;
  }
  c9u4PredatorActive = false;

  const scoreEl = document.getElementById('c9u4-hunt-live-score');
  if (scoreEl) scoreEl.textContent = 'शिकार: ०';

  const timerEl = document.getElementById('c9u4-hunt-timer');
  if (timerEl) timerEl.classList.add('hidden');

  const btnHunt = document.getElementById('c9u4-btn-hunt');
  if (btnHunt) {
    btnHunt.disabled = false;
    btnHunt.className = 'px-3.5 py-2 rounded-xl text-xs font-black bg-amber-500 hover:bg-amber-400 text-slate-950 transition flex items-center gap-1.5 cursor-pointer shadow-sm';
  }

  const resBanner = document.getElementById('c9u4-hunt-result-banner');
  if (resBanner) resBanner.classList.add('hidden');

  if (c9u4MothEnv === 'clean') {
    c9u4WhitePct = 85;
    c9u4BlackPct = 15;
  } else {
    c9u4WhitePct = 15;
    c9u4BlackPct = 85;
  }

  updateMothUI();
  renderMothsC9U4();
}

// -------------------------------------------------------------------------
// Set Environment (Clean vs Polluted)
// -------------------------------------------------------------------------
function setMothEnvC9U4(env) {
  c9u4MothEnv = env;
  const bClean = document.getElementById('c9u4-env-clean-btn');
  const bPol = document.getElementById('c9u4-env-polluted-btn');
  const envLbl = document.getElementById('c9u4-moth-env-label');
  const advBadge = document.getElementById('c9u4-advantage-badge');

  if (env === 'clean') {
    if (bClean) bClean.className = 'py-2 px-3 rounded-xl border bg-emerald-600/30 border-emerald-500 text-emerald-300 font-bold transition cursor-pointer';
    if (bPol) bPol.className = 'py-2 px-3 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white font-bold transition cursor-pointer';
    if (envLbl) {
      envLbl.textContent = 'सफा वन (Clean Lichen Bark)';
      envLbl.className = 'text-xs font-mono text-emerald-400 font-bold';
    }
    if (advBadge) {
      advBadge.textContent = 'सेतो मथ अनुकूलित';
      advBadge.className = 'text-[10px] px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30';
    }
    c9u4WhitePct = 85;
    c9u4BlackPct = 15;
  } else {
    if (bClean) bClean.className = 'py-2 px-3 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white font-bold transition cursor-pointer';
    if (bPol) bPol.className = 'py-2 px-3 rounded-xl border bg-rose-600/30 border-rose-500 text-rose-300 font-bold transition cursor-pointer';
    if (envLbl) {
      envLbl.textContent = 'प्रदूषित औद्योगिक क्षेत्र (Sooty Bark)';
      envLbl.className = 'text-xs font-mono text-rose-400 font-bold';
    }
    if (advBadge) {
      advBadge.textContent = 'कालो मथ अनुकूलित';
      advBadge.className = 'text-[10px] px-2.5 py-1 rounded-full bg-purple-500/20 text-purple-300 font-bold border border-purple-500/30';
    }
    c9u4WhitePct = 15;
    c9u4BlackPct = 85;
  }

  c9u4MothGen = 1;
  updateMothUI();
  renderMothsC9U4();
}

// -------------------------------------------------------------------------
// 10-Second Predator Challenge Mini-game
// -------------------------------------------------------------------------
function startPredatorChallengeC9U4() {
  if (c9u4PredatorActive) return;

  c9u4PredatorActive = true;
  c9u4HuntTimeLeft = 10;
  c9u4PredatorCaughtConspicuous = 0;
  c9u4PredatorCaughtCamouflaged = 0;

  const btnHunt = document.getElementById('c9u4-btn-hunt');
  const timerBadge = document.getElementById('c9u4-hunt-timer');
  const resBanner = document.getElementById('c9u4-hunt-result-banner');

  if (resBanner) resBanner.classList.add('hidden');
  if (btnHunt) {
    btnHunt.disabled = true;
    btnHunt.className = 'px-3.5 py-2 rounded-xl text-xs font-black bg-slate-800 text-slate-500 cursor-not-allowed flex items-center gap-1.5 shadow-sm';
  }
  if (timerBadge) {
    timerBadge.classList.remove('hidden');
    timerBadge.textContent = `समय: १० से.`;
  }

  c9u4HuntTimerId = setInterval(() => {
    c9u4HuntTimeLeft--;
    if (timerBadge) {
      timerBadge.textContent = `समय: ${c9u4HuntTimeLeft} से.`;
    }

    if (c9u4HuntTimeLeft <= 0) {
      clearInterval(c9u4HuntTimerId);
      c9u4HuntTimerId = null;
      c9u4PredatorActive = false;

      playMothAudioC9U4('win');

      if (btnHunt) {
        btnHunt.disabled = false;
        btnHunt.className = 'px-3.5 py-2 rounded-xl text-xs font-black bg-amber-500 hover:bg-amber-400 text-slate-950 transition flex items-center gap-1.5 cursor-pointer shadow-sm';
      }
      if (timerBadge) {
        timerBadge.classList.add('hidden');
      }

      // Display Challenge Results
      if (resBanner) {
        resBanner.classList.remove('hidden');
        const titleEl = document.getElementById('c9u4-hunt-res-title');
        const descEl = document.getElementById('c9u4-hunt-res-desc');
        const total = c9u4PredatorCaughtConspicuous + c9u4PredatorCaughtCamouflaged;

        if (titleEl) {
          titleEl.textContent = `🦅 १० सेकेन्ड सिकारी चराको नतिजा (कुल शिकार: ${total} ओटा)`;
        }
        if (descEl) {
          const conspicuousName = c9u4MothEnv === 'clean' ? 'कालो' : 'सेतो';
          const camouflagedName = c9u4MothEnv === 'clean' ? 'सेतो' : 'कालो';

          descEl.innerHTML = `
            तपाईंले १० सेकेन्डमा कुल <strong>${total}</strong> ओटा मथ शिकार गर्नुभयो।
            जसमध्ये प्रस्ट देखिने <strong>${conspicuousName} मथ: ${c9u4PredatorCaughtConspicuous}</strong> ओटा र
            छलावरण मिलेका <strong>${camouflagedName} मथ: ${c9u4PredatorCaughtCamouflaged}</strong> ओटा थिए।<br/>
            💡 <strong>वैज्ञानिक निष्कर्ष:</strong> शिकारीको आँखामा छलावरण नभएका जीवहरू छिट्टै पर्ने भएकाले प्रकृतिमा अनुकूलित जीवहरूको संख्या निरन्तर वृद्धि हुन्छ।
          `;
        }
      }
    }
  }, 1000);
}

// -------------------------------------------------------------------------
// Moth Generation Timeline
// -------------------------------------------------------------------------
function renderMothTimelineC9U4() {
  const container = document.getElementById('c9u4-gen-timeline');
  if (!container) return;

  const nepDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '१०'];
  let html = '';
  for (let g = 1; g <= 10; g++) {
    const isActive = g === c9u4MothGen;
    const isPast = g < c9u4MothGen;
    let cls = 'w-6 h-6 rounded-full flex items-center justify-center font-mono text-[11px] font-bold transition';

    if (isActive) {
      cls += ' bg-purple-600 text-white ring-2 ring-purple-400 ring-offset-2 ring-offset-slate-900';
    } else if (isPast) {
      cls += ' bg-emerald-600/40 text-emerald-300 border border-emerald-500';
    } else {
      cls += ' bg-slate-800 text-slate-500 border border-slate-700';
    }

    html += `<span class="${cls}" title="पुस्ता ${nepDigits[g]}">${nepDigits[g]}</span>`;
  }
  container.innerHTML = html;
}

// -------------------------------------------------------------------------
// Update Moth UI (Bars & Diagnostics)
// -------------------------------------------------------------------------
function updateMothUI() {
  const nepDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '१०'];
  const wBar = document.getElementById('c9u4-white-bar');
  const bBar = document.getElementById('c9u4-black-bar');
  const wPct = document.getElementById('c9u4-white-pct');
  const bPct = document.getElementById('c9u4-black-pct');
  const genBadge = document.getElementById('c9u4-moth-gen-badge');
  const diagTitle = document.getElementById('c9u4-moth-diag-title');
  const diagDesc = document.getElementById('c9u4-moth-diag-desc');
  const btnNext = document.getElementById('c9u4-btn-next-gen');

  if (wBar) wBar.style.width = `${c9u4WhitePct}%`;
  if (bBar) bBar.style.width = `${c9u4BlackPct}%`;
  if (wPct) wPct.textContent = `${c9u4WhitePct}%`;
  if (bPct) bPct.textContent = `${c9u4BlackPct}%`;
  if (genBadge) genBadge.textContent = `पुस्ता ${nepDigits[c9u4MothGen] || c9u4MothGen} (Generation ${c9u4MothGen})`;

  if (btnNext) {
    if (c9u4MothGen >= 10) {
      btnNext.disabled = true;
      btnNext.className = 'px-4 py-2 rounded-xl text-xs font-black bg-slate-800 text-slate-500 cursor-not-allowed transition flex items-center gap-1.5';
    } else {
      btnNext.disabled = false;
      btnNext.className = 'px-4 py-2 rounded-xl text-xs font-black bg-purple-600 hover:bg-purple-500 text-white shadow-md transition flex items-center gap-1.5 cursor-pointer';
    }
  }

  if (diagTitle && diagDesc) {
    if (c9u4MothEnv === 'clean') {
      diagTitle.textContent = 'सफा वातावरणमा प्राकृतिक छनोट (सेतो मथको प्रभुत्व)';
      diagDesc.textContent = `सफा रुखका काण्डमा हल्का लाइकेन पलाएकाले सेता मथहरू चराको आँखाबाट बच्दछन्। पुस्ता ${c9u4MothGen} सम्म आइपुग्दा सेता मथको अनुपात ${c9u4WhitePct}% पुगेको छ र कालो मथ सजिलै शिकार बनेका छन्।`;
    } else {
      diagTitle.textContent = 'औद्योगिक वातावरणमा प्राकृतिक छनोट (कालो मथको प्रभुत्व)';
      diagDesc.textContent = `धुवाँ र कालो मुस्लोले रुखका काण्डहरू कालो भएपछि कालो मथहरू छलावरण (Camouflage) मिलेर बाँच्न सफल भएका छन्। पुस्ता ${c9u4MothGen} मा कालो मथको अनुपात ${c9u4BlackPct}% पुगेको छ; यो डार्बिनको 'योग्यतमको निरन्तरता' को ज्वलन्त प्रमाण हो।`;
    }
  }

  renderMothTimelineC9U4();
}

// -------------------------------------------------------------------------
// Mode 3: Genetic Mutation Simulator
// -------------------------------------------------------------------------
const C9U4_MUTATION_DATA = {
  polydactyly: {
    title: '६ वटा औँलाहरू (Polydactyly)',
    badge: 'AUTOSOMAL DOMINANT',
    desc: 'औँलाको संख्या निर्धारण गर्ने नियामक वंशाणुमा भएको आकस्मिक उत्परिवर्तनले गर्दा हात वा खुट्टामा अतिरिक्त औँला थपिन्छ। यो उत्परिवर्तन वंशाणुगत रूपमा सन्तानमा सर्दछ।',
    evo: '💡 <strong>क्रमविकासमा भूमिका:</strong> यसले प्राकृतिक जनसंख्यामा नयाँ आनुवंशिक विविधता (Variation) ल्याउँछ।'
  },
  albinism: {
    title: 'अल्बिनिजम (Melanin Loss Mutation)',
    badge: 'RECESSIVE MUTATION',
    desc: 'छाला, रौँ र आँखामा मेलानिन पिग्मेन्ट बनाउने टाइरोसिनेज इन्जाइमको वंशाणुमा उत्परिवर्तन हुँदा शरीर पूर्ण सेतो हुन्छ।',
    evo: '💡 <strong>क्रमविकासमा भूमिका:</strong> जंगलमा छलावरण गुम्ने हुनाले प्राकृतिक छनोटले यस्ता हानिकारक उत्परिवर्तनलाई हटाउने प्रयास गर्छ।'
  },
  sickle: {
    title: 'हँसिया आकारको आरबीसी (Sickle Cell Anemia)',
    badge: 'POINT MUTATION (HbS)',
    desc: 'हेमोग्लोबिनको बिटा-चेनको ६ औँ स्थानमा ग्लुटामिक एसिडको सट्टा भ्यालिन एमिनो एसिड प्रतिस्थापन हुँदा आरबीसी हँसिया जस्तो बन्दछ।',
    evo: '💡 <strong>क्रमविकासमा भूमिका:</strong> अफ्रिका र तराईमा यस गुण भएका विषमयुग्मजी व्यक्तिहरू औलो (Malaria) बाट जोगिने हुनाले प्राकृतिक छनोटले संरक्षण गर्छ।'
  },
  evening: {
    title: 'इभनिङ प्रिमरोज (Hugo De Vries Mutation)',
    badge: 'MUTATION THEORY FOUNDATION',
    desc: 'ह्युगो डी भ्रिजले सन् १९०१ मा ओएनोथेरा लामार्किआनामा अचानक देखा परेका नयाँ भिन्नताहरूको अध्ययन गरी उत्परिवर्तन सिद्धान्त प्रतिपादन गरेका थिए।',
    evo: '💡 <strong>क्रमविकासमा भूमिका:</strong> एकल पुस्तामै नयाँ लक्षण विकास भई क्रमिक परिवृत्तिविना नै नयाँ प्रजाति बन्न सक्छ भन्ने पुष्टि गर्‍यो।'
  }
};

function renderMutationSVGC9U4(type) {
  const wrap = document.getElementById('c9u4-mutation-svg-wrap');
  if (!wrap) return;

  if (type === 'polydactyly') {
    wrap.innerHTML = `
      <svg viewBox="0 0 340 180" class="w-full max-w-[340px] h-auto select-none">
        <text x="170" y="20" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">🖐️ हातमा ६ वटा औँलाहरू (Polydactyly)</text>
        <path d="M 100,160 C 90,120 90,95 120,80 C 150,75 190,75 220,85 C 240,100 240,130 230,160 Z" fill="#334155" stroke="#475569" stroke-width="2"/>
        <rect x="80" y="90" width="18" height="42" rx="9" transform="rotate(-30 80 90)" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
        <rect x="120" y="40" width="16" height="50" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
        <rect x="145" y="30" width="16" height="58" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
        <rect x="170" y="35" width="16" height="54" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
        <rect x="195" y="50" width="16" height="42" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
        <g filter="drop-shadow(0 0 8px rgba(244,63,94,0.8))">
          <rect x="52" y="105" width="18" height="40" rx="9" transform="rotate(-50 52 105)" fill="#f43f5e" stroke="#fda4af" stroke-width="2"/>
        </g>
        <text x="40" y="165" fill="#f43f5e" font-size="10" font-weight="bold">★ अतिरिक्त औँला (६th Digit)</text>
        <text x="260" y="165" fill="#94a3b8" font-size="9">सामान्य ५ औँलाहरू</text>
      </svg>
    `;
  } else if (type === 'sickle') {
    wrap.innerHTML = `
      <svg viewBox="0 0 340 180" class="w-full max-w-[340px] h-auto select-none">
        <text x="170" y="20" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">🩸 सामान्य RBC बनाम हँसिया आकारको RBC (Sickle Cell)</text>
        <circle cx="90" cy="95" r="42" fill="#ef4444" stroke="#b91c1c" stroke-width="2.5"/>
        <circle cx="90" cy="95" r="22" fill="#dc2626" opacity="0.6"/>
        <text x="90" y="155" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">सामान्य RBC (गोलो/लचिलो)</text>
        <text x="90" y="170" fill="#94a3b8" font-size="8" text-anchor="middle">अक्सिजन पूर्ण रूपमा बोक्ने</text>
        <path d="M 210,60 C 265,60 280,120 230,135 C 245,115 240,85 210,60 Z" fill="#f43f5e" stroke="#9f1239" stroke-width="2.5"/>
        <text x="245" y="155" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">हँसिया RBC (कडा/साँगुरो)</text>
        <text x="245" y="170" fill="#94a3b8" font-size="8" text-anchor="middle">रक्तनलीमा अड्किने / औलो प्रतिरोधी</text>
      </svg>
    `;
  } else if (type === 'albinism') {
    wrap.innerHTML = `
      <svg viewBox="0 0 340 180" class="w-full max-w-[340px] h-auto select-none">
        <text x="170" y="20" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">🐭 मेलानिन गुम्ने उत्परिवर्तन (Albinism Mutation)</text>
        <!-- Pigmented Wild-Type Animal (Brown) -->
        <g transform="translate(60, 60)">
          <ellipse cx="30" cy="35" rx="30" ry="22" fill="#78350f" stroke="#451a03" stroke-width="1.5"/>
          <circle cx="55" cy="25" r="16" fill="#78350f" stroke="#451a03" stroke-width="1.5"/>
          <circle cx="62" cy="22" r="3" fill="#09090b"/>
          <ellipse cx="48" cy="10" rx="6" ry="10" fill="#92400e"/>
          <text x="30" y="75" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">सामान्य (मेलानिनयुक्त)</text>
        </g>
        <!-- Albino Animal (Pure White, Pink eyes) -->
        <g transform="translate(200, 60)">
          <ellipse cx="30" cy="35" rx="30" ry="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
          <circle cx="55" cy="25" r="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
          <circle cx="62" cy="22" r="3" fill="#f43f5e"/>
          <ellipse cx="48" cy="10" rx="6" ry="10" fill="#fda4af"/>
          <text x="30" y="75" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">अल्बिनो (रंगविहीन सेतो)</text>
        </g>
        <text x="170" y="165" fill="#94a3b8" font-size="8.5" text-anchor="middle">टाइरोसिनेज इन्जाइमको अभावले मेलानिन उत्पादन बन्द</text>
      </svg>
    `;
  } else {
    // Evening Primrose (Hugo de Vries)
    wrap.innerHTML = `
      <svg viewBox="0 0 340 180" class="w-full max-w-[340px] h-auto select-none">
        <text x="170" y="20" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">🌸 इभनिङ प्रिमरोज (Hugo De Vries Mutation)</text>
        <!-- Normal Flower (Diploid 2n) -->
        <g transform="translate(80, 85)">
          <circle cx="0" cy="0" r="10" fill="#f59e0b"/>
          <ellipse cx="0" cy="-22" rx="10" ry="14" fill="#fde047" stroke="#eab308"/>
          <ellipse cx="0" cy="22" rx="10" ry="14" fill="#fde047" stroke="#eab308"/>
          <ellipse cx="-22" cy="0" rx="14" ry="10" fill="#fde047" stroke="#eab308"/>
          <ellipse cx="22" cy="0" rx="14" ry="10" fill="#fde047" stroke="#eab308"/>
          <text x="0" y="55" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">सामान्य फूल (2n)</text>
        </g>
        <!-- Giant Mutant Flower (Oenothera gigas / Tetraploid 4n) -->
        <g transform="translate(240, 85)">
          <circle cx="0" cy="0" r="14" fill="#d97706"/>
          <g filter="drop-shadow(0 0 6px rgba(234,179,8,0.7))">
            <ellipse cx="0" cy="-30" rx="14" ry="20" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
            <ellipse cx="0" cy="30" rx="14" ry="20" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
            <ellipse cx="-30" cy="0" rx="20" ry="14" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
            <ellipse cx="30" cy="0" rx="20" ry="14" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
            <ellipse cx="-20" cy="-20" rx="12" ry="16" transform="rotate(-45 -20 -20)" fill="#fef08a"/>
            <ellipse cx="20" cy="-20" rx="12" ry="16" transform="rotate(45 20 -20)" fill="#fef08a"/>
            <ellipse cx="-20" cy="20" rx="12" ry="16" transform="rotate(45 -20 20)" fill="#fef08a"/>
            <ellipse cx="20" cy="20" rx="12" ry="16" transform="rotate(-45 20 20)" fill="#fef08a"/>
          </g>
          <text x="0" y="60" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle">विशाल उत्परिवर्ती (4n Gigas)</text>
        </g>
        <text x="170" y="168" fill="#94a3b8" font-size="8.5" text-anchor="middle">एकै पुस्तामा क्रोमोजोम दोब्बर भई नयाँ प्रजाति निर्माण</text>
      </svg>
    `;
  }
}

function selectMutationDemoC9U4(type) {
  activeC9U4Mutation = type;
  const d = C9U4_MUTATION_DATA[type];
  if (!d) return;

  const tEl = document.getElementById('c9u4-mu-title');
  const bEl = document.getElementById('c9u4-mu-badge');
  const descEl = document.getElementById('c9u4-mu-desc');
  const evoEl = document.getElementById('c9u4-mu-evolution');

  if (tEl) tEl.textContent = d.title;
  if (bEl) bEl.textContent = d.badge;
  if (descEl) descEl.textContent = d.desc;
  if (evoEl) evoEl.innerHTML = d.evo;

  const types = ['polydactyly', 'albinism', 'sickle', 'evening'];
  const ids = ['poly', 'albi', 'sickle', 'evening'];
  types.forEach((t, i) => {
    const btn = document.getElementById(`c9u4-mubtn-${ids[i]}`);
    if (btn) {
      if (t === type) {
        btn.className = 'p-2.5 rounded-xl border bg-rose-600/30 border-rose-500 text-rose-300 text-left transition cursor-pointer';
      } else {
        btn.className = 'p-2.5 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer';
      }
    }
  });

  renderMutationSVGC9U4(type);
}

// -------------------------------------------------------------------------
// Exercise Filtering
// -------------------------------------------------------------------------
function filterC9U4Exercises(cat) {
  const cards = document.querySelectorAll('.c9u4-ex-card');
  cards.forEach(card => {
    if (cat === 'all' || card.dataset.cat === cat) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  const cats = ['all', 'mcq', 'reason', 'diff', 'qa', 'project'];
  cats.forEach(c => {
    const btn = document.getElementById(`c9u4-exbtn-${c}`);
    if (btn) {
      if (c === cat) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-black transition bg-purple-600 text-white shadow-sm cursor-pointer whitespace-nowrap';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap';
      }
    }
  });
}

// -------------------------------------------------------------------------
// Tier Filtering
// -------------------------------------------------------------------------
function filterC9U4Tiers(tier) {
  const cards = document.querySelectorAll('.c9u4-tier-card');
  cards.forEach(card => {
    if (tier === 'all' || card.dataset.tier === tier) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  const tiers = ['all', 'k', 'u', 'ha'];
  tiers.forEach(t => {
    const btn = document.getElementById(`c9u4-tierbtn-${t}`);
    if (btn) {
      if (t === tier) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-black transition bg-purple-600 text-white shadow-sm cursor-pointer whitespace-nowrap';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap';
      }
    }
  });
}

// -------------------------------------------------------------------------
// Quiz Data & Engine
// -------------------------------------------------------------------------
const C9U4_QUIZ_DATA = [
  {
    q: '१. प्राकृतिक छनोट (Natural Selection) सिद्धान्तका प्रतिपादक को हुन्?',
    options: [
      'जाँ ब्याप्टिस्ट लेमार्क',
      'चार्ल्स डार्बिन',
      'ह्युगो डी भ्रिज',
      'ग्रेगर मेन्डेल'
    ],
    correct: 1,
    exp: 'चार्ल्स डार्बिनले सन् १८५९ मा "On the Origin of Species" पुस्तक मार्फत प्राकृतिक छनोटको सिद्धान्त प्रतिपादन गरेका हुन्।'
  },
  {
    q: '२. होमोलोगस (समधर्मी) अङ्गको उपयुक्त उदाहरण कुन हो?',
    options: [
      'मानिसको हात र घोडाको अगाडिको खुट्टा',
      'चराको पखेटा र पुतलीको पखेटा',
      'चमेराको पखेटा र माहुरीको पखेटा',
      'माछाको पखेटा र ह्वेलको पुच्छर'
    ],
    correct: 0,
    exp: 'मानिसको हात र घोडाको खुट्टाको आन्तरिक हाडको संरचना (Humerus, Radius, Ulna आदि) एउटै हुन्छ तर कार्य फरक हुन्छ।'
  },
  {
    q: '३. जीवावशेष (Fossils) मुख्यतया कुन प्रकारको चट्टानमा सुरक्षित भेटिन्छन्?',
    options: [
      'आग्नेय चट्टान (Igneous rock)',
      'पत्रे चट्टान (Sedimentary rock)',
      'रूपान्तरित चट्टान (Metamorphic rock)',
      'लाभा चट्टान (Volcanic rock)'
    ],
    correct: 1,
    exp: 'पत्रे चट्टान पानी वा हावाले थुपारेका तहहरूबाट बिस्तारै चाप परेर बन्ने हुँदा मृत जीवका अवशेष सुरक्षित रहन्छन्।'
  },
  {
    q: '४. जीवको वंशाणु संरचना (DNA) मा आउने आकस्मिक र स्थायी परिवर्तनलाई के भनिन्छ?',
    options: [
      'प्राकृतिक छनोट (Natural Selection)',
      'परिवृत्ति (Variation)',
      'उत्परिवर्तन (Mutation)',
      'अनुकूलन (Adaptation)'
    ],
    correct: 2,
    exp: 'डिएनए वा क्रोमोजोमको रासायनिक संरचनामा अचानक हुने स्थायी र वंशाणुगत परिवर्तनलाई उत्परिवर्तन भनिन्छ।'
  },
  {
    q: '५. सरीसृप र चरा दुवै वर्गका गुणहरू भएको ऐतिहासिक संयोजक कडी (Connecting link) कुन हो?',
    options: [
      'डक-बिल्ड प्लाटिपस (Platypus)',
      'आर्कियोप्टेरिक्स (Archaeopteryx)',
      'पेरिप्याटस (Peripatus)',
      'सिलकान्थ (Coelacanth)'
    ],
    correct: 1,
    exp: 'आर्कियोप्टेरिक्समा सरीसृप जस्तो दाँत र लामो पुच्छर तथा चरा जस्तो प्वाँख र पखेटा दुवै पाइएकाले यो सरीसृप र चरा बीचको संयोजक कडी हो।'
  },
  {
    q: '६. मानव शरीरमा सेलुलोज पचाउने पूर्वजहरूको अवशेषका रूपमा रहेको अवशेषाङ्ग कुन हो?',
    options: [
      'कलेजो (Liver)',
      'भर्मिफर्म एपेन्डिक्स (Appendix)',
      'फियो (Spleen)',
      'पित्तथैली (Gallbladder)'
    ],
    correct: 1,
    exp: 'हाम्रा प्राचीन शाकाहारी पूर्वजहरूमा काँचो घाँसपातको सेलुलोज पचाउन ठूलो एपेन्डिक्स आवश्यक थियो, जुन अहिले मानिसमा निष्प्रयोजन अवशेषाङ्ग बनेको छ।'
  },
  {
    q: '७. "उपार्जित गुणहरूको वंशाणुगतता" को सिद्धान्त कसले प्रतिपादन गरेका थिए?',
    options: [
      'चार्ल्स डार्बिन',
      'जाँ ब्याप्टिस्ट लेमार्क',
      'अगस्ट विजम्यान',
      'अल्फ्रेड वालेस'
    ],
    correct: 1,
    exp: 'फ्रान्सेली वैज्ञानिक लेमार्कले सन् १८०९ मा "Philosophie Zoologique" पुस्तकमा उपार्जित गुणहरूको वंशाणुगतता सिद्धान्त प्रस्तुत गरेका थिए।'
  },
  {
    q: '८. मुसाको पुच्छर लगातार २२ पुस्तासम्म काटेर लेमार्कको सिद्धान्तलाई गलत प्रमाणित गर्ने वैज्ञानिक को हुन्?',
    options: [
      'अगस्ट विजम्यान (August Weismann)',
      'थोमस माल्थस (Thomas Malthus)',
      'ह्युगो डी भ्रिज (Hugo de Vries)',
      'कार्ल लिनियस (Carl Linnaeus)'
    ],
    correct: 0,
    exp: 'अगस्ट विजम्यानले २२ पुस्तासम्म पुच्छर काटे तापनि पुच्छरविहीन मुसा नजन्मेपछि सोम्याटोप्लाज्मको परिवर्तन जननकोषमा नसर्ने प्रमाणित गरे।'
  },
  {
    q: '९. ह्युगो डी भ्रिजले आफ्नो उत्परिवर्तन सिद्धान्त कुन वनस्पतिमा अध्ययन गरी प्रतिपादन गरेका थिए?',
    options: [
      'केराउ (Pisum sativum)',
      'इभनिङ प्रिमरोज (Oenothera lamarckiana)',
      'तोरी (Brassica campestris)',
      'मकै (Zea mays)'
    ],
    correct: 1,
    exp: 'ह्युगो डी भ्रिजले सन् १९०१ मा इभनिङ प्रिमरोज (Oenothera lamarckiana) मा आकस्मिक परिवर्तनहरूको अध्ययन गरी उत्परिवर्तन सिद्धान्त प्रतिपादन गरे।'
  },
  {
    q: '१०. बेलायतमा औद्योगिक क्रान्तिपछि रूखको काण्ड कालो हुँदा कालो पेपर्ड मथको संख्या बढ्नु के को उदाहरण हो?',
    options: [
      'कृत्रिम छनोट (Artificial Selection)',
      'लेमार्कको उपार्जित गुण',
      'औद्योगिक कालोपन र प्राकृतिक छनोट (Industrial Melanism)',
      'भौगोलिक अलगाव (Geographic Isolation)'
    ],
    correct: 2,
    exp: 'कालो पृष्ठभूमिमा कालो मथहरू छलावरण मिली चराको आँखाबाट बच्न सके र बाँचेर सन्तान बढाए, जुन प्राकृतिक छनोटको ज्वलन्त उदाहरण हो।'
  }
];

function renderC9U4Quiz() {
  const container = document.getElementById('c9u4-quiz-container');
  if (!container) return;

  container.innerHTML = C9U4_QUIZ_DATA.map((item, qIdx) => {
    const answered = c9u4QuizAnswers[qIdx] !== undefined;
    const userChoice = c9u4QuizAnswers[qIdx];
    const isCorrect = userChoice === item.correct;

    return `
      <div class="bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-slate-400">प्रश्न ${qIdx + 1} / १०</span>
          ${answered ? (isCorrect ? '<span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">✓ सही उत्तर</span>' : '<span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-rose-100 text-rose-800">✗ गलत उत्तर</span>') : ''}
        </div>
        <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
          ${item.options.map((opt, optIdx) => {
            let btnCls = 'bg-slate-50 border-slate-200 text-slate-700 hover:bg-slate-100';
            if (answered) {
              if (optIdx === item.correct) {
                btnCls = 'bg-emerald-50 border-emerald-500 text-emerald-900 font-bold';
              } else if (optIdx === userChoice) {
                btnCls = 'bg-rose-50 border-rose-500 text-rose-900 font-bold';
              } else {
                btnCls = 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
              }
            }

            return `
              <button onclick="selectC9U4QuizOption(${qIdx}, ${optIdx})" ${answered ? 'disabled' : ''} class="p-3 rounded-2xl border text-left transition flex items-center gap-2 ${btnCls} cursor-pointer">
                <span class="w-6 h-6 rounded-full bg-white border flex items-center justify-center text-xs font-black text-slate-500 shrink-0">
                  ${['क', 'ख', 'ग', 'घ'][optIdx]}
                </span>
                <span class="text-xs md:text-sm">${opt}</span>
              </button>
            `;
          }).join('')}
        </div>

        ${answered ? `
          <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 text-xs text-slate-600 space-y-1">
            <strong class="text-slate-900 block">💡 व्याख्या:</strong>
            <p>${item.exp}</p>
          </div>
        ` : ''}
      </div>
    `;
  }).join('');

  updateC9U4QuizScore();
}

function selectC9U4QuizOption(qIdx, optIdx) {
  if (c9u4QuizAnswers[qIdx] !== undefined) return;
  c9u4QuizAnswers[qIdx] = optIdx;
  renderC9U4Quiz();
}

function updateC9U4QuizScore() {
  const badge = document.getElementById('c9u4-quiz-score-badge');
  if (!badge) return;

  let score = 0;
  Object.keys(c9u4QuizAnswers).forEach(qIdx => {
    if (c9u4QuizAnswers[qIdx] === C9U4_QUIZ_DATA[qIdx].correct) {
      score++;
    }
  });

  const nepDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '१०'];
  badge.textContent = `${nepDigits[score]} / १०`;
}

function resetC9U4Quiz() {
  c9u4QuizAnswers = {};
  renderC9U4Quiz();
}

// -------------------------------------------------------------------------
// Global Initialization for Unit 4
// -------------------------------------------------------------------------
function initC9U4() {
  renderHomologySVGC9U4(activeC9U4HomologyOrgan);
  selectVestigialC9U4(activeC9U4VestigialOrgan);
  selectConnectingC9U4(activeC9U4ConnectingOrgan);
  renderMothsC9U4();
  updateMothUI();
  renderMutationSVGC9U4(activeC9U4Mutation);
  renderC9U4Quiz();
}

// Ensure startup trigger
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initC9U4);
} else {
  initC9U4();
}
