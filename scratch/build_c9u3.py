# -*- coding: utf-8 -*-
import sys
import json
import re

print("Generating scratch/c9u3_html.html and scratch/c9u3_js.js ...")

# ----------------- HTML GENERATION -----------------
html_content = """<!-- ================= GRADE 9 UNIT 3: MUSHROOM (च्याउ) ================= -->
<div id="c9-view-3" class="hidden flex-1 min-w-0 flex flex-col">
  <!-- Unit Header Banner -->
  <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-4">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200">
          कक्षा ९ विज्ञान तथा प्रविधि | एकाइ ३
        </span>
        <span class="text-xs text-slate-400">•</span>
        <span class="text-xs text-slate-500 font-medium">पाठ्यपुस्तक पृष्ठ २७–३५</span>
      </div>
      <h2 class="text-2xl md:text-3xl font-black text-slate-900 tracking-tight">
        एकाइ ३: च्याउ (Mushroom)
      </h2>
      <p class="text-xs md:text-sm text-slate-500 mt-1">
        च्याउको बाह्य र आन्तरिक सूक्ष्म गिल्स बनोट, जीवन चक्र (Life Cycle), कन्ने च्याउ खेती प्रविधि र विषालु च्याउ पहिचान
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
    <button onclick="setTabC9U3('concepts')" id="c9u3-tab-concepts" class="px-5 py-2.5 rounded-xl bg-emerald-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
      १. सैद्धान्तिक अवधारणा तथा भर्चुअल च्याउ ल्याब
    </button>
    <button onclick="setTabC9U3('exercises')" id="c9u3-tab-exercises" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      २. सम्पूर्ण अभ्यास समाधान (१ देखि ४ र परियोजना कार्य)
    </button>
    <button onclick="setTabC9U3('tiers')" id="c9u3-tab-tiers" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
    </button>
    <button onclick="setTabC9U3('quiz')" id="c9u3-tab-quiz" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      ४. स्वमूल्याङ्कन क्विज (१० प्रश्न)
    </button>
  </div>

  <!-- Tab Contents -->
  <!-- ================= TAB 1: CONCEPTS & VIRTUAL SCIENCE LAB ================= -->
  <div id="c9u3-view-concepts" class="space-y-8">
    <!-- Key Theoretical Cards Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <!-- Card 1: Introduction & Nature -->
      <div class="bg-gradient-to-br from-emerald-50 to-teal-50 border border-emerald-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-emerald-200/60 pb-3">
          <h3 class="font-black text-emerald-900 text-base md:text-lg flex items-center gap-2">
            <span>🍄 १. च्याउको परिचय, स्वभाव र पोषण</span>
          </h3>
          <span class="text-xs bg-emerald-600 text-white font-bold px-2.5 py-1 rounded-full">अवधारणा</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          च्याउ फन्जाई जगतको <strong>बेसिडियोमाइकोटा (Basidiomycota)</strong> समूहमा पर्ने बहुकोषीय युकेरियोटिक ढुसी हो। यसमा हरितकण नहुने भएकाले प्रकाश-संश्लेषण गर्न सक्दैन र गोबर, पराल तथा सडेगलेका जैविक वस्तुहरूबाट बाह्य पाचन गरी पोषण लिने भएकाले यसलाई <strong>मृतोपजीवी (Saprotroph)</strong> भनिन्छ।
        </p>
        <div class="grid grid-cols-2 gap-2 text-xs pt-1">
          <div class="bg-white/80 p-2.5 rounded-xl border border-emerald-100">
            <span class="font-bold text-emerald-800 block">खानयोग्य च्याउहरू:</span>
            कन्ने, डल्ले, गोब्रे, सिताके
          </div>
          <div class="bg-white/80 p-2.5 rounded-xl border border-emerald-100">
            <span class="font-bold text-emerald-800 block">औषधीय च्याउ:</span>
            रातो च्याउ (<em>Ganoderma</em>) - क्यान्सर प्रतिरोधी
          </div>
        </div>
      </div>

      <!-- Card 2: Morphological Structure -->
      <div class="bg-gradient-to-br from-amber-50 to-orange-50 border border-amber-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-amber-200/60 pb-3">
          <h3 class="font-black text-amber-900 text-base md:text-lg flex items-center gap-2">
            <span>☂️ २. च्याउको शारीरिक बनोट (Anatomy)</span>
          </h3>
          <span class="text-xs bg-amber-600 text-white font-bold px-2.5 py-1 rounded-full">संरचना</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          च्याउको शरीरलाई मुख्यतया दुई भागमा विभाजन गरिन्छ:
        </p>
        <div class="space-y-2 text-xs">
          <div class="bg-white/80 p-2.5 rounded-xl border border-amber-100">
            <span class="font-bold text-amber-900">१. भेजिटेटिभ भाग (माइसेलियम / Mycelium):</span>
            जमिनमुनि धागो जस्ता हाइफीहरूको सञ्जाल जसले पानी र जैविक पोषक तत्व सोस्दछ।
          </div>
          <div class="bg-white/80 p-2.5 rounded-xl border border-amber-100">
            <span class="font-bold text-amber-900">२. फ्रुटिङ बडी (Fruiting Body - प्रजनन भाग):</span>
            जमिनमाथि छाता जस्तो देखिने भाग, जसमा <strong>पाइलस (छतरी)</strong>, <strong>गिल्स (पत्रहरू)</strong>, <strong>स्टाइप (डाँठ)</strong> र <strong>एनुलस (औँठी)</strong> हुन्छन्।
          </div>
        </div>
      </div>

      <!-- Card 3: Internal Gill Anatomy -->
      <div class="bg-gradient-to-br from-indigo-50 to-blue-50 border border-indigo-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-indigo-200/60 pb-3">
          <h3 class="font-black text-indigo-900 text-base md:text-lg flex items-center gap-2">
            <span>🔬 ३. गिल्सको आन्तरिक सूक्ष्म संरचना (Gill T.S.)</span>
          </h3>
          <span class="text-xs bg-indigo-600 text-white font-bold px-2.5 py-1 rounded-full">सूक्ष्म रचना</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          गिल्सको अनुप्रस्थ काट (T.S.) मा भित्रदेखि बाहिरसम्म स्पष्ट तीन तहहरू हुन्छन्:
        </p>
        <div class="space-y-1.5 text-xs">
          <div class="bg-white/80 p-2 rounded-xl border border-indigo-100">
            <strong>१. ट्रामा (Trama):</strong> गिल्सको बीचको लाम्चा हाइफीहरूको केन्द्रीय भाग जसले गिल्सलाई आकार र सहारा दिन्छ।
          </div>
          <div class="bg-white/80 p-2 rounded-xl border border-indigo-100">
            <strong>२. सब-हाइमेनियम (Sub-hymenium):** ट्रामा र हाइमेनियम बीचको साना गोलाकार कोषहरूको मध्य तह।
          </div>
          <div class="bg-white/80 p-2 rounded-xl border border-indigo-100">
            <strong>३. हाइमेनियम (Hymenium):** सबैभन्दा बाहिरी उर्वर तह जसमा **बेसिडियम** (उर्वर कोष, ४ बेसिडियोस्पोर बनाउने) र **प्याराफाइसिस** (बन्ध्या कोष, सहारा दिने) हुन्छन्।
          </div>
        </div>
      </div>

      <!-- Card 4: Life Cycle & Farming -->
      <div class="bg-gradient-to-br from-purple-50 to-pink-50 border border-purple-200 rounded-3xl p-6 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-purple-200/60 pb-3">
          <h3 class="font-black text-purple-900 text-base md:text-lg flex items-center gap-2">
            <span>🌾 ४. जीवन चक्र र कन्ने च्याउ खेती प्रविधि</span>
          </h3>
          <span class="text-xs bg-purple-600 text-white font-bold px-2.5 py-1 rounded-full">व्यावहारिक</span>
        </div>
        <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
          च्याउको बेसिडियममा <strong>क्यारियोगामी (Karyogamy)</strong> र <strong>मियोसिस (Meiosis)</strong> पश्चात् ४ वटा बेसिडियोस्पोर बन्छन्। अंकुरण भई प्राथमिक माइसेलियम (n) बन्दछ र विपरित स्ट्रेन मिसिएर दोस्रो माइसेलियम (n+n) बनी नयाँ फ्रुटिङ बडी बन्दछ।
        </p>
        <div class="bg-white/80 p-2.5 rounded-xl border border-purple-100 text-xs">
          <span class="font-bold text-purple-900 block mb-1">कन्ने च्याउ खेतीका ६ चरण:</span>
          १. पराल काट्ने (२-३ इन्च) ➔ २. पराल उसिन्ने/निर्मलीकरण ➔ ३. चिस्यान नियन्त्रण (६०-६५%) ➔ ४. बीउ मिसाउने र पोका पार्ने ➔ ५. ओथारो (२०-२५°C, अँध्यारो) ➔ ६. झोला खोल्ने र च्याउ टिप्ने।
        </div>
      </div>

    </div>

    <!-- ================= VIRTUAL MUSHROOM SCIENCE LAB ================= -->
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 text-white shadow-xl space-y-6">
      <!-- Lab Header -->
      <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-800 pb-5">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-bold border border-emerald-500/30 mb-2">
            <span>🍄 भर्चुअल च्याउ विज्ञान प्रयोगशाला (Virtual Mushroom Science Lab)</span>
          </div>
          <h3 class="text-xl md:text-2xl font-black text-white">च्याउको आन्तरिक बनोट, कन्ने च्याउ खेती र सुरक्षा ल्याब</h3>
          <p class="text-xs md:text-sm text-slate-400">बाह्य र सूक्ष्म गिल्स बनोट, ६-चरण खेती सिमुलेटर, र विषालु च्याउ पहिचान प्रणाली</p>
        </div>

        <!-- Mode Switcher Buttons -->
        <div class="flex flex-wrap gap-2 bg-slate-800/80 p-1.5 rounded-2xl border border-slate-700">
          <button onclick="setLabModeC9U3('anatomy')" id="c9u3-btn-mode-anatomy" class="px-3.5 py-2 rounded-xl text-xs font-bold transition bg-emerald-600 text-white shadow-sm cursor-pointer">
            🔬 १. च्याउ तथा गिल्स बनोट (Anatomy)
          </button>
          <button onclick="setLabModeC9U3('farming')" id="c9u3-btn-mode-farming" class="px-3.5 py-2 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:bg-slate-700 cursor-pointer">
            🌾 २. कन्ने च्याउ खेती (Cultivation)
          </button>
          <button onclick="setLabModeC9U3('safety')" id="c9u3-btn-mode-safety" class="px-3.5 py-2 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:bg-slate-700 cursor-pointer">
            ⚠️ ३. विषालु च्याउ पहिचान (Safety)
          </button>
        </div>
      </div>

      <!-- ================= MODE 1: MUSHROOM & GILL ANATOMY EXPLORER ================= -->
      <div id="c9u3-lab-mode-anatomy" class="space-y-6">
        <!-- Submode Switcher -->
        <div class="flex flex-wrap gap-2 justify-center">
          <button onclick="setAnatomySubModeC9U3('external')" id="c9u3-subbtn-external" class="px-4 py-2 rounded-2xl text-xs font-black transition border bg-emerald-500/20 border-emerald-400 text-emerald-300 cursor-pointer">
            🍄 बाह्य फ्रुटिङ बडी (External Anatomy)
          </button>
          <button onclick="setAnatomySubModeC9U3('internal')" id="c9u3-subbtn-internal" class="px-4 py-2 rounded-2xl text-xs font-black transition border bg-slate-800/80 border-slate-700 text-slate-400 hover:text-white cursor-pointer">
            🔬 गिल्सको सूक्ष्म अनुप्रस्थ काट (Internal Gill T.S.)
          </button>
        </div>

        <!-- Submode A: External Anatomy Explorer -->
        <div id="c9u3-anat-panel-external" class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
          <!-- SVG Diagram Display -->
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-4 flex flex-col items-center justify-center relative min-h-[380px]">
            <span class="absolute top-3 left-4 text-xs font-mono text-emerald-400 font-bold">● च्याउको बाह्य शारीरिक संरचना (Interactive Visual)</span>
            
            <svg viewBox="0 0 450 380" class="w-full max-w-[420px] h-auto drop-shadow-md select-none">
              <!-- Definitions for gradients -->
              <defs>
                <linearGradient id="c9u3-cap-grad" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="#fbbf24"/>
                  <stop offset="50%" stop-color="#d97706"/>
                  <stop offset="100%" stop-color="#b45309"/>
                </linearGradient>
                <linearGradient id="c9u3-stipe-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#fef3c7"/>
                  <stop offset="50%" stop-color="#fde68a"/>
                  <stop offset="100%" stop-color="#fcd34d"/>
                </linearGradient>
                <filter id="glow-emerald" x="-20%" y="-20%" width="140%" height="140%">
                  <feGaussianBlur stdDeviation="4" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
              </defs>

              <!-- Mycelium / Hyphae at bottom -->
              <g id="svg-part-mycelium" onclick="selectExtPartC9U3('mycelium')" class="cursor-pointer transition hover:opacity-80">
                <!-- Ground line -->
                <line x1="60" y1="310" x2="390" y2="310" stroke="#78350f" stroke-width="4" stroke-dasharray="6,4" />
                <text x="70" y="325" fill="#a1a1aa" font-size="10" font-family="sans-serif">जमिनको सतह (Soil Level)</text>
                <!-- Root like hyphae -->
                <path d="M 210,310 Q 190,335 160,345 M 225,310 Q 225,340 215,365 M 240,310 Q 260,330 290,340 M 180,330 Q 150,340 130,360 M 270,325 Q 300,345 330,365 M 215,345 Q 235,360 245,375" stroke="#34d399" stroke-width="2.5" fill="none" stroke-linecap="round" />
                <circle cx="225" cy="345" r="30" fill="#10b981" opacity="0.15" />
              </g>

              <!-- Stipe (Stem) -->
              <g id="svg-part-stipe" onclick="selectExtPartC9U3('stipe')" class="cursor-pointer transition hover:opacity-90">
                <path d="M 205,170 C 200,220 195,270 190,310 L 260,310 C 255,270 250,220 245,170 Z" fill="url(#c9u3-stipe-grad)" stroke="#b45309" stroke-width="2.5"/>
                <!-- Stipe fiber lines -->
                <line x1="218" y1="180" x2="214" y2="300" stroke="#d97706" stroke-width="1" opacity="0.5"/>
                <line x1="232" y1="180" x2="236" y2="300" stroke="#d97706" stroke-width="1" opacity="0.5"/>
              </g>

              <!-- Annulus (Ring) -->
              <g id="svg-part-annulus" onclick="selectExtPartC9U3('annulus')" class="cursor-pointer transition hover:opacity-90">
                <ellipse cx="225" cy="220" rx="36" ry="10" fill="#fef3c7" stroke="#b45309" stroke-width="2" />
                <path d="M 190,220 Q 225,236 260,220" stroke="#92400e" stroke-width="2" fill="none"/>
              </g>

              <!-- Gills (Under Cap) -->
              <g id="svg-part-gills" onclick="selectExtPartC9U3('gills')" class="cursor-pointer transition hover:opacity-90">
                <path d="M 90,165 Q 225,195 360,165 C 330,175 270,185 225,185 C 180,185 120,175 90,165 Z" fill="#b45309" stroke="#78350f" stroke-width="1.5"/>
                <!-- Gill lines radiating -->
                <line x1="120" y1="168" x2="205" y2="175" stroke="#fde68a" stroke-width="1.5"/>
                <line x1="150" y1="172" x2="210" y2="177" stroke="#fde68a" stroke-width="1.5"/>
                <line x1="180" y1="175" x2="215" y2="178" stroke="#fde68a" stroke-width="1.5"/>
                <line x1="330" y1="168" x2="245" y2="175" stroke="#fde68a" stroke-width="1.5"/>
                <line x1="300" y1="172" x2="240" y2="177" stroke="#fde68a" stroke-width="1.5"/>
                <line x1="270" y1="175" x2="235" y2="178" stroke="#fde68a" stroke-width="1.5"/>
              </g>

              <!-- Pileus (Cap) -->
              <g id="svg-part-pileus" onclick="selectExtPartC9U3('pileus')" class="cursor-pointer transition hover:opacity-90">
                <path d="M 80,165 C 80,75 140,45 225,45 C 310,45 370,75 370,165 C 320,180 130,180 80,165 Z" fill="url(#c9u3-cap-grad)" stroke="#92400e" stroke-width="3"/>
                <!-- Cap spot details -->
                <ellipse cx="160" cy="95" rx="14" ry="7" fill="#fef3c7" opacity="0.4"/>
                <ellipse cx="280" cy="100" rx="18" ry="8" fill="#fef3c7" opacity="0.4"/>
                <ellipse cx="225" cy="70" rx="12" ry="6" fill="#fef3c7" opacity="0.4"/>
              </g>

              <!-- Interactive Pointer Labels -->
              <!-- Pileus -->
              <g onclick="selectExtPartC9U3('pileus')" class="cursor-pointer">
                <line x1="330" y1="80" x2="390" y2="60" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="390" cy="60" r="4" fill="#f59e0b"/>
                <rect x="340" y="38" width="95" height="20" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
                <text x="387" y="52" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">१. पाइलस (Cap)</text>
              </g>

              <!-- Gills -->
              <g onclick="selectExtPartC9U3('gills')" class="cursor-pointer">
                <line x1="120" y1="175" x2="45" y2="165" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="45" cy="165" r="4" fill="#f59e0b"/>
                <rect x="5" y="152" width="85" height="20" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
                <text x="47" y="166" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">२. गिल्स (Gills)</text>
              </g>

              <!-- Annulus -->
              <g onclick="selectExtPartC9U3('annulus')" class="cursor-pointer">
                <line x1="262" y1="222" x2="380" y2="215" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="380" cy="215" r="4" fill="#f59e0b"/>
                <rect x="330" y="202" width="105" height="20" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
                <text x="382" y="216" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">३. एनुलस (Ring)</text>
              </g>

              <!-- Stipe -->
              <g onclick="selectExtPartC9U3('stipe')" class="cursor-pointer">
                <line x1="195" y1="265" x2="50" y2="255" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="50" cy="255" r="4" fill="#f59e0b"/>
                <rect x="10" y="242" width="85" height="20" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
                <text x="52" y="256" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">४. स्टाइप (Stipe)</text>
              </g>

              <!-- Mycelium -->
              <g onclick="selectExtPartC9U3('mycelium')" class="cursor-pointer">
                <line x1="285" y1="345" x2="385" y2="335" stroke="#10b981" stroke-width="2"/>
                <circle cx="385" cy="335" r="4" fill="#10b981"/>
                <rect x="320" y="322" width="120" height="20" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
                <text x="380" y="336" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">५. माइसेलियम (Hyphae)</text>
              </g>
            </svg>

            <!-- Quick Selector Pills -->
            <div class="flex flex-wrap gap-1.5 justify-center mt-3">
              <button onclick="selectExtPartC9U3('pileus')" id="c9u3-pbtn-pileus" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-emerald-600 text-white cursor-pointer">
                पाइलस (Pileus)
              </button>
              <button onclick="selectExtPartC9U3('gills')" id="c9u3-pbtn-gills" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                गिल्स (Gills)
              </button>
              <button onclick="selectExtPartC9U3('annulus')" id="c9u3-pbtn-annulus" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                एनुलस (Annulus)
              </button>
              <button onclick="selectExtPartC9U3('stipe')" id="c9u3-pbtn-stipe" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                स्टाइप (Stipe)
              </button>
              <button onclick="selectExtPartC9U3('mycelium')" id="c9u3-pbtn-mycelium" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                माइसेलियम (Mycelium)
              </button>
            </div>
          </div>

          <!-- Part Details Panel -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/80 pb-3">
              <div>
                <span class="text-xs text-emerald-400 font-mono" id="c9u3-ext-engname">CAP / PILEUS</span>
                <h4 class="text-xl font-black text-white" id="c9u3-ext-nepname">पाइलस (Pileus / Cap)</h4>
              </div>
              <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold" id="c9u3-ext-role">
                सुरक्षा छाता
              </span>
            </div>

            <div class="space-y-3 text-xs md:text-sm text-slate-300">
              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-emerald-400 block mb-1">स्थान तथा बनावट:</strong>
                <p id="c9u3-ext-location" class="leading-relaxed">
                  स्टाइपको माथिल्लो टुप्पोमा रहेको फराकिलो, छाता आकारको भाग। यसको माथिल्लो सतह चिल्लो वा कत्लादार हुन्छ।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-amber-400 block mb-1">मुख्य जैविक कार्य:</strong>
                <p id="c9u3-ext-function" class="leading-relaxed">
                  तल्लो भागमा रहेका संवेदनशील पत्रहरू (गिल्स) र बन्दै गरेका बीजाणु (Basidiospore) हरूलाई घाम, पानी र बाह्य चोटपटकबाट सुरक्षा प्रदान गर्दछ।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-cyan-400 block mb-1">महत्त्वपूर्ण वैज्ञानिक तथ्य:</strong>
                <p id="c9u3-ext-fact" class="leading-relaxed">
                  च्याउको पाइलस, गिल्स र स्टाइप मिलेर प्रजनन भाग (Fruiting Body) बन्दछ, जुन जमिनमाथि मात्र देखिन्छ।
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Submode B: Internal Gill T.S. Explorer -->
        <div id="c9u3-anat-panel-internal" class="hidden grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
          <!-- SVG Diagram Display -->
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-4 flex flex-col items-center justify-center relative min-h-[380px]">
            <span class="absolute top-3 left-4 text-xs font-mono text-cyan-400 font-bold">● गिल्सको अनुप्रस्थ काट (T.S. of Gill Microscopic Anatomy)</span>
            
            <svg viewBox="0 0 450 380" class="w-full max-w-[420px] h-auto drop-shadow-md select-none">
              <!-- Definitions -->
              <defs>
                <linearGradient id="c9u3-trama-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#475569"/>
                  <stop offset="50%" stop-color="#64748b"/>
                  <stop offset="100%" stop-color="#475569"/>
                </linearGradient>
                <linearGradient id="c9u3-subhymen-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#0284c7"/>
                  <stop offset="100%" stop-color="#0369a1"/>
                </linearGradient>
              </defs>

              <!-- Central Core: Trama -->
              <g id="svg-part-trama" onclick="selectIntPartC9U3('trama')" class="cursor-pointer transition hover:opacity-90">
                <rect x="180" y="30" width="90" height="320" rx="8" fill="url(#c9u3-trama-grad)" stroke="#334155" stroke-width="2"/>
                <!-- Trama vertical hyphae filaments -->
                <line x1="200" y1="40" x2="200" y2="340" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,2"/>
                <line x1="215" y1="40" x2="215" y2="340" stroke="#cbd5e1" stroke-width="1.5"/>
                <line x1="230" y1="40" x2="230" y2="340" stroke="#cbd5e1" stroke-width="1.5"/>
                <line x1="245" y1="40" x2="245" y2="340" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,2"/>
                <text x="225" y="195" fill="#f8fafc" font-size="12" font-weight="black" text-anchor="middle">ट्रामा (TRAMA)</text>
              </g>

              <!-- Sub-hymenium Layer (Left & Right) -->
              <g id="svg-part-subhymenium" onclick="selectIntPartC9U3('subhymenium')" class="cursor-pointer transition hover:opacity-90">
                <!-- Left subhymenium -->
                <rect x="135" y="40" width="45" height="300" rx="4" fill="url(#c9u3-subhymen-grad)" stroke="#0284c7" stroke-width="1.5"/>
                <!-- Right subhymenium -->
                <rect x="270" y="40" width="45" height="300" rx="4" fill="url(#c9u3-subhymen-grad)" stroke="#0284c7" stroke-width="1.5"/>
                <!-- Small cellular dots -->
                <circle cx="155" cy="80" r="5" fill="#bae6fd"/>
                <circle cx="160" cy="140" r="6" fill="#bae6fd"/>
                <circle cx="150" cy="200" r="5" fill="#bae6fd"/>
                <circle cx="160" cy="260" r="6" fill="#bae6fd"/>
                <circle cx="295" cy="80" r="5" fill="#bae6fd"/>
                <circle cx="290" cy="140" r="6" fill="#bae6fd"/>
                <circle cx="300" cy="200" r="5" fill="#bae6fd"/>
                <circle cx="290" cy="260" r="6" fill="#bae6fd"/>
              </g>

              <!-- Hymenium Layer (Left side outer) -->
              <!-- Paraphysis (Sterile cells) -->
              <g id="svg-part-paraphysis" onclick="selectIntPartC9U3('paraphysis')" class="cursor-pointer transition hover:opacity-90">
                <!-- Left paraphyses -->
                <rect x="85" y="60" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="85" y="150" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="85" y="240" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <!-- Right paraphyses -->
                <rect x="315" y="60" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="315" y="150" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="315" y="240" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
              </g>

              <!-- Basidium (Club shaped fertile cell) -->
              <g id="svg-part-basidium" onclick="selectIntPartC9U3('basidium')" class="cursor-pointer transition hover:opacity-90">
                <!-- Left Basidium at y=100 -->
                <path d="M 135,95 L 85,90 C 70,85 55,95 55,107 C 55,119 70,129 85,124 L 135,119 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
                <!-- Sterigmata (4 prongs) -->
                <path d="M 55,97 Q 40,92 35,90 M 55,103 Q 38,101 30,101 M 55,111 Q 38,113 30,113 M 55,117 Q 40,122 35,124" stroke="#34d399" stroke-width="2" fill="none"/>

                <!-- Left Basidium at y=190 -->
                <path d="M 135,185 L 85,180 C 70,175 55,185 55,197 C 55,209 70,219 85,214 L 135,209 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
                <path d="M 55,187 Q 40,182 35,180 M 55,193 Q 38,191 30,191 M 55,201 Q 38,203 30,203 M 55,207 Q 40,212 35,214" stroke="#34d399" stroke-width="2" fill="none"/>

                <!-- Right Basidium at y=100 -->
                <path d="M 315,95 L 365,90 C 380,85 395,95 395,107 C 395,119 380,129 365,124 L 315,119 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
                <path d="M 395,97 Q 410,92 415,90 M 395,103 Q 412,101 420,101 M 395,111 Q 412,113 420,113 M 395,117 Q 410,122 415,124" stroke="#34d399" stroke-width="2" fill="none"/>
              </g>

              <!-- Basidiospores on sterigmata -->
              <g id="svg-part-spores" onclick="selectIntPartC9U3('spores')" class="cursor-pointer transition hover:opacity-90">
                <!-- Left spores (y=100) -->
                <ellipse cx="28" cy="88" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="22" cy="101" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="22" cy="113" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="28" cy="126" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>

                <!-- Right spores (y=100) -->
                <ellipse cx="422" cy="88" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="428" cy="101" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="428" cy="113" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="422" cy="126" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
              </g>

              <!-- Labels -->
              <text x="225" y="365" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">← सब-हाइमेनियम | ट्रामा (केन्द्र) | सब-हाइमेनियम →</text>
            </svg>

            <!-- Quick Selector Pills -->
            <div class="flex flex-wrap gap-1.5 justify-center mt-3">
              <button onclick="selectIntPartC9U3('basidium')" id="c9u3-ibtn-basidium" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-emerald-600 text-white cursor-pointer">
                बेसिडियम (Basidium)
              </button>
              <button onclick="selectIntPartC9U3('paraphysis')" id="c9u3-ibtn-paraphysis" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                प्याराफाइसिस (Paraphysis)
              </button>
              <button onclick="selectIntPartC9U3('spores')" id="c9u3-ibtn-spores" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                बेसिडियोस्पोर (Spore)
              </button>
              <button onclick="selectIntPartC9U3('subhymenium')" id="c9u3-ibtn-subhymenium" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                सब-हाइमेनियम (Sub-hymenium)
              </button>
              <button onclick="selectIntPartC9U3('trama')" id="c9u3-ibtn-trama" class="px-3 py-1 rounded-xl text-xs font-bold transition bg-slate-800 text-slate-300 hover:text-white cursor-pointer">
                ट्रामा (Trama)
              </button>
            </div>
          </div>

          <!-- Internal Part Details Panel -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/80 pb-3">
              <div>
                <span class="text-xs text-emerald-400 font-mono" id="c9u3-int-engname">FERTILE CLUB CELL</span>
                <h4 class="text-xl font-black text-white" id="c9u3-int-nepname">बेसिडियम (Basidium)</h4>
              </div>
              <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold" id="c9u3-int-role">
                उर्वर कोष (Fertile)
              </span>
            </div>

            <div class="space-y-3 text-xs md:text-sm text-slate-300">
              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-emerald-400 block mb-1">स्थान तथा आकार:</strong>
                <p id="c9u3-int-location" class="leading-relaxed">
                  गिल्सको सबैभन्दा बाहिरी हाइमेनियम (Hymenium) तहमा प्याराफाइसिसहरूको बीचमा ठाडो मिलेर रहेको गदा आकारको (club-shaped) कोष।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-amber-400 block mb-1">प्रजनन कार्य र बीजाणु उत्पादन:</strong>
                <p id="c9u3-int-function" class="leading-relaxed">
                  यसभित्र क्यारियोगामी भई डिप्लोइड न्युक्लियस बन्छ, त्यसपछि मियोसिस विभाजन पश्चात् ४ ओटा अगुणित (Haploid, n) बेसिडियोस्पोरहरू टुप्पोका स्टिरिग्मामा बन्दछन्।
                </p>
              </div>

              <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700">
                <strong class="text-cyan-400 block mb-1">आनुवंशिक विशेषता:</strong>
                <p id="c9u3-int-fact" class="leading-relaxed">
                  बन्ने ४ वटा बेसिडियोस्पोरहरूमध्ये २ वटा धनात्मक (+) र २ वटा ऋणात्मक (-) स्ट्रेनका हुन्छन्।
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= MODE 2: KANNE MUSHROOM CULTIVATION SIMULATOR ================= -->
      <div id="c9u3-lab-mode-farming" class="hidden space-y-6">
        <!-- Stage Stepper Navigation -->
        <div class="flex items-center justify-between border-b border-slate-800 pb-3 flex-wrap gap-2">
          <div class="text-xs font-bold text-slate-400">
            कन्ने च्याउ खेतीका ६ व्यावहारिक चरणहरू:
          </div>
          <div class="flex gap-1.5 overflow-x-auto pb-1" id="c9u3-farming-stepper">
            <!-- Rendered by JS -->
          </div>
        </div>

        <!-- Main Farming Simulation Display Box -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          <!-- Stage Visual Card & Narrative -->
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30" id="c9u3-farm-step-badge">
                  चरण १ / ६
                </span>
                <span class="text-xs font-mono text-slate-400" id="c9u3-farm-timeline">समय: दिन १</span>
              </div>
              <h4 class="text-xl md:text-2xl font-black text-white" id="c9u3-farm-title">परालको छनोट र टुक्राउने कार्य</h4>
              <p class="text-xs md:text-sm text-slate-300 mt-2 leading-relaxed" id="c9u3-farm-desc">
                ताजा, नकुहिएको र ओस नलागेको सफा सुकेको धानको पराल छान्ने। हँसिया वा मेसिनले पराललाई २ देखि ३ इन्च (५-८ से.मी.) लामा टुक्राहरूमा काट्ने।
              </p>
            </div>

            <!-- Environmental Condition Meters for the Stage -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2">
              <div class="bg-slate-900/90 border border-slate-800 p-2.5 rounded-2xl text-center">
                <span class="text-[10px] text-slate-400 block">तापक्रम</span>
                <span class="text-xs font-bold text-amber-400" id="c9u3-farm-temp">सामान्य (१५-२५°C)</span>
              </div>
              <div class="bg-slate-900/90 border border-slate-800 p-2.5 rounded-2xl text-center">
                <span class="text-[10px] text-slate-400 block">पराल चिस्यान</span>
                <span class="text-xs font-bold text-cyan-400" id="c9u3-farm-straw-moisture">सुख्खा (१०%)</span>
              </div>
              <div class="bg-slate-900/90 border border-slate-800 p-2.5 rounded-2xl text-center">
                <span class="text-[10px] text-slate-400 block">कोठाको प्रकाश</span>
                <span class="text-xs font-bold text-purple-400" id="c9u3-farm-light">उज्यालो</span>
              </div>
              <div class="bg-slate-900/90 border border-slate-800 p-2.5 rounded-2xl text-center">
                <span class="text-[10px] text-slate-400 block">सावधानी स्तर</span>
                <span class="text-xs font-bold text-emerald-400" id="c9u3-farm-hygiene">उच्च सरसफाइ</span>
              </div>
            </div>

            <!-- Navigation Controls -->
            <div class="flex items-center justify-between pt-4 border-t border-slate-800">
              <button onclick="prevFarmStageC9U3()" id="c9u3-farm-prev-btn" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition cursor-pointer">
                ← अघिल्लो चरण
              </button>
              <button onclick="nextFarmStageC9U3()" id="c9u3-farm-next-btn" class="px-5 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white shadow-sm transition cursor-pointer">
                अर्को चरण →
              </button>
            </div>
          </div>

          <!-- Interactive Moisture & Hygiene Test Simulator -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-4">
            <div class="border-b border-slate-700/80 pb-3">
              <span class="text-xs text-amber-400 font-mono">CRITICAL SUCCESS FACTOR</span>
              <h4 class="text-lg font-black text-white">💧 परालको चिस्यान परीक्षण (Moisture Squeeze Test)</h4>
            </div>

            <p class="text-xs text-slate-300 leading-relaxed">
              च्याउ खेती असफल हुने ९०% कारण परालमा गलत चिस्यान हुनु हो। हातको मुठ्ठीमा उसिनेको पराल बेस्सरी निचोरेर परीक्षण गरिन्छ।
            </p>

            <!-- Interactive Squeeze Buttons -->
            <div class="grid grid-cols-3 gap-2">
              <button onclick="setMoistureC9U3('dry')" id="c9u3-mbtn-dry" class="p-2.5 rounded-xl border border-slate-600 text-xs font-bold text-center transition cursor-pointer bg-slate-900 text-slate-300">
                कम चिस्यान<br><span class="text-[10px] font-normal">(<५०% सुख्खा)</span>
              </button>
              <button onclick="setMoistureC9U3('ideal')" id="c9u3-mbtn-ideal" class="p-2.5 rounded-xl border border-emerald-500 text-xs font-bold text-center transition cursor-pointer bg-emerald-600 text-white shadow-sm">
                उपयुक्त चिस्यान<br><span class="text-[10px] font-normal">(६०-६५% आदर्श)</span>
              </button>
              <button onclick="setMoistureC9U3('wet')" id="c9u3-mbtn-wet" class="p-2.5 rounded-xl border border-slate-600 text-xs font-bold text-center transition cursor-pointer bg-slate-900 text-slate-300">
                अत्यधिक चिस्यान<br><span class="text-[10px] font-normal">(>७५% पानी चुहिने)</span>
              </button>
            </div>

            <!-- Test Result Diagnostic Box -->
            <div id="c9u3-moisture-feedback" class="p-3.5 rounded-2xl border text-xs leading-relaxed space-y-1 bg-emerald-950/60 border-emerald-500/50 text-emerald-200">
              <strong class="font-bold text-emerald-300 flex items-center gap-1.5">
                <span>✓ आदर्श अवस्था (६०-६५% चिस्यान)</span>
              </strong>
              <p>
                हातले बेस्सरी निचोर्दा औँलाको कापबाट पानीका थोपा नचुहिने तर हातको हत्केला राम्रोसँग भिज्ने अवस्था। च्याउको बीउ (माइसेलियम) तीब्र गतिमा फैलिनका लागि यो सर्वोत्तम हो।
              </p>
            </div>

            <!-- Scientific Tip -->
            <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-700 text-xs text-slate-400">
              <strong class="text-amber-400 block mb-0.5">💡 किसान वैज्ञानिक सुझाव:</strong>
              पराल उसिनेपछि अनिवार्य रूपमा छायाँमा सफा प्लास्टिकमा सेलाउनुपर्छ। तातो परालमा बीउ हालेमा ढुसीका कोषहरू तापले मर्छन्।
            </div>
          </div>
        </div>
      </div>

      <!-- ================= MODE 3: POISONOUS MUSHROOM IDENTIFIER & SAFETY ================= -->
      <div id="c9u3-lab-mode-safety" class="hidden space-y-6">
        <!-- Specimen Selector Buttons -->
        <div class="flex flex-wrap gap-2 justify-center" id="c9u3-specimen-buttons">
          <!-- Rendered by JS -->
        </div>

        <!-- Specimen Inspection Card -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          <!-- Visual & Safety Audit Checklist -->
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                <div>
                  <span class="text-xs font-mono text-slate-400" id="c9u3-spec-sciname">Pleurotus ostreatus</span>
                  <h4 class="text-xl md:text-2xl font-black text-white" id="c9u3-spec-nepname">कन्ने च्याउ (Oyster Mushroom)</h4>
                </div>
                <span class="text-xs px-3 py-1 rounded-full font-bold border" id="c9u3-spec-verdict-badge">
                  खानयोग्य (सुरक्षित)
                </span>
              </div>

              <!-- Safety Characteristics Grid -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-800">
                  <span class="text-slate-400 block">भल्भा (Volva - फेदको कचौरा):</span>
                  <strong class="text-white text-sm" id="c9u3-spec-volva">छैन (Absent)</strong>
                </div>
                <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-800">
                  <span class="text-slate-400 block">एनुलस (Annulus - डाँठको औँठी):</span>
                  <strong class="text-white text-sm" id="c9u3-spec-annulus">छैन (Absent)</strong>
                </div>
                <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-800">
                  <span class="text-slate-400 block">पाइलसको रंग र सतह:</span>
                  <strong class="text-white text-sm" id="c9u3-spec-cap">हल्का खैरो वा सेतो, चिल्लो</strong>
                </div>
                <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-800">
                  <span class="text-slate-400 block">काट्दा रंग परिवर्तन (Bruising):</span>
                  <strong class="text-white text-sm" id="c9u3-spec-bruise">हुँदैन (स्थिर)</strong>
                </div>
              </div>
            </div>

            <!-- Detailed Scientific Profile -->
            <div class="bg-slate-900/90 p-3.5 rounded-2xl border border-slate-800 text-xs md:text-sm text-slate-300">
              <strong class="text-emerald-400 block mb-1">वैज्ञानिक विश्लेषण तथा उपयोगिता:</strong>
              <p id="c9u3-spec-analysis" class="leading-relaxed">
                नेपालमा व्यावसायिक रूपमा सबैभन्दा धेरै उत्पादन हुने खानयोग्य च्याउ हो। यसमा उच्च प्रोटिन र खनिज हुन्छ।
              </p>
            </div>
          </div>

          <!-- Myth Buster & Safety Rules -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-3">
            <div class="border-b border-slate-700/80 pb-2">
              <span class="text-xs text-rose-400 font-mono">SCIENTIFIC FACT-CHECKER</span>
              <h4 class="text-lg font-black text-white">⚠️ विषालु च्याउका ३ घातक अन्धविश्वास</h4>
            </div>

            <!-- Myth 1 -->
            <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700 space-y-1 text-xs">
              <div class="flex items-center gap-1.5 text-rose-400 font-bold">
                <span>❌ भ्रम १:</span> चाँदीको चम्चा कालो नभए च्याउ विषालु हुँदैन।
              </div>
              <div class="text-emerald-300 pl-4 border-l-2 border-emerald-500 text-[11px] leading-relaxed">
                <strong>वैज्ञानिक सत्य:</strong> चाँदी कालो हुनु सल्फरसँगको प्रतिक्रिया मात्र हो। डेथ क्याप (<em>Amanita</em>) को घातक विष (Amatoxin) ले चाँदी कहिल्यै कालो बनाउँदैन!
              </div>
            </div>

            <!-- Myth 2 -->
            <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700 space-y-1 text-xs">
              <div class="flex items-center gap-1.5 text-rose-400 font-bold">
                <span>❌ भ्रम २:</span> टिमुर, लसुन वा खुर्सानी हालेर पकाउँदा विष नष्ट हुन्छ।
              </div>
              <div class="text-emerald-300 pl-4 border-l-2 border-emerald-500 text-[11px] leading-relaxed">
                <strong>वैज्ञानिक सत्य:</strong> च्याउका प्राणघातक विषहरू ताप र मसलाले नष्ट हुन नसक्ने रासायनिक यौगिक हुन्।
              </div>
            </div>

            <!-- Myth 3 -->
            <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700 space-y-1 text-xs">
              <div class="flex items-center gap-1.5 text-rose-400 font-bold">
                <span>❌ भ्रम ३:</span> कीरा वा जनावरले खाएको च्याउ मानिसका लागि पनि सुरक्षित हुन्छ।
              </div>
              <div class="text-emerald-300 pl-4 border-l-2 border-emerald-500 text-[11px] leading-relaxed">
                <strong>वैज्ञानिक सत्य:</strong> शंखेकिरा, झुसिल्किरा र जंगली जनावरको इन्जाइम प्रणाली मानिसभन्दा फरक हुन्छ; उनीहरूलाई असर नगर्ने च्याउले मानिसको कलेजो फेल गराउन सक्छ।
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= TAB 2: EXERCISES ================= -->
  <div id="c9u3-view-exercises" class="hidden space-y-6">
    <!-- Category Filter Bar -->
    <div class="flex items-center justify-between border-b border-slate-200 pb-3 flex-wrap gap-2">
      <div class="text-xs font-bold text-slate-500">
        प्रश्न प्रकार अनुसार छान्नुहोस्:
      </div>
      <div class="flex flex-wrap gap-1.5">
        <button onclick="filterC9U3Exercises('all')" id="c9u3-exbtn-all" class="px-3 py-1.5 rounded-xl text-xs font-black transition bg-emerald-600 text-white shadow-sm cursor-pointer whitespace-nowrap">
          सबै अभ्यास
        </button>
        <button onclick="filterC9U3Exercises('mcq')" id="c9u3-exbtn-mcq" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          १. बहुवैकल्पिक (MCQs)
        </button>
        <button onclick="filterC9U3Exercises('reason')" id="c9u3-exbtn-reason" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          २. कारण दिनुहोस्
        </button>
        <button onclick="filterC9U3Exercises('diff')" id="c9u3-exbtn-diff" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          ३. फरक लेख्नुहोस्
        </button>
        <button onclick="filterC9U3Exercises('qa')" id="c9u3-exbtn-qa" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          ४. विस्तृत प्रश्नोत्तर
        </button>
        <button onclick="filterC9U3Exercises('project')" id="c9u3-exbtn-project" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          परियोजना कार्यहरू
        </button>
      </div>
    </div>

    <!-- Exercise Items Container -->
    <div class="space-y-6" id="c9u3-exercises-list">
      <!-- (Rendered static HTML cards with category classes for filtering) -->
"""

print("HTML base written.")
