# -*- coding: utf-8 -*-
"""
Class 9 Science Unit 6: JavaScript Controller & SVG Generators
"""
import sys

print("Generating scratch/c9u6_js.js...")

js_code = r'''
// =========================================================================
// GRADE 9 UNIT 6: NATURE AND ENVIRONMENT (प्रकृति र वातावरण)
// =========================================================================

let activeC9U6Tab = 'concepts';
let activeC9U6LabMode = 'ecosystem';
let activeC9U6EcoType = 'grassland';
let activeC9U6Organism = 'grass';

let activeC9U6EnergySub = 'pyramid';
let c9u6SolarInput = 100000;
let c9u6CascadeScenario = 'normal';

let activeC9U6Interaction = 'mutualism';

let c9u6QuizAnswers = {};

// -------------------------------------------------------------------------
// Web Audio Synthesizer (Zero External Dependencies)
// -------------------------------------------------------------------------
let c9u6AudioCtx = null;
function playAudioC9U6(type) {
  try {
    if (!c9u6AudioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) c9u6AudioCtx = new AudioContext();
    }
    if (!c9u6AudioCtx) return;
    if (c9u6AudioCtx.state === 'suspended') {
      c9u6AudioCtx.resume();
    }
    const t = c9u6AudioCtx.currentTime;
    const osc = c9u6AudioCtx.createOscillator();
    const gain = c9u6AudioCtx.createGain();
    osc.connect(gain);
    gain.connect(c9u6AudioCtx.destination);

    if (type === 'click') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(620, t);
      osc.frequency.exponentialRampToValueAtTime(840, t + 0.05);
      gain.gain.setValueAtTime(0.12, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.06);
      osc.start(t);
      osc.stop(t + 0.06);
    } else if (type === 'energy') {
      [440, 554.37, 659.25, 880].forEach((freq, idx) => {
        const o = c9u6AudioCtx.createOscillator();
        const g = c9u6AudioCtx.createGain();
        o.connect(g);
        g.connect(c9u6AudioCtx.destination);
        o.type = 'triangle';
        o.frequency.setValueAtTime(freq, t + idx * 0.06);
        g.gain.setValueAtTime(0.14, t + idx * 0.06);
        g.gain.exponentialRampToValueAtTime(0.01, t + idx * 0.06 + 0.2);
        o.start(t + idx * 0.06);
        o.stop(t + idx * 0.06 + 0.2);
      });
    } else if (type === 'alert') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(320, t);
      osc.frequency.setValueAtTime(240, t + 0.12);
      gain.gain.setValueAtTime(0.18, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.25);
      osc.start(t);
      osc.stop(t + 0.25);
    } else if (type === 'correct') {
      [523.25, 659.25, 783.99, 1046.5].forEach((freq, idx) => {
        const o = c9u6AudioCtx.createOscillator();
        const g = c9u6AudioCtx.createGain();
        o.connect(g);
        g.connect(c9u6AudioCtx.destination);
        o.type = 'sine';
        o.frequency.setValueAtTime(freq, t + idx * 0.08);
        g.gain.setValueAtTime(0.15, t + idx * 0.08);
        g.gain.exponentialRampToValueAtTime(0.01, t + idx * 0.08 + 0.25);
        o.start(t + idx * 0.08);
        o.stop(t + idx * 0.08 + 0.25);
      });
    } else if (type === 'wrong') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(180, t);
      osc.frequency.setValueAtTime(130, t + 0.1);
      gain.gain.setValueAtTime(0.2, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.25);
      osc.start(t);
      osc.stop(t + 0.25);
    }
  } catch (e) {
    // Silently continue if audio context is blocked
  }
}

// -------------------------------------------------------------------------
// Navigation: 4 Main Tabs
// -------------------------------------------------------------------------
function setTabC9U6(tab) {
  activeC9U6Tab = tab;
  playAudioC9U6('click');
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const view = document.getElementById(`c9u6-view-${t}`);
    const btn = document.getElementById(`c9u6-tab-${t}`);
    if (view) {
      if (t === tab) view.classList.remove('hidden');
      else view.classList.add('hidden');
    }
    if (btn) {
      if (t === tab) {
        btn.className = "px-5 py-2.5 rounded-xl bg-emerald-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer";
      } else {
        btn.className = "px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer";
      }
    }
  });

  if (tab === 'concepts') {
    renderCurrentC9U6Lab();
  } else if (tab === 'quiz') {
    renderC9U6Quiz();
  }
}

// -------------------------------------------------------------------------
// Lab Modes Switcher (Mode 1, Mode 2, Mode 3)
// -------------------------------------------------------------------------
function setLabModeC9U6(mode) {
  activeC9U6LabMode = mode;
  playAudioC9U6('click');
  const modes = ['ecosystem', 'energy_web', 'interactions'];
  modes.forEach(m => {
    const panel = document.getElementById(`c9u6-lab-mode-${m}`);
    const btn = document.getElementById(`c9u6-btn-mode-${m}`);
    if (panel) {
      if (m === mode) panel.classList.remove('hidden');
      else panel.classList.add('hidden');
    }
    if (btn) {
      if (m === mode) {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-gradient-to-r from-emerald-600 to-teal-600 text-white font-black text-xs md:text-sm shadow-md transition cursor-pointer";
      } else {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-slate-800 text-slate-400 hover:text-white font-bold text-xs md:text-sm transition cursor-pointer";
      }
    }
  });
  renderCurrentC9U6Lab();
}

function renderCurrentC9U6Lab() {
  if (activeC9U6LabMode === 'ecosystem') {
    renderEcosystemSVGC9U6(activeC9U6EcoType, activeC9U6Organism);
    updateOrganismInfoC9U6(activeC9U6Organism);
  } else if (activeC9U6LabMode === 'energy_web') {
    if (activeC9U6EnergySub === 'pyramid') {
      renderPyramidSVGC9U6();
    } else {
      renderCascadeSVGC9U6(c9u6CascadeScenario);
    }
  } else if (activeC9U6LabMode === 'interactions') {
    renderInteractionSVGC9U6(activeC9U6Interaction);
    updateInteractionInfoC9U6(activeC9U6Interaction);
  }
}

// =========================================================================
// MODE 1: ECOSYSTEM SIMULATOR (GRASSLAND VS POND)
// =========================================================================

const C9U6_ORGANISMS_DATA = {
  // Grassland
  grass: {
    name: 'हरियो घाँस / दुबो (Producers)',
    trophic: 'TROPHIC LEVEL: T1 (उत्पादक)',
    diet: 'स्वपोषी (Autotroph)',
    energy: 'सूर्यको सौर्य ऊर्जाको करिब १% सोसेर प्रकाश संश्लेषणद्वारा प्रति वर्गमिटर १०,००० J रासायनिक ग्लुकोज बनाउँछ।',
    role: 'चउरको आधारभूत खाद्य जग; माटोलाई जराले समातेर भू-क्षय रोक्ने र वातावरणमा अक्सिजन उत्सर्जन गर्ने।',
    desc: 'घाँस नष्ट भएमा सम्पूर्ण शाकाहारी जीव भोकै पर्छन् र चउरको पारिस्थिक संरचना क्षणभरमै भत्किन्छ।'
  },
  grasshopper: {
    name: 'फट्याङ्ग्रा (Grasshopper)',
    trophic: 'TROPHIC LEVEL: T2 (प्राथमिक उपभोक्ता)',
    diet: 'शाकाहारी (Herbivore)',
    energy: 'घाँसको १०% ऊर्जा (१,००० J) ग्रहण गर्छ; बाँकी ९०% ऊर्जा चाल र श्वासप्रश्वासमा खर्च हुन्छ।',
    role: 'हरियो घाँस खाएर वनस्पतिलाई नियन्त्रण गर्ने र भ्यागुता, चराहरूको मुख्य आहारा बन्ने।',
    desc: 'यसको संख्या अनियन्त्रित बढ्दा घाँस सखाप भई खडेरी र मरुभूमिकरणको जोखिम बढ्दछ।'
  },
  frog: {
    name: 'भ्यागुता (Frog)',
    trophic: 'TROPHIC LEVEL: T3 (द्वितीयक उपभोक्ता)',
    diet: 'प्राथमिक मांसाहारी (Carnivore)',
    energy: 'फट्याङ्ग्राबाट १०० J ऊर्जा प्राप्त गर्छ; आहाराको १० गुणा ऊर्जा क्षय हुन्छ।',
    role: 'हानिकारक किरा-फट्याङ्ग्रा खाएर नियन्त्रण गर्ने तथा सर्प र चिलको आहारा बन्ने उभयचर कडी।',
    desc: 'भ्यागुता लोप भएमा किराहरूको प्रकोप बढ्छ र सर्पहरू आहाराको खोजीमा बस्ती पस्न थाल्छन्।'
  },
  snake: {
    name: 'सर्प (Snake)',
    trophic: 'TROPHIC LEVEL: T4 (तृतीयक उपभोक्ता)',
    diet: 'मांसाहारी (Secondary Carnivore)',
    energy: 'भ्यागुताबाट १० J ऊर्जा प्राप्त गर्छ।',
    role: 'भ्यागुता र मुसाको संख्या नियन्त्रण गरी अन्नबाली सुरक्षामा सहयोग गर्ने किसानको मित्र।',
    desc: 'सर्प नष्ट हुँदा मुसाको अनियन्त्रित वृद्धि भई खेतको धानबाली र अन्न भण्डार नष्ट हुन्छ।'
  },
  eagle: {
    name: 'चिल / बाज (Hawk / Eagle)',
    trophic: 'TROPHIC LEVEL: T5 (सर्वोच्च मांसाहारी - Apex)',
    diet: 'शीर्ष सिकारी (Apex Predator)',
    energy: 'सर्पबाट १ J ऊर्जा मात्र प्राप्त गर्छ; यसभन्दा माथि जीवन धान्न ऊर्जा नपुग्ने हुनाले शृङ्खला समाप्त हुन्छ।',
    role: 'चउरको सर्वोच्च सिकारी; कमजोर र बिरामी सर्प तथा मुसा मारेर प्राकृतिक छनोट कायम राख्ने।',
    desc: 'इकोसिस्टमको स्वास्थ्य मापन गर्ने प्रमुख सूचक प्रजाति (Keystone species)।'
  },

  // Pond
  phytoplankton: {
    name: 'फाइटोप्ल्याङ्कटन / सूक्ष्म लेउ (Algae)',
    trophic: 'TROPHIC LEVEL: T1 (जलीय उत्पादक)',
    diet: 'स्वपोषी (Microscopic Autotroph)',
    energy: 'पोखरीको पानीमा छिर्ने सौर्य प्रकाश र घुलित CO2 बाट प्रकाश संश्लेषण गरी खाना र अक्सिजन बनाउँछ।',
    role: 'जलीय खाद्य शृङ्खलाको आधारशिला; पानीमा घुलित अक्सिजन (DO) को मुख्य उत्पादक।',
    desc: 'यसको अभावमा पोखरीका सम्पूर्ण माछा र जलचर अक्सिजन र खानाको अभावमा मर्छन्।'
  },
  zooplankton: {
    name: 'जुप्ल्याङ्कटन (Daphnia & Cyclops)',
    trophic: 'TROPHIC LEVEL: T2 (प्राथमिक जल-उपभोक्ता)',
    diet: 'शाकाहारी जलचर (Herbivore)',
    energy: 'फाइटोप्ल्याङ्कटनबाट १०% ऊर्जा सोसेर साना माछाहरूका लागि पोषण उपलब्ध गराउँछ।',
    role: 'लेउलाई खाएर पोखरीमा लेउको अत्यधिक वृद्धि (Algal bloom) रोक्ने सूक्ष्म जलचर।',
    desc: 'यिनीहरू पानीको प्रदूषण र अम्लीयपनप्रति निकै संवेदनशील जैविक सूचक हुन्।'
  },
  small_fish: {
    name: 'साना माछा (Small Fish / Puntius)',
    trophic: 'TROPHIC LEVEL: T3 (द्वितीयक उपभोक्ता)',
    diet: 'मांसाहारी जलचर (Carnivore)',
    energy: 'जुप्ल्याङ्कटन र लामखुट्टेका लार्भा खाएर ऊर्जाको १०% भाग सञ्चित गर्छ।',
    role: 'लामखुट्टेका लार्भा नष्ट गरी मलेरिया, डेंगु नियन्त्रण गर्ने र ठूला माछाको आहारा बन्ने।',
    desc: 'साना माछा हराएमा पोखरीमा हानिकारक कीटाणु र लामखुट्टेको आतंक फैलिन्छ।'
  },
  big_fish: {
    name: 'ठूला माछा (Large Fish / Catfish)',
    trophic: 'TROPHIC LEVEL: T4 (तृतीयक उपभोक्ता)',
    diet: 'ठूला मांसाहारी (Large Carnivore)',
    energy: 'साना माछाबाट १०% ऊर्जा पाउँछ।',
    role: 'कमजोर र रोगी साना माछाहरूको सिकार गरी पोखरीको माछा समुदायलाई निरोगी राख्ने।',
    desc: 'यसको अत्यधिक सिकार गर्दा साना माछा अनियन्त्रित भई जुप्ल्याङ्कटन सखाप हुन्छन्।'
  },
  heron: {
    name: 'बकुल्ला / हाँस (Water Heron / Bird)',
    trophic: 'TROPHIC LEVEL: T5 (सर्वोच्च जल-उपभोक्ता)',
    diet: 'सर्वोच्च सिकारी (Top Aquatic Predator)',
    energy: 'ठूला माछा खाएर न्यूनतम ऊर्जा प्राप्त गर्छ।',
    role: 'पोखरी र जमिनबीच पोषक तत्व ओसारपसार गर्ने र जल-पारिस्थितिकी सन्तुलित राख्ने।',
    desc: 'यसको विष्ठाले पोखरीमा नाइट्रोजन र फस्फोरस मलको काम गर्छ।'
  }
};

function selectEcosystemTypeC9U6(type) {
  activeC9U6EcoType = type;
  playAudioC9U6('click');
  const btnG = document.getElementById('c9u6-esub-grassland');
  const btnP = document.getElementById('c9u6-esub-pond');
  const btnsG = document.getElementById('c9u6-org-btns-grassland');
  const btnsP = document.getElementById('c9u6-org-btns-pond');
  const lbl = document.getElementById('c9u6-eco-view-label');

  if (type === 'grassland') {
    if (btnG) btnG.className = "px-3.5 py-1.5 rounded-xl bg-emerald-600/30 border border-emerald-500 text-emerald-300 font-bold transition text-xs cursor-pointer";
    if (btnP) btnP.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (btnsG) btnsG.classList.remove('hidden');
    if (btnsP) btnsP.classList.add('hidden');
    if (lbl) lbl.textContent = "GRASSLAND ECOSYSTEM SIMULATION (स्थलीय चउर)";
    selectOrganismC9U6('grass');
  } else {
    if (btnG) btnG.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (btnP) btnP.className = "px-3.5 py-1.5 rounded-xl bg-emerald-600/30 border border-emerald-500 text-emerald-300 font-bold transition text-xs cursor-pointer";
    if (btnsG) btnsG.classList.add('hidden');
    if (btnsP) btnsP.classList.remove('hidden');
    if (lbl) lbl.textContent = "POND ECOSYSTEM SIMULATION (जलीय पोखरी)";
    selectOrganismC9U6('phytoplankton');
  }
}

function selectOrganismC9U6(orgKey) {
  activeC9U6Organism = orgKey;
  playAudioC9U6('click');
  const allOrgs = ['grass', 'grasshopper', 'frog', 'snake', 'eagle', 'phytoplankton', 'zooplankton', 'small_fish', 'big_fish', 'heron'];
  allOrgs.forEach(o => {
    const btn = document.getElementById(`c9u6-obtn-${o}`);
    if (btn) {
      if (o === orgKey) {
        btn.className = "p-3 rounded-2xl border bg-emerald-600/30 border-emerald-500 text-emerald-300 text-left transition cursor-pointer";
      } else {
        btn.className = "p-3 rounded-2xl border bg-slate-950 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer";
      }
    }
  });

  updateOrganismInfoC9U6(orgKey);
  renderEcosystemSVGC9U6(activeC9U6EcoType, orgKey);
}

function updateOrganismInfoC9U6(key) {
  const d = C9U6_ORGANISMS_DATA[key];
  if (!d) return;
  const nameEl = document.getElementById('c9u6-eco-name');
  const trophicEl = document.getElementById('c9u6-eco-trophic');
  const dietEl = document.getElementById('c9u6-eco-diet');
  const energyEl = document.getElementById('c9u6-eco-energy');
  const roleEl = document.getElementById('c9u6-eco-role');
  const descEl = document.getElementById('c9u6-eco-desc');

  if (nameEl) nameEl.textContent = d.name;
  if (trophicEl) trophicEl.textContent = d.trophic;
  if (dietEl) dietEl.textContent = d.diet;
  if (energyEl) energyEl.textContent = d.energy;
  if (roleEl) roleEl.textContent = d.role;
  if (descEl) descEl.textContent = d.desc;
}

function renderEcosystemSVGC9U6(type, activeOrg) {
  const wrap = document.getElementById('c9u6-ecosystem-svg-wrap');
  if (!wrap) return;

  let innerSvg = '';

  if (type === 'grassland') {
    const isGrass = activeOrg === 'grass';
    const isHopper = activeOrg === 'grasshopper';
    const isFrog = activeOrg === 'frog';
    const isSnake = activeOrg === 'snake';
    const isEagle = activeOrg === 'eagle';

    innerSvg = `
      <g>
        <!-- Sky Background -->
        <rect x="0" y="0" width="360" height="230" rx="16" fill="#0c1e33"/>
        
        <!-- Radiant Sun -->
        <circle cx="50" cy="45" r="22" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
        <line x1="50" y1="15" x2="50" y2="8" stroke="#fde047" stroke-width="2.5"/>
        <line x1="50" y1="75" x2="50" y2="82" stroke="#fde047" stroke-width="2.5"/>
        <line x1="20" y1="45" x2="13" y2="45" stroke="#fde047" stroke-width="2.5"/>
        <line x1="80" y1="45" x2="87" y2="45" stroke="#fde047" stroke-width="2.5"/>

        <!-- Rolling Green Grass Hills -->
        <path d="M0,170 Q100,135 220,160 T360,150 L360,230 L0,230 Z" fill="#14532d"/>
        <path d="M0,195 Q140,165 280,185 T360,180 L360,230 L0,230 Z" fill="#166534"/>

        <!-- 1. Grass / Plants (Bottom Center) -->
        <g onclick="selectOrganismC9U6('grass')" class="cursor-pointer">
          <path d="M120,215 L115,165 Q115,145 105,135 Q125,150 125,215 Z" fill="#4ade80" stroke="${isGrass ? '#facc15' : '#22c55e'}" stroke-width="${isGrass ? '2.5' : '1'}"/>
          <path d="M130,215 L135,160 Q145,140 160,130 Q145,150 140,215 Z" fill="#22c55e" stroke="${isGrass ? '#facc15' : '#16a34a'}" stroke-width="${isGrass ? '2.5' : '1'}"/>
          <path d="M125,215 L125,150 Q125,130 120,120 Q130,135 130,215 Z" fill="#86efac" stroke="${isGrass ? '#facc15' : '#4ade80'}" stroke-width="${isGrass ? '2.5' : '1'}"/>
          ${isGrass ? '<circle cx="128" cy="120" r="8" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="128" y="226" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">घाँस (T1)</text>
        </g>

        <!-- 2. Grasshopper (Middle Left) -->
        <g onclick="selectOrganismC9U6('grasshopper')" class="cursor-pointer" transform="translate(60, 140)">
          <!-- Body -->
          <ellipse cx="20" cy="15" rx="14" ry="6" fill="#65a30d" stroke="${isHopper ? '#facc15' : '#4d7c0f'}" stroke-width="${isHopper ? '2.5' : '1.5'}"/>
          <circle cx="32" cy="13" r="5" fill="#84cc16"/>
          <!-- Leg -->
          <polyline points="12,18 6,8 10,24" stroke="#4d7c0f" stroke-width="2" fill="none"/>
          <polyline points="20,18 24,25" stroke="#4d7c0f" stroke-width="1.5" fill="none"/>
          ${isHopper ? '<circle cx="20" cy="15" r="14" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="20" y="34" fill="#bef264" font-size="8" font-weight="bold" text-anchor="middle">फट्याङ्ग्रा (T2)</text>
        </g>

        <!-- 3. Frog (Center Right) -->
        <g onclick="selectOrganismC9U6('frog')" class="cursor-pointer" transform="translate(200, 145)">
          <ellipse cx="20" cy="15" rx="15" ry="10" fill="#059669" stroke="${isFrog ? '#facc15' : '#047857'}" stroke-width="${isFrog ? '2.5' : '1.5'}"/>
          <!-- Eye -->
          <circle cx="27" cy="8" r="4" fill="#34d399"/>
          <circle cx="28" cy="8" r="1.5" fill="#000000"/>
          <!-- Legs -->
          <ellipse cx="9" cy="18" rx="8" ry="4" fill="#047857"/>
          ${isFrog ? '<circle cx="20" cy="15" r="15" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="20" y="34" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">भ्यागुता (T3)</text>
        </g>

        <!-- 4. Snake (Bottom Right) -->
        <g onclick="selectOrganismC9U6('snake')" class="cursor-pointer" transform="translate(275, 165)">
          <path d="M5,25 Q20,5 35,25 T65,25" fill="none" stroke="${isSnake ? '#facc15' : '#d97706'}" stroke-width="${isSnake ? '5' : '3.5'}" stroke-linecap="round"/>
          <circle cx="67" cy="24" r="5" fill="#b45309"/>
          <circle cx="69" cy="23" r="1.5" fill="#fef08a"/>
          ${isSnake ? '<circle cx="35" cy="20" r="15" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="35" y="42" fill="#fcd34d" font-size="8" font-weight="bold" text-anchor="middle">सर्प (T4)</text>
        </g>

        <!-- 5. Eagle / Hawk (Top Center flying) -->
        <g onclick="selectOrganismC9U6('eagle')" class="cursor-pointer" transform="translate(180, 45)">
          <!-- Wings -->
          <path d="M-28,10 Q0,-5 28,10 Q0,2 -28,10 Z" fill="#78350f" stroke="${isEagle ? '#facc15' : '#92400e'}" stroke-width="${isEagle ? '2.5' : '1.5'}"/>
          <circle cx="0" cy="5" r="6" fill="#b45309"/>
          <polygon points="0,9 6,12 0,11" fill="#f59e0b"/>
          ${isEagle ? '<circle cx="0" cy="5" r="18" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="0" y="25" fill="#fed7aa" font-size="8" font-weight="bold" text-anchor="middle">चिल (Apex)</text>
        </g>

        <!-- Decomposers Mushrooms on Left Ground -->
        <g transform="translate(20, 195)">
          <path d="M5,15 Q12,5 20,15 Z" fill="#f43f5e"/>
          <rect x="11" y="15" width="3" height="10" fill="#f1f5f9"/>
          <text x="12" y="32" fill="#fda4af" font-size="7" text-anchor="middle">ढुसी (Decomposer)</text>
        </g>
      </g>
    `;
  } else {
    // Pond Ecosystem
    const isPhyto = activeOrg === 'phytoplankton';
    const isZoo = activeOrg === 'zooplankton';
    const isSmall = activeOrg === 'small_fish';
    const isBig = activeOrg === 'big_fish';
    const isHeron = activeOrg === 'heron';

    innerSvg = `
      <g>
        <!-- Pond Basin & Water Depth -->
        <rect x="0" y="0" width="360" height="60" fill="#0369a1" fill-opacity="0.3"/>
        <rect x="0" y="60" width="360" height="170" rx="16" fill="#075985" fill-opacity="0.6"/>
        
        <!-- Pond Bed (Mud) -->
        <path d="M0,205 Q120,195 240,205 T360,200 L360,230 L0,230 Z" fill="#451a03"/>

        <!-- Water Surface Waves -->
        <path d="M0,60 Q45,55 90,60 T180,60 T270,60 T360,60" fill="none" stroke="#38bdf8" stroke-width="2"/>

        <!-- 1. Phytoplankton / Algae colonies (Floating near surface) -->
        <g onclick="selectOrganismC9U6('phytoplankton')" class="cursor-pointer" transform="translate(40, 85)">
          <circle cx="10" cy="10" r="5" fill="#22c55e" stroke="${isPhyto ? '#facc15' : '#16a34a'}" stroke-width="${isPhyto ? '2' : '1'}"/>
          <circle cx="22" cy="14" r="6" fill="#22c55e" stroke="${isPhyto ? '#facc15' : '#16a34a'}" stroke-width="${isPhyto ? '2' : '1'}"/>
          <circle cx="15" cy="22" r="4.5" fill="#22c55e" stroke="${isPhyto ? '#facc15' : '#16a34a'}" stroke-width="${isPhyto ? '2' : '1'}"/>
          ${isPhyto ? '<circle cx="16" cy="15" r="16" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="16" y="36" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">लेउ (T1)</text>
        </g>

        <!-- 2. Zooplankton (Daphnia / Larva) -->
        <g onclick="selectOrganismC9U6('zooplankton')" class="cursor-pointer" transform="translate(115, 110)">
          <ellipse cx="15" cy="12" rx="9" ry="6" fill="#f472b6" stroke="${isZoo ? '#facc15' : '#db2777'}" stroke-width="${isZoo ? '2' : '1'}"/>
          <line x1="8" y1="10" x2="2" y2="4" stroke="#f472b6" stroke-width="1.5"/>
          <line x1="8" y1="14" x2="2" y2="18" stroke="#f472b6" stroke-width="1.5"/>
          ${isZoo ? '<circle cx="15" cy="12" r="14" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="15" y="28" fill="#fbcfe8" font-size="8" font-weight="bold" text-anchor="middle">जुप्ल्याङ्कटन (T2)</text>
        </g>

        <!-- 3. Small Fish (Middle Depth) -->
        <g onclick="selectOrganismC9U6('small_fish')" class="cursor-pointer" transform="translate(190, 120)">
          <ellipse cx="20" cy="12" rx="14" ry="7" fill="#fb923c" stroke="${isSmall ? '#facc15' : '#ea580c'}" stroke-width="${isSmall ? '2.5' : '1'}"/>
          <polygon points="6,12 0,7 0,17" fill="#f97316"/>
          <circle cx="28" cy="10" r="1.5" fill="#000000"/>
          ${isSmall ? '<circle cx="18" cy="12" r="16" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="18" y="30" fill="#fed7aa" font-size="8" font-weight="bold" text-anchor="middle">साना माछा (T3)</text>
        </g>

        <!-- 4. Large Fish (Deep Bottom) -->
        <g onclick="selectOrganismC9U6('big_fish')" class="cursor-pointer" transform="translate(120, 160)">
          <ellipse cx="35" cy="18" rx="28" ry="14" fill="#0284c7" stroke="${isBig ? '#facc15' : '#0369a1'}" stroke-width="${isBig ? '2.5' : '1.5'}"/>
          <polygon points="10,18 0,8 0,28" fill="#0284c7"/>
          <circle cx="50" cy="14" r="2.5" fill="#f8fafc"/>
          <circle cx="51" cy="14" r="1" fill="#000000"/>
          ${isBig ? '<circle cx="35" cy="18" r="24" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="35" y="42" fill="#bae6fd" font-size="8" font-weight="bold" text-anchor="middle">ठूला माछा (T4)</text>
        </g>

        <!-- 5. Heron / Bird (Pond Bank Top Right) -->
        <g onclick="selectOrganismC9U6('heron')" class="cursor-pointer" transform="translate(290, 20)">
          <!-- Legs standing in shallow water -->
          <line x1="20" y1="50" x2="20" y2="70" stroke="#f59e0b" stroke-width="2"/>
          <line x1="26" y1="50" x2="26" y2="70" stroke="#f59e0b" stroke-width="2"/>
          <!-- Body -->
          <ellipse cx="22" cy="40" rx="14" ry="10" fill="#f8fafc" stroke="${isHeron ? '#facc15' : '#cbd5e1'}" stroke-width="${isHeron ? '2.5' : '1'}"/>
          <!-- Long Neck & Beak -->
          <path d="M28,35 Q35,20 32,10 L45,12 L32,15" fill="#f8fafc" stroke="${isHeron ? '#facc15' : '#cbd5e1'}" stroke-width="1.5"/>
          <polygon points="32,10 48,12 32,14" fill="#f59e0b"/>
          ${isHeron ? '<circle cx="26" cy="35" r="20" fill="none" stroke="#facc15" stroke-width="2" class="animate-ping"/>' : ''}
          <text x="25" y="82" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">बकुल्ला (Apex)</text>
        </g>

        <!-- Water plants / Reeds on Left Bank -->
        <path d="M15,200 L12,140 Q10,110 5,90" fill="none" stroke="#15803d" stroke-width="3"/>
        <path d="M22,200 L25,130 Q28,100 35,80" fill="none" stroke="#16a34a" stroke-width="2.5"/>
      </g>
    `;
  }

  wrap.innerHTML = `
    <svg viewBox="0 0 360 230" class="w-full max-w-[360px] h-auto select-none">
      ${innerSvg}
    </svg>
  `;
}

// =========================================================================
// MODE 2: FOOD WEB & 10% ENERGY PYRAMID
// =========================================================================

function setEnergySubModeC9U6(sub) {
  activeC9U6EnergySub = sub;
  playAudioC9U6('click');
  const btnP = document.getElementById('c9u6-wsub-pyramid');
  const btnC = document.getElementById('c9u6-wsub-cascade');
  const panP = document.getElementById('c9u6-energy-panel-pyramid');
  const panC = document.getElementById('c9u6-energy-panel-cascade');

  if (sub === 'pyramid') {
    if (btnP) btnP.className = "px-3.5 py-1.5 rounded-xl bg-emerald-600/30 border border-emerald-500 text-emerald-300 font-bold transition text-xs cursor-pointer";
    if (btnC) btnC.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (panP) panP.classList.remove('hidden');
    if (panC) panC.classList.add('hidden');
    renderPyramidSVGC9U6();
  } else {
    if (btnP) btnP.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (btnC) btnC.className = "px-3.5 py-1.5 rounded-xl bg-emerald-600/30 border border-emerald-500 text-emerald-300 font-bold transition text-xs cursor-pointer";
    if (panP) panP.classList.add('hidden');
    if (panC) panC.classList.remove('hidden');
    triggerCascadeEventC9U6('rats_killed');
  }
}

function setSolarInputC9U6(joules) {
  c9u6SolarInput = joules;
  playAudioC9U6('energy');
  renderPyramidSVGC9U6();
}

function renderPyramidSVGC9U6() {
  const wrap = document.getElementById('c9u6-pyramid-svg-wrap');
  const sunEl = document.getElementById('c9u6-en-sun');
  const t1El = document.getElementById('c9u6-en-t1');
  const t2El = document.getElementById('c9u6-en-t2');
  const t3El = document.getElementById('c9u6-en-t3');
  const t4El = document.getElementById('c9u6-en-t4');

  const sun = c9u6SolarInput;
  const t1 = sun * 0.01; // 1%
  const t2 = t1 * 0.10;  // 10%
  const t3 = t2 * 0.10;  // 10%
  const t4 = t3 * 0.10;  // 10%

  const fmt = (n) => n.toLocaleString('ne-NP') + ' J';

  if (sunEl) sunEl.textContent = fmt(sun);
  if (t1El) t1El.textContent = fmt(t1);
  if (t2El) t2El.textContent = fmt(t2);
  if (t3El) t3El.textContent = fmt(t3);
  if (t4El) t4El.textContent = fmt(t4);

  if (!wrap) return;

  wrap.innerHTML = `
    <svg viewBox="0 0 380 250" class="w-full max-w-[380px] h-auto select-none">
      <!-- Sun at Top Right -->
      <g transform="translate(320, 35)">
        <circle cx="0" cy="0" r="18" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
        <text x="0" y="4" fill="#78350f" font-size="7" font-weight="black" text-anchor="middle">सौर्य किरण</text>
        <text x="0" y="28" fill="#fde047" font-size="8" font-family="monospace" text-anchor="middle">${fmt(sun)}</text>
      </g>

      <!-- Stepped Pyramid Bars -->
      <!-- T1 Producers (Base) -->
      <g transform="translate(30, 185)">
        <rect x="0" y="0" width="300" height="35" rx="6" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
        <text x="150" y="16" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">T1: उत्पादक (घाँस / वनस्पति)</text>
        <text x="150" y="28" fill="#bbf7d0" font-size="9" font-family="monospace" font-weight="black" text-anchor="middle">${fmt(t1)} (१% संचित)</text>
      </g>

      <!-- Heat Loss 1 Right -->
      <path d="M335,195 Q355,190 350,180" fill="none" stroke="#f87171" stroke-width="1.8" stroke-dasharray="3,2"/>
      <text x="355" y="178" fill="#f87171" font-size="7">९०% ताप क्षय</text>

      <!-- T2 Herbivores (2nd Step) -->
      <g transform="translate(65, 140)">
        <rect x="0" y="0" width="230" height="35" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
        <text x="115" y="16" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">T2: प्राथमिक उपभोक्ता (शाकाहारी फट्याङ्ग्रा)</text>
        <text x="115" y="28" fill="#bae6fd" font-size="9" font-family="monospace" font-weight="black" text-anchor="middle">${fmt(t2)} (१०%)</text>
      </g>

      <!-- Heat Loss 2 -->
      <path d="M300,150 Q320,145 315,135" fill="none" stroke="#f87171" stroke-width="1.8" stroke-dasharray="3,2"/>

      <!-- T3 Carnivores (3rd Step) -->
      <g transform="translate(105, 95)">
        <rect x="0" y="0" width="150" height="35" rx="6" fill="#7c3aed" stroke="#c084fc" stroke-width="2"/>
        <text x="75" y="15" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">T3: द्वितीयक (भ्यागुता)</text>
        <text x="75" y="27" fill="#f3e8ff" font-size="8" font-family="monospace" font-weight="black" text-anchor="middle">${fmt(t3)} (१०%)</text>
      </g>

      <!-- T4 Apex Predator (Top Step) -->
      <g transform="translate(140, 50)">
        <rect x="0" y="0" width="80" height="35" rx="6" fill="#e11d48" stroke="#fb7185" stroke-width="2"/>
        <text x="40" y="14" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">T4: चिल (Apex)</text>
        <text x="40" y="26" fill="#ffe4e6" font-size="8" font-family="monospace" font-weight="black" text-anchor="middle">${fmt(t4)} (१०%)</text>
      </g>

      <text x="180" y="240" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">ऊर्जाको पिरामिड सधैँ ठाडो (Always Upright) हुन्छ</text>
    </svg>
  `;
}

// -------------------------------------------------------------------------
// Trophic Cascade Simulator
// -------------------------------------------------------------------------
function triggerCascadeEventC9U6(scenario) {
  c9u6CascadeScenario = scenario;
  if (scenario === 'normal') playAudioC9U6('click');
  else playAudioC9U6('alert');

  const btns = ['rats', 'frogs', 'locust', 'normal'];
  btns.forEach(b => {
    const btn = document.getElementById(`c9u6-cbtn-${b}`);
    if (btn) {
      if (b === scenario.replace('_killed', '').replace('_extinct', '').replace('_swarm', '')) {
        btn.className = "px-3 py-1.5 rounded-xl bg-rose-600/30 border border-rose-500 text-rose-300 font-bold transition text-xs cursor-pointer";
      } else {
        btn.className = "px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
      }
    }
  });

  const badge = document.getElementById('c9u6-cascade-badge');
  const title = document.getElementById('c9u6-cascade-title');
  const desc = document.getElementById('c9u6-cascade-desc');
  const lesson = document.getElementById('c9u6-cascade-lesson');

  if (scenario === 'rats_killed') {
    if (badge) {
      badge.textContent = "चेतावनी: मुसा सखाप ➔ किराको विस्फोट!";
      badge.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/40 animate-pulse";
    }
    if (title) title.textContent = "किसानले मुसा मार्दा धान उत्पादनमा आएको संकट";
    if (desc) desc.textContent = "मुसाले धान मात्र खाँदैनथ्यो, धानबाली नष्ट गर्ने हजारौँ हानिकारक फट्याङ्ग्रा, लार्भा र किरा पनि खाएर नियन्त्रण गर्थ्यो। सबै मुसा मारिएपछि बाली खाने किराहरू अनियन्त्रित रूपमा बढेर धानको बोट र बाला सखाप पारे! साथै मुसा खाने सर्प र उल्लुहरू आहारा नपाएर भागे।";
    if (lesson) lesson.textContent = "प्राकृतिक खाद्यजालमा कुनै पनि जीवलाई अनावश्यक ठानेर सखाप पार्दा अप्रत्याशित संकट निम्तिन्छ।";
  } else if (scenario === 'frogs_extinct') {
    if (badge) {
      badge.textContent = "चेतावनी: भ्यागुता लोप ➔ लामखुट्टे तथा लेउ सङ्कट";
      badge.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40 animate-pulse";
    }
    if (title) title.textContent = "पोखरीबाट भ्यागुता लोप हुँदाको दुष्परिणाम";
    if (desc) desc.textContent = "भ्यागुता लोप भएपछि पोखरीमा किरा र लामखुट्टेका लार्भा अत्यधिक बढे। किराहरूले जलवनस्पति खाएर पानीमा लेउको अत्यधिक वृद्धि (Algal bloom) गराए र घाम छेकिएर अक्सिजन अभावमा माछाहरू सामूहिक रूपमा मर्न थाले।";
    if (lesson) lesson.textContent = "द्वितीयक उपभोक्ताले प्राथमिक किराहरूको जनसंख्या नियन्त्रण गरी इकोसिस्टमलाई बचाउँछ।";
  } else if (scenario === 'locust_swarm') {
    if (badge) {
      badge.textContent = "विपद्: सलह / किराको अनियन्त्रित आक्रमण!";
      badge.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-red-600/30 text-red-300 border border-red-500 animate-pulse";
    }
    if (title) title.textContent = "प्राथमिक उपभोक्ताको विस्फोट र वनस्पतिको संहार";
    if (desc) desc.textContent = "प्राकृतिक सिकारीहरूको कमीले गर्दा फट्याङ्ग्रा/सलहको संख्या करोडौँमा पुग्यो। यिनीहरूले चउर र खेतको सम्पूर्ण हरियो घाँस र बाली घण्टाभरमै खाएर नाङ्गो पारे। उत्पादक नै समाप्त भएपछि माटोको भू-क्षय भयो र पछि किराहरू आफैँ भोकले मरे।";
    if (lesson) lesson.textContent = "उत्पादक र उपभोक्ताबीचको सन्तुलन नै सम्पूर्ण इकोसिस्टमको आयु हो।";
  } else {
    if (badge) {
      badge.textContent = "अवस्था: प्राकृतिक सन्तुलित खाद्य जाल";
      badge.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40";
    }
    if (title) title.textContent = "स्वस्थ तथा सन्तुलित पारिस्थिक चक्र";
    if (desc) desc.textContent = "उत्पादक, शाकाहारी, मांसाहारी र विच्छेदकहरू आपसी सन्तुलनमा छन्। प्रत्येक जीवको संख्या प्राकृतिक सिकार र खाद्य उपलब्धताले नियन्त्रित छ। कसैको पनि अत्यधिक वृद्धि वा विनाश भएको छैन।";
    if (lesson) lesson.textContent = "विविधतापूर्ण खाद्यजालले प्रकृतिको स्व-नियमन (Homeostasis) लाई सबल बनाउँछ।";
  }

  renderCascadeSVGC9U6(scenario);
}

function renderCascadeSVGC9U6(scenario) {
  const wrap = document.getElementById('c9u6-cascade-svg-wrap');
  if (!wrap) return;

  const isRatsKilled = scenario === 'rats_killed';
  const isFrogsExtinct = scenario === 'frogs_extinct';
  const isLocust = scenario === 'locust_swarm';

  wrap.innerHTML = `
    <svg viewBox="0 0 380 250" class="w-full max-w-[380px] h-auto select-none">
      <!-- Sun -->
      <g transform="translate(40, 40)">
        <circle cx="0" cy="0" r="16" fill="#fbbf24"/>
        <text x="0" y="3" fill="#78350f" font-size="7" font-weight="black" text-anchor="middle">सूर्य</text>
      </g>

      <!-- Node 1: Crops / Grass (Producer) -->
      <g transform="translate(60, 160)">
        <rect x="-35" y="-18" width="70" height="36" rx="8" fill="${isLocust ? '#7f1d1d' : '#14532d'}" stroke="${isLocust ? '#ef4444' : '#22c55e'}" stroke-width="2"/>
        <text x="0" y="-2" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">धान / घाँस</text>
        <text x="0" y="10" fill="${isLocust ? '#fca5a5' : '#86efac'}" font-size="7" text-anchor="middle">${isLocust ? 'सखाप!' : 'उत्पादक'}</text>
      </g>

      <!-- Node 2: Insects / Locusts -->
      <g transform="translate(180, 80)">
        <rect x="-35" y="-18" width="70" height="36" rx="8" fill="${isLocust || isRatsKilled ? '#854d0e' : '#1e293b'}" stroke="${isLocust || isRatsKilled ? '#facc15' : '#64748b'}" stroke-width="${isLocust || isRatsKilled ? '3' : '1.5'}"/>
        <text x="0" y="-2" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">किरा / सलह</text>
        <text x="0" y="10" fill="${isLocust || isRatsKilled ? '#fde047' : '#94a3b8'}" font-size="7" font-weight="bold" text-anchor="middle">${isLocust || isRatsKilled ? 'अनियन्त्रित विस्फोट!' : 'प्राथमिक'}</text>
      </g>

      <!-- Node 3: Rats (Mouse) -->
      <g transform="translate(180, 190)">
        <rect x="-35" y="-18" width="70" height="36" rx="8" fill="${isRatsKilled ? '#450a0a' : '#1e293b'}" stroke="${isRatsKilled ? '#f43f5e' : '#64748b'}" stroke-width="2"/>
        <text x="0" y="-2" fill="${isRatsKilled ? '#f87171' : '#ffffff'}" font-size="8" font-weight="bold" text-anchor="middle">${isRatsKilled ? '☠️ मुसा' : 'मुसा (Rat)'}</text>
        <text x="0" y="10" fill="${isRatsKilled ? '#fca5a5' : '#cbd5e1'}" font-size="7" text-anchor="middle">${isRatsKilled ? 'सखाप (Dead)' : 'किरा+धान खाने'}</text>
      </g>

      <!-- Node 4: Frogs -->
      <g transform="translate(280, 80)">
        <rect x="-30" y="-18" width="60" height="36" rx="8" fill="${isFrogsExtinct ? '#450a0a' : '#065f46'}" stroke="${isFrogsExtinct ? '#f43f5e' : '#10b981'}" stroke-width="2"/>
        <text x="0" y="-2" fill="${isFrogsExtinct ? '#f87171' : '#ffffff'}" font-size="8" font-weight="bold" text-anchor="middle">${isFrogsExtinct ? '☠️ भ्यागुता' : 'भ्यागुता'}</text>
        <text x="0" y="10" fill="${isFrogsExtinct ? '#fca5a5' : '#a7f3d0'}" font-size="7" text-anchor="middle">${isFrogsExtinct ? 'लोप' : 'द्वितीयक'}</text>
      </g>

      <!-- Node 5: Snakes / Owls (Top Predator) -->
      <g transform="translate(300, 180)">
        <rect x="-35" y="-18" width="70" height="36" rx="8" fill="${isRatsKilled ? '#7f1d1d' : '#831843'}" stroke="${isRatsKilled ? '#ef4444' : '#fb7185'}" stroke-width="2"/>
        <text x="0" y="-2" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">सर्प / उल्लु</text>
        <text x="0" y="10" fill="${isRatsKilled ? '#fca5a5' : '#fbcfe8'}" font-size="7" text-anchor="middle">${isRatsKilled ? 'भोकमरी / पलायन' : 'तृतीयक उपभोक्ता'}</text>
      </g>

      <!-- Connecting Arrows -->
      <path d="M50,56 L60,140" stroke="#facc15" stroke-width="1.8" stroke-dasharray="3,2"/>
      <path d="M95,160 Q130,130 145,95" stroke="#22c55e" stroke-width="2"/>
      <path d="M95,170 L145,185" stroke="#22c55e" stroke-width="2"/>
      
      <!-- Rat Eating Insect Arrow -->
      <path d="M180,100 L180,170" stroke="${isRatsKilled ? '#ef4444' : '#38bdf8'}" stroke-width="${isRatsKilled ? '1' : '2'}" stroke-dasharray="${isRatsKilled ? '4,4' : 'none'}"/>
      
      <!-- Insect to Frog -->
      <path d="M215,80 L250,80" stroke="${isFrogsExtinct ? '#ef4444' : '#38bdf8'}" stroke-width="2"/>
      
      <!-- Rat to Snake -->
      <path d="M215,190 L265,185" stroke="${isRatsKilled ? '#ef4444' : '#a855f7'}" stroke-width="2" stroke-dasharray="${isRatsKilled ? '3,3' : 'none'}"/>

      ${isRatsKilled ? `
        <text x="190" y="240" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">मुसा मारिँदा किरा नियन्त्रण टुट्यो र धानबाली नष्ट भयो!</text>
      ` : ''}
    </svg>
  `;
}

// =========================================================================
// MODE 3: BIOTIC INTERACTIONS EXPLORER
// =========================================================================

const C9U6_INTERACTIONS_DATA = {
  mutualism: {
    eng: 'MUTUALISM (+, +)',
    nep: 'पारस्परिकता (आपसी सहजीविता)',
    symbol: 'दुवै लाभान्वित (+, +)',
    desc: 'दुई फरक प्रजातिका जीवहरू मिलेर बस्दा दुवैलाई प्रत्यक्ष र अनिवार्य फाइदा हुन्छ। एकको अनुपस्थितिमा अर्को बाँच्न कठिन वा असम्भव हुन्छ।',
    example: '१. लाइकेन (Lichen): लेउले प्रकाश संश्लेषण गरी खाना दिन्छ; ढुसीले पानी, खनिज र सुरक्षा दिन्छ। २. फूल र मौरी: मौरीले मकरन्द पाउँछ, फूलको परागसेचन हुन्छ। ३. कोसेबालीको जरामा राइजोबियम ब्याक्टेरिया।',
    significance: 'नाङ्गा चट्टानलाई क्षयीकरण गरी पहिलो पटक मलिलो माटो बनाउने (Pedogenesis) र नाइट्रोजन चक्र चलाउने आधारशिला।',
    tip: 'परीक्षामा लाइकेन र राइजोबियमको उदाहरण सबैभन्दा धेरै सोधिने पारस्परिकताका उदाहरण हुन्।'
  },
  commensalism: {
    eng: 'COMMENSALISM (+, 0)',
    nep: 'सहभोजिता (एकतर्फी लाभ)',
    symbol: 'एउटा लाभान्वित, अर्को तटस्थ (+, ०)',
    desc: 'यसमा एउटा जीवले आश्रय, चाल वा सुरक्षाको फाइदा पाउँछ तर आश्रय दिने जीव (Host) लाई कुनै प्रत्यक्ष फाइदा वा हानि केही पनि हुँदैन।',
    example: '१. रुखको हाँगामा उम्रने सुनाखरी (Orchid/Epiphyte): रुखबाट केवल घाम र उचाइ पाउँछ, रुखको खाना वा पानी चोर्दैन। २. सार्क र रेमोरा माछा: रेमोरा सार्कको जिउमा टाँसिएर सित्तैमा यात्रा र जुठो खाना पाउँछ। ३. गौँथलीले घरमा गुँड बनाउनु।',
    significance: 'कमजोर र साना जीवहरूलाई शक्तिशाली जीवको आडमा सुरक्षित आश्रय र अस्तित्व रक्षा गर्न मद्दत गर्छ।',
    tip: 'सुनाखरी परजीवी होइन, यो केवल घाम पाउन रुखमा बस्ने सहभोजी (Epiphyte) मात्र हो।'
  },
  parasitism: {
    eng: 'PARASITISM (+, -)',
    nep: 'परजीविता (शोषक सम्बन्ध)',
    symbol: 'परजीवी लाभान्वित, पोषक पीडित (+, -)',
    desc: 'परजीवी (Parasite) ले पोषक (Host) को शरीरबाट पोषण र रगत खोसी प्रत्यक्ष फाइदा लिन्छ भने पोषक जीव बिरामी, कमजोर र अन्ततः मर्न पनि सक्छ।',
    example: '१. बाह्य परजीवी (Ectoparasite): जुम्रा, किर्ना, उडुस, लामखुट्टे (जनावरको रगत चुस्ने)। २. आन्तरिक परजीवी (Endoparasite): आन्द्रामा बस्ने जुका (Roundworm), फित्तेजुका (Tapeworm)। ३. वनस्पति परजीवी: आकाशबेली (Cuscuta)।',
    significance: 'प्रकृतिमा अत्यधिक जनसंख्या भएका प्रजातिलाई रोगव्याधीमार्फत नियन्त्रण गर्ने जैविक नियमन।',
    tip: 'परजीवीले आफ्नो पोषकलाई तुरुन्तै मार्दैन, किनकि पोषक मरेमा परजीवीको आहारा र बासस्थान पनि समाप्त हुन्छ।'
  },
  predation: {
    eng: 'PREDATION (+, -)',
    nep: 'सिकारिता (सिकारी र सिकार)',
    symbol: 'सिकारी लाभान्वित, सिकार मृत (+, -)',
    desc: 'शक्तिशाली जीव (Predator) ले कमजोर जीव (Prey) लाई मारेर आफ्नो खाना बनाउँछ। यसमा सिकारीले फाइदा पाउँछ र सिकारको ज्यान जान्छ।',
    example: '१. बाघले हरिण मार्नु। २. चिलले सर्प समात्नु। ३. भ्यागुताले फट्याङ्ग्रा निल्नु। ४. बिरालोले मुसा समात्नु।',
    significance: 'शाकाहारीहरूको संख्यालाई सीमाभित्र राख्ने, अत्यधिक चरिचरन रोक्ने, र कमजोर/रोगी जीवहरू हटाएर स्वस्थ वंशाणु मात्र बाँच्न दिने।',
    tip: 'सिकारी लोप हुँदा ट्रॉफिक क्यास्केड भई सम्पूर्ण वनस्पति र वातावरण ध्वस्त हुन्छ।'
  },
  competition: {
    eng: 'COMPETITION (-, -)',
    nep: 'प्रतिस्पर्धा (अस्तित्वको संघर्ष)',
    symbol: 'दुवैको शक्ति क्षय (-, -)',
    desc: 'सीमित प्राकृतिक स्रोतहरू (खाना, पानी, घाम, बासस्थान, जोडी) का लागि दुई वा बढी जीवहरूबीच हुने होडबाजी। यसमा दुवै जीवले तनाव र ऊर्जाको क्षति व्यहोर्छन्।',
    example: '१. एउटै चउरमा घाँसका लागि गाई र बाख्राबीचको प्रतिस्पर्धा (Interspecific)। २. एउटै प्रजातिका दुई भाले बाघबीच क्षेत्र ओगट्ने लडाइँ (Intraspecific)। ३. घना जंगलमा रूखहरूबीच सूर्यको प्रकाश पाउने ठाडो प्रतिस्पर्धा।',
    significance: 'डार्बिनको "बाँच्नका लागि संघर्ष" र प्राकृतिक छनोटको आधार; यसले सक्षम जीवलाई मात्र बाँच्न र नयाँ अनुकूलन विकास गर्न प्रेरित गर्छ।',
    tip: 'गौसको प्रतिस्पर्धी बहिष्कार सिद्धान्त (Gause’s Competitive Exclusion Principle) अनुसार एउटै स्रोतमा दुई समान प्रतिस्पर्धी सधैँ सँगै बाँच्न सक्दैनन्।'
  }
};

function selectInteractionC9U6(key) {
  activeC9U6Interaction = key;
  playAudioC9U6('click');
  const allKeys = ['mutualism', 'commensalism', 'parasitism', 'predation', 'competition'];
  allKeys.forEach(k => {
    const btn = document.getElementById(`c9u6-ibtn-${k}`);
    if (btn) {
      if (k === key) {
        btn.className = "p-3 rounded-2xl border bg-emerald-600/30 border-emerald-500 text-emerald-300 text-left transition cursor-pointer";
      } else {
        btn.className = "p-3 rounded-2xl border bg-slate-950 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer";
      }
    }
  });

  updateInteractionInfoC9U6(key);
  renderInteractionSVGC9U6(key);
}

function updateInteractionInfoC9U6(key) {
  const d = C9U6_INTERACTIONS_DATA[key];
  if (!d) return;

  const eng = document.getElementById('c9u6-i-engname');
  const nep = document.getElementById('c9u6-i-nepname');
  const sym = document.getElementById('c9u6-i-symbol');
  const desc = document.getElementById('c9u6-i-desc');
  const ex = document.getElementById('c9u6-i-example');
  const sig = document.getElementById('c9u6-i-significance');
  const tip = document.getElementById('c9u6-i-tip');

  if (eng) eng.textContent = d.eng;
  if (nep) nep.textContent = d.nep;
  if (sym) sym.textContent = d.symbol;
  if (desc) desc.textContent = d.desc;
  if (ex) ex.textContent = d.example;
  if (sig) sig.textContent = d.significance;
  if (tip) tip.textContent = d.tip;
}

function renderInteractionSVGC9U6(key) {
  const wrap = document.getElementById('c9u6-interaction-svg-wrap');
  if (!wrap) return;

  let innerSvg = '';

  if (key === 'mutualism') {
    // Lichen: Algae + Fungi on rock OR Bee and Flower
    innerSvg = `
      <g>
        <circle cx="160" cy="130" r="100" fill="#064e3b" fill-opacity="0.2" stroke="#10b981" stroke-width="2"/>
        
        <!-- Big Sunflower in Center -->
        <circle cx="160" cy="130" r="28" fill="#78350f" stroke="#eab308" stroke-width="3"/>
        <!-- Yellow Petals -->
        <ellipse cx="160" cy="90" rx="10" ry="20" fill="#facc15"/>
        <ellipse cx="160" cy="170" rx="10" ry="20" fill="#facc15"/>
        <ellipse cx="120" cy="130" rx="20" ry="10" fill="#facc15"/>
        <ellipse cx="200" cy="130" rx="20" ry="10" fill="#facc15"/>
        <ellipse cx="132" cy="102" rx="16" ry="12" fill="#facc15" transform="rotate(-45 132 102)"/>
        <ellipse cx="188" cy="102" rx="16" ry="12" fill="#facc15" transform="rotate(45 188 102)"/>
        <ellipse cx="132" cy="158" rx="16" ry="12" fill="#facc15" transform="rotate(45 132 158)"/>
        <ellipse cx="188" cy="158" rx="16" ry="12" fill="#facc15" transform="rotate(-45 188 158)"/>

        <!-- Bee landing on Flower -->
        <g transform="translate(195, 80)">
          <!-- Bee Body with stripes -->
          <ellipse cx="15" cy="15" rx="14" ry="9" fill="#f59e0b"/>
          <line x1="12" y1="6" x2="12" y2="24" stroke="#000000" stroke-width="2.5"/>
          <line x1="18" y1="6" x2="18" y2="24" stroke="#000000" stroke-width="2.5"/>
          <!-- Bee Wings -->
          <ellipse cx="15" cy="5" rx="9" ry="5" fill="#bae6fd" opacity="0.8"/>
          <!-- Pollen grains stuck on bee legs -->
          <circle cx="8" cy="22" r="2.5" fill="#facc15"/>
          <circle cx="22" cy="22" r="2.5" fill="#facc15"/>
        </g>

        <!-- Mutual benefit labels -->
        <text x="75" y="60" fill="#fde047" font-size="9" font-weight="bold">१. मौरी ➔ मकरन्द (+)</text>
        <text x="245" y="195" fill="#34d399" font-size="9" font-weight="bold">२. फूल ➔ परागसेचन (+)</text>
        <text x="160" y="240" fill="#10b981" font-size="10" font-weight="black" text-anchor="middle">पारस्परिकता: दुवै लाभान्वित (+, +)</text>
      </g>
    `;
  } else if (key === 'commensalism') {
    // Tree trunk with Epiphytic Orchid
    innerSvg = `
      <g>
        <circle cx="160" cy="130" r="100" fill="#0c4a6e" fill-opacity="0.2" stroke="#0284c7" stroke-width="2"/>
        
        <!-- Big Oak Tree Trunk on Left -->
        <path d="M50,20 L130,20 L130,240 L50,240 Z" fill="#451a03" stroke="#78350f" stroke-width="3"/>
        <line x1="80" y1="30" x2="80" y2="230" stroke="#78350f" stroke-width="2" stroke-dasharray="8,6"/>
        <line x1="105" y1="50" x2="105" y2="210" stroke="#78350f" stroke-width="2" stroke-dasharray="10,8"/>

        <!-- Horizontal Branch -->
        <path d="M130,110 Q190,105 260,95 L260,125 Q190,135 130,140 Z" fill="#451a03" stroke="#78350f" stroke-width="2.5"/>

        <!-- Epiphytic Orchid Clinging to Branch (Velamen roots) -->
        <g transform="translate(180, 75)">
          <!-- Hanging aerial roots (Velamen) -->
          <path d="M15,35 Q10,55 5,75" stroke="#cbd5e1" stroke-width="2" fill="none"/>
          <path d="M25,35 Q30,55 35,70" stroke="#cbd5e1" stroke-width="2" fill="none"/>
          <!-- Green Orchid Leaves -->
          <ellipse cx="10" cy="20" rx="14" ry="6" fill="#16a34a" transform="rotate(-30 10 20)"/>
          <ellipse cx="30" cy="20" rx="14" ry="6" fill="#16a34a" transform="rotate(30 30 20)"/>
          <!-- Purple Orchid Flower -->
          <circle cx="20" cy="5" r="7" fill="#c084fc"/>
          <circle cx="20" cy="5" r="3" fill="#facc15"/>
        </g>

        <!-- Labels -->
        <text x="90" y="80" fill="#fed7aa" font-size="9" font-weight="bold" text-anchor="middle">रुख (०)</text>
        <text x="90" y="95" fill="#cbd5e1" font-size="7" text-anchor="middle">कुनै असर छैन</text>
        <text x="240" y="60" fill="#c084fc" font-size="9" font-weight="bold">सुनाखरी (+)</text>
        <text x="240" y="75" fill="#a7f3d0" font-size="7">घाम र आश्रय पायो</text>
        <text x="160" y="240" fill="#38bdf8" font-size="10" font-weight="black" text-anchor="middle">सहभोजिता: एउटालाई फाइदा, अर्को तटस्थ (+, ०)</text>
      </g>
    `;
  } else if (key === 'parasitism') {
    // Tapeworm / Leech feeding on host
    innerSvg = `
      <g>
        <circle cx="160" cy="130" r="100" fill="#881337" fill-opacity="0.2" stroke="#e11d48" stroke-width="2"/>
        
        <!-- Host Skin / Intestinal Wall Layer -->
        <rect x="50" y="160" width="220" height="40" rx="8" fill="#991b1b" stroke="#f43f5e" stroke-width="2"/>
        <text x="160" y="185" fill="#fecdd3" font-size="9" font-weight="bold" text-anchor="middle">पोषक जीव (Host) को रक्तनली / आन्द्रा (-)</text>

        <!-- Parasite: Leech / Hookworm penetrating host -->
        <g transform="translate(130, 70)">
          <!-- Segmented Body -->
          <path d="M30,10 Q20,30 30,50 T30,90" fill="none" stroke="#78350f" stroke-width="12" stroke-linecap="round"/>
          <path d="M30,10 Q20,30 30,50 T30,90" fill="none" stroke="#a16207" stroke-width="8" stroke-linecap="round"/>
          <!-- Sucker Hooks clinging into tissue -->
          <circle cx="30" cy="90" r="7" fill="#450a0a" stroke="#dc2626" stroke-width="2"/>
          <line x1="26" y1="92" x2="23" y2="97" stroke="#dc2626" stroke-width="2"/>
          <line x1="34" y1="92" x2="37" y2="97" stroke="#dc2626" stroke-width="2"/>
        </g>

        <!-- Blood flow being stolen -->
        <circle cx="160" cy="148" r="3.5" fill="#ef4444" class="animate-ping"/>

        <text x="215" y="85" fill="#facc15" font-size="9" font-weight="bold">परजीवी (+)</text>
        <text x="215" y="98" fill="#cbd5e1" font-size="7">रगत/पोषण लुट्छ</text>
        <text x="160" y="240" fill="#f43f5e" font-size="10" font-weight="black" text-anchor="middle">परजीविता: परजीवीलाई फाइदा, पोषकलाई हानि (+, -)</text>
      </g>
    `;
  } else if (key === 'predation') {
    // Eagle catching snake OR Tiger hunting
    innerSvg = `
      <g>
        <circle cx="160" cy="130" r="100" fill="#713f12" fill-opacity="0.2" stroke="#ea580c" stroke-width="2"/>
        
        <!-- Eagle Diving with Open Talons -->
        <g transform="translate(130, 60)">
          <path d="M-35,15 Q0,-10 35,15 Q0,5 -35,15 Z" fill="#9a3412" stroke="#ea580c" stroke-width="2"/>
          <circle cx="0" cy="10" r="10" fill="#7c2d12"/>
          <!-- Sharp Beak -->
          <polygon points="0,18 7,24 0,22" fill="#facc15"/>
          <!-- Sharp Talons -->
          <line x1="-8" y1="26" x2="-12" y2="38" stroke="#facc15" stroke-width="2.5"/>
          <line x1="8" y1="26" x2="12" y2="38" stroke="#facc15" stroke-width="2.5"/>
        </g>

        <!-- Prey: Snake trapped in talons -->
        <g transform="translate(115, 120)">
          <path d="M10,20 Q40,0 60,35 T90,20" fill="none" stroke="#22c55e" stroke-width="5" stroke-linecap="round"/>
          <circle cx="92" cy="18" r="4" fill="#15803d"/>
        </g>

        <text x="220" y="55" fill="#fdba74" font-size="9" font-weight="bold">सिकारी (Predator: +)</text>
        <text x="220" y="145" fill="#f87171" font-size="9" font-weight="bold">सिकार (Prey: -)</text>
        <text x="160" y="240" fill="#ea580c" font-size="10" font-weight="black" text-anchor="middle">सिकारिता: सिकारी लाभान्वित, सिकार मृत (+, -)</text>
      </g>
    `;
  } else if (key === 'competition') {
    // Two trees competing for light and roots competing for water
    innerSvg = `
      <g>
        <circle cx="160" cy="130" r="100" fill="#3f3f46" fill-opacity="0.2" stroke="#a1a1aa" stroke-width="2"/>
        
        <!-- Ground Line -->
        <line x1="70" y1="160" x2="250" y2="160" stroke="#71717a" stroke-width="2.5"/>

        <!-- Tree A on Left -->
        <rect x="110" y="80" width="14" height="80" fill="#78350f"/>
        <circle cx="117" cy="70" r="26" fill="#166534" stroke="#22c55e" stroke-width="1.5"/>

        <!-- Tree B on Right (Very close) -->
        <rect x="155" y="80" width="14" height="80" fill="#78350f"/>
        <circle cx="162" cy="70" r="26" fill="#15803d" stroke="#22c55e" stroke-width="1.5"/>

        <!-- Crown branches clashing for light -->
        <path d="M135,50 L145,50" stroke="#facc15" stroke-width="3" stroke-dasharray="2,2"/>
        <text x="140" y="38" fill="#fde047" font-size="7" font-weight="bold" text-anchor="middle">घामको होड</text>

        <!-- Intertwined Roots competing for water -->
        <g stroke="#a16207" stroke-width="2" fill="none">
          <path d="M117,160 Q130,185 140,205"/>
          <path d="M162,160 Q145,185 135,205"/>
        </g>
        <text x="140" y="215" fill="#fdba74" font-size="7" font-weight="bold" text-anchor="middle">पानी/खनिजको होड</text>

        <text x="160" y="240" fill="#e4e4e7" font-size="10" font-weight="black" text-anchor="middle">प्रतिस्पर्धा: दुवैको शक्ति क्षय (-, -)</text>
      </g>
    `;
  }

  wrap.innerHTML = `
    <svg viewBox="0 0 320 250" class="w-full max-w-[320px] h-auto select-none">
      ${innerSvg}
    </svg>
  `;
}

// =========================================================================
// TAB 2: EXERCISES FILTERING
// =========================================================================
function filterC9U6Exercises(filter) {
  playAudioC9U6('click');
  const cards = document.querySelectorAll('.c9u6-ex-card');
  cards.forEach(card => {
    const cats = (card.getAttribute('data-cat') || '').split(' ');
    if (filter === 'all' || cats.includes(filter)) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  const filterBtns = ['all', 'mcq', 'reason', 'diff', 'qa', 'project'];
  filterBtns.forEach(f => {
    const btn = document.getElementById(`c9u6-exbtn-${f}`);
    if (btn) {
      if (f === filter) {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-black transition bg-emerald-600 text-white shadow-sm cursor-pointer whitespace-nowrap";
      } else {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap";
      }
    }
  });
}

// =========================================================================
// TAB 3: TIERS FILTERING
// =========================================================================
function filterC9U6Tiers(tier) {
  playAudioC9U6('click');
  const cards = document.querySelectorAll('.c9u6-tier-card');
  cards.forEach(card => {
    const t = card.getAttribute('data-tier');
    if (tier === 'all' || t === tier) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  const tierBtns = ['all', 'k', 'u', 'ha'];
  tierBtns.forEach(t => {
    const btn = document.getElementById(`c9u6-tierbtn-${t}`);
    if (btn) {
      if (t === tier) {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-black transition bg-emerald-600 text-white shadow-sm cursor-pointer whitespace-nowrap";
      } else {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap";
      }
    }
  });
}

// =========================================================================
// TAB 4: QUIZ ENGINE (10 Comprehensive Questions)
// =========================================================================
const C9U6_QUIZ_DATA = [
  {
    q: "१. मृत जीव तथा कुहिएका जैविक फोहोरलाई सडाएर खनिज तत्व पुनः माटोमा फर्काउने विच्छेदक कुन हो ?",
    opts: [
      "हरियो लेउ (Spirogyra)",
      "किरा फट्याङ्ग्रा",
      "च्याउ तथा ब्याक्टेरिया (Mushroom & Bacteria)",
      "भ्यागुता"
    ],
    ans: 2,
    exp: "च्याउ तथा ब्याक्टेरिया मृतजीवी सूक्ष्मजीव (विच्छेदक) हुन्, जसले जटिल जैविक पदार्थलाई सरल खनिज तत्वमा विच्छेदन गर्छन्।"
  },
  {
    q: "२. लिन्डम्यानको ऊर्जा स्थानान्तरण नियमअनुसार एउटा पोषण तहबाट अर्को माथिल्लो तहमा कति प्रतिशत ऊर्जा मात्र सर्दछ ?",
    opts: [
      "१ प्रतिशत",
      "१० प्रतिशत",
      "५० प्रतिशत",
      "९० प्रतिशत"
    ],
    ans: 1,
    exp: "लिन्डम्यानको १०% नियमअनुसार केवल १०% ऊर्जा मात्र नयाँ बायोमासमा सञ्चित हुन्छ र बाँकी ९०% ऊर्जा श्वासप्रश्वास र तापमा खेर जान्छ।"
  },
  {
    q: "३. खाद्य शृङ्खलामा पहिलो पोषण तह (First Trophic Level - T1) मा कुन जीवहरू पर्दछन् ?",
    opts: [
      "हरिया बोटबिरुवाहरू (Producers)",
      "शाकाहारी जीवहरू (Herbivores)",
      "मांसाहारी जीवहरू (Carnivores)",
      "विच्छेदकहरू (Decomposers)"
    ],
    ans: 0,
    exp: "सूर्यको प्रकाशमा प्रकाश संश्लेषणद्वारा खाना बनाउने उत्पादक हरिया बोटबिरुवा तथा लेउ नै पहिलो पोषण तह (T1) हुन्।"
  },
  {
    q: "४. रुखको बोक्रामा पाइने लाइकेन्स (Lichens) मा लेउ र ढुसीबीचको सम्बन्ध कुन प्रकारको अन्तरक्रिया हो ?",
    opts: [
      "पारस्परिकता (Mutualism)",
      "सहभोजिता (Commensalism)",
      "परजीविता (Parasitism)",
      "सिकारिता (Predation)"
    ],
    ans: 0,
    exp: "लाइकेनमा लेउले खाना बनाउँछ र ढुसीले पानी तथा सुरक्षा दिन्छ; दुवै अनिवार्य रूपमा लाभान्वित हुने हुनाले यो Mutualism (+, +) हो।"
  },
  {
    q: "५. रुखको हाँगामा उम्रने सुनाखरी (Orchid/Epiphyte) ले रुखलाई कुनै असर नगरी घाम पाउने सम्बन्ध कुन हो ?",
    opts: [
      "पारस्परिकता (Mutualism)",
      "सहभोजिता (Commensalism)",
      "परजीविता (Parasitism)",
      "प्रतिस्पर्धा (Competition)"
    ],
    ans: 1,
    exp: "सहभोजिता (Commensalism - +, ०) मा एउटा जीवलाई फाइदा हुन्छ तर आश्रय दिने रुखलाई कुनै हानि वा फाइदा हुँदैन।"
  },
  {
    q: "६. प्रकृतिका सम्पूर्ण पारिस्थिक पद्धतिहरूमा कुन पारिस्थितिक पिरामिड सदैव ठाडो (Always Upright) मात्र हुन्छ ?",
    opts: [
      "संख्याको पिरामिड",
      "बायोमासको पिरामिड",
      "ऊर्जाको पिरामिड (Pyramid of Energy)",
      "उल्टो पिरामिड"
    ],
    ans: 2,
    exp: "प्रत्येक तहमा ९०% ऊर्जा क्षय भई माथिल्लो तहमा ऊर्जा सधैँ घट्दै मात्र जाने हुनाले ऊर्जाको पिरामिड सदैव ठाडो हुन्छ।"
  },
  {
    q: "७. एकल खाद्य शृङ्खलाभन्दा खाद्य जाल (Food Web) ले इकोसिस्टमलाई कुन प्रमुख फाइदा दिन्छ ?",
    opts: [
      "ऊर्जा नष्ट गर्दछ",
      "वैकल्पिक आहारा दिएर इकोसिस्टमलाई स्थिरता (Stability) प्रदान गर्दछ",
      "उत्पादकको संख्या घटाउँछ",
      "सबै मांसाहारीलाई नष्ट गर्छ"
    ],
    ans: 1,
    exp: "खाद्य जालमा धेरै वैकल्पिक आहाराका बाटाहरू हुने भएकाले एउटा जीव लोप भए पनि अर्को विकल्प उपलब्ध भई प्रणाली स्थिर रहन्छ।"
  },
  {
    q: "८. खेतमा किसानले सबै मुसा मार्दा धान उत्पादन किन घट्यो ?",
    opts: [
      "मुसाले माटो खुकुलो पार्न छाड्यो",
      "मुसाले खाने हानिकारक किराहरूको संख्या अनियन्त्रित बढेर धानबाली सखाप पारे",
      "धानको बीउ उम्रन सकेन",
      "पानीको अभाव भयो"
    ],
    ans: 1,
    exp: "मुसाले धानबाली नष्ट गर्ने किराहरू पनि खान्थ्यो; मुसा सखाप भएपछि ती किराहरू अनियन्त्रित भई धानको बोट र बाला सखाप पारे।"
  },
  {
    q: "९. कोसेबाली (सिमी, भटमास) को जराको गिर्खामा हावाको नाइट्रोजन स्थिर गरी दिने ब्याक्टेरिया कुन हो ?",
    opts: [
      "राइजोबियम (Rhizobium)",
      "इकोलाई (E. coli)",
      "ल्याक्टोब्यासिलस (Lactobacillus)",
      "च्याउ (Mushroom)"
    ],
    ans: 0,
    exp: "राइजोबियमले कोसेबालीको जरामा सहजीविता (Mutualism) गरी हावाको नाइट्रोजनलाई घुलित नाइट्रेटमा जैविक स्थिरीकरण गर्छ।"
  },
  {
    q: "१०. पानीमा मिसिएको गैर-विघटनशील कीटनाशक (DDT) खाद्यशृङ्खलाको सर्वोच्च तहमा करोडौँ गुणा सञ्चित हुने प्रक्रियालाई के भनिन्छ ?",
    opts: [
      "बायोम्याग्निफिकेसन (Biological Magnification)",
      "यूट्रोफिकेशन (Eutrophication)",
      "ट्रान्सपिरेसन (Transpiration)",
      "फोटोसिन्थेसिस (Photosynthesis)"
    ],
    ans: 0,
    exp: "बायोम्याग्निफिकेसन प्रक्रियामा गैर-विघटनशील विषादी प्रत्येक माथिल्लो पोषण तहका जीवहरूको बोसोमा अत्यधिक सघनताका साथ थुप्रिँदै जान्छ।"
  }
];

function renderC9U6Quiz() {
  const container = document.getElementById('c9u6-quiz-container');
  if (!container) return;

  let score = 0;
  let answeredCount = 0;

  let html = '';
  C9U6_QUIZ_DATA.forEach((item, qIdx) => {
    const userAns = c9u6QuizAnswers[qIdx];
    const isAnswered = userAns !== undefined;
    const isCorrect = userAns === item.ans;

    if (isAnswered) {
      answeredCount++;
      if (isCorrect) score++;
    }

    let borderClass = 'border-slate-200';
    if (isAnswered) {
      borderClass = isCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-rose-300 bg-rose-50/20';
    }

    html += `
      <div class="bg-white border ${borderClass} rounded-3xl p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold px-2.5 py-1 rounded-full ${isAnswered ? (isCorrect ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800') : 'bg-slate-100 text-slate-700'}">
            प्रश्न ${qIdx + 1} • वस्तुगत
          </span>
          ${isAnswered ? (isCorrect ? '<span class="text-xs text-emerald-600 font-bold">✓ सही उत्तर (+१)</span>' : '<span class="text-xs text-rose-600 font-bold">✗ गलत उत्तर (०)</span>') : '<span class="text-xs text-slate-400">उत्तर छनोट गर्नुहोस्</span>'}
        </div>

        <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
          ${item.opts.map((opt, optIdx) => {
            let optClass = 'bg-slate-50 border-slate-200 hover:bg-slate-100 text-slate-700';
            if (isAnswered) {
              if (optIdx === item.ans) {
                optClass = 'bg-emerald-100 border-emerald-400 text-emerald-950 font-bold';
              } else if (optIdx === userAns) {
                optClass = 'bg-rose-100 border-rose-400 text-rose-950 font-bold';
              } else {
                optClass = 'bg-slate-50 border-slate-100 text-slate-400 opacity-60';
              }
            }

            return `
              <button onclick="selectC9U6QuizOption(${qIdx}, ${optIdx})" class="p-3 rounded-2xl border text-left text-xs md:text-sm transition cursor-pointer flex items-center gap-2 ${optClass}">
                <span class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold ${optIdx === item.ans && isAnswered ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-700'}">
                  ${String.fromCharCode(65 + optIdx)}
                </span>
                <span class="flex-1">${opt}</span>
              </button>
            `;
          }).join('')}
        </div>

        ${isAnswered ? `
          <div class="p-3 rounded-2xl ${isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-rose-50 border border-rose-200 text-rose-900'} text-xs space-y-1 mt-2">
            <strong>💡 व्याख्या:</strong>
            <p>${item.exp}</p>
          </div>
        ` : ''}
      </div>
    `;
  });

  container.innerHTML = html;

  const toNepaliNumC9U6 = (n) => {
    const d = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
    return String(n).split('').map(c => d[parseInt(c, 10)] || c).join('');
  };
  const scoreBadge = document.getElementById('c9u6-quiz-score-badge');
  if (scoreBadge) {
    scoreBadge.textContent = `${toNepaliNumC9U6(score)} / १०`;
  }
}

function selectC9U6QuizOption(qIdx, optIdx) {
  if (c9u6QuizAnswers[qIdx] !== undefined) return;
  c9u6QuizAnswers[qIdx] = optIdx;

  const isCorrect = optIdx === C9U6_QUIZ_DATA[qIdx].ans;
  if (isCorrect) playAudioC9U6('correct');
  else playAudioC9U6('wrong');

  renderC9U6Quiz();
}

function resetC9U6Quiz() {
  c9u6QuizAnswers = {};
  playAudioC9U6('click');
  renderC9U6Quiz();
}

// -------------------------------------------------------------------------
// Initialization Entrypoint for Unit 6
// -------------------------------------------------------------------------
function initC9U6() {
  selectEcosystemTypeC9U6('grassland');
  selectOrganismC9U6('grass');
  setEnergySubModeC9U6('pyramid');
  setSolarInputC9U6(100000);
  selectInteractionC9U6('mutualism');
  renderC9U6Quiz();
}

// Ensure startup trigger
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    if (typeof initC9U6 === 'function') initC9U6();
  });
} else {
  if (typeof initC9U6 === 'function') initC9U6();
}

'''

# Verify no double virama
assert '\u094d\u094d' not in js_code, "Double virama detected in JS code!"

output_path = "scratch/c9u6_js.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"Successfully generated {output_path} ({len(js_code)} bytes).")
