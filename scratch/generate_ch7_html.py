# -*- coding: utf-8 -*-
"""
Generates the HTML content for Chapter 7 (नाफा र नोक्सान - Profit and Loss) of Class 6 Mathematics.
Matches the design, CSS, and MathJax conventions of Chapters 1 to 6.
"""

def get_ch7_html():
    return """
      <!-- ================= CHAPTER 7: PROFIT AND LOSS (नाफा र नोक्सान) ================= -->
      <div id="chapter-view-7" class="hidden flex-1 flex flex-col">
        <!-- Top Chapter Banner -->
        <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-blue-600 mb-1">एकाइ २: अङ्कगणित (Unit 2: Arithmetic)</div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ ७: नाफा र नोक्सान (Profit and Loss)</h2>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ ९२–९७</span>
            <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-3 py-1 rounded-xl border border-emerald-200">अभ्यास ७ तथा परियोजना कार्य</span>
          </div>
        </div>

        <!-- Chapter 7 Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button id="ch7-tab-concepts" onclick="setTabCh7('concepts')" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap">
            १. अवधारणा र क्याल्कुलेटर
          </button>
          <button id="ch7-tab-exercises" onclick="setTabCh7('exercises')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            २. सम्पूर्ण अभ्यास समाधान (अभ्यास ७)
          </button>
          <button id="ch7-tab-tiers" onclick="setTabCh7('tiers')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
          </button>
          <button id="ch7-tab-quiz" onclick="setTabCh7('quiz')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap">
            ४. आत्म-मूल्याङ्कन क्विज
          </button>
        </div>

        <!-- ================= CH7 TAB 1: CONCEPTS ================= -->
        <div id="ch7-view-concepts" class="space-y-6">

          <!-- Core Concepts Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- C.P. Card -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-blue-50 text-blue-700 border border-blue-200">आधारभूत परिभाषा</span>
                <span class="text-xs font-mono text-slate-400">Cost Price (C.P.)</span>
              </div>
              <h3 class="text-lg font-bold text-slate-900">१. क्रय मूल्य (Cost Price - C.P. वा क्र.मू.)</h3>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                कुनै सामान खरिद गर्दा तिरेको रकम वा सामान बनाउँदा लागेको कुल खर्चलाई <strong>क्रय मूल्य</strong> भनिन्छ।
              </p>
              <div class="p-3 bg-amber-50 rounded-xl border border-amber-200 text-xs text-amber-900 space-y-1">
                <span class="font-bold">⭐ थप खर्चको नियम (Important Rule):</span>
                <p>वस्तु किनेपछि ढुवानी खर्च (Transportation), मर्मत खर्च (Repair) वा कर तिरेमा ती सबै क्रय मूल्यमै जोडिन्छन्:</p>
                <div class="font-mono font-bold bg-white p-2 rounded border border-amber-200 text-center">
                  जम्मा क्रय मूल्य = खरिद मूल्य + थप खर्च
                </div>
              </div>
            </div>

            <!-- S.P. Card -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-emerald-50 text-emerald-700 border border-emerald-200">आधारभूत परिभाषा</span>
                <span class="text-xs font-mono text-slate-400">Selling Price (S.P.)</span>
              </div>
              <h3 class="text-lg font-bold text-slate-900">२. विक्रय मूल्य (Selling Price - S.P. वा वि.मू.)</h3>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                कुनै वस्तु ग्राहक वा अन्य व्यक्तिलाई बेच्दा प्राप्त हुने रकमलाई <strong>विक्रय मूल्य</strong> भनिन्छ।
              </p>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-700 space-y-1">
                <span class="font-bold">व्यापारको अवस्था तुलना:</span>
                <ul class="list-disc pl-4 space-y-1">
                  <li>यदि $S.P. > C.P.$ भए $\\rightarrow$ <strong>नाफा (Profit)</strong></li>
                  <li>यदि $C.P. > S.P.$ भए $\\rightarrow$ <strong>नोक्सान (Loss)</strong></li>
                  <li>यदि $S.P. = C.P.$ भए $\\rightarrow$ <strong>नाफा पनि छैन, नोक्सान पनि छैन</strong></li>
                </ul>
              </div>
            </div>

            <!-- Profit Card -->
            <div class="p-5 bg-white rounded-2xl border border-emerald-200 shadow-sm space-y-3 bg-emerald-50/20">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-emerald-100 text-emerald-800 border border-emerald-300">फाइदा / नाफा</span>
                <span class="text-xs font-mono text-emerald-600 font-bold">S.P. > C.P.</span>
              </div>
              <h3 class="text-lg font-bold text-emerald-950">३. नाफा (Profit) र नाफा प्रतिशत</h3>
              <p class="text-xs md:text-sm text-slate-700">
                जब विक्रय मूल्य क्रय मूल्यभन्दा बढी हुन्छ, तब व्यापारीलाई <strong>नाफा</strong> हुन्छ।
              </p>
              <div class="space-y-2 text-xs md:text-sm bg-white p-3 rounded-xl border border-emerald-200">
                <div>• $\\text{नाफा} = \\text{वि.मू. } (S.P.) - \\text{क्र.मू. } (C.P.)$</div>
                <div>• $\\text{नाफा } \\% = \\frac{\\text{नाफा}}{C.P.} \\times 100\\%$</div>
                <div class="text-slate-500 text-xs pt-1 border-t">• $S.P. = C.P. + \\text{नाफा}$, तथा $C.P. = S.P. - \\text{नाफा}$</div>
              </div>
            </div>

            <!-- Loss Card -->
            <div class="p-5 bg-white rounded-2xl border border-rose-200 shadow-sm space-y-3 bg-rose-50/20">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-rose-100 text-rose-800 border border-rose-300">घाटा / नोक्सान</span>
                <span class="text-xs font-mono text-rose-600 font-bold">C.P. > S.P.</span>
              </div>
              <h3 class="text-lg font-bold text-rose-950">४. नोक्सान (Loss) र नोक्सान प्रतिशत</h3>
              <p class="text-xs md:text-sm text-slate-700">
                जब क्रय मूल्य विक्रय मूल्यभन्दा बढी हुन्छ (कम मूल्यमा बेचिन्छ), तब <strong>नोक्सान</strong> हुन्छ।
              </p>
              <div class="space-y-2 text-xs md:text-sm bg-white p-3 rounded-xl border border-rose-200">
                <div>• $\\text{नोक्सान} = \\text{क्र.मू. } (C.P.) - \\text{वि.मू. } (S.P.)$</div>
                <div>• $\\text{नोक्सान } \\% = \\frac{\\text{नोक्सान}}{C.P.} \\times 100\\%$</div>
                <div class="text-slate-500 text-xs pt-1 border-t">• $S.P. = C.P. - \\text{नोक्सान}$, तथा $C.P. = S.P. + \\text{नोक्सान}$</div>
              </div>
            </div>
          </div>

          <!-- ================= INTERACTIVE PROFIT & LOSS CALCULATOR ================= -->
          <div class="bg-gradient-to-br from-indigo-900 via-blue-900 to-slate-900 p-6 md:p-8 rounded-3xl text-white shadow-xl space-y-6">
            <div class="flex flex-wrap items-center justify-between gap-3">
              <div>
                <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-blue-500/30 text-blue-200 border border-blue-400/30">अन्तरक्रियात्मक गणितीय औजार</span>
                <h3 class="text-xl md:text-2xl font-black mt-1">नाफा-नोक्सान लाइभ क्याल्कुलेटर (Live P & L Simulator)</h3>
                <p class="text-xs md:text-sm text-blue-200">खरिद मूल्य, थप खर्च र बिक्री मूल्य प्रविष्ट गरी तत्काल परिणाम हेर्नुहोस्</p>
              </div>
              <!-- Presets -->
              <div class="flex flex-wrap gap-2 text-xs">
                <button onclick="setCh7Preset(450, 0, 500)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">उदाहरण १ (नाफा)</button>
                <button onclick="setCh7Preset(1200, 0, 1080)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">उदाहरण २ (नोक्सान)</button>
                <button onclick="setCh7Preset(4500, 500, 5500)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">थप खर्च सहित</button>
              </div>
            </div>

            <!-- Calculator Inputs Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- C.P. Input -->
              <div class="bg-white/10 p-4 rounded-2xl border border-white/15 space-y-1">
                <label class="text-xs text-blue-200 font-semibold block">खरिद मूल्य (Buying Price in रु.)</label>
                <input id="ch7-in-cp" type="number" value="1000" min="0" step="any" oninput="runCh7Calc()" class="w-full bg-white/20 border border-white/30 rounded-xl px-3 py-2 text-white font-mono text-lg font-bold focus:outline-none focus:ring-2 focus:ring-blue-400">
                <span class="text-[11px] text-blue-300 block">वस्तु किन्दा तिरेको रकम</span>
              </div>

              <!-- Extra Expenses Input -->
              <div class="bg-white/10 p-4 rounded-2xl border border-white/15 space-y-1">
                <label class="text-xs text-blue-200 font-semibold block">थप खर्च (ढुवानी / मर्मत रु.)</label>
                <input id="ch7-in-exp" type="number" value="100" min="0" step="any" oninput="runCh7Calc()" class="w-full bg-white/20 border border-white/30 rounded-xl px-3 py-2 text-white font-mono text-lg font-bold focus:outline-none focus:ring-2 focus:ring-blue-400">
                <span class="text-[11px] text-blue-300 block">भाडा, मर्मत वा कर खर्च</span>
              </div>

              <!-- S.P. Input -->
              <div class="bg-white/10 p-4 rounded-2xl border border-white/15 space-y-1">
                <label class="text-xs text-blue-200 font-semibold block">विक्रय मूल्य (Selling Price in रु.)</label>
                <input id="ch7-in-sp" type="number" value="1320" min="0" step="any" oninput="runCh7Calc()" class="w-full bg-white/20 border border-white/30 rounded-xl px-3 py-2 text-white font-mono text-lg font-bold focus:outline-none focus:ring-2 focus:ring-blue-400">
                <span class="text-[11px] text-blue-300 block">सामान बेचेर पाएको रकम</span>
              </div>
            </div>

            <!-- Dynamic Result Card -->
            <div id="ch7-calc-res" class="p-5 rounded-2xl bg-white/10 border border-white/20 backdrop-blur-sm space-y-3">
              <!-- Populated dynamically by runCh7Calc() -->
            </div>
          </div>

          <!-- Formula Table & Golden Rules -->
          <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <h4 class="font-bold text-slate-900 text-sm md:text-base border-b pb-2 flex items-center justify-between">
              <span>नाफा र नोक्सानका सम्पूर्ण सूत्रहरू (Formula Reference Table)</span>
              <span class="text-xs font-normal text-slate-500">कक्षा ६ स्तर</span>
            </h4>
            <div class="overflow-x-auto">
              <table class="w-full text-xs md:text-sm text-center border-collapse">
                <thead>
                  <tr class="bg-slate-50 text-slate-700">
                    <th class="p-3 border-b text-left">विवरण / अवस्था</th>
                    <th class="p-3 border-b">सम्बन्ध / सर्त</th>
                    <th class="p-3 border-b text-blue-700">रकम निकाल्ने सूत्र</th>
                    <th class="p-3 border-b text-emerald-700">प्रतिशत निकाल्ने सूत्र</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 text-slate-800">
                  <tr>
                    <td class="p-3 text-left font-bold text-emerald-700">नाफा (Profit)</td>
                    <td class="p-3 font-mono">S.P. > C.P.</td>
                    <td class="p-3 font-mono font-bold">नाफा = S.P. - C.P.</td>
                    <td class="p-3 font-mono font-bold text-emerald-700">नाफा % = (नाफा / C.P.) × 100%</td>
                  </tr>
                  <tr class="bg-slate-50">
                    <td class="p-3 text-left font-bold text-rose-700">नोक्सान (Loss)</td>
                    <td class="p-3 font-mono">C.P. > S.P.</td>
                    <td class="p-3 font-mono font-bold">नोक्सान = C.P. - S.P.</td>
                    <td class="p-3 font-mono font-bold text-rose-700">नोक्सान % = (नोक्सान / C.P.) × 100%</td>
                  </tr>
                  <tr>
                    <td class="p-3 text-left font-bold text-slate-700">नाफा भएको बेला वि.मू.</td>
                    <td class="p-3 font-mono">S.P. = C.P. + Profit</td>
                    <td class="p-3 font-mono">वि.मू. = क्र.मू. + नाफा</td>
                    <td class="p-3 text-slate-400">-</td>
                  </tr>
                  <tr class="bg-slate-50">
                    <td class="p-3 text-left font-bold text-slate-700">नोक्सान भएको बेला वि.मू.</td>
                    <td class="p-3 font-mono">S.P. = C.P. - Loss</td>
                    <td class="p-3 font-mono">वि.मू. = क्र.मू. - नोक्सान</td>
                    <td class="p-3 text-slate-400">-</td>
                  </tr>
                  <tr>
                    <td class="p-3 text-left font-bold text-slate-700">जम्मा क्रय मूल्य</td>
                    <td class="p-3 font-mono">Total C.P.</td>
                    <td class="p-3 font-mono">कुल क्र.मू. = खरिद + ढुवानी + मर्मत</td>
                    <td class="p-3 text-slate-500 font-medium">प्रतिशत सधैं कुल क्र.मू. मा</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Caution and Tips -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
              <div class="p-3.5 bg-rose-50 rounded-xl border border-rose-200 text-xs space-y-1 text-rose-900">
                <span class="font-bold flex items-center gap-1">⚠️ विद्यार्थीहरूले झुक्किने मुख्य गल्ती:</span>
                <p>धेरै विद्यार्थीहरूले नाफा वा नोक्सान प्रतिशत निकाल्दा झुक्किएर <strong>विक्रय मूल्य ($S.P.$) ले भाग</strong> गर्छन्। यो बिल्कुल गलत हो!</p>
                <p class="font-bold">सधैं सम्झनुहोस्: नाफा वा नोक्सान प्रतिशत सधैं क्रय मूल्य ($C.P.$) मा गणना गरिन्छ।</p>
              </div>

              <div class="p-3.5 bg-blue-50 rounded-xl border border-blue-200 text-xs space-y-1 text-blue-900">
                <span class="font-bold flex items-center gap-1">💡 एकाइ समानताको सुनौलो नियम:</span>
                <p>यदि वस्तु दर्जनमा किनेको छ तर गोटामा बेचेको छ भने, हिसाब गर्दा <strong>दुवैलाई गोटामा वा दुवैलाई दर्जनमा</strong> रूपान्तरण गर्नुपर्छ।</p>
                <p class="font-bold">१ दर्जन = १२ गोटा, १ स्कोर = २० गोटा।</p>
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH7 TAB 2: EXERCISES ================= -->
        <div id="ch7-view-exercises" class="hidden space-y-6">
          
          <!-- Exercise Navigation Pills -->
          <div class="flex gap-2 overflow-x-auto pb-2 border-b border-slate-200 text-xs md:text-sm font-bold">
            <button id="ch7-pill-sec1" onclick="setExerciseCh7('sec1')" class="px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap">
              भाग १: प्रश्न १ देखि ५ (आधारभूत र मौखिक)
            </button>
            <button id="ch7-pill-sec2" onclick="setExerciseCh7('sec2')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              भाग २: प्रश्न ६ देखि ९ (शब्द समस्या र व्यावहारिक हिसाब)
            </button>
            <button id="ch7-pill-sec3" onclick="setExerciseCh7('sec3')" class="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap">
              भाग ३: पाठ्यपुस्तकका उदाहरणहरू र परियोजना कार्य
            </button>
          </div>

          <!-- ---------------- SECTION 1: QUESTIONS 1 TO 5 ---------------- -->
          <div id="ch7-sec-sec1" class="space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">अभ्यास ७: प्रश्न १ देखि ५ को १००% विस्तृत समाधान</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ ९५–९६ (सारिणी पूरा गर्ने, नाफा/नोक्सान प्रतिशत र व्यावहारिक मौखिक प्रश्नहरू)</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">११ उपप्रश्नहरू</span>
            </div>

            <!-- Q1 Table -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <div class="border-b pb-2">
                <h4 class="font-bold text-slate-800 text-sm md:text-base">प्रश्न १: तलको तालिका पूरा गर्नुहोस् (Complete the Table):</h4>
                <p class="text-xs text-slate-500">क्रय मूल्य, विक्रय मूल्य, नाफा वा नोक्सान रकम तथा प्रतिशतको आपसी सम्बन्ध</p>
              </div>

              <div class="overflow-x-auto">
                <table class="w-full text-xs md:text-sm border-collapse text-center">
                  <thead>
                    <tr class="bg-slate-100 text-slate-800">
                      <th class="p-2.5 border">क्र.सं.</th>
                      <th class="p-2.5 border">क्रय मूल्य (C.P.)</th>
                      <th class="p-2.5 border">विक्रय मूल्य (S.P.)</th>
                      <th class="p-2.5 border text-emerald-700">नाफा (Profit)</th>
                      <th class="p-2.5 border text-rose-700">नोक्सान (Loss)</th>
                      <th class="p-2.5 border text-blue-700">नाफा वा नोक्सान %</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-200 text-slate-800">
                    <tr>
                      <td class="p-2 border font-bold">(क)</td>
                      <td class="p-2 border">रु. ४५०</td>
                      <td class="p-2 border font-bold text-blue-600">रु. ५००</td>
                      <td class="p-2 border font-bold text-emerald-700">रु. ५०</td>
                      <td class="p-2 border text-slate-400">-</td>
                      <td class="p-2 border font-bold text-emerald-700">११.११% नाफा</td>
                    </tr>
                    <tr class="bg-slate-50">
                      <td class="p-2 border font-bold">(ख)</td>
                      <td class="p-2 border">रु. ६००</td>
                      <td class="p-2 border font-bold text-blue-600">रु. ५४०</td>
                      <td class="p-2 border text-slate-400">-</td>
                      <td class="p-2 border font-bold text-rose-700">रु. ६०</td>
                      <td class="p-2 border font-bold text-rose-700">१०% नोक्सान</td>
                    </tr>
                    <tr>
                      <td class="p-2 border font-bold">(ग)</td>
                      <td class="p-2 border font-bold text-blue-600">रु. ८००</td>
                      <td class="p-2 border">रु. ९२०</td>
                      <td class="p-2 border font-bold text-emerald-700">रु. १२०</td>
                      <td class="p-2 border text-slate-400">-</td>
                      <td class="p-2 border font-bold text-emerald-700">१५% नाफा</td>
                    </tr>
                    <tr class="bg-slate-50">
                      <td class="p-2 border font-bold">(घ)</td>
                      <td class="p-2 border font-bold text-blue-600">रु. १,५००</td>
                      <td class="p-2 border">रु. १,३५०</td>
                      <td class="p-2 border text-slate-400">-</td>
                      <td class="p-2 border font-bold text-rose-700">रु. १५०</td>
                      <td class="p-2 border font-bold text-rose-700">१०% नोक्सान</td>
                    </tr>
                    <tr>
                      <td class="p-2 border font-bold">(ङ)</td>
                      <td class="p-2 border">रु. २,५००</td>
                      <td class="p-2 border font-bold text-blue-600">रु. २,८००</td>
                      <td class="p-2 border font-bold text-emerald-700">रु. ३००</td>
                      <td class="p-2 border text-slate-400">-</td>
                      <td class="p-2 border font-bold text-emerald-700">१२% नाफा</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <!-- Detailed calculation accordion / info box -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 text-xs md:text-sm space-y-2">
                <span class="font-bold text-slate-800">चरणबद्ध हल विधि (Step-by-step Solution):</span>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                  <div class="p-2.5 bg-white rounded-lg border">
                    <strong>(क):</strong> नाफा $= 500 - 450 = \\text{रु. } 50$<br>
                    नाफा $\% = \\frac{50}{450} \\times 100\\% = \\frac{100}{9}\\% \\approx 11.11\\%$
                  </div>
                  <div class="p-2.5 bg-white rounded-lg border">
                    <strong>(ख):</strong> नोक्सान $= 600 - 540 = \\text{रु. } 60$<br>
                    नोक्सान $\% = \\frac{60}{600} \\times 100\\% = 10\\%$
                  </div>
                  <div class="p-2.5 bg-white rounded-lg border">
                    <strong>(ग):</strong> $C.P. = S.P. - \\text{नाफा} = 920 - 120 = \\text{रु. } 800$<br>
                    नाफा $\% = \\frac{120}{800} \\times 100\\% = 15\\%$
                  </div>
                  <div class="p-2.5 bg-white rounded-lg border">
                    <strong>(घ):</strong> $C.P. = S.P. + \\text{नोक्सान} = 1350 + 150 = \\text{रु. } 1500$<br>
                    नोक्सान $\% = \\frac{150}{1500} \\times 100\\% = 10\\%$
                  </div>
                  <div class="p-2.5 bg-white rounded-lg border md:col-span-2">
                    <strong>(ङ):</strong> $S.P. = C.P. + \\text{नाफा} = 2500 + 300 = \\text{रु. } 2800$<br>
                    नाफा $\% = \\frac{300}{2500} \\times 100\\% = 12\\%$
                  </div>
                </div>
              </div>
            </div>

            <!-- Q2 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm md:text-base border-b pb-2">
                प्रश्न २: क्रय मूल्य र विक्रय मूल्यको तुलना गरी नाफा वा नोक्सान प्रतिशत पत्ता लगाउनुहोस्:
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                <!-- 2(k) -->
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <div class="flex justify-between font-bold text-slate-800">
                    <span>(क) क्र.मू. = रु. २००, वि.मू. = रु. २४०</span>
                    <span class="text-emerald-700">नाफा</span>
                  </div>
                  <p class="text-slate-600">यहाँ $S.P. > C.P.$ भएकाले नाफा हुन्छ।</p>
                  <p class="font-mono">नाफा $= 240 - 200 = \\text{रु. } 40$</p>
                  <p class="font-mono font-bold text-emerald-800">नाफा $\% = \\frac{40}{200} \\times 100\\% = 20\\%$</p>
                </div>

                <!-- 2(kh) -->
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <div class="flex justify-between font-bold text-slate-800">
                    <span>(ख) क्र.मू. = रु. ५००, वि.मू. = रु. ४५०</span>
                    <span class="text-rose-700">नोक्सान</span>
                  </div>
                  <p class="text-slate-600">यहाँ $C.P. > S.P.$ भएकाले नोक्सान हुन्छ।</p>
                  <p class="font-mono">नोक्सान $= 500 - 450 = \\text{रु. } 50$</p>
                  <p class="font-mono font-bold text-rose-800">नोक्सान $\% = \\frac{50}{500} \\times 100\\% = 10\\%$</p>
                </div>

                <!-- 2(g) -->
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <div class="flex justify-between font-bold text-slate-800">
                    <span>(ग) क्र.मू. = रु. ८००, वि.मू. = रु. ९२०</span>
                    <span class="text-emerald-700">नाफा</span>
                  </div>
                  <p class="text-slate-600">यहाँ $S.P. > C.P.$ भएकाले नाफा हुन्छ।</p>
                  <p class="font-mono">नाफा $= 920 - 800 = \\text{रु. } 120$</p>
                  <p class="font-mono font-bold text-emerald-800">नाफा $\% = \\frac{120}{800} \\times 100\\% = 15\\%$</p>
                </div>

                <!-- 2(gh) -->
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <div class="flex justify-between font-bold text-slate-800">
                    <span>(घ) क्र.मू. = रु. १,२००, वि.मू. = रु. १,०८०</span>
                    <span class="text-rose-700">नोक्सान</span>
                  </div>
                  <p class="text-slate-600">यहाँ $C.P. > S.P.$ भएकाले नोक्सान हुन्छ।</p>
                  <p class="font-mono">नोक्सान $= 1200 - 1080 = \\text{रु. } 120$</p>
                  <p class="font-mono font-bold text-rose-800">नोक्सान $\% = \\frac{120}{1200} \\times 100\\% = 10\\%$</p>
                </div>

                <!-- 2(ng) -->
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1 md:col-span-2">
                  <div class="flex justify-between font-bold text-slate-800">
                    <span>(ङ) क्र.मू. = रु. २,०००, वि.मू. = रु. २,३००</span>
                    <span class="text-emerald-700">नाफा</span>
                  </div>
                  <p class="text-slate-600">यहाँ $S.P. > C.P.$ भएकाले नाफा हुन्छ।</p>
                  <p class="font-mono">नाफा $= 2300 - 2000 = \\text{रु. } 300$</p>
                  <p class="font-mono font-bold text-emerald-800">नाफा $\% = \\frac{300}{2000} \\times 100\\% = 15\\%$</p>
                </div>
              </div>
            </div>

            <!-- Q3, Q4, Q5 Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Q3 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ३</span>
                <p class="text-slate-700">हरिले एउटा रेडियो रु. १,५०० मा किनेर १०% नोक्सानमा बेचेछन् भने नोक्सान रकम र बिक्री मूल्य कति?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg space-y-1 font-mono text-xs">
                  <div>क्र.मू. $(C.P.) = \\text{रु. } 1,500$</div>
                  <div>नोक्सान $= 1500 \\times 10\\% = \\text{रु. } 150$</div>
                  <div class="font-bold text-rose-700">वि.मू. $= 1500 - 150 = \\text{रु. } 1,350$</div>
                </div>
              </div>

              <!-- Q4 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ४</span>
                <p class="text-slate-700">एउटा तरकारी व्यापारीले ५० केजी काउली रु. १,५०० मा किनेर प्रति केजी रु. ३६ का दरले बेच्दा नाफा वा नोक्सान % कति?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg space-y-1 font-mono text-xs">
                  <div>क्र.मू. $= \\text{रु. } 1,500$</div>
                  <div>वि.मू. $= 50 \\times 36 = \\text{रु. } 1,800$</div>
                  <div>नाफा $= 1800 - 1500 = \\text{रु. } 300$</div>
                  <div class="font-bold text-emerald-700">नाफा $\% = \\frac{300}{1500} \\times 100\\% = 20\\%$</div>
                </div>
              </div>

              <!-- Q5 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-xs">प्रश्न ५</span>
                <p class="text-slate-700">एउटा फलफूल व्यापारीले १ दर्जन सुन्तला रु. २४० मा किनेर प्रतिगोटा रु. २५ मा बेच्दा नाफा वा नोक्सान % कति?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg space-y-1 font-mono text-xs">
                  <div>१२ गोटाको क्र.मू. $= \\text{रु. } 240$</div>
                  <div>१२ गोटाको वि.मू. $= 12 \\times 25 = \\text{रु. } 300$</div>
                  <div>नाफा $= 300 - 240 = \\text{रु. } 60$</div>
                  <div class="font-bold text-emerald-700">नाफा $\% = \\frac{60}{240} \\times 100\\% = 25\\%$</div>
                </div>
              </div>
            </div>

          </div>

          <!-- ---------------- SECTION 2: QUESTIONS 6 TO 9 ---------------- -->
          <div id="ch7-sec-sec2" class="hidden space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">अभ्यास ७: प्रश्न ६ देखि ९ को १००% विस्तृत समाधान</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ ९६–९७ (शब्द समस्या, थप खर्च, र बहुचरणीय व्यावहारिक हिसाब)</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">८ उपप्रश्नहरू</span>
            </div>

            <!-- Q6 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm md:text-base border-b pb-2">
                प्रश्न ६: स्टेसनरी तथा पुस्तक खरिद-बिक्री सम्बन्धी समस्या
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
                <!-- 6(k) -->
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                  <span class="font-bold text-blue-700">(क) १ दर्जन कापी रु. ६०० मा किनेर प्रतिगोटा रु. ५५ मा बेच्दा:</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• १ दर्जन $= 12$ गोटाको क्रय मूल्य $(C.P.) = \\text{रु. } 600$</p>
                    <p>• १२ वटा कापीको विक्रय मूल्य $(S.P.) = 12 \\times 55 = \\text{रु. } 660$</p>
                    <p>• यहाँ $S.P. > C.P.$ भएकाले नाफा हुन्छ।</p>
                    <p>• नाफा $= 660 - 600 = \\text{रु. } 60$</p>
                    <p class="font-bold text-emerald-800">• नाफा $\% = \\frac{60}{600} \\times 100\\% = 10\\%$</p>
                  </div>
                </div>

                <!-- 6(kh) -->
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                  <span class="font-bold text-blue-700">(ख) एउटा पुस्तक पसलेले रु. ३,५०० का पुस्तकहरू १५% नाफा लिएर बेच्दा:</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• क्रय मूल्य $(C.P.) = \\text{रु. } 3,500$</p>
                    <p>• नाफा प्रतिशत $= 15\\%$</p>
                    <p>• नाफा रकम $= 3500 \\times \\frac{15}{100} = 35 \\times 15 = \\text{रु. } 525$</p>
                    <p>• विक्रय मूल्य $(S.P.) = C.P. + \\text{नाफा} = 3500 + 525$</p>
                    <p class="font-bold text-emerald-800">• जम्मा विक्रय मूल्य $= \\text{रु. } 4,025$</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Q7 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm md:text-base border-b pb-2">
                प्रश्न ७: घडी खरिद-बिक्री सम्बन्धी समस्या
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
                <!-- 7(k) -->
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                  <span class="font-bold text-blue-700">(क) सीताले रु. १,२०० मा किनेको घडी रु. १,३२० मा बेच्दा:</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• क्र.मू. $(C.P.) = \\text{रु. } 1,200$</p>
                    <p>• वि.मू. $(S.P.) = \\text{रु. } 1,320$</p>
                    <p>• नाफा $= 1320 - 1200 = \\text{रु. } 120$</p>
                    <p class="font-bold text-emerald-800">• नाफा $\% = \\frac{120}{1200} \\times 100\\% = 10\\%$</p>
                  </div>
                </div>

                <!-- 7(kh) -->
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                  <span class="font-bold text-blue-700">(ख) रु. २,४०० मा किनेको घडी १२% नाफामा बेच्दा:</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• क्र.मू. $(C.P.) = \\text{रु. } 2,400$</p>
                    <p>• नाफा रकम $= 2400 \\times \\frac{12}{100} = 24 \\times 12 = \\text{रु. } 288$</p>
                    <p>• विक्रय मूल्य $(S.P.) = 2400 + 288$</p>
                    <p class="font-bold text-emerald-800">• विक्रय मूल्य $= \\text{रु. } 2,688$</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Q8 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-800 text-sm md:text-base border-b pb-2">
                प्रश्न ८: रेडियो तथा विद्युतीय उपकरण खरिद-बिक्री (नोक्सान सम्बन्धी)
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
                <!-- 8(k) -->
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                  <span class="font-bold text-rose-700">(क) रु. १,६०० मा किनेको रेडियो रु. १,४४० मा बेच्दा:</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• क्र.मू. $(C.P.) = \\text{रु. } 1,600$</p>
                    <p>• वि.मू. $(S.P.) = \\text{रु. } 1,440$</p>
                    <p>• नोक्सान $= 1600 - 1440 = \\text{रु. } 160$</p>
                    <p class="font-bold text-rose-800">• नोक्सान $\% = \\frac{160}{1600} \\times 100\\% = 10\\%$</p>
                  </div>
                </div>

                <!-- 8(kh) -->
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                  <span class="font-bold text-rose-700">(ख) रु. ४,००० मा किनेको सामान ८% नोक्सानमा बेच्दा:</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• क्र.मू. $(C.P.) = \\text{रु. } 4,000$</p>
                    <p>• नोक्सान रकम $= 4000 \\times \\frac{8}{100} = 40 \\times 8 = \\text{रु. } 320$</p>
                    <p>• विक्रय मूल्य $(S.P.) = 4000 - 320$</p>
                    <p class="font-bold text-rose-800">• विक्रय मूल्य $= \\text{रु. } 3,680$</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Q9 (Overhead expenses) -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-900 text-sm md:text-base border-b pb-2 flex items-center justify-between">
                <span>प्रश्न ९: थप खर्च (ढुवानी र मर्मत खर्च) समावेश भएका समस्याहरू</span>
                <span class="text-xs bg-amber-100 text-amber-800 font-bold px-2 py-0.5 rounded">उच्च प्राथमिकता</span>
              </h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
                <!-- 9(k) -->
                <div class="p-4 bg-amber-50/50 rounded-xl border border-amber-200 space-y-2">
                  <span class="font-bold text-slate-800">(क) रमेशले पुरानो साइकल रु. ३,२०० मा किनेर रु. ३०० मर्मत खर्च गरे। पछि रु. ३,८५० मा बेच्दा:</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• खरिद मूल्य $= \\text{रु. } 3,200$</p>
                    <p>• मर्मत खर्च $= \\text{रु. } 300$</p>
                    <p>• <strong>जम्मा क्रय मूल्य $(C.P.) = 3200 + 300 = \\text{रु. } 3,500$</strong></p>
                    <p>• विक्रय मूल्य $(S.P.) = \\text{रु. } 3,850$</p>
                    <p>• नाफा $= 3850 - 3500 = \\text{रु. } 350$</p>
                    <p class="font-bold text-emerald-800">• नाफा $\% = \\frac{350}{3500} \\times 100\\% = 10\\%$</p>
                  </div>
                </div>

                <!-- 9(kh) -->
                <div class="p-4 bg-amber-50/50 rounded-xl border border-amber-200 space-y-2">
                  <span class="font-bold text-slate-800">(ख) व्यापारीले रु. १०,००० को सामान खरिद गरी रु. ५०० ढुवानी खर्च तिरे। १०% नाफा कमाउन कतिमा बेच्नुपर्छ?</span>
                  <div class="space-y-1 text-slate-700">
                    <p>• खरिद मूल्य $= \\text{रु. } 10,000$</p>
                    <p>• ढुवानी खर्च $= \\text{रु. } 500$</p>
                    <p>• <strong>जम्मा क्रय मूल्य $(C.P.) = 10000 + 500 = \\text{रु. } 10,500$</strong></p>
                    <p>• आवश्यक नाफा $= 10500 \\times \\frac{10}{100} = \\text{रु. } 1,050$</p>
                    <p>• विक्रय मूल्य $(S.P.) = 10500 + 1050$</p>
                    <p class="font-bold text-emerald-800">• जम्मा विक्रय मूल्य $= \\text{रु. } 11,550$</p>
                  </div>
                </div>
              </div>
            </div>

          </div>

          <!-- ---------------- SECTION 3: EXAMPLES & PROJECT WORK ---------------- -->
          <div id="ch7-sec-sec3" class="hidden space-y-6">
            <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="font-black text-blue-900 text-sm md:text-base">पाठ्यपुस्तकका उदाहरणहरू र परियोजना कार्य प्रतिवेदन</h4>
                <p class="text-xs text-blue-700">पाठ्यपुस्तक पृष्ठ ९२–९५ का उदाहरण १, २, र ३ तथा व्यावहारिक परियोजना कार्य ढाँचा</p>
              </div>
              <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">उदाहरण १–३ र परियोजना</span>
            </div>

            <!-- Textbook Examples -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Ex 1 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <div class="flex items-center justify-between">
                  <span class="font-bold text-blue-700">उदाहरण १ (नाफा प्रतिशत)</span>
                  <span class="text-[11px] text-slate-500">पृष्ठ ९३</span>
                </div>
                <p class="text-slate-600">एउटा ब्याग रु. ४५० मा किनेर रु. ५०० मा बेच्दा कति नाफा प्रतिशत हुन्छ?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs space-y-1">
                  <div>$C.P. = \\text{रु. } 450, S.P. = \\text{रु. } 500$</div>
                  <div>$\\text{नाफा} = 500 - 450 = \\text{रु. } 50$</div>
                  <div class="text-emerald-700 font-bold">$\\text{नाफा } \\% = \\frac{50}{450} \\times 100\\% = 11.11\\%$</div>
                </div>
              </div>

              <!-- Ex 2 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <div class="flex items-center justify-between">
                  <span class="font-bold text-rose-700">उदाहरण २ (नोक्सान प्रतिशत)</span>
                  <span class="text-[11px] text-slate-500">पृष्ठ ९४</span>
                </div>
                <p class="text-slate-600">रु. १,२०० मा किनेको सामान रु. १,०८० मा बेच्दा नोक्सान प्रतिशत कति हुन्छ?</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs space-y-1">
                  <div>$C.P. = \\text{रु. } 1200, S.P. = \\text{रु. } 1080$</div>
                  <div>$\\text{नोक्सान} = 1200 - 1080 = \\text{रु. } 120$</div>
                  <div class="text-rose-700 font-bold">$\\text{नोक्सान } \\% = \\frac{120}{1200} \\times 100\\% = 10\\%$</div>
                </div>
              </div>

              <!-- Ex 3 -->
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <div class="flex items-center justify-between">
                  <span class="font-bold text-amber-700">उदाहरण ३ (थप खर्च सहित)</span>
                  <span class="text-[11px] text-slate-500">पृष्ठ ९४</span>
                </div>
                <p class="text-slate-600">साइकल रु. ४,५०० मा किनी रु. ५०० मर्मत गरी रु. ५,५०० मा बेच्दा:</p>
                <div class="p-2.5 bg-slate-50 rounded-lg font-mono text-xs space-y-1">
                  <div>$\\text{जम्मा } C.P. = 4500 + 500 = \\text{रु. } 5000$</div>
                  <div>$\\text{नाफा} = 5500 - 5000 = \\text{रु. } 500$</div>
                  <div class="text-emerald-700 font-bold">$\\text{नाफा } \\% = \\frac{500}{5000} \\times 100\\% = 10\\%$</div>
                </div>
              </div>
            </div>

            <!-- Project Work Template Card -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
              <div class="border-b pb-2 flex items-center justify-between">
                <div>
                  <h4 class="font-bold text-slate-900 text-sm md:text-base">परियोजना कार्य (Project Work): स्थानीय किराना पसलको नाफा मार्जिन सर्वेक्षण</h4>
                  <p class="text-xs text-slate-500">पाठ्यपुस्तक पृष्ठ ९७ को निर्देशन अनुरूप तयार गरिएको नमुना प्रतिवेदन</p>
                </div>
                <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-lg">व्यावहारिक परियोजना</span>
              </div>

              <div class="overflow-x-auto text-xs md:text-sm">
                <table class="w-full text-center border-collapse">
                  <thead>
                    <tr class="bg-slate-100 text-slate-800">
                      <th class="p-2 border text-left">वस्तुको नाम</th>
                      <th class="p-2 border">एकाइ</th>
                      <th class="p-2 border">खरिद मूल्य (C.P.)</th>
                      <th class="p-2 border">बिक्री मूल्य (S.P.)</th>
                      <th class="p-2 border text-emerald-700">नाफा रकम</th>
                      <th class="p-2 border text-blue-700">नाफा प्रतिशत</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-200 text-slate-700">
                    <tr>
                      <td class="p-2 border text-left font-medium">१. चिनी</td>
                      <td class="p-2 border">१ केजी</td>
                      <td class="p-2 border">रु. ९५</td>
                      <td class="p-2 border">रु. १०५</td>
                      <td class="p-2 border text-emerald-700 font-bold">रु. १०</td>
                      <td class="p-2 border font-bold">१०.५३%</td>
                    </tr>
                    <tr class="bg-slate-50">
                      <td class="p-2 border text-left font-medium">२. सूर्यमुखी तेल</td>
                      <td class="p-2 border">१ लिटर</td>
                      <td class="p-2 border">रु. २२०</td>
                      <td class="p-2 border">रु. २५०</td>
                      <td class="p-2 border text-emerald-700 font-bold">रु. ३०</td>
                      <td class="p-2 border font-bold">१३.६४%</td>
                    </tr>
                    <tr>
                      <td class="p-2 border text-left font-medium">३. जिरा मसिनो चामल</td>
                      <td class="p-2 border">२५ केजी बोरा</td>
                      <td class="p-2 border">रु. २,०००</td>
                      <td class="p-2 border">रु. २,२५०</td>
                      <td class="p-2 border text-emerald-700 font-bold">रु. २५०</td>
                      <td class="p-2 border font-bold">१२.५०%</td>
                    </tr>
                    <tr class="bg-slate-50">
                      <td class="p-2 border text-left font-medium">४. नुहाउने साबुन</td>
                      <td class="p-2 border">१ गोटा</td>
                      <td class="p-2 border">रु. ४०</td>
                      <td class="p-2 border">रु. ५०</td>
                      <td class="p-2 border text-emerald-700 font-bold">रु. १०</td>
                      <td class="p-2 border font-bold">२५.००%</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <p class="text-xs text-slate-500 bg-slate-50 p-2.5 rounded-lg border">
                <strong>निष्कर्ष:</strong> खुद्रा पसलमा विभिन्न वस्तुहरूमा नाफा प्रतिशत १०% देखि २५% सम्म राखेको पाइयो। दैनिक उपभोग्य आधारभूत वस्तु (जस्तै चामल, चिनी) मा नाफा प्रतिशत कम र कस्मेटिक्स वा साबुनमा नाफा प्रतिशत बढी हुने देखियो।
              </p>
            </div>

          </div>

        </div>

        <!-- ================= CH7 TAB 3: TIERS (EXPANDED TO 16 QUESTIONS) ================= -->
        <div id="ch7-view-tiers" class="hidden space-y-6">
          <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
            <div>
              <h4 class="font-black text-blue-900 text-sm md:text-base">तीन तहका नमुना परीक्षा प्रश्नहरू (३-Tier Cognitive Questions)</h4>
              <p class="text-xs text-blue-700">नेपाल परीक्षा बोर्डको ब्लूप्रिन्ट अनुसार ज्ञान, प्रयोग र उच्च दक्षताका १६ वटा परीक्षा-केन्द्रित प्रश्नहरू</p>
            </div>
            <span class="text-xs font-bold bg-white text-blue-800 px-3 py-1 rounded-xl shadow-xs border border-blue-200">१६ प्रश्नहरू पूर्ण हल सहित</span>
          </div>

          <!-- Tier 1: Knowledge & Understanding (6 Questions) -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center justify-between border-b pb-2">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-500 inline-block"></span>
                <h4 class="font-bold text-slate-800 text-sm md:text-base">तह १: ज्ञान तथा बोध (Knowledge & Understanding - ६ प्रश्नहरू)</h4>
              </div>
              <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800">१-२ अङ्कका प्रश्नहरू</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.१ नाफा र नोक्सान हुने अवस्था:</span>
                <p class="text-slate-600">कुन अवस्थामा नाफा र कुन अवस्थामा नोक्सान हुन्छ?</p>
                <div class="text-emerald-700 font-medium">उत्तर: यदि $S.P. > C.P.$ भए नाफा, र $C.P. > S.P.$ भए नोक्सान हुन्छ।</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.२ नाफा र नोक्सान प्रतिशत सूत्र:</span>
                <p class="text-slate-600">नाफा प्रतिशत र नोक्सान प्रतिशतको सूत्र लेख्नुहोस्।</p>
                <div class="text-emerald-700 font-medium">उत्तर: $\\text{नाफा } \\% = \\frac{\\text{नाफा}}{C.P.} \\times 100\\%$, $\\text{नोक्सान } \\% = \\frac{\\text{नोक्सान}}{C.P.} \\times 100\\%$।</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.३ थप खर्चको नियम:</span>
                <p class="text-slate-600">ढुवानी वा मर्मत खर्चलाई कुन मूल्यमा जोडिन्छ?</p>
                <div class="text-emerald-700 font-medium">उत्तर: थप खर्चलाई सधैं खरिद मूल्यमा जोडेर कुल क्रय मूल्य $(C.P.)$ बनाइन्छ।</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.४ प्रत्यक्ष गणना (नाफा):</span>
                <p class="text-slate-600">रु. २,५०० मा किनेको सामान रु. २,८०० मा बेच्दा नाफा रकम कति?</p>
                <div class="text-emerald-700 font-medium">उत्तर: $\\text{नाफा} = 2800 - 2500 = \\text{रु. } 300$।</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.५ नोक्सान गणना:</span>
                <p class="text-slate-600">रु. १,५०० मा किनेको घडी रु. १,३५० मा बेच्दा नोक्सान कति?</p>
                <div class="text-rose-700 font-medium">उत्तर: $\\text{नोक्सान} = 1500 - 1350 = \\text{रु. } 150$।</div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">१.६ विक्रय मूल्य निकाल्ने:</span>
                <p class="text-slate-600">क्र.मू. रु. ८०० र नाफा रु. १२० भए वि.मू. कति हुन्छ?</p>
                <div class="text-emerald-700 font-medium">उत्तर: $S.P. = 800 + 120 = \\text{रु. } 920$।</div>
              </div>
            </div>
          </div>

          <!-- Tier 2: Application & Problem Solving (6 Questions) -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center justify-between border-b pb-2">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-blue-500 inline-block"></span>
                <h4 class="font-bold text-slate-800 text-sm md:text-base">तह २: प्रयोग तथा समस्या समाधान (Application - ६ प्रश्नहरू)</h4>
              </div>
              <span class="text-xs font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800">२-३ अङ्कका प्रश्नहरू</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.१ दर्जन र गोटाको मिलान:</span>
                <p class="text-slate-600">१ दर्जन कापी रु. ७२० मा किनेर प्रतिगोटा रु. ७५ मा बेच्दा नाफा % कति?</p>
                <div class="text-slate-700 text-xs">
                  १२ वटाको वि.मू. $= 12 \\times 75 = \\text{रु. } 900$<br>
                  नाफा $= 900 - 720 = \\text{रु. } 180$<br>
                  <strong>नाफा % $= \\frac{180}{720} \\times 100\\% = 25\\%$</strong>
                </div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.२ ढुवानी खर्च सहितको फर्निचर:</span>
                <p class="text-slate-600">एउटा टेबुल रु. ४,२०० मा किनी रु. ३०० ढुवानी खर्च लाग्यो र रु. ५,४०० मा बेचियो भने नाफा % कति?</p>
                <div class="text-slate-700 text-xs">
                  कुल $C.P. = 4200 + 300 = \\text{रु. } 4,500$<br>
                  नाफा $= 5400 - 4500 = \\text{रु. } 900$<br>
                  <strong>नाफा % $= \\frac{900}{4500} \\times 100\\% = 20\\%$</strong>
                </div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.३ पसलहरूको तुलनात्मक अध्ययन:</span>
                <p class="text-slate-600">पसल 'क' ले रु. ४०० को सामान रु. ४६० मा र 'ख' ले रु. ५०० को रु. ५६० मा बेचे, कसको नाफा % बढी?</p>
                <div class="text-slate-700 text-xs">
                  'क' को नाफा % $= \\frac{60}{400} \\times 100\\% = 15\\%$<br>
                  'ख' को नाफा % $= \\frac{60}{500} \\times 100\\% = 12\\%$<br>
                  <strong>निष्कर्ष: पसल 'क' को नाफा प्रतिशत बढी छ।</strong>
                </div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.४ नोक्सान प्रतिशतबाट वि.मू.:</span>
                <p class="text-slate-600">रु. ५,००० को मोबाइल ८% नोक्सानमा बेच्दा बिक्री मूल्य कति?</p>
                <div class="text-slate-700 text-xs">
                  नोक्सान रकम $= 5000 \\times \\frac{8}{100} = \\text{रु. } 400$<br>
                  <strong>वि.मू. $= 5000 - 400 = \\text{रु. } 4,600$</strong>
                </div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.५ सुन्तला व्यापार (गोटा र दर्जन):</span>
                <p class="text-slate-600">१५० वटा सुन्तला रु. १,२०० मा किनेर प्रतिदर्जन रु. १२० मा बेच्दा नाफा वा नोक्सान % कति?</p>
                <div class="text-slate-700 text-xs">
                  दर्जन सङ्ख्या $= \\frac{150}{12} = 12.5$ दर्जन<br>
                  वि.मू. $= 12.5 \\times 120 = \\text{रु. } 1,500$<br>
                  नाफा $= 1500 - 1200 = \\text{रु. } 300$<br>
                  <strong>नाफा % $= \\frac{300}{1200} \\times 100\\% = 25\\%$</strong>
                </div>
              </div>

              <div class="p-3 bg-slate-50 rounded-xl border space-y-1">
                <span class="font-bold text-slate-800">२.६ किसानको तरकारी बिक्री:</span>
                <p class="text-slate-600">१०० केजी गोलभेँडा रु. २,००० मा किनी ढुवानी रु. ४०० लाग्यो। प्रति केजी रु. ३५ मा बेच्दा नाफा % कति?</p>
                <div class="text-slate-700 text-xs">
                  कुल $C.P. = 2000 + 400 = \\text{रु. } 2,400$<br>
                  वि.मू. $= 100 \\times 35 = \\text{रु. } 3,500$<br>
                  नाफा $= 3500 - 2400 = \\text{रु. } 1,100$<br>
                  <strong>नाफा % $= \\frac{1100}{2400} \\times 100\\% \\approx 45.83\\%$</strong>
                </div>
              </div>
            </div>
          </div>

          <!-- Tier 3: Higher Ability & Multi-Step Problems (4 Questions) -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center justify-between border-b pb-2">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-purple-500 inline-block"></span>
                <h4 class="font-bold text-slate-800 text-sm md:text-base">तह ३: उच्च दक्षता तथा बहु-चरणीय समस्याहरू (Higher Ability - ४ प्रश्नहरू)</h4>
              </div>
              <span class="text-xs font-bold px-2 py-0.5 rounded bg-purple-100 text-purple-800">४ अङ्कका बहुचरणीय प्रश्नहरू</span>
            </div>

            <div class="space-y-3 text-xs md:text-sm">
              <!-- 3.1 -->
              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-2">
                <h5 class="font-bold text-purple-950">प्रश्न ३.१: अण्डा व्यापारीको फुट्ने क्षति र नाफा निर्धारण (Breakage Loss)</h5>
                <p class="text-slate-700">एउटा व्यापारीले २०० वटा अण्डा रु. ३,००० मा खरिद गर्यो। ढुवानी गर्दा २० वटा अण्डा फुटे। बाँकी रहेका अण्डा प्रतिगोटा रु. २० का दरले बेच्दा उसलाई कति प्रतिशत नाफा वा नोक्सान भयो?</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>१. क्रय मूल्य:</strong><br>$C.P. = \\text{रु. } 3,000$<br>फुटेका अण्डा $= 20$
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>२. बिक्री मूल्य:</strong><br>बाँकी अण्डा $= 200 - 20 = 180$<br>$S.P. = 180 \\times 20 = \\text{रु. } 3,600$
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>३. नाफा प्रतिशत:</strong><br>नाफा $= 3600 - 3000 = \\text{रु. } 600$<br><strong>नाफा % $= \\frac{600}{3000} \\times 100\\% = 20\\%$</strong>
                  </div>
                </div>
              </div>

              <!-- 3.2 -->
              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-2">
                <h5 class="font-bold text-purple-950">प्रश्न ३.२: संयुक्त खाद्यान्न व्यापार (Combined Trade Analysis)</h5>
                <p class="text-slate-700">एक व्यापारीले रु. ४,००० को चामल र रु. २,००० को दाल किने। ढुवानीमा रु. ५०० खर्च भयो। उनले चामल रु. ४,८०० मा र दाल रु. २,४०० मा बेचे भने समग्र कारोबारमा नाफा वा नोक्सान प्रतिशत कति?</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>१. कुल क्रय मूल्य:</strong><br>$4000 + 2000 + 500 = \\text{रु. } 6,500$
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>२. कुल विक्रय मूल्य:</strong><br>$4800 + 2400 = \\text{रु. } 7,200$
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>३. कुल नाफा प्रतिशत:</strong><br>नाफा $= 7200 - 6500 = \\text{रु. } 700$<br><strong>नाफा % $= \\frac{700}{6500} \\times 100\\% \\approx 10.77\\%$</strong>
                  </div>
                </div>
              </div>

              <!-- 3.3 -->
              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-2">
                <h5 class="font-bold text-purple-950">प्रश्न ३.३: बिग्रेको सामान र नोक्सान न्यूनीकरण निर्णय विश्लेषण (Decision Making)</h5>
                <p class="text-slate-700">एउटा फलफूल व्यापारीले रु. १०,००० मा ५० केजी स्याउ किन्यो। तीमध्ये १० केजी स्याउ कुहिएर फाल्नुपर्यो। बाँकी स्याउलाई उसले प्रति केजी रु. २५० मा बेच्यो भने समग्रमा नाफा भयो कि नोक्सान?</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>१. क्रय मूल्य:</strong><br>$C.P. = \\text{रु. } 10,000$<br>कुहिएको $= 10$ केजी
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>२. बिक्री मूल्य:</strong><br>बाँकी $= 50 - 10 = 40$ केजी<br>$S.P. = 40 \\times 250 = \\text{रु. } 10,000$
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>३. निष्कर्ष:</strong><br>$S.P. = C.P. = \\text{रु. } 10,000$<br><strong>नाफा पनि छैन, नोक्सान पनि छैन (0%)</strong>
                  </div>
                </div>
              </div>

              <!-- 3.4 -->
              <div class="p-4 bg-purple-50/40 rounded-xl border border-purple-200 space-y-2">
                <h5 class="font-bold text-purple-950">प्रश्न ३.४: दुई वस्तुको व्यापार (एउटामा नाफा, अर्कोमा नोक्सान)</h5>
                <p class="text-slate-700">एक पसलेले दुईवटा फ्यान प्रत्येक रु. २,००० का दरले किने। पहिलो फ्यान १५% नाफामा र दोस्रो फ्यान १०% नोक्सानमा बेच्दा कुल कारोबारमा कति नाफा वा नोक्सान भयो?</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>१. फ्यान १ (नाफा):</strong><br>नाफा $= 2000 \\times 15\\% = \\text{रु. } 300$<br>$S.P._1 = \\text{रु. } 2,300$
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>२. फ्यान २ (नोक्सान):</strong><br>नोक्सान $= 2000 \\times 10\\% = \\text{रु. } 200$<br>$S.P._2 = \\text{रु. } 1,800$
                  </div>
                  <div class="bg-white p-2.5 rounded-lg border">
                    <strong>३. कुल विश्लेषण:</strong><br>कुल $C.P. = 4000$, कुल $S.P. = 4100$<br><strong>कुल नाफा $= \\text{रु. } 100$ ($2.5\\%$ नाफा)</strong>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH7 TAB 4: QUIZ ================= -->
        <div id="ch7-view-quiz" class="hidden space-y-6">
          <div class="bg-blue-50 border border-blue-200 p-4 rounded-2xl flex items-center justify-between">
            <div>
              <h4 class="font-black text-blue-900 text-sm md:text-base">पाठ ७: अन्तरक्रियात्मक आत्म-मूल्याङ्कन क्विज</h4>
              <p class="text-xs text-blue-700">५ वटा बहुवैकल्पिक प्रश्नहरू हल गरी आफ्नो बुझाइ तत्काल परीक्षण गर्नुहोस्</p>
            </div>
            <button onclick="resetQuizCh7()" class="text-xs font-bold bg-white text-blue-800 px-3 py-1.5 rounded-xl border border-blue-200 hover:bg-blue-50 shadow-xs cursor-pointer">
              🔄 पुनः सुरु गर्नुहोस्
            </button>
          </div>

          <!-- Q0 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न १: कुनै वस्तुको व्यापारमा नाफा हुने अवस्था कुन हो?</span>
              <span id="ch7-qbadge-0" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch7-qbtn-0-0" onclick="checkQuizCh7(0, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) क्रय मूल्य > विक्रय मूल्य ($C.P. > S.P.$)</button>
              <button id="ch7-qbtn-0-1" onclick="checkQuizCh7(0, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) विक्रय मूल्य > क्रय मूल्य ($S.P. > C.P.$)</button>
              <button id="ch7-qbtn-0-2" onclick="checkQuizCh7(0, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) क्रय मूल्य = विक्रय मूल्य ($C.P. = S.P.$)</button>
              <button id="ch7-qbtn-0-3" onclick="checkQuizCh7(0, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) विक्रय मूल्य = ० ($S.P. = 0$)</button>
            </div>
            <div id="ch7-qexp-0" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q1 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न २: रु. ५०० मा किनेको सामान रु. ५७५ मा बेच्दा कति प्रतिशत नाफा हुन्छ?</span>
              <span id="ch7-qbadge-1" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch7-qbtn-1-0" onclick="checkQuizCh7(1, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) १०%</button>
              <button id="ch7-qbtn-1-1" onclick="checkQuizCh7(1, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) १२%</button>
              <button id="ch7-qbtn-1-2" onclick="checkQuizCh7(1, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) १५%</button>
              <button id="ch7-qbtn-1-3" onclick="checkQuizCh7(1, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) २०%</button>
            </div>
            <div id="ch7-qexp-1" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q2 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ३: रु. १,२०० मा किनेको घडी १०% नोक्सानमा बेच्दा विक्रय मूल्य कति हुन्छ?</span>
              <span id="ch7-qbadge-2" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch7-qbtn-2-0" onclick="checkQuizCh7(2, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) रु. १,०८०</button>
              <button id="ch7-qbtn-2-1" onclick="checkQuizCh7(2, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) रु. १,१००</button>
              <button id="ch7-qbtn-2-2" onclick="checkQuizCh7(2, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) रु. ९८०</button>
              <button id="ch7-qbtn-2-3" onclick="checkQuizCh7(2, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) रु. १,३२०</button>
            </div>
            <div id="ch7-qexp-2" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q3 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ४: रु. ३,००० मा सामान किनी रु. २०० ढुवानी खर्च लाग्यो। सो सामान रु. ३,५२० मा बेच्दा नाफा % कति?</span>
              <span id="ch7-qbadge-3" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch7-qbtn-3-0" onclick="checkQuizCh7(3, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) ८%</button>
              <button id="ch7-qbtn-3-1" onclick="checkQuizCh7(3, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) १०%</button>
              <button id="ch7-qbtn-3-2" onclick="checkQuizCh7(3, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) १२%</button>
              <button id="ch7-qbtn-3-3" onclick="checkQuizCh7(3, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) १५%</button>
            </div>
            <div id="ch7-qexp-3" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

          <!-- Q4 -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800 text-sm">प्रश्न ५: १ दर्जन अण्डा रु. २४० मा किनेर प्रतिगोटा रु. २५ मा बेच्दा कति नाफा हुन्छ?</span>
              <span id="ch7-qbadge-4" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs md:text-sm">
              <button id="ch7-qbtn-4-0" onclick="checkQuizCh7(4, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) रु. ५०</button>
              <button id="ch7-qbtn-4-1" onclick="checkQuizCh7(4, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) रु. ६०</button>
              <button id="ch7-qbtn-4-2" onclick="checkQuizCh7(4, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) रु. ७०</button>
              <button id="ch7-qbtn-4-3" onclick="checkQuizCh7(4, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) रु. ४०</button>
            </div>
            <div id="ch7-qexp-4" class="hidden p-3 rounded-xl text-xs md:text-sm"></div>
          </div>

        </div>

      </div>
      <!-- ================= END OF CHAPTER 7 VIEW ================= -->
"""

if __name__ == '__main__':
    html = get_ch7_html()
    print("Generated Chapter 7 HTML! Length:", len(html))
