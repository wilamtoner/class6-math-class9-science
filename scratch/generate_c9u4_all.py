# -*- coding: utf-8 -*-
"""
Class 9 Science Unit 4: क्रम विकास (Evolution)
Generates:
  1. scratch/c9u4_html.html
  2. scratch/c9u4_js.js
"""
import json
import re

html_path = "scratch/c9u4_html.html"
js_path = "scratch/c9u4_js.js"

print("Compiling Unit 4 HTML & JS...")

# =========================================================================
# TAB 1: CONCEPTS & VIRTUAL EVOLUTION LAB
# =========================================================================
tab1_html = """<!-- ================= CLASS 9 UNIT 4 CONTAINER ================= -->
<div id="c9-view-4" class="hidden flex-1 min-w-0 flex flex-col">
  <!-- Unit Header Banner -->
  <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-4">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-100 text-purple-800 border border-purple-200">
          कक्षा ९ विज्ञान तथा प्रविधि | एकाइ ४
        </span>
        <span class="text-xs text-slate-400">•</span>
        <span class="text-xs text-slate-500 font-medium">पाठ्यपुस्तक पृष्ठ ३६–४८</span>
      </div>
      <h2 class="text-2xl md:text-3xl font-black text-slate-900 tracking-tight">
        एकाइ ४: क्रम विकास (Evolution)
      </h2>
      <p class="text-xs md:text-sm text-slate-500 mt-1">
        सजीवहरूको उत्पत्ति र क्रमविकास, जीवावशेष, तुलनात्मक शरीर रचना, डार्बिनको प्राकृतिक छनोट, लेमार्कवाद र उत्परिवर्तन
      </p>
    </div>
    <div class="flex items-center gap-2">
      <span class="inline-flex items-center px-3 py-1 rounded-xl text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
        ✓ सम्पूर्ण पाठ्यपुस्तक अभ्यास तथा परियोजना कार्य समावेश
      </span>
    </div>
  </div>

  <!-- 4-Tab Navigation Bar -->
  <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
    <button onclick="setTabC9U4('concepts')" id="c9u4-tab-concepts" class="px-5 py-2.5 rounded-xl bg-purple-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
      १. सैद्धान्तिक अवधारणा तथा भर्चुअल क्रमविकास ल्याब
    </button>
    <button onclick="setTabC9U4('exercises')" id="c9u4-tab-exercises" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      २. सम्पूर्ण अभ्यास समाधान (१ देखि ४ र परियोजना कार्य)
    </button>
    <button onclick="setTabC9U4('tiers')" id="c9u4-tab-tiers" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
    </button>
    <button onclick="setTabC9U4('quiz')" id="c9u4-tab-quiz" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      ४. स्वमूल्याङ्कन क्विज (१० प्रश्न)
    </button>
  </div>

  <!-- Tab Contents -->
  <!-- ================= TAB 1: CONCEPTS & VIRTUAL SCIENCE LAB ================= -->
  <div id="c9u4-view-concepts" class="space-y-8">
    <!-- Key Theoretical Cards Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <!-- Card 1: Concept of Evolution -->
      <div class="bg-gradient-to-br from-purple-50 to-indigo-50 border border-purple-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-purple-200/60 pb-3">
          <h3 class="font-black text-purple-900 text-base md:text-lg flex items-center gap-2">
            <span>🌍 १. क्रमविकासको अवधारणा र ऐतिहासिक यात्रा</span>
          </h3>
          <span class="text-xs bg-purple-600 text-white font-bold px-2.5 py-1 rounded-full">अवधारणा</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          लाखौँ वर्षको लामो समयावधिमा प्रारम्भिक कालका अति सरल जीवहरूबाट क्रमिक परिवर्तन भई आजका जटिल र नयाँ प्रजातिको उत्पत्ति हुने प्रक्रियालाई <strong>क्रमविकास (Organic Evolution)</strong> भनिन्छ।
        </p>
        <div class="space-y-1.5 text-xs pt-1">
          <div class="bg-white/80 p-2.5 rounded-xl border border-purple-100">
            <strong>क्रमविकासको ऐतिहासिक प्रवाह:</strong><br>
            सरल प्रोकारियोट्स (३.५ अर्ब वर्ष) ➔ एककोषीय युकारियोट्स ➔ ढाड नभएका बहुकोषीय ➔ माछा ➔ उभयचर ➔ सरीसृप ➔ चरा तथा स्तनधारी।
          </div>
        </div>
      </div>

      <!-- Card 2: Evidences of Evolution -->
      <div class="bg-gradient-to-br from-blue-50 to-cyan-50 border border-blue-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-blue-200/60 pb-3">
          <h3 class="font-black text-blue-900 text-base md:text-lg flex items-center gap-2">
            <span>🦴 २. क्रमविकासका प्रमुख वैज्ञानिक प्रमाणहरू</span>
          </h3>
          <span class="text-xs bg-blue-600 text-white font-bold px-2.5 py-1 rounded-full">प्रमाणहरू</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          क्रमविकासलाई पुष्टि गर्ने प्रमुख वैज्ञानिक प्रमाणहरू निम्न हुन्:
        </p>
        <div class="space-y-1.5 text-xs">
          <div class="bg-white/80 p-2 rounded-xl border border-blue-100">
            <strong>१. जीवावशेष (Fossils):</strong> पत्रे चट्टानमा पाइएका पुराना अवशेषहरू (प्यालेन्टोलोजी)।
          </div>
          <div class="bg-white/80 p-2 rounded-xl border border-blue-100">
            <strong>२. समधर्मी अङ्गहरू (Homologous Organs):</strong> उत्पत्ति एउटै, कार्य फरक (मानिसको हात, घोडाको खुट्टा)।
          </div>
          <div class="bg-white/80 p-2 rounded-xl border border-blue-100">
            <strong>३. अवशेषाङ्ग (Vestigial Organs):</strong> पूर्वजमा काम लाग्ने, हाल निष्प्रयोजन (एपेन्डिक्स, पुच्छ्रे हाड)।
          </div>
          <div class="bg-white/80 p-2 rounded-xl border border-blue-100">
            <strong>४. संयोजक कडी (Connecting Links):</strong> आर्कियोप्टेरिक्स (सरीसृप + चरा)।
          </div>
        </div>
      </div>

      <!-- Card 3: Darwinism & Natural Selection -->
      <div class="bg-gradient-to-br from-emerald-50 to-teal-50 border border-emerald-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-emerald-200/60 pb-3">
          <h3 class="font-black text-emerald-900 text-base md:text-lg flex items-center gap-2">
            <span>🌿 ३. डार्बिनको प्राकृतिक छनोटको सिद्धान्त</span>
          </h3>
          <span class="text-xs bg-emerald-600 text-white font-bold px-2.5 py-1 rounded-full">डार्बिनवाद</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          चार्ल्स डार्बिन (१८५९) का अनुसार सीमित स्रोतका लागि जीवहरू बीच हुने सङ्घर्षमा वातावरण अनुकूल सक्षम जीवहरू मात्र बाँच्छन् र सन्तान जन्माउँछन्:
        </p>
        <div class="p-2.5 rounded-xl bg-white/80 border border-emerald-100 text-xs font-mono leading-relaxed">
          अत्यधिक सन्तानोत्पादन ➔ बाँच्नका लागि संघर्ष ➔ परिवृत्ति ➔ योग्यतमको उत्तरजीविता ➔ प्राकृतिक छनोट ➔ नयाँ प्रजातिको उत्पत्ति
        </div>
      </div>

      <!-- Card 4: Lamarckism & Mutation Theory -->
      <div class="bg-gradient-to-br from-amber-50 to-orange-50 border border-amber-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-amber-200/60 pb-3">
          <h3 class="font-black text-amber-900 text-base md:text-lg flex items-center gap-2">
            <span>🧬 ४. लेमार्कवाद, उत्परिवर्तन र नव-डार्बिनवाद</span>
          </h3>
          <span class="text-xs bg-amber-600 text-white font-bold px-2.5 py-1 rounded-full">सिद्धान्तहरू</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          <strong>लेमार्कको सिद्धान्त (१८०९):</strong> अङ्गको बढी प्रयोग र उपार्जित गुणको वंशाणुगतता (विजम्यानले मुसाको पुच्छर काटेर गलत सावित गरे)।<br>
          <strong>ह्युगो डी भ्रिज (१९०१):</strong> उत्परिवर्तन (Mutation) - वंशाणुमा हुने आकस्मिक स्थायी परिवर्तन जसले नयाँ गुण दिन्छ।
        </p>
        <div class="bg-white/80 p-2 rounded-xl border border-amber-100 text-xs">
          <strong>नव-डार्बिनवाद (Modern Synthesis):</strong> प्राकृतिक छनोट + उत्परिवर्तन + वंशाणुगत पुनर्संयोजन = आधुनिक क्रमविकास।
        </div>
      </div>

    </div>

    <!-- ================= VIRTUAL EVOLUTION SCIENCE LAB ================= -->
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 text-white shadow-xl space-y-6">
      <!-- Lab Header -->
      <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-800 pb-5">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/20 text-purple-300 text-xs font-bold border border-purple-500/30 mb-2">
            <span>🦕 भर्चुअल क्रमविकास प्रयोगशाला (Virtual Evolution Science Lab)</span>
          </div>
          <h3 class="text-xl md:text-2xl font-black text-white">क्रमविकासका प्रमाण, प्राकृतिक छनोट र उत्परिवर्तन ल्याब</h3>
          <p class="text-xs md:text-sm text-slate-400">समधर्मी अङ्गहरू, पेपर्ड मथ छलावरण सिमुलेटर, र जीवावशेष/उत्परिवर्तन अन्वेषक</p>
        </div>

        <!-- Mode Switcher Buttons -->
        <div class="flex flex-wrap gap-2 bg-slate-800/80 p-1.5 rounded-2xl border border-slate-700">
          <button onclick="setLabModeC9U4('anatomy')" id="c9u4-btn-mode-anatomy" class="px-3.5 py-2 rounded-xl text-xs font-bold transition bg-purple-600 text-white shadow-sm cursor-pointer">
            🦴 १. शारीरिक तुलना र प्रमाण (Comparative Anatomy)
          </button>
          <button onclick="setLabModeC9U4('selection')" id="c9u4-btn-mode-selection" class="px-3.5 py-2 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:bg-slate-700 cursor-pointer">
            🦋 २. प्राकृतिक छनोट सिमुलेटर (Natural Selection)
          </button>
          <button onclick="setLabModeC9U4('mutation')" id="c9u4-btn-mode-mutation" class="px-3.5 py-2 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:bg-slate-700 cursor-pointer">
            🧬 ३. जीवावशेष र उत्परिवर्तन (Fossils & Mutation)
          </button>
        </div>
      </div>

      <!-- ================= MODE 1: COMPARATIVE ANATOMY & EVIDENCES ================= -->
      <div id="c9u4-lab-mode-anatomy" class="space-y-6">
        <!-- Submode Switcher -->
        <div class="flex flex-wrap gap-2 justify-center">
          <button onclick="setAnatomySubModeC9U4('homology')" id="c9u4-subbtn-homology" class="px-4 py-2 rounded-2xl text-xs font-black transition border bg-purple-500/20 border-purple-400 text-purple-300 cursor-pointer">
            🦴 समधर्मी अङ्गहरू (Homologous Forelimbs)
          </button>
          <button onclick="setAnatomySubModeC9U4('vestigial')" id="c9u4-subbtn-vestigial" class="px-4 py-2 rounded-2xl text-xs font-black transition border bg-slate-800/80 border-slate-700 text-slate-400 hover:text-white cursor-pointer">
            👀 मानव अवशेषाङ्गहरू (Vestigial Organs)
          </button>
          <button onclick="setAnatomySubModeC9U4('connecting')" id="c9u4-subbtn-connecting" class="px-4 py-2 rounded-2xl text-xs font-black transition border bg-slate-800/80 border-slate-700 text-slate-400 hover:text-white cursor-pointer">
            🦅 संयोजक कडी (Archaeopteryx & Platypus)
          </button>
        </div>

        <!-- Submode A: Homologous Forelimbs Interactive Comparison -->
        <div id="c9u4-anat-panel-homology" class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          <!-- Specimen Selector & Visual Comparison -->
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-5 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                <span class="text-xs font-bold text-purple-400">● ढाड भएका जीवहरूको अग्रअङ्ग (Forelimbs Bone Comparison)</span>
                <span class="text-xs px-2.5 py-0.5 rounded-full bg-purple-500/20 text-purple-300 font-mono">HOMOLOGY</span>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                यी सबै जीवहरूको अग्रअङ्गमा ह्युमरस, रेडियस, अल्ना, कार्पल्स, मेटाकार्पल्स र फ्यालेन्जेज समान हुन्छन्:
              </p>
            </div>

            <!-- Organ Selector Pills -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-bold">
              <button onclick="selectHomologyOrganC9U4('human')" id="c9u4-hbtn-human" class="p-2.5 rounded-xl border bg-purple-600 border-purple-500 text-white transition text-center cursor-pointer shadow-sm">
                ✋ मानिसको हात<br><span class="text-[10px] font-normal">(वस्तु समात्न)</span>
              </button>
              <button onclick="selectHomologyOrganC9U4('horse')" id="c9u4-hbtn-horse" class="p-2.5 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white transition text-center cursor-pointer">
                🐎 घोडाको खुट्टा<br><span class="text-[10px] font-normal">(तीव्र दौडिन)</span>
              </button>
              <button onclick="selectHomologyOrganC9U4('bat')" id="c9u4-hbtn-bat" class="p-2.5 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white transition text-center cursor-pointer">
                🦇 चमेराको पखेटा<br><span class="text-[10px] font-normal">(हावामा उड्न)</span>
              </button>
              <button onclick="selectHomologyOrganC9U4('whale')" id="c9u4-hbtn-whale" class="p-2.5 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white transition text-center cursor-pointer">
                🐋 ह्वेलको फ्लीपर<br><span class="text-[10px] font-normal">(पानीमा पौडिन)</span>
              </button>
            </div>

            <!-- Dynamic Skeletal Diagram Display (SVG) -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 flex flex-col items-center justify-center min-h-[180px]">
              <svg viewBox="0 0 400 140" class="w-full max-w-[380px] h-auto select-none" id="c9u4-homology-svg">
                <!-- Humerus (Arm) -->
                <rect x="20" y="55" width="80" height="26" rx="6" fill="#a855f7" stroke="#9333ea" stroke-width="2"/>
                <text x="60" y="72" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Humerus</text>

                <!-- Joint -->
                <circle cx="105" cy="68" r="6" fill="#cbd5e1"/>

                <!-- Radius & Ulna (Forearm) -->
                <rect x="115" y="45" width="85" height="18" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
                <text x="157" y="58" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Radius</text>
                <rect x="115" y="70" width="85" height="18" rx="4" fill="#0ea5e9" stroke="#0284c7" stroke-width="1.5"/>
                <text x="157" y="83" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Ulna</text>

                <!-- Carpals (Wrist) -->
                <rect x="205" y="50" width="35" height="36" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
                <text x="222" y="72" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Carpals</text>

                <!-- Metacarpals & Phalanges (Digits) -->
                <rect x="245" y="45" width="55" height="10" rx="3" fill="#10b981"/>
                <rect x="245" y="58" width="60" height="10" rx="3" fill="#10b981"/>
                <rect x="245" y="71" width="65" height="10" rx="3" fill="#10b981"/>
                <rect x="245" y="84" width="55" height="10" rx="3" fill="#10b981"/>
                <text x="280" y="110" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">Phalanges (औँलाहरू)</text>
              </svg>
              <span class="text-[11px] text-slate-400 mt-2 font-mono">आधारभूत अस्थिपञ्जर ढाँचा: Humerus ➔ Radius/Ulna ➔ Carpals ➔ Phalanges</span>
            </div>
          </div>

          <!-- Detail Card for Selected Organ -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-3">
            <div class="border-b border-slate-700/80 pb-2">
              <span class="text-xs text-purple-400 font-mono" id="c9u4-h-engtitle">HUMAN FORELIMB (HAND)</span>
              <h4 class="text-xl font-black text-white" id="c9u4-h-neptitle">मानिसको हात (Human Hand)</h4>
            </div>

            <div class="space-y-2.5 text-xs text-slate-300">
              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-purple-400 block mb-0.5">बाह्य कार्य र अनुकूलन:</strong>
                <p id="c9u4-h-function" class="leading-relaxed">
                  विभिन्न वस्तुहरू समात्न, लेख्न र औजार चलाउनका लागि विपरित दिशामा चल्ने बुढी औँला (Opposable thumb) सहित अनुकूलित।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-cyan-400 block mb-0.5">हाडहरूको आन्तरिक विशेषता:</strong>
                <p id="c9u4-h-bones" class="leading-relaxed">
                  Humerus, Radius, Ulna, Carpals (८ वटा), Metacarpals (५ वटा), र Phalanges (१४ वटा) मिलेर पूर्ण लचिलोपन दिन्छन्।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-emerald-400 block mb-0.5">क्रमविकासको अर्थ (Evolutionary Meaning):</strong>
                <p id="c9u4-h-meaning" class="leading-relaxed">
                  घोडा, चमेरो र ह्वेलसँग हाडको ढाँचा ठ्याक्कै मिल्नुले यी सबै स्तनधारीहरू एउटै साझा चौपाया पुर्खाबाट विकसित भएका हुन् (Divergent Evolution) भन्ने पुष्टि गर्छ।
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Submode B: Vestigial Organs Explorer -->
        <div id="c9u4-anat-panel-vestigial" class="hidden grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-5 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
              <h4 class="text-sm font-bold text-cyan-400">मानव शरीरका ५ प्रमुख अवशेषाङ्गहरू (Vestigial Organs)</h4>
              <span class="text-xs text-slate-400">पूर्वजको प्रत्यक्ष प्रमाण</span>
            </div>

            <!-- Vestigial Pills -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              <button onclick="selectVestigialC9U4('appendix')" id="c9u4-vbtn-appendix" class="p-3 rounded-2xl border bg-cyan-600/30 border-cyan-500 text-cyan-300 text-left transition cursor-pointer">
                <strong>१. भर्मिफर्म एपेन्डिक्स (Appendix)</strong><br>
                <span class="text-[11px] text-slate-400">ठूलो आन्द्राको फेदमा रहेको सानो नली</span>
              </button>
              <button onclick="selectVestigialC9U4('coccyx')" id="c9u4-vbtn-coccyx" class="p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer">
                <strong>२. पुच्छ्रे हाड (Coccyx / Tailbone)</strong><br>
                <span class="text-[11px] text-slate-400">मेरुदण्डको फेदका ४ जोडिएका हाडहरू</span>
              </button>
              <button onclick="selectVestigialC9U4('plica')" id="c9u4-vbtn-plica" class="p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer">
                <strong>३. प्लीका सेमिल्युनारिस (Plica)</strong><br>
                <span class="text-[11px] text-slate-400">आँखाको भित्री कुनाको रातो पत्र</span>
              </button>
              <button onclick="selectVestigialC9U4('ear')" id="c9u4-vbtn-ear" class="p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer">
                <strong>४. कानको मांसपेशी (Ear Muscles)</strong><br>
                <span class="text-[11px] text-slate-400">कानको लोती हल्लाउने मांसपेशी</span>
              </button>
              <button onclick="selectVestigialC9U4('wisdom')" id="c9u4-vbtn-wisdom" class="p-3 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer sm:col-span-2">
                <strong>५. अक्कल दाँत (Wisdom Teeth)</strong><br>
                <span class="text-[11px] text-slate-400">कच्चा कडा खाना चपाउने तेस्रो बङ्गरा</span>
              </button>
            </div>
          </div>

          <!-- Vestigial Detail -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-3">
            <div class="border-b border-slate-700/80 pb-2">
              <span class="text-xs text-cyan-400 font-mono" id="c9u4-v-engname">VERMIFORM APPENDIX</span>
              <h4 class="text-xl font-black text-white" id="c9u4-v-nepname">भर्मिफर्म एपेन्डिक्स</h4>
            </div>

            <div class="space-y-2.5 text-xs text-slate-300">
              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-amber-400 block mb-0.5">पूर्वजहरूमा उपयोगिता:</strong>
                <p id="c9u4-v-ancestor" class="leading-relaxed">
                  हाम्रा प्राचीन शाकाहारी पूर्वजहरूमा काँचो घाँस-पात र रुखका बोक्रामा भएको सेलुलोज (Cellulose) पचाउने ब्याक्टेरिया भण्डारण गर्न यो निकै लामो र पूर्ण कार्यशील थियो।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-rose-400 block mb-0.5">वर्तमान मानिसमा अवस्था:</strong>
                <p id="c9u4-v-present" class="leading-relaxed">
                  मानिसले खाना पकाएर खान थालेपछि सेलुलोज पचाउने आवश्यकता परेन र यो खुम्चिएर काम नलाग्ने अवशेषाङ्ग बन्यो। कहिलेकाहीँ यसमा संक्रमण भई एपेन्डिसाइटिस (Appendicitis) हुन्छ।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-emerald-400 block mb-0.5">क्रमविकासको निष्कर्ष:</strong>
                <p id="c9u4-v-conclusion" class="leading-relaxed">
                  यसले मानिस शाकाहारी चौपाया पूर्वजबाट विकसित भएको अकाट्य प्रमाण दिन्छ।
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Submode C: Connecting Links Explorer -->
        <div id="c9u4-anat-panel-connecting" class="hidden grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-5 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
              <h4 class="text-sm font-bold text-amber-400">संयोजक कडीहरू (Missing / Connecting Links)</h4>
              <span class="text-xs text-slate-400">दुई वर्ग बीचको पुल</span>
            </div>

            <div class="grid grid-cols-2 gap-3 text-xs">
              <button onclick="selectConnectingC9U4('archaeopteryx')" id="c9u4-cbtn-archaeo" class="p-3.5 rounded-2xl border bg-amber-600/30 border-amber-500 text-amber-300 text-left transition cursor-pointer">
                <strong>१. आर्कियोप्टेरिक्स (Archaeopteryx)</strong><br>
                <span class="text-[11px] text-slate-400">सरीसृप र चरा बीचको कडी (Fossil)</span>
              </button>
              <button onclick="selectConnectingC9U4('platypus')" id="c9u4-cbtn-platypus" class="p-3.5 rounded-2xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer">
                <strong>२. डकबिल्ड प्लाटिपस (Platypus)</strong><br>
                <span class="text-[11px] text-slate-400">सरीसृप र स्तनधारी बीचको कडी (Living)</span>
              </button>
            </div>

            <!-- Visual representation of dual traits -->
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-800 text-xs space-y-2">
              <div class="flex items-center justify-between">
                <span class="text-amber-400 font-bold" id="c9u4-c-class1">सरीसृपका गुणहरू (Reptilian Traits)</span>
                <span class="text-cyan-400 font-bold" id="c9u4-c-class2">चराका गुणहरू (Avian Traits)</span>
              </div>
              <div class="grid grid-cols-2 gap-3 pt-1">
                <ul class="list-disc pl-4 text-slate-300 space-y-1" id="c9u4-c-traits1">
                  <li>च्यापुमा तीखा दाँत</li>
                  <li>हाडयुक्त लामो पुच्छर</li>
                  <li>पखेटामा नंग्रा भएका औँलाहरू</li>
                </ul>
                <ul class="list-disc pl-4 text-slate-300 space-y-1" id="c9u4-c-traits2">
                  <li>शरीरमा प्वाँखको आवरण</li>
                  <li>उड्न मिल्ने पखेटा</li>
                  <li>मुख चराको जस्तै चुच्चो (Beak)</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-3">
            <div class="border-b border-slate-700/80 pb-2">
              <span class="text-xs text-amber-400 font-mono" id="c9u4-c-sci">ARCHAEOPTERYX LITHOGRAPHICA</span>
              <h4 class="text-xl font-black text-white" id="c9u4-c-title">आर्कियोप्टेरिक्स (Archaeopteryx)</h4>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed" id="c9u4-c-desc">
              करिब १५ करोड वर्ष पुरानो जुरासिक कालको जीवावशेष। यसमा सरीसृप र चरा दुवैका लक्षण स्पष्ट देखिन्छन् जसले चराहरूको क्रमविकास प्राचीन सरीसृपबाटै भएको हो भन्ने प्रमाणित गर्छ।
            </p>
            <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700 text-xs text-emerald-300">
              <strong>💡 थोमस हक्स्लेको निष्कर्ष:</strong> "चराहरू वास्तवमा पखेटा पलाएका महिमण्डित सरीसृपहरू (Glorified reptiles) हुन्।"
            </div>
          </div>
        </div>
      </div>

      <!-- ================= MODE 2: NATURAL SELECTION SIMULATOR ================= -->
      <div id="c9u4-lab-mode-selection" class="hidden space-y-6">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3 flex-wrap gap-2">
          <div>
            <h4 class="text-base font-black text-white flex items-center gap-2">
              <span>🦋 औद्योगिक कालोपन (Industrial Melanism) सिमुलेटर</span>
            </h4>
            <p class="text-xs text-slate-400">पेपर्ड मथ (*Biston betularia*) मा डार्बिनको प्राकृतिक छनोटको प्रत्यक्ष अवलोकन</p>
          </div>
          <!-- Environment Switcher -->
          <div class="flex gap-2">
            <button onclick="setMothEnvC9U4('clean')" id="c9u4-env-clean-btn" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-emerald-600 text-white cursor-pointer shadow-sm">
              🌳 सफा वातावरण (Lichen Bark)
            </button>
            <button onclick="setMothEnvC9U4('polluted')" id="c9u4-env-polluted-btn" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-400 hover:text-white cursor-pointer">
              🏭 प्रदूषित वातावरण (Sooty Bark)
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          <!-- Moth Environment Simulation Canvas -->
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-5 flex flex-col justify-between space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold px-3 py-1 rounded-full bg-purple-500/20 text-purple-300" id="c9u4-moth-gen-badge">
                पुस्ता १ (Generation 1)
              </span>
              <span class="text-xs font-mono text-slate-400" id="c9u4-moth-env-label">रुखको काण्ड: सेतो लाइकेनले ढाकिएको</span>
            </div>

            <!-- Interactive Visual Bark with Moths -->
            <div id="c9u4-bark-view" class="h-44 rounded-2xl border flex items-center justify-around relative overflow-hidden transition-all bg-emerald-950/40 border-emerald-800/50">
              <!-- Moths rendered by JS -->
            </div>

            <!-- Generation Stepper Controls -->
            <div class="flex items-center justify-between pt-2 border-t border-slate-800">
              <button onclick="resetMothSimC9U4()" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition cursor-pointer">
                पुनः सुरु गर्नुहोस् (Reset)
              </button>
              <div class="flex gap-2">
                <button onclick="stepMothGenC9U4()" class="px-4 py-2 rounded-xl text-xs font-bold bg-purple-600 hover:bg-purple-500 text-white shadow-sm transition cursor-pointer">
                  अर्को पुस्ता हेर्नुहोस् (Next Generation ➔)
                </button>
              </div>
            </div>
          </div>

          <!-- Population Chart & Scientific Explanation -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-4">
            <div class="border-b border-slate-700/80 pb-2">
              <span class="text-xs text-amber-400 font-mono">NATURAL SELECTION IN ACTION</span>
              <h4 class="text-lg font-black text-white">📊 जनसंख्या अनुपात (Population Ratio)</h4>
            </div>

            <!-- Ratio Bars -->
            <div class="space-y-3 text-xs">
              <div>
                <div class="flex justify-between mb-1 font-bold">
                  <span class="text-slate-300">⚪ सेतो मथ (Typical White):</span>
                  <span id="c9u4-white-pct" class="text-emerald-400">८५%</span>
                </div>
                <div class="w-full bg-slate-900 rounded-full h-3 overflow-hidden border border-slate-700">
                  <div id="c9u4-white-bar" class="bg-emerald-500 h-full rounded-full transition-all duration-500" style="width: 85%;"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between mb-1 font-bold">
                  <span class="text-slate-300">⚫ कालो मथ (Carbonaria Black):</span>
                  <span id="c9u4-black-pct" class="text-purple-400">१५%</span>
                </div>
                <div class="w-full bg-slate-900 rounded-full h-3 overflow-hidden border border-slate-700">
                  <div id="c9u4-black-bar" class="bg-purple-500 h-full rounded-full transition-all duration-500" style="width: 15%;"></div>
                </div>
              </div>
            </div>

            <!-- Diagnostic Narrative -->
            <div class="bg-slate-900/80 p-3.5 rounded-2xl border border-slate-700 text-xs text-slate-300 space-y-1">
              <strong class="text-amber-400 block" id="c9u4-moth-diag-title">छलावरण (Camouflage) प्रभाव:</strong>
              <p id="c9u4-moth-diag-desc" class="leading-relaxed">
                सफा रुखको बोक्रामा सेतो मथ सजिलै लुक्न सक्छन्, तर कालो मथ टाढैबाट देखिने भएकाले चराहरूले सिकार गरी खाइदिन्छन्। त्यसैले प्रकृतिले सेतो मथलाई बचाउँछ।
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= MODE 3: FOSSILS & MUTATION LAB ================= -->
      <div id="c9u4-lab-mode-mutation" class="hidden space-y-6">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-stretch">
          
          <!-- Fossilization Process Explorer -->
          <div class="bg-slate-950/70 border border-slate-800 rounded-3xl p-5 space-y-4">
            <div class="border-b border-slate-800 pb-3">
              <span class="text-xs text-cyan-400 font-mono">FOSSILIZATION PROCESS</span>
              <h4 class="text-lg font-black text-white">🪨 जीवावशेष बन्ने ४ चरणहरू</h4>
            </div>

            <div class="space-y-2 text-xs">
              <div class="p-3 rounded-2xl border bg-slate-900 border-slate-800 space-y-1">
                <strong class="text-cyan-300 block">चरण १: जीवको मृत्यु र द्रुत रूपमा पुरिनु</strong>
                <p class="text-slate-400 leading-relaxed">
                  ताल वा नदीको किनारमा मरेका जीवहरू बाढीले ल्याएको बालुवा र हिलोको थेग्ग्रोमुनि तुरुन्तै पुरिन्छन्।
                </p>
              </div>

              <div class="p-3 rounded-2xl border bg-slate-900 border-slate-800 space-y-1">
                <strong class="text-cyan-300 block">चरण २: अक्सिजनविहीन अवस्था र कुहिनबाट बचावट</strong>
                <p class="text-slate-400 leading-relaxed">
                  बाक्लो माटोको तहमुनि हावा नहुँदा ब्याक्टेरियाले मासु नष्ट गरे पनि कडा हाड र दाँत सुरक्षित रहन्छन्।
                </p>
              </div>

              <div class="p-3 rounded-2xl border bg-slate-900 border-slate-800 space-y-1">
                <strong class="text-cyan-300 block">चरण ३: खनिजीकरण (Petrification)</strong>
                <p class="text-slate-400 leading-relaxed">
                  जमिनमुनिको पानीमा घुलेको सिलिका र क्याल्सियम हाडको मसिना छिद्रमा पसेर हाडलाई नै ढुङ्गामा बदल्छ।
                </p>
              </div>

              <div class="p-3 rounded-2xl border bg-slate-900 border-slate-800 space-y-1">
                <strong class="text-cyan-300 block">चरण ४: भू-उत्थान र उत्खनन (Discovery)</strong>
                <p class="text-slate-400 leading-relaxed">
                  लाखौँ वर्षपछि भूकम्प वा कटानले पत्रे चट्टान सतहमा आउँदा वैज्ञानिकहरूले जीवावशेष उत्खनन गर्दछन्।
                </p>
              </div>
            </div>
          </div>

          <!-- Mutation Simulator -->
          <div class="bg-slate-950/70 border border-slate-800 rounded-3xl p-5 space-y-4">
            <div class="border-b border-slate-800 pb-3">
              <span class="text-xs text-rose-400 font-mono">GENETIC MUTATION SIMULATOR</span>
              <h4 class="text-lg font-black text-white">🧬 उत्परिवर्तन (DNA Mutation) सिमुलेटर</h4>
            </div>

            <p class="text-xs text-slate-300">
              डीएनए कोडमा आकस्मिक परिवर्तन हुँदा जीवमा कस्ता नौला शारीरिक लक्षणहरू देखिन्छन्:
            </p>

            <!-- Mutation Type Buttons -->
            <div class="grid grid-cols-2 gap-2 text-xs font-bold">
              <button onclick="selectMutationDemoC9U4('polydactyly')" id="c9u4-mubtn-poly" class="p-2.5 rounded-xl border bg-rose-600/30 border-rose-500 text-rose-300 text-left transition cursor-pointer">
                🖐️ ६ वटा औँलाहरू (Polydactyly)
              </button>
              <button onclick="selectMutationDemoC9U4('albinism')" id="c9u4-mubtn-albi" class="p-2.5 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer">
                ⚪ अल्बिनिजम (Melanin Loss)
              </button>
              <button onclick="selectMutationDemoC9U4('sickle')" id="c9u4-mubtn-sickle" class="p-2.5 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer">
                🩸 हँसिया आकारको आरबीसी (Sickle Cell)
              </button>
              <button onclick="selectMutationDemoC9U4('evening')" id="c9u4-mubtn-evening" class="p-2.5 rounded-xl border bg-slate-900 border-slate-800 text-slate-400 hover:text-white text-left transition cursor-pointer">
                🌸 इभनिङ प्रिमरोज (Hugo De Vries)
              </button>
            </div>

            <!-- Mutation Diagnostic Result -->
            <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs">
              <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                <span class="font-bold text-white text-sm" id="c9u4-mu-title">६ वटा औँलाहरू (Polydactyly)</span>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-rose-500/20 text-rose-300 font-mono" id="c9u4-mu-badge">AUTOSOMAL DOMINANT</span>
              </div>
              <p class="text-slate-300 leading-relaxed" id="c9u4-mu-desc">
                औँलाको संख्या निर्धारण गर्ने नियामक वंशाणुमा भएको आकस्मिक उत्परिवर्तनले गर्दा हात वा खुट्टामा अतिरिक्त औँला थपिन्छ। यो उत्परिवर्तन वंशाणुगत रूपमा सन्तानमा सर्दछ।
              </p>
              <div class="text-emerald-400 text-[11px] pt-1" id="c9u4-mu-evolution">
                💡 <strong>क्रमविकासमा भूमिका:</strong> यसले प्राकृतिक जनसंख्यामा नयाँ आनुवंशिक विविधता (Variation) ल्याउँछ।
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
"""

print("Tab 1 ready.")
