# -*- coding: utf-8 -*-
"""
1. Adds missing responsive display rules to @media (min-width: 768px):
   .md:flex, .md:inline-flex, .md:block, .md:hidden
2. Adds explicit sizing classes and attributes for SVG icons (.icon-sm, .icon-md, .icon-lg).
3. Fixes magnifying glass SVG in sidebar and all header SVGs.
4. Synchronizes index.html and bundle.
"""
import sys

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update @media (min-width: 768px)
media_target = """@media (min-width: 768px) {
  .md\\:col-span-2 { grid-column: span 2 / span 2; }
  .md\\:flex-row { flex-direction: row; }"""

media_replacement = """@media (min-width: 768px) {
  .md\\:flex { display: flex !important; }
  .md\\:inline-flex { display: inline-flex !important; }
  .md\\:block { display: block !important; }
  .md\\:hidden { display: none !important; }
  .md\\:col-span-2 { grid-column: span 2 / span 2; }
  .md\\:flex-row { flex-direction: row; }"""

if media_target not in html:
    print("ERROR: media_target not found!")
    sys.exit(1)

html = html.replace(media_target, media_replacement, 1)
print("1. Added .md:flex, .md:inline-flex, .md:block, .md:hidden to 768px media query!")

# 2. Add SVG icon rules in CSS
icon_css_target = """.offline-math {"""
icon_css_replacement = """    /* SVG Icon Sizing */
    svg.icon-sm, .icon-sm { width: 16px !important; height: 16px !important; min-width: 16px !important; min-height: 16px !important; flex-shrink: 0; }
    svg.icon-md, .icon-md { width: 20px !important; height: 20px !important; min-width: 20px !important; min-height: 20px !important; flex-shrink: 0; }
    svg.icon-lg, .icon-lg { width: 24px !important; height: 24px !important; min-width: 24px !important; min-height: 24px !important; flex-shrink: 0; }

    .offline-math {"""

if icon_css_target not in html:
    print("ERROR: icon_css_target not found!")
    sys.exit(1)

html = html.replace(icon_css_target, icon_css_replacement, 1)
print("2. Added SVG icon sizing utility rules!")

# 3. Fix sidebar search SVG
search_svg_target = """      <div class="relative mb-3">
        <svg class="absolute left-3.5 top-3 w-4 h-4 text-slate-400 pointer-events-none" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <input type="text" id="search-input" placeholder="पाठ वा एकाइ खोज्नुहोस्..." class="w-full pl-10 pr-3.5 py-2.5 text-xs md:text-sm bg-slate-50 hover:bg-slate-100/80 focus:bg-white border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all min-h-[44px]">
      </div>"""

search_svg_replacement = """      <div class="relative mb-3 flex items-center">
        <svg class="absolute left-3.5 text-slate-400 pointer-events-none icon-sm" width="16" height="16" style="width:16px;height:16px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <input type="text" id="search-input" placeholder="पाठ वा एकाइ खोज्नुहोस्..." class="w-full pl-10 pr-3.5 py-2 text-xs md:text-sm bg-slate-50 hover:bg-slate-100/80 focus:bg-white border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all min-h-[42px]">
      </div>"""

if search_svg_target not in html:
    print("ERROR: search_svg_target not found!")
    sys.exit(1)

html = html.replace(search_svg_target, search_svg_replacement, 1)
print("3. Fixed sidebar search icon size to 16px!")

# 4. Fix Grade switcher SVGs
grade_target = """        <button id="btn-grade-6" onclick="selectGrade(6)" class="px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-black transition-all flex items-center gap-1.5 bg-white text-indigo-950 shadow-md ring-2 ring-indigo-400/40 cursor-pointer min-h-[40px] md:min-h-[44px]">
          <svg class="w-3.5 h-3.5 md:w-4 md:h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
          <span>कक्षा ६</span>
        </button>
        <button id="btn-grade-9" onclick="selectGrade(9)" class="px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-bold transition-all flex items-center gap-1.5 text-white/80 hover:text-white hover:bg-white/10 cursor-pointer min-h-[40px] md:min-h-[44px]">
          <svg class="w-3.5 h-3.5 md:w-4 md:h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
          <span>कक्षा ९</span>
        </button>"""

grade_replacement = """        <button id="btn-grade-6" onclick="selectGrade(6)" class="px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-black transition-all flex items-center gap-1.5 bg-white text-indigo-950 shadow-md ring-2 ring-indigo-400/40 cursor-pointer min-h-[40px] md:min-h-[44px]">
          <svg class="icon-sm shrink-0" width="16" height="16" style="width:16px;height:16px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
          <span>कक्षा ६</span>
        </button>
        <button id="btn-grade-9" onclick="selectGrade(9)" class="px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-bold transition-all flex items-center gap-1.5 text-white/80 hover:text-white hover:bg-white/10 cursor-pointer min-h-[40px] md:min-h-[44px]">
          <svg class="icon-sm shrink-0" width="16" height="16" style="width:16px;height:16px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
          <span>कक्षा ९</span>
        </button>"""

if grade_target not in html:
    print("ERROR: grade_target not found!")
    sys.exit(1)

html = html.replace(grade_target, grade_replacement, 1)
print("4. Fixed Grade switcher SVGs with explicit icon-sm sizes!")

# 5. Fix Header right SVGs
right_target = """        <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-200 border border-emerald-400/30 shadow-xs">
          <svg class="w-3.5 h-3.5 text-emerald-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
          <span>सम्पूर्ण अभ्यास र समाधान</span>
        </span>
        <!-- Font Switcher Control -->
        <div class="inline-flex items-center gap-1.5 bg-white/10 backdrop-blur-md px-2.5 py-1 rounded-xl text-xs font-bold border border-white/20 text-white shadow-xs" title="फन्ट छनौट गर्नुहोस्">
          <svg class="w-3.5 h-3.5 opacity-90 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5h12M9 5v14m4-7h8m-4-7v14"/></svg>
          <select id="global-font-select" onchange="changeGlobalFont(this.value, true)" class="bg-slate-800 text-white text-xs font-bold rounded-lg px-2 py-0.5 border border-white/20 focus:outline-none focus:ring-1 focus:ring-amber-300 cursor-pointer">
            <option value="preeti" selected>प्रिती (Preeti - डिफल्ट)</option>
            <option value="mukta">मुक्ता (Mukta - युनिकोड)</option>
            <option value="system">प्रणाली (System Sans)</option>
          </select>
        </div>
        <!-- Preeti Converter & Typing Pad Modal Button -->
        <button onclick="togglePreetiModal(true)" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-black bg-amber-400 text-slate-950 hover:bg-amber-300 transition-all cursor-pointer shadow-md hover:scale-105 active:scale-95 border border-amber-300 min-h-[36px]" title="युनिकोड ↔ प्रिती रुपान्तरक तथा टाइपिङ प्याड">
          <svg class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M6 8h.01M10 8h.01M14 8h.01M18 8h.01M6 12h.01M10 12h.01M14 12h.01M18 12h.01M8 16h8"/></svg>
          <span>प्रिती रुपान्तरक</span>
        </button>
        <span id="offline-status-badge" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold bg-white/10 text-white border border-white/20 shadow-xs" title="इन्टरनेट वा सर्भर बिना पनि १००% काम गर्छ">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>अफलाइन सक्रिय</span>
        </span>
        <button id="pwa-install-btn" class="hidden inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold bg-amber-400 text-slate-950 hover:bg-amber-300 transition-all cursor-pointer shadow-md min-h-[36px]" title="यस उपकरणमा एपका रूपमा इन्स्टल गर्नुहोस्">
          <svg class="w-3.5 h-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          <span>एप इन्स्टल</span>
        </button>"""

right_replacement = """        <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-200 border border-emerald-400/30 shadow-xs">
          <svg class="icon-sm text-emerald-400 shrink-0" width="14" height="14" style="width:14px;height:14px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
          <span>सम्पूर्ण अभ्यास र समाधान</span>
        </span>
        <!-- Font Switcher Control -->
        <div class="inline-flex items-center gap-1.5 bg-white/10 backdrop-blur-md px-2.5 py-1 rounded-xl text-xs font-bold border border-white/20 text-white shadow-xs" title="फन्ट छनौट गर्नुहोस्">
          <svg class="icon-sm opacity-90 shrink-0" width="14" height="14" style="width:14px;height:14px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5h12M9 5v14m4-7h8m-4-7v14"/></svg>
          <select id="global-font-select" onchange="changeGlobalFont(this.value, true)" class="bg-slate-800 text-white text-xs font-bold rounded-lg px-2 py-0.5 border border-white/20 focus:outline-none focus:ring-1 focus:ring-amber-300 cursor-pointer">
            <option value="preeti" selected>प्रिती (Preeti - डिफल्ट)</option>
            <option value="mukta">मुक्ता (Mukta - युनिकोड)</option>
            <option value="system">प्रणाली (System Sans)</option>
          </select>
        </div>
        <!-- Preeti Converter & Typing Pad Modal Button -->
        <button onclick="togglePreetiModal(true)" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-black bg-amber-400 text-slate-950 hover:bg-amber-300 transition-all cursor-pointer shadow-md hover:scale-105 active:scale-95 border border-amber-300 min-h-[36px]" title="युनिकोड ↔ प्रिती रुपान्तरक तथा टाइपिङ प्याड">
          <svg class="icon-sm shrink-0" width="14" height="14" style="width:14px;height:14px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M6 8h.01M10 8h.01M14 8h.01M18 8h.01M6 12h.01M10 12h.01M14 12h.01M18 12h.01M8 16h8"/></svg>
          <span>प्रिती रुपान्तरक</span>
        </button>
        <span id="offline-status-badge" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold bg-white/10 text-white border border-white/20 shadow-xs" title="इन्टरनेट वा सर्भर बिना पनि १००% काम गर्छ">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>अफलाइन सक्रिय</span>
        </span>
        <button id="pwa-install-btn" class="hidden inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold bg-amber-400 text-slate-950 hover:bg-amber-300 transition-all cursor-pointer shadow-md min-h-[36px]" title="यस उपकरणमा एपका रूपमा इन्स्टल गर्नुहोस्">
          <svg class="icon-sm shrink-0" width="14" height="14" style="width:14px;height:14px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          <span>एप इन्स्टल</span>
        </button>"""

if right_target not in html:
    print("ERROR: right_target not found!")
    sys.exit(1)

html = html.replace(right_target, right_replacement, 1)
print("5. Fixed Header right SVGs with explicit icon-sm sizes!")

# 6. Fix Unit 7 navigation tabs SVGs
tabs_target = """    <button onclick="setTabC9U7('concepts')" id="c9u7-tab-concepts" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl bg-indigo-600 text-white shadow-md font-bold transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer ring-2 ring-indigo-400/30 min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
      <span>३-मोड भौतिक प्रयोगशाला (Virtual Physics Lab)</span>
    </button>
    <button onclick="setTabC9U7('exercises')" id="c9u7-tab-exercises" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
      <span>सम्पूर्ण अभ्यास तथा समाधान (CDC Solutions)</span>
    </button>
    <button onclick="setTabC9U7('tiers')" id="c9u7-tab-tiers" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
      <span>१६ स्तरीकृत प्रश्नोत्तर (Model Q&As)</span>
    </button>
    <button onclick="setTabC9U7('quiz')" id="c9u7-tab-quiz" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
      <span>स्वमूल्याङ्कन क्विज (Interactive Quiz)</span>
    </button>"""

tabs_replacement = """    <button onclick="setTabC9U7('concepts')" id="c9u7-tab-concepts" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl bg-indigo-600 text-white shadow-md font-bold transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer ring-2 ring-indigo-400/30 min-h-[44px]">
      <svg class="icon-sm shrink-0" width="18" height="18" style="width:18px;height:18px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
      <span>३-मोड भौतिक प्रयोगशाला (Virtual Physics Lab)</span>
    </button>
    <button onclick="setTabC9U7('exercises')" id="c9u7-tab-exercises" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="icon-sm shrink-0" width="18" height="18" style="width:18px;height:18px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
      <span>सम्पूर्ण अभ्यास तथा समाधान (CDC Solutions)</span>
    </button>
    <button onclick="setTabC9U7('tiers')" id="c9u7-tab-tiers" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="icon-sm shrink-0" width="18" height="18" style="width:18px;height:18px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
      <span>१६ स्तरीकृत प्रश्नोत्तर (Model Q&As)</span>
    </button>
    <button onclick="setTabC9U7('quiz')" id="c9u7-tab-quiz" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="icon-sm shrink-0" width="18" height="18" style="width:18px;height:18px;" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
      <span>स्वमूल्याङ्कन क्विज (Interactive Quiz)</span>
    </button>"""

if tabs_target not in html:
    print("ERROR: tabs_target not found!")
    sys.exit(1)

html = html.replace(tabs_target, tabs_replacement, 1)
print("6. Fixed Unit 7 tabs SVGs with explicit sizes!")

# Double virama check
if '\u094d\u094d' in html:
    print("ERROR: Double virama in html!")
    sys.exit(1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved index.html successfully!")

bundle = "कक्षा_६_गणित_डिजिटल_साथी.html"
with open(bundle, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved {bundle} successfully (100% sync)!")
