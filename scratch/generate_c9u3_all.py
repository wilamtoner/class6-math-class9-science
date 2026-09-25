# -*- coding: utf-8 -*-
"""
Class 9 Science Unit 3: च्याउ (Mushroom)
Generates:
  1. scratch/c9u3_html.html
  2. scratch/c9u3_js.js
"""
import json
import re

html_path = "scratch/c9u3_html.html"
js_path = "scratch/c9u3_js.js"

print("Compiling Unit 3 HTML & JS...")

# =========================================================================
# TAB 1: CONCEPTS & VIRTUAL MUSHROOM LAB
# =========================================================================
tab1_html = """<!-- ================= CLASS 9 UNIT 3 CONTAINER ================= -->
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
        च्याउको बाह्य र सूक्ष्म गिल्स बनोट, जीवन चक्र (Life Cycle), कन्ने च्याउ खेती प्रविधि र विषालु च्याउ पहिचान
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
            <strong>२. सब-हाइमेनियम (Sub-hymenium):</strong> ट्रामा र हाइमेनियम बीचको साना गोलाकार कोषहरूको मध्य तह।
          </div>
          <div class="bg-white/80 p-2 rounded-xl border border-indigo-100">
            <strong>३. हाइमेनियम (Hymenium):</strong> सबैभन्दा बाहिरी उर्वर तह जसमा <strong>बेसिडियम</strong> (उर्वर कोष, ४ बेसिडियोस्पोर बनाउने) र <strong>प्याराफाइसिस</strong> (बन्ध्या कोष, सहारा दिने) हुन्छन्।
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
                <line x1="200" y1="40" x2="200" y2="340" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,2"/>
                <line x1="215" y1="40" x2="215" y2="340" stroke="#cbd5e1" stroke-width="1.5"/>
                <line x1="230" y1="40" x2="230" y2="340" stroke="#cbd5e1" stroke-width="1.5"/>
                <line x1="245" y1="40" x2="245" y2="340" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,2"/>
                <text x="225" y="195" fill="#f8fafc" font-size="12" font-weight="black" text-anchor="middle">ट्रामा (TRAMA)</text>
              </g>

              <!-- Sub-hymenium Layer (Left & Right) -->
              <g id="svg-part-subhymenium" onclick="selectIntPartC9U3('subhymenium')" class="cursor-pointer transition hover:opacity-90">
                <rect x="135" y="40" width="45" height="300" rx="4" fill="url(#c9u3-subhymen-grad)" stroke="#0284c7" stroke-width="1.5"/>
                <rect x="270" y="40" width="45" height="300" rx="4" fill="url(#c9u3-subhymen-grad)" stroke="#0284c7" stroke-width="1.5"/>
                <circle cx="155" cy="80" r="5" fill="#bae6fd"/>
                <circle cx="160" cy="140" r="6" fill="#bae6fd"/>
                <circle cx="150" cy="200" r="5" fill="#bae6fd"/>
                <circle cx="160" cy="260" r="6" fill="#bae6fd"/>
                <circle cx="295" cy="80" r="5" fill="#bae6fd"/>
                <circle cx="290" cy="140" r="6" fill="#bae6fd"/>
                <circle cx="300" cy="200" r="5" fill="#bae6fd"/>
                <circle cx="290" cy="260" r="6" fill="#bae6fd"/>
              </g>

              <!-- Hymenium Layer: Paraphysis -->
              <g id="svg-part-paraphysis" onclick="selectIntPartC9U3('paraphysis')" class="cursor-pointer transition hover:opacity-90">
                <rect x="85" y="60" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="85" y="150" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="85" y="240" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="315" y="60" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="315" y="150" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
                <rect x="315" y="240" width="50" height="22" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
              </g>

              <!-- Hymenium Layer: Basidium -->
              <g id="svg-part-basidium" onclick="selectIntPartC9U3('basidium')" class="cursor-pointer transition hover:opacity-90">
                <!-- Left Basidium at y=100 -->
                <path d="M 135,95 L 85,90 C 70,85 55,95 55,107 C 55,119 70,129 85,124 L 135,119 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
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
                <ellipse cx="28" cy="88" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="22" cy="101" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="22" cy="113" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="28" cy="126" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>

                <ellipse cx="422" cy="88" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="428" cy="101" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="428" cy="113" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                <ellipse cx="422" cy="126" rx="6" ry="5" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
              </g>

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
        <div class="flex items-center justify-between border-b border-slate-800 pb-3 flex-wrap gap-2">
          <div class="text-xs font-bold text-slate-400">
            कन्ने च्याउ खेतीका ६ व्यावहारिक चरणहरू:
          </div>
          <div class="flex gap-1.5 overflow-x-auto pb-1" id="c9u3-farming-stepper">
            <!-- Rendered by JS -->
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
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

            <div class="flex items-center justify-between pt-4 border-t border-slate-800">
              <button onclick="prevFarmStageC9U3()" id="c9u3-farm-prev-btn" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition cursor-pointer">
                ← अघिल्लो चरण
              </button>
              <button onclick="nextFarmStageC9U3()" id="c9u3-farm-next-btn" class="px-5 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white shadow-sm transition cursor-pointer">
                अर्को चरण →
              </button>
            </div>
          </div>

          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-4">
            <div class="border-b border-slate-700/80 pb-3">
              <span class="text-xs text-amber-400 font-mono">CRITICAL SUCCESS FACTOR</span>
              <h4 class="text-lg font-black text-white">💧 परालको चिस्यान परीक्षण (Moisture Squeeze Test)</h4>
            </div>

            <p class="text-xs text-slate-300 leading-relaxed">
              च्याउ खेती असफल हुने ९०% कारण परालमा गलत चिस्यान हुनु हो। हातको मुठ्ठीमा उसिनेको पराल बेस्सरी निचोरेर परीक्षण गरिन्छ।
            </p>

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

            <div id="c9u3-moisture-feedback" class="p-3.5 rounded-2xl border text-xs leading-relaxed space-y-1 bg-emerald-950/60 border-emerald-500/50 text-emerald-200">
              <strong class="font-bold text-emerald-300 flex items-center gap-1.5">
                <span>✓ आदर्श अवस्था (६०-६५% चिस्यान)</span>
              </strong>
              <p>
                हातले बेस्सरी निचोर्दा औँलाको कापबाट पानीका थोपा नचुहिने तर हातको हत्केला राम्रोसँग भिज्ने अवस्था। च्याउको बीउ (माइसेलियम) तीब्र गतिमा फैलिनका लागि यो सर्वोत्तम हो।
              </p>
            </div>

            <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-700 text-xs text-slate-400">
              <strong class="text-amber-400 block mb-0.5">💡 किसान वैज्ञानिक सुझाव:</strong>
              पराल उसिनेपछि अनिवार्य रूपमा छायाँमा सफा प्लास्टिकमा सेलाउनुपर्छ। तातो परालमा बीउ हालेमा ढुसीका कोषहरू तापले मर्छन्।
            </div>
          </div>
        </div>
      </div>

      <!-- ================= MODE 3: POISONOUS MUSHROOM IDENTIFIER & SAFETY ================= -->
      <div id="c9u3-lab-mode-safety" class="hidden space-y-6">
        <div class="flex flex-wrap gap-2 justify-center" id="c9u3-specimen-buttons">
          <!-- Rendered by JS -->
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
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

            <div class="bg-slate-900/90 p-3.5 rounded-2xl border border-slate-800 text-xs md:text-sm text-slate-300">
              <strong class="text-emerald-400 block mb-1">वैज्ञानिक विश्लेषण तथा उपयोगिता:</strong>
              <p id="c9u3-spec-analysis" class="leading-relaxed">
                नेपालमा व्यावसायिक रूपमा सबैभन्दा धेरै उत्पादन हुने खानयोग्य च्याउ हो। यसमा उच्च प्रोटिन र खनिज हुन्छ।
              </p>
            </div>
          </div>

          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 space-y-3">
            <div class="border-b border-slate-700/80 pb-2">
              <span class="text-xs text-rose-400 font-mono">SCIENTIFIC FACT-CHECKER</span>
              <h4 class="text-lg font-black text-white">⚠️ विषालु च्याउका ३ घातक अन्धविश्वास</h4>
            </div>

            <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700 space-y-1 text-xs">
              <div class="flex items-center gap-1.5 text-rose-400 font-bold">
                <span>❌ भ्रम १:</span> चाँदीको चम्चा कालो नभए च्याउ विषालु हुँदैन।
              </div>
              <div class="text-emerald-300 pl-4 border-l-2 border-emerald-500 text-[11px] leading-relaxed">
                <strong>वैज्ञानिक सत्य:</strong> चाँदी कालो हुनु सल्फरसँगको प्रतिक्रिया मात्र हो। डेथ क्याप (<em>Amanita</em>) को घातक विष (Amatoxin) ले चाँदी कहिल्यै कालो बनाउँदैन!
              </div>
            </div>

            <div class="bg-slate-900/80 p-3 rounded-2xl border border-slate-700 space-y-1 text-xs">
              <div class="flex items-center gap-1.5 text-rose-400 font-bold">
                <span>❌ भ्रम २:</span> टिमुर, लसुन वा खुर्सानी हालेर पकाउँदा विष नष्ट हुन्छ।
              </div>
              <div class="text-emerald-300 pl-4 border-l-2 border-emerald-500 text-[11px] leading-relaxed">
                <strong>वैज्ञानिक सत्य:</strong> च्याउका प्राणघातक विषहरू ताप र मसलाले नष्ट हुन नसक्ने रासायनिक यौगिक हुन्।
              </div>
            </div>

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
"""

print("Tab 1 generated.")

# =========================================================================
# TAB 2: EXERCISES
# =========================================================================
tab2_html = """  <!-- ================= TAB 2: EXERCISES ================= -->
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

    <!-- Exercise Cards Container -->
    <div class="space-y-6">

      <!-- ================= 1. MCQS ================= -->
      <div class="c9u3-ex-card" data-cat="mcq">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center text-xs font-black">१</span>
              <span>तल दिइएका प्रश्नहरूको सही उत्तरमा ठीक चिह्न (✓) लगाउनुहोस् (MCQs):</span>
            </h3>
            <span class="text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold px-2.5 py-0.5 rounded-full">वस्तुगत प्रश्न</span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            
            <!-- MCQ 1 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200/80 space-y-2">
              <div class="text-xs font-bold text-slate-800">
                (क) च्याउलाई मृतोपजीवी (saprotrophic) जीव भन्नुको कारण कुन हो ?
              </div>
              <div class="grid grid-cols-2 gap-1.5 text-xs">
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(अ) यसले आफ्नो खाना आफैँ बनाउन सक्दैन ।</div>
                <div class="p-2 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-900 font-bold flex items-center gap-1.5">
                  <span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[10px]">✓</span>
                  <span>(आ) सडेगलेका वस्तुबाट खाना लिन्छ ।</span>
                </div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(इ) आफ्नो खानाका लागि अरूमा भर पर्छ ।</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(ई) जीवको शरीरबाट खाना सोसेर लिन्छ ।</div>
              </div>
              <p class="text-[11px] text-slate-500 bg-white p-2 rounded-xl border border-slate-100">
                💡 <strong>कारण:</strong> च्याउमा हरितकण नहुने भएकाले गोबर, पराल र सडेगलेका जैविक वस्तुबाट बाह्य पाचन गरी पोषण लिने हुनाले यसलाई मृतोपजीवी भनिन्छ।
              </p>
            </div>

            <!-- MCQ 2 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200/80 space-y-2">
              <div class="text-xs font-bold text-slate-800">
                (ख) च्याउमा पाइने मुख्य तत्त्व के के हुन् ?
              </div>
              <div class="grid grid-cols-2 gap-1.5 text-xs">
                <div class="p-2 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-900 font-bold flex items-center gap-1.5">
                  <span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[10px]">✓</span>
                  <span>(अ) खनिज, भिटामिन, प्रोटिन</span>
                </div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(आ) सोडियम, कार्बोहाइड्रेट र प्रोटिन</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(इ) एमिनो एसिड, भिटामिन र प्रोटिन</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(ई) क्याल्सियम, चिल्लो र खनिज</div>
              </div>
              <p class="text-[11px] text-slate-500 bg-white p-2 rounded-xl border border-slate-100">
                💡 <strong>कारण:</strong> च्याउमा करिब २०-३५% प्रोटिन, भिटामिन डी र बी-कम्प्लेक्स तथा पोटासियम/फलाम जस्ता खनिज प्रचुर मात्रामा पाइन्छन्।
              </p>
            </div>

            <!-- MCQ 3 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200/80 space-y-2">
              <div class="text-xs font-bold text-slate-800">
                (ग) कुन च्याउबाट क्यान्सर रोगका उपचारका लागि औषधि बनाइन्छ ?
              </div>
              <div class="grid grid-cols-2 gap-1.5 text-xs">
                <div class="p-2 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-900 font-bold flex items-center gap-1.5">
                  <span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[10px]">✓</span>
                  <span>(अ) रातो च्याउ (Ganoderma)</span>
                </div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(आ) डल्ले च्याउ</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(इ) कन्ने च्याउ</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(ई) गोब्रे च्याउ</div>
              </div>
              <p class="text-[11px] text-slate-500 bg-white p-2 rounded-xl border border-slate-100">
                💡 <strong>कारण:</strong> रातो च्याउ (<em>Ganoderma lucidum</em>) मा पोलिस्याकराइड्स र ट्राइटरपेन्स पाइने भएकाले यसबाट क्यान्सर प्रतिरोधी औषधि बनाइन्छ।
              </p>
            </div>

            <!-- MCQ 4 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200/80 space-y-2">
              <div class="text-xs font-bold text-slate-800">
                (घ) हाइमेनियममा भएको स्टेराइल (sterile) कोष कुन हो ?
              </div>
              <div class="grid grid-cols-2 gap-1.5 text-xs">
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(अ) बेसिडियम</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(आ) बेसिडियोस्पोर</div>
                <div class="p-2 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-900 font-bold flex items-center gap-1.5">
                  <span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[10px]">✓</span>
                  <span>(इ) प्याराफाइसिस</span>
                </div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(ई) स्टिरिग्मा</div>
              </div>
              <p class="text-[11px] text-slate-500 bg-white p-2 rounded-xl border border-slate-100">
                💡 <strong>कारण:</strong> प्याराफाइसिस (Paraphysis) बन्ध्या (sterile) कोष हो जसले बीजाणु बनाउँदैन तर बेसिडियमलाई सहारा र ओसिलोपन दिन्छ।
              </p>
            </div>

            <!-- MCQ 5 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200/80 space-y-2 md:col-span-2">
              <div class="text-xs font-bold text-slate-800">
                (ङ) बेसिडियोस्पोर (Basidiospore) कहाँ बन्दछ ?
              </div>
              <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 text-xs">
                <div class="p-2 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-900 font-bold flex items-center gap-1.5">
                  <span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[10px]">✓</span>
                  <span>(अ) हाइमेनियम</span>
                </div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(आ) सब-हाइमेनियम</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(इ) ट्रामा</div>
                <div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">(ई) माइसेलियम</div>
              </div>
              <p class="text-[11px] text-slate-500 bg-white p-2 rounded-xl border border-slate-100">
                💡 <strong>कारण:</strong> गिल्सको सबैभन्दा बाहिरी उर्वर तह हाइमेनियम (Hymenium) हो, जहाँ बेसिडियमको टुप्पोमा ४ ओटा बेसिडियोस्पोर बन्दछन्।
              </p>
            </div>

          </div>
        </div>
      </div>

      <!-- ================= 2. REASONS ================= -->
      <div class="c9u3-ex-card" data-cat="reason">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-xs font-black">२</span>
              <span>कारण दिनुहोस् (Give reasons):</span>
            </h3>
            <span class="text-xs bg-amber-50 text-amber-700 border border-amber-200 font-bold px-2.5 py-0.5 rounded-full">कारण खुलाउने</span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            
            <!-- Reason 1 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-amber-900">
                (क) च्याउलाई हरितकणविहीन मृतोपजीवी भनिन्छ, किन ?
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3 rounded-xl border border-slate-200">
                <strong>उत्तर:</strong> च्याउका कोषहरूमा बिरुवामा जस्तो हरितकण (Chlorophyll) हुँदैन, जसले गर्दा यसले प्रकाश-संश्लेषण मार्फत आफ्नो खाना आफैँ बनाउन सक्दैन। यसले गोबर, पराल, काठका मुढा र सडेगलेका जैविक वस्तुहरूमा पाचन रस निष्कासन गरी बाह्य पाचन मार्फत तरल रूपमा पोषक तत्व सोसेर लिने भएकाले च्याउलाई <strong>हरितकणविहीन मृतोपजीवी (Non-chlorophyllous saprotroph)</strong> भनिन्छ।
              </div>
            </div>

            <!-- Reason 2 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-amber-900">
                (ख) च्याउको खेती गर्दा पराललाई राम्ररी उसिन्नुपर्छ, किन ?
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3 rounded-xl border border-slate-200">
                <strong>उत्तर:</strong> सुख्खा परालमा विभिन्न प्रकारका हानिकारक जंगली ढुसीका बीजाणुहरू, हानिकारक ब्याक्टेरिया र कीराका अण्डाहरू टाँसिएका हुन सक्छन्। यदि पराललाई नउसिनी बीउ रोपियो भने ती प्रतिस्पर्धी ढुसी र ब्याक्टेरिया मौलाएर च्याउको माइसेलियमलाई नष्ट गर्छन् र बाली कुहिएर पूरै खेर जान्छ। त्यसैले पराललाई पूर्णतया <strong>जीवाणुरहित (Sterilize)</strong> बनाई च्याउको बीउलाई अनुकूल वातावरण दिन पराललाई १-२ घण्टा राम्ररी उसिन्नुपर्छ।
              </div>
            </div>

            <!-- Reason 3 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-amber-900">
                (ग) च्याउलाई प्रोटिनको राम्रो स्रोत मानिन्छ, किन ?
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3 rounded-xl border border-slate-200">
                <strong>उत्तर:</strong> सुख्खा च्याउमा करिब २० देखि ३५ प्रतिशतसम्म उच्च गुणस्तरको सुपाच्य प्रोटिन पाइन्छ, जसमा मानव शरीरलाई आवश्यक पर्ने सम्पूर्ण अत्यावश्यक एमिनो एसिडहरू (Essential amino acids) सन्तुलित रूपमा पाइन्छन्। यसमा मासुको जस्तो हानिकारक कोलेस्टेरोल र अत्यधिक चिल्लो पदार्थ नहुने भएकाले च्याउलाई प्रोटिनको अत्यन्तै स्वस्थ र उत्तम स्रोत मानिन्छ।
              </div>
            </div>

            <!-- Reason 4 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-amber-900">
                (घ) जंगलमा पाइने सबै प्रकारका च्याउ खानुहुँदैन, किन ?
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3 rounded-xl border border-slate-200">
                <strong>उत्तर:</strong> जंगलमा प्राकृतिक रूपमा उम्रने धेरैजसो च्याउहरू (जस्तै: <em>Amanita phalloides</em>) मा 'अमानिटिन' र 'म्युस्कारिन' जस्ता घातक विषहरू हुन्छन्। यस्ता विषालु च्याउ खाँदा कलेजो, मिर्गौला र स्नायु प्रणाली फेल भई केही घण्टामै मानिसको मृत्यु हुन सक्छ। सामान्य आँखाले हेर्दा विषालु र खानयोग्य च्याउ उस्तै देखिने भएकाले नचिनिएका जंगली च्याउ खानुहुँदैन।
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- ================= 3. DIFFERENCES ================= -->
      <div class="c9u3-ex-card" data-cat="diff">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-black">३</span>
              <span>फरक छुट्याउनुहोस् (Distinguish between):</span>
            </h3>
            <span class="text-xs bg-purple-50 text-purple-700 border border-purple-200 font-bold px-2.5 py-0.5 rounded-full">तुलनात्मक तालिका</span>
          </div>

          <div class="space-y-4">
            
            <!-- Diff 1 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-purple-900">(क) खानयोग्य च्याउ र विषालु च्याउ</h4>
              <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border border-slate-200 bg-white rounded-xl">
                  <thead class="bg-slate-100 text-slate-700 font-bold">
                    <tr><th class="p-2 border-b">आधार</th><th class="p-2 border-b">खानयोग्य च्याउ (Edible Mushroom)</th><th class="p-2 border-b">विषालु च्याउ (Poisonous Mushroom)</th></tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 text-slate-600">
                    <tr><td class="p-2 font-semibold">१. शारीरिक विष</td><td class="p-2">यसमा मानिसलाई हानी पुर्‍याउने कुनै विषाक्त तत्व हुँदैन।</td><td class="p-2">यसमा अमानिटिन, फ्यालोइडिन जस्ता घातक विषहरू हुन्छन्।</td></tr>
                    <tr><td class="p-2 font-semibold">२. भल्भा र एनुलस</td><td class="p-2">डाँठको फेदमा भल्भा (कचौरा) हुँदैन (अपवाद बाहेक)।</td><td class="p-2">प्रायः डाँठको फेदमा भल्भा र डाँठमा एनुलस दुवै पाइन्छन्।</td></tr>
                    <tr><td class="p-2 font-semibold">३. रंग र गन्ध</td><td class="p-2">प्रायः फिक्का, सेतो वा खैरो हुन्छ; मिठो सुगन्ध आउँछ।</td><td class="p-2">चहकिलो, गाढा आकर्षक रंगको हुन सक्छ र तिखो नमिठो गन्ध आउँछ।</td></tr>
                    <tr><td class="p-2 font-semibold">४. उदाहरणहरू</td><td class="p-2">कन्ने च्याउ, डल्ले च्याउ, गोब्रे च्याउ, सिताके च्याउ।</td><td class="p-2">डेथ क्याप (<em>Amanita phalloides</em>), फ्लाई एगारिक।</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Diff 2 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-purple-900">(ख) प्राथमिक माइसेलियम र दोस्रो माइसेलियम</h4>
              <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border border-slate-200 bg-white rounded-xl">
                  <thead class="bg-slate-100 text-slate-700 font-bold">
                    <tr><th class="p-2 border-b">आधार</th><th class="p-2 border-b">प्राथमिक माइसेलियम (Primary Mycelium)</th><th class="p-2 border-b">दोस्रो माइसेलियम (Secondary Mycelium)</th></tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 text-slate-600">
                    <tr><td class="p-2 font-semibold">१. कोषीय अवस्था</td><td class="p-2">मोनोक्यारियोटिक (Monokaryotic) - प्रत्येक कोषमा एउटा मात्र अगुणित (n) न्युक्लियस हुन्छ।</td><td class="p-2">डिक्यारियोटिक (Dikaryotic) - प्रत्येक कोषमा दुईओटा अगुणित (n + n) न्युक्लियसहरू हुन्छन्।</td></tr>
                    <tr><td class="p-2 font-semibold">२. उत्पत्ति</td><td class="p-2">बेसिडियोस्पोर (Basidiospore) को प्रत्यक्ष अंकुरणबाट बन्दछ।</td><td class="p-2">दुई विपरित स्ट्रेनका (+ र -) प्राथमिक माइसेलियम मिसिएर (Plasmogamy भई) बन्दछ।</td></tr>
                    <tr><td class="p-2 font-semibold">३. फ्रुटिङ बडी निर्माण</td><td class="p-2">यसले एक्लै च्याउ (Fruiting body) बनाउन सक्दैन।</td><td class="p-2">यसले विकसित भएर छाता आकारको च्याउ (Fruiting body) बनाउँछ।</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Diff 3 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-purple-900">(ग) प्याराफाइसिस र बेसिडियम</h4>
              <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border border-slate-200 bg-white rounded-xl">
                  <thead class="bg-slate-100 text-slate-700 font-bold">
                    <tr><th class="p-2 border-b">आधार</th><th class="p-2 border-b">प्याराफाइसिस (Paraphysis)</th><th class="p-2 border-b">बेसिडियम (Basidium)</th></tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 text-slate-600">
                    <tr><td class="p-2 font-semibold">१. कोषको प्रकार</td><td class="p-2">बन्ध्या (Sterile) कोष हो।</td><td class="p-2">उर्वर (Fertile) प्रजनन कोष हो।</td></tr>
                    <tr><td class="p-2 font-semibold">२. बीजाणु उत्पादन</td><td class="p-2">यसले कुनै पनि बीजाणु (स्पोर) उत्पादन गर्दैन।</td><td class="p-2">यसको टुप्पोमा ४ ओटा बेसिडियोस्पोरहरू बन्दछन्।</td></tr>
                    <tr><td class="p-2 font-semibold">३. आकार र कार्य</td><td class="p-2">पातलो खम्बा आकारको हुन्छ; बेसिडियमलाई सहारा, ओसिलोपन र सुरक्षा दिन्छ।</td><td class="p-2">फुकेको गदा (club-shaped) आकारको हुन्छ; लैंगिक प्रजनन र बीजाणु फैलाउने कार्य गर्छ।</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- ================= 4. DETAILED Q&A ================= -->
      <div class="c9u3-ex-card" data-cat="qa">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-5">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-black">४</span>
              <span>तलका प्रश्नहरूको विस्तृत उत्तर लेख्नुहोस् (Detailed Q&A):</span>
            </h3>
            <span class="text-xs bg-blue-50 text-blue-700 border border-blue-200 font-bold px-2.5 py-0.5 rounded-full">११ विस्तृत प्रश्नोत्तर</span>
          </div>

          <div class="space-y-4">

            <!-- Q4 (a) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(क)</span>
                <span>च्याउको पौष्टिक महत्त्व उल्लेख गर्नुहोस् ।</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-1.5">
                <p><strong>उत्तर:</strong> च्याउ मानव शरीरका लागि अत्यावश्यक पोषक तत्वहरूले भरिपूर्ण एक अत्यन्तै पोषिलो आहार हो। यसका प्रमुख पौष्टिक महत्त्वहरू निम्न छन्:</p>
                <ol class="list-decimal pl-5 space-y-1">
                  <li><strong>उच्च गुणस्तरको प्रोटिन:</strong> सुकेको च्याउमा २० देखि ३५ प्रतिशतसम्म सुपाच्य प्रोटिन पाइन्छ, जसमा शरीरलाई चाहिने सबै अत्यावश्यक एमिनो एसिडहरू समावेश हुन्छन्।</li>
                  <li><strong>भिटामिनको प्रचुरता:</strong> यसमा भिटामिन बी-कम्प्लेक्स (थायमिन, राइबोफ्लेभिन, नियासिन) र प्राकृतिक भिटामिन 'डी' प्रशस्त मात्रामा पाइन्छ।</li>
                  <li><strong>खनिज तत्वहरूको भण्डार:</strong> यसमा पोटासियम, फस्फोरस, क्याल्सियम, तामा, सेलेनियम र फलाम जस्ता शरीर निर्माण गर्ने खनिजहरू हुन्छन्।</li>
                  <li><strong>कम चिल्लो र शून्य कोलेस्टेरोल:</strong> च्याउमा चिल्लो पदार्थ १ प्रतिशतभन्दा कम हुने र कोलेस्टेरोल शून्य हुने भएकाले यो मुटुरोग, उच्च रक्तचाप र मधुमेहका बिरामीका लागि उत्तम आहार हो।</li>
                </ol>
              </div>
            </div>

            <!-- Q4 (b) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(ख)</span>
                <span>च्याउको औषधीय महत्त्व प्रस्ट पार्नुहोस् ।</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-1.5">
                <p><strong>उत्तर:</strong> विभिन्न प्रजातिका च्याउहरूमा रोग निको पार्ने र शरीरको प्रतिरोधात्मक क्षमता बढाउने विशिष्ट औषधीय गुणहरू हुन्छन्:</p>
                <ul class="list-disc pl-5 space-y-1">
                  <li><strong>क्यान्सर प्रतिरोधी गुण:</strong> रातो च्याउ (<em>Ganoderma lucidum</em>) र सिताके च्याउमा पाइने 'बिटा-ग्लुकान' र 'पोलिस्याकराइड्स' ले क्यान्सर कोषहरूको अनियन्त्रित वृद्धिलाई रोक्दछन्।</li>
                  <li><strong>रोग प्रतिरोधात्मक क्षमता (Immunity):</strong> च्याउको नियमित सेवनले शरीरको सेतो रक्तकोषहरूलाई सक्रिय बनाई भाइरस र ब्याक्टेरियाविरुद्ध लड्ने क्षमता बढाउँछ।</li>
                  <li><strong>मुटु र रक्तचाप नियन्त्रण:</strong> च्याउमा सोडियम न्यून र पोटासियम उच्च हुने भएकाले रक्तचाप सन्तुलनमा राख्न र धमनीमा रगत जम्न नदिन सहयोग पुर्‍याउँछ।</li>
                  <li><strong>एन्टिअक्सिडेन्ट गुण:</strong> यसमा हुने सेलेनियम र अर्गोथायोनिनले शरीरका कोषहरूलाई बुढ्यौली र विषाक्त असरबाट जोगाउँछन्।</li>
                </ul>
              </div>
            </div>

            <!-- Q4 (c) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(ग)</span>
                <span>च्याउ खेतीले मानिसको स्वास्थ्य र आयआर्जनमा कसरी सहयोग पुर्‍याउँछ ?</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                <div>
                  <strong class="text-emerald-700 block">१. स्वास्थ्यमा सहयोग:</strong>
                  कुपोषण हटाउन, प्रोटिनको आपूर्ति गर्न, र मुटु, मधुमेह तथा रक्तचाप जस्ता नसर्ने रोगहरूबाट बच्न मद्दत गर्दछ।
                </div>
                <div>
                  <strong class="text-blue-700 block">२. आयआर्जनमा सहयोग:</strong>
                  च्याउ खेतीका लागि धेरै जग्गा जमिन चाहिन्न; घरको सानो कोठा वा छाप्रोमा खेर गइरहेको पराल प्रयोग गरी थोरै लगानीमा सुरु गर्न सकिन्छ। बीउ रोपेको ३-४ हप्तामै उत्पादन सुरु भई किसानले दैनिक नगद आम्दानी प्राप्त गर्न सक्छन्। यसले ग्रामीण महिला, युवा र बेरोजगार नागरिकलाई स्वरोजगार बनाई गरिबी निवारणमा ठूलो सहयोग पुर्‍याउँछ।
                </div>
              </div>
            </div>

            <!-- Q4 (d) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(घ)</span>
                <span>कन्ने च्याउ खेती गर्ने तरिका छोटकरीमा वर्णन गर्नुहोस् ।</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-1.5">
                <p><strong>उत्तर:</strong> कन्ने च्याउ (<em>Pleurotus ostreatus</em>) खेती गर्ने मुख्य ६ चरणहरू निम्न छन्:</p>
                <ol class="list-decimal pl-5 space-y-1">
                  <li><strong>पराल काट्ने:</strong> ताजा सफा पराललाई हँसिया वा मेसिनले २ देखि ३ इन्च लामा टुक्राहरूमा काट्ने।</li>
                  <li><strong>पराल भिजाउने र उसिन्ने:</strong> काटेको पराललाई १०-१२ घण्टा पानीमा भिजाउने र ड्रममा हालेर बाफमा १-२ घण्टा उसिनेर जीवाणुरहित बनाउने।</li>
                  <li><strong>पराल सेलाउने र चिस्यान नियन्त्रण:</strong> उसिनेको पराललाई सफा प्लास्टिकमा सेलाउने; हातले बेस्सरी निचोर्दा पानी नचुहिने तर हात भिज्ने (६०-६५% चिस्यान) बनाउने।</li>
                  <li><strong>बीउ मिसाउने र पोका पार्ने:</strong> पोलिथिन झोलामा पराल र च्याउको बीउ तह-तह गरी भर्ने, मुख कसिलो बाँध्ने र १०-१५ साना प्वालहरू पार्ने।</li>
                  <li><strong>ओथारो (Incubation):** पोकाहरूलाई २०-२५°C तापक्रम भएको अँध्यारो कोठामा १५-२० दिन राख्ने, जबसम्म सेतो ढुसी (माइसेलियम) पूरै फैलिँदैन।</li>
                  <li><strong>झोला खोल्ने र च्याउ टिप्ने:</strong> माइसेलियम फैलिएपछि प्लास्टिक हटाउने वा प्वाल ठूलो पार्ने, दिनको २-३ पटक पानी छर्कने र ४-५ दिनपछि च्याउ तयार भएपछि हल्का बटारेर टिप्ने।</li>
                </ol>
              </div>
            </div>

            <!-- Q4 (e) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(ङ)</span>
                <span>च्याउबाट बन्ने विभिन्न परिकारहरू र उत्पादनहरू के के हुन् ?</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200">
                <strong>उत्तर:</strong> च्याउबाट घरायसी तथा औद्योगिक रूपमा निम्न स्वादिष्ट र पौष्टिक परिकारहरू बनाइन्छ:
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 mt-2">
                  <div class="bg-slate-50 p-2 rounded-xl border border-slate-200">१. च्याउको तरकारी र करी</div>
                  <div class="bg-slate-50 p-2 rounded-xl border border-slate-200">२. च्याउको तातो सूप</div>
                  <div class="bg-slate-50 p-2 rounded-xl border border-slate-200">३. च्याउको मसलेदार अचार</div>
                  <div class="bg-slate-50 p-2 rounded-xl border border-slate-200">४. च्याउको सुकुटी (Dry)</div>
                  <div class="bg-slate-50 p-2 rounded-xl border border-slate-200">५. क्यान्ड च्याउ (Canned)</div>
                  <div class="bg-slate-50 p-2 rounded-xl border border-slate-200">६. च्याउको सूप पाउडर/औषधि</div>
                </div>
              </div>
            </div>

            <!-- Q4 (f) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(च)</span>
                <span>च्याउको सुकुटी बनाउने विधि र यसको आवश्यकता उल्लेख गर्नुहोस् ।</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                <p><strong>सुकुटी बनाउने विधि:</strong> ताजा च्याउलाई सफा कपडाले पुछेर वा धिएर पातला टुक्रा पार्ने। त्यसलाई घाममा वा सोलार/विद्युतीय ड्रायरमा सुकाएर पानीको मात्रा १०% भन्दा कम बनाउने र हावा नछिर्ने प्लास्टिकको झोला वा डिब्बामा सिलबन्दी गरी भण्डारण गर्ने।</p>
                <p><strong>सुकुटीको आवश्यकता:</strong> काँचो च्याउमा ९०% पानी हुने भएकाले २४-४८ घण्टामै कुहिन्छ। सुकुटी बनाउँदा च्याउ १ वर्षभन्दा बढी बिग्रँदैन, ढुवानी गर्न सजिलो हुन्छ, र अफ-सिजनमा बढी मूल्यमा बेच्न सकिन्छ।</p>
              </div>
            </div>

            <!-- Q4 (g) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(छ)</span>
                <span>विषालु च्याउका मुख्य बाह्य लक्षणहरू के के हुन् ?</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200">
                <strong>उत्तर:</strong> विषालु च्याउमा देखिने प्रमुख बाह्य लक्षणहरू निम्न छन्:
                <ul class="list-disc pl-5 mt-1.5 space-y-1">
                  <li>डाँठको फेदमा कचौरा जस्तो भल्भा (Volva) र डाँठको माथि औँठी जस्तो एनुलस (Annulus) दुवै पाइने।</li>
                  <li>छाता (पाइलस) को रंग निकै चहकिलो, गाढा रातो, पहेंलो वा बैजनी हुनु र त्यसमाथि सेता कत्लाहरू (scales) हुनु।</li>
                  <li>च्याउलाई भाँच्दा वा काट्दा नीलो, कालो वा बैजनी रंगमा परिवर्तन हुनु वा दूध जस्तो सेतो रस निस्कनु।</li>
                  <li>च्याउबाट नमिठो, तिखो वा दुर्गन्ध आउनु।</li>
                </ul>
              </div>
            </div>

            <!-- Q4 (h) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(ज)</span>
                <span>च्याउको बाह्य शारीरिक बनावटको सफा चित्र कोरी व्याख्या गर्नुहोस् ।</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                <p><strong>उत्तर:</strong> च्याउको शरीरलाई दुई मुख्य भागमा बाँडिएको हुन्छ:</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                  <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
                    <strong>१. माइसेलियम (Mycelium):</strong> जमिनमुनि वा माध्यमभित्र रहेका धागो जस्ता मसिना हाइफीहरूको जालो। यसले पानी र घुलित जैविक पदार्थ सोस्दछ।
                  </div>
                  <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
                    <strong>२. फ्रुटिङ बडी (Fruiting Body):</strong> जमिनमाथि देखिने छाता आकारको भाग, जसमा स्टाइप (डाँठ), पाइलस (छाता), एनुलस (औँठी) र गिल्स (पत्रहरू) हुन्छन्।
                  </div>
                </div>
              </div>
            </div>

            <!-- Q4 (i) -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">(झ)</span>
                <span>च्याउको जीवन चक्र प्रक्रियागत रूपमा व्याख्या गर्नुहोस् ।</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                <p><strong>जीवन चक्रका प्रमुख चरणहरू:</strong></p>
                <div class="p-2.5 rounded-xl bg-slate-100 font-mono text-[11px] leading-relaxed">
                  वयस्क च्याउ (गिल्सको बेसिडियम) ➔ क्यारियोगामी (2n) ➔ मियोसिस विभाजन ➔ ४ बेसिडियोस्पोर (n) ➔ अंकुरण ➔ प्राथमिक माइसेलियम (n) ➔ प्लाज्मोग्यामी (+ र - मिसिने) ➔ दोस्रो माइसेलियम (n+n) ➔ बटन स्टेज ➔ पुनः वयस्क च्याउ
                </div>
              </div>
            </div>

            <!-- Q4 (j) Textbook Diagram Analysis 1 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-emerald-700 font-black">(ञ)</span>
                <span>पाठ्यपुस्तक पृष्ठ ३५ को चित्र (च्याउको बाह्य बनावट) अध्ययन गरी सोधिएका प्रश्नको उत्तर दिनुहोस्:</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 font-mono text-[11px]">
                  क = पाइलस (Pileus / Cap) | ख = गिल्स (Gills) | ग = स्टाइप (Stipe) | घ = माइसेलियम (Mycelium)
                </div>
                <ul class="list-disc pl-5 space-y-1">
                  <li><strong>क (पाइलस) को काम:</strong> गिल्स र बन्दै गरेका बीजाणुलाई घाम, पानी र बाह्य चोटपटकबाट सुरक्षा प्रदान गर्ने।</li>
                  <li><strong>घ (माइसेलियम) को काम:</strong> जमिनमुनि वा माध्यमबाट पानी, खनिज लवण र जैविक पोषक तत्व सोस्ने तथा अड्याउने।</li>
                  <li><strong>फ्रुटिङ बडी कुन कुन मिलेर बन्छ:</strong> भाग <strong>क (पाइलस)</strong>, <strong>ख (गिल्स)</strong>, र <strong>ग (स्टाइप)</strong> मिलेर फ्रुटिङ बडी बन्दछ।</li>
                </ul>
              </div>
            </div>

            <!-- Q4 (k) Textbook Diagram Analysis 2 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-emerald-700 font-black">(ट)</span>
                <span>पाठ्यपुस्तक पृष्ठ ३५ को चित्र (गिल्सको सूक्ष्म काट T.S.) अध्ययन गरी सोधिएका प्रश्नको उत्तर दिनुहोस्:</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 font-mono text-[11px]">
                  क = प्याराफाइसिस (Paraphysis) | ख = बेसिडियम (Basidium) | ग = सब-हाइमेनियम (Sub-hymenium) | घ = ट्रामा (Trama)
                </div>
                <ul class="list-disc pl-5 space-y-1">
                  <li><strong>क (प्याराफाइसिस) को काम:</strong> बन्ध्या कोष; बेसिडियमलाई एकआपसमा टाँसिन नदिई अलग राख्ने र ओसिलोपना दिई सुरक्षा प्रदान गर्ने।</li>
                  <li><strong>ख (बेसिडियम) को काम:</strong> उर्वर कोष; मियोसिस विभाजन मार्फत टुप्पोमा ४ ओटा बेसिडियोस्पोरहरू उत्पादन गर्ने।</li>
                  <li><strong>ख को टुप्पोमा कतिओटा बीजाणु बन्छन्:</strong> ख को टुप्पोमा <strong>४ ओटा बेसिडियोस्पोरहरू</strong> (२ वटा धनात्मक + स्ट्रेन र २ वटा ऋणात्मक - स्ट्रेन) बन्दछन् र यी <strong>अगुणित (Haploid, n)</strong> हुन्छन्।</li>
                </ul>
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- ================= 5. PRACTICAL PROJECTS ================= -->
      <div class="c9u3-ex-card" data-cat="project">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center text-xs font-black">🛠️</span>
              <span>परियोजना कार्यहरू (Practical Projects):</span>
            </h3>
            <span class="text-xs bg-teal-50 text-teal-700 border border-teal-200 font-bold px-2.5 py-0.5 rounded-full">प्रयोगात्मक</span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
              <h4 class="font-bold text-teal-900 text-sm">परियोजना १: घर/विद्यालयमा च्याउ खेती</h4>
              <p class="text-slate-600 leading-relaxed">
                पराल काटेर उसिनी, बीउ मिसाएर प्लास्टिकको झोलामा पोका पारी १५-२० दिन ओथारो राखेर कन्ने च्याउ उत्पादन गर्ने र दैनिक वृद्धि डायरीमा टिपोट गर्ने।
              </p>
            </div>
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
              <h4 class="font-bold text-teal-900 text-sm">परियोजना २: च्याउ फार्म अवलोकन भ्रमण</h4>
              <p class="text-slate-600 leading-relaxed">
                नजिकको व्यावसायिक च्याउ फार्ममा गई किसानसँग बीउ, पराल निर्मलीकरण, रोग नियन्त्रण, बजार भाउ र नाफा-घाटा सम्बन्धी अन्तर्वार्ता लिई प्रतिवेदन तयार पार्ने।
              </p>
            </div>
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
              <h4 class="font-bold text-teal-900 text-sm">परियोजना ३: विषालु च्याउ सचेतना अभियान</h4>
              <p class="text-slate-600 leading-relaxed">
                वर्षायाममा जंगलका नचिनिएका च्याउ नखान, चाँदी कालो हुने भ्रम त्याग्न र सुरक्षित च्याउ मात्र उपभोग गर्न जनचेतनामूलक पोस्टर र पम्प्लेट तयार पारी प्रदर्शन गर्ने।
              </p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
"""

print("Tab 2 generated.")

# =========================================================================
# TAB 3: 16 TIERED MODEL QUESTIONS
# =========================================================================
tab3_html = """  <!-- ================= TAB 3: 16 TIERED MODEL QUESTIONS ================= -->
  <div id="c9u3-view-tiers" class="hidden space-y-6">
    <!-- Tier Filter Bar -->
    <div class="flex items-center justify-between border-b border-slate-200 pb-3 flex-wrap gap-2">
      <div class="text-xs font-bold text-slate-500">
        क्षमता तह (Cognitive Level) अनुसार प्रश्नहरू:
      </div>
      <div class="flex flex-wrap gap-1.5">
        <button onclick="filterC9U3Tiers('all')" id="c9u3-tierbtn-all" class="px-3 py-1.5 rounded-xl text-xs font-black transition bg-emerald-600 text-white shadow-sm cursor-pointer whitespace-nowrap">
          सबै १६ प्रश्नहरू
        </button>
        <button onclick="filterC9U3Tiers('k')" id="c9u3-tierbtn-k" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          ज्ञानात्मक तह (Knowledge - ५)
        </button>
        <button onclick="filterC9U3Tiers('u')" id="c9u3-tierbtn-u" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          बोधात्मक तह (Understanding - ६)
        </button>
        <button onclick="filterC9U3Tiers('ha')" id="c9u3-tierbtn-ha" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          उच्च दक्षता तथा प्रयोगात्मक (Higher Ability - ५)
        </button>
      </div>
    </div>

    <!-- Tiered Questions Container -->
    <div class="space-y-4">

      <!-- ================= KNOWLEDGE (5 QUESTIONS) ================= -->
      <!-- T1 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="k">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800">प्रश्न १ • ज्ञानात्मक (Knowledge)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: १</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">च्याउलाई किन मृतोपजीवी (Saprotroph) भनिएको हो?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> च्याउमा हरितकण (Chlorophyll) नहुने भएकाले यसले प्रकाश-संश्लेषण गर्न सक्दैन र यसले गोबर, पराल, काठ जस्ता सडेगलेका जैविक वस्तुहरूबाट पाचन रस निष्कासन गरी तरल रूपमा खाना सोसेर प्राप्त गर्ने भएकाले यसलाई मृतोपजीवी भनिएको हो।
        </div>
      </div>

      <!-- T2 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="k">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800">प्रश्न २ • ज्ञानात्मक (Knowledge)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: १</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">हाइमेनियम (Hymenium) मा पाइने दुई प्रकारका कोषहरूको नाम र तिनीहरूको एउटा मुख्य भिन्नता लेख्नुहोस्।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> हाइमेनियममा पाइने दुई कोषहरू <strong>प्याराफाइसिस (Paraphysis)</strong> र <strong>बेसिडियम (Basidium)</strong> हुन्।<br>
          <strong>मुख्य भिन्नता:</strong> बेसिडियम उर्वर (fertile) कोष हो जसले बेसिडियोस्पोर उत्पादन गर्छ भने प्याराफाइसिस बन्ध्या (sterile) कोष हो जसले बेसिडियमलाई सहारा र ओसिलोपना प्रदान गर्छ।
        </div>
      </div>

      <!-- T3 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="k">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800">प्रश्न ३ • ज्ञानात्मक (Knowledge)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: १</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">क्यान्सर रोगको रोकथाम र उपचारमा प्रयोग हुने प्रसिद्ध च्याउको नाम के हो?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> क्यान्सर रोगको रोकथाम र उपचारका लागि औषधि बनाउन प्रयोग हुने प्रसिद्ध च्याउ <strong>रातो च्याउ (<em>Ganoderma lucidum</em>)</strong> हो।
        </div>
      </div>

      <!-- T4 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="k">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800">प्रश्न ४ • ज्ञानात्मक (Knowledge)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: १</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">च्याउको जीवन चक्रमा 'क्यारियोगामी' (Karyogamy) भनेको के हो?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> च्याउको बेसिडियम भित्र दुईओटा अगुणित (Haploid, n) न्युक्लियसहरू (+ स्ट्रेन र - स्ट्रेन) आपसमा संयुक्त भई एउटा द्वैगुणी (Diploid, 2n) न्युक्लियस बन्ने प्रक्रियालाई क्यारियोगामी भनिन्छ।
        </div>
      </div>

      <!-- T5 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="k">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800">प्रश्न ५ • ज्ञानात्मक (Knowledge)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: १</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">कन्ने च्याउ खेती गर्दा पराललाई किन उसिन्न वा बाफमा तताउनु पर्दछ?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> परालमा प्राकृतिक रूपमा रहेका विभिन्न हानिकारक ब्याक्टेरिया, प्रतिस्पर्धी जंगली ढुसीका जीवाणु र कीराका अण्डाहरूलाई नष्ट गरी पराललाई पूर्णतया जीवाणुरहित (Sterilize) बनाउन पराललाई उसिन्न वा बाफमा तताउनु पर्दछ।
        </div>
      </div>

      <!-- ================= UNDERSTANDING (6 QUESTIONS) ================= -->
      <!-- T6 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="u">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">प्रश्न ६ • बोधात्मक (Understanding)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: २</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">प्राथमिक माइसेलियम (Primary mycelium) र दोस्रो माइसेलियम (Secondary mycelium) बीच कुनै दुई फरक लेख्नुहोस्।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed space-y-1">
          <p><strong>१. कोषीय अवस्था:</strong> प्राथमिक माइसेलियम मोनोक्यारियोटिक (n न्युक्लियस भएको) हुन्छ भने दोस्रो माइसेलियम डिक्यारियोटिक (n+n न्युक्लियस भएको) हुन्छ।</p>
          <p><strong>२. उत्पत्ति र आयु:</strong> प्राथमिक माइसेलियम बेसिडियोस्पोरको अंकुरणबाट बन्दछ र अल्पायु हुन्छ; दोस्रो माइसेलियम दुई विपरित स्ट्रेन मिसिएर बन्दछ र यसले फ्रुटिङ बडी उत्पादन गर्छ।</p>
        </div>
      </div>

      <!-- T7 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="u">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">प्रश्न ७ • बोधात्मक (Understanding)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: २</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">च्याउलाई पोषिलो र स्वास्थ्यवर्द्धक पौष्टिक आहार मान्नुका तीनओटा वैज्ञानिक कारणहरू स्पष्ट पार्नुहोस्।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed space-y-1">
          <p>१. <strong>सुपाच्य उच्च प्रोटिन:</strong> करिब २०-३५% प्रोटिन पाइने र सबै अत्यावश्यक एमिनो एसिडहरू सन्तुलित रहने।</p>
          <p>२. <strong>शून्य कोलेस्टेरोल र न्यून चिल्लो:</strong> मुटुरोग, उच्च रक्तचाप र मधुमेहका बिरामीका लागि सुरक्षित र उत्तम आहार।</p>
          <p>३. <strong>भिटामिन र खनिजको प्रचुरता:</strong> भिटामिन डी, भिटामिन बी-कम्प्लेक्स, फलाम र पोटासियम जस्ता पोषक तत्वहरू पाइने।</p>
        </div>
      </div>

      <!-- T8 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="u">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">प्रश्न ८ • बोधात्मक (Understanding)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: २</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">च्याउ टिप्दा डाँठको फेदमै चक्कुले काट्नुभन्दा हल्का बटारेर टिप्नु किन राम्रो मानिन्छ?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> चक्कुले फेदमै काट्दा डाँठको केही ठुटो भाग परालको पोकामै बाँकी रहन्छ, जुन ओसिलो वातावरणमा कुहिएर हानिकारक ढुसी र ब्याक्टेरियाको संक्रमण हुन सक्छ। तर हल्का बटारेर टिप्दा च्याउ जरासहित सफासँग निस्कन्छ र पोकामा कुहिने भाग बाँकी नहुँदा अर्को लटको च्याउ स्वस्थ रूपमा उम्रन पाउँछ।
        </div>
      </div>

      <!-- T9 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="u">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">प्रश्न ९ • बोधात्मक (Understanding)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: २</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">"च्याउ पकाउँदा चाँदीको चम्चा कालो भएन भने त्यो खानयोग्य हुन्छ" भन्ने मान्यता किन अवैज्ञानिक र खतरनाक छ?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> चाँदी कालो हुनु च्याउमा भएको सल्फर यौगिकसँग चाँदीको रासायनिक प्रतिक्रिया मात्र हो। संसारका सबैभन्दा घातक विषालु च्याउहरू (जस्तै: <em>Amanita phalloides</em> को अमानिटिन विष) मा सल्फर यौगिक नहुन सक्छ, जसले गर्दा चाँदी पटक्कै कालो हुँदैन तर उक्त च्याउ खाएमा कलेजो फेल भई ज्यान जान्छ। त्यसैले यो पूर्णतया ज्यानमारा अन्धविश्वास हो।
        </div>
      </div>

      <!-- T10 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="u">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">प्रश्न १० • बोधात्मक (Understanding)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: २</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">च्याउको जीवन चक्रमा बेसिडियोस्पोर बन्नुअघि मियोसिस (Meiosis) विभाजन हुनु किन अनिवार्य छ?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> बेसिडियमभित्र क्यारियोगामी भई दुई न्युक्लियस जोडिएर द्वैगुणी (Diploid, 2n) न्युक्लियस बनिसकेको हुन्छ। मियोसिस विभाजन नभएमा भावी पुस्तामा क्रोमोजोम संख्या दोब्बर हुँदै जान्छ। मियोसिसले क्रोमोजोम संख्या पुनः आधा (Haploid, n) बनाएर प्रजातिको क्रोमोजोम सन्तुलन कायम राख्न, नयाँ आनुवंशिक गुण सिर्जना गर्न र २ वटा (+) तथा २ वटा (-) स्ट्रेनका बेसिडियोस्पोर उत्पादन गर्न अनिवार्य हुन्छ।
        </div>
      </div>

      <!-- T11 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="u">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">प्रश्न ११ • बोधात्मक (Understanding)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: २</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">च्याउको ताजा उत्पादनपछि तुरुन्तै सुकुटी बनाउने प्रविधिको आवश्यकता किन पर्दछ?</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed">
          <strong>आदर्श उत्तर:</strong> ताजा च्याउमा ९०-९२% पानी हुने भएकाले २४-४८ घण्टामै ब्याक्टेरिया लागेर कुहिन्छ। सुकाएर पानीको मात्रा १०% भन्दा तल झार्दा सूक्ष्मजीवको वृद्धि रोकिन्छ। यसले गर्दा च्याउ वर्षौंसम्म सुरक्षित राख्न, ढुवानी गर्न सहज बनाउन, अफ-सिजनमा उपभोग गर्न र किसानलाई आर्थिक क्षतिबाट जोगाउन सुकुटी बनाउने प्रविधि आवश्यक पर्दछ।
        </div>
      </div>

      <!-- ================= HIGHER ABILITY (5 QUESTIONS) ================= -->
      <!-- T12 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="ha">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-800">प्रश्न १२ • उच्च दक्षता (Higher Ability)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: ४</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">रामबहादुरले कन्ने च्याउ खेती गर्दा पराल उसिनेपछि राम्ररी नसुकाई अत्यधिक चिसो (पानी चुहिने अवस्था) मै बीउ मिसाएर प्लास्टिकको पोका बाँधेछन्। केही दिनपछि पोकाबाट दुर्गन्ध आयो र च्याउ उम्रिएन।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed space-y-1.5">
          <p><strong>(क) असफलताको कारण:</strong> परालमा अत्यधिक पानी हुँदा पोकाभित्र अक्सिजनको अभाव भई अवायवीय (Anaerobic) अवस्था बन्यो। यसले च्याउको माइसेलियम निसास्सिएर मर्यो र अवायवीय सडन गराउने ब्याक्टेरिया मौलाएर दुर्गन्ध आयो।</p>
          <p><strong>(ख) चिस्यान जाँच्ने परम्परागत तरिका:</strong> उसिनेको पराललाई हत्केलामा बेस्सरी निचोर्दा औँलाका कापबाट पानी नचुहिने तर हातको हत्केला भिज्ने अवस्था नै ६०-६५% आदर्श चिस्यान हो।</p>
          <p><strong>(ग) सुधारका उपाय:</strong> १. पराललाई प्लास्टिकमा राम्रोसँग फैलाएर पानी तर्काउने र चिस्यान ६०-६५% पुर्‍याउने। २. पोकामा हावा आवतजावतका लागि १०-१५ साना प्वालहरू पार्ने।</p>
        </div>
      </div>

      <!-- T13 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="ha">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-800">प्रश्न १३ • उच्च दक्षता (Higher Ability)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: ४</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">कन्ने च्याउ खेती गर्दा किसानले १० पोका राखेका छन्। प्रति पोका २.५ के.जी. ताजा च्याउ उत्पादन हुन्छ। ताजा च्याउको मूल्य रु. २०० प्रति के.जी. छ। सुकाउँदा ताजा तौलको १०% सुकुटी बन्छ र सुकुटीको मूल्य रु. २,५०० प्रति के.जी. छ। आर्थिक विश्लेषण गर्नुहोस्।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed space-y-1.5">
          <p><strong>१. ताजा च्याउ बिक्री आम्दानी:</strong> जम्मा उत्पादन = १० × २.५ = २५ के.जी.। आम्दानी = २५ × २०० = <strong>रु. ५,०००</strong>।</p>
          <p><strong>२. सुकुटी च्याउ बिक्री आम्दानी:</strong> सुकुटीको तौल = २५ को १०% = २.५ के.जी.। आम्दानी = २.५ × २,५०० = <strong>रु. ६,२५०</strong>।</p>
          <p><strong>निष्कर्ष:</strong> सुकुटी बेच्दा रु. १,२५० बढी आम्दानी हुनुका साथै च्याउ बिग्रिएर हुने जोखिमबाट बचिने भएकाले सुकुटी प्रविधि किसानका लागि आर्थिक रूपमा बढी लाभदायक छ।</p>
        </div>
      </div>

      <!-- T14 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="ha">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-800">प्रश्न १४ • उच्च दक्षता (Higher Ability)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: ४</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">गिल्सको सूक्ष्म अनुप्रस्थ काट (T.S.) मा प्याराफाइसिस (क), बेसिडियम (ख), सब-हाइमेनियम (ग) र ट्रामा (घ) को विश्लेषण गर्नुहोस्।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed space-y-1">
          <p><strong>क (प्याराफाइसिस):</strong> बन्ध्या कोष; बेसिडियमलाई एकआपसमा टाँसिन नदिई अलग राख्ने, ठाडो अड्याउने र ओसिलो बनाई सुरक्षा दिने।</p>
          <p><strong>ख (बेसिडियम):</strong> उर्वर कोष; यसको टुप्पोमा ४ ओटा अगुणित (Haploid, n) बेसिडियोस्पोरहरू (२ वटा + र २ वटा -) बन्दछन्।</p>
          <p><strong>घ (ट्रामा):</strong> गिल्सको भित्री केन्द्रीय मेरुदण्ड; यसले गिल्सलाई आकार र दृढता प्रदान गर्दछ।</p>
        </div>
      </div>

      <!-- T15 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="ha">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-800">प्रश्न १५ • उच्च दक्षता (Higher Ability)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: ४</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">जंगलमा भेटिएका च्याउ विषालु हुन् कि होइनन् भनी पहिचान गर्ने कुनै चार लक्षण र समुदायमा सचेतना जगाउने दुई बुँदा सुझाव दिनुहोस्।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed space-y-1.5">
          <p><strong>चार लक्षणहरू:</strong> १. डाँठको फेदमा भल्भा (कचौरा) र माथि एनुलस (औँठी) दुवै हुनु। २. काट्दा नीलो/कालो रंगमा परिवर्तन हुनु वा सेतो तरल आउनु। ३. गाढा चहकिलो रातो/पहेंलो रंग र कत्ला हुनु। ४. तिखो दुर्गन्ध आउनु।</p>
          <p><strong>सचेतना सुझावहरू:</strong> १. "नचिनिएका जंगली च्याउ कहिल्यै नखाऔँ; चाँदी कालो हुने भ्रम त्यागाैँ।" २. "प्रमाणित फार्मबाट उत्पादित कन्ने वा डल्ले च्याउ मात्र उपभोग गरौँ।"</p>
        </div>
      </div>

      <!-- T16 -->
      <div class="c9u3-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="ha">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-800">प्रश्न १६ • उच्च दक्षता (Higher Ability)</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: ४</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">नेपालको ग्रामीण भेगमा गरिबी निवारण र स्वरोजगार सिर्जना गर्न च्याउ खेती कसरी वरदान सावित हुन सक्छ? चारओटा तर्क दिनुहोस्।</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-2xl border border-slate-100 leading-relaxed space-y-1">
          <p>१. <strong>थोरै जग्गा र लगानी:</strong> सानो कोठा वा छाप्रोमा ठाडो र्‍याक बनाएर न्यून लगानीमै सुरु गर्न सकिने।</p>
          <p>२. <strong>कृषि अवशेषको सदुपयोग:</strong> खेर गइरहेको धानको पराल र काठको भुस प्रयोग गर्न सकिने।</p>
          <p>३. <strong>छिटो प्रतिफल:</strong> बीउ रोपेको ३-४ हप्तामै उत्पादन सुरु भई किसानले दैनिक नगद पाउने।</p>
          <p>४. <strong>महिला तथा विपन्न वर्गको सशक्तिकरण:</strong> घरमै बसेर सहजै सञ्चालन गर्न सकिने भएकाले आत्मनिर्भरता बढ्ने।</p>
        </div>
      </div>

    </div>
  </div>
"""

# =========================================================================
# TAB 4: SELF-ASSESSMENT QUIZ
# =========================================================================
tab4_html = """  <!-- ================= TAB 4: SELF-ASSESSMENT QUIZ ================= -->
  <div id="c9u3-view-quiz" class="hidden space-y-6">
    <!-- Quiz Header Banner -->
    <div class="bg-gradient-to-r from-emerald-600 to-teal-700 rounded-3xl p-6 text-white shadow-md flex flex-wrap items-center justify-between gap-4">
      <div>
        <span class="text-xs font-bold uppercase tracking-wider bg-white/20 px-3 py-1 rounded-full">
          इन्टरएक्टिभ वस्तुगत परीक्षा
        </span>
        <h3 class="text-2xl font-black mt-2">एकाइ ३: च्याउ (Mushroom) - स्वमूल्याङ्कन क्विज</h3>
        <p class="text-xs md:text-sm text-emerald-100 mt-1">
          १० ओटा बहुवैकल्पिक प्रश्नहरूको उत्तर दिनुहोस् र आफ्नो प्राप्ताङ्क तुरुन्त जाँच्नुहोस्।
        </p>
      </div>

      <div class="flex items-center gap-4">
        <div class="bg-white/10 backdrop-blur-md border border-white/20 px-5 py-3 rounded-2xl text-center">
          <span class="text-xs text-emerald-200 block font-semibold">तपाईंको प्राप्ताङ्क</span>
          <span id="c9u3-quiz-score-badge" class="text-2xl font-black text-white">० / १०</span>
        </div>
        <button onclick="resetC9U3Quiz()" class="px-4 py-2.5 rounded-xl bg-white/20 hover:bg-white/30 text-white text-xs font-bold transition cursor-pointer">
          पुनः सुरु गर्नुहोस्
        </button>
      </div>
    </div>

    <!-- Quiz Question Cards Container -->
    <div id="c9u3-quiz-container" class="space-y-4">
      <!-- Populated dynamically by JS -->
    </div>
  </div>
</div>
<!-- ================= END CLASS 9 UNIT 3 CONTAINER ================= -->
"""

full_html = tab1_html + tab2_html + tab3_html + tab4_html
with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Wrote full HTML to {html_path} ({len(full_html)} bytes)")

