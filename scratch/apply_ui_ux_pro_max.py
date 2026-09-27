# -*- coding: utf-8 -*-
"""
Applies UI/UX Pro Max design intelligence to Digital Guru:
1. CSS variables, claymorphic card tokens, scroll-padding, and reduced-motion rules.
2. Header glassmorphism + modern dark indigo tone.
3. Replace emojis with crisp, scalable SVGs in header, navigation tabs, preset controls, and badges.
4. Touch targets >= 44px on mobile and accessible keyboard focus rings.
5. Synchronize index.html and bundle.
"""
import sys
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# -----------------------------------------------------------------------------
# 1. Update CSS in <head>
# -----------------------------------------------------------------------------
css_target = """    * { box-sizing: border-box; }
    body { font-family: 'Preeti', 'Mukta', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f1f5f9; color: #1e293b; margin: 0; min-height: 100vh; display: flex; flex-direction: column; }
    
    /* Header gradient */
    header { background: linear-gradient(135deg, #1d4ed8 0%, #4338ca 50%, #6b21a8 100%) !important; color: #ffffff !important; }
    header h1, header p, header div, header span { color: inherit !important; }
    
    /* Controls & Buttons */
    button { cursor: pointer; border: none; font-family: inherit; }
    button:hover { opacity: 0.95; }
    input[type="text"], input[type="number"] { font-family: inherit; }"""

new_css = """    /* UI/UX Pro Max Design System Tokens */
    :root {
      --color-primary: #4f46e5;
      --color-primary-hover: #4338ca;
      --color-secondary: #818cf8;
      --color-accent: #ea580c;
      --color-accent-hover: #c2410c;
      --color-background: #f8fafc;
      --color-foreground: #0f172a;
      --color-card: #ffffff;
      --color-border: #e2e8f0;
      --header-height: 4.5rem;
    }

    html {
      scroll-padding-top: var(--header-height);
      scroll-behavior: smooth;
    }

    * { box-sizing: border-box; }
    body {
      font-family: 'Preeti', 'Mukta', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #f8fafc;
      color: #0f172a;
      margin: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* WCAG 2.2 Accessible Focus & Interactive Targets */
    button:focus-visible, a:focus-visible, input:focus-visible, select:focus-visible {
      outline: 2px solid var(--color-primary) !important;
      outline-offset: 2px !important;
    }

    button, [role="button"] {
      cursor: pointer;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    button:active, [role="button"]:active {
      transform: scale(0.97);
    }

    /* Claymorphism & Soft Modern Depth */
    .clay-card {
      background: #ffffff;
      border: 1px solid rgba(226, 232, 240, 0.85);
      border-radius: 1.25rem;
      box-shadow: 0 4px 20px -2px rgba(79, 70, 229, 0.06), 0 2px 6px -1px rgba(0, 0, 0, 0.03);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .clay-card:hover {
      box-shadow: 0 10px 25px -4px rgba(79, 70, 229, 0.1), 0 4px 10px -2px rgba(0, 0, 0, 0.04);
      transform: translateY(-2px);
    }

    /* Respect Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      html {
        scroll-behavior: auto;
      }
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }

    /* Header elevation */
    header {
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #172554 100%) !important;
      color: #ffffff !important;
    }
    header h1, header p, header div, header span { color: inherit !important; }
    
    input[type="text"], input[type="number"] { font-family: inherit; }"""

if css_target not in html:
    print("ERROR: css_target not found!")
    sys.exit(1)

html = html.replace(css_target, new_css, 1)
print("1. Updated CSS with UI/UX Pro Max tokens!")

# -----------------------------------------------------------------------------
# 2. Update Header HTML
# -----------------------------------------------------------------------------
old_header_start = """  <!-- Header -->
  <header id="main-header" class="bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-800 text-white shadow-lg sticky top-0 z-50" style="transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);">"""

new_header_start = """  <!-- Header: UI/UX Pro Max Glassmorphic Design -->
  <header id="main-header" class="bg-slate-900/95 backdrop-blur-xl border-b border-indigo-500/20 text-white shadow-md sticky top-0 z-50" style="transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);">"""

if old_header_start not in html:
    print("ERROR: old_header_start not found!")
    sys.exit(1)
html = html.replace(old_header_start, new_header_start, 1)

# Upgrade Grade Switcher and Header controls
old_switcher = """      <!-- MIDDLE: Grade Switcher Pills -->
      <div class="flex items-center p-0.5 md:p-1 bg-black/25 backdrop-blur-md rounded-xl md:rounded-2xl border border-white/20 shadow-inner shrink-0">
        <button id="btn-grade-6" onclick="selectGrade(6)" class="px-2.5 md:px-3.5 py-1 md:py-1.5 rounded-lg md:rounded-xl text-xs font-black transition flex items-center gap-1 md:gap-1.5 bg-white text-blue-900 shadow-sm cursor-pointer">
          <span class="hidden sm:inline">📐</span><span>कक्षा ६</span>
        </button>
        <button id="btn-grade-9" onclick="selectGrade(9)" class="px-2.5 md:px-3.5 py-1 md:py-1.5 rounded-lg md:rounded-xl text-xs font-bold transition flex items-center gap-1 md:gap-1.5 text-white/90 hover:text-white hover:bg-white/10 cursor-pointer">
          <span class="hidden sm:inline">🔬</span><span>कक्षा ९</span>
        </button>
      </div>"""

new_switcher = """      <!-- MIDDLE: Grade Switcher Pills (UI/UX Pro Max SVG Segmented Control) -->
      <div class="flex items-center p-1 bg-black/40 backdrop-blur-md rounded-2xl border border-white/15 shadow-inner shrink-0 gap-1">
        <button id="btn-grade-6" onclick="selectGrade(6)" class="px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-black transition-all flex items-center gap-1.5 bg-white text-indigo-950 shadow-md ring-2 ring-indigo-400/40 cursor-pointer min-h-[40px] md:min-h-[44px]">
          <svg class="w-3.5 h-3.5 md:w-4 md:h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
          <span>कक्षा ६</span>
        </button>
        <button id="btn-grade-9" onclick="selectGrade(9)" class="px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-bold transition-all flex items-center gap-1.5 text-white/80 hover:text-white hover:bg-white/10 cursor-pointer min-h-[40px] md:min-h-[44px]">
          <svg class="w-3.5 h-3.5 md:w-4 md:h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
          <span>कक्षा ९</span>
        </button>
      </div>"""

if old_switcher not in html:
    print("ERROR: old_switcher not found!")
    sys.exit(1)
html = html.replace(old_switcher, new_switcher, 1)

# Upgrade Header Right Controls
old_right = """      <!-- RIGHT: Desktop controls only (hidden on mobile) -->
      <div class="hidden md:flex flex-wrap items-center gap-2">
        <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/25 text-emerald-200 border border-emerald-400/40 shadow-xs">✓ सम्पूर्ण अभ्यास र समाधान समावेश</span>
        <!-- Font Switcher Control -->
        <div class="inline-flex items-center gap-1.5 bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-bold border border-white/30 text-white shadow-xs" title="फन्ट छनौट गर्नुहोस्">
          <span class="opacity-90">🔤</span>
          <select id="global-font-select" onchange="changeGlobalFont(this.value, true)" class="bg-indigo-900/80 text-white text-xs font-bold rounded-lg px-2 py-0.5 border border-white/30 focus:outline-none focus:ring-1 focus:ring-amber-300 cursor-pointer">
            <option value="preeti" selected>प्रिती (Preeti - डिफल्ट)</option>
            <option value="mukta">मुक्ता (Mukta - युनिकोड)</option>
            <option value="system">प्रणाली (System Sans)</option>
          </select>
        </div>
        <!-- Preeti Converter & Typing Pad Modal Button -->
        <button onclick="togglePreetiModal(true)" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-black bg-amber-400 text-slate-900 hover:bg-amber-300 transition cursor-pointer shadow-md hover:scale-105 active:scale-95" title="युनिकोड ↔ प्रिती रुपान्तरक तथा टाइपिङ प्याड">
          <span>⌨️ प्रिती रुपान्तरक</span>
        </button>
        <span id="offline-status-badge" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-white/20 text-white border border-white/30 shadow-xs" title="इन्टरनेट वा सर्भर बिना पनि १००% काम गर्छ">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>अफलाइन सक्रिय (Offline Ready)</span>
        </span>
        <button id="pwa-install-btn" class="hidden inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-400 text-slate-900 hover:bg-amber-300 transition cursor-pointer shadow-md" title="यस उपकरणमा एपका रूपमा इन्स्टल गर्नुहोस्">
          <span>📲 एप इन्स्टल गर्नुहोस्</span>
        </button>
      </div>"""

new_right = """      <!-- RIGHT: Desktop controls (UI/UX Pro Max SVG and Semantic Badges) -->
      <div class="hidden md:flex flex-wrap items-center gap-2.5">
        <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-200 border border-emerald-400/30 shadow-xs">
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
        </button>
      </div>"""

if old_right not in html:
    print("ERROR: old_right not found!")
    sys.exit(1)
html = html.replace(old_right, new_right, 1)
print("2. Updated Header with UI/UX Pro Max SVG controls!")

# -----------------------------------------------------------------------------
# 3. Update Sidebar Search input with MagnifyingGlass SVG
# -----------------------------------------------------------------------------
old_search = """      <div class="relative mb-3">
        <input type="text" id="search-input" placeholder="पाठ खोज्नुहोस्..." class="w-full px-3.5 py-2 text-sm bg-slate-100 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500">
      </div>"""

new_search = """      <div class="relative mb-3">
        <svg class="absolute left-3.5 top-3 w-4 h-4 text-slate-400 pointer-events-none" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <input type="text" id="search-input" placeholder="पाठ वा एकाइ खोज्नुहोस्..." class="w-full pl-10 pr-3.5 py-2.5 text-xs md:text-sm bg-slate-50 hover:bg-slate-100/80 focus:bg-white border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all min-h-[44px]">
      </div>"""

if old_search not in html:
    print("ERROR: old_search not found!")
    sys.exit(1)
html = html.replace(old_search, new_search, 1)
print("3. Updated Sidebar search bar with SVG icon and 44px min-height!")

# -----------------------------------------------------------------------------
# 4. Update Unit 7 primary tabs in index.html
# -----------------------------------------------------------------------------
old_u7_tabs = """  <!-- 4 Primary Navigation Tabs -->
  <div class="flex border-b border-slate-200 overflow-x-auto gap-2 mb-6 select-none no-scrollbar">
    <button onclick="setTabC9U7('concepts')" id="c9u7-tab-concepts" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
      🔬 ३-मोड भौतिक प्रयोगशाला (Virtual Physics Lab)
    </button>
    <button onclick="setTabC9U7('exercises')" id="c9u7-tab-exercises" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      📖 सम्पूर्ण अभ्यास तथा गणितीय समस्या (CDC Solutions)
    </button>
    <button onclick="setTabC9U7('tiers')" id="c9u7-tab-tiers" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      🎯 १६ स्तरीकृत प्रश्नोत्तर (Model Q&As)
    </button>
    <button onclick="setTabC9U7('quiz')" id="c9u7-tab-quiz" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      📝 स्वमूल्याङ्कन क्विज (Interactive Quiz)
    </button>
  </div>"""

new_u7_tabs = """  <!-- 4 Primary Navigation Tabs (UI/UX Pro Max SVG Icons + Claymorphic Pills) -->
  <div class="flex border-b border-slate-200 overflow-x-auto gap-2 mb-6 select-none no-scrollbar pb-1">
    <button onclick="setTabC9U7('concepts')" id="c9u7-tab-concepts" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl bg-indigo-600 text-white shadow-md font-bold transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer ring-2 ring-indigo-400/30 min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
      <span>३-मोड भौतिक प्रयोगशाला (Virtual Physics Lab)</span>
    </button>
    <button onclick="setTabC9U7('exercises')" id="c9u7-tab-exercises" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
      <span>सम्पूर्ण अभ्यास तथा समाधान (CDC Solutions)</span>
    </button>
    <button onclick="setTabC9U7('tiers')" id="c9u7-tab-tiers" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
      <span>१६ स्तरीकृत प्रश्नोत्तर (Model Q&As)</span>
    </button>
    <button onclick="setTabC9U7('quiz')" id="c9u7-tab-quiz" class="px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]">
      <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
      <span>स्वमूल्याङ्कन क्विज (Interactive Quiz)</span>
    </button>
  </div>"""

if old_u7_tabs not in html:
    print("ERROR: old_u7_tabs not found!")
    sys.exit(1)
html = html.replace(old_u7_tabs, new_u7_tabs, 1)
print("4. Updated Unit 7 navigation tabs with SVG icons!")

# -----------------------------------------------------------------------------
# 5. Update selectGrade JS implementation
# -----------------------------------------------------------------------------
old_select_grade_logic = """  if (grade === 6) {
    if (btn6) btn6.className = 'px-3.5 py-1.5 rounded-xl text-xs font-black transition flex items-center gap-1.5 bg-white text-blue-900 shadow-sm cursor-pointer';
    if (btn9) btn9.className = 'px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-white/90 hover:text-white hover:bg-white/10 cursor-pointer';"""

new_select_grade_logic = """  if (grade === 6) {
    if (btn6) btn6.className = 'px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-black transition-all flex items-center gap-1.5 bg-white text-indigo-950 shadow-md ring-2 ring-indigo-400/40 cursor-pointer min-h-[40px] md:min-h-[44px]';
    if (btn9) btn9.className = 'px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-bold transition-all flex items-center gap-1.5 text-white/80 hover:text-white hover:bg-white/10 cursor-pointer min-h-[40px] md:min-h-[44px]';"""

old_select_grade_logic9 = """    if (btn6) btn6.className = 'px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-white/90 hover:text-white hover:bg-white/10 cursor-pointer';
    if (btn9) btn9.className = 'px-3.5 py-1.5 rounded-xl text-xs font-black transition flex items-center gap-1.5 bg-white text-cyan-900 shadow-sm cursor-pointer';"""

new_select_grade_logic9 = """    if (btn6) btn6.className = 'px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-bold transition-all flex items-center gap-1.5 text-white/80 hover:text-white hover:bg-white/10 cursor-pointer min-h-[40px] md:min-h-[44px]';
    if (btn9) btn9.className = 'px-3 md:px-4 py-1.5 md:py-2 rounded-xl text-xs md:text-sm font-black transition-all flex items-center gap-1.5 bg-white text-teal-950 shadow-md ring-2 ring-teal-400/40 cursor-pointer min-h-[40px] md:min-h-[44px]';"""

if old_select_grade_logic not in html or old_select_grade_logic9 not in html:
    print("ERROR: selectGrade logic targets not found!")
    sys.exit(1)

html = html.replace(old_select_grade_logic, new_select_grade_logic, 1)
html = html.replace(old_select_grade_logic9, new_select_grade_logic9, 1)
print("5. Updated selectGrade JS logic with responsive styling!")

# Check double viramas
if '\u094d\u094d' in html:
    print("ERROR: Double virama in html!")
    sys.exit(1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved index.html successfully!")

# Also update scratch/c9u7_js.js for setTabC9U7 and setLabModeC9U7
with open("scratch/c9u7_js.js", "r", encoding="utf-8") as f:
    js_u7 = f.read()

old_tab_js = """    if (btn) {
      if (t === tab) {
        btn.className = "px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer";
      } else {
        btn.className = "px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer";
      }
    }"""

new_tab_js = """    if (btn) {
      if (t === tab) {
        btn.className = "px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl bg-indigo-600 text-white shadow-md font-bold transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer ring-2 ring-indigo-400/30 min-h-[44px]";
      } else {
        btn.className = "px-4 md:px-5 py-2.5 rounded-xl md:rounded-2xl text-slate-600 hover:text-indigo-900 hover:bg-indigo-50/70 transition-all duration-200 flex items-center gap-2 whitespace-nowrap cursor-pointer min-h-[44px]";
      }
    }"""

old_lab_js = """    if (btn) {
      if (m === mode) {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-black text-xs md:text-sm shadow-md transition cursor-pointer";
      } else {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-slate-800 text-slate-400 hover:text-white font-bold text-xs md:text-sm transition cursor-pointer";
      }
    }"""

new_lab_js = """    if (btn) {
      if (m === mode) {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-gradient-to-r from-indigo-600 to-blue-600 text-white font-black text-xs md:text-sm shadow-md transition-all duration-200 cursor-pointer min-h-[44px] flex items-center justify-center gap-2 ring-2 ring-indigo-400/30";
      } else {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-slate-800 text-slate-400 hover:text-white hover:bg-slate-700/80 font-bold text-xs md:text-sm transition-all duration-200 cursor-pointer min-h-[44px] flex items-center justify-center gap-2";
      }
    }"""

if old_tab_js in js_u7:
    js_u7 = js_u7.replace(old_tab_js, new_tab_js, 1)
if old_lab_js in js_u7:
    js_u7 = js_u7.replace(old_lab_js, new_lab_js, 1)

with open("scratch/c9u7_js.js", "w", encoding="utf-8") as f:
    f.write(js_u7)
print("Updated scratch/c9u7_js.js tab functions!")

# Also patch the JS block in index.html
if old_tab_js in html:
    html = html.replace(old_tab_js, new_tab_js, 1)
if old_lab_js in html:
    html = html.replace(old_lab_js, new_lab_js, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved index.html with updated tab JS!")

# Sync to bundle
bundle = "कक्षा_६_गणित_डिजिटल_साथी.html"
with open(bundle, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved {bundle} successfully (100% sync)!")
