# -*- coding: utf-8 -*-
"""
Generates the HTML content for Chapter 5 (दशमलव - Decimals) of Class 6 Mathematics.
Matches the design, CSS, and MathJax conventions of Chapters 1 to 4.
"""

def get_ch5_html():
    return """
      <!-- ================= CHAPTER 5: DECIMALS (दशमलव) ================= -->
      <div id="chapter-view-5" class="hidden flex-1 flex flex-col">
        <!-- Top Chapter Banner -->
        <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-blue-600 mb-1">एकाइ २: अङ्कगणित (Unit 2: Arithmetic)</div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ ५: दशमलव (Decimals)</h2>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ ७६–८५</span>
            <span class="text-xs bg-blue-100 text-blue-800 font-bold px-3 py-1 rounded-xl border border-blue-200">अभ्यास ५.१ देखि ५.३ सम्म</span>
          </div>
        </div>

        <!-- Chapter 5 Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button id="ch5-tab-concepts" onclick="setTabCh5('concepts')" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap">
            १. अवधारणा र नियमहरू
          </button>
          <button id="ch5-tab-exercises" onclick="setTabCh5('exercises')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            २. सम्पूर्ण अभ्यासहरू (५.१ – ५.३)
          </button>
          <button id="ch5-tab-tiers" onclick="setTabCh5('tiers')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ३. तीन तहका नमुना प्रश्नहरू
          </button>
          <button id="ch5-tab-quiz" onclick="setTabCh5('quiz')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ४. आत्म-मूल्याङ्कन क्विज
          </button>
        </div>

        <!-- ================= CH5 TAB 1: CONCEPTS ================= -->
        <div id="ch5-view-concepts" class="space-y-6">
          
          <!-- Concept 1: Definition & Place Value -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-base">🔍</span>
              दशमलवको परिचय र स्थानीय मान तालिका (Place Value of Decimals)
            </h3>
            <p class="text-xs md:text-sm text-slate-600 mb-4">
              दैनिक जीवनमा कुनै सिङ्गो वस्तुलाई १०, १००, १००० वा १० का कुनै पनि घातका बराबर भागहरूमा बाँड्दा आउने परिमाणलाई <strong>दशमलव सङ्ख्या (Decimal Number)</strong> भनिन्छ। पूर्ण सङ्ख्या र दशमलव भागलाई छुट्याउन बीचमा प्रयोग गरिने थोप्लो ($.$) लाई <strong>दशमलव बिन्दु (Decimal Point)</strong> भनिन्छ।
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
              <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl">
                <span class="text-xs font-bold text-blue-600 uppercase tracking-wider block mb-1">दशमलवको संरचना</span>
                <div class="text-sm font-semibold text-slate-800">
                  $$\\text{दशमलव सङ्ख्या} = \\text{पूर्ण भाग} \\;.\\; \\text{दशमलव भाग}$$
                </div>
                <p class="text-xs text-slate-600 mt-2">
                  उदाहरण: $२५.३४७$ मा $२५$ पूर्ण भाग हो भने $३४७$ दशमलव भाग हो (पढ्दा: पच्चीस दशमलव तीन चार सात)।
                </p>
              </div>

              <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl">
                <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider block mb-1">दशमलव बिन्दु दायाँका स्थानहरू</span>
                <ul class="text-xs text-slate-700 space-y-1 mt-1">
                  <li>• <strong>दशांश (Tenths):</strong> पहिलो स्थान $\\implies \\frac{1}{10} = 0.1$</li>
                  <li>• <strong>शतांश (Hundredths):</strong> दोस्रो स्थान $\\implies \\frac{1}{100} = 0.01$</li>
                  <li>• <strong>सहस्रांश (Thousandths):</strong> तेस्रो स्थान $\\implies \\frac{1}{1000} = 0.001$</li>
                </ul>
              </div>
            </div>

            <!-- Table of Place Values -->
            <div class="overflow-x-auto rounded-xl border border-slate-200">
              <table class="w-full text-xs md:text-sm text-center">
                <thead class="bg-slate-100 font-bold text-slate-700">
                  <tr>
                    <th class="p-2.5 border-b">सङ्ख्या</th>
                    <th class="p-2.5 border-b">सय ($100$)</th>
                    <th class="p-2.5 border-b">दस ($10$)</th>
                    <th class="p-2.5 border-b">एक ($1$)</th>
                    <th class="p-2.5 border-b text-blue-600">दशमलव ($.$)</th>
                    <th class="p-2.5 border-b">दशांश ($\\frac{1}{10}$)</th>
                    <th class="p-2.5 border-b">शतांश ($\\frac{1}{100}$)</th>
                    <th class="p-2.5 border-b">सहस्रांश ($\\frac{1}{1000}$)</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 text-slate-800">
                  <tr>
                    <td class="p-2 font-bold bg-slate-50">$२.५१$</td>
                    <td class="p-2 text-slate-400">-</td>
                    <td class="p-2 text-slate-400">-</td>
                    <td class="p-2">२</td>
                    <td class="p-2 font-bold text-blue-600">.</td>
                    <td class="p-2">५</td>
                    <td class="p-2">१</td>
                    <td class="p-2 text-slate-400">-</td>
                  </tr>
                  <tr>
                    <td class="p-2 font-bold bg-slate-50">$३७.०४८$</td>
                    <td class="p-2 text-slate-400">-</td>
                    <td class="p-2">३</td>
                    <td class="p-2">७</td>
                    <td class="p-2 font-bold text-blue-600">.</td>
                    <td class="p-2">०</td>
                    <td class="p-2">४</td>
                    <td class="p-2">८</td>
                  </tr>
                  <tr>
                    <td class="p-2 font-bold bg-slate-50">$१४९.०४$</td>
                    <td class="p-2">१</td>
                    <td class="p-2">४</td>
                    <td class="p-2">९</td>
                    <td class="p-2 font-bold text-blue-600">.</td>
                    <td class="p-2">०</td>
                    <td class="p-2">४</td>
                    <td class="p-2 text-slate-400">-</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Concept 2: Multiplication Rules -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-base">✖️</span>
              दशमलव सङ्ख्याको गुणनका नियमहरू (Multiplication Rules)
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-sm mb-2 text-indigo-700">१. १०, १००, १००० ले गुणन गर्दा:</h4>
                <p class="text-xs text-slate-600 mb-3">
                  दशमलव बिन्दु शून्यको सङ्ख्या बराबर <strong>दायाँतर्फ (Right)</strong> सर्दछ:
                </p>
                <ul class="text-xs space-y-1.5 font-medium text-slate-700">
                  <li>• $10 \\times 0.6284 = 6.284$ <span class="text-slate-400">(१ स्थान दायाँ)</span></li>
                  <li>• $100 \\times 0.6284 = 62.84$ <span class="text-slate-400">(२ स्थान दायाँ)</span></li>
                  <li>• $1000 \\times 0.6284 = 628.4$ <span class="text-slate-400">(३ स्थान दायाँ)</span></li>
                </ul>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-sm mb-2 text-indigo-700">२. दुई दशमलवहरूको गुणन:</h4>
                <p class="text-xs text-slate-600 mb-2">
                  दशमलव बिन्दुलाई बेवास्ता गरी सामान्य गुणन गर्ने, त्यसपछि दुवैका दशमलव अङ्क जोडी दायाँबाट बिन्दु राख्ने:
                </p>
                <div class="p-3 bg-white border border-slate-200 rounded-lg text-xs">
                  <div class="font-bold text-slate-800 mb-1">उदा: $३७.७ \\times २.८$</div>
                  <div>$377 \\times 28 = 10556$</div>
                  <div>कुल दशमलव अङ्क $= 1 + 1 = 2$</div>
                  <div class="font-bold text-indigo-600 mt-1">अन्तिम गुणनफल $= 105.56$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Concept 3: Division Rules -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-teal-100 text-teal-700 flex items-center justify-center text-base">➗</span>
              दशमलव सङ्ख्याको भागका नियमहरू (Division Rules)
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-sm mb-1 text-teal-700">१०, १०० ले भाग</h4>
                <p class="text-xs text-slate-600 mb-2">दशमलव बिन्दु <strong>बायाँतर्फ (Left)</strong> सर्दछ:</p>
                <ul class="text-xs text-slate-700 space-y-1">
                  <li>• $232.59 \\div 10 = 23.259$</li>
                  <li>• $232.59 \\div 100 = 2.3259$</li>
                  <li>• $232.59 \\div 1000 = 0.23259$</li>
                </ul>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-sm mb-1 text-teal-700">पूर्ण सङ्ख्याले भाग</h4>
                <p class="text-xs text-slate-600 mb-2">दशमलवपछिको अङ्क तल झार्ने बित्तिकै भागफलमा बिन्दु राख्ने:</p>
                <div class="text-xs font-mono bg-white p-2 border rounded">
                  $149.04 \\div 12 = 12.42$
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-sm mb-1 text-teal-700">दशमलवलाई दशमलवले भाग</h4>
                <p class="text-xs text-slate-600 mb-2">भाजकलाई पूर्ण सङ्ख्या बनाउन अंश र हरलाई १०, १०० ले गुणन गर्ने:</p>
                <div class="text-xs font-mono bg-white p-2 border rounded">
                  $\\frac{171}{2.85} = \\frac{17100}{285} = 60$
                </div>
              </div>
            </div>
          </div>

          <!-- Concept 4: Rounding off Rules -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-base">🎯</span>
              दशमलवको शून्यान्त / निकटीकरण (Rounding off Decimals)
            </h3>
            <p class="text-xs md:text-sm text-slate-600 mb-4">
              तोकिएको स्थानपछिको ठीक दायाँतर्फको अङ्क हेरेर निर्णय गरिन्छ:
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl">
                <h4 class="font-bold text-rose-800 text-sm mb-1">अङ्क ५ भन्दा सानो भए ($< 5$, अर्थात् $0, 1, 2, 3, 4$)</h4>
                <p class="text-xs text-slate-700 mb-2">तोकिएको स्थानको अङ्कमा कुनै थपथाप नगर्ने, पछिका अङ्क हटाउने।</p>
                <div class="text-xs font-bold text-rose-900 bg-white p-2 border rounded">
                  $३.५७३$ लाई दोस्रो स्थानमा $\\implies ३.५७$ ($३ < 5$)
                </div>
              </div>

              <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl">
                <h4 class="font-bold text-emerald-800 text-sm mb-1">अङ्क ५ वा सोभन्दा ठूलो भए ($\\ge 5$, अर्थात् $5, 6, 7, 8, 9$)</h4>
                <p class="text-xs text-slate-700 mb-2">तोकिएको स्थानको अङ्कमा <strong>१ थप्ने</strong>, पछिका अङ्क हटाउने।</p>
                <div class="text-xs font-bold text-emerald-900 bg-white p-2 border rounded">
                  $९२.६३७$ लाई दोस्रो स्थानमा $\\implies ९२.६४$ ($७ \\ge 5$)
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH5 TAB 2: EXERCISES ================= -->
        <div id="ch5-view-exercises" class="hidden space-y-6">
          
          <!-- Exercise Navigation Pills -->
          <div class="flex gap-2 overflow-x-auto pb-2 border-b border-slate-200 text-xs md:text-sm font-bold">
            <button id="ch5-pill-ex5_1" onclick="setExerciseCh5('ex5_1')" class="px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap">
              अभ्यास ५.१ (गुणन र रूपान्तरण)
            </button>
            <button id="ch5-pill-ex5_2" onclick="setExerciseCh5('ex5_2')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              अभ्यास ५.२ (दशमलवको भाग र समस्याहरू)
            </button>
            <button id="ch5-pill-ex5_3" onclick="setExerciseCh5('ex5_3')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              अभ्यास ५.३ (दशमलवको शून्यान्त)
            </button>
          </div>

          <!-- ---------------- SECTION: EXERCISE 5.1 ---------------- -->
          <div id="ch5-sec-ex5_1" class="space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">अभ्यास ५.१: दशमलव भिन्न रूपान्तरण, गुणन र समस्याहरू</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ ७९–८० (प्रश्न १, २ र ३ का सम्पूर्ण उपप्रश्नहरूको शतप्रतिशत समाधान)</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">कुल २३ प्रश्नहरू</span>
            </div>

            <!-- Q1: Conversion -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
              <h3 class="font-black text-slate-800 text-base mb-3 flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold">१</span>
                तलका दशमलव भिन्नहरूलाई दशमलव सङ्ख्यामा रूपान्तरण गर्नुहोस्:
              </h3>
              
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-xs text-slate-500 mb-1">(क) $\\frac{3}{10}$</div>
                  <div class="text-xs text-slate-700 mb-1">हरमा १० भएकाले १ स्थान बायाँ बिन्दु:</div>
                  <div class="font-bold text-sm text-blue-600">$= 0.3$ <span class="text-xs font-normal text-slate-500">(शून्य दशमलव तीन)</span></div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-xs text-slate-500 mb-1">(ख) $\\frac{34}{100}$</div>
                  <div class="text-xs text-slate-700 mb-1">हरमा १०० भएकाले २ स्थान बायाँ बिन्दु:</div>
                  <div class="font-bold text-sm text-blue-600">$= 0.34$ <span class="text-xs font-normal text-slate-500">(शून्य दशमलव तीन चार)</span></div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-xs text-slate-500 mb-1">(ग) $\\frac{713}{1000}$</div>
                  <div class="text-xs text-slate-700 mb-1">हरमा १००० भएकाले ३ स्थान बायाँ बिन्दु:</div>
                  <div class="font-bold text-sm text-blue-600">$= 0.713$ <span class="text-xs font-normal text-slate-500">(शून्य दशमलव सात एक तीन)</span></div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-xs text-slate-500 mb-1">(घ) $\\frac{191}{100}$</div>
                  <div class="text-xs text-slate-700 mb-1">हरमा १०० भएकाले २ स्थान बायाँ बिन्दु:</div>
                  <div class="font-bold text-sm text-blue-600">$= 1.91$ <span class="text-xs font-normal text-slate-500">(एक दशमलव नौ एक)</span></div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-xs text-slate-500 mb-1">(ङ) $\\frac{3471}{100}$</div>
                  <div class="text-xs text-slate-700 mb-1">हरमा १०० भएकाले २ स्थान बायाँ बिन्दु:</div>
                  <div class="font-bold text-sm text-blue-600">$= 34.71$ <span class="text-xs font-normal text-slate-500">(चौँतीस दशमलव सात एक)</span></div>
                </div>
              </div>
            </div>

            <!-- Q2: Multiplication -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
              <h3 class="font-black text-slate-800 text-base mb-3 flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold">२</span>
                गुणन गर्नुहोस् (१४ उपप्रश्नहरू):
              </h3>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(क) $2 \\times 2.51$</div>
                  <div class="text-slate-600">$251 \\times 2 = 502$, २ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $5.02$</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ख) $5 \\times 1.25$</div>
                  <div class="text-slate-600">$125 \\times 5 = 625$, २ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $6.25$</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ग) $4 \\times 12.67$</div>
                  <div class="text-slate-600">$1267 \\times 4 = 5068$, २ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $50.68$</span> <span class="text-slate-400">(किताबमा ५०.२८ मुद्रण दोष)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(घ) $7 \\times 0.923$</div>
                  <div class="text-slate-600">$923 \\times 7 = 6461$, ३ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $6.461$ (वा $6.46$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ङ) $9 \\times 9.9$</div>
                  <div class="text-slate-600">$99 \\times 9 = 891$, १ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $89.1$ (वा $89.10$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(च) $10 \\times 8.297$</div>
                  <div class="text-slate-600">१० ले गुणन गर्दा १ स्थान दायाँ $\\implies$ <span class="font-bold text-blue-600">उत्तर: $82.97$</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(छ) $100 \\times 0.657$</div>
                  <div class="text-slate-600">१०० ले गुणन गर्दा २ स्थान दायाँ $\\implies$ <span class="font-bold text-blue-600">उत्तर: $65.7$ (वा $65.70$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ज) $21 \\times 0.21$</div>
                  <div class="text-slate-600">$21 \\times 21 = 441$, २ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $4.41$</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(झ) $101.03 \\times 2.35$</div>
                  <div class="text-slate-600">$10103 \\times 235 = 2374205$, ४ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $237.4205$ (वा $237.42$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ञ) $232.01 \\times 4.2$</div>
                  <div class="text-slate-600">$23201 \\times 42 = 974442$, ३ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $974.442$ (वा $974.44$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ट) $183.31 \\times 3.1$</div>
                  <div class="text-slate-600">$18331 \\times 31 = 568261$, ३ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $568.261$ (वा $568.26$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ठ) $530.12 \\times 1.52$</div>
                  <div class="text-slate-600">$53012 \\times 152 = 8057824$, ४ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $805.7824$ (वा $805.78$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ड) $986.41 \\times 1.02$</div>
                  <div class="text-slate-600">$98641 \\times 102 = 10061382$, ४ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $1006.1382$ (वा $1006.14$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ढ) $555.76 \\times 5.05$</div>
                  <div class="text-slate-600">$55576 \\times 505 = 28065880$, ४ अङ्क अघि दशमलव $\\implies$ <span class="font-bold text-blue-600">उत्तर: $2806.588$ (वा $2806.59$)</span></div>
                </div>
              </div>
            </div>

            <!-- Q3: Word Problems -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <h3 class="font-black text-slate-800 text-base flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold">३</span>
                व्यावहारिक समस्या समाधान (Word Problems):
              </h3>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (क) एन्जिलाका ३.७५ इन्चका तीनओटा राता रङ्गका रङ्गीन सिसाकलम छन् भने जम्मा लम्बाइ कति होला?
                </h4>
                <div class="text-xs text-slate-700">
                  १ सिसाकलमको लम्बाइ $= 3.75\\text{ in}$, जम्मा $= 3 \\times 3.75 = 11.25\\text{ in}$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: जम्मा लम्बाइ ११.२५ इन्च ($11.25\\text{ in}$) होला।
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (ख) एउटा वर्गाकार खेतको लम्बाइ ८.४५ मिटर छ भने उक्त खेतको परिमिति पत्ता लगाउनुहोस्।
                </h4>
                <div class="text-xs text-slate-700">
                  वर्गाकार खेतको परिमिति $P = 4 \\times l = 4 \\times 8.45 = 33.8\\text{ m}$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: खेतको परिमिति ३३.८ मिटर ($33.8\\text{ m}$) हुन्छ। <span class="font-normal text-slate-500">(किताबमा ३१.८ मुद्रण दोष)</span>
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (ग) लम्बाइ ७.२५ मिटर र चौडाइ ५.१३ मिटर भएको आयताकार बगैँचाको परिमिति कति होला?
                </h4>
                <div class="text-xs text-slate-700">
                  आयतको परिमिति $P = 2(l + b) = 2(7.25 + 5.13) = 2 \\times 12.38 = 24.76\\text{ m}$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: बगैँचाको परिमिति २४.७६ मिटर ($24.76\\text{ m}$) हुन्छ।
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (घ) एउटा रुलरको मूल्य रु २५.५० पर्दछ भने १० ओटा रुलरको जम्मा मूल्य कति पर्ला?
                </h4>
                <div class="text-xs text-slate-700">
                  १० वटा रुलरको मूल्य $= 10 \\times 25.50 = \\text{रु } 255.00$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: १० ओटा रुलरको जम्मा मूल्य रु २५५ पर्ला।
                </div>
              </div>
            </div>

          </div>

          <!-- ---------------- SECTION: EXERCISE 5.2 ---------------- -->
          <div id="ch5-sec-ex5_2" class="hidden space-y-6">
            <div class="bg-teal-50 border border-teal-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-teal-900 text-sm md:text-base">अभ्यास ५.२: दशमलव सङ्ख्याको भाग र व्यावहारिक समस्याहरू</h4>
                <p class="text-xs text-teal-700">पाठ्यपुस्तक पृष्ठ ८२–८३ (प्रश्न १ र २ का सम्पूर्ण उपप्रश्नहरूको शतप्रतिशत समाधान)</p>
              </div>
              <span class="text-xs font-bold bg-white text-teal-800 px-3 py-1 rounded-xl shadow-xs border border-teal-200">कुल १० प्रश्नहरू</span>
            </div>

            <!-- Q1: Divisions -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
              <h3 class="font-black text-slate-800 text-base mb-3 flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-700 flex items-center justify-center text-xs font-bold">१</span>
                भाग गर्नुहोस् (६ उपप्रश्नहरू):
              </h3>

              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(क) $183.31 \\div 10$</div>
                  <div class="text-slate-600">१० ले भाग गर्दा १ स्थान बायाँ $\\implies$ <span class="font-bold text-teal-700">उत्तर: $18.331$ (वा $18.33$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ख) $288.012 \\div 12$</div>
                  <div class="text-slate-600">भाग गर्दा $24.001 \\implies$ <span class="font-bold text-teal-700">उत्तर: लगभग $24$</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ग) $121.77 \\div 11$</div>
                  <div class="text-slate-600">भाग गर्दा $11.07 \\implies$ <span class="font-bold text-teal-700">उत्तर: $11.07$</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(घ) $530.1 \\div 100$</div>
                  <div class="text-slate-600">१०० ले भाग गर्दा २ स्थान बायाँ $\\implies$ <span class="font-bold text-teal-700">उत्तर: $5.301$ (वा $5.30$)</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(ङ) $966.45 \\div 15$</div>
                  <div class="text-slate-600">भाग गर्दा $64.43 \\implies$ <span class="font-bold text-teal-700">उत्तर: $64.43$</span></div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                  <div class="font-bold text-slate-800">(च) $557.825 \\div 25$</div>
                  <div class="text-slate-600">भाग गर्दा $22.313 \\implies$ <span class="font-bold text-teal-700">उत्तर: $22.313$ (वा $22.31$)</span></div>
                </div>
              </div>
            </div>

            <!-- Q2: Word Problems -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <h3 class="font-black text-slate-800 text-base flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-700 flex items-center justify-center text-xs font-bold">२</span>
                व्यावहारिक समस्या समाधान (Word Problems):
              </h3>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (क) १० मिनेटमा ७.५ किमी मोटरसाइकल यात्रा गर्ने मानिसले १ मिनेटमा कति यात्रा गर्ला?
                </h4>
                <div class="text-xs text-slate-700">
                  १ मिनेटमा पार गर्ने दूरी $= 7.5 \\div 10 = 0.75\\text{ km}$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: १ मिनेटमा ०.७५ किमी ($0.75\\text{ km}$ वा ७५० मिटर) यात्रा गर्ला।
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (ख) एउटा वर्गाकार खेतको परिमिति ४८.६४ मिटर छ भने त्यस खेतको लम्बाइ पत्ता लगाउनुहोस्।
                </h4>
                <div class="text-xs text-slate-700">
                  खेतको लम्बाइ $l = \\frac{P}{4} = \\frac{48.64}{4} = 12.16\\text{ m}$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: खेतको लम्बाइ १२.१६ मिटर ($12.16\\text{ m}$) हुन्छ।
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (ग) एउटा आयताकार खेतको क्षेत्रफल २४८.६४ वर्ग मिटर र लम्बाइ १६ मिटर भए चौडाइ कति होला?
                </h4>
                <div class="text-xs text-slate-700">
                  खेतको चौडाइ $b = \\frac{A}{l} = \\frac{248.64}{16} = 15.54\\text{ m}$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: खेतको चौडाइ १५.५४ मिटर ($15.54\\text{ m}$) हुन्छ।
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  (घ) २.८५ केजी तौल भएको काउलीको मूल्य रु १७१ भए १ केजी काउलीको मूल्य कति पर्ला?
                </h4>
                <div class="text-xs text-slate-700">
                  १ केजीको मूल्य $= \\frac{171}{2.85} = \\frac{171 \\times 100}{2.85 \\times 100} = \\frac{17100}{285} = \\text{रु } 60$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: १ केजी काउलीको मूल्य रु ६० पर्ला।
                </div>
              </div>
            </div>

          </div>

          <!-- ---------------- SECTION: EXERCISE 5.3 ---------------- -->
          <div id="ch5-sec-ex5_3" class="hidden space-y-6">
            <div class="bg-amber-50 border border-amber-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-amber-900 text-sm md:text-base">अभ्यास ५.३: दशमलवको शून्यान्त (Rounding Off Decimals)</h4>
                <p class="text-xs text-amber-700">पाठ्यपुस्तक पृष्ठ ८४–८५ (८ वटा सङ्ख्याहरूको तालिका, ३ व्यावहारिक समस्याहरू र प्रयोगात्मक कार्य)</p>
              </div>
              <span class="text-xs font-bold bg-white text-amber-800 px-3 py-1 rounded-xl shadow-xs border border-amber-200">१००% समाधान</span>
            </div>

            <!-- Q1: Rounding table -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
              <h3 class="font-black text-slate-800 text-base mb-3 flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-xs font-bold">१</span>
                तलका सङ्ख्याहरूलाई दशमलवको तेस्रो, दोस्रो र पहिलो स्थानमा शून्यान्त गर्नुहोस्:
              </h3>

              <div class="overflow-x-auto rounded-xl border border-slate-200">
                <table class="w-full text-xs md:text-sm text-left">
                  <thead class="bg-slate-100 text-slate-700 font-bold">
                    <tr>
                      <th class="p-2.5 border-b">क्र.सं.</th>
                      <th class="p-2.5 border-b">दिइएको सङ्ख्या</th>
                      <th class="p-2.5 border-b text-blue-700">तेस्रो स्थानमा शून्यान्त</th>
                      <th class="p-2.5 border-b text-emerald-700">दोस्रो स्थानमा शून्यान्त</th>
                      <th class="p-2.5 border-b text-purple-700">पहिलो स्थानमा शून्यान्त</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 text-slate-800">
                    <tr>
                      <td class="p-2 font-bold">(i)</td>
                      <td class="p-2 font-mono font-bold">$५.६३४२$</td>
                      <td class="p-2">$५.६३४$ <span class="text-[10px] text-slate-400">($२ < 5$)</span></td>
                      <td class="p-2 font-semibold text-emerald-600">$५.६३$ <span class="text-[10px] text-slate-400">($४ < 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$५.६$ <span class="text-[10px] text-slate-400">($३ < 5$)</span></td>
                    </tr>
                    <tr>
                      <td class="p-2 font-bold">(ii)</td>
                      <td class="p-2 font-mono font-bold">$२३.४७२$</td>
                      <td class="p-2">$२३.४७२$</td>
                      <td class="p-2 font-semibold text-emerald-600">$२३.४७$ <span class="text-[10px] text-slate-400">($२ < 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$२३.५$ <span class="text-[10px] text-slate-400">($७ \\ge 5$)</span></td>
                    </tr>
                    <tr>
                      <td class="p-2 font-bold">(iii)</td>
                      <td class="p-2 font-mono font-bold">$४५.७३६$</td>
                      <td class="p-2">$४५.७३६$</td>
                      <td class="p-2 font-semibold text-emerald-600">$४५.७४$ <span class="text-[10px] text-slate-400">($६ \\ge 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$४५.७$ <span class="text-[10px] text-slate-400">($३ < 5$)</span></td>
                    </tr>
                    <tr>
                      <td class="p-2 font-bold">(iv)</td>
                      <td class="p-2 font-mono font-bold">$७८.८६२$</td>
                      <td class="p-2">$७८.८६२$</td>
                      <td class="p-2 font-semibold text-emerald-600">$७८.८६$ <span class="text-[10px] text-slate-400">($२ < 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$७८.९$ <span class="text-[10px] text-slate-400">($६ \\ge 5$)</span></td>
                    </tr>
                    <tr>
                      <td class="p-2 font-bold">(v)</td>
                      <td class="p-2 font-mono font-bold">$०.९१७$</td>
                      <td class="p-2">$०.९१७$</td>
                      <td class="p-2 font-semibold text-emerald-600">$०.९२$ <span class="text-[10px] text-slate-400">($७ \\ge 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$०.९$ <span class="text-[10px] text-slate-400">($१ < 5$)</span></td>
                    </tr>
                    <tr>
                      <td class="p-2 font-bold">(vi)</td>
                      <td class="p-2 font-mono font-bold">$३६.७२७$</td>
                      <td class="p-2">$३६.७२७$</td>
                      <td class="p-2 font-semibold text-emerald-600">$३६.७३$ <span class="text-[10px] text-slate-400">($७ \\ge 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$३६.७$ <span class="text-[10px] text-slate-400">($२ < 5$)</span></td>
                    </tr>
                    <tr>
                      <td class="p-2 font-bold">(vii)</td>
                      <td class="p-2 font-mono font-bold">$१०४.९८३$</td>
                      <td class="p-2">$१०४.९८३$</td>
                      <td class="p-2 font-semibold text-emerald-600">$१०४.९८$ <span class="text-[10px] text-slate-400">($३ < 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$१०५.०$ <span class="text-[10px] text-slate-400">($८ \\ge 5$, ९ मा १ थपिँदा १०)</span></td>
                    </tr>
                    <tr>
                      <td class="p-2 font-bold">(viii)</td>
                      <td class="p-2 font-mono font-bold">$०.८६२४$</td>
                      <td class="p-2">$०.८६२$ <span class="text-[10px] text-slate-400">($४ < 5$)</span></td>
                      <td class="p-2 font-semibold text-emerald-600">$०.८६$ <span class="text-[10px] text-slate-400">($२ < 5$)</span></td>
                      <td class="p-2 font-semibold text-purple-600">$०.९$ <span class="text-[10px] text-slate-400">($६ \\ge 5$)</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Q2 & Q3: Problems and Activity -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <h3 class="font-black text-slate-800 text-base flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-xs font-bold">२ र ३</span>
                व्यावहारिक समस्याहरू र प्रयोगात्मक कार्य:
              </h3>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  २ (क) डिजिटल तराजुमा मूल्य रु ३४६.७२ देखाउँदा कति रुपियाँ तिर्नुपर्ला?
                </h4>
                <div class="text-xs text-slate-700">
                  नेपालमा १ रुपियाँभन्दा सानो पैसा चलनचल्तीमा नभएकाले निकटतम पूर्णाङ्कमा शून्यान्त गरिन्छ। दशमलवपछिको अङ्क $७ \\ge 5$ भएकाले ३४६ मा १ थपिन्छ $\\implies 346.72 \\approx 347$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: रु ३४७ तिर्नुपर्ला।
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  २ (ख) घनाकार ट्याङ्कीको आयतन ३४५.५४३ घनफिट ($\text{ft}^3$) भए:
                </h4>
                <div class="text-xs text-slate-700 space-y-1">
                  <div>(i) पूर्णाङ्कमा: $345.543 \\approx 346\\text{ ft}^3$ <span class="text-slate-400">(दशांश अङ्क $५ \\ge 5$)</span></div>
                  <div>(ii) दोस्रो दशमलव स्थानमा: $345.543 \\approx 345.54\\text{ ft}^3$ <span class="text-slate-400">(तेस्रो अङ्क $३ < 5$)</span></div>
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: (i) ३४६ घनफिट र (ii) ३४५.५४ घनफिट
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm">
                  २ (ग) ४ ओटा सयपत्री मालाको मूल्य रु २७५ पर्दा १ ओटाको मूल्य कति पर्ला? (दशमलवको १ स्थानमा शून्यान्त)
                </h4>
                <div class="text-xs text-slate-700">
                  १ मालाको मूल्य $= 275 \\div 4 = \\text{रु } 68.75$। दोस्रो अङ्क $५ \\ge 5$ भएकाले ७ मा १ थपिन्छ $\\implies 68.75 \\approx 68.8$
                </div>
                <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-2 rounded-lg border border-emerald-200 inline-block">
                  ✓ उत्तर: एउटा मालाको मूल्य रु ६८.८० पर्ला।
                </div>
              </div>

              <div class="p-4 bg-blue-50 rounded-xl border border-blue-200 space-y-2">
                <h4 class="font-bold text-blue-900 text-xs md:text-sm">
                  ३. प्रयोगात्मक कार्य (Classroom Activity)
                </h4>
                <p class="text-xs text-blue-800">
                  कक्षाकोठामा बेन्चको लम्बाइ (उदा: $120.4\\text{ cm}$) र सिसाकलम (उदा: $14.8\\text{ cm}$) नापेर वास्तविक भाग $\\frac{120.4}{14.8} \\approx 8.135$ र शून्यान्तपछिको भाग $\\frac{120}{15} = 8$ तुलना गर्दा शून्यान्तले छिटो र भरपर्दो अनुमान निकाल्न मद्दत गर्दछ भनी निष्कर्ष निकालिन्छ।
                </p>
              </div>
            </div>

          </div>

        </div>

        <!-- ================= CH5 TAB 3: TIERS ================= -->
        <div id="ch5-view-tiers" class="hidden space-y-6">
          <div class="bg-indigo-50 border border-indigo-200 p-4 rounded-2xl">
            <h4 class="font-black text-indigo-950 text-sm md:text-base">पाठ्यक्रम विकास केन्द्र (CDC) विशिष्टीकरण तालिकामा आधारित ३-तहका नमुना प्रश्नहरू</h4>
            <p class="text-xs text-indigo-800 mt-1">
              विद्यार्थीहरूको अवधारणागत स्पष्टता, सीप प्रयोग, र उच्चस्तरीय समस्या समाधान क्षमता परीक्षण गर्न तयार पारिएका प्रश्नहरू र मार्किङ स्किम:
            </p>
          </div>

          <!-- Tier 1: Knowledge (1 mark) -->
          <div class="bg-white p-6 rounded-2xl border-l-4 border-amber-500 border-slate-200 border shadow-sm space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-xs font-bold">K</span>
                तह १: आधारभूत ज्ञान तथा बुझाइ (Knowledge Level - १ अङ्क)
              </h3>
              <span class="text-xs font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-xl">४ प्रश्नहरू</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न १.१: $४७.३०९$ मा अङ्क $०$ को स्थानीय मान कति हो?</div>
                <div class="text-slate-600">दशमलवपछिको दोस्रो स्थान भएकाले शतांश (Hundredths) हो।</div>
                <div class="font-bold text-amber-800">उत्तर: शतांश ($\\frac{0}{100}$) [१ अङ्क]</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न १.२: $\\frac{9}{100}$ लाई दशमलव सङ्ख्यामा रूपान्तरण गर्नुहोस्।</div>
                <div class="text-slate-600">हरमा १०० भएकाले दायाँबाट २ स्थान बायाँ बिन्दु बस्छ।</div>
                <div class="font-bold text-amber-800">उत्तर: $0.09$ [१ अङ्क]</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न १.३: $५.४३२ \\times १०००$ को मान कति हुन्छ?</div>
                <div class="text-slate-600">१००० ले गुणन गर्दा दशमलव बिन्दु ३ स्थान दायाँ सर्दछ।</div>
                <div class="font-bold text-amber-800">उत्तर: $5432$ [१ अङ्क]</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न १.४: $७२.८५ \\div १००$ को मान कति हुन्छ?</div>
                <div class="text-slate-600">१०० ले भाग गर्दा दशमलव बिन्दु २ स्थान बायाँ सर्दछ।</div>
                <div class="font-bold text-amber-800">उत्तर: $0.7285$ [१ अङ्क]</div>
              </div>
            </div>
          </div>

          <!-- Tier 2: Application (2 marks) -->
          <div class="bg-white p-6 rounded-2xl border-l-4 border-blue-500 border-slate-200 border shadow-sm space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold">A</span>
                तह २: सीप तथा प्रयोग (Application Level - २ अङ्क)
              </h3>
              <span class="text-xs font-bold bg-blue-100 text-blue-800 px-3 py-1 rounded-xl">४ प्रश्नहरू</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न २.१: मान पत्ता लगाउनुहोस्: $४.२५ \\times ३.२$</div>
                <div class="text-slate-600">• $425 \\times 32 = 13600$ [१ अङ्क]</div>
                <div class="text-slate-600">• ३ अङ्क अघि दशमलव: $13.600 = 13.6$ [१ अङ्क]</div>
                <div class="font-bold text-blue-800">उत्तर: $13.6$</div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न २.२: भाग गर्नुहोस्: $४५.३६ \\div ०.६$</div>
                <div class="text-slate-600">• १० ले गुणन गर्दा: $\\frac{453.6}{6}$ [१ अङ्क]</div>
                <div class="text-slate-600">• भाग गर्दा: $75.6$ [१ अङ्क]</div>
                <div class="font-bold text-blue-800">उत्तर: $75.6$</div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न २.३: १ कलमको मूल्य रु १५.७५ भए ८ कलमको मूल्य कति पर्ला?</div>
                <div class="text-slate-600">• सूत्र: $8 \\times 15.75$ [१ अङ्क]</div>
                <div class="text-slate-600">• गुणनफल: $\\text{रु } 126.00$ [१ अङ्क]</div>
                <div class="font-bold text-blue-800">उत्तर: रु १२६</div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs">
                <div class="font-bold text-slate-800">प्रश्न २.४: $१२.३४२, ४५.६७८, ०.९५१$ लाई दोस्रो स्थानमा शून्यान्त गर्नुहोस्।</div>
                <div class="text-slate-600">• $12.342 \\approx 12.34$, $45.678 \\approx 45.68$ [१ अङ्क]</div>
                <div class="text-slate-600">• $0.951 \\approx 0.95$ [१ अङ्क]</div>
                <div class="font-bold text-blue-800">उत्तर: क्रमशः १२.३४, ४५.६८ र ०.९५</div>
              </div>
            </div>
          </div>

          <!-- Tier 3: Higher Ability (4 marks) -->
          <div class="bg-white p-6 rounded-2xl border-l-4 border-purple-500 border-slate-200 border shadow-sm space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-bold">HA</span>
                तह ३: उच्च दक्षता तथा समस्या समाधान (Higher Ability - ४ अङ्क)
              </h3>
              <span class="text-xs font-bold bg-purple-100 text-purple-800 px-3 py-1 rounded-xl">२ विस्तृत प्रश्नहरू</span>
            </div>

            <!-- Problem 1 -->
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2 text-xs md:text-sm">
              <h4 class="font-black text-slate-900">
                प्रश्न ३.१: लम्बाइ १२.५ मिटर र चौडाइ ८.४ मिटर भएको एउटा आयताकार कोठाको भुइँमा प्रति वर्गमिटर रु १५० का दरले कार्पेट ओछ्याउन कति खर्च लाग्ला?
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
                <div class="p-3 bg-white border border-slate-200 rounded-lg">
                  <div class="font-bold text-slate-700 mb-1">(क) कोठाको क्षेत्रफल</div>
                  <div class="text-xs text-slate-600">$A = l \\times b = 12.5 \\times 8.4 = 105\\text{ m}^2$</div>
                  <div class="font-bold text-purple-700 text-xs mt-1">[अङ्क: १.५]</div>
                </div>
                <div class="p-3 bg-white border border-slate-200 rounded-lg">
                  <div class="font-bold text-slate-700 mb-1">(ख) कार्पेट ओछ्याउने खर्च</div>
                  <div class="text-xs text-slate-600">$T = 105 \\times 150 = \\text{रु } 15,750$</div>
                  <div class="font-bold text-purple-700 text-xs mt-1">[अङ्क: १.५]</div>
                </div>
                <div class="p-3 bg-white border border-slate-200 rounded-lg">
                  <div class="font-bold text-slate-700 mb-1">(ग) कोठाको परिमिति</div>
                  <div class="text-xs text-slate-600">$P = 2(12.5 + 8.4) = 41.8\\text{ m}$</div>
                  <div class="font-bold text-purple-700 text-xs mt-1">[अङ्क: १.०]</div>
                </div>
              </div>
            </div>

            <!-- Problem 2 -->
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2 text-xs md:text-sm">
              <h4 class="font-black text-slate-900">
                प्रश्न ३.२: एउटा किराना पसलेले रु ५,४०० मा ७५ केजी चिनी किनेर प्रति केजी रु ७८.५० का दरले बेचेछन्।
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
                <div class="p-3 bg-white border border-slate-200 rounded-lg">
                  <div class="font-bold text-slate-700 mb-1">(क) १ केजीको खरिद मूल्य</div>
                  <div class="text-xs text-slate-600">$= \\frac{5400}{75} = \\text{रु } 72$</div>
                  <div class="font-bold text-purple-700 text-xs mt-1">[अङ्क: १.५]</div>
                </div>
                <div class="p-3 bg-white border border-slate-200 rounded-lg">
                  <div class="font-bold text-slate-700 mb-1">(ख) १ केजीमा नाफा</div>
                  <div class="text-xs text-slate-600">$= 78.50 - 72 = \\text{रु } 6.50$</div>
                  <div class="font-bold text-purple-700 text-xs mt-1">[अङ्क: १.५]</div>
                </div>
                <div class="p-3 bg-white border border-slate-200 rounded-lg">
                  <div class="font-bold text-slate-700 mb-1">(ग) कुल ७५ केजीमा नाफा</div>
                  <div class="text-xs text-slate-600">$= 75 \\times 6.50 = \\text{रु } 487.50$</div>
                  <div class="font-bold text-purple-700 text-xs mt-1">[अङ्क: १.०]</div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- ================= CH5 TAB 4: QUIZ ================= -->
        <div id="ch5-view-quiz" class="hidden space-y-6">
          <div class="bg-emerald-50 border border-emerald-200 p-4 rounded-2xl flex items-center justify-between">
            <div>
              <h4 class="font-black text-emerald-950 text-sm md:text-base">पाठ ५: दशमलव - आत्म-मूल्याङ्कन क्विज</h4>
              <p class="text-xs text-emerald-800">प्रत्येक प्रश्नको सही विकल्प रोज्नुहोस् र तुरुन्तै विस्तृत गणितीय व्याख्या प्राप्त गर्नुहोस्।</p>
            </div>
            <button onclick="resetQuizCh5()" class="px-3.5 py-1.5 rounded-xl bg-white border border-emerald-300 text-xs font-bold text-emerald-700 hover:bg-emerald-100 shadow-xs">
              🔄 रिसेट
            </button>
          </div>

          <!-- Quiz Question 1 -->
          <div class="bg-white p-5 md:p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">प्रश्न १ / ४</span>
              <span id="ch5-qbadge-0" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <h4 class="font-black text-slate-800 text-sm md:text-base">
              $\\frac{7}{100}$ लाई दशमलव सङ्ख्यामा लेख्दा कुन मान सही हुन्छ?
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch5-qbtn-0-0" onclick="checkQuizCh5(0, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (A) $0.7$
              </button>
              <button id="ch5-qbtn-0-1" onclick="checkQuizCh5(0, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (B) $0.07$
              </button>
              <button id="ch5-qbtn-0-2" onclick="checkQuizCh5(0, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (C) $0.007$
              </button>
              <button id="ch5-qbtn-0-3" onclick="checkQuizCh5(0, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (D) $7.0$
              </button>
            </div>
            <div id="ch5-qexp-0" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Quiz Question 2 -->
          <div class="bg-white p-5 md:p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">प्रश्न २ / ४</span>
              <span id="ch5-qbadge-1" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <h4 class="font-black text-slate-800 text-sm md:text-base">
              $३.४५ \\times १०$ को गुणनफल कति हुन्छ?
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch5-qbtn-1-0" onclick="checkQuizCh5(1, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (A) $०.३४५$
              </button>
              <button id="ch5-qbtn-1-1" onclick="checkQuizCh5(1, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (B) $३४.५$
              </button>
              <button id="ch5-qbtn-1-2" onclick="checkQuizCh5(1, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (C) $३४५$
              </button>
              <button id="ch5-qbtn-1-3" onclick="checkQuizCh5(1, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (D) $३.४५०$
              </button>
            </div>
            <div id="ch5-qexp-1" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Quiz Question 3 -->
          <div class="bg-white p-5 md:p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">प्रश्न ३ / ४</span>
              <span id="ch5-qbadge-2" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <h4 class="font-black text-slate-800 text-sm md:text-base">
              $२५.४ \\div १००$ गर्दा भागफल कति आउँछ?
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch5-qbtn-2-0" onclick="checkQuizCh5(2, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (A) $०.२५४$
              </button>
              <button id="ch5-qbtn-2-1" onclick="checkQuizCh5(2, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (B) $२.५४$
              </button>
              <button id="ch5-qbtn-2-2" onclick="checkQuizCh5(2, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (C) $२५४$
              </button>
              <button id="ch5-qbtn-2-3" onclick="checkQuizCh5(2, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (D) $२५४०$
              </button>
            </div>
            <div id="ch5-qexp-2" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Quiz Question 4 -->
          <div class="bg-white p-5 md:p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">प्रश्न ४ / ४</span>
              <span id="ch5-qbadge-3" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <h4 class="font-black text-slate-800 text-sm md:text-base">
              $०.५ \\times ०.२$ को मान कति हुन्छ?
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch5-qbtn-3-0" onclick="checkQuizCh5(3, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (A) $०.१$
              </button>
              <button id="ch5-qbtn-3-1" onclick="checkQuizCh5(3, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (B) $०.०१$
              </button>
              <button id="ch5-qbtn-3-2" onclick="checkQuizCh5(3, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (C) $१.०$
              </button>
              <button id="ch5-qbtn-3-3" onclick="checkQuizCh5(3, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">
                (D) $०.००१$
              </button>
            </div>
            <div id="ch5-qexp-3" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

        </div>

      </div>
      <!-- ================= END OF CHAPTER 5 VIEW ================= -->
"""

if __name__ == "__main__":
    html = get_ch5_html()
    print("Generated Chapter 5 HTML successfully. Length:", len(html))
