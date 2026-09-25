# -*- coding: utf-8 -*-
"""
Class 9 Science Unit 3 JavaScript Generator
"""
import json

js_path = "scratch/c9u3_js.js"

print("Compiling Unit 3 JS...")

js_code = r'''
// =========================================================================
// GRADE 9 UNIT 3: MUSHROOM (च्याउ) INTERACTIVE CONTROLLER
// =========================================================================

let activeC9U3Tab = 'concepts';
let activeC9U3LabMode = 'anatomy';
let activeC9U3AnatSub = 'external';
let activeC9U3ExtPart = 'pileus';
let activeC9U3IntPart = 'basidium';
let activeC9U3FarmStage = 1;
let activeC9U3Moisture = 'ideal';
let activeC9U3Specimen = 'kanne';
let c9u3QuizAnswers = {};

// Tab Switching
function setTabC9U3(tab) {
  activeC9U3Tab = tab;
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const view = document.getElementById(`c9u3-view-${t}`);
    const btn = document.getElementById(`c9u3-tab-${t}`);
    if (view) {
      if (t === tab) {
        view.classList.remove('hidden');
      } else {
        view.classList.add('hidden');
      }
    }
    if (btn) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-emerald-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer font-bold';
      }
    }
  });

  if (tab === 'quiz') {
    renderC9U3Quiz();
  }
}

// Lab Mode Switching
function setLabModeC9U3(mode) {
  activeC9U3LabMode = mode;
  const modes = ['anatomy', 'farming', 'safety'];
  modes.forEach(m => {
    const container = document.getElementById(`c9u3-lab-mode-${m}`);
    const btn = document.getElementById(`c9u3-btn-mode-${m}`);
    if (container) {
      if (m === mode) {
        container.classList.remove('hidden');
      } else {
        container.classList.add('hidden');
      }
    }
    if (btn) {
      if (m === mode) {
        btn.className = 'px-3.5 py-2 rounded-xl text-xs font-bold transition bg-emerald-600 text-white shadow-sm cursor-pointer';
      } else {
        btn.className = 'px-3.5 py-2 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:bg-slate-700 cursor-pointer';
      }
    }
  });

  if (mode === 'anatomy') {
    setAnatomySubModeC9U3(activeC9U3AnatSub);
  } else if (mode === 'farming') {
    renderFarmStepperC9U3();
    setFarmStageC9U3(activeC9U3FarmStage);
  } else if (mode === 'safety') {
    renderSpecimenButtonsC9U3();
    selectSpecimenC9U3(activeC9U3Specimen);
  }
}

// Anatomy Submode Switching
function setAnatomySubModeC9U3(sub) {
  activeC9U3AnatSub = sub;
  const extPanel = document.getElementById('c9u3-anat-panel-external');
  const intPanel = document.getElementById('c9u3-anat-panel-internal');
  const extBtn = document.getElementById('c9u3-subbtn-external');
  const intBtn = document.getElementById('c9u3-subbtn-internal');

  if (sub === 'external') {
    if (extPanel) extPanel.classList.remove('hidden');
    if (intPanel) intPanel.classList.add('hidden');
    if (extBtn) extBtn.className = 'px-4 py-2 rounded-2xl text-xs font-black transition border bg-emerald-500/20 border-emerald-400 text-emerald-300 cursor-pointer';
    if (intBtn) intBtn.className = 'px-4 py-2 rounded-2xl text-xs font-black transition border bg-slate-800/80 border-slate-700 text-slate-400 hover:text-white cursor-pointer';
    selectExtPartC9U3(activeC9U3ExtPart);
  } else {
    if (extPanel) extPanel.classList.add('hidden');
    if (intPanel) intPanel.classList.remove('hidden');
    if (extBtn) extBtn.className = 'px-4 py-2 rounded-2xl text-xs font-black transition border bg-slate-800/80 border-slate-700 text-slate-400 hover:text-white cursor-pointer';
    if (intBtn) intBtn.className = 'px-4 py-2 rounded-2xl text-xs font-black transition border bg-cyan-500/20 border-cyan-400 text-cyan-300 cursor-pointer';
    selectIntPartC9U3(activeC9U3IntPart);
  }
}

// External Anatomy Data & Handlers
const C9U3_EXT_ANATOMY_DATA = {
  pileus: {
    eng: 'PILEUS / CAP',
    nep: 'पाइलस (Pileus / छाता)',
    role: 'सुरक्षा छाता',
    loc: 'स्टाइपको माथिल्लो टुप्पोमा रहेको फराकिलो, छाता आकारको भाग। यसको सतह चिल्लो, फुस्रो वा कत्लादार हुन्छ।',
    fn: 'तल्लो भागमा रहेका संवेदनशील पत्रहरू (गिल्स) र बन्दै गरेका बीजाणु (Basidiospore) हरूलाई घाम, पानी र बाह्य चोटपटकबाट सुरक्षा प्रदान गर्दछ।',
    fact: 'पाइलसको आकार च्याउको उमेर अनुसार बटन अवस्थामा गोलो र परिपक्व अवस्थामा फराकिलो छाता जस्तै फुल्दछ।'
  },
  gills: {
    eng: 'GILLS / LAMELLAE',
    nep: 'गिल्स (Gills / पत्रहरू)',
    role: 'बीजाणु उत्पादन केन्द्र',
    loc: 'पाइलसको भित्री (तल्लो) सतहमा साइकलको पाङ्ग्राका स्पोक जस्तै केन्द्रबाट बाहिरतिर फिँजारिएका पत्रैपत्र संरचना।',
    fn: 'मियोसिस विभाजन मार्फत करोडौँ बेसिडियोस्पोरहरू उत्पादन गर्ने र हावामा सजिलै उडेर टाढासम्म फैलिन मद्दत गर्ने।',
    fact: 'गिल्सको सूक्ष्म अनुप्रस्थ काटमा ट्रामा, सब-हाइमेनियम र हाइमेनियम गरी तीन स्पष्ट तहहरू पाइन्छन्।'
  },
  annulus: {
    eng: 'ANNULUS / RING',
    nep: 'एनुलस (Annulus / औँठी)',
    role: 'झिल्लीदार अवशेष',
    loc: 'डाँठ (स्टाइप) को माथिल्लो भागमा पाइने औँठी जस्तो पातलो झिल्लीदार घेरा। (यो केही च्याउमा मात्र पाइन्छ)।',
    fn: 'च्याउ सानो छँदा गिल्सलाई छोपेर राख्ने भेल (Velum) च्याउ फुल्दा च्यातिएर बाँकी रहेको अवशेष हो।',
    fact: 'विषालु च्याउ (विशेषगरी Amanita) पहिचान गर्न डाँठमा एनुलस र फेदमा भल्भा हुनु एक प्रमुख सूचक हो।'
  },
  stipe: {
    eng: 'STIPE / STEM',
    nep: 'स्टाइप (Stipe / डाँठ)',
    role: 'शारीरिक खम्बा',
    loc: 'माटोको सतहबाट ठाडो माथितिर उठेको बेलनाकार, बलियो र सेतो वा खैरो रङको डाँठ।',
    fn: 'पाइलस (छाता) लाई माटोभन्दा माथि उठाएर अड्याउने र हावामा बीजाणुहरू टाढासम्म फैलाउन सहयोग गर्ने।',
    fact: 'स्टाइप हाइफीहरू बाक्लो र समानान्तर रूपमा मिलेर बनेको हुन्छ जसले पोषक तत्व माथितिर ढुवानी गर्छ।'
  },
  mycelium: {
    eng: 'MYCELIUM / HYPHAE',
    nep: 'माइसेलियम (Mycelium / जरा जालो)',
    role: 'भेजिटेटिभ पोषण भाग',
    loc: 'जमिनमुनि, परालभित्र वा काठको मुढाभित्र मसिना सेता धागाहरू (Hyphae) को रूपमा फैलिएको जालो।',
    fn: 'सडेगलेका जैविक वस्तुमा पाचन रस निष्कासन गरी बाह्य पाचन मार्फत पानी, खनिज र पोषक तत्व सोस्ने।',
    fact: 'च्याउको वास्तविक शरीर माइसेलियम हो, जसले वर्षौंसम्म माटोमुनि बाँचेर अनुकूल मौसममा फ्रुटिङ बडी निकाल्छ।'
  }
};

function selectExtPartC9U3(partId) {
  activeC9U3ExtPart = partId;
  const data = C9U3_EXT_ANATOMY_DATA[partId];
  if (!data) return;

  const engEl = document.getElementById('c9u3-ext-engname');
  const nepEl = document.getElementById('c9u3-ext-nepname');
  const roleEl = document.getElementById('c9u3-ext-role');
  const locEl = document.getElementById('c9u3-ext-location');
  const fnEl = document.getElementById('c9u3-ext-function');
  const factEl = document.getElementById('c9u3-ext-fact');

  if (engEl) engEl.textContent = data.eng;
  if (nepEl) nepEl.textContent = data.nep;
  if (roleEl) roleEl.textContent = data.role;
  if (locEl) locEl.textContent = data.loc;
  if (fnEl) fnEl.textContent = data.fn;
  if (factEl) factEl.textContent = data.fact;

  // Update button highlights
  const parts = ['pileus', 'gills', 'annulus', 'stipe', 'mycelium'];
  parts.forEach(p => {
    const btn = document.getElementById(`c9u3-pbtn-${p}`);
    if (btn) {
      if (p === partId) {
        btn.className = 'px-3 py-1 rounded-xl text-xs font-bold transition bg-emerald-600 text-white cursor-pointer';
      } else {
        btn.className = 'px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer';
      }
    }
  });
}

// Internal Gill Anatomy Data & Handlers
const C9U3_INT_ANATOMY_DATA = {
  basidium: {
    eng: 'FERTILE CLUB CELL',
    nep: 'बेसिडियम (Basidium)',
    role: 'उर्वर कोष (Fertile)',
    loc: 'गिल्सको सबैभन्दा बाहिरी हाइमेनियम तहमा प्याराफाइसिसहरूको बीचमा ठाडो मिलेर रहेको गदा आकारको कोष।',
    fn: 'यसभित्र क्यारियोगामी र मियोसिस विभाजन भई टुप्पोका ४ ओटा स्टिरिग्मामा ४ बेसिडियोस्पोरहरू बन्दछन्।',
    fact: 'उत्पादित ४ ओटा बीजाणुहरूमध्ये २ वटा धनात्मक (+) र २ वटा ऋणात्मक (-) स्ट्रेनका अगुणित (n) हुन्छन्।'
  },
  paraphysis: {
    eng: 'STERILE SUPPORT CELL',
    nep: 'प्याराफाइसिस (Paraphysis)',
    role: 'बन्ध्या कोष (Sterile)',
    loc: 'हाइमेनियम तहमा बेसिडियमहरूको बीच-बीचमा रहेका पातला लाम्चा कोषहरू।',
    fn: 'बेसिडियमहरूलाई एकआपसमा टाँसिन नदिई अलग राख्ने, ठाडो अड्याउने र ओसिलो बनाई सुरक्षा दिने।',
    fact: 'यी कोषहरू बन्ध्या हुन्छन्, अर्थात् यिनीहरूले कुनै पनि बीजाणु (spores) उत्पादन गर्दैनन्।'
  },
  spores: {
    eng: 'BASIDIOSPORES (n)',
    nep: 'बेसिडियोस्पोर (Basidiospores)',
    role: 'प्रजनन बीजाणु (Haploid)',
    loc: 'बेसिडियमको टुप्पोमा रहेका मसिना स्टिरिग्मा (Sterigmata) का काँडामा झुण्डिएका सूक्ष्म बीजाणुहरू।',
    fn: 'परिपक्व भएपछि हावाद्वारा टाढासम्म उडेर अनुकूल चिस्यानयुक्त ठाउँमा अंकुरण भई प्राथमिक माइसेलियम बनाउने।',
    fact: 'एउटै च्याउको छाताबाट २४ घण्टाभित्र करोडौँको संख्यामा बेसिडियोस्पोरहरू हावामा उडाइन्छन्।'
  },
  subhymenium: {
    eng: 'SUB-HYMENIUM LAYER',
    nep: 'सब-हाइमेनियम (Sub-hymenium)',
    role: 'मध्यवर्ती पोषक तह',
    loc: 'केन्द्रीय ट्रामा र बाहिरी हाइमेनियमको बीचमा रहने साना गोलाकार कोषहरूको तह।',
    fn: 'ट्रामाका हाइफीहरूबाट पोषक तत्व र पानी ग्रहण गरी हाइमेनियमका बेसिडियम र प्याराफाइसिससम्म पुर्‍याउने।',
    fact: 'यसमा कोषहरू धेरै बाक्ला र घना रूपमा मिलेका हुन्छन्।'
  },
  trama: {
    eng: 'TRAMA / CENTRAL CORE',
    nep: 'ट्रामा (Trama)',
    role: 'केन्द्रीय मेरुदण्ड',
    loc: 'गिल्सको ठीक बीचमा रहने समानान्तर र लामा हाइफीहरूको केन्द्रीय भित्री तह।',
    fn: 'गिल्सलाई बाहिरी दृढता र आकार प्रदान गर्नुका साथै पाइलसबाट गिल्सभरि पोषक तत्व ढुवानी गर्ने।',
    fact: 'गिल्सको मेरुदण्डको रूपमा यसले दुवै छेउका सब-हाइमेनियम र हाइमेनियमलाई मजबुत आधार दिन्छ।'
  }
};

function selectIntPartC9U3(partId) {
  activeC9U3IntPart = partId;
  const data = C9U3_INT_ANATOMY_DATA[partId];
  if (!data) return;

  const engEl = document.getElementById('c9u3-int-engname');
  const nepEl = document.getElementById('c9u3-int-nepname');
  const roleEl = document.getElementById('c9u3-int-role');
  const locEl = document.getElementById('c9u3-int-location');
  const fnEl = document.getElementById('c9u3-int-function');
  const factEl = document.getElementById('c9u3-int-fact');

  if (engEl) engEl.textContent = data.eng;
  if (nepEl) nepEl.textContent = data.nep;
  if (roleEl) roleEl.textContent = data.role;
  if (locEl) locEl.textContent = data.loc;
  if (fnEl) fnEl.textContent = data.fn;
  if (factEl) factEl.textContent = data.fact;

  const parts = ['basidium', 'paraphysis', 'spores', 'subhymenium', 'trama'];
  parts.forEach(p => {
    const btn = document.getElementById(`c9u3-ibtn-${p}`);
    if (btn) {
      if (p === partId) {
        btn.className = 'px-3 py-1 rounded-xl text-xs font-bold transition bg-emerald-600 text-white cursor-pointer';
      } else {
        btn.className = 'px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer';
      }
    }
  });
}

// Cultivation Simulator Data & Handlers
const C9U3_FARM_STAGES_DATA = [
  {
    step: 1,
    title: '१. परालको छनोट र टुक्राउने कार्य',
    desc: 'ताजा, नकुहिएको र ओस नलागेको सफा सुकेको धानको पराल छान्ने। हँसिया वा मेसिनले पराललाई २ देखि ३ इन्च (५-८ से.मी.) लामा टुक्राहरूमा काट्ने।',
    timeline: 'समय: दिन १',
    temp: 'सामान्य (१५-२५°C)',
    moisture: 'सुख्खा (१०%)',
    light: 'उज्यालो',
    hygiene: 'उच्च सरसफाइ'
  },
  {
    step: 2,
    title: '२. पराल भिजाउने र उसिन्ने (स्टीम निर्मलीकरण)',
    desc: 'काटेको पराललाई सफा पानीमा १०-१२ घण्टा भिजाउने। त्यसपछि ड्रममा हालेर बाफमा १ देखि २ घण्टासम्म उमाल्ने। यसले हानिकारक ढुसी, ब्याक्टेरिया र कीराका अण्डा पूर्ण नष्ट गर्छ।',
    timeline: 'समय: दिन २',
    temp: 'उच्च (१००°C बाफ)',
    moisture: 'पूर्ण भिजेको (१००%)',
    light: 'आवश्यक छैन',
    hygiene: 'जीवाणुविहीन'
  },
  {
    step: 3,
    title: '३. पराल सेलाउने र चिस्यान नियन्त्रण',
    desc: 'उसिनेको पराललाई सफा प्लास्टिकमाथि छायाँमा फैलाएर सेलाउने। हातले मुठ्ठी पारेर बेस्सरी निचोर्दा पानी नचुहिने तर हात भिज्ने (६०-६५% चिस्यान) कायम गर्ने।',
    timeline: 'समय: दिन २ (साँझ)',
    temp: 'कोठाको (२०-२५°C)',
    moisture: 'आदर्श (६०-६५%)',
    light: 'छायाँ',
    hygiene: 'हात धोएर सफा'
  },
  {
    step: 4,
    title: '४. बीउ (Spawn) मिसाउने र प्लास्टिकको पोका बाँध्ने',
    desc: '१६×२६ इन्चको प्लास्टिक झोलामा ४ इन्च पराल र किनारमा च्याउको बीउ तह-तह गरी भर्ने। मुख कसिलो बाँध्ने र हावा सञ्चारका लागि १०-१५ साना प्वालहरू पार्ने।',
    timeline: 'समय: दिन ३',
    temp: '२०-२५°C',
    moisture: '६०-६५%',
    light: 'सामान्य',
    hygiene: 'स्पटलेस निर्मल'
  },
  {
    step: 5,
    title: '५. ओथारो (Incubation) र माइसेलियम विस्तार',
    desc: 'पोकाहरूलाई अँध्यारो र न्यानो (२०-२५°C) कोठामा र्‍याकमा राख्ने। १५ देखि २० दिनभित्र पराल पूरै सेतो कपास जस्तो ढुसी (माइसेलियम) ले ढाकिन्छ।',
    timeline: 'समय: दिन ४-२२',
    temp: '२०-२५°C (न्यानो)',
    moisture: '७०-८०% (कोठा)',
    light: 'पूर्ण अँध्यारो',
    hygiene: 'ढुसीरहित कोठा'
  },
  {
    step: 6,
    title: '६. झोला खोल्ने, पानी छर्कने र च्याउ टिप्ने',
    desc: 'सेतो माइसेलियम फैलिएपछि प्लास्टिक झोला चक्कुले काटेर हटाउने। कोठामा मधुरो उज्यालो र ताजा हावा दिने तथा दिनको २-३ पटक पानी छर्कने। ४-५ दिनमा च्याउ पूर्ण तयार भएपछि हल्का बटारेर टिप्ने।',
    timeline: 'समय: दिन २३-३५',
    temp: '१८-२२°C',
    moisture: '८५-९०% (चिसो)',
    light: 'मधुरो प्रकाश',
    hygiene: 'दैनिक रेखदेख'
  }
];

function renderFarmStepperC9U3() {
  const container = document.getElementById('c9u3-farming-stepper');
  if (!container) return;
  container.innerHTML = C9U3_FARM_STAGES_DATA.map((s, idx) => {
    const isCurrent = s.step === activeC9U3FarmStage;
    const btnCls = isCurrent
      ? 'bg-emerald-600 text-white font-black border-emerald-400'
      : 'bg-slate-800 text-slate-400 hover:text-white border-slate-700 font-bold';
    const nepDigits = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९", "१०"];
    return `<button onclick="setFarmStageC9U3(${s.step})" class="w-8 h-8 rounded-xl border text-xs transition flex items-center justify-center cursor-pointer ${btnCls}">${nepDigits[s.step]}</button>`;
  }).join('');
}

function setFarmStageC9U3(stageNum) {
  activeC9U3FarmStage = stageNum;
  const data = C9U3_FARM_STAGES_DATA[stageNum - 1];
  if (!data) return;

  const nepDigits = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९", "१०"];
  const badgeEl = document.getElementById('c9u3-farm-step-badge');
  const timeEl = document.getElementById('c9u3-farm-timeline');
  const titleEl = document.getElementById('c9u3-farm-title');
  const descEl = document.getElementById('c9u3-farm-desc');
  const tempEl = document.getElementById('c9u3-farm-temp');
  const strawMEl = document.getElementById('c9u3-farm-straw-moisture');
  const lightEl = document.getElementById('c9u3-farm-light');
  const hygEl = document.getElementById('c9u3-farm-hygiene');
  const prevBtn = document.getElementById('c9u3-farm-prev-btn');
  const nextBtn = document.getElementById('c9u3-farm-next-btn');

  if (badgeEl) badgeEl.textContent = `चरण ${nepDigits[data.step]} / ६`;
  if (timeEl) timeEl.textContent = data.timeline;
  if (titleEl) titleEl.textContent = data.title;
  if (descEl) descEl.textContent = data.desc;
  if (tempEl) tempEl.textContent = data.temp;
  if (strawMEl) strawMEl.textContent = data.moisture;
  if (lightEl) lightEl.textContent = data.light;
  if (hygEl) hygEl.textContent = data.hygiene;

  if (prevBtn) prevBtn.disabled = (stageNum === 1);
  if (nextBtn) nextBtn.disabled = (stageNum === 6);

  renderFarmStepperC9U3();
}

function prevFarmStageC9U3() {
  if (activeC9U3FarmStage > 1) {
    setFarmStageC9U3(activeC9U3FarmStage - 1);
  }
}

function nextFarmStageC9U3() {
  if (activeC9U3FarmStage < 6) {
    setFarmStageC9U3(activeC9U3FarmStage + 1);
  }
}

function setMoistureC9U3(level) {
  activeC9U3Moisture = level;
  const btnDry = document.getElementById('c9u3-mbtn-dry');
  const btnIdeal = document.getElementById('c9u3-mbtn-ideal');
  const btnWet = document.getElementById('c9u3-mbtn-wet');
  const feedbackEl = document.getElementById('c9u3-moisture-feedback');

  // Reset styles
  [btnDry, btnIdeal, btnWet].forEach(b => {
    if (b) b.className = 'p-2.5 rounded-xl border border-slate-600 text-xs font-bold text-center transition cursor-pointer bg-slate-900 text-slate-300';
  });

  if (level === 'dry') {
    if (btnDry) btnDry.className = 'p-2.5 rounded-xl border border-amber-500 text-xs font-bold text-center transition cursor-pointer bg-amber-600 text-white shadow-sm';
    if (feedbackEl) {
      feedbackEl.className = 'p-3.5 rounded-2xl border text-xs leading-relaxed space-y-1 bg-amber-950/60 border-amber-500/50 text-amber-200';
      feedbackEl.innerHTML = `<strong class="font-bold text-amber-300 flex items-center gap-1.5"><span>⚠️ चेतावनी: चिस्यान अपुग (<५०% सुख्खा)</span></strong><p>पराल धेरै सुख्खा भएमा बीउमा भएको ढुसीले खाना र पानी सोस्न नसकी माइसेलियम फैलिँदैन र सुकेर नष्ट हुन्छ।</p>`;
    }
  } else if (level === 'ideal') {
    if (btnIdeal) btnIdeal.className = 'p-2.5 rounded-xl border border-emerald-500 text-xs font-bold text-center transition cursor-pointer bg-emerald-600 text-white shadow-sm';
    if (feedbackEl) {
      feedbackEl.className = 'p-3.5 rounded-2xl border text-xs leading-relaxed space-y-1 bg-emerald-950/60 border-emerald-500/50 text-emerald-200';
      feedbackEl.innerHTML = `<strong class="font-bold text-emerald-300 flex items-center gap-1.5"><span>✓ आदर्श अवस्था (६०-६५% चिस्यान)</span></strong><p>हातले बेस्सरी निचोर्दा औँलाको कापबाट पानीका थोपा नचुहिने तर हातको हत्केला राम्रोसँग भिज्ने अवस्था। माइसेलियम द्रुत गतिमा फैलिनका लागि यो सर्वोत्तम हो।</p>`;
    }
  } else if (level === 'wet') {
    if (btnWet) btnWet.className = 'p-2.5 rounded-xl border border-rose-500 text-xs font-bold text-center transition cursor-pointer bg-rose-600 text-white shadow-sm';
    if (feedbackEl) {
      feedbackEl.className = 'p-3.5 rounded-2xl border text-xs leading-relaxed space-y-1 bg-rose-950/60 border-rose-500/50 text-rose-200';
      feedbackEl.innerHTML = `<strong class="font-bold text-rose-300 flex items-center gap-1.5"><span>❌ खतरा: अत्यधिक चिस्यान (>७५% पानी चुहिने)</span></strong><p>अत्यधिक पानीले पोकाभित्र अक्सिजन समाप्त पार्छ। अवायवीय जीवाणु मौलाएर पराल कुहिन थाल्छ र दुर्गन्ध आई पूरै बाली नष्ट हुन्छ।</p>`;
    }
  }
}

// Poisonous Mushroom Safety Inspector Data & Handlers
const C9U3_SPECIMEN_DATA = {
  kanne: {
    id: 'kanne',
    nep: 'कन्ने च्याउ (Oyster Mushroom)',
    sci: 'Pleurotus ostreatus',
    badge: 'खानयोग्य (सुरक्षित)',
    badgeCls: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
    volva: 'छैन (Absent)',
    annulus: 'छैन (Absent)',
    cap: 'हल्का खैरो वा सेतो, चिल्लो छाता',
    bruise: 'हुँदैन (रङ स्थिर)',
    analysis: 'नेपालमा व्यावसायिक रूपमा सबैभन्दा धेरै उत्पादन हुने खानयोग्य च्याउ हो। यसमा करिब ३०% उच्च प्रोटिन, भिटामिन बी र खनिज प्रशस्त हुन्छ। घरमै परालमा सहजै उब्जाउन सकिन्छ।'
  },
  deathcap: {
    id: 'deathcap',
    nep: 'डेथ क्याप (Death Cap Mushroom)',
    sci: 'Amanita phalloides',
    badge: 'घातक विषालु (Deadly Toxic)',
    badgeCls: 'bg-rose-500/20 text-rose-300 border-rose-500/40',
    volva: 'उपस्थित (कचौरा जस्तो सेतो भल्भा)',
    annulus: 'उपस्थित (डाँठमा औँठी जस्तो एनुलस)',
    cap: 'फिक्का हरियो, पहेंलो वा सेतो, चिल्लो',
    bruise: 'हुँदैन (चाँदी कालो बनाउँदैन!)',
    analysis: 'संसारकै सबैभन्दा घातक च्याउ जसले च्याउ विषसम्बन्धी ९०% मृत्यु गराउँछ। यसमा हुने अमानिटिन (Amatoxin) ले कलेजो र मिर्गौला पूर्णतया नष्ट गर्छ। यसको कुनै प्रतिविष (Antidote) हुँदैन!'
  },
  gobre: {
    id: 'gobre',
    nep: 'डल्ले / गोब्रे च्याउ (Button Mushroom)',
    sci: 'Agaricus bisporus',
    badge: 'खानयोग्य (व्यावसायिक)',
    badgeCls: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
    volva: 'छैन (Absent)',
    annulus: 'सानो छँदा झिल्ली हुन्छ, पछि हराउँछ',
    cap: 'सेतो वा हल्का खैरो, डल्लो',
    bruise: 'हल्का गुलाबी/खैरो हुन सक्छ',
    analysis: 'विश्वव्यापी रूपमा सबैभन्दा बढी खपत हुने डल्ले च्याउ। यसलाई सडेको गोबर र कम्पोस्ट मलमा खेती गरिन्छ। यसमा उच्च भिटामिन डी, फलाम र सेलेनियम पाइन्छ।'
  },
  flyagaric: {
    id: 'flyagaric',
    nep: 'फ्लाई एगारिक (Fly Agaric)',
    sci: 'Amanita muscaria',
    badge: 'विषालु / भ्रामक (Hallucinogenic)',
    badgeCls: 'bg-amber-500/20 text-amber-300 border-amber-500/40',
    volva: 'उपस्थित (फेदमा गाँठो र कत्ला)',
    annulus: 'उपस्थित (सेतो झिल्लीदार औँठी)',
    cap: 'गाढा चहकिलो रातो र त्यसमाथि सेता कत्लाहरू',
    bruise: 'काट्दा पहेंलो हुन सक्छ',
    analysis: 'गाढा रातो छातामा सेता खटिरा जस्ता थोप्ला हुने आकर्षक च्याउ। यसमा म्युसिमोल (Muscimol) र इबोटेनिक एसिड हुन्छ जसले स्नायु प्रणालीमा भ्रम (Hallucination), वाकवाकी र बेहोसी गराउँछ।'
  },
  ganoderma: {
    id: 'ganoderma',
    nep: 'रातो च्याउ (Reishi / Lingzhi)',
    sci: 'Ganoderma lucidum',
    badge: 'औषधीय (Medicinal / Anti-cancer)',
    badgeCls: 'bg-purple-500/20 text-purple-300 border-purple-500/40',
    volva: 'छैन (Absent)',
    annulus: 'छैन (Absent)',
    cap: 'काठ जस्तो कडा, चम्किलो रातो-खैरो',
    bruise: 'हुँदैन (काठ जस्तै दह्रो)',
    analysis: 'यसलाई तरकारीको रूपमा खाइँदैन तर सुकाएर धूलो वा चिया बनाइन्छ। यसमा पाइने पोलिस्याकराइड्स र ट्राइटरपेन्सले क्यान्सर प्रतिरोधी, रक्तचाप नियन्त्रण र आयु बढाउने अचुक औषधिको काम गर्छन्।'
  }
};

function renderSpecimenButtonsC9U3() {
  const container = document.getElementById('c9u3-specimen-buttons');
  if (!container) return;
  const specimens = Object.values(C9U3_SPECIMEN_DATA);
  container.innerHTML = specimens.map(s => {
    const isCurrent = s.id === activeC9U3Specimen;
    const btnCls = isCurrent
      ? 'bg-emerald-600 text-white font-black border-emerald-400'
      : 'bg-slate-800 text-slate-300 hover:text-white border-slate-700 font-bold';
    return `<button onclick="selectSpecimenC9U3('${s.id}')" class="px-3.5 py-2 rounded-2xl text-xs transition border cursor-pointer ${btnCls}">${s.nep.split(' ')[0]} (${s.sci})</button>`;
  }).join('');
}

function selectSpecimenC9U3(specId) {
  activeC9U3Specimen = specId;
  const data = C9U3_SPECIMEN_DATA[specId];
  if (!data) return;

  const sciEl = document.getElementById('c9u3-spec-sciname');
  const nepEl = document.getElementById('c9u3-spec-nepname');
  const badgeEl = document.getElementById('c9u3-spec-verdict-badge');
  const volvaEl = document.getElementById('c9u3-spec-volva');
  const annEl = document.getElementById('c9u3-spec-annulus');
  const capEl = document.getElementById('c9u3-spec-cap');
  const bruiseEl = document.getElementById('c9u3-spec-bruise');
  const analysisEl = document.getElementById('c9u3-spec-analysis');

  if (sciEl) sciEl.textContent = data.sci;
  if (nepEl) nepEl.textContent = data.nep;
  if (badgeEl) {
    badgeEl.textContent = data.badge;
    badgeEl.className = `text-xs px-3 py-1 rounded-full font-bold border ${data.badgeCls}`;
  }
  if (volvaEl) volvaEl.textContent = data.volva;
  if (annEl) annEl.textContent = data.annulus;
  if (capEl) capEl.textContent = data.cap;
  if (bruiseEl) bruiseEl.textContent = data.bruise;
  if (analysisEl) analysisEl.textContent = data.analysis;

  renderSpecimenButtonsC9U3();
}

// Exercise Filtering
function filterC9U3Exercises(cat) {
  const cards = document.querySelectorAll('.c9u3-ex-card');
  cards.forEach(card => {
    if (cat === 'all' || card.dataset.cat === cat) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  const cats = ['all', 'mcq', 'reason', 'diff', 'qa', 'project'];
  cats.forEach(c => {
    const btn = document.getElementById(`c9u3-exbtn-${c}`);
    if (btn) {
      if (c === cat) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-black transition bg-emerald-600 text-white shadow-sm cursor-pointer whitespace-nowrap';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap';
      }
    }
  });
}

// Tier Filtering
function filterC9U3Tiers(tier) {
  const cards = document.querySelectorAll('.c9u3-tier-card');
  cards.forEach(card => {
    if (tier === 'all' || card.dataset.tier === tier) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  const tiers = ['all', 'k', 'u', 'ha'];
  tiers.forEach(t => {
    const btn = document.getElementById(`c9u3-tierbtn-${t}`);
    if (btn) {
      if (t === tier) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-black transition bg-emerald-600 text-white shadow-sm cursor-pointer whitespace-nowrap';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap';
      }
    }
  });
}

// Quiz Data & Engine
const C9U3_QUIZ_DATA = [
  {
    q: '१. च्याउलाई मृतोपजीवी (Saprotrophic) जीव भन्नुको मुख्य कारण कुन हो?',
    options: [
      'यसले प्रकाश-संश्लेषण गर्न सक्दैन',
      'यसले सडेगलेका जैविक वस्तुबाट खाना सोसेर प्राप्त गर्छ',
      'यो जमिनमुनि मात्र बाँच्न सक्छ',
      'यसले अरू जीवित प्राणीको रगत चुस्छ'
    ],
    correct: 1,
    exp: 'च्याउमा हरितकण नहुने भएकाले गोबर, पराल र कुहिएका जैविक पदार्थमा पाचन रस निष्कासन गरी तरल पोषण सोस्दछ।'
  },
  {
    q: '२. च्याउको कुन भागले जमिन वा माध्यमबाट पानी र पोषक तत्व सोस्ने कार्य गर्दछ?',
    options: [
      'पाइलस (Pileus)',
      'गिल्स (Gills)',
      'माइसेलियम (Mycelium)',
      'स्टाइप (Stipe)'
    ],
    correct: 2,
    exp: 'माइसेलियम मसिना धागो जस्ता हाइफीहरूको जालो हो जसले जमिनमुनिबाट पानी र जैविक वस्तु सोस्दछ।'
  },
  {
    q: '३. कुन च्याउबाट क्यान्सर रोगका उपचारका लागि औषधि बनाइन्छ?',
    options: [
      'रातो च्याउ (Ganoderma lucidum)',
      'डल्ले च्याउ (Agaricus bisporus)',
      'कन्ने च्याउ (Pleurotus ostreatus)',
      'डेथ क्याप (Amanita phalloides)'
    ],
    correct: 0,
    exp: 'रातो च्याउ (Ganoderma lucidum) मा क्यान्सर कोषको वृद्धिलाई रोक्ने विशिष्ट पोलिस्याकराइड्स र ट्राइटरपेन्स पाइन्छन्।'
  },
  {
    q: '४. गिल्सको हाइमेनियम (Hymenium) मा पाइने बन्ध्या (Sterile) कोष कुन हो?',
    options: [
      'बेसिडियम (Basidium)',
      'बेसिडियोस्पोर (Basidiospore)',
      'प्याराफाइसिस (Paraphysis)',
      'स्टिरिग्मा (Sterigma)'
    ],
    correct: 2,
    exp: 'प्याराफाइसिस बन्ध्या (sterile) कोष हो जसले कुनै बीजाणु बनाउँदैन तर बेसिडियमलाई सहारा र ओसिलोपन दिन्छ।'
  },
  {
    q: '५. एउटा परिपक्व बेसिडियम (Basidium) को टुप्पोमा कतिओटा बेसिडियोस्पोर बन्दछन्?',
    options: [
      '२ ओटा',
      '४ ओटा',
      '८ ओटा',
      '१६ ओटा'
    ],
    correct: 1,
    exp: 'बेसिडियममा मियोसिस विभाजन पश्चात् ४ ओटा स्टिरिग्मामा ठीक ४ ओटा बेसिडियोस्पोरहरू (२+ र २-) बन्दछन्।'
  },
  {
    q: '६. बेसिडियोस्पोर (Basidiospore) को आनुवंशिक अवस्था (Ploidy level) कस्तो हुन्छ?',
    options: [
      'अगुणित (Haploid, n)',
      'द्वैगुणी (Diploid, 2n)',
      'त्रिगुणी (Triploid, 3n)',
      'डिक्यारियोटिक (n + n)'
    ],
    correct: 0,
    exp: 'मियोसिस विभाजनपछि बन्ने भएकाले बेसिडियोस्पोर अगुणित (Haploid, n) हुन्छ।'
  },
  {
    q: '७. कन्ने च्याउ खेती गर्दा परालमा कति प्रतिशत चिस्यान कायम गरिनुपर्छ?',
    options: [
      '२० देखि ३० प्रतिशत',
      '४० देखि ५० प्रतिशत',
      '६० देखि ६५ प्रतिशत',
      '८५ देखि ९५ प्रतिशत'
    ],
    correct: 2,
    exp: '६० देखि ६५% चिस्यान आदर्श हो; हातले बेस्सरी निचोर्दा पानी नचुहिने तर हातको हत्केला भिज्ने अवस्था उपयुक्त हुन्छ।'
  },
  {
    q: '८. प्राथमिक माइसेलियम (Primary Mycelium) को कोषीय अवस्था कस्तो हुन्छ?',
    options: [
      'मोनोक्यारियोटिक (Monokaryotic, n)',
      'डिक्यारियोटिक (Dikaryotic, n+n)',
      'डिप्लोइड (Diploid, 2n)',
      'अकोषीय (Acellular)'
    ],
    correct: 0,
    exp: 'बेसिडियोस्पोरबाट सिधै उम्रने भएकाले प्राथमिक माइसेलियमको प्रत्येक कोषमा एउटा मात्र n न्युक्लियस (मोनोक्यारियोटिक) हुन्छ।'
  },
  {
    q: '९. सबैभन्दा घातक विषालु च्याउ डेथ क्याप (Amanita) मा पाइने मुख्य लक्षण कुन हो?',
    options: [
      'डाँठको फेदमा भल्भा र माथि एनुलस दुवै हुनु',
      'काँचो च्याउ छुँदा कालो हुनु',
      'हरितकण पाइने हुनु',
      'काठको मुढामा मात्र उम्रनु'
    ],
    correct: 0,
    exp: 'फेदमा कचौरा जस्तो भल्भा र डाँठमा औँठी जस्तो एनुलस हुनु अमानिटा प्रजातिका घातक विषालु च्याउको विशिष्ट लक्षण हो।'
  },
  {
    q: '१०. च्याउको सुकुटी बनाउँदा पानीको मात्रा कति प्रतिशतभन्दा कम झारिन्छ?',
    options: [
      '५० प्रतिशतभन्दा कम',
      '३० प्रतिशतभन्दा कम',
      '१० प्रतिशतभन्दा कम',
      '१ प्रतिशतभन्दा कम'
    ],
    correct: 2,
    exp: 'च्याउलाई सुकाएर पानीको मात्रा १०% भन्दा तल झार्दा सूक्ष्मजीवहरू मौलाउन नसकी च्याउ वर्षौंसम्म सुरक्षित रहन्छ।'
  }
];

function renderC9U3Quiz() {
  const container = document.getElementById('c9u3-quiz-container');
  if (!container) return;

  container.innerHTML = C9U3_QUIZ_DATA.map((item, qIdx) => {
    const answered = c9u3QuizAnswers[qIdx] !== undefined;
    const userChoice = c9u3QuizAnswers[qIdx];
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
              <button onclick="selectC9U3QuizOption(${qIdx}, ${optIdx})" ${answered ? 'disabled' : ''} class="p-3 rounded-2xl border text-left transition flex items-center gap-2 ${btnCls} cursor-pointer">
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

  updateC9U3QuizScore();
}

function selectC9U3QuizOption(qIdx, optIdx) {
  if (c9u3QuizAnswers[qIdx] !== undefined) return;
  c9u3QuizAnswers[qIdx] = optIdx;
  renderC9U3Quiz();
}

function updateC9U3QuizScore() {
  const badge = document.getElementById('c9u3-quiz-score-badge');
  if (!badge) return;

  let score = 0;
  Object.keys(c9u3QuizAnswers).forEach(qIdx => {
    if (c9u3QuizAnswers[qIdx] === C9U3_QUIZ_DATA[qIdx].correct) {
      score++;
    }
  });

  const nepDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '१०'];
  badge.textContent = `${nepDigits[score]} / १०`;
}

function resetC9U3Quiz() {
  c9u3QuizAnswers = {};
  renderC9U3Quiz();
}

'''

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"Wrote full JS to {js_path} ({len(js_code)} bytes)")
