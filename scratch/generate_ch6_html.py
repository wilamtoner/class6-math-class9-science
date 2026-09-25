# -*- coding: utf-8 -*-
"""
Generates the HTML content for Chapter 6 (प्रतिशत - Percentage) of Class 6 Mathematics.
Matches the design, CSS, and MathJax conventions of Chapters 1 to 5.
"""

def get_ch6_html():
    return """
      <!-- ================= CHAPTER 6: PERCENTAGE (प्रतिशत) ================= -->
      <div id="chapter-view-6" class="hidden flex-1 flex flex-col">
        <!-- Top Chapter Banner -->
        <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-blue-600 mb-1">एकाइ २: अङ्कगणित (Unit 2: Arithmetic)</div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ ६: प्रतिशत (Percentage)</h2>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ ८६–९१</span>
            <span class="text-xs bg-blue-100 text-blue-800 font-bold px-3 py-1 rounded-xl border border-blue-200">अभ्यास ६ तथा परियोजना कार्य</span>
          </div>
        </div>

        <!-- Chapter 6 Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button id="ch6-tab-concepts" onclick="setTabCh6('concepts')" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap">
            १. अवधारणा, नियम र क्याल्कुलेटर
          </button>
          <button id="ch6-tab-exercises" onclick="setTabCh6('exercises')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            २. सम्पूर्ण अभ्यास समाधान (अभ्यास ६)
          </button>
          <button id="ch6-tab-tiers" onclick="setTabCh6('tiers')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ३. तीन तहका नमुना प्रश्नहरू
          </button>
          <button id="ch6-tab-quiz" onclick="setTabCh6('quiz')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ४. आत्म-मूल्याङ्कन क्विज
          </button>
        </div>

        <!-- ================= CH6 TAB 1: CONCEPTS ================= -->
        <div id="ch6-view-concepts" class="space-y-6">
          
          <!-- Concept 1: Definition & Visual Model -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-base">💯</span>
              प्रतिशतको परिचय र १००-ग्रिड अवधारणा (Concept of Percentage)
            </h3>
            <p class="text-xs md:text-sm text-slate-600 mb-4">
              <strong>प्रतिशत (Percentage)</strong> दुई शब्द <em>'प्रति' (Per)</em> र <em>'शत' (Hundred/सय)</em> मिलेर बनेको हो, जसको अर्थ <strong>"प्रति सय"</strong> वा <strong>"सयमा कति"</strong> भन्ने हुन्छ। गणितीय रूपमा <strong>हर (Denominator) १०० भएको भिन्नलाई प्रतिशत भनिन्छ</strong>। यसको सङ्केत <strong>$\\%$</strong> हो।
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
              <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl">
                <span class="text-xs font-bold text-blue-600 uppercase tracking-wider block mb-1">प्रतिशतको गणितीय सूत्र</span>
                <div class="text-base font-bold text-slate-800">
                  $$\\text{प्रतिशत } (\\%) = \\frac{\\text{मान}}{१००} = \\frac{\\text{अंश}}{१००}$$
                </div>
                <p class="text-xs text-slate-600 mt-2">
                  उदाहरण: $२५\\% = \\frac{25}{100} = \\frac{1}{4}$ (१०० भागमा २५ भाग अर्थात् एक चौथाइ)।
                </p>
              </div>

              <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl">
                <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider block mb-1">परिमाणको प्रतिशत निकाल्ने सूत्र</span>
                <div class="text-base font-bold text-slate-800">
                  $$\\text{मान} = \\text{कुल परिमाण} \\times \\frac{\\text{प्रतिशत}}{१००}$$
                </div>
                <p class="text-xs text-slate-600 mt-2">
                  उदाहरण: रु. ५०० को २०% $= 500 \\times \\frac{20}{100} = \\text{रु. } 100$।
                </p>
              </div>
            </div>

            <!-- INTERACTIVE PERCENTAGE VISUALIZER -->
            <div class="p-5 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-2xl">
              <h4 class="text-sm font-bold text-slate-800 mb-2 flex items-center justify-between">
                <span class="flex items-center gap-2">🎨 अन्तरक्रियात्मक १००-ग्रिड र बार भिजुअलाइजर (Interactive Visualizer)</span>
                <span id="ch6-vis-val-badge" class="px-2.5 py-0.5 rounded-lg bg-blue-600 text-white font-mono text-xs">40%</span>
              </h4>
              <p class="text-xs text-slate-600 mb-3">तलको स्लाइडर सार्नुहोस् र प्रतिशत, भिन्न, र दशमलवको तत्काल रूपान्तरण हेर्नुहोस्:</p>
              
              <div class="flex items-center gap-3 mb-4">
                <span class="text-xs font-bold text-slate-500">0%</span>
                <input id="ch6-slider" type="range" min="0" max="100" value="40" oninput="updateCh6Visualizer(this.value)" class="w-full accent-blue-600 cursor-pointer">
                <span class="text-xs font-bold text-slate-500">100%</span>
              </div>

              <!-- Progress Bar Representation -->
              <div class="w-full bg-slate-200 h-6 rounded-xl overflow-hidden mb-4 p-0.5 border border-slate-300">
                <div id="ch6-progress-bar" class="bg-gradient-to-r from-blue-500 to-indigo-600 h-full rounded-lg transition-all duration-200 flex items-center justify-end pr-2 text-[10px] font-bold text-white" style="width: 40%;">
                  40%
                </div>
              </div>

              <!-- Output Cards -->
              <div class="grid grid-cols-3 gap-2 text-center text-xs md:text-sm">
                <div class="bg-white p-2.5 rounded-xl border border-slate-200 shadow-xs">
                  <span class="text-[10px] uppercase font-bold text-slate-400 block">प्रतिशत</span>
                  <span id="ch6-vis-pct" class="font-black text-blue-600 text-base">40%</span>
                </div>
                <div class="bg-white p-2.5 rounded-xl border border-slate-200 shadow-xs">
                  <span class="text-[10px] uppercase font-bold text-slate-400 block">भिन्न (लघुतम पद)</span>
                  <span id="ch6-vis-frac" class="font-black text-emerald-600 text-base">2/5</span>
                </div>
                <div class="bg-white p-2.5 rounded-xl border border-slate-200 shadow-xs">
                  <span class="text-[10px] uppercase font-bold text-slate-400 block">दशमलव</span>
                  <span id="ch6-vis-dec" class="font-black text-indigo-600 text-base">0.40</span>
                </div>
              </div>
            </div>

          </div>

          <!-- Concept 2: Live Percentage Calculator -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-teal-100 text-teal-700 flex items-center justify-center text-base">🧮</span>
              लाइभ प्रतिशत क्याल्कुलेटर (Live Interactive Percentage Calculators)
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Calculator 1: X of Y% -->
              <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-3">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm flex items-center gap-1.5 text-teal-800">
                  <span>१. परिमाणको प्रतिशत निकाल्नुहोस् ($X \\text{ को } Y\\%$)</span>
                </h4>
                <div class="flex items-center gap-2 text-xs">
                  <input id="calc1-qty" type="number" value="400" placeholder="परिमाण (X)" class="w-1/2 p-2 rounded-lg border border-slate-300 font-bold text-slate-800">
                  <span>को</span>
                  <input id="calc1-pct" type="number" value="85" placeholder="प्रतिशत (Y)" class="w-1/3 p-2 rounded-lg border border-slate-300 font-bold text-slate-800">
                  <span>%</span>
                  <button onclick="runCh6Calc1()" class="px-3 py-2 bg-teal-600 text-white rounded-lg font-bold hover:bg-teal-700">निकाल</button>
                </div>
                <div id="calc1-res" class="p-2.5 bg-white rounded-lg border border-teal-200 text-xs font-semibold text-teal-900">
                  उत्तर: <strong>४०० को ८५% = ३४०</strong> ($400 \\times \\frac{85}{100} = 340$)
                </div>
              </div>

              <!-- Calculator 2: Fraction to Percentage -->
              <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-3">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm flex items-center gap-1.5 text-indigo-800">
                  <span>२. भिन्न वा दशमलव $\\rightarrow$ प्रतिशत कन्भर्टर</span>
                </h4>
                <div class="flex items-center gap-2 text-xs">
                  <input id="calc2-num" type="number" value="3" placeholder="अंश" class="w-1/4 p-2 rounded-lg border border-slate-300 font-bold text-slate-800">
                  <span class="font-bold text-slate-500">/</span>
                  <input id="calc2-den" type="number" value="20" placeholder="हर" class="w-1/4 p-2 rounded-lg border border-slate-300 font-bold text-slate-800">
                  <button onclick="runCh6Calc2()" class="px-3 py-2 bg-indigo-600 text-white rounded-lg font-bold hover:bg-indigo-700">बदल</button>
                </div>
                <div id="calc2-res" class="p-2.5 bg-white rounded-lg border border-indigo-200 text-xs font-semibold text-indigo-900">
                  उत्तर: <strong>3/20 = 15%</strong> (दशमलव: 0.15)
                </div>
              </div>
            </div>
          </div>

          <!-- Concept 3: Conversion Rules -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-base">⚡</span>
              प्रतिशत रूपान्तरणका ३ सुनौला नियमहरू (3 Golden Conversion Rules)
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm mb-1 text-blue-700">१. भिन्न $\\rightarrow$ प्रतिशत</h4>
                <p class="text-xs text-slate-600 mb-2">भिन्नलाई $१००\\%$ ले गुणन गर्ने वा हरलाई १०० बनाउने:</p>
                <div class="text-xs bg-white p-2 border rounded font-mono">
                  $\\frac{2}{5} \\times 100\\% = 40\\%$
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm mb-1 text-emerald-700">२. दशमलव $\\rightarrow$ प्रतिशत</h4>
                <p class="text-xs text-slate-600 mb-2">दशमलवलाई १००% ले गुणन गर्दा बिन्दु २ स्थान दायाँ सर्छ:</p>
                <div class="text-xs bg-white p-2 border rounded font-mono">
                  $0.45 = 45\\%$<br>$1.8 = 180\\%$
                </div>
              </div>

              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                <h4 class="font-bold text-slate-800 text-xs md:text-sm mb-1 text-rose-700">३. प्रतिशत $\\rightarrow$ भिन्न/दशमलव</h4>
                <p class="text-xs text-slate-600 mb-2">% हटाएर १०० ले भाग गर्ने र न्यूनतम पदमा लैजाने:</p>
                <div class="text-xs bg-white p-2 border rounded font-mono">
                  $25\\% = \\frac{25}{100} = \\frac{1}{4} = 0.25$
                </div>
              </div>
            </div>
          </div>

          <!-- Concept 4: Standard Conversion Reference Table -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h3 class="text-lg font-black text-slate-800 mb-2 flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-purple-100 text-purple-700 flex items-center justify-center text-base">📊</span>
              दैनिक जीवनमा प्रयोग हुने महत्त्वपूर्ण रूपान्तरण तालिका (Reference Table)
            </h3>
            
            <div class="overflow-x-auto rounded-xl border border-slate-200">
              <table class="w-full text-xs md:text-sm text-center">
                <thead class="bg-slate-100 font-bold text-slate-700">
                  <tr>
                    <th class="p-2.5 border-b">भिन्न (Fraction)</th>
                    <th class="p-2.5 border-b">दशमलव (Decimal)</th>
                    <th class="p-2.5 border-b text-blue-600">प्रतिशत (Percentage)</th>
                    <th class="p-2.5 border-b text-left">दैनिक जीवनमा अर्थ</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 text-slate-800">
                  <tr><td class="p-2 font-mono">1/10</td><td class="p-2">0.1</td><td class="p-2 font-bold text-blue-600">10%</td><td class="p-2 text-left text-slate-500">दसमा एक भाग</td></tr>
                  <tr class="bg-slate-50"><td class="p-2 font-mono">1/5</td><td class="p-2">0.2</td><td class="p-2 font-bold text-blue-600">20%</td><td class="p-2 text-left text-slate-500">पाँचमा एक भाग</td></tr>
                  <tr><td class="p-2 font-mono">1/4</td><td class="p-2">0.25</td><td class="p-2 font-bold text-blue-600">25%</td><td class="p-2 text-left text-slate-500">एक चौथाइ (Quarter)</td></tr>
                  <tr class="bg-slate-50"><td class="p-2 font-mono">1/3</td><td class="p-2">0.333...</td><td class="p-2 font-bold text-blue-600">33⅓%</td><td class="p-2 text-left text-slate-500">एक तिहाइ</td></tr>
                  <tr><td class="p-2 font-mono">2/5</td><td class="p-2">0.4</td><td class="p-2 font-bold text-blue-600">40%</td><td class="p-2 text-left text-slate-500">पाँचमा दुई भाग</td></tr>
                  <tr class="bg-slate-50"><td class="p-2 font-mono">1/2</td><td class="p-2">0.5</td><td class="p-2 font-bold text-blue-600">50%</td><td class="p-2 text-left text-slate-500">आधा (Half)</td></tr>
                  <tr><td class="p-2 font-mono">3/5</td><td class="p-2">0.6</td><td class="p-2 font-bold text-blue-600">60%</td><td class="p-2 text-left text-slate-500">पाँचमा तीन भाग</td></tr>
                  <tr class="bg-slate-50"><td class="p-2 font-mono">3/4</td><td class="p-2">0.75</td><td class="p-2 font-bold text-blue-600">75%</td><td class="p-2 text-left text-slate-500">तीन चौथाइ</td></tr>
                  <tr><td class="p-2 font-mono">1/1</td><td class="p-2">1.0</td><td class="p-2 font-bold text-blue-600">100%</td><td class="p-2 text-left text-slate-500">सम्पूर्ण सिङ्गो वस्तु</td></tr>
                </tbody>
              </table>
            </div>
          </div>

        </div>

        <!-- ================= CH6 TAB 2: EXERCISES ================= -->
        <div id="ch6-view-exercises" class="hidden space-y-6">
          
          <!-- Exercise Navigation Pills -->
          <div class="flex gap-2 overflow-x-auto pb-2 border-b border-slate-200 text-xs md:text-sm font-bold">
            <button id="ch6-pill-sec1" onclick="setExerciseCh6('sec1')" class="px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap">
              भाग १: प्रश्न १ देखि ३ (आधारभूत रूपान्तरण)
            </button>
            <button id="ch6-pill-sec2" onclick="setExerciseCh6('sec2')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              भाग २: प्रश्न ४ देखि ७ (मान तथा व्यावहारिक समस्या)
            </button>
            <button id="ch6-pill-sec3" onclick="setExerciseCh6('sec3')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              भाग ३: परियोजना कार्य तथा उदाहरणहरू
            </button>
          </div>

          <!-- ---------------- SECTION: EXERCISE 6 PART 1 ---------------- -->
          <div id="ch6-sec-sec1" class="space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">अभ्यास ६: आधारभूत रूपान्तरण तथा तथ्य परीक्षण</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ ९० (प्रश्न १, २, र ३ को १००% विस्तृत समाधान)</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">१४ उपप्रश्नहरू</span>
            </div>

            <!-- Q1 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न १: तलका तथ्यहरू ठीक भए (√) र बेठीक भए (×) चिह्न लगाउनुहोस्:</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="flex items-center justify-between mb-1">
                    <span class="font-bold text-slate-700">(क) १०० भागमा २५ भागलाई २५% भनिन्छ।</span>
                    <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold text-xs">✓ ठीक</span>
                  </div>
                  <p class="text-xs text-slate-500">कारण: परिभाषानुसार हर १०० भएको भिन्न $\\frac{25}{100} = 25\\%$ हो।</p>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="flex items-center justify-between mb-1">
                    <span class="font-bold text-slate-700">(ख) $\\frac{3}{4}$ लाई प्रतिशतमा लेख्दा २५% हुन्छ।</span>
                    <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-bold text-xs">✗ बेठीक</span>
                  </div>
                  <p class="text-xs text-slate-500">कारण: $\\frac{3}{4} \\times 100\\% = 75\\%$ हुन्छ, २५% होइन।</p>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="flex items-center justify-between mb-1">
                    <span class="font-bold text-slate-700">(ग) $०.४५\\%$ लाई लघुतम पदमा लेख्दा $\\frac{9}{20}$ हुन्छ।</span>
                    <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-bold text-xs">✗ बेठीक</span>
                  </div>
                  <p class="text-xs text-slate-500">कारण: $0.45\\% = \\frac{45}{10000} = \\frac{9}{2000}$ हुन्छ। $\\frac{9}{20}$ हुन दशमलव $0.45$ मात्र हुनुपर्छ।</p>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="flex items-center justify-between mb-1">
                    <span class="font-bold text-slate-700">(घ) भिन्न वा दशमलवलाई प्रतिशतमा बदल्दा १०० ले भाग गरी % चिह्न राख्नुपर्दछ।</span>
                    <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-bold text-xs">✗ बेठीक</span>
                  </div>
                  <p class="text-xs text-slate-500">कारण: प्रतिशतमा बदल्न १०० ले <strong>गुणन</strong> गर्नुपर्छ, भाग होइन।</p>
                </div>

              </div>
            </div>

            <!-- Q2 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न २: तलका प्रत्येक प्रतिशतलाई भिन्नमा व्यक्त गरी लघुतम पदमा रूपान्तरण गर्नुहोस्:</h4>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs md:text-sm">
                
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(क) $२२\\%$</div>
                  <div class="text-xs text-slate-600">$= \\frac{22}{100} = \\frac{22 \\div 2}{100 \\div 2}$</div>
                  <div class="text-xs font-bold text-blue-600 mt-1">उत्तर: $\\frac{11}{50}$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(ख) $५७\\%$</div>
                  <div class="text-xs text-slate-600">$= \\frac{57}{100}$ (साझा गुणनखण्ड १ मात्र)</div>
                  <div class="text-xs font-bold text-blue-600 mt-1">उत्तर: $\\frac{57}{100}$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(ग) $६३\\%$</div>
                  <div class="text-xs text-slate-600">$= \\frac{63}{100}$ (साझा गुणनखण्ड १ मात्र)</div>
                  <div class="text-xs font-bold text-blue-600 mt-1">उत्तर: $\\frac{63}{100}$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(घ) $१.५\\%$</div>
                  <div class="text-xs text-slate-600">$= \\frac{1.5}{100} = \\frac{15}{1000} = \\frac{15 \\div 5}{1000 \\div 5}$</div>
                  <div class="text-xs font-bold text-blue-600 mt-1">उत्तर: $\\frac{3}{200}$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(ङ) $०.५\\%$</div>
                  <div class="text-xs text-slate-600">$= \\frac{0.5}{100} = \\frac{5}{1000} = \\frac{5 \\div 5}{1000 \\div 5}$</div>
                  <div class="text-xs font-bold text-blue-600 mt-1">उत्तर: $\\frac{1}{200}$</div>
                </div>

              </div>
            </div>

            <!-- Q3 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न ३: तल दिइएका भिन्न र दशमलवलाई प्रतिशतमा व्यक्त गर्नुहोस्:</h4>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs md:text-sm">
                
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(क) $\\frac{2}{5}$</div>
                  <div class="text-xs text-slate-600">$= \\frac{2}{5} \\times 100\\% = 2 \\times 20\\%$</div>
                  <div class="text-xs font-bold text-emerald-600 mt-1">उत्तर: $40\\%$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(ख) $\\frac{3}{20}$</div>
                  <div class="text-xs text-slate-600">$= \\frac{3}{20} \\times 100\\% = 3 \\times 5\\%$</div>
                  <div class="text-xs font-bold text-emerald-600 mt-1">उत्तर: $15\\%$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(ग) $०.४५$</div>
                  <div class="text-xs text-slate-600">$= 0.45 \\times 100\\%$ (बिन्दु २ स्थान दायाँ)</div>
                  <div class="text-xs font-bold text-emerald-600 mt-1">उत्तर: $45\\%$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(घ) $१.८$</div>
                  <div class="text-xs text-slate-600">$= 1.8 \\times 100\\%$</div>
                  <div class="text-xs font-bold text-emerald-600 mt-1">उत्तर: $180\\%$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-700 mb-1">(ङ) $०.०३$</div>
                  <div class="text-xs text-slate-600">$= 0.03 \\times 100\\%$</div>
                  <div class="text-xs font-bold text-emerald-600 mt-1">उत्तर: $3\\%$</div>
                </div>

              </div>
            </div>

          </div>

          <!-- ---------------- SECTION: EXERCISE 6 PART 2 ---------------- -->
          <div id="ch6-sec-sec2" class="hidden space-y-6">
            <div class="bg-emerald-50 border border-emerald-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-emerald-900 text-sm md:text-base">अभ्यास ६: परिमाणको प्रतिशत र व्यावहारिक समस्याहरू</h4>
                <p class="text-xs text-emerald-700">पाठ्यपुस्तक पृष्ठ ९० (प्रश्न ४, ५, ६, र ७ को विस्तृत चरणबद्ध समाधान)</p>
              </div>
              <span class="text-xs font-bold bg-white text-emerald-800 px-3 py-1 rounded-xl shadow-xs border border-emerald-200">प्रश्न ४ देखि ७</span>
            </div>

            <!-- Q4 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न ४: तल दिइएका अवस्थाहरूको मान निकाल्नुहोस्:</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">(क) रु. ४०० को ८५% कति हुन्छ?</div>
                  <div class="text-xs text-slate-600 mb-1">$= 400 \\times \\frac{85}{100} = 4 \\times 85$</div>
                  <div class="text-sm font-bold text-blue-600">उत्तर: रु. ३४०</div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">(ख) रु. १५०० को २०% कति हुन्छ?</div>
                  <div class="text-xs text-slate-600 mb-1">$= 1500 \\times \\frac{20}{100} = 15 \\times 20$</div>
                  <div class="text-sm font-bold text-blue-600">उत्तर: रु. ३००</div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">(ग) १००० l (लिटर) को २५% कति हुन्छ?</div>
                  <div class="text-xs text-slate-600 mb-1">$= 1000 \\times \\frac{25}{100} = 10 \\times 25$</div>
                  <div class="text-sm font-bold text-blue-600">उत्तर: २५० लिटर ($250\\text{ l}$)</div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">(घ) २ km को १५% कति हुन्छ?</div>
                  <div class="text-xs text-slate-600 mb-1">$2\\text{ km} = 2000\\text{ m} \\implies 2000 \\times \\frac{15}{100} = 20 \\times 15$</div>
                  <div class="text-sm font-bold text-blue-600">उत्तर: ३०० मिटर ($300\\text{ m}$) वा $0.3\\text{ km}$</div>
                </div>

                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 md:col-span-2">
                  <div class="font-bold text-slate-800 mb-1">(ङ) १२८० m को ७५% कति हुन्छ?</div>
                  <div class="text-xs text-slate-600 mb-1">$= 1280 \\times \\frac{75}{100} = 1280 \\times \\frac{3}{4} = 320 \\times 3$</div>
                  <div class="text-sm font-bold text-blue-600">उत्तर: ९६० मिटर ($960\\text{ m}$)</div>
                </div>

              </div>
            </div>

            <!-- Q5 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2 flex items-center justify-between">
                <span>प्रश्न ५: ५०० विद्यार्थीमध्ये २०० ले फुटबल मन पराएको अवस्था</span>
                <span class="text-xs px-2 py-0.5 rounded bg-amber-100 text-amber-800 font-bold">मुद्रणदोष विश्लेषण सहित</span>
              </h4>
              <p class="text-xs text-slate-600">५०० विद्यार्थीहरूमध्ये २०० विद्यार्थीहरूले फुटबल खेल्न मन पराए भने:</p>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl">
                  <span class="font-bold text-blue-900 block text-xs mb-1">(क) फुटबल मन पराउने विद्यार्थीको प्रतिशत:</span>
                  <div class="text-xs text-slate-700">$$\\frac{200}{500} \\times 100\\% = \\frac{200}{5}\\% = 40\\%$$</div>
                  <div class="text-xs font-bold text-blue-700 mt-1">उत्तर: ४०%</div>
                </div>

                <div class="p-4 bg-indigo-50 border border-indigo-200 rounded-xl">
                  <span class="font-bold text-indigo-900 block text-xs mb-1">(ख) फुटबल मन नपराउने विद्यार्थीको प्रतिशत:</span>
                  <div class="text-xs text-slate-700">मन नपराउने $= 500 - 200 = 300$<br>$$\\frac{300}{500} \\times 100\\% = 60\\%$$</div>
                  <div class="text-xs font-bold text-indigo-700 mt-1">उत्तर: ६०%</div>
                </div>
              </div>

              <div class="p-3 bg-amber-50 border border-amber-200 rounded-xl text-xs text-amber-900">
                <strong>💡 शिक्षक तथा विद्यार्थीका लागि विशेष जानकारी:</strong> पाठ्यपुस्तक पृष्ठ ९१ को उत्तरकुञ्जिकामा (क) मा ६०% र (ख) मा ४०% छापिएको छ जुन मुद्रण दोष (Typo) हो। मन पराउने २००/५०० = ४०% नै शतप्रतिशत सही र गणितीय रूपमा प्रमाणित छ।
              </div>
            </div>

            <!-- Q6 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न ६: २ km सडकमध्ये ५०० m सडक कालोपत्रे गरिएको प्रतिशत</h4>
              <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl text-xs md:text-sm space-y-2">
                <p>• जम्मा सडकको लम्बाइ $= 2\\text{ km} = 2 \\times 1000\\text{ m} = 2000\\text{ m}$</p>
                <p>• कालोपत्रे गरिएको सडक $= 500\\text{ m}$</p>
                <div>
                  $$\\text{कालोपत्रे भएको प्रतिशत} = \\left( \\frac{500\\text{ m}}{2000\\text{ m}} \\times 100 \\right)\\% = \\frac{500}{20}\\% = 25\\%$$
                </div>
                <div class="font-bold text-emerald-700 text-sm">उत्तर: कालोपत्रे गरिएको सडक २५% रहेछ।</div>
              </div>
            </div>

            <!-- Q7 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न ७: ८०० विद्यार्थीको खेलकुद सप्ताह मेडल वितरण समस्या</h4>
              <p class="text-xs text-slate-600">कुल विद्यार्थी $= 800$। स्वर्ण $= 20\\%$, रजत $= 30\\%$, कांस्य $= 35\\%$, बाँकी पदक नपाउने:</p>
              
              <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs">
                <div class="p-3 bg-amber-50 border border-amber-200 rounded-xl text-center">
                  <span class="font-bold text-amber-800 block">(क) स्वर्ण पदक</span>
                  <div class="text-xs text-slate-600 mt-1">$800 \\times 20\\%$</div>
                  <div class="font-bold text-amber-900 text-sm mt-1">१६० जना</div>
                </div>

                <div class="p-3 bg-slate-100 border border-slate-300 rounded-xl text-center">
                  <span class="font-bold text-slate-700 block">(ख) रजत पदक</span>
                  <div class="text-xs text-slate-600 mt-1">$800 \\times 30\\%$</div>
                  <div class="font-bold text-slate-900 text-sm mt-1">२४० जना</div>
                </div>

                <div class="p-3 bg-orange-50 border border-orange-200 rounded-xl text-center">
                  <span class="font-bold text-orange-800 block">(ग) कांस्य पदक</span>
                  <div class="text-xs text-slate-600 mt-1">$800 \\times 35\\%$</div>
                  <div class="font-bold text-orange-900 text-sm mt-1">२८० जना</div>
                </div>

                <div class="p-3 bg-rose-50 border border-rose-200 rounded-xl text-center">
                  <span class="font-bold text-rose-800 block">(घ) पदक नपाउने</span>
                  <div class="text-xs text-slate-600 mt-1">$100\\% - 85\\% = 15\\%$</div>
                  <div class="font-bold text-rose-900 text-sm mt-1">१५% (१२० जना)</div>
                </div>
              </div>
            </div>

          </div>

          <!-- ---------------- SECTION: EXERCISE 6 PART 3 ---------------- -->
          <div id="ch6-sec-sec3" class="hidden space-y-6">
            <div class="bg-purple-50 border border-purple-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-purple-900 text-sm md:text-base">परियोजना कार्य तथा पाठ्यपुस्तकका उदाहरणहरू</h4>
                <p class="text-xs text-purple-700">पाठ्यपुस्तक पृष्ठ ८७–८९ का उदाहरण १ देखि ४ र पृष्ठ ९१ को परियोजना कार्य</p>
              </div>
              <span class="text-xs font-bold bg-white text-purple-800 px-3 py-1 rounded-xl shadow-xs border border-purple-200">प्रायोगिक अभ्यास</span>
            </div>

            <!-- Project Work Table -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">परियोजना कार्य: विद्यालयको कक्षागत विद्यार्थी प्रतिशत प्रतिवेदन</h4>
              <p class="text-xs text-slate-600">विद्यालयको कक्षागत छात्र, छात्रा सङ्ख्या टिपोट गरी प्रतिशत निकाल्ने नमुना प्रतिवेदन तालिका:</p>
              
              <div class="overflow-x-auto rounded-xl border border-slate-200">
                <table class="w-full text-xs text-center">
                  <thead class="bg-slate-100 font-bold text-slate-700">
                    <tr>
                      <th class="p-2 border-b">कक्षा</th>
                      <th class="p-2 border-b">छात्रा</th>
                      <th class="p-2 border-b">छात्र</th>
                      <th class="p-2 border-b">जम्मा ($N$)</th>
                      <th class="p-2 border-b text-blue-600">छात्रा %</th>
                      <th class="p-2 border-b text-indigo-600">छात्र %</th>
                      <th class="p-2 border-b">कुल %</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 text-slate-800">
                    <tr><td class="p-2 font-bold">कक्षा ६</td><td>२४</td><td>१६</td><td class="font-bold">४०</td><td class="text-blue-600 font-bold">६०%</td><td class="text-indigo-600 font-bold">४०%</td><td>१००%</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 font-bold">कक्षा ७</td><td>२७</td><td>१८</td><td class="font-bold">४५</td><td class="text-blue-600 font-bold">६०%</td><td class="text-indigo-600 font-bold">४०%</td><td>१००%</td></tr>
                    <tr><td class="p-2 font-bold">कक्षा ८</td><td>२५</td><td>२५</td><td class="font-bold">५०</td><td class="text-blue-600 font-bold">५०%</td><td class="text-indigo-600 font-bold">५०%</td><td>१००%</td></tr>
                    <tr class="bg-blue-50 font-bold"><td class="p-2">जम्मा</td><td>७६</td><td>५९</td><td>१३५</td><td class="text-blue-700">५६.३%</td><td class="text-indigo-700">४३.७%</td><td>१००%</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Textbook Examples 1-4 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <h4 class="font-bold text-slate-800 text-sm border-b pb-2">पाठ्यपुस्तकका प्रमुख उदाहरणहरूको समाधान सारांश</h4>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">उदा १: $\\frac{2}{5}$ लाई प्रतिशतमा लैजाने ३ तरिका:</div>
                  <div>१) हर १०० बनाएर: $\\frac{2 \\times 20}{5 \\times 20} = \\frac{40}{100} = 40\\%$</div>
                  <div>२) १००% ले गुणन: $\\frac{2}{5} \\times 100\\% = 40\\%$</div>
                  <div>३) ऐकिक नियम: ५ मा २, १०० मा ४० $\\implies 40\\%$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">उदा २: ८% लाई न्यूनतम भिन्नमा:</div>
                  <div>$8\\% = \\frac{8}{100} = \\frac{8 \\div 4}{100 \\div 4} = \\frac{2}{25}$</div>
                  <div class="font-bold text-emerald-600 mt-1">लघुतम पद $= \\frac{2}{25}$</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">उदा ३: रु. १२० को ७५%</div>
                  <div>$= 120 \\times \\frac{75}{100} = 120 \\times \\frac{3}{4} = 30 \\times 3$</div>
                  <div class="font-bold text-blue-600 mt-1">मान $=$ रु. ९०</div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="font-bold text-slate-800 mb-1">उदा ४: ५० मा ८ जना अनुपस्थित</div>
                  <div>अनुपस्थित $\% = \\frac{8}{50} \\times 100\\% = 16\\%$</div>
                  <div class="font-bold text-indigo-600 mt-1">उपस्थित $\% = 100\\% - 16\\% = 84\\%$</div>
                </div>
              </div>
            </div>

          </div>

        </div>

        <!-- ================= CH6 TAB 3: TIERS ================= -->
        <div id="ch6-view-tiers" class="hidden space-y-6">
          <div class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
            <div>
              <h4 class="font-black text-slate-800 text-sm md:text-base">३-तहका विशिष्ट परीक्षा-केन्द्रित नमुना प्रश्नहरू</h4>
              <p class="text-xs text-slate-600">आधारभूत बुझाइ (१ अङ्क), ज्ञानको प्रयोग तथा सीप (२ अङ्क), र उच्च दक्षता (४ अङ्क)</p>
            </div>
            <span class="text-xs font-bold bg-blue-600 text-white px-3 py-1 rounded-xl shadow-xs">CDC विशिष्टीकरण तालिका अनुसार</span>
          </div>

          <!-- Tier 1 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-blue-900 text-sm border-b pb-2 flex items-center gap-2">
              <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 text-xs">तह १</span>
              आधारभूत बुझाइ (Knowledge Level - १ अङ्कका प्रश्नहरू)
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <span class="font-bold text-slate-700 block mb-1">प्रश्न १.१: प्रतिशतको शाब्दिक अर्थ र सङ्केत:</span>
                <p class="text-slate-600">'प्रतिशत' को अर्थ "प्रति सय" वा "सयमा कति" हो। सङ्केत <strong>$\\%$</strong> हो।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <span class="font-bold text-slate-700 block mb-1">प्रश्न १.२: $\\frac{4}{25}$ लाई प्रतिशतमा:</span>
                <p class="text-slate-600">$\\frac{4}{25} \\times 100\\% = 4 \\times 4\\% = 16\\%$</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <span class="font-bold text-slate-700 block mb-1">प्रश्न १.३: ०.०८ लाई प्रतिशतमा:</span>
                <p class="text-slate-600">$0.08 \\times 100\\% = 8\\%$</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <span class="font-bold text-slate-700 block mb-1">प्रश्न १.४: ४५% लाई न्यूनतम भिन्नमा:</span>
                <p class="text-slate-600">$\\frac{45}{100} = \\frac{45 \\div 5}{100 \\div 5} = \\frac{9}{20}$</p>
              </div>
            </div>
          </div>

          <!-- Tier 2 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-emerald-900 text-sm border-b pb-2 flex items-center gap-2">
              <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-xs">तह २</span>
              ज्ञानको प्रयोग तथा सीप (Application Level - २ अङ्कका प्रश्नहरू)
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                <span class="font-bold text-slate-800 block">प्रश्न २.१: रु. २५०० को १२%</span>
                <div class="text-xs text-slate-600">$= 2500 \\times \\frac{12}{100} = 25 \\times 12$</div>
                <div class="font-bold text-emerald-700 text-xs">उत्तर: रु. ३००</div>
              </div>

              <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                <span class="font-bold text-slate-800 block">प्रश्न २.२: ६० सुन्तलामा १५ वटा कुहिएका</span>
                <div class="text-xs text-slate-600">कुहिएको $\% = \\frac{15}{60} \\times 100\\% = 25\\%$</div>
                <div class="font-bold text-emerald-700 text-xs">राम्रो $\% = 100\\% - 25\\% = 75\\%$</div>
              </div>

              <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                <span class="font-bold text-slate-800 block">प्रश्न २.३: ५० पूर्णाङ्कमा विमलको ३८ अङ्क</span>
                <div class="text-xs text-slate-600">प्राप्त $\% = \\frac{38}{50} \\times 100\\% = 38 \\times 2\\%$</div>
                <div class="font-bold text-emerald-700 text-xs">उत्तर: विमलले ७६% प्राप्त गरे।</div>
              </div>

              <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                <span class="font-bold text-slate-800 block">प्रश्न २.४: ५ लिटरमा १.२५ लिटर प्रयोग भए बाँकी</span>
                <div class="text-xs text-slate-600">बाँकी $= 5 - 1.25 = 3.75\\text{ l} \\implies \\frac{3.75}{5} \\times 100\\%$</div>
                <div class="font-bold text-emerald-700 text-xs">उत्तर: बाँकी दूध ७५% रह्यो।</div>
              </div>
            </div>
          </div>

          <!-- Tier 3 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <h4 class="font-bold text-purple-900 text-sm border-b pb-2 flex items-center gap-2">
              <span class="px-2 py-0.5 rounded bg-purple-100 text-purple-800 text-xs">तह ३</span>
              उच्च दक्षता तथा समस्या समाधान (Higher Ability - ४ अङ्कका बहुचरणीय प्रश्नहरू)
            </h4>
            
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 text-xs md:text-sm space-y-2">
              <h5 class="font-bold text-slate-800">प्रश्न ३.१: गाउँको जनसङ्ख्या ४००० (४८% महिला, ४२% पुरुष, बाँकी बालबालिका)</h5>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                <div class="bg-white p-2.5 rounded-lg border">
                  <strong>(क) बालबालिका %:</strong><br>$100\\% - (48\\% + 42\\%) = 10\\%$
                </div>
                <div class="bg-white p-2.5 rounded-lg border">
                  <strong>(ख) छुट्टाछुट्टै सङ्ख्या:</strong><br>महिला: $40 \\times 48 = 1,920$<br>पुरुष: $40 \\times 42 = 1,680$<br>बालबालिका: $400$
                </div>
                <div class="bg-white p-2.5 rounded-lg border">
                  <strong>(ग) २०० महिला थपिँदा नयाँ %:</strong><br>नयाँ महिला $= 2,120$<br>नयाँ जम्मा $= 4,200$<br>नयाँ $\% = \\frac{2120}{42}\\% \\approx 50.48\\%$
                </div>
              </div>
            </div>

            <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 text-xs md:text-sm space-y-2">
              <h5 class="font-bold text-slate-800">प्रश्न ३.२: पुस्तकालयमा १२०० पुस्तक (४०% नेपाली, ३५% अङ्ग्रेजी, बाँकी गणित/विज्ञान)</h5>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                <div class="bg-white p-2.5 rounded-lg border">
                  <strong>(क) गणित/विज्ञान %:</strong><br>$100\\% - 75\\% = 25\\%$
                </div>
                <div class="bg-white p-2.5 rounded-lg border">
                  <strong>(ख) पुस्तक सङ्ख्या:</strong><br>नेपाली: $480$, अङ्ग्रेजी: $420$<br>गणित/विज्ञान: $300$
                </div>
                <div class="bg-white p-2.5 rounded-lg border">
                  <strong>(ग) ३०० गणित पुस्तक थपिँदा:</strong><br>नयाँ गणित $= 600$, कुल $= 1,500$<br>नयाँ $\% = \\frac{600}{15}\\% = 40\\%$
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH6 TAB 4: QUIZ ================= -->
        <div id="ch6-view-quiz" class="hidden space-y-6">
          <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
            <div>
              <h4 class="font-black text-blue-900 text-sm md:text-base">पाठ ६: अन्तरक्रियात्मक आत्म-मूल्याङ्कन क्विज</h4>
              <p class="text-xs text-blue-700">४ वटा बहुवैकल्पिक प्रश्नहरू हल गरी आफ्नो बुझाइ परीक्षण गर्नुहोस्</p>
            </div>
            <button onclick="resetQuizCh6()" class="text-xs font-bold bg-white text-blue-800 px-3 py-1.5 rounded-xl border border-blue-200 hover:bg-blue-50 shadow-xs">
              🔄 पुनः सुरु गर्नुहोस्
            </button>
          </div>

          <!-- Quiz Questions 0 to 3 -->
          <!-- Q0 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न १: $\\frac{3}{5}$ लाई प्रतिशतमा रूपान्तरण गर्दा कुन मान आउँछ?</span>
              <span id="ch6-qbadge-0" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch6-qbtn-0-0" onclick="checkQuizCh6(0, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(A) $३०\\%$</button>
              <button id="ch6-qbtn-0-1" onclick="checkQuizCh6(0, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(B) $४०\\%$</button>
              <button id="ch6-qbtn-0-2" onclick="checkQuizCh6(0, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(C) $६०\\%$</button>
              <button id="ch6-qbtn-0-3" onclick="checkQuizCh6(0, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(D) $७५\\%$</button>
            </div>
            <div id="ch6-qexp-0" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q1 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न २: रु. ८०० को १५% कति हुन्छ?</span>
              <span id="ch6-qbadge-1" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch6-qbtn-1-0" onclick="checkQuizCh6(1, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(A) रु. १२०</button>
              <button id="ch6-qbtn-1-1" onclick="checkQuizCh6(1, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(B) रु. ८०</button>
              <button id="ch6-qbtn-1-2" onclick="checkQuizCh6(1, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(C) रु. १५०</button>
              <button id="ch6-qbtn-1-3" onclick="checkQuizCh6(1, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(D) रु. १००</button>
            </div>
            <div id="ch6-qexp-1" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q2 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ३: $०.०६$ लाई प्रतिशतमा बदल्दा कति हुन्छ?</span>
              <span id="ch6-qbadge-2" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch6-qbtn-2-0" onclick="checkQuizCh6(2, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(A) $०.६\\%$</button>
              <button id="ch6-qbtn-2-1" onclick="checkQuizCh6(2, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(B) $६\\%$</button>
              <button id="ch6-qbtn-2-2" onclick="checkQuizCh6(2, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(C) $६०\\%$</button>
              <button id="ch6-qbtn-2-3" onclick="checkQuizCh6(2, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(D) $००.६\\%$</button>
            </div>
            <div id="ch6-qexp-2" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q3 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ४: ५०० विद्यार्थीमध्ये २०० ले फुटबल मन पराए भने मन नपराउने विद्यार्थीको प्रतिशत कति हुन्छ?</span>
              <span id="ch6-qbadge-3" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch6-qbtn-3-0" onclick="checkQuizCh6(3, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(A) $४०\\%$</button>
              <button id="ch6-qbtn-3-1" onclick="checkQuizCh6(3, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(B) $६०\\%$</button>
              <button id="ch6-qbtn-3-2" onclick="checkQuizCh6(3, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(C) $५०\\%$</button>
              <button id="ch6-qbtn-3-3" onclick="checkQuizCh6(3, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium">(D) $२५\\%$</button>
            </div>
            <div id="ch6-qexp-3" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

        </div>

      </div>
      <!-- ================= END OF CHAPTER 6 VIEW ================= -->
"""

if __name__ == '__main__':
    html = get_ch6_html()
    print("Generated Chapter 6 HTML length:", len(html), "chars")
