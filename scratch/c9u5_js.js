
// =========================================================================
// GRADE 9 UNIT 5: BODY STRUCTURE & LIFE PROCESS (शारीरिक संरचना र जीवन प्रक्रिया)
// =========================================================================

let activeC9U5Tab = 'concepts';
let activeC9U5LabMode = 'tissues';
let activeC9U5TissueSub = 'plant';
let activeC9U5Tissue = 'xylem';

let activeC9U5NervousSub = 'brain';
let activeC9U5BrainPart = 'cerebrum';
let c9u5ReflexStep = 0;
let c9u5ReflexTimer = null;
let c9u5ReflexAnimating = false;

let activeC9U5EndoSub = 'glucose';
let c9u5GlucoseLevel = 90;
let c9u5GlucoseStatus = 'normal';
let activeC9U5Gland = 'pituitary';
let activeC9U5AuxinDir = 'left';

let c9u5QuizAnswers = {};

// -------------------------------------------------------------------------
// Web Audio Synthesizer (Zero External Dependencies)
// -------------------------------------------------------------------------
let c9u5AudioCtx = null;
function playAudioC9U5(type) {
  try {
    if (!c9u5AudioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) c9u5AudioCtx = new AudioContext();
    }
    if (!c9u5AudioCtx) return;
    if (c9u5AudioCtx.state === 'suspended') {
      c9u5AudioCtx.resume();
    }
    const t = c9u5AudioCtx.currentTime;
    const osc = c9u5AudioCtx.createOscillator();
    const gain = c9u5AudioCtx.createGain();
    osc.connect(gain);
    gain.connect(c9u5AudioCtx.destination);

    if (type === 'click') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, t);
      osc.frequency.exponentialRampToValueAtTime(800, t + 0.05);
      gain.gain.setValueAtTime(0.12, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.06);
      osc.start(t);
      osc.stop(t + 0.06);
    } else if (type === 'impulse') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(880, t);
      osc.frequency.exponentialRampToValueAtTime(220, t + 0.15);
      gain.gain.setValueAtTime(0.18, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.16);
      osc.start(t);
      osc.stop(t + 0.16);
    } else if (type === 'hormone') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(320, t);
      osc.frequency.exponentialRampToValueAtTime(540, t + 0.2);
      gain.gain.setValueAtTime(0.15, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.22);
      osc.start(t);
      osc.stop(t + 0.22);
    } else if (type === 'correct') {
      [523.25, 659.25, 783.99, 1046.5].forEach((freq, idx) => {
        const o = c9u5AudioCtx.createOscillator();
        const g = c9u5AudioCtx.createGain();
        o.connect(g);
        g.connect(c9u5AudioCtx.destination);
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
      osc.frequency.setValueAtTime(140, t + 0.1);
      gain.gain.setValueAtTime(0.2, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.25);
      osc.start(t);
      osc.stop(t + 0.25);
    } else if (type === 'jerk') {
      osc.type = 'square';
      osc.frequency.setValueAtTime(150, t);
      osc.frequency.exponentialRampToValueAtTime(40, t + 0.2);
      gain.gain.setValueAtTime(0.25, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + 0.22);
      osc.start(t);
      osc.stop(t + 0.22);
    }
  } catch (e) {
    // Silently continue if audio context is blocked
  }
}

// -------------------------------------------------------------------------
// Navigation: 4 Main Tabs
// -------------------------------------------------------------------------
function setTabC9U5(tab) {
  activeC9U5Tab = tab;
  playAudioC9U5('click');
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const view = document.getElementById(`c9u5-view-${t}`);
    const btn = document.getElementById(`c9u5-tab-${t}`);
    if (view) {
      if (t === tab) view.classList.remove('hidden');
      else view.classList.add('hidden');
    }
    if (btn) {
      if (t === tab) {
        btn.className = "px-5 py-2.5 rounded-xl bg-purple-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer";
      } else {
        btn.className = "px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer";
      }
    }
  });

  if (tab === 'concepts') {
    renderCurrentC9U5Lab();
  } else if (tab === 'quiz') {
    renderC9U5Quiz();
  }
}

// -------------------------------------------------------------------------
// Lab Modes Switcher (Mode 1, Mode 2, Mode 3)
// -------------------------------------------------------------------------
function setLabModeC9U5(mode) {
  activeC9U5LabMode = mode;
  playAudioC9U5('click');
  const modes = ['tissues', 'nervous', 'endocrine'];
  modes.forEach(m => {
    const panel = document.getElementById(`c9u5-lab-mode-${m}`);
    const btn = document.getElementById(`c9u5-btn-mode-${m}`);
    if (panel) {
      if (m === mode) panel.classList.remove('hidden');
      else panel.classList.add('hidden');
    }
    if (btn) {
      if (m === mode) {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-black text-xs md:text-sm shadow-md transition cursor-pointer";
      } else {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-slate-800 text-slate-400 hover:text-white font-bold text-xs md:text-sm transition cursor-pointer";
      }
    }
  });
  renderCurrentC9U5Lab();
}

function renderCurrentC9U5Lab() {
  if (activeC9U5LabMode === 'tissues') {
    renderTissueSVGC9U5(activeC9U5Tissue);
    updateTissueInfoC9U5(activeC9U5Tissue);
  } else if (activeC9U5LabMode === 'nervous') {
    if (activeC9U5NervousSub === 'brain') {
      renderBrainSVGC9U5(activeC9U5BrainPart);
      updateBrainInfoC9U5(activeC9U5BrainPart);
    } else {
      renderReflexSVGC9U5(c9u5ReflexStep);
    }
  } else if (activeC9U5LabMode === 'endocrine') {
    if (activeC9U5EndoSub === 'glucose') {
      renderGlucoseSVGC9U5(c9u5GlucoseLevel, c9u5GlucoseStatus);
    } else if (activeC9U5EndoSub === 'glands') {
      renderGlandSVGC9U5(activeC9U5Gland);
      updateGlandInfoC9U5(activeC9U5Gland);
    } else if (activeC9U5EndoSub === 'auxin') {
      renderAuxinSVGC9U5(activeC9U5AuxinDir);
    }
  }
}

// =========================================================================
// MODE 1: MICROSCOPIC TISSUES EXPLORER
// =========================================================================

const C9U5_TISSUES_DATA = {
  // Plant Tissues
  xylem: {
    cat: 'plant',
    eng: 'XYLEM COMPLEX PERMANENT TISSUE',
    nep: 'जाइलम (पानी तथा खनिज परिवहन तन्तु)',
    loc: 'बिरुवाको जरा, काण्ड र पातका भास्कुलर बन्डलको भित्री भाग (Wood) मा।',
    struct: 'चार घटक मिलेर बनेको जटिल तन्तु: भेसल्स (खुला बेलनाकार नली), ट्र्याकिड्स (चुच्चा मृत कोष), जाइलम फाइबर (कडा मृत रेसा) र जाइलम प्यारेन्काइमा (एकमात्र जीवित घटक)।',
    func: 'जराले माटोबाट सोसेको पानी र खनिज लवणहरूलाई काण्ड हुँदै पातहरूसम्म एकतर्फी (माथितर्फ) तीव्र गतिमा परिवहन गर्ने तथा बिरुवालाई यान्त्रिक आड दिने।',
    clinical: 'डिक्सन र जोलीको ट्रान्सपिरेसन पुल (Transpiration pull) र कोहेसन-टेन्सन सिद्धान्तका कारण १०० मिटर अग्ला रुखमा पनि पानी सजिलै टुप्पासम्म उक्लन्छ।'
  },
  phloem: {
    cat: 'plant',
    eng: 'PHLOEM COMPLEX PERMANENT TISSUE',
    nep: 'फ्लोएम (घुलित खाना वितरण तन्तु)',
    loc: 'भास्कुलर बन्डलको बाहिरी भाग (काण्डको बोक्राको मुन्तिर / Bast) मा।',
    struct: 'सिभ ट्युब (Sieve tubes - न्युक्लियस नभएका चालनीजस्ता प्लेट भएका नली), कम्पेनियन सेल (Companion cells - ठूलो न्युक्लियस भएका साथी कोष), फ्लोएम प्यारेन्काइमा र फ्लोएम फाइबर।',
    func: 'पातमा प्रकाश संश्लेषणबाट बनेको घुलित खाद्य पदार्थ (ग्लुकोज/सुक्रोज) लाई जरा, फल र बढ्दो टुप्पाहरूमा दुईतर्फी (Translocation) वितरण गर्ने।',
    clinical: 'सिभ ट्युबमा न्युक्लियस नहुने भएकाले यसको सम्पूर्ण मेटाबोलिक गतिविधि नजिकै रहेको कम्पेनियन सेलको न्युक्लियसले नियन्त्रण गर्दछ।'
  },
  apical: {
    cat: 'plant',
    eng: 'APICAL MERISTEMATIC TISSUE',
    nep: 'शीर्षस्थ मेरिस्टमेटिक तन्तु (वृद्धि तन्तु)',
    loc: 'बिरुवाको जरा र काण्डको सबैभन्दा टुप्पो (Growing tips) मा।',
    struct: 'स-साना, पातलो सेलुलोज भित्ता भएका, घना साइटोप्लाज्म, ठूलो स्पष्ट न्युक्लियस भएका र रसधानी (vacuole) नभएका वा धेरै साना भएका निरन्तर विभाजित कोषहरू।',
    func: 'तीव्र समसूत्री कोष विभाजन (Mitosis) गरी जरा र काण्डको लम्बाइ ठाडो रूपमा बढाउने (Primary Growth)।',
    clinical: 'बिरुवाको टुप्पो काट्दा यो तन्तु नष्ट हुने हुनाले ठाडो उचाइ वृद्धि रोकिन्छ र पार्श्व मुकुलहरू पलाएर बिरुवा झाडीदार बन्दछ।'
  },
  sclerenchyma: {
    cat: 'plant',
    eng: 'SCLERENCHYMA SIMPLE PERMANENT TISSUE',
    nep: 'स्क्लेरेन्काइमा (कडा मृत लिग्निन तन्तु)',
    loc: 'काण्डको हाइपोडर्मिस, भास्कुलर बन्डल वरिपरि तथा फलफूलका कडा बोक्रा र दानामा (उदा. ओखर, नास्पाती)।',
    struct: 'लिग्निन (Lignin) जम्मा भएर अत्यधिक बाक्लो र कडा भित्ता भएका मृत कोषहरू; कोषको भित्री भाग खाली (Empty lumen) हुन्छ र कुनै प्रोटोप्लाज्म हुँदैन।',
    func: 'बिरुवालाई अत्यधिक यान्त्रिक शक्ति, कडापन, कठोरता र बाह्य भौतिक चाप सहन सक्ने क्षमता प्रदान गर्ने।',
    clinical: 'ओखरको कडा खोल, नरिवलको जटा र नास्पाती खाँदा जिब्रोमा आउने कडा कणहरू (Stone cells / Sclereids) स्क्लेरेन्काइमा हुन्।'
  },
  collenchyma: {
    cat: 'plant',
    eng: 'COLLENCHYMA SIMPLE PERMANENT TISSUE',
    nep: 'कोलेन्काइमा (लचिलो पेक्टिन तन्तु)',
    loc: 'द्विदलीय बिरुवाको डाँठको बोक्रा (एपिडर्मिस) मुनि र पातको डाँठ (Petiole) मा।',
    struct: 'जीवित लाम्चा कोषहरू जसको कुना-कुनामा पेक्टिन र सेलुलोज जम्मा भई बाक्लो बनेको हुन्छ। अन्तरकोषीय खाली ठाउँ हुँदैन।',
    func: 'बिरुवाका कलिला हाँगा र पातहरूलाई लचिलोपन (Flexibility) दिई हावाहुरी चल्दा नभाँचिने गरी यान्त्रिक सहारा दिने।',
    clinical: 'बलियो हावाहुरी चल्दा रुखका हाँगाहरू लचक्क नुहिन्छन् तर भाँचिँदैनन्, यसको श्रेय कोलेन्काइमा तन्तुको लचिलोपनलाई जान्छ।'
  },

  // Animal Tissues
  neuron: {
    cat: 'animal',
    eng: 'NEURON (NERVOUS TISSUE)',
    nep: 'न्युरोन (स्नायु कोष र आवेग चालक)',
    loc: 'मस्तिष्क (Brain), मेरुदण्ड (सुषुम्ना) र शरीरभरि फैलिएका स्नायु जालोहरूमा।',
    struct: 'तीन मुख्य भाग: साइटोन (न्युक्लियस र निस्ल ग्रेन्युल्स भएको सेल बडी), डेन्ड्राइट्स (शाखायुक्त संवेदी रेसा), र एक्सोन (लामो माइलिन सिथ र नोड्स अफ रानभिएरले बेरिएको रेसा)।',
    func: 'विद्युतीय तथा रासायनिक तरङ्ग (Electrochemical impulses) को रूपमा शरीरभरि तीव्र गतिमा सन्देशहरू आदानप्रदान गर्ने।',
    clinical: 'न्युरोनहरू जन्मपछि कहिल्यै विभाजित हुन सक्दैनन् किनकि यिनीहरूमा सेन्ट्रोजोम निष्क्रिय हुन्छ। त्यसैले मस्तिष्कमा चोट लाग्दा स्नायु पक्षाघात हुन सक्छ।'
  },
  striated: {
    cat: 'animal',
    eng: 'STRIATED / SKELETAL MUSCLE TISSUE',
    nep: 'कङ्काल मांसपेशी (ऐच्छिक रेखादार मांसल तन्तु)',
    loc: 'हाडहरूसँग जोडिएका मांसपेशीहरू (उदा. हात, खुट्टा, जिब्रो, पाखुराका बाइसेप्स र ट्राइसेप्स)।',
    struct: 'लामा, बेलनाकार, नशाखिएका, धेरैवटा न्युक्लियस (Multinucleate) भएका र एकापसपछि अर्को गाढा र फिक्का धर्साहरू (Striations) देखिने रेसाहरू।',
    func: 'मानिसको इच्छा अनुसार खुम्चने र फैलिने (ऐच्छिक चाल); शरीरलाई हिँड्न, उफ्रन, भारी उचाल्न मद्दत गर्ने। निरन्तर काम गर्दा छिट्टै थकित हुन्छ।',
    clinical: 'अत्यधिक कडा व्यायाम गर्दा अक्सिजनको अभावमा यी मांसपेशीहरूमा ल्याक्टिक एसिड जम्मा भई मांशपेशी बाउँडिने र गल्ने (Fatigue) हुन्छ।'
  },
  smooth: {
    cat: 'animal',
    eng: 'SMOOTH / UNSTRIATED MUSCLE TISSUE',
    nep: 'चिल्लो मांसपेशी (अनैच्छिक मांसल तन्तु)',
    loc: 'आन्तरिक अङ्गहरूको भित्ता (उदा. आमाशय, आन्द्रा, रक्तनली, पिसाबथैली, गर्भाशय)।',
    struct: 'दुवै छेउ चुच्चो भएको स्पिन्डल आकारको (Spindle-shaped), एउटा मात्र केन्द्रीय न्युक्लियस भएको र कुनै धर्सा नभएको।',
    func: 'स्वतः निरन्तर मन्द गतिमा खुम्चने (अनैच्छिक चाल, उदा. पेरिस्टाल्सिस चालले खाना आन्द्रामा धकेल्ने)। कहिल्यै छिट्टै थकित हुँदैन।',
    clinical: 'आन्द्रामा खाना सर्ने पेरिस्टाल्टिक चाल र रक्तचाप नियन्त्रण गर्ने रक्तनलीको खुम्चाइ चिल्लो मांसपेशीले गर्दछ।'
  },
  cardiac: {
    cat: 'animal',
    eng: 'CARDIAC MUSCLE TISSUE',
    nep: 'कार्डियाक मांसपेशी (मुटुको मांसल तन्तु)',
    loc: 'मुटुको मायोकार्डियम (Heart wall) मा मात्र पाइन्छ।',
    struct: 'बेलनाकार, शाखायुक्त (Branched), १ वा २ न्युक्लियस भएका, हल्का धर्साहरू भएका र विशेष इन्टरक्यालेटेड डिस्क (Intercalated discs) भएका रेसाहरू।',
    func: 'जीवनभर निरन्तर तालबद्ध रूपमा (Rhythmic contraction & relaxation) नथाकीकन रगत पम्प गर्ने।',
    clinical: 'इन्टरक्यालेटेड डिस्कले गर्दा मुटुको एउटा कोषको विद्युत संवेग सम्पूर्ण मुटुभर तुरुन्तै फैलिन्छ।'
  },
  blood: {
    cat: 'animal',
    eng: 'BLOOD FLUID CONNECTIVE TISSUE',
    nep: 'रक्त तन्तु (तरल संयोजी तन्तु)',
    loc: 'हृदय र सम्पूर्ण शरीरका रक्तनलीहरू (धमनी, शिरा, केशिका) भित्र।',
    struct: '५५% तरल म्याट्रिक्स (प्लाज्मा) + ४५% रक्तकोषहरू: आरबिसी (RBC - रातो, बाइकन्केभ, न्युक्लियसविहीन), डब्लुबिसि (WBC - रोग प्रतिरोधी, न्युक्लियसयुक्त), प्लेटलेट्स (रक्तबिम्ब - रगत जमाउने)।',
    func: 'अक्सिजन र कार्बनडाइअक्साइड परिवहन, पोषक तत्व र हर्मोन वितरण, शरीरको तापक्रम नियमन र इम्युनिटी प्रदान गर्ने।',
    clinical: 'आरबिसीको आयु करिब १२० दिन हुन्छ; हेमोग्लोबिनको कमीले रक्तअल्पता (Anemia) रोग लाग्छ।'
  }
};

function setTissueSubModeC9U5(sub) {
  activeC9U5TissueSub = sub;
  playAudioC9U5('click');
  const btnP = document.getElementById('c9u5-tsub-plant');
  const btnA = document.getElementById('c9u5-tsub-animal');
  const btnsPlantWrap = document.getElementById('c9u5-tissue-btns-plant');
  const btnsAnimWrap = document.getElementById('c9u5-tissue-btns-animal');

  if (sub === 'plant') {
    if (btnP) btnP.className = "px-3.5 py-1.5 rounded-xl bg-emerald-600/30 border border-emerald-500 text-emerald-300 font-bold transition text-xs cursor-pointer";
    if (btnA) btnA.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (btnsPlantWrap) btnsPlantWrap.classList.remove('hidden');
    if (btnsAnimWrap) btnsAnimWrap.classList.add('hidden');
    selectTissueC9U5('xylem');
  } else {
    if (btnP) btnP.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (btnA) btnA.className = "px-3.5 py-1.5 rounded-xl bg-purple-600/30 border border-purple-500 text-purple-300 font-bold transition text-xs cursor-pointer";
    if (btnsPlantWrap) btnsPlantWrap.classList.add('hidden');
    if (btnsAnimWrap) btnsAnimWrap.classList.remove('hidden');
    selectTissueC9U5('neuron');
  }
}

function selectTissueC9U5(tissueKey) {
  activeC9U5Tissue = tissueKey;
  playAudioC9U5('click');
  const allTissues = ['xylem', 'phloem', 'apical', 'sclerenchyma', 'collenchyma', 'neuron', 'striated', 'smooth', 'cardiac', 'blood'];
  allTissues.forEach(t => {
    const btn = document.getElementById(`c9u5-tbtn-${t}`);
    if (btn) {
      if (t === tissueKey) {
        btn.className = "p-3 rounded-2xl border bg-purple-600/30 border-purple-500 text-purple-300 text-left transition cursor-pointer";
      } else {
        btn.className = "p-3 rounded-2xl border bg-slate-950 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer";
      }
    }
  });

  updateTissueInfoC9U5(tissueKey);
  renderTissueSVGC9U5(tissueKey);
}

function updateTissueInfoC9U5(key) {
  const d = C9U5_TISSUES_DATA[key];
  if (!d) return;
  const eng = document.getElementById('c9u5-t-engname');
  const nep = document.getElementById('c9u5-t-nepname');
  const loc = document.getElementById('c9u5-t-loc');
  const struct = document.getElementById('c9u5-t-struct');
  const func = document.getElementById('c9u5-t-func');
  const clinical = document.getElementById('c9u5-t-clinical');

  if (eng) eng.textContent = d.eng;
  if (nep) nep.textContent = d.nep;
  if (loc) loc.textContent = d.loc;
  if (struct) struct.textContent = d.struct;
  if (func) func.textContent = d.func;
  if (clinical) clinical.textContent = d.clinical;
}

function renderTissueSVGC9U5(key) {
  const wrap = document.getElementById('c9u5-tissue-svg-wrap');
  if (!wrap) return;

  let innerSvg = '';

  if (key === 'xylem') {
    innerSvg = `
      <g>
        <!-- Circular microscope backdrop -->
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        <circle cx="160" cy="140" r="116" fill="none" stroke="#6366f1" stroke-dasharray="4,4" opacity="0.3"/>
        
        <!-- Large Xylem Vessels (Tube & Spiral Rings) -->
        <g stroke="#38bdf8" stroke-width="2.5" fill="#0284c7" fill-opacity="0.15">
          <ellipse cx="120" cy="110" rx="35" ry="40" />
          <ellipse cx="120" cy="110" rx="27" ry="32" stroke="#60a5fa" stroke-dasharray="6,4" fill="none" />
          
          <ellipse cx="185" cy="145" rx="42" ry="48" />
          <ellipse cx="185" cy="145" rx="34" ry="40" stroke="#60a5fa" stroke-dasharray="8,5" fill="none" />
          
          <ellipse cx="125" cy="180" rx="26" ry="28" />
        </g>
        
        <!-- Tracheids with Tapered overlapping pits -->
        <g fill="#1e293b" stroke="#0ea5e9" stroke-width="1.8">
          <polygon points="75,80 90,110 80,160 65,130" opacity="0.8"/>
          <polygon points="190,75 220,105 210,140 180,100" opacity="0.8"/>
          <polygon points="215,130 240,160 230,195 205,170" opacity="0.8"/>
        </g>
        
        <!-- Pits / Pores -->
        <circle cx="115" cy="100" r="3" fill="#38bdf8" opacity="0.7"/>
        <circle cx="125" cy="120" r="2.5" fill="#38bdf8" opacity="0.7"/>
        <circle cx="175" cy="135" r="3.5" fill="#38bdf8" opacity="0.7"/>
        <circle cx="195" cy="155" r="3.5" fill="#38bdf8" opacity="0.7"/>
        
        <!-- Living Parenchyma cells around with nucleus -->
        <g fill="#064e3b" stroke="#10b981" stroke-width="1.5">
          <circle cx="85" cy="175" r="14" />
          <circle cx="85" cy="175" r="3.5" fill="#34d399"/>
          <circle cx="160" cy="80" r="12" />
          <circle cx="160" cy="80" r="3" fill="#34d399"/>
          <circle cx="215" cy="80" r="11" />
          <circle cx="215" cy="80" r="2.8" fill="#34d399"/>
        </g>
        
        <!-- Upward Water Flow Arrows -->
        <path d="M120,135 L120,85" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" marker-end="url(#c9u5-arrow-up)" />
        <path d="M185,175 L185,115" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round" />
        <polygon points="185,110 181,118 189,118" fill="#38bdf8"/>
        <polygon points="120,80 116,88 124,88" fill="#38bdf8"/>
        
        <!-- Labels -->
        <text x="185" y="148" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Vessel</text>
        <text x="80" y="125" fill="#bae6fd" font-size="8" text-anchor="middle">Tracheid</text>
        <text x="160" y="245" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">पानी/खनिजको उध्र्व प्रवाह (एकतर्फी)</text>
      </g>
    `;
  } else if (key === 'phloem') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Longitudinal Sieve Tube Column -->
        <rect x="110" y="45" width="55" height="190" rx="6" fill="#064e3b" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
        
        <!-- Sieve Plates with pores -->
        <line x1="110" y1="105" x2="165" y2="105" stroke="#34d399" stroke-width="3.5" stroke-dasharray="4,4"/>
        <line x1="110" y1="175" x2="165" y2="175" stroke="#34d399" stroke-width="3.5" stroke-dasharray="4,4"/>
        
        <!-- Solute streaming bidirectional arrows -->
        <path d="M132,65 L132,150" stroke="#facc15" stroke-width="2" stroke-linecap="round"/>
        <polygon points="132,155 128,147 136,147" fill="#facc15"/>
        <path d="M145,215 L145,130" stroke="#facc15" stroke-width="2" stroke-linecap="round"/>
        <polygon points="145,125 141,133 149,133" fill="#facc15"/>
        
        <!-- Companion Cells on both sides with big prominent nucleus -->
        <!-- Left Companion Cell -->
        <rect x="75" y="60" width="30" height="75" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <circle cx="90" cy="97" r="7" fill="#c084fc"/>
        <circle cx="90" cy="97" r="2.5" fill="#ffffff"/>
        
        <rect x="75" y="145" width="30" height="75" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <circle cx="90" cy="182" r="7" fill="#c084fc"/>
        <circle cx="90" cy="182" r="2.5" fill="#ffffff"/>

        <!-- Right Companion Cell -->
        <rect x="170" y="85" width="30" height="90" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <circle cx="185" cy="130" r="8" fill="#c084fc"/>
        <circle cx="185" cy="130" r="3" fill="#ffffff"/>

        <!-- Plasmodesmata channels -->
        <line x1="105" y1="95" x2="110" y2="95" stroke="#a78bfa" stroke-width="3"/>
        <line x1="165" y1="130" x2="170" y2="130" stroke="#a78bfa" stroke-width="3"/>

        <!-- Labels -->
        <text x="137" y="100" fill="#a7f3d0" font-size="8" font-weight="bold" text-anchor="middle">सिभ प्लेट (छान्ने)</text>
        <text x="90" y="52" fill="#c084fc" font-size="8" font-weight="bold" text-anchor="middle">Companion Cell</text>
        <text x="137" y="228" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">घुलित सुक्रोज (दुईतर्फी प्रवाह)</text>
      </g>
    `;
  } else if (key === 'apical') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Root Tip / Shoot Apex Dome Outline -->
        <path d="M90,220 C90,120 120,60 160,50 C200,60 230,120 230,220 Z" fill="#042f2e" stroke="#14b8a6" stroke-width="2"/>
        
        <!-- Apical Dome Zone of Active Mitotic Division -->
        <g fill="#0f766e" stroke="#2dd4bf" stroke-width="1.2">
          <!-- Small tightly packed hexagonal cells with large nuclei -->
          <rect x="145" y="65" width="12" height="12" rx="2"/><circle cx="151" cy="71" r="3" fill="#f43f5e"/>
          <rect x="160" y="65" width="12" height="12" rx="2"/><circle cx="166" cy="71" r="3" fill="#f43f5e"/>
          <rect x="138" y="80" width="13" height="13" rx="2"/><circle cx="144" cy="86" r="3.5" fill="#f43f5e"/>
          <rect x="154" y="80" width="13" height="13" rx="2"/><circle cx="160" cy="86" r="3.5" fill="#f43f5e"/>
          <rect x="170" y="80" width="13" height="13" rx="2"/><circle cx="176" cy="86" r="3.5" fill="#f43f5e"/>
          
          <!-- Metaphase spindle visualization in a cell -->
          <rect x="145" y="96" width="15" height="15" rx="2" fill="#134e4a"/>
          <line x1="147" y1="103" x2="158" y2="103" stroke="#facc15" stroke-width="2"/>
          <circle cx="152" cy="103" r="1.5" fill="#ffffff"/>

          <rect x="163" y="96" width="14" height="14" rx="2"/><circle cx="170" cy="103" r="3.5" fill="#f43f5e"/>
          <rect x="130" y="114" width="16" height="16" rx="2"/><circle cx="138" cy="122" r="4" fill="#f43f5e"/>
          <rect x="150" y="114" width="18" height="18" rx="2"/><circle cx="159" cy="123" r="4.5" fill="#f43f5e"/>
          <rect x="172" y="114" width="16" height="16" rx="2"/><circle cx="180" cy="122" r="4" fill="#f43f5e"/>
        </g>
        
        <!-- Zone of Elongation below -->
        <g fill="#042f2e" stroke="#0d9488" stroke-width="1.2">
          <rect x="125" y="138" width="20" height="35" rx="3"/><circle cx="135" cy="155" r="4" fill="#f43f5e"/>
          <rect x="150" y="138" width="20" height="35" rx="3"/><circle cx="160" cy="155" r="4" fill="#f43f5e"/>
          <rect x="175" y="138" width="20" height="35" rx="3"/><circle cx="185" cy="155" r="4" fill="#f43f5e"/>
        </g>
        
        <!-- Growth vector arrow -->
        <path d="M160,40 L160,20" stroke="#2dd4bf" stroke-width="2.5"/>
        <polygon points="160,15 155,25 165,25" fill="#2dd4bf"/>
        
        <text x="160" y="10" fill="#2dd4bf" font-size="9" font-weight="bold" text-anchor="middle">लम्बाइ वृद्धि (Mitosis)</text>
        <text x="160" y="245" fill="#99f6e4" font-size="9" text-anchor="middle">शीर्षस्थ मेरिस्टमेटिक कोषहरू</text>
      </g>
    `;
  } else if (key === 'sclerenchyma') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Thick polygonal sclerenchyma cells with heavy lignin and narrow lumen -->
        <g stroke="#d97706" stroke-width="6" fill="#451a03">
          <!-- Hexagon 1 Central -->
          <polygon points="160,105 185,120 185,150 160,165 135,150 135,120" />
          <!-- Hexagon 2 Top Left -->
          <polygon points="135,75 160,90 160,105 135,120 110,105 110,75" />
          <!-- Hexagon 3 Top Right -->
          <polygon points="185,75 210,90 210,120 185,135 160,120 160,90" />
          <!-- Hexagon 4 Bottom Left -->
          <polygon points="135,150 160,165 160,195 135,210 110,195 110,165" />
          <!-- Hexagon 5 Bottom Right -->
          <polygon points="185,150 210,165 210,195 185,210 160,195 160,165" />
          <!-- Left outer -->
          <polygon points="110,105 135,120 135,150 110,165 85,150 85,120" />
          <!-- Right outer -->
          <polygon points="210,105 235,120 235,150 210,165 185,150 185,120" />
        </g>
        
        <!-- Narrow inner empty lumen (dead interior) -->
        <g fill="#0f172a" stroke="#f59e0b" stroke-width="1.5">
          <circle cx="160" cy="135" r="9"/>
          <circle cx="135" cy="97" r="8"/>
          <circle cx="185" cy="105" r="8"/>
          <circle cx="135" cy="180" r="8"/>
          <circle cx="185" cy="180" r="8"/>
          <circle cx="110" cy="135" r="8"/>
          <circle cx="210" cy="135" r="8"/>
        </g>
        
        <!-- Pits / Canaliculi radiating through lignin -->
        <line x1="151" y1="135" x2="142" y2="135" stroke="#f59e0b" stroke-width="1.5"/>
        <line x1="169" y1="135" x2="178" y2="135" stroke="#f59e0b" stroke-width="1.5"/>
        <line x1="160" y1="126" x2="160" y2="115" stroke="#f59e0b" stroke-width="1.5"/>
        <line x1="160" y1="144" x2="160" y2="155" stroke="#f59e0b" stroke-width="1.5"/>

        <text x="160" y="138" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Lumen</text>
        <text x="160" y="235" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">बाक्लो लिग्निन भित्ता (मृत कोष)</text>
      </g>
    `;
  } else if (key === 'collenchyma') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Living cells with green cytoplasm -->
        <g fill="#14532d" stroke="#22c55e" stroke-width="1.5">
          <!-- Polygonal cells -->
          <polygon points="120,95 155,80 185,100 175,140 140,150 115,130"/>
          <polygon points="185,100 220,90 245,115 235,155 195,160 175,140"/>
          <polygon points="140,150 175,140 195,160 180,200 145,210 120,185"/>
          <polygon points="85,110 120,95 115,130 90,150 70,135"/>
          <polygon points="90,150 115,130 140,150 120,185 95,190"/>
        </g>
        
        <!-- Pectin thick deposits at corners (intercellular corners) -->
        <g fill="#86efac">
          <circle cx="155" cy="80" r="7"/>
          <circle cx="185" cy="100" r="8"/>
          <circle cx="175" cy="140" r="9"/>
          <circle cx="140" cy="150" r="8"/>
          <circle cx="115" cy="130" r="7"/>
          <circle cx="120" cy="95" r="7"/>
          <circle cx="195" cy="160" r="7.5"/>
          <circle cx="180" cy="200" r="7"/>
          <circle cx="145" cy="210" r="7"/>
          <circle cx="120" cy="185" r="7.5"/>
        </g>
        
        <!-- Nucleus in each living collenchyma cell -->
        <circle cx="150" cy="115" r="4.5" fill="#facc15"/>
        <circle cx="210" cy="125" r="4.5" fill="#facc15"/>
        <circle cx="160" cy="175" r="4.5" fill="#facc15"/>
        <circle cx="100" cy="165" r="3.5" fill="#facc15"/>

        <text x="150" y="118" fill="#000" font-size="6" font-weight="bold" text-anchor="middle">N</text>
        <text x="175" y="142" fill="#052e16" font-size="6" font-weight="bold" text-anchor="middle">P</text>
        <text x="160" y="240" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">कुनामा पेक्टिन जम्मा (लचिलो जीवित तन्तु)</text>
      </g>
    `;
  } else if (key === 'neuron') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Star-shaped Cyton / Cell Body -->
        <path d="M75,130 C65,115 50,110 40,115 C52,125 55,135 60,140 C50,148 42,160 45,170 C55,165 65,155 75,150 C70,165 75,185 85,190 C88,175 85,160 90,150 C100,155 110,155 115,145 C115,135 100,135 90,130 C90,115 100,100 95,90 C88,105 82,118 75,130 Z" fill="#312e81" stroke="#818cf8" stroke-width="2"/>
        
        <!-- Cyton Nucleus -->
        <circle cx="78" cy="138" r="8" fill="#c084fc"/>
        <circle cx="78" cy="138" r="3" fill="#ffffff"/>
        
        <!-- Nissl granules -->
        <circle cx="70" cy="130" r="1.5" fill="#a5b4fc"/>
        <circle cx="85" cy="145" r="1.5" fill="#a5b4fc"/>
        <circle cx="72" cy="146" r="1.5" fill="#a5b4fc"/>
        
        <!-- Long Axon extending to right -->
        <line x1="115" y1="142" x2="235" y2="142" stroke="#6366f1" stroke-width="3.5"/>
        
        <!-- Schwann Cells / Myelin Sheaths -->
        <rect x="125" y="132" width="24" height="20" rx="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1.8"/>
        <circle cx="137" cy="136" r="2" fill="#ffffff"/>
        
        <rect x="156" y="132" width="24" height="20" rx="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1.8"/>
        <circle cx="168" cy="136" r="2" fill="#ffffff"/>
        
        <rect x="187" y="132" width="24" height="20" rx="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1.8"/>
        <circle cx="199" cy="136" r="2" fill="#ffffff"/>

        <!-- Nodes of Ranvier gaps -->
        <circle cx="152" cy="142" r="2.5" fill="#f43f5e"/>
        <circle cx="183" cy="142" r="2.5" fill="#f43f5e"/>

        <!-- Axon Terminals with Synaptic Knobs -->
        <path d="M235,142 C245,130 255,125 265,120" stroke="#818cf8" stroke-width="2"/>
        <circle cx="265" cy="120" r="3.5" fill="#38bdf8"/>
        
        <path d="M235,142 C250,142 258,145 268,142" stroke="#818cf8" stroke-width="2"/>
        <circle cx="268" cy="142" r="3.5" fill="#38bdf8"/>
        
        <path d="M235,142 C245,155 255,160 265,168" stroke="#818cf8" stroke-width="2"/>
        <circle cx="265" cy="168" r="3.5" fill="#38bdf8"/>

        <!-- Impulse Flow Arrow -->
        <path d="M95,115 L225,115" stroke="#facc15" stroke-width="2" stroke-dasharray="5,3"/>
        <polygon points="230,115 222,111 222,119" fill="#facc15"/>

        <!-- Labels -->
        <text x="78" y="80" fill="#a78bfa" font-size="8" font-weight="bold" text-anchor="middle">Dendrites & Cyton</text>
        <text x="170" y="172" fill="#38bdf8" font-size="8" text-anchor="middle">Myelin Sheath & Nodes</text>
        <text x="160" y="240" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">विद्युतीय आवेगको तीव्र प्रवाह (Saltatory)</text>
      </g>
    `;
  } else if (key === 'striated') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Striated Muscle Fibers (Parallel cylindrical) -->
        <!-- Fiber 1 -->
        <g stroke="#f43f5e" stroke-width="2">
          <rect x="65" y="70" width="190" height="38" rx="8" fill="#881337" fill-opacity="0.4"/>
          <!-- Striations -->
          <line x1="85" y1="70" x2="85" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="100" y1="70" x2="100" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="115" y1="70" x2="115" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="130" y1="70" x2="130" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="145" y1="70" x2="145" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="160" y1="70" x2="160" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="175" y1="70" x2="175" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="190" y1="70" x2="190" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="205" y1="70" x2="205" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="220" y1="70" x2="220" y2="108" stroke="#fb7185" stroke-width="3"/>
          <line x1="235" y1="70" x2="235" y2="108" stroke="#fb7185" stroke-width="3"/>
          <!-- Peripheral nuclei -->
          <ellipse cx="95" cy="74" rx="7" ry="3.5" fill="#67e8f9"/>
          <ellipse cx="180" cy="104" rx="7" ry="3.5" fill="#67e8f9"/>
        </g>
        
        <!-- Fiber 2 -->
        <g stroke="#f43f5e" stroke-width="2">
          <rect x="65" y="120" width="190" height="38" rx="8" fill="#881337" fill-opacity="0.4"/>
          <!-- Striations -->
          <line x1="85" y1="120" x2="85" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="100" y1="120" x2="100" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="115" y1="120" x2="115" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="130" y1="120" x2="130" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="145" y1="120" x2="145" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="160" y1="120" x2="160" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="175" y1="120" x2="175" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="190" y1="120" x2="190" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="205" y1="120" x2="205" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="220" y1="120" x2="220" y2="158" stroke="#fb7185" stroke-width="3"/>
          <line x1="235" y1="120" x2="235" y2="158" stroke="#fb7185" stroke-width="3"/>
          <!-- Nuclei -->
          <ellipse cx="140" cy="124" rx="7" ry="3.5" fill="#67e8f9"/>
          <ellipse cx="215" cy="154" rx="7" ry="3.5" fill="#67e8f9"/>
        </g>
        
        <!-- Fiber 3 -->
        <g stroke="#f43f5e" stroke-width="2">
          <rect x="65" y="170" width="190" height="38" rx="8" fill="#881337" fill-opacity="0.4"/>
          <!-- Striations -->
          <line x1="85" y1="170" x2="85" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="100" y1="170" x2="100" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="115" y1="170" x2="115" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="130" y1="170" x2="130" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="145" y1="170" x2="145" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="160" y1="170" x2="160" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="175" y1="170" x2="175" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="190" y1="170" x2="190" y2="208" stroke="#fb7185" stroke-width="3"/>
          <line x1="205" y1="170" x2="205" y2="208" stroke="#fb7185" stroke-width="3"/>
          <!-- Nuclei -->
          <ellipse cx="105" cy="204" rx="7" ry="3.5" fill="#67e8f9"/>
          <ellipse cx="170" cy="174" rx="7" ry="3.5" fill="#67e8f9"/>
        </g>

        <text x="160" y="240" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">ऐच्छिक रेखादार रेसा (बहुकेन्द्रकीय)</text>
      </g>
    `;
  } else if (key === 'smooth') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Spindle shaped unstriated muscle cells with single central nucleus -->
        <!-- Cell 1 -->
        <path d="M50,105 Q120,80 190,105 Q120,130 50,105 Z" fill="#9d174d" fill-opacity="0.5" stroke="#f472b6" stroke-width="2"/>
        <ellipse cx="120" cy="105" rx="9" ry="5" fill="#a7f3d0"/>

        <!-- Cell 2 overlapping right -->
        <path d="M130,125 Q200,100 270,125 Q200,150 130,125 Z" fill="#9d174d" fill-opacity="0.5" stroke="#f472b6" stroke-width="2"/>
        <ellipse cx="200" cy="125" rx="9" ry="5" fill="#a7f3d0"/>

        <!-- Cell 3 overlapping bottom -->
        <path d="M60,150 Q130,125 200,150 Q130,175 60,150 Z" fill="#9d174d" fill-opacity="0.5" stroke="#f472b6" stroke-width="2"/>
        <ellipse cx="130" cy="150" rx="9" ry="5" fill="#a7f3d0"/>

        <!-- Cell 4 bottom right -->
        <path d="M120,175 Q190,150 260,175 Q190,200 120,175 Z" fill="#9d174d" fill-opacity="0.5" stroke="#f472b6" stroke-width="2"/>
        <ellipse cx="190" cy="175" rx="9" ry="5" fill="#a7f3d0"/>

        <!-- Cell 5 top center -->
        <path d="M80,75 Q150,55 220,75 Q150,95 80,75 Z" fill="#9d174d" fill-opacity="0.4" stroke="#f472b6" stroke-width="1.8"/>
        <ellipse cx="150" cy="75" rx="8" ry="4.5" fill="#a7f3d0"/>

        <text x="160" y="240" fill="#f472b6" font-size="9" font-weight="bold" text-anchor="middle">अनैच्छिक चिल्लो मांसपेशी (एकल केन्द्रकीय)</text>
      </g>
    `;
  } else if (key === 'cardiac') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Branched Cardiac Muscle Fibers -->
        <!-- Main Upper Trunk -->
        <path d="M60,90 L140,90 L170,75 L260,75 L260,105 L180,105 L150,120 L60,120 Z" fill="#831843" fill-opacity="0.5" stroke="#fb7185" stroke-width="2"/>
        
        <!-- Branch connecting to lower trunk -->
        <path d="M140,90 L180,150 L180,175 L130,120 Z" fill="#831843" fill-opacity="0.5" stroke="#fb7185" stroke-width="1.8"/>
        
        <!-- Main Lower Trunk -->
        <path d="M60,150 L130,150 L160,165 L260,165 L260,195 L150,195 L120,180 L60,180 Z" fill="#831843" fill-opacity="0.5" stroke="#fb7185" stroke-width="2"/>

        <!-- Intercalated Discs (Dark vertical zig-zag junctions) -->
        <g stroke="#ffffff" stroke-width="3">
          <line x1="100" y1="90" x2="100" y2="120"/>
          <line x1="220" y1="75" x2="220" y2="105"/>
          <line x1="95" y1="150" x2="95" y2="180"/>
          <line x1="210" y1="165" x2="210" y2="195"/>
        </g>
        
        <!-- Central Oval Nuclei -->
        <ellipse cx="78" cy="105" rx="7" ry="5" fill="#fef08a"/>
        <ellipse cx="190" cy="90" rx="7" ry="5" fill="#fef08a"/>
        <ellipse cx="78" cy="165" rx="7" ry="5" fill="#fef08a"/>
        <ellipse cx="180" cy="180" rx="7" ry="5" fill="#fef08a"/>

        <!-- Faint Cross Striations -->
        <line x1="115" y1="92" x2="115" y2="118" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2,2"/>
        <line x1="125" y1="92" x2="125" y2="118" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2,2"/>
        <line x1="135" y1="92" x2="135" y2="118" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2,2"/>
        
        <text x="100" y="80" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Intercalated Disc</text>
        <text x="160" y="240" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">मुटुको शाखायुक्त मांसपेशी (अविराम चाल)</text>
      </g>
    `;
  } else if (key === 'blood') {
    innerSvg = `
      <g>
        <circle cx="160" cy="140" r="120" fill="#090d16" stroke="#334155" stroke-width="3"/>
        
        <!-- Blood Plasma Background Glow -->
        <circle cx="160" cy="140" r="115" fill="#450a0a" fill-opacity="0.35"/>
        
        <!-- Red Blood Cells (RBCs) - Biconcave Discs -->
        <g stroke="#991b1b" stroke-width="2">
          <!-- RBC 1 -->
          <circle cx="110" cy="100" r="22" fill="#dc2626"/>
          <circle cx="110" cy="100" r="11" fill="#ef4444" opacity="0.6"/>

          <!-- RBC 2 -->
          <circle cx="170" cy="85" r="20" fill="#dc2626"/>
          <circle cx="170" cy="85" r="10" fill="#ef4444" opacity="0.6"/>

          <!-- RBC 3 side view -->
          <ellipse cx="225" cy="120" rx="20" ry="10" fill="#dc2626"/>
          <ellipse cx="225" cy="120" rx="9" ry="4" fill="#991b1b"/>

          <!-- RBC 4 -->
          <circle cx="120" cy="180" r="21" fill="#dc2626"/>
          <circle cx="120" cy="180" r="10.5" fill="#ef4444" opacity="0.6"/>

          <!-- RBC 5 -->
          <circle cx="210" cy="175" r="19" fill="#dc2626"/>
          <circle cx="210" cy="175" r="9" fill="#ef4444" opacity="0.6"/>
        </g>
        
        <!-- White Blood Cell (WBC) - Multilobed nucleus (Neutrophil) -->
        <g stroke="#93c5fd" stroke-width="2">
          <circle cx="165" cy="140" r="25" fill="#1e3a8a" fill-opacity="0.7"/>
          <!-- Multilobed Nucleus -->
          <circle cx="157" cy="133" r="6" fill="#818cf8"/>
          <circle cx="173" cy="135" r="7" fill="#818cf8"/>
          <circle cx="162" cy="148" r="6.5" fill="#818cf8"/>
          <line x1="157" y1="133" x2="173" y2="135" stroke="#818cf8" stroke-width="2"/>
          <line x1="173" y1="135" x2="162" y2="148" stroke="#818cf8" stroke-width="2"/>
        </g>
        
        <!-- Platelets (Small purple fragments) -->
        <g fill="#c084fc">
          <polygon points="80,140 85,138 88,143 82,145"/>
          <polygon points="195,110 200,108 202,112 197,114"/>
          <polygon points="145,210 150,208 153,212 147,215"/>
        </g>

        <!-- Labels -->
        <text x="110" y="103" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">RBC</text>
        <text x="165" y="142" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">WBC</text>
        <text x="83" y="153" fill="#c084fc" font-size="6" font-weight="bold">Platelet</text>
        <text x="160" y="240" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">तरल संयोजी तन्तु (प्लाज्मा + रक्तकोषहरू)</text>
      </g>
    `;
  }

  wrap.innerHTML = `
    <svg viewBox="0 0 320 270" class="w-full max-w-[320px] h-auto select-none">
      ${innerSvg}
    </svg>
  `;
}

// =========================================================================
// MODE 2: NERVOUS SYSTEM & REFLEX ARC
// =========================================================================

const C9U5_BRAIN_DATA = {
  cerebrum: {
    eng: 'CEREBRUM (PROSENCEPHALON / FOREBRAIN)',
    nep: 'ठुलो मस्तिष्क (प्रमस्तिष्क)',
    loc: 'मस्तिष्कको सबैभन्दा माथिल्लो तथा अगाडिको ठूलो भाग। यसले कुल मस्तिष्कको करिब ८०-८५% भाग ओगट्दछ। बाहिरी तह कोर्टेक्स (Grey matter) र भित्री तह मेडुला (White matter) हुन्छ।',
    func: 'सोच्ने, सम्झने (स्मरणशक्ति), तर्क गर्ने, योजना बनाउने, बोल्ने, सुन्ने, देख्ने तथा ज्ञानेन्द्रियहरूबाट प्राप्त सम्पूर्ण संवेगहरूको विश्लेषण गर्ने चेतना र बुद्धिको सर्वोच्च केन्द्र।',
    injury: 'सेरेब्रममा गम्भीर चोट लाग्दा स्मरणशक्ति गुम्न सक्छ (Amnesia), पक्षाघात हुन सक्छ वा मानिस लामो समयसम्म गहिरो अचेतन अवस्था (Coma) मा पुग्न सक्छ।'
  },
  cerebellum: {
    eng: 'CEREBELLUM (METENCEPHALON / HINDBRAIN)',
    nep: 'सानो मस्तिष्क (अनुमस्तिष्क)',
    loc: 'ठुलो मस्तिष्कको पछाडि र मेडुलाको ठीक माथितिर, खोपडीको पछाडिको तल्लो भाग (Occipital region) मा अवस्थित।',
    func: 'शारीरिक सन्तुलन (Body posture & balance) कायम राख्ने, ऐच्छिक मांसपेशीहरूको आपसी समन्वय मिलाउने (उदा. हिँड्दा, दौडिँदा, साइकल चलाउँदा वा नाच्दा शरीर लड्न नदिने)।',
    injury: 'मादक पदार्थ (अल्कोहल) सेवन गर्दा सेरेबेलम निष्क्रिय भई मानिसको खुट्टा लरखराउँछ र शरीरको सन्तुलन तथा बोलीको तालमेल बिग्रन्छ।'
  },
  medulla: {
    eng: 'MEDULLA OBLONGATA (MYELENCEPHALON)',
    nep: 'मेडुला अब्लङ्गेटा (मस्तिष्क स्तम्भ)',
    loc: 'मस्तिष्कको सबैभन्दा तल्लो भाग जसले मस्तिष्कलाई तल रहेको मेरुदण्ड (सुषुम्ना) सँग जोड्दछ।',
    func: 'जीवन सञ्चालनका लागि अनिवार्य अनैच्छिक क्रियाहरूको नियन्त्रण केन्द्र: मुटुको धड्कन, रक्तचाप, श्वासप्रश्वासको गति, खोक्ने, हाछ्युँ गर्ने, उल्टी गर्ने र खाना निल्ने कार्यको नियन्त्रण।',
    injury: 'मेडुला अब्लङ्गेटामा चोट लाग्दा मुटु र श्वासप्रश्वास तुरुन्तै रोकिने भएकाले मानिसको क्षणभरमै मृत्यु (Instant death) हुन्छ।'
  },
  spinal_cord: {
    eng: 'SPINAL CORD (MEDULLA SPINALIS)',
    nep: 'सुषुम्ना (मेरुदण्ड / स्पाइनल कर्ड)',
    loc: 'मेडुला अब्लङ्गेटाको तल्लो भागबाट सुरु भई ढाडको मेरुदण्डको भित्री नली (Neural canal) भित्र सुरक्षित रहन्छ।',
    func: 'अकाम्य क्रियाहरू (Reflex actions) को मुख्य सञ्चालक तथा नियन्त्रण केन्द्र; शरीरका अङ्गहरूबाट मस्तिष्कसम्म र मस्तिष्कबाट अङ्गहरूसम्म ३१ जोडी स्पाइनल स्नायुमार्फत सन्देश आदानप्रदान गर्ने।',
    injury: 'सुषुम्ना भाँचिएमा वा काटिएमा चोट लागेको भागभन्दा मुनिको सम्पूर्ण शरीर पूर्णतया पक्षाघात (Paralysis) भई संवेदनशीलता र चाल दुवै गुम्दछ।'
  },
  meninges: {
    eng: 'MENINGES & CEREBROSPINAL FLUID (CSF)',
    nep: 'मेनिन्जेज र CSF (मस्तिष्क सुरक्षा झिल्ली)',
    loc: 'खोपडीको हाड र मस्तिष्कको बीचमा रहेका तीन तहका सुरक्षात्मक झिल्लीहरू।',
    func: 'बाहिरबाट भित्र: १. डुराम्याटर (Duramater - कडा बाहिरी झिल्ली), २. एराक्नोइडम्याटर (Arachnoid - माकुराको जालो आकारको), र ३. पायम्याटर (Piamater - रक्तनलीयुक्त भित्री झिल्ली)। यी झिल्लीहरूको बीचमा रहने CSF ले मस्तिष्कलाई बाह्य धक्का र चोटबाट बचाउँछ र ओसिलो राख्छ।',
    injury: 'यी झिल्लीहरूमा ब्याक्टेरिया वा भाइरसको संक्रमण हुँदा तीव्र टाउको दुख्ने, घाँटी कडा हुने र उच्च ज्वरो आउने ज्यानमारा रोग मेनिन्जाइटिस (Meningitis) लाग्दछ।'
  }
};

function setNervousSubModeC9U5(sub) {
  activeC9U5NervousSub = sub;
  playAudioC9U5('click');
  const btnB = document.getElementById('c9u5-nsub-brain');
  const btnR = document.getElementById('c9u5-nsub-reflex');
  const panelB = document.getElementById('c9u5-nervous-panel-brain');
  const panelR = document.getElementById('c9u5-nervous-panel-reflex');

  if (sub === 'brain') {
    if (btnB) btnB.className = "px-3.5 py-1.5 rounded-xl bg-purple-600/30 border border-purple-500 text-purple-300 font-bold transition text-xs cursor-pointer";
    if (btnR) btnR.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (panelB) panelB.classList.remove('hidden');
    if (panelR) panelR.classList.add('hidden');
    selectBrainPartC9U5('cerebrum');
  } else {
    if (btnB) btnB.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
    if (btnR) btnR.className = "px-3.5 py-1.5 rounded-xl bg-purple-600/30 border border-purple-500 text-purple-300 font-bold transition text-xs cursor-pointer";
    if (panelB) panelB.classList.add('hidden');
    if (panelR) panelR.classList.remove('hidden');
    resetReflexC9U5();
  }
}

function selectBrainPartC9U5(partKey) {
  activeC9U5BrainPart = partKey;
  playAudioC9U5('click');
  const parts = ['cerebrum', 'cerebellum', 'medulla', 'spinal_cord', 'meninges'];
  parts.forEach(p => {
    const btn = document.getElementById(`c9u5-bbtn-${p}`);
    if (btn) {
      if (p === partKey) {
        btn.className = "p-3 rounded-2xl border bg-purple-600/30 border-purple-500 text-purple-300 text-left transition cursor-pointer";
      } else {
        btn.className = "p-3 rounded-2xl border bg-slate-950 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer";
      }
    }
  });

  updateBrainInfoC9U5(partKey);
  renderBrainSVGC9U5(partKey);
}

function updateBrainInfoC9U5(key) {
  const d = C9U5_BRAIN_DATA[key];
  if (!d) return;
  const eng = document.getElementById('c9u5-b-engname');
  const nep = document.getElementById('c9u5-b-nepname');
  const loc = document.getElementById('c9u5-b-loc');
  const func = document.getElementById('c9u5-b-func');
  const injury = document.getElementById('c9u5-b-injury');

  if (eng) eng.textContent = d.eng;
  if (nep) nep.textContent = d.nep;
  if (loc) loc.textContent = d.loc;
  if (func) func.textContent = d.func;
  if (injury) injury.textContent = d.injury;
}

function renderBrainSVGC9U5(activePart) {
  const wrap = document.getElementById('c9u5-brain-svg-wrap');
  if (!wrap) return;

  const isCerebrum = activePart === 'cerebrum';
  const isCerebellum = activePart === 'cerebellum';
  const isMedulla = activePart === 'medulla';
  const isSpinal = activePart === 'spinal_cord';
  const isMeninges = activePart === 'meninges';

  const cerebrumFill = isCerebrum ? '#8b5cf6' : '#4338ca';
  const cerebrumStroke = isCerebrum ? '#c084fc' : '#6366f1';
  const cerebrumWidth = isCerebrum ? '3.5' : '1.8';

  const cerebellumFill = isCerebellum ? '#ec4899' : '#9d174d';
  const cerebellumStroke = isCerebellum ? '#f472b6' : '#db2777';
  const cerebellumWidth = isCerebellum ? '3.5' : '1.8';

  const medullaFill = isMedulla ? '#f59e0b' : '#b45309';
  const medullaStroke = isMedulla ? '#fcd34d' : '#d97706';
  const medullaWidth = isMedulla ? '3.5' : '1.8';

  const spinalFill = isSpinal ? '#10b981' : '#047857';
  const spinalStroke = isSpinal ? '#6ee7b7' : '#059669';
  const spinalWidth = isSpinal ? '3.5' : '1.8';

  const meningesStroke = isMeninges ? '#38bdf8' : '#334155';
  const meningesWidth = isMeninges ? '4' : '2';

  wrap.innerHTML = `
    <svg viewBox="0 0 340 270" class="w-full max-w-[340px] h-auto select-none">
      <!-- Outer Skull / Meninges Boundary -->
      <path d="M50,170 C40,110 70,35 170,30 C270,35 295,110 285,180 C275,210 240,225 210,225 L190,260 L150,260 L145,215 C110,215 60,205 50,170 Z" fill="#090d16" stroke="${meningesStroke}" stroke-width="${meningesWidth}" ${isMeninges ? 'stroke-dasharray="6,4"' : ''}/>
      
      ${isMeninges ? '<text x="170" y="22" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">मेनिन्जेज (Dura, Arachnoid, Pia + CSF)</text>' : ''}

      <!-- CEREBRUM (Forebrain with deep gyri & sulci folds) -->
      <g onclick="selectBrainPartC9U5('cerebrum')" class="cursor-pointer">
        <path d="M70,160 C55,120 80,50 170,45 C250,50 280,110 270,165 C250,150 230,155 215,145 C195,140 180,150 160,140 C140,140 120,150 100,145 C85,150 75,155 70,160 Z" fill="${cerebrumFill}" fill-opacity="${isCerebrum ? '0.7' : '0.4'}" stroke="${cerebrumStroke}" stroke-width="${cerebrumWidth}"/>
        
        <!-- Cerebrum internal Gyri / Sulci curves -->
        <path d="M90,120 Q120,80 160,100 T230,85" fill="none" stroke="${cerebrumStroke}" stroke-width="1.8" opacity="0.6"/>
        <path d="M110,140 Q150,110 190,125 T250,120" fill="none" stroke="${cerebrumStroke}" stroke-width="1.8" opacity="0.6"/>
        <path d="M140,65 Q180,85 200,60" fill="none" stroke="${cerebrumStroke}" stroke-width="1.8" opacity="0.6"/>
        
        <text x="170" y="100" fill="#ffffff" font-size="10" font-weight="black" text-anchor="middle">सेरेब्रम (ठुलो मस्तिष्क)</text>
      </g>

      <!-- Corpus Callosum arch -->
      <path d="M125,145 C135,130 175,130 195,145" fill="none" stroke="#e0e7ff" stroke-width="3" stroke-linecap="round"/>

      <!-- CEREBELLUM (Hindbrain cauliflower tree pattern) -->
      <g onclick="selectBrainPartC9U5('cerebellum')" class="cursor-pointer">
        <path d="M75,168 C65,185 85,210 120,210 C140,210 145,190 140,175 C120,165 95,165 75,168 Z" fill="${cerebellumFill}" fill-opacity="${isCerebellum ? '0.8' : '0.45'}" stroke="${cerebellumStroke}" stroke-width="${cerebellumWidth}"/>
        
        <!-- Arbor Vitae Tree pattern -->
        <path d="M110,195 Q105,185 100,175 M110,185 Q118,178 125,174 M100,185 L90,188" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" opacity="0.8"/>
        
        <text x="105" y="200" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">सेरेबेलम</text>
      </g>

      <!-- BRAIN STEM: PONS & MEDULLA OBLONGATA -->
      <g onclick="selectBrainPartC9U5('medulla')" class="cursor-pointer">
        <path d="M145,160 C155,160 175,165 175,180 C175,195 168,215 165,225 L145,225 C145,205 140,180 145,160 Z" fill="${medullaFill}" fill-opacity="${isMedulla ? '0.85' : '0.5'}" stroke="${medullaStroke}" stroke-width="${medullaWidth}"/>
        <text x="175" y="195" fill="#ffffff" font-size="8" font-weight="bold">मेडुला</text>
      </g>

      <!-- SPINAL CORD extending into vertebral canal -->
      <g onclick="selectBrainPartC9U5('spinal_cord')" class="cursor-pointer">
        <rect x="145" y="225" width="20" height="35" rx="3" fill="${spinalFill}" fill-opacity="${isSpinal ? '0.85' : '0.5'}" stroke="${spinalStroke}" stroke-width="${spinalWidth}"/>
        <line x1="155" y1="225" x2="155" y2="260" stroke="#a7f3d0" stroke-width="2" stroke-dasharray="3,3"/>
        <text x="155" y="247" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">सुषुम्ना</text>
      </g>
    </svg>
  `;
}

// -------------------------------------------------------------------------
// Reflex Arc Simulator Animation
// -------------------------------------------------------------------------
function triggerReflexC9U5() {
  if (c9u5ReflexAnimating) return;
  c9u5ReflexAnimating = true;
  c9u5ReflexStep = 1;
  playAudioC9U5('impulse');
  updateReflexUI();

  c9u5ReflexTimer = setInterval(() => {
    c9u5ReflexStep++;
    if (c9u5ReflexStep === 2) playAudioC9U5('impulse');
    if (c9u5ReflexStep === 3) playAudioC9U5('impulse');
    if (c9u5ReflexStep === 4) playAudioC9U5('impulse');
    if (c9u5ReflexStep === 5) {
      playAudioC9U5('jerk');
      clearInterval(c9u5ReflexTimer);
      c9u5ReflexAnimating = false;
    }
    updateReflexUI();
  }, 450);
}

function resetReflexC9U5() {
  if (c9u5ReflexTimer) clearInterval(c9u5ReflexTimer);
  c9u5ReflexAnimating = false;
  c9u5ReflexStep = 0;
  playAudioC9U5('click');
  updateReflexUI();
}

function updateReflexUI() {
  const badge = document.getElementById('c9u5-reflex-step-badge');
  const latency = document.getElementById('c9u5-reflex-latency-badge');
  const desc = document.getElementById('c9u5-reflex-desc');

  const steps = [
    { title: 'अवस्था: सामान्य विश्राम (Resting State)', lat: '~२५ मिलिसेकेन्ड', desc: 'हात विश्राम अवस्थामा छ। तातो वस्तु छुनासाथ छालाका रिसेप्टरहरू उत्तेजित हुनेछन्।' },
    { title: 'चरण १: उत्तेजना तथा संवेदी रिसेप्टर (Receptor)', lat: '५ ms', desc: 'औंलाले तातो भाँडो छुँदा छालाका थर्मोरिसेप्टरहरू उत्तेजित भई विद्युतीय संवेग पैदा भयो।' },
    { title: 'चरण २: संवेदी स्नायु (Sensory / Afferent Neuron)', lat: '१० ms', desc: 'संवेदी न्युरोनमार्फत विद्युतीय संवेग पाखुरा हुँदै मेरुदण्डको सुषुम्ना (Dorsal horn) तर्फ तीव्र गतिमा दौडियो।' },
    { title: 'चरण ३: रिले स्नायु (Spinal Interneuron Relay)', lat: '१५ ms', desc: 'सुषुम्नाको खरानी पदार्थमा रहेको रिले न्युरोनले मस्तिष्कको ढिलाइविना तुरुन्त आपतकालीन आदेश चालक स्नायुमा पठायो।' },
    { title: 'चरण ४: चालक स्नायु (Motor / Efferent Neuron)', lat: '२० ms', desc: 'चालक न्युरोनले पाखुराको बाइसेप्स मांसपेशीलाई तत्काल खुम्चनका लागि संवेग पुर्‍यायो।' },
    { title: 'चरण ५: मांसपेशीको चाल र हात फिर्ता (Effector Jerk)', lat: '२५ ms (सम्पन्न)', desc: 'बाइसेप्स मांसपेशी क्षणभरमै खुम्चिएर हात स्वतः पछाडि हट्यो! यसरी मस्तिष्कले पीडा थाहा पाउनुअघि नै शरीर डढ्नबाट जोगियो।' }
  ];

  const curr = steps[c9u5ReflexStep] || steps[0];
  if (badge) badge.textContent = curr.title;
  if (latency) latency.textContent = `प्रतिक्रिया समय: ${curr.lat}`;
  if (desc) desc.textContent = curr.desc;

  renderReflexSVGC9U5(c9u5ReflexStep);
}

function renderReflexSVGC9U5(step) {
  const wrap = document.getElementById('c9u5-reflex-svg-wrap');
  if (!wrap) return;

  const handOffset = step === 5 ? -25 : 0;
  const flamePulse = step >= 1 ? 'animate-pulse' : '';
  const sensoryPulse = step >= 2 ? '#38bdf8' : '#334155';
  const relayPulse = step >= 3 ? '#a855f7' : '#334155';
  const motorPulse = step >= 4 ? '#ef4444' : '#334155';
  const muscleContract = step === 5 ? '#f43f5e' : '#64748b';

  wrap.innerHTML = `
    <svg viewBox="0 0 460 220" class="w-full max-w-[460px] h-auto select-none">
      <!-- Stimulus: Hot Pan / Flame on left -->
      <g transform="translate(30, 110)">
        <!-- Pan base -->
        <ellipse cx="25" cy="45" rx="22" ry="7" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
        <rect x="5" y="32" width="40" height="13" rx="3" fill="#334155"/>
        <!-- Hot Flame -->
        <path d="M25,32 C15,22 15,10 25,0 C35,10 35,22 25,32 Z" fill="#f97316" class="${flamePulse}"/>
        <path d="M25,30 C20,24 20,16 25,8 C30,16 30,24 25,30 Z" fill="#facc15" class="${flamePulse}"/>
        <text x="25" y="60" fill="#f97316" font-size="8" font-weight="bold" text-anchor="middle">तातो भाँडो (Stimulus)</text>
      </g>

      <!-- Human Arm & Finger Touching Hot Pan -->
      <g transform="translate(${80 + handOffset}, 95)">
        <!-- Forearm -->
        <path d="M30,35 Q70,25 110,30 L110,55 Q70,50 30,48 Z" fill="#78350f" fill-opacity="0.5" stroke="#d97706" stroke-width="2"/>
        
        <!-- Finger Receptor -->
        <path d="M30,35 Q10,35 0,38 Q10,48 30,48 Z" fill="#92400e" stroke="${step >= 1 ? '#f59e0b' : '#78350f'}" stroke-width="${step >= 1 ? '2.5' : '1.5'}"/>
        
        ${step >= 1 ? '<circle cx="5" cy="40" r="4" fill="#f59e0b" class="animate-ping"/>' : ''}

        <!-- Biceps Effector Muscle on Upper Arm -->
        <ellipse cx="90" cy="25" rx="${step === 5 ? '22' : '18'}" ry="${step === 5 ? '16' : '10'}" fill="${muscleContract}" stroke="#fda4af" stroke-width="2"/>
        <text x="90" y="28" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">मांसपेशी</text>
      </g>

      <!-- SPINAL CORD CROSS SECTION (Right side) -->
      <g transform="translate(340, 45)">
        <!-- White Matter border -->
        <ellipse cx="55" cy="65" rx="50" ry="45" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
        
        <!-- Grey Matter Butterfly Pattern -->
        <path d="M35,45 C45,55 45,75 35,85 C50,80 60,80 75,85 C65,75 65,55 75,45 C60,50 50,50 35,45 Z" fill="${relayPulse}" fill-opacity="${step >= 3 ? '0.9' : '0.4'}" stroke="#c084fc" stroke-width="1.8"/>
        
        <!-- Central Canal -->
        <circle cx="55" cy="65" r="3" fill="#ffffff"/>

        <text x="55" y="125" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">सुषुम्ना (Spinal Cord)</text>
      </g>

      <!-- SENSORY NEURON PATHWAY (Blue) -->
      <g>
        <path d="M100,135 Q220,70 345,95" fill="none" stroke="${sensoryPulse}" stroke-width="${step >= 2 ? '3' : '1.5'}" stroke-dasharray="${step >= 2 ? 'none' : '4,4'}"/>
        <!-- Dorsal Root Ganglion -->
        <circle cx="280" cy="98" r="${step >= 2 ? '6' : '4'}" fill="${sensoryPulse}"/>
        ${step === 2 ? '<circle cx="200" cy="110" r="4" fill="#38bdf8" class="animate-ping"/>' : ''}
        <text x="210" y="85" fill="#38bdf8" font-size="8" font-weight="bold">संवेदी स्नायु (Sensory)</text>
      </g>

      <!-- MOTOR NEURON PATHWAY (Red) -->
      <g>
        <path d="M355,125 Q230,170 170,125" fill="none" stroke="${motorPulse}" stroke-width="${step >= 4 ? '3' : '1.5'}" stroke-dasharray="${step >= 4 ? 'none' : '4,4'}"/>
        ${step === 4 ? '<circle cx="240" cy="155" r="4" fill="#ef4444" class="animate-ping"/>' : ''}
        <text x="235" y="175" fill="#ef4444" font-size="8" font-weight="bold">चालक स्नायु (Motor)</text>
      </g>
    </svg>
  `;
}

// =========================================================================
// MODE 3: ENDOCRINE GLANDS & HOMEOSTASIS
// =========================================================================

function setEndoSubModeC9U5(sub) {
  activeC9U5EndoSub = sub;
  playAudioC9U5('click');
  const btnG = document.getElementById('c9u5-esub-glucose');
  const btnM = document.getElementById('c9u5-esub-glands');
  const btnA = document.getElementById('c9u5-esub-auxin');

  const panG = document.getElementById('c9u5-endo-panel-glucose');
  const panM = document.getElementById('c9u5-endo-panel-glands');
  const panA = document.getElementById('c9u5-endo-panel-auxin');

  const allBtns = [btnG, btnM, btnA];
  const allPans = [panG, panM, panA];

  allBtns.forEach(b => {
    if (b) b.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
  });
  allPans.forEach(p => {
    if (p) p.classList.add('hidden');
  });

  if (sub === 'glucose') {
    if (btnG) btnG.className = "px-3.5 py-1.5 rounded-xl bg-purple-600/30 border border-purple-500 text-purple-300 font-bold transition text-xs cursor-pointer";
    if (panG) panG.classList.remove('hidden');
    renderGlucoseSVGC9U5(c9u5GlucoseLevel, c9u5GlucoseStatus);
  } else if (sub === 'glands') {
    if (btnM) btnM.className = "px-3.5 py-1.5 rounded-xl bg-purple-600/30 border border-purple-500 text-purple-300 font-bold transition text-xs cursor-pointer";
    if (panM) panM.classList.remove('hidden');
    selectGlandC9U5('pituitary');
  } else if (sub === 'auxin') {
    if (btnA) btnA.className = "px-3.5 py-1.5 rounded-xl bg-purple-600/30 border border-purple-500 text-purple-300 font-bold transition text-xs cursor-pointer";
    if (panA) panA.classList.remove('hidden');
    setAuxinLightC9U5('left');
  }
}

// -------------------------------------------------------------------------
// Blood Glucose Feedback Loop
// -------------------------------------------------------------------------
function triggerGlucoseEventC9U5(event) {
  playAudioC9U5('hormone');
  const badge = document.getElementById('c9u5-glucose-level-badge');
  const ins = document.getElementById('c9u5-insulin-status');
  const glu = document.getElementById('c9u5-glucagon-status');
  const title = document.getElementById('c9u5-glucose-diag-title');
  const desc = document.getElementById('c9u5-glucose-diag-desc');

  if (event === 'meal') {
    c9u5GlucoseLevel = 150;
    c9u5GlucoseStatus = 'high';
    if (badge) {
      badge.textContent = '१५० mg/dL (उच्च ग्लुकोज)';
      badge.className = "text-sm font-mono font-black px-3 py-1 rounded-xl bg-amber-500/20 text-amber-300 border border-amber-500/40";
    }
    if (ins) ins.innerHTML = '<strong class="text-emerald-400">अत्यधिक सक्रिय!</strong> बिटा कोषहरूले तुरुन्त इन्सुलिन निकाली बढी ग्लुकोजलाई कलेजोमा ग्लाइकोजेन बनाउँदैछन्।';
    if (glu) glu.innerHTML = '<strong class="text-slate-400">निष्क्रिय</strong> (ग्लुकागन स्राव रोकियो)।';
    if (title) title.textContent = 'प्रतिक्रिया: इन्सुलिन रिलिज भई सन्तुलनतर्फ';
    if (desc) desc.textContent = 'खानाबाट कार्बोहाइड्रेट पचेर ग्लुकोज रगतमा बढ्यो। इन्सुलिनको कामले यो चाँडै पुनः सामान्य (९० mg/dL) मा झर्नेछ।';
  } else if (event === 'fast') {
    c9u5GlucoseLevel = 65;
    c9u5GlucoseStatus = 'low';
    if (badge) {
      badge.textContent = '६५ mg/dL (न्यून ग्लुकोज)';
      badge.className = "text-sm font-mono font-black px-3 py-1 rounded-xl bg-sky-500/20 text-sky-300 border border-sky-500/40";
    }
    if (ins) ins.innerHTML = '<strong class="text-slate-400">निष्क्रिय</strong> (इन्सुलिन स्राव रोकियो)।';
    if (glu) glu.innerHTML = '<strong class="text-amber-400">अत्यधिक सक्रिय!</strong> अल्फा कोषहरूले ग्लुकागन निकाली कलेजोको सञ्चित ग्लाइकोजेनलाई ग्लुकोजमा तोड्दैछन्।';
    if (title) title.textContent = 'प्रतिक्रिया: ग्लुकागन रिलिज भई ग्लुकोज वृद्धि';
    if (desc) desc.textContent = 'उपवास वा कडा व्यायामले गर्दा रगतमा ग्लुकोज घट्यो। ग्लुकागनले कलेजोबाट ग्लुकोज रगतमा पठाई सामान्य बनाउँछ।';
  } else if (event === 'diabetic') {
    c9u5GlucoseLevel = 240;
    c9u5GlucoseStatus = 'diabetic';
    playAudioC9U5('wrong');
    if (badge) {
      badge.textContent = '२४० mg/dL (खतरनाक उच्च - मधुमेह)';
      badge.className = "text-sm font-mono font-black px-3 py-1 rounded-xl bg-rose-500/20 text-rose-300 border border-rose-500/40 animate-pulse";
    }
    if (ins) ins.innerHTML = '<strong class="text-rose-400">पूर्ण अभाव / अप्रभावकारी!</strong> प्यान्क्रियाजको बिटा कोष नष्ट वा इन्सुलिन रेसिस्टेन्स।';
    if (glu) glu.innerHTML = 'अन्तर्स्राव असन्तुलित।';
    if (title) title.textContent = 'क्लिनिकल अवस्था: मधुमेह (Diabetes Mellitus)';
    if (desc) desc.textContent = 'इन्सुलिन नभएकाले ग्लुकोज कोषभित्र छिर्न नसकी रगतमा अत्यधिक जम्मा हुन्छ र पिसाबबाट बाहिर खेर जान्छ (Glycosuria)। उपचारका लागि बाहिरी इन्सुलिन सुई अनिवार्य हुन्छ।';
  } else {
    c9u5GlucoseLevel = 90;
    c9u5GlucoseStatus = 'normal';
    if (badge) {
      badge.textContent = '९० mg/dL (सामान्य सन्तुलन)';
      badge.className = "text-sm font-mono font-black px-3 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 border border-emerald-500/40";
    }
    if (ins) ins.textContent = 'रगतमा ग्लुकोज बढ्दा बिटा कोषहरूले इन्सुलिन निकाली ग्लुकोजलाई कलेजोमा ग्लाइकोजेन बनाउँछन्।';
    if (glu) glu.textContent = 'रगतमा ग्लुकोज घट्दा अल्फा कोषहरूले ग्लुकागन निकाली कलेजोको ग्लाइकोजेनलाई ग्लुकोजमा तोड्छन्।';
    if (title) title.textContent = 'सन्तुलनको अवस्था (Homeostasis):';
    if (desc) desc.textContent = 'सामान्य अवस्थामा रगतमा ग्लुकोजको मात्रा ८० देखि १२० mg/dL को बीचमा स्थिर रहन्छ।';
  }

  renderGlucoseSVGC9U5(c9u5GlucoseLevel, c9u5GlucoseStatus);
}

function renderGlucoseSVGC9U5(level, status) {
  const wrap = document.getElementById('c9u5-glucose-svg-wrap');
  if (!wrap) return;

  let gaugeColor = '#10b981';
  let angle = 0; // -90 (40mg/dL) to +90 (300mg/dL)
  if (status === 'low') {
    gaugeColor = '#0ea5e9';
    angle = -45;
  } else if (status === 'high') {
    gaugeColor = '#f59e0b';
    angle = 35;
  } else if (status === 'diabetic') {
    gaugeColor = '#f43f5e';
    angle = 75;
  }

  wrap.innerHTML = `
    <svg viewBox="0 0 360 210" class="w-full max-w-[360px] h-auto select-none">
      <!-- Blood Vessel Background Tube -->
      <path d="M40,105 C100,50 260,50 320,105 C260,160 100,160 40,105 Z" fill="#450a0a" fill-opacity="0.3" stroke="#b91c1c" stroke-width="2"/>
      
      <!-- Flowing Glucose Molecules -->
      <circle cx="80" cy="105" r="4" fill="#fbbf24"/>
      <circle cx="120" cy="85" r="4" fill="#fbbf24"/>
      <circle cx="240" cy="125" r="4" fill="#fbbf24"/>
      <circle cx="280" cy="105" r="4" fill="#fbbf24"/>
      ${status === 'high' || status === 'diabetic' ? `
        <circle cx="100" cy="120" r="4" fill="#fbbf24"/>
        <circle cx="140" cy="115" r="4" fill="#fbbf24"/>
        <circle cx="220" cy="90" r="4" fill="#fbbf24"/>
        <circle cx="260" cy="115" r="4" fill="#fbbf24"/>
      ` : ''}

      <!-- Center Semi-Circular Dial Meter -->
      <g transform="translate(180, 125)">
        <!-- Meter Arc -->
        <path d="M-60,0 A60,60 0 0,1 60,0" fill="none" stroke="#334155" stroke-width="12"/>
        <!-- Safe Normal Range Highlight -->
        <path d="M-25,-54 A60,60 0 0,1 25,-54" fill="none" stroke="#10b981" stroke-width="12"/>
        
        <!-- Dial Needle -->
        <line x1="0" y1="0" x2="0" y2="-52" stroke="${gaugeColor}" stroke-width="3.5" stroke-linecap="round" transform="rotate(${angle})"/>
        <circle cx="0" cy="0" r="7" fill="${gaugeColor}"/>
        <circle cx="0" cy="0" r="2.5" fill="#ffffff"/>

        <!-- Digital Value -->
        <text x="0" y="24" fill="${gaugeColor}" font-size="14" font-weight="black" text-anchor="middle">${level} mg/dL</text>
      </g>

      <!-- Organ 1: Pancreas (Top Left) -->
      <g transform="translate(60, 25)">
        <ellipse cx="25" cy="15" rx="22" ry="12" fill="#713f12" stroke="#eab308" stroke-width="1.8"/>
        <text x="25" y="18" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">प्यान्क्रियाज</text>
      </g>

      <!-- Organ 2: Liver (Top Right) -->
      <g transform="translate(240, 25)">
        <polygon points="10,25 45,5 45,28 15,30" fill="#881337" stroke="#f43f5e" stroke-width="1.8"/>
        <text x="32" y="20" fill="#ffe4e6" font-size="8" font-weight="bold" text-anchor="middle">कलेजो</text>
      </g>

      <!-- Dynamic Feedback Arrow -->
      ${status === 'high' ? `
        <path d="M90,35 Q180,-5 250,30" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="180" y="15" fill="#34d399" font-size="7" font-weight="bold" text-anchor="middle">इन्सुलिन ➔ ग्लाइकोजेन भण्डारण</text>
      ` : ''}
      ${status === 'low' ? `
        <path d="M250,35 Q180,5 90,30" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="180" y="15" fill="#fbbf24" font-size="7" font-weight="bold" text-anchor="middle">ग्लुकागन ➔ ग्लुकोज निष्कासन</text>
      ` : ''}
    </svg>
  `;
}

// -------------------------------------------------------------------------
// Human Endocrine Map
// -------------------------------------------------------------------------
const C9U5_GLANDS_DATA = {
  pituitary: {
    eng: 'PITUITARY GLAND (MASTER GLAND)',
    nep: 'पिट्युटरी ग्रन्थि (मास्टर ग्रन्थि)',
    loc: 'मस्तिष्कको फेदमा हाइपोथालामससँग जोडिएर क्रेनियमको सेला टर्सिका हाडको खाल्डोमा मटरको गेडा आकारको हुन्छ।',
    hormones: 'वृद्धि हर्मोन (GH / Somatotropin), TSH, ACTH, FSH, LH, प्रोल्याक्टिन र अक्सिटोसिन।',
    func: 'शरीरको समग्र शारीरिक वृद्धि, हाडहरूको लम्बाइ विकास तथा अन्य सम्पूर्ण अन्तःस्रावी ग्रन्थिहरूको गतिविधि नियन्त्रण गर्ने।',
    disorders: 'बाल्यकालमा कमी भएमा पुड्कोपन (Dwarfism); बढी भएमा भीमकाय शरीर (Gigantism); वयस्कमा बढी भएमा एक्रोमेगाली (Acromegaly)।'
  },
  thyroid: {
    eng: 'THYROID GLAND',
    nep: 'थाइरोइड ग्रन्थि',
    loc: 'घाँटीको अगाडि श्वासनली (Trachea) को दुवैतिर पुतली आकार (Butterfly-shaped) को हुन्छ।',
    hormones: 'थाइरोक्सिन (Thyroxine / T4) र क्याल्सिटोनिन (Calcitonin)।',
    func: 'शरीरको आधारभूत उपापचयीय दर (BMR), ऊर्जा उत्पादन, कोषीय श्वासप्रश्वास र मानसिक विकासको नियमन गर्ने।',
    disorders: 'आयोडिनको कमीले घाँटी सुन्निने गलगाँड (Goiter); बाल्यकालमा कमी भएमा सुस्त मनस्थिति हुने क्रेटिनिज्म (Cretinism)।'
  },
  parathyroid: {
    eng: 'PARATHYROID GLANDS',
    nep: 'प्याराथाइरोइड ग्रन्थिहरू',
    loc: 'थाइरोइड ग्रन्थिको पछाडिको सतहमा मटरका गेडाजस्ता ४ वटा साना ग्रन्थिहरू हुन्छन्।',
    hormones: 'प्याराथर्मोन (Parathormone / PTH)।',
    func: 'रगतमा क्याल्सियम र फस्फोरसको सन्तुलन कायम राख्ने (हाडबाट क्याल्सियम रगतमा ल्याउने)।',
    disorders: 'यसको कमी भएमा रगतमा क्याल्सियम घटी मांसपेशीहरू तीव्र बाउँडिने टिटानी (Tetany) रोग लाग्दछ।'
  },
  adrenal: {
    eng: 'ADRENAL GLAND (SUPRARENAL GLAND)',
    nep: 'एड्रिनल ग्रन्थि (आपतकालीन ग्रन्थि)',
    loc: 'दुवै मिर्गौला (Kidneys) को माथिल्लो भागमा टोपीजस्तो (Cap-shaped) अवस्थित।',
    hormones: 'एड्रेनालिन (Adrenaline / 3F Hormone) र कोर्टिकोस्टेरोइड्स।',
    func: 'डर, त्रास, रिस, संकट वा आपतकालमा मुटुको धड्कन र रक्तचाप बढाई शरीरलाई सामना गर्न (Fight) वा भाग्न (Flight) तयार गर्ने।',
    disorders: 'कमी भएमा एडिसन्स रोग (Addison’s disease - कमजोरी, छाला कालो हुने); बढी भएमा कसिङ सिन्ड्रोम।'
  },
  pancreas: {
    eng: 'PANCREAS (HETEROCRINE / MIXED GLAND)',
    nep: 'प्यान्क्रियाज (मिश्रित ग्रन्थि)',
    loc: 'आमाशय (Stomach) को मुन्तिर ‘C’ आकारको ड्युओडेनमको बीचमा।',
    hormones: 'इन्सुलिन (Insulin - Beta cells) र ग्लुकागन (Glucagon - Alpha cells)।',
    func: 'रगतमा ग्लुकोजको मात्रा (८०-१२० mg/dL) स्थिर राख्ने; ग्लुकोज र ग्लाइकोजेनको आपसी रूपान्तरण नियन्त्रण गर्ने।',
    disorders: 'इन्सुलिनको कमीले रगतमा चिनी बढी पिसाबबाट जाने विश्वव्यापी रोग मधुमेह (Diabetes Mellitus) लाग्दछ।'
  },
  gonads: {
    eng: 'GONADS (TESTES & OVARIES)',
    nep: 'गोनाड्स (प्रजनन ग्रन्थिहरू)',
    loc: 'पुरुषमा स्क्रोटमभित्र अण्डकोष (Testes) र महिलामा तल्लो पेटको पेल्भिक भागमा डिम्बाशय (Ovaries)।',
    hormones: 'पुरुषमा टेस्टोस्टेरोन (Testosterone); महिलामा एस्ट्रोजेन (Estrogen) र प्रोजेस्टेरोन (Progesterone)।',
    func: 'शुक्राणु र डिम्ब उत्पादन तथा किशोरावस्थामा दोस्रो लैङ्गिक लक्षणहरू (दारीजुँगा, आवाज, स्तन विकास) को विकास।',
    disorders: 'हर्मोनको अभाव भएमा बाँझोपन (Infertility) र यौनिक विकास अवरुद्ध हुन्छ।'
  }
};

function selectGlandC9U5(glandKey) {
  activeC9U5Gland = glandKey;
  playAudioC9U5('click');
  const glands = ['pituitary', 'thyroid', 'parathyroid', 'adrenal', 'pancreas', 'gonads'];
  glands.forEach(g => {
    const btn = document.getElementById(`c9u5-gbtn-${g}`);
    if (btn) {
      if (g === glandKey) {
        btn.className = "p-3 rounded-2xl border bg-purple-600/30 border-purple-500 text-purple-300 text-left transition cursor-pointer";
      } else {
        btn.className = "p-3 rounded-2xl border bg-slate-950 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer";
      }
    }
  });

  updateGlandInfoC9U5(glandKey);
  renderGlandSVGC9U5(glandKey);
}

function updateGlandInfoC9U5(key) {
  const d = C9U5_GLANDS_DATA[key];
  if (!d) return;
  const eng = document.getElementById('c9u5-g-engname');
  const nep = document.getElementById('c9u5-g-nepname');
  const loc = document.getElementById('c9u5-g-loc');
  const horm = document.getElementById('c9u5-g-hormones');
  const func = document.getElementById('c9u5-g-func');
  const dis = document.getElementById('c9u5-g-disorders');

  if (eng) eng.textContent = d.eng;
  if (nep) nep.textContent = d.nep;
  if (loc) loc.textContent = d.loc;
  if (horm) horm.textContent = d.hormones;
  if (func) func.textContent = d.func;
  if (dis) dis.textContent = d.disorders;
}

function renderGlandSVGC9U5(key) {
  const wrap = document.getElementById('c9u5-gland-svg-wrap');
  if (!wrap) return;

  const glandCoords = {
    pituitary: { x: 120, y: 35, name: 'पिट्युटरी (मस्तिष्क)' },
    thyroid: { x: 120, y: 65, name: 'थाइरोइड (घाँटी)' },
    parathyroid: { x: 120, y: 70, name: 'प्याराथाइरोइड' },
    adrenal: { x: 120, y: 135, name: 'एड्रिनल (मिर्गौलामाथि)' },
    pancreas: { x: 120, y: 125, name: 'प्यान्क्रियाज' },
    gonads: { x: 120, y: 165, name: 'गोनाड्स (प्रजनन)' }
  };

  const curr = glandCoords[key] || glandCoords.pituitary;

  wrap.innerHTML = `
    <svg viewBox="0 0 240 260" class="w-full max-w-[240px] h-auto select-none">
      <!-- Human Body Silhouette -->
      <g fill="#1e293b" stroke="#334155" stroke-width="1.8">
        <!-- Head -->
        <circle cx="120" cy="35" r="20"/>
        <!-- Neck -->
        <rect x="114" y="55" width="12" height="15"/>
        <!-- Torso -->
        <path d="M85,70 C85,70 110,65 120,65 C130,65 155,70 155,70 L148,170 L92,170 Z"/>
        <!-- Arms -->
        <path d="M85,70 L65,140 L72,143 L90,85 Z"/>
        <path d="M155,70 L175,140 L168,143 L150,85 Z"/>
        <!-- Legs -->
        <path d="M95,170 L90,250 L104,250 L115,170 Z"/>
        <path d="M145,170 L150,250 L136,250 L125,170 Z"/>
      </g>

      <!-- Gland Marker Pins -->
      <!-- Pituitary -->
      <circle cx="120" cy="35" r="4" fill="${key === 'pituitary' ? '#c084fc' : '#64748b'}"/>
      <!-- Thyroid -->
      <circle cx="120" cy="65" r="5" fill="${key === 'thyroid' ? '#38bdf8' : '#64748b'}"/>
      <!-- Adrenal -->
      <circle cx="112" cy="135" r="4.5" fill="${key === 'adrenal' ? '#f59e0b' : '#64748b'}"/>
      <circle cx="128" cy="135" r="4.5" fill="${key === 'adrenal' ? '#f59e0b' : '#64748b'}"/>
      <!-- Pancreas -->
      <ellipse cx="120" cy="120" rx="9" ry="4" fill="${key === 'pancreas' ? '#10b981' : '#64748b'}"/>
      <!-- Gonads -->
      <circle cx="120" cy="165" r="5" fill="${key === 'gonads' ? '#f43f5e' : '#64748b'}"/>

      <!-- Glowing Active Pin Ring -->
      <circle cx="${curr.x}" cy="${curr.y}" r="11" fill="none" stroke="#a855f7" stroke-width="2.5" class="animate-ping"/>
      <circle cx="${curr.x}" cy="${curr.y}" r="7" fill="#a855f7"/>
      <circle cx="${curr.x}" cy="${curr.y}" r="3" fill="#ffffff"/>

      <!-- Label -->
      <text x="${curr.x}" y="${curr.y - 14}" fill="#f3e8ff" font-size="9" font-weight="black" text-anchor="middle">${curr.name}</text>
    </svg>
  `;
}

// -------------------------------------------------------------------------
// Auxin Phototropism Simulation
// -------------------------------------------------------------------------
function setAuxinLightC9U5(dir) {
  activeC9U5AuxinDir = dir;
  playAudioC9U5('hormone');
  const btnO = document.getElementById('c9u5-abtn-overhead');
  const btnL = document.getElementById('c9u5-abtn-left');
  const btnR = document.getElementById('c9u5-abtn-right');
  const desc = document.getElementById('c9u5-auxin-desc');

  const btns = [btnO, btnL, btnR];
  btns.forEach(b => {
    if (b) b.className = "px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 font-bold transition text-xs cursor-pointer";
  });

  if (dir === 'overhead') {
    if (btnO) btnO.className = "px-3 py-1.5 rounded-xl bg-amber-600/30 border border-amber-500 text-amber-300 font-bold transition text-xs cursor-pointer";
    if (desc) desc.textContent = 'प्रकाश माथिबाट सीधै पर्दा अक्सिन हर्मोन काण्डको दुवैतिर बराबर रूपमा वितरण हुन्छ। फलस्वरूप दुवैतर्फका कोषहरू समान दरमा लाम्चिन्छन् र डाँठ सीधै माथितर्फ बढ्छ।';
  } else if (dir === 'left') {
    if (btnL) btnL.className = "px-3 py-1.5 rounded-xl bg-amber-600/30 border border-amber-500 text-amber-300 font-bold transition text-xs cursor-pointer";
    if (desc) desc.textContent = 'प्रकाश बायाँतर्फबाट आउँदा अक्सिन हर्मोन प्रकाशबाट भागेर छायाँ परेको दायाँ (अँध्यारो) भागमा बसाइँ सर्दछ। दायाँ भागका कोषहरू तीव्र लाम्चिन्छन् र डाँठ बायाँ (प्रकाशतर्फ) बाङ्किन्छ।';
  } else if (dir === 'right') {
    if (btnR) btnR.className = "px-3 py-1.5 rounded-xl bg-amber-600/30 border border-amber-500 text-amber-300 font-bold transition text-xs cursor-pointer";
    if (desc) desc.textContent = 'प्रकाश दायाँतर्फबाट आउँदा अक्सिन हर्मोन छायाँ परेको बायाँ भागमा बसाइँ सर्दछ। बायाँ भागका कोषहरू छिटो लाम्चिएर डाँठ दायाँ (प्रकाशतर्फ) ढल्किन्छ।';
  }

  renderAuxinSVGC9U5(dir);
}

function renderAuxinSVGC9U5(dir) {
  const wrap = document.getElementById('c9u5-auxin-svg-wrap');
  if (!wrap) return;

  let stemPath = '';
  let sunX = 160;
  let sunY = 30;

  if (dir === 'overhead') {
    stemPath = 'M150,210 L150,90 Q150,70 150,60 L170,60 Q170,70 170,90 L170,210 Z';
    sunX = 160;
    sunY = 25;
  } else if (dir === 'left') {
    stemPath = 'M150,210 Q150,130 115,85 L130,75 Q165,125 170,210 Z';
    sunX = 45;
    sunY = 55;
  } else if (dir === 'right') {
    stemPath = 'M150,210 Q150,125 185,75 L200,85 Q165,130 170,210 Z';
    sunX = 275;
    sunY = 55;
  }

  wrap.innerHTML = `
    <svg viewBox="0 0 320 250" class="w-full max-w-[320px] h-auto select-none">
      <!-- Sun Icon with glowing rays -->
      <g transform="translate(${sunX}, ${sunY})">
        <circle cx="0" cy="0" r="14" fill="#facc15" stroke="#f59e0b" stroke-width="2"/>
        <line x1="0" y1="-20" x2="0" y2="-25" stroke="#facc15" stroke-width="2"/>
        <line x1="0" y1="20" x2="0" y2="25" stroke="#facc15" stroke-width="2"/>
        <line x1="-20" y1="0" x2="-25" y2="0" stroke="#facc15" stroke-width="2"/>
        <line x1="20" y1="0" x2="25" y2="0" stroke="#facc15" stroke-width="2"/>
        <text x="0" y="4" fill="#78350f" font-size="7" font-weight="black" text-anchor="middle">सूर्य</text>
      </g>

      <!-- Flower Pot -->
      <g transform="translate(125, 205)">
        <polygon points="5,0 65,0 55,35 15,35" fill="#9a3412" stroke="#ea580c" stroke-width="1.8"/>
        <rect x="0" y="-5" width="70" height="6" rx="2" fill="#c2410c"/>
      </g>

      <!-- Plant Stem bending towards light -->
      <path d="${stemPath}" fill="#15803d" stroke="#4ade80" stroke-width="2"/>

      <!-- Growing Apex Leaf Bud -->
      ${dir === 'overhead' ? `
        <ellipse cx="150" cy="55" rx="10" ry="6" fill="#22c55e"/>
        <ellipse cx="170" cy="55" rx="10" ry="6" fill="#22c55e"/>
      ` : dir === 'left' ? `
        <ellipse cx="115" cy="75" rx="10" ry="6" fill="#22c55e" transform="rotate(-30 115 75)"/>
        <ellipse cx="130" cy="65" rx="10" ry="6" fill="#22c55e" transform="rotate(-30 130 65)"/>
      ` : `
        <ellipse cx="195" cy="75" rx="10" ry="6" fill="#22c55e" transform="rotate(30 195 75)"/>
        <ellipse cx="180" cy="65" rx="10" ry="6" fill="#22c55e" transform="rotate(30 180 65)"/>
      `}

      <!-- Auxin Dots Concentration (Yellow Dots on the shaded side) -->
      ${dir === 'left' ? `
        <!-- High Auxin on Right (Dark Side) -->
        <g fill="#fde047">
          <circle cx="155" cy="110" r="2.5"/><circle cx="160" cy="115" r="2.5"/>
          <circle cx="150" cy="130" r="2.5"/><circle cx="158" cy="135" r="2.5"/>
          <circle cx="145" cy="150" r="2.5"/><circle cx="155" cy="155" r="2.5"/>
        </g>
        <text x="195" y="130" fill="#fde047" font-size="7" font-weight="bold">छायाँमा बढी अक्सिन</text>
      ` : dir === 'right' ? `
        <!-- High Auxin on Left (Dark Side) -->
        <g fill="#fde047">
          <circle cx="155" cy="110" r="2.5"/><circle cx="150" cy="115" r="2.5"/>
          <circle cx="160" cy="130" r="2.5"/><circle cx="152" cy="135" r="2.5"/>
          <circle cx="165" cy="150" r="2.5"/><circle cx="155" cy="155" r="2.5"/>
        </g>
        <text x="125" y="130" fill="#fde047" font-size="7" font-weight="bold" text-anchor="end">छायाँमा बढी अक्सिन</text>
      ` : `
        <g fill="#fde047">
          <circle cx="155" cy="110" r="2.5"/><circle cx="165" cy="110" r="2.5"/>
          <circle cx="155" cy="135" r="2.5"/><circle cx="165" cy="135" r="2.5"/>
        </g>
      `}
    </svg>
  `;
}

// =========================================================================
// TAB 2: EXERCISES FILTERING
// =========================================================================
function filterC9U5Exercises(filter) {
  playAudioC9U5('click');
  const cards = document.querySelectorAll('.c9u5-ex-card');
  cards.forEach(card => {
    const cats = (card.getAttribute('data-cat') || '').split(' ');
    if (filter === 'all' || cats.includes(filter)) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  const filterBtns = ['all', 'tissues', 'nervous', 'endocrine', 'mcq', 'reason', 'diff', 'qa', 'project'];
  filterBtns.forEach(f => {
    const btn = document.getElementById(`c9u5-exbtn-${f}`);
    if (btn) {
      if (f === filter) {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-black transition bg-purple-600 text-white shadow-sm cursor-pointer whitespace-nowrap";
      } else {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap";
      }
    }
  });
}

// =========================================================================
// TAB 3: TIERS FILTERING
// =========================================================================
function filterC9U5Tiers(tier) {
  playAudioC9U5('click');
  const cards = document.querySelectorAll('.c9u5-tier-card');
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
    const btn = document.getElementById(`c9u5-tierbtn-${t}`);
    if (btn) {
      if (t === tier) {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-black transition bg-purple-600 text-white shadow-sm cursor-pointer whitespace-nowrap";
      } else {
        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap";
      }
    }
  });
}

// =========================================================================
// TAB 4: QUIZ ENGINE (10 Comprehensive Questions)
// =========================================================================
const C9U5_QUIZ_DATA = [
  {
    q: "१. निरन्तर समसूत्री विभाजन भई नयाँ कोष उत्पादन गर्ने क्षमता कुन वनस्पति तन्तुमा हुन्छ ?",
    opts: [
      "स्थायी तन्तु (Permanent tissue)",
      "मेरिस्टेमेटिक तन्तु (Meristematic tissue)",
      "स्क्लेरेन्काइमा तन्तु (Sclerenchyma)",
      "जाइलम भेसल्स (Xylem vessels)"
    ],
    ans: 1,
    exp: "मेरिस्टेमेटिक तन्तुका कोषहरूमा तीव्र समसूत्री कोष विभाजन (Mitosis) हुने क्षमता हुन्छ, जसले बिरुवाको उचाइ र मोटाइ बढाउँछ।"
  },
  {
    q: "२. लिग्निन (Lignin) जम्मा भई भित्ता अत्यधिक बाक्लो र कडा बनेका मृत कोषहरूको समूह कुन हो ?",
    opts: [
      "प्यारेन्काइमा (Parenchyma)",
      "कोलेन्काइमा (Collenchyma)",
      "स्क्लेरेन्काइमा (Sclerenchyma)",
      "फ्लोएम सिभ ट्युब (Sieve tube)"
    ],
    ans: 2,
    exp: "स्क्लेरेन्काइमा तन्तुका कोषहरूमा लिग्निन जम्मा भएर भित्ता कडा बनेको हुन्छ र भित्र कुनै जीवद्रव्य नहुने मृत कोषहरू हुन्छन्।"
  },
  {
    q: "३. मुटुको मांसपेशी (Cardiac muscle) मा मात्र पाइने विशेष जोडनी संरचना कुन हो ?",
    opts: [
      "इन्टरक्यालेटेड डिस्क (Intercalated disc)",
      "नोड्स अफ रानभिएर (Nodes of Ranvier)",
      "सिभ प्लेट (Sieve plate)",
      "माइलिन सिथ (Myelin sheath)"
    ],
    ans: 0,
    exp: "इन्टरक्यालेटेड डिस्क कार्डियाक मांसपेशीको अद्वितीय विशेषता हो, जसले विद्युतीय संवेग सम्पूर्ण मुटुमा तुरुन्तै फैलाई तालबद्ध पम्प गराउँछ।"
  },
  {
    q: "४. आन्तरिक अङ्गहरू (उदा. आमाशय, आन्द्रा, रक्तनली) को भित्तामा कुन प्रकारको मांसपेशी पाइन्छ ?",
    opts: [
      "ऐच्छिक कङ्काल मांसपेशी (Striated)",
      "चिल्लो अनैच्छिक मांसपेशी (Smooth muscle)",
      "कार्डियाक मांसपेशी (Cardiac)",
      "रेखायुक्त मांसपेशी"
    ],
    ans: 1,
    exp: "आन्तरिक अङ्गहरूको भित्तामा मानिसको इच्छाविना स्वतः खुम्चने स्पिन्डल आकारको चिल्लो (Smooth / Unstriated) मांसपेशी हुन्छ।"
  },
  {
    q: "५. मानव मस्तिष्कलाई घेर्ने तीन तहका मेनिन्जेजमध्ये सबैभन्दा बाहिरी कडा तह कुन हो ?",
    opts: [
      "पायम्याटर (Piamater)",
      "एराक्नोइडम्याटर (Arachnoidmater)",
      "डुराम्याटर (Duramater)",
      "सेरेब्रल कोर्टेक्स"
    ],
    ans: 2,
    exp: "बाहिरबाट भित्रको सही क्रम: डुराम्याटर (कडा बाहिरी तह) ➔ एराक्नोइडम्याटर (माकुराको जालो आकार) ➔ पायम्याटर (भित्री पातलो तह)।"
  },
  {
    q: "६. शारीरिक सन्तुलन (Posture & Balance) र ऐच्छिक मांसपेशीको समन्वय मस्तिष्कको कुन भागले गर्छ ?",
    opts: [
      "सेरेब्रम (प्रमस्तिष्क)",
      "सेरेबेलम (अनुमस्तिष्क)",
      "मेडुला अब्लङ्गेटा",
      "हाइपोथालामस"
    ],
    ans: 1,
    exp: "सेरेबेलमले शरीरको सन्तुलन कायम राख्दछ र मांसपेशीहरूको तालमेल मिलाउँछ; मदिरा सेवन गर्दा यही भाग निष्क्रिय हुन्छ।"
  },
  {
    q: "७. तातो भाँडो छुँदा मस्तिष्कले थाहा पाउनुअगावै हात पछि हट्ने अकाम्य क्रिया कसले नियन्त्रण गर्छ ?",
    opts: [
      "सुषुम्ना (Spinal Cord)",
      "सेरेब्रम (Cerebrum)",
      "थाइरोइड ग्रन्थि",
      "पिट्युटरी ग्रन्थि"
    ],
    ans: 0,
    exp: "अकाम्य क्रिया (Reflex Action) को मुख्य केन्द्र सुषुम्ना (Spinal cord) हो, जसले आपतकालीन अवस्थामा मस्तिष्कभन्दा अगाडि नै निर्णय लिन्छ।"
  },
  {
    q: "८. अन्य अन्तःस्रावी ग्रन्थिहरूको स्राव नियन्त्रण गर्ने हुनाले 'मास्टर ग्रन्थि' कुन ग्रन्थिलाई भनिन्छ ?",
    opts: [
      "थाइरोइड ग्रन्थि",
      "एड्रिनल ग्रन्थि",
      "पिट्युटरी ग्रन्थि (Pituitary Gland)",
      "प्यान्क्रियाज"
    ],
    ans: 2,
    exp: "पिट्युटरी ग्रन्थिबाट निस्कने ट्रपिक हर्मोनहरूले शरीरका अन्य धेरै ग्रन्थिहरूको गतिविधि निर्देशन गर्ने भएकाले यसलाई मास्टर ग्रन्थि भनिन्छ।"
  },
  {
    q: "९. रगतमा ग्लुकोजको मात्रा घट्दा प्यान्क्रियाजको अल्फा कोषबाट कुन हर्मोन निस्कन्छ ?",
    opts: [
      "इन्सुलिन (Insulin)",
      "ग्लुकागन (Glucagon)",
      "थाइरोक्सिन (Thyroxine)",
      "एड्रेनालिन (Adrenaline)"
    ],
    ans: 1,
    exp: "ग्लुकागनले कलेजोमा सञ्चित ग्लाइकोजेनलाई ग्लुकोजमा तोडेर रगतमा ग्लुकोज बढाउँछ; इन्सुलिनले भने ग्लुकोज घटाउने काम गर्छ।"
  },
  {
    q: "१०. बोटबिरुवामा फलफूल प्राकृतिक रूपमा छिट्टै पकाउन मद्दत गर्ने एकमात्र ग्यासयुक्त हर्मोन कुन हो ?",
    opts: [
      "अक्सिन (Auxin)",
      "जिबरेलिन (Gibberellin)",
      "इथाइलिन (Ethylene)",
      "साइटोकाइनिन (Cytokinin)"
    ],
    ans: 2,
    exp: "इथाइलिन ग्यासको रूपमा पाइने एकमात्र प्राकृतिक वनस्पति हर्मोन हो, जसले फल पकाउने र बुढो बनाउने कार्य गर्दछ।"
  }
];

function renderC9U5Quiz() {
  const container = document.getElementById('c9u5-quiz-container');
  if (!container) return;

  let score = 0;
  let answeredCount = 0;

  let html = '';
  C9U5_QUIZ_DATA.forEach((item, qIdx) => {
    const userAns = c9u5QuizAnswers[qIdx];
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
              <button onclick="selectC9U5QuizOption(${qIdx}, ${optIdx})" class="p-3 rounded-2xl border text-left text-xs md:text-sm transition cursor-pointer flex items-center gap-2 ${optClass}">
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

  const toNepaliNumC9U5 = (n) => {
    const d = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
    return String(n).split('').map(c => d[parseInt(c, 10)] || c).join('');
  };
  const scoreBadge = document.getElementById('c9u5-quiz-score-badge');
  if (scoreBadge) {
    scoreBadge.textContent = `${toNepaliNumC9U5(score)} / १०`;
  }
}

function selectC9U5QuizOption(qIdx, optIdx) {
  if (c9u5QuizAnswers[qIdx] !== undefined) return; // already answered
  c9u5QuizAnswers[qIdx] = optIdx;

  const isCorrect = optIdx === C9U5_QUIZ_DATA[qIdx].ans;
  if (isCorrect) playAudioC9U5('correct');
  else playAudioC9U5('wrong');

  renderC9U5Quiz();
}

function resetC9U5Quiz() {
  c9u5QuizAnswers = {};
  playAudioC9U5('click');
  renderC9U5Quiz();
}

// -------------------------------------------------------------------------
// Initialization Entrypoint for Unit 5
// -------------------------------------------------------------------------
function initC9U5() {
  selectTissueC9U5('xylem');
  selectBrainPartC9U5('cerebrum');
  resetReflexC9U5();
  selectGlandC9U5('pituitary');
  setAuxinLightC9U5('left');
  triggerGlucoseEventC9U5('reset');
  renderC9U5Quiz();
}



// Ensure startup trigger
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    if (typeof initC9U5 === 'function') initC9U5();
  });
} else {
  if (typeof initC9U5 === 'function') initC9U5();
}
