# -*- coding: utf-8 -*-
"""
Generates the HTML content for Chapter 8 (ऐकिक नियम - Unitary Method) and Unit 2 Review.
Matches the design, CSS, and MathJax conventions of Chapters 1 to 7.
"""

def get_ch8_html():
    return """
      <!-- ================= CHAPTER 8: UNITARY METHOD (ऐकिक नियम) ================= -->
      <div id="chapter-view-8" class="hidden flex-1 flex flex-col">
        <!-- Top Chapter Banner -->
        <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-blue-600 mb-1">एकाइ २: अङ्कगणित (Unit 2: Arithmetic - अन्तिम पाठ तथा समीक्षा)</div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ ८: ऐकिक नियम (Unitary Method) तथा एकाइ २ समीक्षा</h2>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ ९८–१०५</span>
            <span class="text-xs bg-indigo-100 text-indigo-800 font-bold px-3 py-1 rounded-xl border border-indigo-200">अभ्यास ८ तथा एकाइ २ समीक्षा</span>
          </div>
        </div>

        <!-- Chapter 8 Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button id="ch8-tab-concepts" onclick="setTabCh8('concepts')" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
            १. अवधारणा, बिल र क्याल्कुलेटर
          </button>
          <button id="ch8-tab-exercises" onclick="setTabCh8('exercises')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            २. सम्पूर्ण अभ्यास समाधान (अभ्यास ८ र समीक्षा)
          </button>
          <button id="ch8-tab-tiers" onclick="setTabCh8('tiers')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
          </button>
          <button id="ch8-tab-quiz" onclick="setTabCh8('quiz')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ४. आत्म-मूल्याङ्कन क्विज
          </button>
        </div>

        <!-- ================= CH8 TAB 1: CONCEPTS ================= -->
        <div id="ch8-view-concepts" class="space-y-6">

          <!-- Core Concepts Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Card 1: Definition & Rules -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-blue-50 text-blue-700 border border-blue-200">मूल सिद्धान्त</span>
                <span class="text-xs font-mono text-slate-400">Unitary Concept</span>
              </div>
              <h3 class="text-lg font-bold text-slate-900">१. ऐकिक नियम (Unitary Method) को परिचय</h3>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                धेरै वस्तुहरूको मूल्य वा परिमाणबाट पहिले <strong>१ एकाइ (१ वटा)</strong> को मान निकाल्ने र त्यसपछि माग गरिएको सङ्ख्याको मान निकाल्ने गणितीय विधिलाई <strong>ऐकिक नियम</strong> भनिन्छ।
              </p>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-800 space-y-1.5 font-medium">
                <div class="text-blue-700 font-bold">• धेरैबाट १ एकाइ निकाल्दा $\\rightarrow$ भाग $(\\div)$ गर्ने:</div>
                <div class="pl-3 font-mono text-slate-600">एकाइ मूल्य = जम्मा मूल्य / वस्तुको सङ्ख्या</div>
                <div class="text-emerald-700 font-bold">• १ एकाइबाट धेरै निकाल्दा $\\rightarrow$ गुणन $(\\times)$ गर्ने:</div>
                <div class="pl-3 font-mono text-slate-600">जम्मा मूल्य = एकाइ मूल्य &times; माग गरिएको सङ्ख्या</div>
              </div>
            </div>

            <!-- Card 2: Invoicing & Bills -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-emerald-50 text-emerald-700 border border-emerald-200">व्यावहारिक ज्ञान</span>
                <span class="text-xs font-mono text-slate-400">Bills & Invoicing</span>
              </div>
              <h3 class="text-lg font-bold text-slate-900">२. बिल तथा इनभ्वाइस (Bills and Invoices)</h3>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                पसलबाट सामान खरिद गर्दा सामानको विवरण, परिमाण, दर र जम्मा रकम उल्लेख गरी दिइने आधिकारिक कागजातलाई <strong>बिल</strong> भनिन्छ।
              </p>
              <div class="p-3 bg-emerald-50/50 rounded-xl border border-emerald-200 text-xs text-emerald-900 space-y-1">
                <p>• <strong>दर (Rate):</strong> १ एकाइ (१ गोटा, १ केजी, वा १ लिटर) को मूल्य।</p>
                <p>• <strong>सामानको रकम:</strong> परिमाण (Quantity) $\\times$ दर (Rate)</p>
                <p>• <strong>कुल जम्मा:</strong> सबै सामानहरूको रकमको कुल जोड।</p>
                <p>• <strong>फिर्ता रकम:</strong> पसलेलाई दिएको नोट $-$ कुल जम्मा रकम।</p>
              </div>
            </div>

            <!-- Card 3: Unit Conversions -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-amber-50 text-amber-700 border border-amber-200">एकाइ समानता</span>
                <span class="text-xs font-mono text-slate-400">Units & Quantities</span>
              </div>
              <h3 class="text-lg font-bold text-slate-900">३. दैनिक जीवनका मुख्य एकाइ रूपान्तरणहरू</h3>
              <div class="grid grid-cols-2 gap-2 text-xs text-slate-700">
                <div class="bg-slate-50 p-2.5 rounded-lg border"><strong>१ दर्जन:</strong> १२ गोटा</div>
                <div class="bg-slate-50 p-2.5 rounded-lg border"><strong>१ स्कोर (Score):</strong> २० गोटा</div>
                <div class="bg-slate-50 p-2.5 rounded-lg border"><strong>१ वर्ष:</strong> १२ महिना / ३६५ दिन</div>
                <div class="bg-slate-50 p-2.5 rounded-lg border"><strong>१ किलोग्राम:</strong> १,००० ग्राम</div>
              </div>
              <p class="text-xs text-amber-900 bg-amber-50 p-2 rounded-lg border border-amber-200">
                <strong>सुनौलो नियम:</strong> प्रश्नमा दर्जन र गोटा मिसिएको भए पहिले सबैलाई गोटामा वा दर्जनमा रूपान्तरण गर्नुपर्छ।
              </p>
            </div>

            <!-- Card 4: Two Types of Variation -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-purple-50 text-purple-700 border border-purple-200">विचरण सिद्धान्त</span>
                <span class="text-xs font-mono text-slate-400">Variations</span>
              </div>
              <h3 class="text-lg font-bold text-slate-900">४. प्रत्यक्ष विचरण (Direct Variation)</h3>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                वस्तुको परिमाण बढ्दा कुल मूल्य पनि बढ्छ र परिमाण घट्दा कुल मूल्य पनि घट्छ। यस्तो सम्बन्धलाई <strong>प्रत्यक्ष विचरण</strong> भनिन्छ।
              </p>
              <div class="p-3 bg-purple-50/50 rounded-xl border border-purple-200 text-xs text-purple-900 space-y-1">
                <div>• धेरै सामान $\\rightarrow$ धेरै मूल्य (Direct)</div>
                <div>• थोरै सामान $\\rightarrow$ थोरै मूल्य (Direct)</div>
                <div class="text-[11px] text-slate-500 pt-1 border-t">*अप्रत्यक्ष विचरण (जस्तै कामदार र दिन) मा भने कामदार बढ्दा दिन घट्छ।</div>
              </div>
            </div>
          </div>

          <!-- ================= INTERACTIVE UNITARY CALCULATOR ================= -->
          <div class="bg-gradient-to-br from-slate-900 via-indigo-950 to-blue-950 p-6 md:p-8 rounded-3xl text-white shadow-xl space-y-6">
            <div class="flex flex-wrap items-center justify-between gap-3">
              <div>
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-blue-500/30 text-blue-200 border border-blue-400/30">अन्तरक्रियात्मक सिम्युलेटर</span>
                <h3 class="text-xl md:text-2xl font-black mt-1">ऐकिक नियम लाइभ क्याल्कुलेटर (Live Unitary Simulator)</h3>
                <p class="text-xs md:text-sm text-blue-200">कुनै पनि परिमाणको मूल्य प्रविष्ट गरी १ एकाइ र नयाँ परिमाणको मूल्य तुरुन्त निकाल्नुहोस्</p>
              </div>
              <!-- Presets -->
              <div class="flex flex-wrap gap-2 text-xs">
                <button onclick="setCh8Preset(3, 270, 5)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">३ कापी रु. २७० $\\rightarrow$ ५ कापी</button>
                <button onclick="setCh8Preset(1, 1275, 4)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">१ फुटबल रु. १२७५ $\\rightarrow$ ४ फुटबल</button>
                <button onclick="setCh8Preset(25, 2250, 60)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">२५ केजी रु. २२५० $\\rightarrow$ ६० केजी</button>
                <button onclick="setCh8Preset(10, 1100, 5)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">१० लि. पेट्रोल $\\rightarrow$ ५ लिटर</button>
              </div>
            </div>

            <!-- Calculator Inputs Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Q1 Input -->
              <div class="bg-white/10 p-4 rounded-2xl border border-white/15 space-y-1">
                <label class="text-xs text-blue-200 font-semibold block">दिइएको वस्तुको सङ्ख्या / परिमाण ($Q_1$)</label>
                <input id="ch8-in-q1" type="number" value="8" min="1" step="any" oninput="runCh8Calc()" class="w-full bg-white/20 border border-white/30 rounded-xl px-3 py-2 text-white font-mono text-lg font-bold focus:outline-none focus:ring-2 focus:ring-blue-400">
                <span class="text-[11px] text-blue-300 block">जस्तै: ८ ओटा कापी</span>
              </div>

              <!-- C1 Input -->
              <div class="bg-white/10 p-4 rounded-2xl border border-white/15 space-y-1">
                <label class="text-xs text-blue-200 font-semibold block">दिइएको परिमाणको जम्मा मूल्य ($C_1$ in रु.)</label>
                <input id="ch8-in-c1" type="number" value="480" min="0" step="any" oninput="runCh8Calc()" class="w-full bg-white/20 border border-white/30 rounded-xl px-3 py-2 text-white font-mono text-lg font-bold focus:outline-none focus:ring-2 focus:ring-blue-400">
                <span class="text-[11px] text-blue-300 block">जस्तै: जम्मा रु. ४८०</span>
              </div>

              <!-- Q2 Input -->
              <div class="bg-white/10 p-4 rounded-2xl border border-white/15 space-y-1">
                <label class="text-xs text-blue-200 font-semibold block">मूल्य निकाल्नुपर्ने नयाँ परिमाण ($Q_2$)</label>
                <input id="ch8-in-q2" type="number" value="12" min="1" step="any" oninput="runCh8Calc()" class="w-full bg-white/20 border border-white/30 rounded-xl px-3 py-2 text-white font-mono text-lg font-bold focus:outline-none focus:ring-2 focus:ring-blue-400">
                <span class="text-[11px] text-blue-300 block">जस्तै: १२ ओटा कापी</span>
              </div>
            </div>

            <!-- Dynamic Result Card -->
            <div id="ch8-calc-res" class="p-5 rounded-2xl bg-white/10 border border-white/20 backdrop-blur-sm space-y-3">
              <!-- Populated dynamically by runCh8Calc() -->
            </div>
          </div>

          <!-- Textbook Invoicing Sample -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center justify-between border-b pb-2">
              <div>
                <h4 class="font-bold text-slate-900 text-sm md:text-base">पाठ्यपुस्तक नमुना बिल (Textbook Bill Observation - पृष्ठ ९९)</h4>
                <p class="text-xs text-slate-500">हाम्रो किराना पसल, बल्खु, काठमाडौँ (बिल नं: ०२५)</p>
              </div>
              <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-lg">नमुना इनभ्वाइस</span>
            </div>

            <div class="overflow-x-auto text-xs md:text-sm">
              <table class="w-full text-center border-collapse">
                <thead>
                  <tr class="bg-slate-100 text-slate-800">
                    <th class="p-2 border">क्र.सं.</th>
                    <th class="p-2 border text-left">सामानको विवरण</th>
                    <th class="p-2 border">परिमाण</th>
                    <th class="p-2 border">दर (रु.)</th>
                    <th class="p-2 border text-emerald-700">जम्मा रकम (रु.)</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-slate-700">
                  <tr>
                    <td class="p-2 border">१</td>
                    <td class="p-2 border text-left font-medium">चिनी</td>
                    <td class="p-2 border">३ केजी</td>
                    <td class="p-2 border">रु. ८०</td>
                    <td class="p-2 border font-mono font-bold text-emerald-700">रु. २४०.००</td>
                  </tr>
                  <tr class="bg-slate-50">
                    <td class="p-2 border">२</td>
                    <td class="p-2 border text-left font-medium">आँटा</td>
                    <td class="p-2 border">५ केजी</td>
                    <td class="p-2 border">रु. ४५</td>
                    <td class="p-2 border font-mono font-bold text-emerald-700">रु. २२५.००</td>
                  </tr>
                  <tr>
                    <td class="p-2 border">३</td>
                    <td class="p-2 border text-left font-medium">चियापत्ति</td>
                    <td class="p-2 border">२ प्याकेट</td>
                    <td class="p-2 border">रु. १००</td>
                    <td class="p-2 border font-mono font-bold text-emerald-700">रु. २००.००</td>
                  </tr>
                  <tr class="bg-slate-50">
                    <td class="p-2 border">४</td>
                    <td class="p-2 border text-left font-medium">तेल</td>
                    <td class="p-2 border">२ लिटर</td>
                    <td class="p-2 border">रु. २५०</td>
                    <td class="p-2 border font-mono font-bold text-emerald-700">रु. ५००.००</td>
                  </tr>
                  <tr class="bg-emerald-50 font-bold text-emerald-950">
                    <td colspan="4" class="p-2 border text-right pr-4">कुल जम्मा रकम (Grand Total):</td>
                    <td class="p-2 border font-mono text-base text-emerald-800">रु. १,१६५.००</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p class="text-xs text-slate-600 bg-slate-50 p-2.5 rounded-lg border">
              <strong>अक्षरेपी:</strong> एक हजार एक सय पैंसट्ठी रुपैयाँ मात्र। ग्राहकले रु. १५०० बुझाउँदा फिर्ता पाउने रकम $= 1500 - 1165 = \\text{रु. } 335$ हुन्छ।
            </p>
          </div>

        </div>

        <!-- ================= CH8 TAB 2: EXERCISES ================= -->
        <div id="ch8-view-exercises" class="hidden space-y-6">
          
          <!-- Exercise Navigation Pills -->
          <div class="flex gap-2 overflow-x-auto pb-2 border-b border-slate-200 text-xs md:text-sm font-bold">
            <button id="ch8-pill-sec1" onclick="setExerciseCh8('sec1')" class="px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap cursor-pointer">
              भाग १: अभ्यास ८ (प्रश्न १ देखि ८)
            </button>
            <button id="ch8-pill-sec2" onclick="setExerciseCh8('sec2')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer">
              भाग २: अभ्यास ८ (प्रश्न ९ देखि १५ र परियोजना)
            </button>
            <button id="ch8-pill-sec3" onclick="setExerciseCh8('sec3')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer">
              भाग ३: एकाइ २ अङ्कगणित मिश्रित अभ्यास (प्रश्न १ देखि ११)
            </button>
          </div>

          <!-- ---------------- SECTION 1: EXERCISE 8 (QUESTIONS 1 TO 8) ---------------- -->
          <div id="ch8-sec-sec1" class="space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">अभ्यास ८: प्रश्न १ देखि ८ को १००% विस्तृत समाधान</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ १०१–१०२ (ठीक/बेठीक, एकाइ मूल्य, जम्मा मूल्य र आधारभूत समस्याहरू)</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">८ मुख्य प्रश्नहरू</span>
            </div>

            <!-- Q1 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm md:text-base border-b pb-2">
                प्रश्न १: तलका तथ्यहरू ठीक भए (√) र बेठीक भए (×) चिह्न लगाउनुहोस्:
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex justify-between items-center">
                  <span>(क) उस्तै धेरै वस्तुको मूल्य पत्ता लगाउन एकाइ वस्तुको मूल्यलाई वस्तुको सङ्ख्याले भाग गर्नुपर्छ।</span>
                  <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-bold text-xs">× बेठीक (गुणन गर्नुपर्छ)</span>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex justify-between items-center">
                  <span>(ख) एकाइ वस्तुको मूल्य पत्ता लगाउन वस्तुको कुल मूल्यलाई वस्तुहरूको सङ्ख्याले भाग गर्नुपर्छ।</span>
                  <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold text-xs">√ ठीक</span>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex justify-between items-center">
                  <span>(ग) ५ ओटा ज्यामिति बाकसको मूल्य रु. ६०० भए १ ओटाको मूल्य रु. १२० हुन्छ।</span>
                  <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold text-xs">√ ठीक (६००÷५=१२०)</span>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex justify-between items-center">
                  <span>(घ) एकओटा सिसाकलमको मूल्य रु. १० भए १ दर्जनको मूल्य रु. १०० हुन्छ।</span>
                  <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-bold text-xs">× बेठीक (१२×१०=१२०)</span>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex justify-between items-center md:col-span-2">
                  <span>(ङ) जम्मा मूल्य = वस्तुको एकाइ मूल्य &times; वस्तुको सङ्ख्या हुन्छ।</span>
                  <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold text-xs">√ ठीक</span>
                </div>
              </div>
            </div>

            <!-- Q2 & Q3 Tables -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q2 Table -->
              <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न २: जम्मा मूल्य निकाल्नुहोस्:</h4>
                <div class="space-y-2 text-xs md:text-sm">
                  <div class="p-2.5 bg-slate-50 rounded-lg flex justify-between items-center">
                    <span>(क) सङ्ख्या २३, एकाइ मूल्य रु. ७५:</span>
                    <span class="font-bold text-blue-700">$23 \\times 75 = \\text{रु. } 1,725$</span>
                  </div>
                  <div class="p-2.5 bg-slate-50 rounded-lg flex justify-between items-center">
                    <span>(ख) सङ्ख्या २, एकाइ मूल्य रु. ९५०:</span>
                    <span class="font-bold text-blue-700">$2 \\times 950 = \\text{रु. } 1,900$</span>
                  </div>
                  <div class="p-2.5 bg-slate-50 rounded-lg flex justify-between items-center">
                    <span>(ग) सङ्ख्या ५५, एकाइ मूल्य रु. ४५:</span>
                    <span class="font-bold text-blue-700">$55 \\times 45 = \\text{रु. } 2,475$</span>
                  </div>
                </div>
              </div>

              <!-- Q3 Table -->
              <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <h4 class="font-bold text-slate-800 text-sm border-b pb-2">प्रश्न ३: एकाइ मूल्य निकाल्नुहोस्:</h4>
                <div class="space-y-2 text-xs md:text-sm">
                  <div class="p-2.5 bg-slate-50 rounded-lg flex justify-between items-center">
                    <span>(क) सङ्ख्या ३२५, जम्मा मूल्य रु. २,९२५:</span>
                    <span class="font-bold text-emerald-700">$\\frac{2925}{325} = \\text{रु. } 9$</span>
                  </div>
                  <div class="p-2.5 bg-slate-50 rounded-lg flex justify-between items-center">
                    <span>(ख) सङ्ख्या २५, जम्मा मूल्य रु. ६००:</span>
                    <span class="font-bold text-emerald-700">$\\frac{600}{25} = \\text{रु. } 24$</span>
                  </div>
                  <div class="p-2.5 bg-slate-50 rounded-lg flex justify-between items-center">
                    <span>(ग) सङ्ख्या २५, जम्मा रु. ६०० जस्तै:</span>
                    <span class="font-bold text-emerald-700">$\\text{एकाइ मूल्य } = \\text{रु. } 24$</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Q4, Q5, Q6, Q7, Q8 Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q4 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ४</span>
                <p class="text-slate-700">एउटा फुटबलको मूल्य रु. १,२७५ पर्छ भने ४ ओटा फुटबलको मूल्य कति पर्ला?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs text-slate-800">
                  <div>१ ओटाको मूल्य $= \\text{रु. } 1,275$</div>
                  <div class="font-bold text-emerald-700">४ ओटाको मूल्य $= 1275 \\times 4 = \\text{रु. } 5,100$</div>
                </div>
              </div>

              <!-- Q5 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ५</span>
                <p class="text-slate-700">कर्मचारीको १ महिनाको तलब रु. ३५,००० छ भने १ वर्ष (१२ महिना) को तलब कति?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs text-slate-800">
                  <div>१ वर्ष $= 12$ महिना</div>
                  <div class="font-bold text-emerald-700">१ वर्षको तलब $= 35000 \\times 12 = \\text{रु. } 4,20,000$</div>
                </div>
              </div>

              <!-- Q6 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ६</span>
                <p class="text-slate-700">सविनाले एउटाको रु. ४५ का दरले १ दर्जन (१२ ओटा) कापी किन्दा कति तिर्नुपर्छ?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs text-slate-800">
                  <div>१ दर्जन $= 12$ ओटा</div>
                  <div class="font-bold text-emerald-700">जम्मा मूल्य $= 12 \\times 45 = \\text{रु. } 540$</div>
                </div>
              </div>

              <!-- Q7 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ७</span>
                <p class="text-slate-700">१०० ओटा चकलेटको १ प्याकेटको मूल्य रु. ५०० पर्छ भने १ ओटाको मूल्य कति?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs text-slate-800">
                  <div class="font-bold text-emerald-700">१ ओटा चकलेटको मूल्य $= \\frac{500}{100} = \\text{रु. } 5$</div>
                </div>
              </div>

              <!-- Q8 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm md:col-span-2">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ८</span>
                <p class="text-slate-700">५ दर्जन केरा किन्दा रामले रु. ६०० तिरेछन् भने १ दर्जन मात्र किनेको भए कति तिर्नुपर्थ्यो?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs text-slate-800">
                  <div class="font-bold text-emerald-700">१ दर्जन केराको मूल्य $= \\frac{600}{5} = \\text{रु. } 120$</div>
                </div>
              </div>
            </div>

          </div>

          <!-- ---------------- SECTION 2: EXERCISE 8 (QUESTIONS 9 TO 15 & PROJECT) ---------------- -->
          <div id="ch8-sec-sec2" class="hidden space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">अभ्यास ८: प्रश्न ९ देखि १५ र परियोजना कार्य समाधान</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ १०२–१०३ (२-चरणीय ऐकिक नियम, तालिका भर्ने र व्यावहारिक समस्याहरू)</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">७ प्रश्न + परियोजना</span>
            </div>

            <!-- Q9 & Q10 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q9 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ९</span>
                <p class="text-slate-700">मिनाले ६० ओटा नोटबुक रु. ६,००० मा किनिन्। १ दर्जन (१२ ओटा) मात्र किनेको भए कति तिर्नुपर्थ्यो?</p>
                <div class="p-3 bg-slate-50 rounded-xl space-y-1 font-mono text-xs text-slate-800">
                  <div>१ ओटाको मूल्य $= \\frac{6000}{60} = \\text{रु. } 100$</div>
                  <div class="font-bold text-emerald-700">१२ ओटाको मूल्य $= 100 \\times 12 = \\text{रु. } 1,200$</div>
                </div>
              </div>

              <!-- Q10 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न १०</span>
                <p class="text-slate-700">पार्कमा १०० जनाको टिकटको जम्मा मूल्य रु. ३,६०० पर्छ भने १ जनाको टिकटको मूल्य कति?</p>
                <div class="p-3 bg-slate-50 rounded-xl space-y-1 font-mono text-xs text-slate-800">
                  <div class="font-bold text-emerald-700">१ जनाको मूल्य $= \\frac{3600}{100} = \\text{रु. } 36$</div>
                </div>
              </div>
            </div>

            <!-- Q11 Table -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <h4 class="font-bold text-slate-800 text-sm md:text-base border-b pb-2">
                प्रश्न ११: दिइएको मूल्यका आधारमा तालिका पूरा गर्नुहोस्:
              </h4>
              <div class="overflow-x-auto">
                <table class="w-full text-xs md:text-sm border-collapse text-center">
                  <thead>
                    <tr class="bg-slate-100 text-slate-800">
                      <th class="p-2.5 border">क्र.सं.</th>
                      <th class="p-2.5 border">२ ओटाको मूल्य</th>
                      <th class="p-2.5 border text-blue-700">एकाइ मूल्य (१ ओटाको)</th>
                      <th class="p-2.5 border">५ ओटाको मूल्य</th>
                      <th class="p-2.5 border text-emerald-700">८ ओटाको मूल्य</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-200 text-slate-800">
                    <tr>
                      <td class="p-2 border font-bold">(क)</td>
                      <td class="p-2 border font-bold text-slate-900">रु. १६</td>
                      <td class="p-2 border font-bold text-blue-600">रु. ८ (१६÷२)</td>
                      <td class="p-2 border">रु. ४० (८&times;५)</td>
                      <td class="p-2 border font-bold text-emerald-700">रु. ६४ (८&times;८)</td>
                    </tr>
                    <tr class="bg-slate-50">
                      <td class="p-2 border font-bold">(ख)</td>
                      <td class="p-2 border">रु. ३०० (१५०&times;२)</td>
                      <td class="p-2 border font-bold text-blue-600">रु. १५०</td>
                      <td class="p-2 border">रु. ७५० (१५०&times;५)</td>
                      <td class="p-2 border font-bold text-emerald-700">रु. १,२०० (१५०&times;८)</td>
                    </tr>
                    <tr>
                      <td class="p-2 border font-bold">(ग)</td>
                      <td class="p-2 border">रु. ४०० (२००&times;२)</td>
                      <td class="p-2 border font-bold text-blue-600">रु. २०० (१०००÷५)</td>
                      <td class="p-2 border font-bold text-slate-900">रु. १,०००</td>
                      <td class="p-2 border font-bold text-emerald-700">रु. १,६०० (२००&times;८)</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Q12, Q13, Q14, Q15 Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q12 -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs md:text-sm">
                <span class="font-bold text-blue-700">प्रश्न १२: ६ ओटा क्रिकेट ब्याटको मूल्य रु. ९०० भए ४ ओटाको मूल्य कति?</span>
                <p>• १ ओटाको मूल्य $= \\frac{900}{6} = \\text{रु. } 150$</p>
                <p class="font-bold text-emerald-800">• ४ ओटाको मूल्य $= 150 \\times 4 = \\text{रु. } 600$</p>
              </div>

              <!-- Q13 -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs md:text-sm">
                <span class="font-bold text-blue-700">प्रश्न १३: ३ ओटा झोलाको मूल्य रु. १,७२५ भए ५ ओटाको मूल्य कति?</span>
                <p>• १ ओटाको मूल्य $= \\frac{1725}{3} = \\text{रु. } 575$</p>
                <p class="font-bold text-emerald-800">• ५ ओटाको मूल्य $= 575 \\times 5 = \\text{रु. } 2,875$</p>
              </div>

              <!-- Q14 -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs md:text-sm">
                <span class="font-bold text-blue-700">प्रश्न १४: २५ केजी चामलको मूल्य रु. २,२५० भए ६० केजी चामलको मूल्य कति?</span>
                <p>• १ केजीको मूल्य $= \\frac{2250}{25} = \\text{रु. } 90$</p>
                <p class="font-bold text-emerald-800">• ६० केजीको मूल्य $= 90 \\times 60 = \\text{रु. } 5,400$</p>
              </div>

              <!-- Q15 -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-1 text-xs md:text-sm">
                <span class="font-bold text-blue-700">प्रश्न १५: १० लिटर पेट्रोलको मूल्य रु. १,१०० भए ५ लिटर पेट्रोलको कति?</span>
                <p>• १ लिटरको मूल्य $= \\frac{1100}{10} = \\text{रु. } 110$</p>
                <p class="font-bold text-emerald-800">• ५ लिटरको मूल्य $= 110 \\times 5 = \\text{रु. } 550$</p>
              </div>
            </div>

            <!-- Project Work Template Card -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <div class="border-b pb-2 flex items-center justify-between">
                <div>
                  <h4 class="font-bold text-slate-900 text-sm md:text-base">परियोजना कार्य: ६ ओटा वस्तुहरूको एकाइ मूल्य र १०/१० ओटाको मूल्य सर्वेक्षण</h4>
                  <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ १०३ को निर्देशन अनुरूप तयार गरिएको प्रतिवेदन</p>
                </div>
                <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-lg">परियोजना प्रतिवेदन</span>
              </div>

              <div class="overflow-x-auto text-xs md:text-sm">
                <table class="w-full text-center border-collapse">
                  <thead>
                    <tr class="bg-slate-100 text-slate-800">
                      <th class="p-2 border text-left">वस्तुको नाम</th>
                      <th class="p-2 border">एकाइ</th>
                      <th class="p-2 border">एकाइ मूल्य (दर)</th>
                      <th class="p-2 border text-blue-700">१० ओटाको मूल्य</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-200 text-slate-700">
                    <tr><td class="p-2 border text-left">१. कापी</td><td class="p-2 border">१ गोटा</td><td class="p-2 border">रु. ५५</td><td class="p-2 border font-bold text-blue-700">रु. ५५०</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 border text-left">२. डटपेन</td><td class="p-2 border">१ गोटा</td><td class="p-2 border">रु. १५</td><td class="p-2 border font-bold text-blue-700">रु. १५०</td></tr>
                    <tr><td class="p-2 border text-left">३. साबुन</td><td class="p-2 border">१ गोटा</td><td class="p-2 border">रु. ४५</td><td class="p-2 border font-bold text-blue-700">रु. ४५०</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 border text-left">४. चिनी</td><td class="p-2 border">१ केजी</td><td class="p-2 border">रु. ९५</td><td class="p-2 border font-bold text-blue-700">रु. ९५०</td></tr>
                    <tr><td class="p-2 border text-left">५. नुन</td><td class="p-2 border">१ पोका</td><td class="p-2 border">रु. २६</td><td class="p-2 border font-bold text-blue-700">रु. २६०</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 border text-left">६. चाउचाउ</td><td class="p-2 border">१ प्याकेट</td><td class="p-2 border">रु. २५</td><td class="p-2 border font-bold text-blue-700">रु. २५०</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

          </div>

          <!-- ---------------- SECTION 3: UNIT 2 COMPREHENSIVE REVIEW ---------------- -->
          <div id="ch8-sec-sec3" class="hidden space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">एकाइ २: अङ्कगणित मिश्रित अभ्यास (Comprehensive Review)</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ १०३–१०५ (प्रश्न १ देखि ११ को १००% पूर्ण समाधान)</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">११ विस्तृत प्रश्नहरू</span>
            </div>

            <!-- Review Questions Grid -->
            <div class="space-y-4 text-xs md:text-sm">
              <!-- Q1 -->
              <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                <span class="font-bold text-indigo-700">प्रश्न १: खरायोको उफ्राइ र साझा अपवर्त्य (L.C.M.):</span>
                <p class="text-slate-600">पहिलो खरायो २/२ फिट र दोस्रो खरायो ३/३ फिटको दूरीमा उफ्रन्छ:</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                  <div class="bg-slate-50 p-2.5 rounded-lg"><strong>(क, ख) पार गरेको दूरी:</strong><br>१st: २, ४, ६, ८, १०, १२, ...<br>२nd: ३, ६, ९, १२, १५, ...</div>
                  <div class="bg-slate-50 p-2.5 rounded-lg"><strong>(ग, घ) साझा स्थान र ल.स.:</strong><br>साझा: ६, १२, १८ फिट।<br>प्रथम भेट: <strong>६ फिट (L.C.M. वा ल.स.)</strong></div>
                </div>
              </div>

              <!-- Q2 & Q3 -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न २: ६ ओटा चकलेट बराबर बाँडफाँड:</span>
                  <p class="text-slate-600">१, २, ३, वा ६ जनालाई बाँड्न सकिन्छ।</p>
                  <p class="font-bold text-emerald-800">निष्कर्ष: यी सङ्ख्याहरू ६ का गुणनखण्डहरू (Factors) हुन्।</p>
                </div>

                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ३: ३० र १०५ को रूढ गुणनखण्ड:</span>
                  <p>$30 = 2 \\times 3 \\times 5$, $105 = 3 \\times 5 \\times 7$</p>
                  <p>साझा: $3, 5$ | बाँकी: $2, 7$</p>
                  <p class="font-bold text-emerald-800">ल.स. $= 15 \\times 14 = 210$</p>
                </div>
              </div>

              <!-- Q4 & Q5 -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ४: सडक कालोपत्रे (भिन्न):</span>
                  <p>१st: $36 \\times \\frac{3}{4} = 27 \\text{ किमी}$ | २nd: $60 \\times \\frac{2}{3} = 40 \\text{ किमी}$</p>
                  <p class="font-bold text-emerald-800">जम्मा $= 67 \\text{ किमी}$, दोस्रो सडक १३ किमी बढी।</p>
                </div>

                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ५: सुमनको आम्दानी (रु. ३२,५००):</span>
                  <p>घरखर्च $= 32500 \\times \\frac{1}{2} = \\text{रु. } 16,250$</p>
                  <p class="font-bold text-emerald-800">कपडा $= 32500 \\times \\frac{1}{4} = \\text{रु. } 8,125$ (२५%)</p>
                </div>
              </div>

              <!-- Q6 & Q7 -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ६: रमिलाको परीक्षा प्राप्ताङ्क:</span>
                  <p>अंग्रेजी: $\\frac{20}{25} = 80\\%$ | विज्ञान: $\\frac{30}{40} = 75\\%$</p>
                  <p class="font-bold text-emerald-800">अंग्रेजी विषयमा ५% राम्रो अङ्क छ।</p>
                </div>

                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ७: रमणको कलम खरिद (६ ओटा रु. ४५०):</span>
                  <p>१ ओटाको मूल्य $= \\text{रु. } 75$ | रु. ६७५ मा $= 9$ ओटा</p>
                  <p class="font-bold text-emerald-800">रु. १५० नाफामा बिक्री मूल्य $= \\text{रु. } 600$</p>
                </div>
              </div>

              <!-- Q8 & Q9 -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ८: पूर्णमानको अण्डा व्यापार (४०० अण्डा):</span>
                  <p>कुल $C.P. = 4000 + 300 = \\text{रु. } 4,300$</p>
                  <p>३५० अण्डा रु. १३ मा बेच्दा: नाफा $= \\text{रु. } 250$</p>
                  <p class="font-bold text-emerald-800">रु. ६०० नाफा गर्न दर $= \\frac{4900}{350} = \\text{रु. } 14$ प्रतिगोटा</p>
                </div>

                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ९: हरिबहादुरको घडी व्यापार (२ ओटा रु. ६५००):</span>
                  <p>१ ओटाको $C.P. = \\text{रु. } 3,250$</p>
                  <p>१st घडी रु. ३५०० मा बेच्दा नाफा $= \\text{रु. } 250$</p>
                  <p class="font-bold text-emerald-800">कुल रु. ६०० नाफा गर्न २nd घडीको $S.P. = \\text{रु. } 3,600$</p>
                </div>
              </div>

              <!-- Q10 & Q11 -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न १०: दूध क्यान क्षमता (१७० लिटर):</span>
                  <p>क्यान क्षमता $= 8.5 \\text{ लिटर}$</p>
                  <p class="font-bold text-emerald-800">क्यान सङ्ख्या $= \\frac{170}{8.5} = \\mathbf{20 \\text{ ओटा क्यान}}$</p>
                </div>

                <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2">
                  <span class="font-bold text-indigo-700">प्रश्न ११: डोरी विभाजन (३४.४८ मिटर):</span>
                  <p>८ टुक्रा गर्दा १ टुक्रा $= \\frac{34.48}{8} = 4.31 \\text{ मिटर}$</p>
                  <p class="font-bold text-emerald-800">३ टुक्राको जम्मा लम्बाइ $= 4.31 \\times 3 = \\mathbf{12.93 \\text{ मिटर}}$</p>
                </div>
              </div>
            </div>

          </div>

        </div>

        <!-- ================= CH8 TAB 3: TIERS (EXPANDED TO 16 QUESTIONS) ================= -->
        <div id="ch8-view-tiers" class="hidden space-y-6">
          <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
            <div>
              <h4 class="font-black text-blue-900 text-sm md:text-base">तीन तहका नमुना परीक्षा प्रश्नहरू (३-Tier Cognitive Questions)</h4>
              <p class="text-xs text-blue-700">ज्ञान, प्रयोग र उच्च दक्षताका १६ वटा परीक्षा-केन्द्रित प्रश्नहरू पूर्ण हल सहित</p>
            </div>
            <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">१६ प्रश्नहरू पूर्ण हल सहित</span>
          </div>

          <!-- Tier 1 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center justify-between border-b pb-2">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-500 inline-block"></span>
                <h4 class="font-bold text-slate-800 text-sm md:text-base">तह १: ज्ञान तथा बोध (६ प्रश्नहरू)</h4>
              </div>
              <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800">१-२ अङ्कका प्रश्नहरू</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.१ ऐकिक नियमको परिभाषा:</span>
                <p class="text-slate-600">पहिले १ एकाइको मान निकाली माग गरिएको परिमाणको मान निकाल्ने विधि।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.२ धेरैबाट एउटा निकाल्दा:</span>
                <p class="text-slate-600">जम्मा मूल्यलाई सङ्ख्याले भाग $(\\div)$ गरिन्छ।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.३ एउटाबाट धेरै निकाल्दा:</span>
                <p class="text-slate-600">एकाइ मूल्यलाई माग गरिएको सङ्ख्याले गुणन $(\\times)$ गरिन्छ।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.४ १ दर्जन अण्डा रु. २४०:</span>
                <p class="text-slate-600">१ ओटाको मूल्य $= \\frac{240}{12} = \\text{रु. } 20$।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.५ १ केजी स्याउ रु. २००:</span>
                <p class="text-slate-600">५ केजीको मूल्य $= 200 \\times 5 = \\text{रु. } 1,000$।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.६ बिलमा दरको अर्थ:</span>
                <p class="text-slate-600">सामानको प्रति एकाइ (१ गोटा/केजी/लिटर) को मूल्य।</p>
              </div>
            </div>
          </div>

          <!-- Tier 2 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center justify-between border-b pb-2">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-blue-500 inline-block"></span>
                <h4 class="font-bold text-slate-800 text-sm md:text-base">तह २: प्रयोग तथा समस्या समाधान (६ प्रश्नहरू)</h4>
              </div>
              <span class="text-xs font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800">२-३ अङ्कका प्रश्नहरू</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.१ ८ कापीको रु. ४८० भए १२ कापीको:</span>
                <p class="text-slate-600">१ को $60$, १२ को $= 60 \\times 12 = \\mathbf{\\text{रु. } 720}$।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.२ कारको गति (४ घण्टामा २४० किमी):</span>
                <p class="text-slate-600">१ घण्टामा ६० किमी, ६ घण्टामा $= 60 \\times 6 = \\mathbf{360 \\text{ किमी}}$।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.३ १५ केजी आलु रु. ६००:</span>
                <p class="text-slate-600">१ केजीको रु. ४०, रु. १००० मा $= \\frac{1000}{40} = \\mathbf{25 \\text{ केजी}}$।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.४ १ दर्जन सिसाकलम रु. १८०:</span>
                <p class="text-slate-600">१ को रु. १५, १५ ओटाको $= 15 \\times 15 = \\mathbf{\\text{रु. } 225}$।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.५ ६ दिनको ज्याला रु. ४,८००:</span>
                <p class="text-slate-600">१ दिनको रु. ८००, १८ दिनको $= 800 \\times 18 = \\mathbf{\\text{रु. } 14,400}$।</p>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.६ ट्याङ्की १० मिनेटमा २०० लिटर:</span>
                <p class="text-slate-600">१ मिनेटमा २० लि., २५ मिनेटमा $= 20 \\times 25 = \\mathbf{500 \\text{ लिटर}}$।</p>
              </div>
            </div>
          </div>

          <!-- Tier 3 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center justify-between border-b pb-2">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-purple-500 inline-block"></span>
                <h4 class="font-bold text-slate-800 text-sm md:text-base">तह ३: उच्च दक्षता तथा बहु-चरणीय समस्याहरू (४ प्रश्नहरू)</h4>
              </div>
              <span class="text-xs font-bold px-2 py-0.5 rounded bg-purple-100 text-purple-800">४ अङ्कका बहुचरणीय प्रश्नहरू</span>
            </div>

            <div class="space-y-3 text-xs md:text-sm">
              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-1">
                <h5 class="font-bold text-purple-950">३.१ बिल निर्माण तथा फिर्ता रकम:</h5>
                <p class="text-slate-700">६ कापी (दर रु. ६५ = रु. ३९०), ४ डटपेन (दर रु. २५ = रु. १००), १ ज्यामिति बाकस (रु. १५०)। कुल जम्मा $= \\text{रु. } 640$। रु. १००० दिँदा फिर्ता पाउने रकम $= 1000 - 640 = \\mathbf{\\text{रु. } 360}$।</p>
              </div>

              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-1">
                <h5 class="font-bold text-purple-950">३.२ दुई पसलको मूल्य तुलना र निर्णय:</h5>
                <p class="text-slate-700">पसल 'क' मा रु. १६०/केजी, 'ख' मा रु. १५०/केजी। पसल 'ख' रु. १० सस्तो छ। १० केजी किन्दा बचत $= 10 \\times 10 = \\mathbf{\\text{रु. } 100 \\text{ बचत}}$।</p>
              </div>

              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-1">
                <h5 class="font-bold text-purple-950">३.३ कामदार, दिन र पारिश्रमिक:</h5>
                <p class="text-slate-700">३ जनाको ५ दिनको रु. १५,००० $\\rightarrow$ १ जनाको १ दिनको रु. १,०००। ५ जनाको ८ दिनको ज्याला $= 1000 \\times 5 \\times 8 = \\mathbf{\\text{रु. } 40,000}$।</p>
              </div>

              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-1">
                <h5 class="font-bold text-purple-950">३.४ खाद्यान्न उपभोग र सदस्य विस्तार:</h5>
                <p class="text-slate-700">४ जनालाई २० केजी चामल २५ दिन पुग्छ $\\rightarrow$ १ जनालाई १०० दिन $\\rightarrow$ ५ जनालाई पुग्ने दिन $= \\frac{100}{5} = \\mathbf{20 \\text{ दिन}}$।</p>
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH8 TAB 4: QUIZ ================= -->
        <div id="ch8-view-quiz" class="hidden space-y-6">
          <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
            <div>
              <h4 class="font-black text-blue-900 text-sm md:text-base">पाठ ८: अन्तरक्रियात्मक आत्म-मूल्याङ्कन क्विज</h4>
              <p class="text-xs text-blue-700">५ वटा बहुवैकल्पिक प्रश्नहरू हल गरी आफ्नो बुझाइ तत्काल परीक्षण गर्नुहोस्</p>
            </div>
            <button onclick="resetQuizCh8()" class="text-xs font-bold bg-white text-blue-800 px-3 py-1.5 rounded-xl border border-blue-200 hover:bg-blue-50 shadow-xs cursor-pointer">
              🔄 पुनः सुरु गर्नुहोस्
            </button>
          </div>

          <!-- Q0 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न १: ५ ओटा कलमको मूल्य रु. ७५ पर्छ भने १ ओटा कलमको मूल्य कति हुन्छ?</span>
              <span id="ch8-qbadge-0" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch8-qbtn-0-0" onclick="checkQuizCh8(0, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) रु. १०</button>
              <button id="ch8-qbtn-0-1" onclick="checkQuizCh8(0, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) रु. १२</button>
              <button id="ch8-qbtn-0-2" onclick="checkQuizCh8(0, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) रु. १५</button>
              <button id="ch8-qbtn-0-3" onclick="checkQuizCh8(0, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) रु. २५</button>
            </div>
            <div id="ch8-qexp-0" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q1 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न २: १ दर्जन कापीको मूल्य रु. ४८० पर्छ भने ८ ओटा कापीको मूल्य कति हुन्छ?</span>
              <span id="ch8-qbadge-1" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch8-qbtn-1-0" onclick="checkQuizCh8(1, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) रु. ३२०</button>
              <button id="ch8-qbtn-1-1" onclick="checkQuizCh8(1, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) रु. ३००</button>
              <button id="ch8-qbtn-1-2" onclick="checkQuizCh8(1, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) रु. ३६०</button>
              <button id="ch8-qbtn-1-3" onclick="checkQuizCh8(1, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) रु. २४०</button>
            </div>
            <div id="ch8-qexp-1" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q2 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ३: ६ ओटा क्रिकेट ब्याटको मूल्य रु. ९०० पर्छ भने ४ ओटाको मूल्य कति होला?</span>
              <span id="ch8-qbadge-2" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch8-qbtn-2-0" onclick="checkQuizCh8(2, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) रु. ५००</button>
              <button id="ch8-qbtn-2-1" onclick="checkQuizCh8(2, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) रु. ६००</button>
              <button id="ch8-qbtn-2-2" onclick="checkQuizCh8(2, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) रु. ७००</button>
              <button id="ch8-qbtn-2-3" onclick="checkQuizCh8(2, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) रु. ५५०</button>
            </div>
            <div id="ch8-qexp-2" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q3 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ४: ४ ओटा कुर्सीको मूल्य रु. ४,८०० पर्छ भने ७ ओटा कुर्सीको मूल्य कति पर्ला?</span>
              <span id="ch8-qbadge-3" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch8-qbtn-3-0" onclick="checkQuizCh8(3, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) रु. ७,०००</button>
              <button id="ch8-qbtn-3-1" onclick="checkQuizCh8(3, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) रु. ७,८००</button>
              <button id="ch8-qbtn-3-2" onclick="checkQuizCh8(3, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) रु. ८,४००</button>
              <button id="ch8-qbtn-3-3" onclick="checkQuizCh8(3, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) रु. ९,६००</button>
            </div>
            <div id="ch8-qexp-3" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q4 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ५: ऐकिक नियममा धेरैबाट एउटा र एउटाबाट धेरै मान निकाल्दा गरिने गणितीय क्रियाहरूको सही क्रम कुन हो?</span>
              <span id="ch8-qbadge-4" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch8-qbtn-4-0" onclick="checkQuizCh8(4, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) गुणन, त्यसपछि भाग</button>
              <button id="ch8-qbtn-4-1" onclick="checkQuizCh8(4, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) पहिले भाग $(\\div)$, त्यसपछि गुणन $(\\times)$</button>
              <button id="ch8-qbtn-4-2" onclick="checkQuizCh8(4, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) जोड, त्यसपछि घटाउ</button>
              <button id="ch8-qbtn-4-3" onclick="checkQuizCh8(4, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) घटाउ, त्यसपछि जोड</button>
            </div>
            <div id="ch8-qexp-4" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

        </div>

      </div>
      <!-- ================= END OF CHAPTER 8 VIEW ================= -->
"""

if __name__ == '__main__':
    html = get_ch8_html()
    print("Generated Chapter 8 HTML! Length:", len(html))
