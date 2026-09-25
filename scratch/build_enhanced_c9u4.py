# -*- coding: utf-8 -*-
"""
Class 9 Science Unit 4 (Evolution): Enhanced Interactive Simulator Builder
"""
import re
import os

print("Generating enhanced HTML and JS for Unit 4...")

# =========================================================================
# 1. READ EXISTING TAB 1, 2, 3, 4
# =========================================================================
with open("scratch/c9u4_html.html", "r", encoding="utf-8") as f:
    old_html = f.read()

# Replace c9u4-homology-svg with c9u4-homology-svg-wrap
old_homology_target = '''            <!-- Dynamic Skeletal Diagram Display (SVG) -->
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
                <rect x="115" y="72" width="85" height="18" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
                <text x="157" y="85" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Ulna</text>

                <!-- Wrist (Carpals) -->
                <rect x="208" y="48" width="24" height="42" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
                <text x="220" y="72" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Carpals</text>

                <!-- Digits (Metacarpals & Phalanges) -->
                <g stroke="#34d399" stroke-width="3" stroke-linecap="round">
                  <line x1="238" y1="52" x2="310" y2="40"/>
                  <line x1="238" y1="60" x2="330" y2="55"/>
                  <line x1="238" y1="69" x2="340" y2="69"/>
                  <line x1="238" y1="78" x2="330" y2="83"/>
                  <line x1="238" y1="86" x2="310" y2="98"/>
                </g>
                <text x="285" y="125" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">Metacarpals & Phalanges (५ औँलाहरू)</text>
              </svg>
            </div>'''

new_homology_target = '''            <!-- Dynamic Skeletal Diagram Display (SVG) -->
            <div id="c9u4-homology-svg-wrap" class="bg-slate-900 border border-slate-800 rounded-2xl p-4 flex flex-col items-center justify-center min-h-[190px]">
              <!-- Populated dynamically by JS renderHomologySVGC9U4() -->
            </div>'''

if old_homology_target in old_html:
    old_html = old_html.replace(old_homology_target, new_homology_target)
    print("Replaced homology svg wrap.")

# Replace Selection Mode with Enhanced Simulator
old_selection_target = '''        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
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
        </div>'''

new_selection_target = '''        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          <!-- Moth Environment Simulation Canvas -->
          <div class="lg:col-span-7 bg-slate-950/70 border border-slate-800 rounded-3xl p-5 flex flex-col justify-between space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="text-xs font-bold px-3 py-1 rounded-full bg-purple-500/20 text-purple-300" id="c9u4-moth-gen-badge">
                  पुस्ता १ (Generation 1)
                </span>
                <span id="c9u4-moth-env-label" class="text-xs font-mono text-emerald-400 font-bold">सफा वन (Clean Lichen Bark)</span>
              </div>
              <span class="text-[11px] text-slate-400">कुल मथ: १२ ओटा</span>
            </div>

            <!-- Instructional Hint Banner -->
            <div class="text-[11px] text-amber-300 bg-amber-950/40 border border-amber-800/60 rounded-xl px-3 py-1.5 flex items-center justify-between gap-2">
              <div class="flex items-center gap-1.5">
                <span>💡</span>
                <span>छलावरण नमिलेका मथमा सिधै क्लिक गरी शिकारी चरा जस्तै शिकार गर्नुहोस् वा 'अर्को पुस्ता' थिच्नुहोस्।</span>
              </div>
              <span id="c9u4-hunt-live-score" class="font-mono text-emerald-400 font-bold shrink-0">शिकार: ०</span>
            </div>

            <!-- Interactive Visual Bark with Moths (Rich Canvas) -->
            <div id="c9u4-bark-view" class="h-64 rounded-2xl border border-slate-700/80 flex items-center justify-center relative overflow-hidden transition-all shadow-inner select-none cursor-crosshair bg-slate-900">
              <!-- Rendered dynamically by JS renderMothsC9U4() -->
            </div>

            <!-- Generation Stepper & Predator Challenge Controls -->
            <div class="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-slate-800">
              <div class="flex items-center gap-2">
                <button onclick="startPredatorChallengeC9U4()" id="c9u4-btn-hunt" class="px-3.5 py-2 rounded-xl text-xs font-black bg-amber-500 hover:bg-amber-400 text-slate-950 transition flex items-center gap-1.5 cursor-pointer shadow-sm">
                  <span>🦅</span>
                  <span id="c9u4-hunt-label">शिकारी चराको खेल (१० से. शिकार चुनौती)</span>
                </button>
                <span id="c9u4-hunt-timer" class="hidden text-xs font-mono font-bold px-2.5 py-1 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/40">
                  समय: १० से.
                </span>
              </div>
              <div class="flex items-center gap-2">
                <button onclick="resetMothSimC9U4()" class="px-3 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition cursor-pointer">
                  पुनः सुरु (Reset)
                </button>
                <button onclick="stepMothGenC9U4()" id="c9u4-btn-next-gen" class="px-4 py-2 rounded-xl text-xs font-black bg-purple-600 hover:bg-purple-500 text-white shadow-md transition flex items-center gap-1.5 cursor-pointer">
                  <span>अर्को पुस्ता</span>
                  <span>➔</span>
                </button>
              </div>
            </div>

            <!-- Generation Timeline Track -->
            <div class="bg-slate-900/90 border border-slate-800 p-2.5 rounded-2xl flex items-center justify-between text-xs">
              <span class="text-slate-400 font-bold">पुस्तागत विकासक्रम (Timeline):</span>
              <div id="c9u4-gen-timeline" class="flex items-center gap-1.5 overflow-x-auto py-0.5">
                <!-- Rendered dynamically by JS -->
              </div>
            </div>
          </div>

          <!-- Population Chart & Scientific Explanation -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-3xl p-5 flex flex-col justify-between space-y-4">
            <div class="border-b border-slate-700/80 pb-2 flex items-center justify-between">
              <div>
                <span class="text-xs text-amber-400 font-mono">NATURAL SELECTION IN ACTION</span>
                <h4 class="text-lg font-black text-white">📊 जनसंख्या अनुपात (Population Ratio)</h4>
              </div>
              <span id="c9u4-advantage-badge" class="text-[10px] px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30">
                सेतो मथ अनुकूलित
              </span>
            </div>

            <!-- Live Count Badges -->
            <div class="flex items-center justify-between text-xs bg-slate-900/70 p-3 rounded-2xl border border-slate-700/60 font-mono">
              <span class="text-slate-200 flex items-center gap-2">
                <span class="w-3.5 h-3.5 rounded-full bg-slate-100 border border-slate-400 shadow-sm inline-block"></span>
                <span>सेतो मथ (Typica):</span>
                <strong id="c9u4-white-count" class="text-emerald-400 text-sm">१० ओटा</strong>
              </span>
              <span class="text-slate-200 flex items-center gap-2">
                <span class="w-3.5 h-3.5 rounded-full bg-black border border-slate-600 shadow-sm inline-block"></span>
                <span>कालो मथ (Carbonaria):</span>
                <strong id="c9u4-black-count" class="text-purple-400 text-sm">२ ओटा</strong>
              </span>
            </div>

            <!-- Ratio Bars -->
            <div class="space-y-3 text-xs">
              <div>
                <div class="flex justify-between mb-1 font-bold">
                  <span class="text-slate-300">⚪ सेतो मथ प्रतिशत:</span>
                  <span id="c9u4-white-pct" class="text-emerald-400 text-sm font-black">८५%</span>
                </div>
                <div class="w-full bg-slate-900 rounded-full h-3.5 overflow-hidden border border-slate-700">
                  <div id="c9u4-white-bar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500" style="width: 85%;"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between mb-1 font-bold">
                  <span class="text-slate-300">⚫ कालो मथ प्रतिशत:</span>
                  <span id="c9u4-black-pct" class="text-purple-400 text-sm font-black">१५%</span>
                </div>
                <div class="w-full bg-slate-900 rounded-full h-3.5 overflow-hidden border border-slate-700">
                  <div id="c9u4-black-bar" class="bg-gradient-to-r from-purple-500 to-indigo-500 h-full rounded-full transition-all duration-500" style="width: 15%;"></div>
                </div>
              </div>
            </div>

            <!-- Predator Hunt Result Banner (Appears after 10s game) -->
            <div id="c9u4-hunt-result-banner" class="hidden p-3 rounded-2xl bg-amber-950/60 border border-amber-700/80 text-xs text-amber-200 space-y-1">
              <strong class="text-amber-300 block font-bold" id="c9u4-hunt-res-title">🦅 १० सेकेन्ड शिकार नतिजा:</strong>
              <p id="c9u4-hunt-res-desc">तपाईंले शिकार गर्नुभएका मथहरू...</p>
            </div>

            <!-- Diagnostic Narrative -->
            <div class="bg-slate-900/80 p-3.5 rounded-2xl border border-slate-700 text-xs text-slate-300 space-y-1">
              <strong class="text-amber-400 block" id="c9u4-moth-diag-title">छलावरण (Camouflage) प्रभाव:</strong>
              <p id="c9u4-moth-diag-desc" class="leading-relaxed">
                सफा रुखको बोक्रामा सेतो मथ सजिलै लुक्न सक्छन्, तर कालो मथ टाढैबाट देखिने भएकाले चराहरूले सिकार गरी खाइदिन्छन्। त्यसैले प्रकृतिले सेतो मथलाई बचाउँछ।
              </p>
            </div>
          </div>
        </div>'''

if old_selection_target in old_html:
    old_html = old_html.replace(old_selection_target, new_selection_target)
    print("Replaced selection simulator HTML.")
else:
    print("ERROR: old_selection_target not found!")

# Add mutation SVG wrap
old_mutation_target = '''            <!-- Mutation Diagnostic Result -->
            <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs">'''

new_mutation_target = '''            <!-- Mutation Visual SVG Display -->
            <div id="c9u4-mutation-svg-wrap" class="bg-slate-900/90 border border-slate-800 rounded-2xl p-3 flex items-center justify-center min-h-[140px]">
              <!-- Populated dynamically by JS renderMutationSVGC9U4() -->
            </div>

            <!-- Mutation Diagnostic Result -->
            <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs">'''

if old_mutation_target in old_html:
    old_html = old_html.replace(old_mutation_target, new_mutation_target)
    print("Replaced mutation svg wrap.")

# Double virama check
assert '\u094d\u094d' not in old_html

with open("scratch/c9u4_html.html", "w", encoding="utf-8") as f:
    f.write(old_html)

print("Saved updated scratch/c9u4_html.html.")
