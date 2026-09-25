# generate_ch4_html.py
# Generates complete Chapter 4 HTML snippet for portal

def get_ch4_html():
    return r'''
      <!-- ================= CHAPTER 4 VIEW: FRACTIONS ================= -->
      <div id="chapter-view-4" class="hidden flex-1 flex flex-col">
        <!-- Top Chapter Banner -->
        <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-blue-600 mb-1">एकाइ २: अङ्कगणित (Unit 2: Arithmetic)</div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ ४: भिन्न (Fractions)</h2>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ ५३–७५</span>
            <span class="text-xs bg-blue-100 text-blue-800 font-bold px-3 py-1 rounded-xl border border-blue-200">अभ्यास ४.१ देखि ४.५ सम्म</span>
          </div>
        </div>

        <!-- Chapter 4 Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button id="ch4-tab-concepts" onclick="setTabCh4('concepts')" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap">
            १. अवधारणा र नियमहरू
          </button>
          <button id="ch4-tab-exercises" onclick="setTabCh4('exercises')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            २. सम्पूर्ण अभ्यासहरू (४.१ – ४.५)
          </button>
          <button id="ch4-tab-tiers" onclick="setTabCh4('tiers')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ३. तीन तहका नमुना प्रश्नहरू
          </button>
          <button id="ch4-tab-quiz" onclick="setTabCh4('quiz')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ४. आत्म-मूल्याङ्कन क्विज
          </button>
        </div>

        <!-- ================= CH4 TAB 1: CONCEPTS ================= -->
        <div id="ch4-view-concepts" class="space-y-6">
          
          <!-- Concept 1: Definition & Visual Model -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-base">🍰</span>
              भिन्नको परिचय र संरचना (Introduction & Visual Fraction Model)
            </h3>
            <p class="text-xs md:text-sm text-slate-600 mb-4">
              कुनै एउटा सिंगो (Whole) वस्तु वा समूहलाई बराबर भागहरूमा बाँड्दा त्यसको केही भागलाई जनाउने गणितीय रूपलाई <strong>भिन्न (Fraction)</strong> भनिन्छ।
            </p>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
              <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl text-center">
                <span class="text-xs font-bold text-blue-600 uppercase tracking-wider block mb-1">अंश (Numerator)</span>
                <span class="text-2xl font-black text-blue-900 font-mono">a</span>
                <p class="text-xs text-blue-800 mt-1">सिंगो वस्तुबाट लिइएको वा छानिएको भाग</p>
              </div>
              <div class="p-4 bg-indigo-50 border border-indigo-200 rounded-xl text-center">
                <span class="text-xs font-bold text-indigo-600 uppercase tracking-wider block mb-1">विभाजक रेखा (Fraction Bar)</span>
                <span class="text-2xl font-black text-indigo-900 font-mono">—</span>
                <p class="text-xs text-indigo-800 mt-1">अंश र हरलाई छुट्याउने भाग रेखा</p>
              </div>
              <div class="p-4 bg-purple-50 border border-purple-200 rounded-xl text-center">
                <span class="text-xs font-bold text-purple-600 uppercase tracking-wider block mb-1">हर (Denominator)</span>
                <span class="text-2xl font-black text-purple-900 font-mono">b</span>
                <p class="text-xs text-purple-800 mt-1">जम्मा बराबर भागहरूको सङ्ख्या ($b \neq 0$)</p>
              </div>
            </div>

            <!-- Vector SVG Fraction Strip Model -->
            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-center">
              <span class="text-xs font-bold text-slate-600 block mb-2">भिन्न स्ट्रिप मोडलिङ (Visual Fraction Strips: $\frac{1}{2}, \frac{2}{4}, \frac{4}{8}$)</span>
              <svg viewBox="0 0 600 130" class="w-full max-w-xl mx-auto overflow-visible">
                <!-- Whole Bar -->
                <rect x="10" y="5" width="580" height="24" fill="#3b82f6" rx="4" />
                <text x="300" y="21" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">१ सिंगो भाग (Whole = 1)</text>

                <!-- 1/2 Split -->
                <rect x="10" y="35" width="288" height="24" fill="#059669" rx="4" />
                <rect x="302" y="35" width="288" height="24" fill="#cbd5e1" rx="4" />
                <text x="154" y="51" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">१/२ (आधा भाग)</text>
                <text x="446" y="51" text-anchor="middle" fill="#475569" font-size="12" font-weight="bold">१/२</text>

                <!-- 1/4 Split -->
                <rect x="10" y="65" width="142" height="24" fill="#0d9488" rx="4" />
                <rect x="156" y="65" width="142" height="24" fill="#0d9488" rx="4" />
                <rect x="302" y="65" width="142" height="24" fill="#cbd5e1" rx="4" />
                <rect x="448" y="65" width="142" height="24" fill="#cbd5e1" rx="4" />
                <text x="81" y="81" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">१/४</text>
                <text x="227" y="81" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">१/४</text>
                <text x="373" y="81" text-anchor="middle" fill="#475569" font-size="11">१/४</text>
                <text x="519" y="81" text-anchor="middle" fill="#475569" font-size="11">१/४</text>

                <!-- 1/8 Split -->
                <g fill="#0284c7">
                  <rect x="10" y="95" width="69" height="24" rx="3" />
                  <rect x="83" y="95" width="69" height="24" rx="3" />
                  <rect x="156" y="95" width="69" height="24" rx="3" />
                  <rect x="229" y="95" width="69" height="24" rx="3" />
                </g>
                <g fill="#cbd5e1">
                  <rect x="302" y="95" width="69" height="24" rx="3" />
                  <rect x="375" y="95" width="69" height="24" rx="3" />
                  <rect x="448" y="95" width="69" height="24" rx="3" />
                  <rect x="521" y="95" width="69" height="24" rx="3" />
                </g>
                <text x="154" y="111" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">४ वटा १/८ = ४/८ (समतुल्य)</text>
                <text x="446" y="111" text-anchor="middle" fill="#475569" font-size="11">४/८</text>
              </svg>
            </div>
          </div>

          <!-- Concept 2: Types of Fractions -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-4 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center text-base">📊</span>
              भिन्नका प्रकारहरू (Classification of Fractions)
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Proper -->
              <div class="p-4 border border-blue-200 bg-blue-50/50 rounded-xl space-y-2">
                <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">१. उचित भिन्न (Proper)</span>
                <p class="text-xs text-slate-700">अंश हरभन्दा सानो ($a < b$) हुने भिन्न। यसको मान सधैँ $१$ भन्दा कम हुन्छ।</p>
                <div class="p-2 bg-white rounded border border-blue-100 font-mono text-xs text-blue-900 text-center font-bold">
                  $$\frac{1}{2}, \quad \frac{2}{3}, \quad \frac{3}{5}, \quad \frac{7}{10} < 1$$
                </div>
              </div>
              <!-- Improper -->
              <div class="p-4 border border-purple-200 bg-purple-50/50 rounded-xl space-y-2">
                <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-purple-100 text-purple-800">२. अनुचित भिन्न (Improper)</span>
                <p class="text-xs text-slate-700">अंश हरसँग बराबर वा हरभन्दा ठूलो ($a \ge b$) हुने भिन्न। यसको मान $\ge 1$ हुन्छ।</p>
                <div class="p-2 bg-white rounded border border-purple-100 font-mono text-xs text-purple-900 text-center font-bold">
                  $$\frac{3}{2}, \quad \frac{5}{3}, \quad \frac{7}{4}, \quad \frac{9}{5} \ge 1$$
                </div>
              </div>
              <!-- Mixed -->
              <div class="p-4 border border-emerald-200 bg-emerald-50/50 rounded-xl space-y-2">
                <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-800">३. मिश्रित भिन्न (Mixed)</span>
                <p class="text-xs text-slate-700">पूर्ण सङ्ख्या र उचित भिन्न मिलेर बनेको रूप। जस्तै: $2\frac{3}{4}$।</p>
                <div class="p-2 bg-white rounded border border-emerald-100 font-mono text-xs text-emerald-900 text-center font-bold">
                  $$2\frac{3}{4} = \frac{(2 \times 4) + 3}{4} = \frac{11}{4}$$
                </div>
              </div>
            </div>
          </div>

          <!-- Concept 3: Operations & Rules Summary Table -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-4 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-base">⚙️</span>
              भिन्नका मुख्य गणितीय नियमहरू (Core Rules & Operations)
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-sm flex items-center gap-1.5">
                  <span class="text-blue-600">➕</span> जोड र घटाउ (Addition & Subtraction)
                </h4>
                <p class="text-slate-600">असमान हर भएमा पहिले हरहरूको <strong>ल.स. (LCM)</strong> निकाली समान हर बनाउने र अंशहरूको जोड/घटाउ गर्ने:</p>
                <div class="p-2 bg-white rounded border font-mono text-center">
                  $$\frac{a}{b} + \frac{c}{d} = \frac{a \cdot d + b \cdot c}{b \cdot d}$$
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-sm flex items-center gap-1.5">
                  <span class="text-emerald-600">✖️</span> गुणन र 'को' नियम (Multiplication & 'Of')
                </h4>
                <p class="text-slate-600">अंशलाई अंशसँग र हरलाई हरसँग गुणन गर्ने। 'को' को अर्थ गुणन हुन्छ:</p>
                <div class="p-2 bg-white rounded border font-mono text-center">
                  $$\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}$$
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-sm flex items-center gap-1.5">
                  <span class="text-rose-600">➗</span> भाग र व्युत्क्रम (Division & Reciprocal)
                </h4>
                <p class="text-slate-600">भाग चिह्नलाई गुणनमा बदली भाजक भिन्नलाई त्यसको <strong>व्युत्क्रम (उल्टो)</strong> भिन्नले गुणन गर्ने:</p>
                <div class="p-2 bg-white rounded border font-mono text-center">
                  $$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{a \times d}{b \times c}$$
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-sm flex items-center gap-1.5">
                  <span class="text-purple-600">⚖️</span> भिन्नहरूको तुलना (Comparison Rules)
                </h4>
                <p class="text-slate-600">छड्के गुणन (Cross Multiplication) वा समान हर विधिबाट ठूलो/सानो पत्ता लगाउने:</p>
                <div class="p-2 bg-white rounded border font-mono text-center">
                  $$a \times d > b \times c \implies \frac{a}{b} > \frac{c}{d}$$
                </div>
              </div>
            </div>

            <!-- Warning Alert Box -->
            <div class="mt-4 p-3 bg-amber-50 rounded-xl border border-amber-200 text-amber-900 text-xs flex items-start gap-2">
              <span class="text-base">⚠️</span>
              <div>
                <strong>विद्यार्थीहरूले ध्यान दिनुपर्ने सामान्य गल्ती:</strong>
                भिन्न जोड्दा अंश र हर दुवै सोझै जोड्नु पूर्णतः गलत हो (जस्तै: $\frac{1}{2} + \frac{1}{3} \neq \frac{2}{5}$)। सधैँ पहिले हरहरूको ल.स. निकालेर समान हर बनाएपछि मात्र अंश जोड्नुपर्छ ($\frac{3}{6} + \frac{2}{6} = \frac{5}{6}$)।
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH4 TAB 2: EXERCISES ================= -->
        <div id="ch4-view-exercises" class="hidden space-y-6">
          
          <!-- Sub-tab exercise selector pills -->
          <div class="flex gap-2 overflow-x-auto pb-2 border-b border-slate-200 text-xs font-bold">
            <button id="ch4-pill-ex4_1" onclick="setExerciseCh4('ex4_1')" class="px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap">
              अभ्यास ४.१ (समतुल्य भिन्न)
            </button>
            <button id="ch4-pill-ex4_2" onclick="setExerciseCh4('ex4_2')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              अभ्यास ४.२ (तुलना र क्रम)
            </button>
            <button id="ch4-pill-ex4_3" onclick="setExerciseCh4('ex4_3')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              अभ्यास ४.३ (जोड र घटाउ)
            </button>
            <button id="ch4-pill-ex4_4_1" onclick="setExerciseCh4('ex4_4_1')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              अभ्यास ४.४.१ (भिन्न × पूर्ण सङ्ख्या)
            </button>
            <button id="ch4-pill-ex4_4_2" onclick="setExerciseCh4('ex4_4_2')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              अभ्यास ४.४.२ (भिन्न × भिन्न)
            </button>
            <button id="ch4-pill-ex4_5" onclick="setExerciseCh4('ex4_5')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              अभ्यास ४.५ (भिन्नको भाग)
            </button>
          </div>

          <!-- ---------------- SUB-TAB 4.1 ---------------- -->
          <div id="ch4-sec-ex4_1" class="space-y-4">
            <div class="border-b border-slate-200 pb-2">
              <h3 class="text-lg font-black text-slate-900">अभ्यास ४.१: भिन्न र समतुल्य भिन्न</h3>
              <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ ५६–५७ का सम्पूर्ण प्रश्नहरूको पूर्ण समाधान</p>
            </div>

            <!-- Q1 -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न १</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">तल दिइएका चित्रमा दिइएको भिन्न जनाउने भागमा रङ्ग लगाउने:</p>
              <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
                <div class="p-2.5 bg-slate-50 rounded-xl border text-center">
                  <strong>(क) $\frac{2}{5}$:</strong> ५ भागमध्ये २ भाग रङ्ग्याउने
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border text-center">
                  <strong>(ख) $\frac{1}{4}$:</strong> ४ भागमध्ये १ भाग रङ्ग्याउने
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border text-center">
                  <strong>(ग) $\frac{5}{6}$:</strong> ६ भागमध्ये ५ भाग रङ्ग्याउने
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border text-center">
                  <strong>(घ) $\frac{2}{3}$:</strong> ३ भागमध्ये २ भाग रङ्ग्याउने
                </div>
              </div>
            </div>

            <!-- Q2 & Q3 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q2 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न २</span>
                <p class="text-xs md:text-sm text-slate-800 font-bold">चित्रलाई दुई बराबर भाग लगाई बन्ने नयाँ भिन्न लेख्ने:</p>
                <div class="space-y-1.5 text-xs text-slate-700">
                  <p>• (क) सुरुको $\frac{1}{2}$ लाई दुई भाग गर्दा: $\frac{1 \times 2}{2 \times 2} = \mathbf{\frac{2}{4}}$</p>
                  <p>• (ख) सुरुको $\frac{1}{3}$ लाई दुई भाग गर्दा: $\frac{1 \times 2}{3 \times 2} = \mathbf{\frac{2}{6}}$</p>
                  <p>• (ग) सुरुको $\frac{1}{4}$ लाई दुई भाग गर्दा: $\frac{1 \times 2}{4 \times 2} = \mathbf{\frac{2}{8}}$</p>
                  <p>• (घ) सुरुको $\frac{2}{3}$ लाई दुई भाग गर्दा: $\frac{2 \times 2}{3 \times 2} = \mathbf{\frac{4}{6}}$</p>
                </div>
              </div>

              <!-- Q3 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ३</span>
                <p class="text-xs md:text-sm text-slate-800 font-bold">खाली ठाउँमा उपयुक्त सङ्ख्या भर्ने:</p>
                <div class="space-y-1.5 text-xs font-mono">
                  <p>• (क) $\frac{3}{7} = \frac{\mathbf{21}}{49}$ ($7 \times 7 = 49$, सो $3 \times 7 = 21$)</p>
                  <p>• (ख) $\frac{2}{9} = \frac{14}{\mathbf{63}}$ ($2 \times 7 = 14$, सो $9 \times 7 = 63$)</p>
                  <p>• (ग) $\frac{1}{5} = \frac{\mathbf{6}}{30}$ ($5 \times 6 = 30$, सो $1 \times 6 = 6$)</p>
                  <p>• (घ) $\frac{3}{11} = \frac{12}{\mathbf{44}}$ ($3 \times 4 = 12$, सो $11 \times 4 = 44$)</p>
                </div>
              </div>
            </div>

            <!-- Q4 & Q5 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q4 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ४</span>
                <p class="text-xs md:text-sm text-slate-800 font-bold">प्रत्येकका २/२ वटा समतुल्य भिन्नहरू:</p>
                <div class="space-y-1 text-xs font-mono">
                  <p>• (क) $\frac{2}{5} \rightarrow \mathbf{\frac{4}{10}, \; \frac{6}{15}}$</p>
                  <p>• (ख) $\frac{1}{7} \rightarrow \mathbf{\frac{2}{14}, \; \frac{3}{21}}$</p>
                  <p>• (ग) $\frac{5}{8} \rightarrow \mathbf{\frac{10}{16}, \; \frac{15}{24}}$</p>
                  <p>• (घ) $\frac{4}{9} \rightarrow \mathbf{\frac{8}{18}, \; \frac{12}{27}}$</p>
                </div>
              </div>

              <!-- Q5 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ५</span>
                <p class="text-xs md:text-sm text-slate-800 font-bold">हरमा १६ आउने समतुल्य भिन्न:</p>
                <div class="space-y-1 text-xs font-mono">
                  <p>• (क) $\frac{1}{2} = \frac{1 \times 8}{2 \times 8} = \mathbf{\frac{8}{16}}$</p>
                  <p>• (ख) $\frac{3}{4} = \frac{3 \times 4}{4 \times 4} = \mathbf{\frac{12}{16}}$</p>
                  <p>• (ग) $\frac{5}{8} = \frac{5 \times 2}{8 \times 2} = \mathbf{\frac{10}{16}}$</p>
                  <p>• (घ) $\frac{1}{4} = \frac{1 \times 4}{4 \times 4} = \mathbf{\frac{4}{16}}$</p>
                </div>
              </div>
            </div>

            <!-- Q6 & Q7 -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ६ र ७</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">समतुल्य भिन्न पहिचान तथा तालिका भर्ने:</p>
              <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs">
                <p><strong>प्रश्न ६:</strong> (क) $\frac{1}{2} = \frac{2}{4}$ र $\frac{2}{3} = \frac{6}{9}$। (ख) $\frac{3}{4} = \frac{9}{12}$ र $\frac{4}{7} = \frac{12}{21}$।</p>
                <p><strong>प्रश्न ७:</strong></p>
                <p class="font-mono">• $\frac{4}{9} = \frac{8}{18} = \frac{12}{27} = \frac{16}{36} = \frac{20}{45}$</p>
                <p class="font-mono">• $\frac{2}{3} = \frac{10}{15} = \frac{12}{18} = \frac{14}{21} = \frac{16}{24}$</p>
                <p class="font-mono">• $\frac{1}{3} = \frac{2}{6} = \frac{3}{9} = \frac{4}{12} = \frac{5}{15}$</p>
              </div>
            </div>
          </div>

          <!-- ---------------- SUB-TAB 4.2 ---------------- -->
          <div id="ch4-sec-ex4_2" class="hidden space-y-4">
            <div class="border-b border-slate-200 pb-2">
              <h3 class="text-lg font-black text-slate-900">अभ्यास ४.२: भिन्नहरूको तुलना र क्रम</h3>
              <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ ६१ का सम्पूर्ण प्रश्नहरूको पूर्ण समाधान</p>
            </div>

            <!-- Q1: Convert to like denominators -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न १</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">समान हर भएका भिन्नमा बदल्ने (ल.स. विधि):</p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs font-mono">
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (क) $\frac{3}{4}$ र $\frac{1}{5}$ (ल.स. २०): $\mathbf{\frac{15}{20}}$ र $\mathbf{\frac{4}{20}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ख) $\frac{5}{7}$ र $\frac{3}{5}$ (ल.स. ३५): $\mathbf{\frac{25}{35}}$ र $\mathbf{\frac{21}{35}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ग) $\frac{4}{7}$ र $\frac{8}{9}$ (ल.स. ६३): $\mathbf{\frac{36}{63}}$ र $\mathbf{\frac{56}{63}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (घ) $\frac{1}{3}$ र $\frac{2}{5}$ (ल.स. १५): $\mathbf{\frac{5}{15}}$ र $\mathbf{\frac{6}{15}}$
                </div>
              </div>
            </div>

            <!-- Q2 & Q3 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q2: Fill <, >, = -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न २</span>
                <p class="text-xs md:text-sm text-slate-800 font-bold">खाली ठाउँमा $<, >$ र $=$ भर्ने:</p>
                <div class="space-y-1.5 text-xs font-mono">
                  <p>• (क) $\frac{2}{3} \mathbf{>} \frac{3}{8}$ ($2 \times 8 = 16 > 3 \times 3 = 9$)</p>
                  <p>• (ख) $\frac{2}{7} \mathbf{<} \frac{3}{5}$ ($2 \times 5 = 10 < 7 \times 3 = 21$)</p>
                  <p>• (ग) $\frac{2}{9} \mathbf{<} \frac{5}{8}$ ($2 \times 8 = 16 < 9 \times 5 = 45$)</p>
                  <p>• (घ) $3\frac{1}{3} \mathbf{=} \frac{10}{3}$ ($3\frac{1}{3} = \frac{10}{3}$)</p>
                </div>
              </div>

              <!-- Q3: Find greater fraction -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ३</span>
                <p class="text-xs md:text-sm text-slate-800 font-bold">ठूलो भिन्न छुट्याउने:</p>
                <div class="space-y-1.5 text-xs font-mono">
                  <p>• (क) $\frac{5}{6}$ र $\frac{7}{8}$ (ल.स. २४): $\frac{20}{24} < \frac{21}{24} \implies \mathbf{\frac{7}{8}}$</p>
                  <p>• (ख) $\frac{9}{7}$ र $\frac{5}{6}$ (अनुचित vs उचित): $\mathbf{\frac{9}{7}}$</p>
                  <p>• (ग) $\frac{3}{8}$ र $\frac{9}{20}$ (ल.स. ४०): $\frac{15}{40} < \frac{18}{40} \implies \mathbf{\frac{9}{20}}$</p>
                  <p>• (घ) $\frac{2}{3}$ र $\frac{3}{4}$ (ल.स. १२): $\frac{8}{12} < \frac{9}{12} \implies \mathbf{\frac{3}{4}}$</p>
                </div>
              </div>
            </div>

            <!-- Q4: Ascending Order -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ४</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">आरोही क्रम (सानोबाट ठूलो): $\frac{4}{5}, \frac{3}{4}, \frac{9}{10}$</p>
              <div class="p-3 bg-slate-50 rounded-xl text-xs space-y-1">
                <p>हरहरू ५, ४, १० को ल.स. $= 20$। समान हर बनाउँदा:</p>
                <p class="font-mono">$$\frac{3}{4} = \frac{15}{20}, \quad \frac{4}{5} = \frac{16}{20}, \quad \frac{9}{10} = \frac{18}{20}$$</p>
                <p class="font-bold text-emerald-800">उत्तर (आरोही क्रम): $\frac{3}{4}, \; \frac{4}{5}, \; \frac{9}{10}$</p>
              </div>
            </div>

            <!-- Q5 to Q8: Word problems -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ५ (रोटी समस्या)</span>
                <p>दीपा $= \frac{2}{3} = \frac{14}{21}$, दिपेश $= \frac{5}{7} = \frac{15}{21}$।</p>
                <p class="font-bold text-emerald-800">उत्तर: दिपेशले बढी रोटी खाएछन् ($15 > 14$)।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ६ (खम्बा रङ्ग समस्या)</span>
                <p>कालो $= \frac{2}{3} = \frac{16}{24}$, सेतो $= \frac{7}{8} = \frac{21}{24}$।</p>
                <p class="font-bold text-emerald-800">उत्तर: सेतो रङ्ग लगाएको भाग बढी छ ($21 > 16$)।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ७ (आम्दानी खर्च समस्या)</span>
                <p>खाना $= \frac{2}{7} = \frac{18}{63}$, शिक्षा $= \frac{5}{9} = \frac{35}{63}$।</p>
                <p class="font-bold text-emerald-800">उत्तर: खानामा कम खर्च गरिछन् ($18 < 35$)।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ८ (केक समस्या)</span>
                <p>बिहान $= \frac{1}{3} = \frac{5}{15}$, बेलुकी $= \frac{3}{5} = \frac{9}{15}$।</p>
                <p class="font-bold text-emerald-800">उत्तर: बिहानमा थोरै केक खाएछन् ($5 < 9$)।</p>
              </div>
            </div>
          </div>

          <!-- ---------------- SUB-TAB 4.3 ---------------- -->
          <div id="ch4-sec-ex4_3" class="hidden space-y-4">
            <div class="border-b border-slate-200 pb-2">
              <h3 class="text-lg font-black text-slate-900">अभ्यास ४.३: भिन्नहरूको जोड र घटाउ</h3>
              <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ ६५–६६ का सम्पूर्ण प्रश्नहरूको पूर्ण समाधान</p>
            </div>

            <!-- Q1: Computation grid -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न १</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">हिसाब गर्नुहोस् (जोड तथा घटाउ):</p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs font-mono">
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (क) $\frac{3}{4} + \frac{5}{6} = \frac{9+10}{12} = \mathbf{1\frac{7}{12}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ख) $\frac{2}{5} + \frac{1}{3} = \frac{6+5}{15} = \mathbf{\frac{11}{15}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ग) $4\frac{1}{7} + 2\frac{3}{4} = \frac{29}{7} + \frac{11}{4} = \frac{116+77}{28} = \mathbf{6\frac{25}{28}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (घ) $\frac{5}{9} + \frac{1}{3} = \frac{5+3}{9} = \mathbf{\frac{8}{9}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ङ) $1\frac{1}{10} + 9\frac{1}{5} = \frac{11+92}{10} = \mathbf{10\frac{3}{10}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (च) $\frac{11}{15} - \frac{3}{10} = \frac{22-9}{30} = \mathbf{\frac{13}{30}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (छ) $\frac{17}{2} - \frac{27}{4} = \frac{34-27}{4} = \mathbf{1\frac{3}{4}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ज) $3\frac{1}{5} - 2\frac{1}{10} = \frac{32-21}{10} = \mathbf{1\frac{1}{10}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (झ) $\frac{5}{6} - \frac{5}{12} = \frac{10-5}{12} = \mathbf{\frac{5}{12}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ञ) $8\frac{2}{9} - \frac{1}{4} = \frac{296-9}{36} = \mathbf{7\frac{35}{36}}$
                </div>
              </div>
            </div>

            <!-- Q2 to Q6: Word problems -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q2 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न २</span>
                <p class="font-bold text-slate-800">विनिताको स्याउ बाँकी भाग:</p>
                <p>$\frac{3}{4} - \frac{1}{5} = \frac{15 - 4}{20} = \mathbf{\frac{11}{20}}$ भाग स्याउ बाँकी।</p>
              </div>

              <!-- Q3 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ३</span>
                <p class="font-bold text-slate-800">स्थान A देखि C सम्मको जम्मा दूरी:</p>
                <p>$32\frac{1}{4} + 3\frac{1}{2} = \frac{129+14}{4} = \frac{143}{4} = \mathbf{35\frac{3}{4}\text{ m}}$।</p>
                <p class="text-[10px] text-slate-500">(यदि मुद्रणमा $8\frac{1}{4}$ भए मान $11\frac{3}{4}\text{ m}$ हुन्छ)</p>
              </div>

              <!-- Q4 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ४</span>
                <p class="font-bold text-slate-800">योगफलबाट दोस्रो भिन्न निकाल्ने:</p>
                <p>$6\frac{1}{6} - 2\frac{1}{3} = \frac{37 - 14}{6} = \frac{23}{6} = \mathbf{3\frac{5}{6}}$।</p>
              </div>

              <!-- Q5 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ५</span>
                <p class="font-bold text-slate-800">प्रसुन र प्राञ्जलले खाएको स्याउ:</p>
                <p>$\frac{3}{8} + \frac{1}{4} = \frac{3+2}{8} = \mathbf{\frac{5}{8}}$ भाग।</p>
              </div>

              <!-- Q6 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5 text-xs md:col-span-2">
                <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न ६</span>
                <p class="font-bold text-slate-800">आदित्यसँग बाँकी रहेको मिठाई:</p>
                <p>जम्मा मिठाई $= 5\frac{5}{6}\text{ kg}$। बाँडिएको $= 1\frac{2}{3} + 3\frac{1}{3} = 5\text{ kg}$।</p>
                <p class="font-bold text-emerald-800">बाँकी मिठाई $= 5\frac{5}{6} - 5 = \mathbf{\frac{5}{6}\text{ kg}}$।</p>
              </div>
            </div>
          </div>

          <!-- ---------------- SUB-TAB 4.4.1 ---------------- -->
          <div id="ch4-sec-ex4_4_1" class="hidden space-y-4">
            <div class="border-b border-slate-200 pb-2">
              <h3 class="text-lg font-black text-slate-900">अभ्यास ४.४.१: भिन्न र पूर्ण सङ्ख्याको गुणन</h3>
              <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ ६८–६९ का सम्पूर्ण प्रश्नहरूको पूर्ण समाधान</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न १ (टायल समस्या)</span>
                <p>$3 \times \frac{3}{10} = \mathbf{\frac{9}{10}}$ भाग छतमा बिछ्याउन पुग्छ।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न २ (पार्क ढुङ्गा)</span>
                <p>$6 \times \frac{2}{15} = \frac{12}{15} = \mathbf{\frac{4}{5}}$ भागमा पुग्छ।</p>
              </div>
            </div>

            <!-- Q3 & Q4 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <!-- Q3 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ३: गुणनफल</span>
                <div class="space-y-1 font-mono">
                  <p>• (क) $\frac{2}{3} \times 12 = \mathbf{8}$</p>
                  <p>• (ख) $\frac{3}{8} \times 15 = \mathbf{5\frac{5}{8}}$</p>
                  <p>• (ग) $\frac{1}{3} \times 25 = \mathbf{8\frac{1}{3}}$</p>
                  <p>• (घ) $\frac{1}{9} \times 27 = \mathbf{3}$</p>
                </div>
              </div>
              <!-- Q4 -->
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ४: मान निकाल्ने</span>
                <div class="space-y-1">
                  <p>• (क) २ केजीको $\frac{3}{4} = 2000 \times \frac{3}{4} = \mathbf{1500\text{ gm}}$</p>
                  <p>• (ख) १०० सेमीको $\frac{5}{4} = 100 \times \frac{5}{4} = \mathbf{125\text{ cm}}$</p>
                  <p>• (ग) १ वर्षको $\frac{2}{3} = 12 \times \frac{2}{3} = \mathbf{8\text{ महिना}}$</p>
                  <p>• (घ) २०० विद्यार्थीको $\frac{3}{4} = \mathbf{150\text{ विद्यार्थी}}$</p>
                </div>
              </div>
            </div>

            <!-- Q5 to Q8 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ५: हिसाब</span>
                <p>• (क) २५ को $\frac{1}{5} = \mathbf{5}$</p>
                <p>• (ख) १२० को $\frac{3}{4} = \mathbf{90}$</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ६: रामविलास सापटी</span>
                <p>• (क) सापटी $= 1000 \times \frac{3}{5} = \mathbf{\text{रु } 600}$</p>
                <p>• (ख) बाँकी $= 1000 - 600 = \mathbf{\text{रु } 400}$</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ७: चामल बोरा</span>
                <p>• निकालिएको $= 25 \times \frac{1}{5} = \mathbf{5\text{ kg}}$</p>
                <p>• बाँकी चामल $= 25 - 5 = \mathbf{20\text{ kg}}$</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ८: कालोपत्रे बाटो</span>
                <p>• कालोपत्रे $= 18 \times \frac{2}{3} = \mathbf{12\text{ km}}$</p>
                <p>• बाँकी बाटो $= 18 - 12 = \mathbf{6\text{ km}}$</p>
              </div>
            </div>
          </div>

          <!-- ---------------- SUB-TAB 4.4.2 ---------------- -->
          <div id="ch4-sec-ex4_4_2" class="hidden space-y-4">
            <div class="border-b border-slate-200 pb-2">
              <h3 class="text-lg font-black text-slate-900">अभ्यास ४.४.२: भिन्नलाई भिन्नले गुणन</h3>
              <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ ७०–७१ का सम्पूर्ण प्रश्नहरूको पूर्ण समाधान</p>
            </div>

            <!-- Q1: Multiplication -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न १</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">गुणनफल निकाल्नुहोस्:</p>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs font-mono">
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (क) $\frac{4}{5} \times \frac{3}{8} = \frac{12}{40} = \mathbf{\frac{3}{10}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ख) $\frac{1}{5} \times \frac{1}{3} = \mathbf{\frac{1}{15}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ग) $2\frac{1}{7} \times 2\frac{4}{9} = \frac{15}{7} \times \frac{22}{9} = \mathbf{5\frac{5}{21}}$
                </div>
              </div>
            </div>

            <!-- Q2 to Q5: Word problems -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न २ (भित्ता कागज)</span>
                <p>आधा प्याकेट कागजले টাँस्न सकिने क्षेत्रफल:</p>
                <p class="font-bold text-emerald-800">$\frac{3}{4} \times \frac{1}{2} = \mathbf{\frac{3}{8}\text{ m}^2}$</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ३ (खरबुजा तौल)</span>
                <p>$5\frac{1}{2}$ वटा खरबुजाको जम्मा तौल:</p>
                <p class="font-bold text-emerald-800">$6\frac{2}{3} \times 5\frac{1}{2} = \frac{20}{3} \times \frac{11}{2} = \mathbf{36\frac{2}{3}\text{ kg}}$</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ४ (पेट्रोल खपत)</span>
                <p>$5\frac{2}{5}$ घण्टामा आवश्यक पेट्रोल:</p>
                <p class="font-bold text-emerald-800">$2\frac{1}{5} \times 5\frac{2}{5} = \frac{11}{5} \times \frac{27}{5} = \mathbf{11\frac{22}{25}\text{ L}}$</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1.5">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ५ (दूध गिलास)</span>
                <p>• (i) पिएको दूध $= \frac{3}{4} \times \frac{2}{3} = \mathbf{\frac{1}{2}}$ गिलास</p>
                <p>• (ii) बाँकी दूध $= \frac{3}{4} - \frac{1}{2} = \mathbf{\frac{1}{4}}$ गिलास</p>
              </div>
            </div>
          </div>

          <!-- ---------------- SUB-TAB 4.5 ---------------- -->
          <div id="ch4-sec-ex4_5" class="hidden space-y-4">
            <div class="border-b border-slate-200 pb-2">
              <h3 class="text-lg font-black text-slate-900">अभ्यास ४.५: भिन्नको भाग तथा सरलीकरण</h3>
              <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ ७४–७५ का सम्पूर्ण प्रश्नहरूको पूर्ण समाधान</p>
            </div>

            <!-- Q1: Division by whole or fraction -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न १</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">भाग गर्नुहोस् (व्युत्क्रम नियम प्रयोग):</p>
              <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs font-mono">
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (क) $\frac{1}{3} \div 5 = \mathbf{\frac{1}{15}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ख) $\frac{1}{4} \div 3 = \mathbf{\frac{1}{12}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ग) $\frac{1}{2} \div 10 = \mathbf{\frac{1}{20}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (घ) $\frac{2}{5} \div 12 = \mathbf{\frac{1}{30}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ङ) $20 \div \frac{4}{7} = \mathbf{35}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (च) $4 \div \frac{1}{2} = \mathbf{8}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (छ) $8 \div \frac{2}{3} = \mathbf{12}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ज) $5 \div \frac{3}{5} = \mathbf{8\frac{1}{3}}$
                </div>
              </div>
            </div>

            <!-- Q2: Fraction division -->
            <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-2">
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">प्रश्न २</span>
              <p class="text-xs md:text-sm text-slate-800 font-bold">हिसाब गर्नुहोस् (भिन्नलाई भिन्नले भाग):</p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs font-mono">
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (क) $\frac{18}{13} \div \frac{9}{8} = \frac{18}{13} \times \frac{8}{9} = \mathbf{1\frac{3}{13}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ख) $\frac{32}{7} \div \frac{16}{7} = \frac{32}{7} \times \frac{7}{16} = \mathbf{2}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (ग) $3\frac{5}{7} \div 2\frac{5}{7} = \frac{26}{7} \times \frac{7}{19} = \mathbf{1\frac{7}{19}}$
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border">
                  (घ) $4\frac{4}{5} \div 2\frac{2}{15} = \frac{24}{5} \times \frac{15}{32} = \mathbf{2\frac{1}{4}}$
                </div>
              </div>
            </div>

            <!-- Q3 to Q9 Word problems -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ३: खेत खन्ने काम</span>
                <p>१ जनाले खनेको भाग $= \frac{3}{4} \div 15 = \mathbf{\frac{1}{20}}$ भाग।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ४: इँटा छाप्ने काम</span>
                <p>१ ट्रक इँटाले छाप्ने बाटो $= \frac{2}{7} \div \frac{1}{3} = \mathbf{\frac{6}{7}}$ भाग।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ५: डोरीका टुक्रा</span>
                <p>टुक्रा सङ्ख्या $= 25 \div \frac{5}{6} = 25 \times \frac{6}{5} = \mathbf{30}$ टुक्रा।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ६: झ्यालका पर्दा</span>
                <p>झ्याल सङ्ख्या $= 30 \div \frac{3}{4} = 30 \times \frac{4}{3} = \mathbf{40}$ वटा।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ७: दूधका सिसी</span>
                <p>सिसी सङ्ख्या $= 20 \div 1\frac{1}{4} = 20 \times \frac{4}{5} = \mathbf{16}$ वटा।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ८: तेलका भाँडा</span>
                <p>भाँडा सङ्ख्या $= 41\frac{1}{2} \div \frac{1}{2} = \frac{83}{2} \times 2 = \mathbf{83}$ वटा।</p>
              </div>
              <div class="border border-slate-200 rounded-2xl p-4 bg-white shadow-xs space-y-1 md:col-span-2">
                <span class="px-2 py-0.5 rounded font-bold bg-blue-100 text-blue-800">प्रश्न ९: बहु-चरणीय सरलीकरण</span>
                <p>$\left(3\frac{1}{2} - \frac{2}{5}\right) \div \frac{1}{2} \times 1\frac{1}{2} = \frac{31}{10} \times \frac{2}{1} \times \frac{3}{2} = \mathbf{9\frac{3}{10}}$ (वा $\frac{93}{10}$)।</p>
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH4 TAB 3: 3-TIER QUESTIONS ================= -->
        <div id="ch4-view-tiers" class="hidden space-y-6">
          <div class="border-b border-slate-200 pb-2">
            <h3 class="text-lg font-black text-slate-900">तीन तहका परीक्षा-केन्द्रित नमुना प्रश्नहरू</h3>
            <p class="text-xs text-slate-500">CDC विशिष्टीकरण तालिका अनुसार ज्ञान, सीप र उच्च दक्षता प्रश्नहरू</p>
          </div>

          <!-- Tier 1: 1 Mark -->
          <div class="border border-blue-200 bg-blue-50/30 rounded-2xl p-5 space-y-3">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full text-xs font-black bg-blue-600 text-white">तह १: आधारभूत बुझाइ (१ अङ्क)</span>
              <span class="text-xs text-blue-800 font-bold">Knowledge Level</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div class="bg-white p-3.5 rounded-xl border border-blue-100 space-y-1">
                <p class="font-bold text-slate-800">प्रश्न १: उचित र अनुचित भिन्नमा के फरक छ?</p>
                <p class="text-slate-600">उचित भिन्नमा अंश हरभन्दा सानो ($a < b$) हुन्छ, तर अनुचित भिन्नमा अंश हरसँग बराबर वा ठूलो ($a \ge b$) हुन्छ।</p>
              </div>
              <div class="bg-white p-3.5 rounded-xl border border-blue-100 space-y-1">
                <p class="font-bold text-slate-800">प्रश्न २: भिन्न $\frac{7}{9}$ को व्युत्क्रम भिन्न कति हुन्छ?</p>
                <p class="text-slate-600">अंश र हर उल्टाउँदा: $\mathbf{\frac{9}{7}}$ हुन्छ।</p>
              </div>
            </div>
          </div>

          <!-- Tier 2: 2 Marks -->
          <div class="border border-emerald-200 bg-emerald-50/30 rounded-2xl p-5 space-y-3">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full text-xs font-black bg-emerald-600 text-white">तह २: ज्ञानको प्रयोग तथा सीप (२ अङ्क)</span>
              <span class="text-xs text-emerald-800 font-bold">Application Level</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div class="bg-white p-3.5 rounded-xl border border-emerald-100 space-y-1">
                <p class="font-bold text-slate-800">प्रश्न १: भिन्नहरू $\frac{5}{6}$ र $\frac{7}{9}$ को तुलना गर्नुहोस्।</p>
                <p class="text-slate-600">ल.स. १८ बनाउँदा: $\frac{15}{18}$ र $\frac{14}{18}$। अतः $\mathbf{\frac{5}{6} > \frac{7}{9}}$।</p>
              </div>
              <div class="bg-white p-3.5 rounded-xl border border-emerald-100 space-y-1">
                <p class="font-bold text-slate-800">प्रश्न २: मान निकाल्नुहोस्: $\frac{16}{25} \div \frac{8}{15}$</p>
                <p class="text-slate-600">$\frac{16}{25} \times \frac{15}{8} = \frac{2 \times 3}{5 \times 1} = \mathbf{1\frac{1}{5}}$ (वा $\frac{6}{5}$)।</p>
              </div>
            </div>
          </div>

          <!-- Tier 3: 4 Marks -->
          <div class="border border-purple-200 bg-purple-50/30 rounded-2xl p-5 space-y-3">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full text-xs font-black bg-purple-600 text-white">तह ३: उच्च दक्षता तथा समस्या समाधान (४ अङ्क)</span>
              <span class="text-xs text-purple-800 font-bold">Higher Ability</span>
            </div>
            <div class="bg-white p-4 rounded-xl border border-purple-100 space-y-2 text-xs">
              <p class="font-bold text-slate-800">प्रश्न: एक कृषकसँग भएको जग्गामध्ये $\frac{1}{3}$ भागमा धान, $\frac{2}{5}$ भागमा मकै र बाँकी भागमा तरकारी खेती गरिएको छ। (क) धान र मकैले जम्मा कति भाग ओगटेको छ? (ख) तरकारी खेती गरिएको भाग कति होला? (ग) यदि जग्गा ३० रोपनी भए तरकारी खेती कति रोपनीमा गरिएको रहेछ?</p>
              <div class="p-3 bg-purple-50/50 rounded-lg space-y-1 text-slate-700">
                <p>• (क) धान + मकै $= \frac{1}{3} + \frac{2}{5} = \frac{5+6}{15} = \mathbf{\frac{11}{15}}$ भाग [१.५ अङ्क]</p>
                <p>• (ख) तरकारी खेती $= 1 - \frac{11}{15} = \mathbf{\frac{4}{15}}$ भाग [१.५ अङ्क]</p>
                <p>• (ग) क्षेत्रफल $= 30 \times \frac{4}{15} = \mathbf{8\text{ रोपनी}}$ [१ अङ्क]</p>
              </div>
            </div>
          </div>
        </div>

        <!-- ================= CH4 TAB 4: QUIZ ================= -->
        <div id="ch4-view-quiz" class="hidden space-y-6">
          <div class="border-b border-slate-200 pb-2">
            <h3 class="text-lg font-black text-slate-900">पाठ ४: आत्म-मूल्याङ्कन क्विज</h3>
            <p class="text-xs text-slate-500">उत्तर छान्नुहोस् र आफ्नो बुझाइ तत्काल प्रमाणीकरण गर्नुहोस्</p>
          </div>

          <!-- Interactive Questions -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            
            <!-- Q1 -->
            <div id="ch4-qbox-0" class="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3 text-xs">
              <div class="flex justify-between items-center">
                <span class="font-black text-blue-700">प्रश्न १</span>
                <span id="ch4-qbadge-0" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-600">उत्तर दिनुहोस्</span>
              </div>
              <p class="font-bold text-slate-800 text-sm">तलका मध्ये कुन उचित भिन्न (Proper Fraction) हो?</p>
              <div class="space-y-1.5">
                <button id="ch4-qbtn-0-0" onclick="checkQuizCh4(0, 0)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">A) $\frac{5}{3}$</button>
                <button id="ch4-qbtn-0-1" onclick="checkQuizCh4(0, 1)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">B) $\frac{7}{4}$</button>
                <button id="ch4-qbtn-0-2" onclick="checkQuizCh4(0, 2)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">C) $\frac{4}{7}$</button>
                <button id="ch4-qbtn-0-3" onclick="checkQuizCh4(0, 3)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">D) $1\frac{1}{2}$</button>
              </div>
              <div id="ch4-qexp-0" class="hidden p-3 rounded-xl bg-slate-50 border text-slate-700"></div>
            </div>

            <!-- Q2 -->
            <div id="ch4-qbox-1" class="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3 text-xs">
              <div class="flex justify-between items-center">
                <span class="font-black text-blue-700">प्रश्न २</span>
                <span id="ch4-qbadge-1" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-600">उत्तर दिनुहोस्</span>
              </div>
              <p class="font-bold text-slate-800 text-sm">$\frac{1}{3} + \frac{1}{6}$ को मान कति हुन्छ?</p>
              <div class="space-y-1.5">
                <button id="ch4-qbtn-1-0" onclick="checkQuizCh4(1, 0)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">A) $\frac{2}{9}$</button>
                <button id="ch4-qbtn-1-1" onclick="checkQuizCh4(1, 1)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">B) $\frac{1}{2}$</button>
                <button id="ch4-qbtn-1-2" onclick="checkQuizCh4(1, 2)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">C) $\frac{2}{6}$</button>
                <button id="ch4-qbtn-1-3" onclick="checkQuizCh4(1, 3)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">D) $\frac{1}{9}$</button>
              </div>
              <div id="ch4-qexp-1" class="hidden p-3 rounded-xl bg-slate-50 border text-slate-700"></div>
            </div>

            <!-- Q3 -->
            <div id="ch4-qbox-2" class="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3 text-xs">
              <div class="flex justify-between items-center">
                <span class="font-black text-blue-700">प्रश्न ३</span>
                <span id="ch4-qbadge-2" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-600">उत्तर दिनुहोस्</span>
              </div>
              <p class="font-bold text-slate-800 text-sm">$\frac{3}{5} \times \frac{10}{9}$ को सरल मान कति हुन्छ?</p>
              <div class="space-y-1.5">
                <button id="ch4-qbtn-2-0" onclick="checkQuizCh4(2, 0)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">A) $\frac{2}{3}$</button>
                <button id="ch4-qbtn-2-1" onclick="checkQuizCh4(2, 1)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">B) $\frac{3}{2}$</button>
                <button id="ch4-qbtn-2-2" onclick="checkQuizCh4(2, 2)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">C) $\frac{30}{45}$</button>
                <button id="ch4-qbtn-2-3" onclick="checkQuizCh4(2, 3)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">D) $\frac{13}{14}$</button>
              </div>
              <div id="ch4-qexp-2" class="hidden p-3 rounded-xl bg-slate-50 border text-slate-700"></div>
            </div>

            <!-- Q4 -->
            <div id="ch4-qbox-3" class="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3 text-xs">
              <div class="flex justify-between items-center">
                <span class="font-black text-blue-700">प्रश्न ४</span>
                <span id="ch4-qbadge-3" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-600">उत्तर दिनुहोस्</span>
              </div>
              <p class="font-bold text-slate-800 text-sm">$\frac{4}{7} \div \frac{2}{7}$ को मान कति हुन्छ?</p>
              <div class="space-y-1.5">
                <button id="ch4-qbtn-3-0" onclick="checkQuizCh4(3, 0)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">A) $\frac{8}{49}$</button>
                <button id="ch4-qbtn-3-1" onclick="checkQuizCh4(3, 1)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">B) $2$</button>
                <button id="ch4-qbtn-3-2" onclick="checkQuizCh4(3, 2)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">C) $\frac{1}{2}$</button>
                <button id="ch4-qbtn-3-3" onclick="checkQuizCh4(3, 3)" class="w-full text-left p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">D) $1$</button>
              </div>
              <div id="ch4-qexp-3" class="hidden p-3 rounded-xl bg-slate-50 border text-slate-700"></div>
            </div>

          </div>
        </div>

      </div>
      <!-- ================= END OF CHAPTER 4 VIEW ================= -->
'''
