# -*- coding: utf-8 -*-
"""
Sets authentic textbook formatted equations into scratch/c9u7_js.js and synchronizes index.html
1. Pure math in LaTeX math blocks (no Devanagari inside math mode).
2. Proper double backslashes in JS template literals (\\frac, \\left, etc.).
3. Equation tags in beautiful badges aligned with textbook style.
4. Direct replacement into index.html and bundle.
"""
import sys
import os

c9u7_js_path = "scratch/c9u7_js.js"

with open(c9u7_js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# 1. Authentic Textbook struct-1
new_struct1 = r"""  {
    type: 'structured',
    id: 'struct-1',
    q: '४ (क). औसत गति र प्रवेगको परिभाषा लेख्नुहोस् ।',
    htmlContent: `
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-3xl mx-auto">
        <!-- Card 1: Average Velocity -->
        <div class="p-5 rounded-2xl bg-white border-2 border-blue-100 shadow-sm space-y-3">
          <div class="flex items-center justify-between border-b border-blue-100 pb-2">
            <span class="text-xs font-bold px-3 py-1 rounded-full bg-blue-600 text-white">१. औसत गति (Average Velocity)</span>
            <span class="text-xs font-mono font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded">SI: m/s</span>
          </div>
          <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
            कुनै चालमा रहेको वस्तुले पार गरेको जम्मा स्थानान्तरणलाई उक्त स्थानान्तरण पार गर्न लागेको जम्मा समयले भाग गर्दा आउने मानलाई <strong>औसत गति</strong> भनिन्छ।
          </p>
          <div class="p-3.5 rounded-xl bg-blue-50/70 border border-blue-200 text-center space-y-2">
            <span class="text-xs font-bold text-blue-900 block">पाठ्यपुस्तक सूत्र (TEXTBOOK FORMULA):</span>
            <div class="text-sm md:text-base font-serif text-blue-950">
              $$v_{av} = \\frac{s}{t}$$
            </div>
            <div class="pt-2 text-xs text-slate-600 border-t border-blue-200/60">
              समान प्रवेगको अवस्थामा: $$v_{av} = \\frac{u + v}{2}$$
            </div>
          </div>
        </div>

        <!-- Card 2: Acceleration -->
        <div class="p-5 rounded-2xl bg-white border-2 border-indigo-100 shadow-sm space-y-3">
          <div class="flex items-center justify-between border-b border-indigo-100 pb-2">
            <span class="text-xs font-bold px-3 py-1 rounded-full bg-indigo-600 text-white">२. प्रवेग (Acceleration)</span>
            <span class="text-xs font-mono font-bold text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded">SI: m/s²</span>
          </div>
          <p class="text-xs md:text-sm text-slate-700 leading-relaxed">
            समयको अन्तरालसँगै वस्तुको वेग वा गतिमा आउने परिवर्तनको दरलाई <strong>प्रवेग</strong> भनिन्छ। (समयसँगै गति घट्ने दरलाई मन्दता वा ऋणात्मक प्रवेग भनिन्छ)।
          </p>
          <div class="p-3.5 rounded-xl bg-indigo-50/70 border border-indigo-200 text-center space-y-2">
            <span class="text-xs font-bold text-indigo-900 block">पाठ्यपुस्तक सूत्र (TEXTBOOK FORMULA):</span>
            <div class="text-sm md:text-base font-serif text-indigo-950">
              $$a = \\frac{v - u}{t}$$
            </div>
            <div class="pt-2 text-xs text-slate-600 border-t border-indigo-200/60 flex items-center justify-center gap-1.5">
              <span>मन्दता (Retardation):</span>
              <span class="font-serif font-bold text-indigo-950">$$a = -a$$</span>
              <span class="text-slate-500 font-sans">(ऋणात्मक मान)</span>
            </div>
          </div>
        </div>
      </div>
    `
  },"""

# 2. Authentic Textbook struct-2
new_struct2 = r"""  {
    type: 'structured',
    id: 'struct-2',
    q: '४ (ख). सिधा रेखीय चालका ३ समीकरणहरूको निगमन गर्नुहोस् ।',
    htmlContent: `
      <div class="space-y-5 max-w-3xl mx-auto">
        <!-- Assumptions Header Box -->
        <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs md:text-sm text-amber-950 space-y-1">
          <div class="font-bold flex items-center gap-1.5 text-amber-900">
            <span>📌</span><span>पाठ्यपुस्तक प्रारम्भिक मान्यताहरू (Initial Assumptions & Symbols):</span>
          </div>
          <p class="leading-relaxed">
            मानौँ, कुनै वस्तु सुरुको गति $u$ ले सिधा रेखामा गुडिरहेको छ। समान प्रवेग $a$ का कारण $t$ समयपछि उक्त वस्तुले $s$ स्थानान्तरण पार गरी अन्तिम गति $v$ प्राप्त गर्दछ।
          </p>
        </div>

        <!-- Derivation 1: v = u + at -->
        <div class="p-5 md:p-6 rounded-2xl bg-white border border-slate-200 space-y-3 shadow-xs">
          <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
            <h5 class="font-bold text-sm md:text-base text-blue-900 flex items-center gap-2">
              <span class="w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-xs font-bold">१</span>
              पहिलो समीकरण: $v = u + at$ को निगमन (गति, प्रवेग र समय सम्बन्धी)
            </h5>
            <span class="text-xs font-bold px-3 py-1 rounded-full bg-blue-100 text-blue-800">समीकरण (i)</span>
          </div>
          <div class="space-y-2 text-xs md:text-sm text-slate-800">
            <p class="font-semibold text-slate-700">प्रवेगको परिभाषा अनुसार:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$a = \\frac{v - u}{t}$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">क्रस-गुणन (Cross-multiplication) गर्दा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$at = v - u$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">स्थान परिवर्तन गरी मिलाउँदा:</p>
            <div class="p-3.5 my-2 rounded-xl bg-gradient-to-r from-blue-50 to-indigo-50 border-2 border-blue-500 flex items-center justify-between shadow-xs">
              <div>
                <span class="text-xs font-bold text-blue-700 uppercase tracking-wider block">प्रमाणित पहिलो समीकरण:</span>
                <span class="text-xs md:text-sm font-semibold text-slate-700">गति, प्रवेग र समय सम्बन्ध</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="text-base md:text-xl font-bold text-blue-950 font-serif">
                  $$v = u + at$$
                </div>
                <span class="text-xs font-bold text-blue-800 bg-blue-100 border border-blue-300 px-2 py-1 rounded-md font-sans">समीकरण (i)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Derivation 2: v² = u² + 2as -->
        <div class="p-5 md:p-6 rounded-2xl bg-white border border-slate-200 space-y-3 shadow-xs">
          <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
            <h5 class="font-bold text-sm md:text-base text-indigo-900 flex items-center gap-2">
              <span class="w-6 h-6 rounded-full bg-indigo-600 text-white flex items-center justify-center text-xs font-bold">२</span>
              दोस्रो समीकरण: $v^2 = u^2 + 2as$ को निगमन (गति, प्रवेग र स्थानान्तरण सम्बन्धी)
            </h5>
            <span class="text-xs font-bold px-3 py-1 rounded-full bg-indigo-100 text-indigo-800">समीकरण (ii)</span>
          </div>
          <div class="space-y-2 text-xs md:text-sm text-slate-800">
            <p class="font-semibold text-slate-700">समान प्रवेगमा गुडिरहेको वस्तुको औसत गति:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$v_{av} = \\frac{u + v}{2}$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">हामीलाई थाहा छ, स्थानान्तरण = औसत गति × समय:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between text-sm md:text-base font-serif">
              <div>
                $$s = \\left(\\frac{u + v}{2}\\right) \\times t$$
              </div>
              <span class="text-xs font-bold text-slate-500 bg-slate-200/70 px-2.5 py-0.5 rounded font-sans">समीकरण (क)</span>
            </div>
            <p class="font-semibold text-slate-700 pt-1">पहिलो समीकरण $v = u + at$ बाट समय $t$ को मान निकाल्दा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between text-sm md:text-base font-serif">
              <div>
                $$v - u = at \\implies t = \\frac{v - u}{a}$$
              </div>
              <span class="text-xs font-bold text-slate-500 bg-slate-200/70 px-2.5 py-0.5 rounded font-sans">समीकरण (ख)</span>
            </div>
            <p class="font-semibold text-slate-700 pt-1">समीकरण (ख) बाट $t$ को मान समीकरण (क) मा प्रतिस्थापन गर्दा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$s = \\left(\\frac{v + u}{2}\\right) \\times \\left(\\frac{v - u}{a}\\right)$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">अंशहरू गुणन गर्दा [सूत्र: $(a+b)(a-b) = a^2 - b^2$]:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$s = \\frac{v^2 - u^2}{2a}$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">क्रस-गुणन (Cross-multiplication) गर्दा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$2as = v^2 - u^2$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">स्थान परिवर्तन गरी मिलाउँदा:</p>
            <div class="p-3.5 my-2 rounded-xl bg-gradient-to-r from-indigo-50 to-blue-50 border-2 border-indigo-500 flex items-center justify-between shadow-xs">
              <div>
                <span class="text-xs font-bold text-indigo-700 uppercase tracking-wider block">प्रमाणित दोस्रो समीकरण:</span>
                <span class="text-xs md:text-sm font-semibold text-slate-700">गति, प्रवेग र स्थानान्तरण सम्बन्ध</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="text-base md:text-xl font-bold text-indigo-950 font-serif">
                  $$v^2 = u^2 + 2as$$
                </div>
                <span class="text-xs font-bold text-indigo-800 bg-indigo-100 border border-indigo-300 px-2 py-1 rounded-md font-sans">समीकरण (ii)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Derivation 3: s = ut + 1/2at^2 -->
        <div class="p-5 md:p-6 rounded-2xl bg-white border border-slate-200 space-y-3 shadow-xs">
          <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
            <h5 class="font-bold text-sm md:text-base text-purple-900 flex items-center gap-2">
              <span class="w-6 h-6 rounded-full bg-purple-600 text-white flex items-center justify-center text-xs font-bold">३</span>
              तेस्रो समीकरण: $s = ut + \\frac{1}{2}at^2$ को निगमन (समय, प्रवेग र स्थानान्तरण सम्बन्धी)
            </h5>
            <span class="text-xs font-bold px-3 py-1 rounded-full bg-purple-100 text-purple-800">समीकरण (iii)</span>
          </div>
          <div class="space-y-2 text-xs md:text-sm text-slate-800">
            <p class="font-semibold text-slate-700">समान प्रवेगमा स्थानान्तरण = औसत गति × समय:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between text-sm md:text-base font-serif">
              <div>
                $$s = \\left(\\frac{u + v}{2}\\right) \\times t$$
              </div>
              <span class="text-xs font-bold text-slate-500 bg-slate-200/70 px-2.5 py-0.5 rounded font-sans">समीकरण (क)</span>
            </div>
            <p class="font-semibold text-slate-700 pt-1">पहिलो समीकरण $v = u + at$ बाट $v$ को मान समीकरण (क) मा राख्दा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$s = \\left(\\frac{u + (u + at)}{2}\\right) \\times t$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">अंशहरू जोड्दा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$s = \\left(\\frac{2u + at}{2}\\right) \\times t$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">भिन्नलाई छुट्याउँदा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$s = \\left(\\frac{2u}{2} + \\frac{at}{2}\\right) \\times t = \\left(u + \\frac{1}{2}at\\right) \\times t$$
            </div>
            <p class="font-semibold text-slate-700 pt-1">कोष्ठक खोली $t$ ले गुणन गर्दा:</p>
            <div class="p-3.5 my-2 rounded-xl bg-gradient-to-r from-purple-50 to-pink-50 border-2 border-purple-500 flex items-center justify-between shadow-xs">
              <div>
                <span class="text-xs font-bold text-purple-700 uppercase tracking-wider block">प्रमाणित तेस्रो समीकरण:</span>
                <span class="text-xs md:text-sm font-semibold text-slate-700">समय, प्रवेग र स्थानान्तरण सम्बन्ध</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="text-base md:text-xl font-bold text-purple-950 font-serif">
                  $$s = ut + \\frac{1}{2}at^2$$
                </div>
                <span class="text-xs font-bold text-purple-800 bg-purple-100 border border-purple-300 px-2 py-1 rounded-md font-sans">समीकरण (iii)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  },"""

# 3. Authentic Textbook struct-4
new_struct4 = r"""  {
    type: 'structured',
    id: 'struct-4',
    q: '४ (घ). दिइएको तथ्याङ्कका आधारमा स्थानान्तरण समय ग्राफको झुकावबाट पहिलो ४ सेकेन्डको औसत गति हिसाब गर्नुहोस् ।',
    htmlContent: `
      <div class="space-y-4 text-xs md:text-sm max-w-3xl mx-auto">
        <div class="overflow-x-auto">
          <table class="w-full border-collapse border border-slate-200 text-center font-mono">
            <tr class="bg-slate-100 font-bold text-slate-800">
              <td class="border border-slate-200 p-2.5 font-bold">समय (t) [s]</td>
              <td class="border border-slate-200 p-2">०</td>
              <td class="border border-slate-200 p-2">२</td>
              <td class="border border-slate-200 p-2">४</td>
              <td class="border border-slate-200 p-2">६</td>
              <td class="border border-slate-200 p-2">८</td>
              <td class="border border-slate-200 p-2">१०</td>
              <td class="border border-slate-200 p-2">१२</td>
              <td class="border border-slate-200 p-2">१४</td>
            </tr>
            <tr class="text-slate-700">
              <td class="border border-slate-200 p-2.5 font-bold">दूरी (s) [m]</td>
              <td class="border border-slate-200 p-2">०</td>
              <td class="border border-slate-200 p-2">४</td>
              <td class="border border-slate-200 p-2">८</td>
              <td class="border border-slate-200 p-2">१२</td>
              <td class="border border-slate-200 p-2">१६</td>
              <td class="border border-slate-200 p-2">२०</td>
              <td class="border border-slate-200 p-2">२४</td>
              <td class="border border-slate-200 p-2">२८</td>
            </tr>
          </table>
        </div>
        <div class="p-4 rounded-2xl bg-blue-50/70 border border-blue-200 space-y-3">
          <strong class="text-blue-900 block text-sm">पहिलो ४ सेकेन्ड (० देखि ४ s) को औसत गति हिसाब:</strong>
          <div class="space-y-1 text-slate-700">
            <div>सुरुको बिन्दु: $t_1 = 0\\text{ s}, s_1 = 0\\text{ m}$</div>
            <div>अन्तिम बिन्दु: $t_2 = 4\\text{ s}, s_2 = 8\\text{ m}$</div>
          </div>
          <p class="font-semibold text-slate-700 pt-1">औसत गति $(v)$ = झुकाव (Slope):</p>
          <div class="py-2 px-3 rounded-xl bg-white border border-blue-200 text-center md:text-left md:pl-6 text-sm md:text-base font-serif text-blue-950">
            $$v = \\frac{s_2 - s_1}{t_2 - t_1} = \\frac{8\\text{ m} - 0\\text{ m}}{4\\text{ s} - 0\\text{ s}} = \\frac{8}{4} = 2\\text{ m/s}$$
          </div>
          <div class="p-2.5 rounded-xl bg-emerald-100 text-emerald-950 font-bold text-xs md:text-sm">
            ✓ उत्तर: पहिलो ४ सेकेन्डमा वस्तुको औसत गति २ m/s (समान गति) रहेको छ।
          </div>
        </div>
      </div>
    `
  },"""

# 4. Authentic Textbook struct-11 (F = ma)
new_struct11 = r"""  {
    type: 'structured',
    id: 'struct-11',
    q: '४ (ट). न्युटनको दोस्रो नियमबाट F = ma प्रमाणित गर्नुहोस् ।',
    htmlContent: `
      <div class="bg-white border-2 border-emerald-100 rounded-2xl p-5 md:p-6 shadow-sm space-y-4 max-w-3xl mx-auto">
        <div class="text-xs md:text-sm text-slate-700 leading-relaxed border-b border-emerald-100 pb-3">
          <strong>मानौँ:</strong> $m$ पिण्ड भएको वस्तुमा $F$ परिमाणको बाहिरी असन्तुलित बल लगाउँदा $a$ प्रवेग उत्पन्न हुन्छ।
        </div>

        <div class="space-y-3 text-xs md:text-sm text-slate-800">
          <div>
            <p class="font-semibold text-slate-700">१. नियमको पहिलो खण्ड अनुसार (पिण्ड $m$ स्थिर हुँदा प्रवेग बलसँग समानुपातिक हुन्छ):</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between text-sm md:text-base font-serif">
              <div>
                $$a \\propto F$$
              </div>
              <span class="text-xs font-bold text-slate-500 bg-slate-200/70 px-2.5 py-0.5 rounded font-sans">समीकरण (१)</span>
            </div>
          </div>

          <div>
            <p class="font-semibold text-slate-700">२. नियमको दोस्रो खण्ड अनुसार (बल $F$ स्थिर हुँदा प्रवेग पिण्डसँग व्युत्क्रमानुपातिक हुन्छ):</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between text-sm md:text-base font-serif">
              <div>
                $$a \\propto \\frac{1}{m}$$
              </div>
              <span class="text-xs font-bold text-slate-500 bg-slate-200/70 px-2.5 py-0.5 rounded font-sans">समीकरण (२)</span>
            </div>
          </div>

          <div>
            <p class="font-semibold text-slate-700">३. सम्बन्ध (१) र (२) लाई संयुक्त रूपमा मिलाउँदा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 text-center md:text-left md:pl-6 text-sm md:text-base font-serif">
              $$a \\propto \\frac{F}{m} \\implies F \\propto ma$$
            </div>
          </div>

          <div>
            <p class="font-semibold text-slate-700">४. समानुपातिक चिन्ह हटाई समानुपातिक स्थिराङ्क $k$ राख्दा:</p>
            <div class="py-1.5 px-3 my-1 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-between text-sm md:text-base font-serif">
              <div>
                $$F = k \\cdot ma$$
              </div>
              <span class="text-xs font-bold text-slate-500 bg-slate-200/70 px-2.5 py-0.5 rounded font-sans">समीकरण (३)</span>
            </div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 text-xs md:text-sm text-slate-700 space-y-1">
            <strong class="text-slate-900">५. १ न्युटन ($1\\text{ N}$) बलको परिभाषा अनुसार:</strong>
            <p>$1\\text{ kg}$ पिण्ड भएको वस्तुमा $1\\text{ m/s}^2$ प्रवेग उत्पन्न गराउने बललाई $1\\text{ N}$ भनिन्छ।<br>
            अर्थात् $m = 1\\text{ kg}, a = 1\\text{ m/s}^2$ हुँदा $F = 1\\text{ N}$ हुन्छ।<br>
            यो मान समीकरण (३) मा राख्दा: $1 = k \\times 1 \\times 1 \\implies \\mathbf{k = 1}$ हुन्छ।</p>
          </div>

          <div class="mt-4 p-4 rounded-xl bg-gradient-to-r from-emerald-50 to-teal-50 border-2 border-emerald-500 flex items-center justify-between shadow-xs">
            <div>
              <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider block">$k = 1$ को मान समीकरण (३) मा राख्दा:</span>
              <span class="text-sm md:text-base font-bold text-slate-800">💡 न्युटनको चाल सम्बन्धी दोस्रो नियम</span>
            </div>
            <div class="flex items-center gap-3">
              <div class="text-lg md:text-xl font-bold text-emerald-950 font-serif">
                $$\\mathbf{F = ma}$$
              </div>
              <span class="text-xs font-bold text-emerald-800 bg-emerald-100 border border-emerald-300 px-2.5 py-1 rounded-md font-sans">प्रमाणित</span>
            </div>
          </div>
        </div>
      </div>
    `
  },"""

# 5. Authentic Textbook Numericals (५ क देखि ङ)
new_numericals = r"""  // 5. Numerical Problems (५ वटा पूर्ण - ५ क देखि ङ सम्म)
  {
    type: 'numerical',
    id: 'num-1',
    q: '५ (क). स्थिर अवस्थाबाट धावनमार्गमा दक्षिणतर्फ गुड्दा हवाईजहाजको स्थानान्तरण र गति',
    given: '• सुरुको गति ($u$) = $0\\text{ m/s}$ (स्थिर अवस्थाबाट धावनमार्गमा गुड्न सुरु गरेको)<br>• समान प्रवेग ($a$) = $+1.5\\text{ m/s}^2$ (दक्षिणतर्फ)<br>• उड्न लागेको समय ($t$) = $30\\text{ s}$',
    formula: '• पार गरेको स्थानान्तरण: $s = ut + \\frac{1}{2}at^2$<br>• उड्नुपूर्वको अन्तिम गति: $v = u + at$',
    calc: '<div class="space-y-3"><div><strong>१. स्थानान्तरणका लागि:</strong><br>$$s = (0 \\times 30) + \\frac{1}{2} \\times 1.5 \\times (30)^2 = 0 + 0.75 \\times 900 = 675\\text{ m}$$ <span class="text-xs font-semibold text-slate-600 font-sans">(दक्षिणतर्फ)</span></div><div><strong>२. जमिन छोड्नुपूर्वको गतिको लागि:</strong><br>$$v = 0 + (1.5 \\times 30) = 45\\text{ m/s}$$ <span class="text-xs font-semibold text-slate-600 font-sans">(दक्षिणतर्फ) [45 × 3.6 = 162 km/h]</span></div></div>',
    res: 'स्थानान्तरण = ६७५ m (दक्षिण) र उड्नुपूर्वको गति = ४५ m/s (दक्षिण)'
  },
  {
    type: 'numerical',
    id: 'num-2',
    q: '५ (ख). पुलबाट नदीको पानीमा ढुङ्गा खसाल्दा पानीको सतहबाट पुलको उचाइ',
    given: '• सुरुको गति ($u$) = $0\\text{ m/s}$ (स्वतन्त्र रूपमा खसालिएको)<br>• गुरुत्वप्रवेग ($g$) = $9.8\\text{ m/s}^2$<br>• पानीसम्म पुग्न लागेको समय ($t$) = $2\\text{ s}$',
    formula: '• ठाडो खसाइको उचाइ सूत्र: $h = ut + \\frac{1}{2}gt^2$<br>• पानी छुँदाको अन्तिम गति: $v = u + gt$',
    calc: '<div class="space-y-3"><div><strong>१. पुलको उचाइका लागि:</strong><br>$$h = (0 \\times 2) + \\frac{1}{2} \\times 9.8 \\times (2)^2 = 0 + 4.9 \\times 4 = 19.6\\text{ m}$$</div><div><strong>२. पानी छुँदाको गतिको लागि:</strong><br>$$v = 0 + (9.8 \\times 2) = 19.6\\text{ m/s}$$ <span class="text-xs font-semibold text-slate-600 font-sans">(तलतिर)</span></div></div>',
    res: 'पुलको उचाइ = १९.६ m र पानी छुँदाको गति = १९.६ m/s'
  },
  {
    type: 'numerical',
    id: 'num-3',
    q: '५ (ग). सुरज र साइकलको ओरालो चालमा उत्पन्न प्रवेग र लागेको बल',
    given: '• सुरज र साइकलको कुल पिण्ड ($m$) = $65\\text{ kg}$<br>• सुरुको गति ($u$) = $0\\text{ m/s}$ (स्थिर अवस्थाबाट)<br>• अन्तिम गति ($v$) = $10\\text{ m/s}$<br>• समय ($t$) = $5\\text{ s}$',
    formula: '• प्रवेग: $a = \\frac{v - u}{t}$<br>• लागेको परिणामात्मक बल: $F = ma$',
    calc: '<div class="space-y-3"><div><strong>१. उत्पन्न प्रवेगको हिसाब:</strong><br>$$a = \\frac{10 - 0}{5} = \\frac{10}{5} = 2\\text{ m/s}^2$$</div><div><strong>२. परिणामात्मक बलको हिसाब:</strong><br>$$F = ma = 65\\text{ kg} \\times 2\\text{ m/s}^2 = 130\\text{ N}$$</div></div>',
    res: 'प्रवेग = २ m/s² र लागेको बल = १३० N'
  },
  {
    type: 'numerical',
    id: 'num-4',
    q: '५ (घ). गुडिरहेको कारमा ब्रेक लगाउँदा उत्पन्न मन्दन, बल र पार गरेको दूरी',
    given: '• कारको पिण्ड ($m$) = $1500\\text{ kg}$<br>• सुरुको गति ($u$) = $54\\text{ km/h} = \\frac{54 \\times 1000}{3600} = 15\\text{ m/s}$<br>• अन्तिम गति ($v$) = $0\\text{ m/s}$ (कार रोकिएको)<br>• समय ($t$) = $4\\text{ s}$',
    formula: '• प्रवेग (मन्दता): $a = \\frac{v - u}{t}$<br>• गतिरोधक बल: $F = ma$<br>• पार गरेको दूरी: $s = ut + \\frac{1}{2}at^2$',
    calc: '<div class="space-y-3"><div><strong>१. प्रवेग (मन्दता):</strong><br>$$a = \\frac{0 - 15}{4} = -3.75\\text{ m/s}^2$$ <span class="text-xs font-semibold text-slate-600 font-sans">(मन्दता = 3.75 m/s²)</span></div><div><strong>२. गतिरोधक बल:</strong><br>$$F = 1500 \\times (-3.75) = -5625\\text{ N}$$ <span class="text-xs font-semibold text-slate-600 font-sans">(दिशा: चालको विपरित)</span></div><div><strong>३. रोकिन पार गरेको दूरी:</strong><br>$$s = (15 \\times 4) + \\frac{1}{2} \\times (-3.75) \\times (4)^2 = 60 - 30 = 30\\text{ m}$$</div></div>',
    res: 'मन्दता = ३.७५ m/s², गतिरोधक बल = ५६२५ N, रोकिन लागेको दूरी = ३० m'
  },
  {
    type: 'numerical',
    id: 'num-5',
    q: '५ (ङ). गति-समय ग्राफको खण्ड CD मा प्रवेग र पार गरेको स्थानान्तरण',
    given: '• गति-समय ग्राफको खण्ड CD मा रेखा तेर्सो भएकाले गति स्थिर ($v = 20\\text{ m/s}$) छ।<br>• खण्ड CD को समय: $t = 14\\text{ s} - 10\\text{ s} = 4\\text{ s}$',
    formula: '• प्रवेग: $a = \\frac{v_2 - v_1}{t_2 - t_1}$<br>• स्थानान्तरण: $s = v \\times t$ (रेखा मुनिको आयतको क्षेत्रफल)',
    calc: '<div class="space-y-3"><div><strong>१. प्रवेग:</strong><br>$$a = \\frac{20 - 20}{14 - 10} = \\frac{0}{4} = 0\\text{ m/s}^2$$ <span class="text-xs font-semibold text-slate-600 font-sans">(समान चालका कारण प्रवेग शून्य)</span></div><div><strong>२. पार गरेको स्थानान्तरण:</strong><br>$$s = 20\\text{ m/s} \\times 4\\text{ s} = 80\\text{ m}$$ <span class="text-xs font-semibold text-slate-600 font-sans">(पूर्वतर्फ)</span></div></div>',
    res: 'खण्ड CD को प्रवेग = ० m/s² र स्थानान्तरण = ८० m पूर्व'
  },
"""

# Pattern replace struct-1 to struct-3
s1_idx = js_content.find("id: 'struct-1'")
s3_idx = js_content.find("id: 'struct-3'")
open_brace_s1 = js_content.rfind("{", 0, s1_idx)
open_brace_s3 = js_content.rfind("{", 0, s3_idx)
js_content = js_content[:open_brace_s1] + new_struct1 + "\n" + new_struct2 + "\n" + js_content[open_brace_s3:]

# Pattern replace struct-4 to struct-5
s4_idx = js_content.find("id: 'struct-4'")
s5_idx = js_content.find("id: 'struct-5'")
open_brace_s4 = js_content.rfind("{", 0, s4_idx)
open_brace_s5 = js_content.rfind("{", 0, s5_idx)
js_content = js_content[:open_brace_s4] + new_struct4 + "\n" + js_content[open_brace_s5:]

# Pattern replace struct-11 to struct-12
s11_idx = js_content.find("id: 'struct-11'")
s12_idx = js_content.find("id: 'struct-12'")
open_brace_s11 = js_content.rfind("{", 0, s11_idx)
open_brace_s12 = js_content.rfind("{", 0, s12_idx)
js_content = js_content[:open_brace_s11] + new_struct11 + "\n" + js_content[open_brace_s12:]

# Pattern replace numericals
num_start = js_content.find("// 5. Numerical Problems")
proj_start = js_content.find("// 6. Project Works")
js_content = js_content[:num_start] + new_numericals + "\n\n  " + js_content[proj_start:]

# Check double viramas in js_content
if '\u094d\u094d' in js_content:
    print("ERROR: Double virama detected in c9u7_js!")
    sys.exit(1)

with open(c9u7_js_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print(f"Updated {c9u7_js_path}!")

# Now patch index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

m1_str = "// CLASS 9 SCIENCE: UNIT 7 - FORCE AND MOTION (बल र चाल)"
m2_str = "const urlParams = new URLSearchParams(window.location.search);"

# Find start of the comment block above m1_str
m1_pos = html.find(m1_str)
if m1_pos == -1:
    print("ERROR: m1_str not found in index.html!")
    sys.exit(1)

# Find the separator line right before m1_str
line_start = html.rfind("// =========================================================================", 0, m1_pos)
if line_start == -1:
    line_start = m1_pos

m2_pos = html.find(m2_str)
if m2_pos == -1:
    print("ERROR: m2_str not found in index.html!")
    sys.exit(1)

html = html[:line_start] + js_content.strip() + "\n\n  " + html[m2_pos:]

if '\u094d\u094d' in html:
    print("ERROR: Double virama in html!")
    sys.exit(1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html!")

# Bundle sync
bundle = "कक्षा_६_गणित_डिजिटल_साथी.html"
with open(bundle, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated {bundle} (100% sync)!")
