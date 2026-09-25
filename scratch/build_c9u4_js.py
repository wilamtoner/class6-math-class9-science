# -*- coding: utf-8 -*-
"""
Class 9 Science Unit 4 (Evolution) JavaScript Generator
"""
import os

print("Generating scratch/c9u4_js.js...")

js_code = r'''
// =========================================================================
// GRADE 9 UNIT 4: EVOLUTION (क्रम विकास) INTERACTIVE CONTROLLER
// =========================================================================

let activeC9U4Tab = 'concepts';
let activeC9U4LabMode = 'anatomy';
let activeC9U4AnatSub = 'homology';
let activeC9U4HomologyOrgan = 'human';
let activeC9U4VestigialOrgan = 'appendix';
let activeC9U4ConnectingOrgan = 'archaeopteryx';
let c9u4MothEnv = 'clean';
let c9u4MothGen = 1;
let c9u4WhitePct = 85;
let c9u4BlackPct = 15;
let activeC9U4Mutation = 'polydactyly';
let c9u4QuizAnswers = {};

// Tab Switching
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

// Lab Mode Switching
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
}

// Anatomy Submode Switching
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
}

// Homology Organ Explorer
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
}

// Vestigial Organs Explorer
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

// Connecting Links Explorer
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

// Mode 2: Natural Selection Simulator (Industrial Melanism)
function setMothEnvC9U4(env) {
  c9u4MothEnv = env;
  const bClean = document.getElementById('c9u4-env-clean-btn');
  const bPol = document.getElementById('c9u4-env-polluted-btn');
  const barkView = document.getElementById('c9u4-bark-view');
  const envLbl = document.getElementById('c9u4-moth-env-label');

  if (env === 'clean') {
    if (bClean) bClean.className = 'py-2 px-3 rounded-xl border bg-emerald-600/30 border-emerald-500 text-emerald-300 font-bold transition cursor-pointer';
    if (bPol) bPol.className = 'py-2 px-3 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white font-bold transition cursor-pointer';
    if (barkView) barkView.className = 'w-full h-40 rounded-2xl border border-slate-700 bg-gradient-to-r from-stone-200 via-amber-100 to-stone-300 flex items-center justify-around relative overflow-hidden p-4 shadow-inner';
    if (envLbl) envLbl.textContent = 'सफा वन (Clean Lichen Bark)';
    c9u4WhitePct = 85;
    c9u4BlackPct = 15;
  } else {
    if (bClean) bClean.className = 'py-2 px-3 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white font-bold transition cursor-pointer';
    if (bPol) bPol.className = 'py-2 px-3 rounded-xl border bg-rose-600/30 border-rose-500 text-rose-300 font-bold transition cursor-pointer';
    if (barkView) barkView.className = 'w-full h-40 rounded-2xl border border-slate-700 bg-gradient-to-r from-stone-900 via-neutral-900 to-black flex items-center justify-around relative overflow-hidden p-4 shadow-inner';
    if (envLbl) envLbl.textContent = 'प्रदूषित औद्योगिक क्षेत्र (Sooty Bark)';
    c9u4WhitePct = 15;
    c9u4BlackPct = 85;
  }
  c9u4MothGen = 1;
  updateMothUI();
}

function stepMothGenC9U4() {
  if (c9u4MothGen < 10) {
    c9u4MothGen++;
  }
  if (c9u4MothEnv === 'clean') {
    c9u4WhitePct = Math.min(95, c9u4WhitePct + 2);
    c9u4BlackPct = 100 - c9u4WhitePct;
  } else {
    c9u4BlackPct = Math.min(96, c9u4BlackPct + 2);
    c9u4WhitePct = 100 - c9u4BlackPct;
  }
  updateMothUI();
}

function resetMothSimC9U4() {
  c9u4MothGen = 1;
  if (c9u4MothEnv === 'clean') {
    c9u4WhitePct = 85;
    c9u4BlackPct = 15;
  } else {
    c9u4WhitePct = 15;
    c9u4BlackPct = 85;
  }
  updateMothUI();
}

function updateMothUI() {
  const nepDigits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '१०'];
  const wBar = document.getElementById('c9u4-white-bar');
  const bBar = document.getElementById('c9u4-black-bar');
  const wPct = document.getElementById('c9u4-white-pct');
  const bPct = document.getElementById('c9u4-black-pct');
  const genBadge = document.getElementById('c9u4-moth-gen-badge');
  const diagTitle = document.getElementById('c9u4-moth-diag-title');
  const diagDesc = document.getElementById('c9u4-moth-diag-desc');

  if (wBar) wBar.style.width = `${c9u4WhitePct}%`;
  if (bBar) bBar.style.width = `${c9u4BlackPct}%`;
  if (wPct) wPct.textContent = `${c9u4WhitePct}%`;
  if (bPct) bPct.textContent = `${c9u4BlackPct}%`;
  if (genBadge) genBadge.textContent = `पुस्ता नं. ${nepDigits[c9u4MothGen] || c9u4MothGen}`;

  if (diagTitle && diagDesc) {
    if (c9u4MothEnv === 'clean') {
      diagTitle.textContent = 'सफा वातावरणमा प्राकृतिक छनोट (सेतो मथको प्रभुत्व)';
      diagDesc.textContent = `सफा रुखका काण्डमा हल्का लाइकेन पलाएकाले सेता मथहरू चराको आँखाबाट बच्दछन्। पुस्ता ${c9u4MothGen} सम्म आइपुग्दा सेता मथको अनुपात ${c9u4WhitePct}% पुगेको छ र कालो मथ सजिलै शिकार बनेका छन्।`;
    } else {
      diagTitle.textContent = 'औद्योगिक वातावरणमा प्राकृतिक छनोट (कालो मथको प्रभुत्व)';
      diagDesc.textContent = `धुवाँ र कालो मुस्लोले रुखका काण्डहरू कालो भएपछि कालो मथहरू छलावरण (Camouflage) मिलेर बाँच्न सफल भएका छन्। पुस्ता ${c9u4MothGen} मा कालो मथको अनुपात ${c9u4BlackPct}% पुगेको छ; यो डार्बिनको 'योग्यतमको निरन्तरता' को ज्वलन्त प्रमाण हो।`;
    }
  }
}

// Mode 3: Genetic Mutation Simulator
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
}

// Exercise Filtering
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

// Tier Filtering
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

// Quiz Data & Engine
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
'''

# Verify no double virama
assert '\u094d\u094d' not in js_code, "Double virama detected in JS!"

js_path = "scratch/c9u4_js.js"
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"Successfully generated {js_path} ({len(js_code)} bytes, {len(js_code.splitlines())} lines).")
