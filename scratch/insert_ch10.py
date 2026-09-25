import re
import shutil

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar
old_side = '''        <button onclick="alert('पाठ १० को विस्तृत नोट notes/10_parimiti_kshetraphal_aayatan.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ १०: परिमिति, क्षेत्रफल र आयतन</span>
          <span class="text-[10px] opacity-75">एकाइ ३</span>
        </button>'''

new_side = '''        <button id="side-ch-10" onclick="switchChapter(10)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium cursor-pointer">
          <span>पाठ १०: परिमिति, क्षेत्रफल र आयतन</span>
          <span class="text-[10px] opacity-75">एकाइ ३</span>
        </button>'''

html = html.replace(old_side, new_side)

# 2. Build Chapter 10 HTML view
ch10_view = '''
      <!-- ================= CHAPTER 10: PERIMETER, AREA AND VOLUME (परिमिति, क्षेत्रफल र आयतन) ================= -->
      <div id="chapter-view-10" class="hidden space-y-6">

        <!-- Chapter Header Banner -->
        <div class="p-6 md:p-8 rounded-3xl bg-gradient-to-r from-emerald-50 via-teal-50 to-cyan-50 border border-emerald-200/80 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-emerald-700 mb-1">एकाइ ३: क्षेत्रमिति (Unit 3: Mensuration — दोस्रो पाठ)</div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ १०: परिमिति, क्षेत्रफल र आयतन</h2>
          </div>
          <div class="flex flex-wrap items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ १११–१२७</span>
            <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-3 py-1 rounded-xl border border-emerald-200">अभ्यास १०.१, १०.२, १०.३, मिश्रित र परियोजना</span>
          </div>
        </div>

        <!-- Chapter 10 Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button id="ch10-tab-concepts" onclick="setTabCh10('concepts')" class="px-5 py-2.5 rounded-xl bg-emerald-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
            १. अवधारणा र क्षेत्रमिति ल्याब
          </button>
          <button id="ch10-tab-exercises" onclick="setTabCh10('exercises')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            २. सम्पूर्ण अभ्यास समाधान (१०.१, १०.२, १०.३ र मिश्रित)
          </button>
          <button id="ch10-tab-tiers" onclick="setTabCh10('tiers')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
          </button>
          <button id="ch10-tab-quiz" onclick="setTabCh10('quiz')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ४. आत्म-मूल्याङ्कन क्विज
          </button>
        </div>

        <!-- ================= CH10 TAB 1: CONCEPTS ================= -->
        <div id="ch10-view-concepts" class="space-y-6">

          <!-- Core Concepts Grid -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- Card 1: Perimeter -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-sm">१</span>
                <h3 class="font-bold text-slate-800 text-base">परिमिति (Perimeter — P)</h3>
              </div>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                कुनै बन्द समतलीय आकृतिको वरिपरिको बाहिरी घेराको जम्मा लम्बाइलाई <strong>परिमिति</strong> भनिन्छ। (एकाइ: $\\text{cm, m, ft}$)।
              </p>
              <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-xl space-y-1 text-xs">
                <div>• <strong>आयत:</strong> $P = 2(l + b)$</div>
                <div>• <strong>वर्ग:</strong> $P = 4l$</div>
                <div>• <strong>त्रिभुज:</strong> $P = a + b + c$</div>
              </div>
            </div>

            <!-- Card 2: Area -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center font-bold text-sm">२</span>
                <h3 class="font-bold text-slate-800 text-base">क्षेत्रफल (Area — A)</h3>
              </div>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                कुनै बन्द आकृतिले सतहमा ओगटेको ठाउँको परिमाणलाई <strong>क्षेत्रफल</strong> भनिन्छ। (एकाइ: $\\text{cm}^2, \\text{m}^2, \\text{ft}^2$)।
              </p>
              <div class="p-3 bg-teal-50 border border-teal-200 rounded-xl space-y-1 text-xs">
                <div>• <strong>आयत:</strong> $A = l \\times b \\implies l = \\frac{A}{b}$</div>
                <div>• <strong>वर्ग:</strong> $A = l^2 \\implies l = \\sqrt{A}$</div>
                <div>• <strong>छाया परेको भाग:</strong> बाहिरी $-$ भित्री भाग</div>
              </div>
            </div>

            <!-- Card 3: Volume & Capacity -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-cyan-100 text-cyan-700 flex items-center justify-center font-bold text-sm">३</span>
                <h3 class="font-bold text-slate-800 text-base">आयतन र क्षमता (Volume & Capacity)</h3>
              </div>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                कुनै ३-D ठोस वस्तुले अन्तरिक्षमा ओगटेको स्थानलाई <strong>आयतन</strong> भनिन्छ। (एकाइ: $\\text{cm}^3, \\text{m}^3$)।
              </p>
              <div class="p-3 bg-cyan-50 border border-cyan-200 rounded-xl space-y-1 text-xs">
                <div>• <strong>षट्मुख:</strong> $V = l \\times b \\times h$</div>
                <div>• <strong>घन:</strong> $V = l^3 \\implies l = \\sqrt[3]{V}$</div>
                <div>• <strong>क्षमता:</strong> $1\\text{ m}^3 = 1000\\text{ L}$, $1000\\text{ cm}^3 = 1\\text{ L}$</div>
              </div>
            </div>
          </div>

          <!-- Master Formula Table & Circle Section -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <h3 class="font-bold text-slate-800 text-sm md:text-base flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span>
              वृत्तको आधारभूत परिचय तथा मुख्य अङ्गहरू (Circle Anatomy)
            </h3>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs md:text-sm">
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">व्यास र अर्धव्यास</span>
                <span class="font-bold text-slate-900 font-mono text-sm">$d = 2r \\iff r = \\frac{d}{2}$</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">वृत्तको परिधि (Circumference)</span>
                <span class="font-bold text-slate-900 font-mono text-sm">$C = 2\\pi r = \\pi d$</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">वृत्तको जीवा (Chord)</span>
                <span class="font-bold text-slate-900 text-xs font-sans">परिधिका दुई बिन्दु जोड्ने रेखा</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">वृत्तको चाप (Arc)</span>
                <span class="font-bold text-slate-900 text-xs font-sans">परिधिको कुनै एक खण्ड</span>
              </div>
            </div>
          </div>

          <!-- Interactive Mensuration Lab / Simulator -->
          <div class="p-5 md:p-6 bg-gradient-to-br from-teal-950 via-emerald-900 to-slate-900 text-white rounded-3xl shadow-xl space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-3 border-b border-white/15 pb-4">
              <div>
                <span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-400 text-slate-950 inline-block mb-1">प्रत्यक्ष डिजिटल ल्याब</span>
                <h3 class="text-lg md:text-xl font-black">क्षेत्रमिति प्रत्यक्ष सिमुलेटर (2D/3D Mensuration Lab)</h3>
              </div>
              <div class="flex items-center gap-1 bg-white/10 p-1 rounded-xl text-xs font-bold">
                <button id="ch10-btn-rect" onclick="setCh10Shape('rect')" class="px-3 py-1.5 rounded-lg bg-emerald-500 text-white transition cursor-pointer">आयत</button>
                <button id="ch10-btn-sq" onclick="setCh10Shape('square')" class="px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer">वर्ग</button>
                <button id="ch10-btn-cuboid" onclick="setCh10Shape('cuboid')" class="px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer">षट्मुख</button>
                <button id="ch10-btn-cube" onclick="setCh10Shape('cube')" class="px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer">घन</button>
              </div>
            </div>

            <!-- Dynamic Inputs -->
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3" id="ch10-input-grid">
              <div>
                <label id="ch10-lbl-l" class="block text-xs text-emerald-200 mb-1 font-semibold">लम्बाइ (Length - l):</label>
                <input id="ch10-in-l" type="number" step="any" value="20" oninput="runCh10Calc()" class="w-full bg-white/10 border border-white/20 rounded-xl px-3.5 py-2 text-white font-mono font-bold focus:outline-none focus:ring-2 focus:ring-emerald-400 text-base">
              </div>
              <div id="ch10-box-b">
                <label class="block text-xs text-emerald-200 mb-1 font-semibold">चौडाइ (Breadth - b):</label>
                <input id="ch10-in-b" type="number" step="any" value="8" oninput="runCh10Calc()" class="w-full bg-white/10 border border-white/20 rounded-xl px-3.5 py-2 text-white font-mono font-bold focus:outline-none focus:ring-2 focus:ring-emerald-400 text-base">
              </div>
              <div id="ch10-box-h" class="hidden">
                <label class="block text-xs text-emerald-200 mb-1 font-semibold">उचाइ (Height - h):</label>
                <input id="ch10-in-h" type="number" step="any" value="5" oninput="runCh10Calc()" class="w-full bg-white/10 border border-white/20 rounded-xl px-3.5 py-2 text-white font-mono font-bold focus:outline-none focus:ring-2 focus:ring-emerald-400 text-base">
              </div>
              <div>
                <label class="block text-xs text-emerald-200 mb-1 font-semibold">एकाइ (Unit):</label>
                <select id="ch10-in-unit" onchange="runCh10Calc()" class="w-full bg-slate-800 border border-white/20 rounded-xl px-3.5 py-2 text-white font-bold focus:outline-none focus:ring-2 focus:ring-emerald-400 text-sm cursor-pointer">
                  <option value="cm" selected>सेन्टिमिटर (cm)</option>
                  <option value="m">मिटर (m)</option>
                  <option value="ft">फिट (ft)</option>
                </select>
              </div>
            </div>

            <!-- Presets -->
            <div class="flex flex-wrap items-center gap-2 pt-1 text-xs">
              <span class="text-emerald-200 font-semibold">द्रुत नमुनाहरू:</span>
              <button onclick="setCh10Preset('rect', 20, 8, 0, 'cm')" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">उदा: २० $\\times$ ८ cm आयत</button>
              <button onclick="setCh10Preset('square', 25, 25, 0, 'cm')" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">रुमाल: २५ cm वर्ग</button>
              <button onclick="setCh10Preset('cuboid', 55, 40, 25, 'cm')" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">बाकस: ५५ $\\times$ ४० $\\times$ २५ cm</button>
              <button onclick="setCh10Preset('cuboid', 2.5, 2, 1.2, 'm')" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">ट्याङ्की: २.५ $\\times$ २ $\\times$ १.२ m</button>
              <button onclick="setCh10Preset('cube', 8, 8, 8, 'cm')" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">घन: ८ cm किनारा</button>
            </div>

            <!-- Result Box -->
            <div id="ch10-calc-res" class="bg-black/30 border border-white/15 rounded-2xl p-4 space-y-3">
              <!-- Dynamically populated by runCh10Calc() -->
            </div>
          </div>

        </div>

        <!-- ================= CH10 TAB 2: EXERCISES ================= -->
        <div id="ch10-view-exercises" class="hidden space-y-6">

          <!-- Sub-section Switcher -->
          <div class="flex flex-wrap gap-2 border-b border-slate-200 pb-3">
            <button id="ch10-ex-btn-sec1" onclick="setExerciseCh10('sec1')" class="px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-emerald-600 text-white shadow-xs transition cursor-pointer">
              खण्ड १: अभ्यास १०.१ (परिमिति — प्रश्न १ देखि ११ र परियोजना)
            </button>
            <button id="ch10-ex-btn-sec2" onclick="setExerciseCh10('sec2')" class="px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-600 hover:bg-slate-100 transition cursor-pointer">
              खण्ड २: अभ्यास १०.२ (क्षेत्रफल — प्रश्न १ देखि ६ र परियोजना)
            </button>
            <button id="ch10-ex-btn-sec3" onclick="setExerciseCh10('sec3')" class="px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-600 hover:bg-slate-100 transition cursor-pointer">
              खण्ड ३: अभ्यास १०.३ (आयतन — प्रश्न १ देखि ७ र परियोजना)
            </button>
            <button id="ch10-ex-btn-sec4" onclick="setExerciseCh10('sec4')" class="px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-600 hover:bg-slate-100 transition cursor-pointer">
              खण्ड ४: पाठ १० मिश्रित अभ्यास (प्रश्न १ देखि ११)
            </button>
          </div>

          <!-- Section 1: Exercise 10.1 (Perimeter) -->
          <div id="ch10-ex-sec1" class="space-y-4">
            <!-- Q1 Card -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                <h4 class="font-bold text-slate-900 text-sm md:text-base">प्रश्न १: साँचो वा झुटो छुट्याउनुहोस् (True / False)</h4>
                <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-0.5 rounded-lg">७ उप-प्रश्नहरू</span>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span class="font-bold text-emerald-700">(क)</span> लम्बाइ र चौडाइ जोडेर आयतको परिमिति निकालिन्छ।
                  <div class="mt-1"><strong class="text-rose-700 bg-rose-50 px-2 py-0.5 rounded border border-rose-200">झुटो (False)</strong> <span class="text-slate-500 text-xs">कारण: $P = 2(l + b)$ हुन्छ, २ ले गुणन गर्नुपर्छ।</span></div>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span class="font-bold text-emerald-700">(ख)</span> $15\\text{ cm}$ लम्बाइ र $10\\text{ cm}$ चौडाइ भएको पुस्तकको परिमिति $50\\text{ cm}$ हुन्छ।
                  <div class="mt-1"><strong class="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">साँचो (True)</strong> <span class="text-slate-500 text-xs">कारण: $2(15 + 10) = 50\\text{ cm}$।</span></div>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span class="font-bold text-emerald-700">(ग)</span> $6\\text{ m}$ लम्बाइ र $2\\text{ m}$ चौडाइ भएको टेबलको परिमिति $12\\text{ m}$ हुन्छ।
                  <div class="mt-1"><strong class="text-rose-700 bg-rose-50 px-2 py-0.5 rounded border border-rose-200">झुटो (False)</strong> <span class="text-slate-500 text-xs">कारण: $2(6 + 2) = 16\\text{ m}$ हुन्छ ($12$ त क्षेत्रफल हो)।</span></div>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span class="font-bold text-emerald-700">(घ)</span> $2\\text{ m}$ लम्बाइ र $1\\text{ m}$ चौडाइ भएको आयतको परिमिति $6\\text{ m}$ हुन्छ।
                  <div class="mt-1"><strong class="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">साँचो (True)</strong> <span class="text-slate-500 text-xs">कारण: $2(2 + 1) = 6\\text{ m}$।</span></div>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span class="font-bold text-emerald-700">(ङ)</span> वर्गको लम्बाइलाई ४ ले गुणन गरेर वर्गको परिमिति निकालिन्छ।
                  <div class="mt-1"><strong class="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">साँचो (True)</strong> <span class="text-slate-500 text-xs">कारण: $P = 4l$।</span></div>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span class="font-bold text-emerald-700">(च)</span> $5\\text{ m}$ लम्बाइ भएको वर्गाकार रुमालको परिमिति $25\\text{ m}$ हुन्छ।
                  <div class="mt-1"><strong class="text-rose-700 bg-rose-50 px-2 py-0.5 rounded border border-rose-200">झुटो (False)</strong> <span class="text-slate-500 text-xs">कारण: $P = 4 \\times 5 = 20\\text{ m}$ हुनुपर्छ।</span></div>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 md:col-span-2">
                  <span class="font-bold text-emerald-700">(छ)</span> $4\\text{ m}$ परिमिति भएको वर्गको लम्बाइ $1\\text{ m}$ हुन्छ।
                  <div class="mt-1"><strong class="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">साँचो (True)</strong> <span class="text-slate-500 text-xs">कारण: $l = \\frac{4}{4} = 1\\text{ m}$।</span></div>
                </div>
              </div>
            </div>

            <!-- Q2 & Q3 Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Q2 -->
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न २: आयत तथा वर्गको परिमिति गणना</h4>
                <div class="space-y-1.5 text-slate-700">
                  <div><strong>(क)</strong> $AB = 8\\text{ cm}, BC = 5\\text{ cm} \\implies 2(8+5) =$ <span class="text-emerald-700 font-bold">26 cm</span></div>
                  <div><strong>(ख)</strong> $AB = 15\\text{ m}, BC = 5\\text{ m} \\implies 2(15+5) =$ <span class="text-emerald-700 font-bold">40 m</span></div>
                  <div><strong>(ग)</strong> $PQ = 9\\text{ cm}, QR = 6\\text{ cm} \\implies 2(9+6) =$ <span class="text-emerald-700 font-bold">30 cm</span></div>
                  <div><strong>(घ)</strong> $XY = 12.5\\text{ ft}, YZ = 7\\text{ ft} \\implies 2(12.5+7) =$ <span class="text-emerald-700 font-bold">39 ft</span></div>
                  <div><strong>(ङ)</strong> $AB = 28\\text{ cm}, BC = 15\\text{ cm} \\implies 2(28+15) =$ <span class="text-emerald-700 font-bold">86 cm</span></div>
                  <div><strong>(च)</strong> $AB = BC = 35\\text{ ft}$ (वर्ग) $\\implies 4 \\times 35 =$ <span class="text-emerald-700 font-bold">140 ft</span></div>
                  <div><strong>(छ)</strong> $QR = RS = 40\\text{ m}$ (वर्ग) $\\implies 4 \\times 40 =$ <span class="text-emerald-700 font-bold">160 m</span></div>
                </div>
              </div>

              <!-- Q3 -->
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न ३: चित्रका नापको परिमिति</h4>
                <div class="space-y-1.5 text-slate-700">
                  <div><strong>(क)</strong> $l = 3\\text{ cm}, b = 2\\text{ cm} \\implies 2(3+2) =$ <span class="text-emerald-700 font-bold">10 cm</span></div>
                  <div><strong>(ख)</strong> $l = 5\\text{ cm}, b = 3\\text{ cm} \\implies 2(5+3) =$ <span class="text-emerald-700 font-bold">16 cm</span></div>
                  <div><strong>(ग)</strong> वर्ग $l = 4.5\\text{ cm} \\implies 4 \\times 4.5 =$ <span class="text-emerald-700 font-bold">18 cm</span></div>
                  <div><strong>(घ)</strong> $l = 18.5\\text{ ft}, b = 13.5\\text{ ft} \\implies 2(18.5+13.5) =$ <span class="text-emerald-700 font-bold">64 ft</span></div>
                </div>
              </div>
            </div>

            <!-- Q4 to Q11 Practical Problems -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">प्रश्न ४ देखि ११ सम्मका व्यावहारिक समस्या समाधान</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ४ (तौलिया):</strong> $l = 190\\text{ cm}, b = 110\\text{ cm}$<br>
                  $P = 2(190 + 110) = 2 \\times 300 =$ <strong class="text-emerald-700">600 cm (६ m)</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ५ (खेत):</strong> $l = 27\\text{ ft}, b = 22\\text{ ft}$<br>
                  $P = 2(27 + 22) = 2 \\times 49 =$ <strong class="text-emerald-700">98 ft</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ६ (रुमाल):</strong> $l = 25\\text{ cm}$<br>
                  $P = 4 \\times 25 =$ <strong class="text-emerald-700">100 cm (१ m)</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ७ (चौर):</strong> $P = 360\\text{ m}, b = 60\\text{ m}$<br>
                  $l = \\frac{360}{2} - 60 = 180 - 60 =$ <strong class="text-emerald-700">120 m</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ८ (पलङ):</strong> $P = 22\\text{ ft}, l = 6\\text{ ft}$<br>
                  $b = \\frac{22}{2} - 6 = 11 - 6 =$ <strong class="text-emerald-700">5 ft</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ९ (जग्गा):</strong> $l = 2x, b = x, P = 42\\text{ m}$<br>
                  $6x = 42 \\implies x = 7\\text{ m}$<br>
                  लम्बाइ $= 2 \\times 7 =$ <strong class="text-emerald-700">14 m</strong>, चौडाइ $= $ <strong class="text-emerald-700">7 m</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न १० (वर्ग):</strong> $P = 84\\text{ cm}$<br>
                  $l = \\frac{84}{4} =$ <strong class="text-emerald-700">21 cm</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ११ (रुखहरू):</strong> चौर वरिपरि ३४० रुखहरू<br>
                  लम्बाइतर्फ रुख सङ्ख्या $= \\frac{340}{4} =$ <strong class="text-emerald-700">85 ओटा रुखहरू</strong>
                </div>
              </div>
            </div>

            <!-- Project Work 10.1 -->
            <div class="p-4 bg-emerald-50 rounded-2xl border border-emerald-200 text-xs md:text-sm">
              <strong class="text-emerald-950 block mb-1">परियोजना कार्य (भलिबल कोर्ट डोरी मापन):</strong>
              भलिबल कोर्टको लम्बाइ $18\\text{ m}$ र चौडाइ $9\\text{ m}$ हुन्छ। परिमिति $P = 2(18 + 9) = 2 \\times 27 = \\mathbf{54\\text{ m}}$। अतः बाहिरी घेरामा डोरी राख्न ५४ मिटर डोरी आवश्यक पर्छ।
            </div>
          </div>

          <!-- Section 2: Exercise 10.2 (Area) -->
          <div id="ch10-ex-sec2" class="hidden space-y-4">
            <!-- Q1 Fill in blanks -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न १: खाली ठाउँ भर्नुहोस्</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">(क) लम्बाइलाई वर्ग गरेर: <strong class="text-emerald-700">क्षेत्रफल</strong> निकालिन्छ।</div>
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">(ख) लम्बाइ/चौडाइ cm भए क्षेत्रफल: <strong class="text-emerald-700">cm²</strong> हुन्छ।</div>
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">(ग) ३ m × २ m कागजले: <strong class="text-emerald-700">6 m²</strong> ठाउँ ओगट्छ।</div>
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">(घ) ५ cm × ३ cm कागजको क्षेत्रफल: <strong class="text-emerald-700">15 cm²</strong> हुन्छ।</div>
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">(ङ) २ m लम्बाइ भएको वर्गको क्षेत्रफल: <strong class="text-emerald-700">4 m²</strong> हुन्छ।</div>
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">(च) अनियमित वस्तुको क्षेत्रफल: <strong class="text-emerald-700">ग्राफपेपर (कोठा गणना)</strong> विधिद्वारा निकालिन्छ।</div>
              </div>
            </div>

            <!-- Q3 & Q4 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न ३: क्षेत्रफल निकाल्नुहोस्</h4>
                <div><strong>(क)</strong> $5 \\times 3 =$ <strong class="text-emerald-700">15 cm²</strong></div>
                <div><strong>(ख)</strong> $18 \\times 7 =$ <strong class="text-emerald-700">126 cm²</strong></div>
                <div><strong>(ग)</strong> वर्ग: $19^2 =$ <strong class="text-emerald-700">361 cm²</strong></div>
                <div><strong>(घ)</strong> $14.2 \\times 11.5 =$ <strong class="text-emerald-700">163.3 m² (वा ft²)</strong></div>
              </div>
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न ४: लम्बाइ वा चौडाइ पत्ता लगाउनुहोस्</h4>
                <div><strong>(क)</strong> $l = 7\\text{ ft}, A = 21\\text{ ft}^2 \\implies b = \\frac{21}{7} =$ <strong class="text-emerald-700">3 ft</strong></div>
                <div><strong>(ख)</strong> $l = 18\\text{ cm}, A = 90\\text{ cm}^2 \\implies b = \\frac{90}{18} =$ <strong class="text-emerald-700">5 cm</strong></div>
                <div><strong>(ग)</strong> $b = 3.2\\text{ m}, A = 38.4\\text{ m}^2 \\implies l = \\frac{38.4}{3.2} =$ <strong class="text-emerald-700">12 m</strong></div>
                <div><strong>(घ)</strong> $b = 1\\text{ ft}, A = 15\\text{ ft}^2 \\implies l = \\frac{15}{1} =$ <strong class="text-emerald-700">15 ft</strong></div>
              </div>
            </div>

            <!-- Q5 & Q6 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न ५: वर्गको लम्बाइ ($l = \\sqrt{A}$)</h4>
                <div><strong>(क)</strong> $A = 1\\text{ cm}^2 \\implies l =$ <strong class="text-emerald-700">1 cm</strong></div>
                <div><strong>(ख)</strong> $A = 121\\text{ ft}^2 \\implies l =$ <strong class="text-emerald-700">11 ft</strong></div>
                <div><strong>(ग)</strong> $A = 196\\text{ m}^2 \\implies l =$ <strong class="text-emerald-700">14 m</strong></div>
                <div><strong>(घ)</strong> $A = 625\\text{ m}^2 \\implies l =$ <strong class="text-emerald-700">25 m</strong></div>
              </div>
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न ६: छाया परेको भागको क्षेत्रफल</h4>
                <div><strong>(क)</strong> बाहिरी $20$ $-$ भित्री $2 =$ <strong class="text-emerald-700">18 cm²</strong></div>
                <div><strong>(ख)</strong> बाहिरी $80$ $-$ भित्री $15 =$ <strong class="text-emerald-700">65 cm²</strong></div>
                <div><strong>(ग)</strong> बाहिरी $30$ $-$ भित्री $7 =$ <strong class="text-emerald-700">23 cm²</strong></div>
                <div><strong>(घ)</strong> बाहिरी $75$ $-$ भित्री $30 =$ <strong class="text-emerald-700">45 cm²</strong></div>
              </div>
            </div>
          </div>

          <!-- Section 3: Exercise 10.3 (Volume) -->
          <div id="ch10-ex-sec3" class="hidden space-y-4">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न १: चित्रका वस्तुको आयतन</h4>
                <div><strong>(क)</strong> $5 \\times 4 \\times 3 =$ <strong class="text-emerald-700">60 cm³</strong></div>
                <div><strong>(ख)</strong> $7 \\times 2 \\times 1 =$ <strong class="text-emerald-700">14 cm³</strong></div>
                <div><strong>(ग)</strong> घन $8^3 =$ <strong class="text-emerald-700">512 cm³</strong></div>
                <div><strong>(घ)</strong> $13.5 \\times 6 \\times 5 =$ <strong class="text-emerald-700">405 cm³ (वा m³)</strong></div>
              </div>
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न २: षट्मुखको आयतन</h4>
                <div><strong>(क)</strong> $12 \\times 8 \\times 4 =$ <strong class="text-emerald-700">384 cm³</strong></div>
                <div><strong>(ख)</strong> $25 \\times 15 \\times 5 =$ <strong class="text-emerald-700">1,875 ft³</strong> <span class="text-slate-400 text-[10px]">(पु: ३७५)</span></div>
                <div><strong>(ग)</strong> $3.5 \\times 2.2 \\times 2 =$ <strong class="text-emerald-700">15.4 m³</strong></div>
                <div><strong>(घ)</strong> $16 \\times 10.5 \\times 5.5 =$ <strong class="text-emerald-700">924 cm³</strong></div>
              </div>
              <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs md:text-sm">
                <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2">प्रश्न ३: घनको आयतन ($V = l^3$)</h4>
                <div><strong>(क)</strong> $1^3 =$ <strong class="text-emerald-700">1 m³</strong></div>
                <div><strong>(ख)</strong> $7^3 =$ <strong class="text-emerald-700">343 cm³</strong></div>
                <div><strong>(ग)</strong> $16^3 =$ <strong class="text-emerald-700">4,096 ft³</strong></div>
                <div><strong>(घ)</strong> $29^3 =$ <strong class="text-emerald-700">24,389 m³</strong></div>
              </div>
            </div>

            <!-- Q4 to Q7 Word Problems -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">प्रश्न ४ देखि ७ सम्मका आयतन समस्याहरू</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ४ (आयताकार बाकस):</strong> $55 \\times 40 \\times 25 =$ <strong class="text-emerald-700 font-mono">55,000 cm³</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ५ (घनाकार बाकस):</strong> $17^3 = 17 \\times 17 \\times 17 =$ <strong class="text-emerald-700 font-mono">4,913 cm³</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ६ (घनाकार वस्तु):</strong> $V = 64\\text{ m}^3 \\implies l = \\sqrt[3]{64} =$ <strong class="text-emerald-700 font-mono">4 m</strong>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <strong>प्रश्न ७ (षट्मुख):</strong> $V = 100\\text{ ft}^3, h = 2\\text{ ft}, l = 2x, b = x$<br>
                  $4x^2 = 100 \\implies x^2 = 25 \\implies x = 5\\text{ ft}$<br>
                  चौडाइ $= $ <strong class="text-emerald-700">5 ft</strong>, लम्बाइ $= $ <strong class="text-emerald-700">10 ft</strong>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 4: Mixed Review (मिश्रित अभ्यास) -->
          <div id="ch10-ex-sec4" class="hidden space-y-4">
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                <h4 class="font-bold text-slate-900 text-sm md:text-base">पाठ १० मिश्रित अभ्यासका सम्पूर्ण समाधान (पृष्ठ १२६–१२७)</h4>
                <span class="text-xs bg-indigo-100 text-indigo-800 font-bold px-2 py-0.5 rounded">११ प्रश्नहरू</span>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न २ (तौलिया):</strong> $l = 120\\text{ cm}, b = 80\\text{ cm}$<br>
                  • परिमिति: $2(120+80) =$ <strong class="text-emerald-700 font-mono">400 cm</strong><br>
                  • क्षेत्रफल: $120 \\times 80 =$ <strong class="text-emerald-700 font-mono">9,600 cm²</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ३ (खेत):</strong> $A = 85\\text{ ft}^2, b = 5\\text{ ft}$<br>
                  • लम्बाइ: $\\frac{85}{5} = 17\\text{ ft}$<br>
                  • परिमिति: $2(17+5) =$ <strong class="text-emerald-700 font-mono">44 ft</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ४ (वर्ग):</strong> $l = 45\\text{ cm}$<br>
                  • परिमिति: $4 \\times 45 =$ <strong class="text-emerald-700 font-mono">180 cm</strong><br>
                  • क्षेत्रफल: $45^2 =$ <strong class="text-emerald-700 font-mono">2,025 cm²</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ५ (चौर):</strong> $P = 280\\text{ m}, b = 50\\text{ m}$<br>
                  • लम्बाइ: $140 - 50 =$ <strong class="text-emerald-700 font-mono">90 m</strong><br>
                  • क्षेत्रफल: $90 \\times 50 =$ <strong class="text-emerald-700 font-mono">4,500 m²</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ६ (वर्ग):</strong> $A = 196\\text{ cm}^2$<br>
                  • लम्बाइ: $\\sqrt{196} =$ <strong class="text-emerald-700 font-mono">14 cm</strong><br>
                  • परिमिति: $4 \\times 14 =$ <strong class="text-emerald-700 font-mono">56 cm</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ७ (जग्गा):</strong> $l = 2x, b = x, A = 648\\text{ m}^2$<br>
                  $2x^2 = 648 \\implies x = 18\\text{ m}$<br>
                  लम्बाइ $= $ <strong class="text-emerald-700 font-mono">36 m</strong>, चौडाइ $= $ <strong class="text-emerald-700 font-mono">18 m</strong>, $P =$ <strong class="text-emerald-700 font-mono">108 m</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ८ (घनाकार वस्तु):</strong> $V = 1331\\text{ cm}^3$<br>
                  • लम्बाइ: $\\sqrt[3]{1331} =$ <strong class="text-emerald-700 font-mono">11 cm</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ९ (षट्मुख):</strong> $V = 250\\text{ m}^3, h = 5\\text{ m}, l = 2x, b = x$<br>
                  $10x^2 = 250 \\implies x = 5\\text{ m}$<br>
                  लम्बाइ $= $ <strong class="text-emerald-700 font-mono">10 m</strong>, चौडाइ $= $ <strong class="text-emerald-700 font-mono">5 m</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न १० (वर्ग र आयत बराबर क्षेत्रफल):</strong> $A = 16\\text{ m}^2$<br>
                  $l_{\\text{वर्ग}} = 4\\text{ m} \\implies l_{\\text{आयत}} = 8\\text{ m}$<br>
                  आयतको चौडाइ $= \\frac{16}{8} =$ <strong class="text-emerald-700 font-mono">2 m</strong>
                </div>
                <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                  <strong>प्रश्न ११ (वृत्तको नामावली):</strong><br>
                  केन्द्रबिन्दु, अर्धव्यास ($r$), व्यास ($d = 2r$), परिधि ($C$), जीवा (Chord), चाप (Arc)।
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- ================= CH10 TAB 3: TIERS ================= -->
        <div id="ch10-view-tiers" class="hidden space-y-4">
          <!-- Tier 1 -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">तह १: ज्ञान तथा बोध तह (Knowledge & Understanding)</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१. परिमिति र क्षेत्रफलको भिन्नता:</strong> परिमिति बाहिरी घेराको लम्बाइ हो (cm, m); क्षेत्रफल ओगटेको सतह हो (cm², m²)।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>२. वर्गको सूत्र:</strong> परिमिति $P = 4l$ र क्षेत्रफल $A = l^2$।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>३. षट्मुख र घनको आयतन:</strong> षट्मुख $V = l \\times b \\times h$, घन $V = l^3$।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>४. लिटर र घनमिटर:</strong> $1\\text{ m}^3 = 1000\\text{ लिटर}$ हुन्छ।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>५. व्यास र अर्धव्यास:</strong> व्यास अर्धव्यासको दोब्बर हुन्छ ($d = 2r$ वा $r = d/2$)।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>६. आयतको लम्बाइ सूत्र:</strong> $l = \\frac{P}{2} - b$।
              </div>
            </div>
          </div>

          <!-- Tier 2 -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">तह २: बोध तथा प्रयोग तह (Understanding & Application)</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>७. १२ cm वर्ग:</strong> $P = 4 \\times 12 =$ <strong class="text-emerald-700">48 cm</strong>, $A = 12^2 =$ <strong class="text-emerald-700">144 cm²</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>८. कोठामा कार्पेट खर्च:</strong> $8 \\times 6 = 48\\text{ m}^2$, खर्च $= 48 \\times 300 =$ <strong class="text-emerald-700">रु. १४,४००</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>९. १००० इँटाको आयतन:</strong> $20 \\times 10 \\times 5 = 1000\\text{ cm}^3$, १००० ओटाको $= 1,000,000\\text{ cm}^3 =$ <strong class="text-emerald-700">1 m³</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१०. वृत्तको परिधि:</strong> $r = 7\\text{ cm} \\implies C = 2 \\times \\frac{22}{7} \\times 7 =$ <strong class="text-emerald-700">44 cm</strong>
              </div>
            </div>
          </div>

          <!-- Tier 3 -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">तह ३: उच्च दक्षता बहु-चरणीय समस्याहरू (Higher Ability)</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१३. ट्याङ्की क्षमता र खपत:</strong> $2.5 \\times 2 \\times 1.2 = 6\\text{ m}^3 = 6000\\text{ लिटर}$। ५ जनाले दैनिक ६०० लि खपत गर्दा भरिएको पानी <strong class="text-emerald-700">१० दिन</strong> पुग्छ।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१४. बगैँचाको बाटो:</strong> बाहिरी $34 \\times 24 = 816\\text{ m}^2$, भित्री $30 \\times 20 = 600\\text{ m}^2$। बाटोको क्षेत्रफल $= 816 - 600 =$ <strong class="text-emerald-700">216 m²</strong>।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१५. खेत घेरा र क्षेत्रफल:</strong> आयत क्षेत्रफल $= 800\\text{ m}^2$, वर्ग क्षेत्रफल $= 30^2 = 900\\text{ m}^2$। वर्ग घेर्दा <strong class="text-emerald-700">100 m² बढी</strong> क्षेत्रफल घेरिन्छ।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१६. टायल सङ्ख्या:</strong> भुइँ $= 240,000\\text{ cm}^2$, १ टायल $= 2,000\\text{ cm}^2$। जम्मा टायल $= \\frac{240000}{2000} =$ <strong class="text-emerald-700">120 ओटा</strong>।
              </div>
            </div>
          </div>
        </div>

        <!-- ================= CH10 TAB 4: QUIZ ================= -->
        <div id="ch10-view-quiz" class="hidden space-y-4">
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
            <div>
              <h4 class="font-bold text-slate-900 text-sm md:text-base">पाठ १० आत्म-मूल्याङ्कन क्विज</h4>
              <p class="text-xs text-slate-500">५ ओटा परीक्षा केन्द्रित वस्तुगत प्रश्नहरू</p>
            </div>
            <button onclick="resetQuizCh10()" class="px-3.5 py-1.5 rounded-xl border border-slate-300 text-xs font-bold text-slate-700 hover:bg-slate-50 cursor-pointer">पुनः सुरु गर्नुहोस्</button>
          </div>

          <div class="space-y-3">
            <!-- Q1 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-emerald-700">प्रश्न १</span>
                <span id="ch10-qbadge-0" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">लम्बाइ ८ cm र चौडाइ ५ cm भएको आयतको परिमिति कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch10-qbtn-0-0" onclick="checkQuizCh10(0, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) 13 cm</button>
                <button id="ch10-qbtn-0-1" onclick="checkQuizCh10(0, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) 26 cm</button>
                <button id="ch10-qbtn-0-2" onclick="checkQuizCh10(0, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) 40 cm</button>
                <button id="ch10-qbtn-0-3" onclick="checkQuizCh10(0, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) 20 cm</button>
              </div>
              <div id="ch10-qexp-0" class="hidden"></div>
            </div>

            <!-- Q2 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-emerald-700">प्रश्न २</span>
                <span id="ch10-qbadge-1" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">भुजाको लम्बाइ ९ cm भएको वर्गको क्षेत्रफल कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch10-qbtn-1-0" onclick="checkQuizCh10(1, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) 36 cm²</button>
                <button id="ch10-qbtn-1-1" onclick="checkQuizCh10(1, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) 81 cm²</button>
                <button id="ch10-qbtn-1-2" onclick="checkQuizCh10(1, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) 18 cm²</button>
                <button id="ch10-qbtn-1-3" onclick="checkQuizCh10(1, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) 72 cm²</button>
              </div>
              <div id="ch10-qexp-1" class="hidden"></div>
            </div>

            <!-- Q3 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-emerald-700">प्रश्न ३</span>
                <span id="ch10-qbadge-2" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">लम्बाइ ६ m, चौडाइ ४ m र उचाइ ३ m भएको षट्मुखको आयतन कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch10-qbtn-2-0" onclick="checkQuizCh10(2, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) 26 m³</button>
                <button id="ch10-qbtn-2-1" onclick="checkQuizCh10(2, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) 48 m³</button>
                <button id="ch10-qbtn-2-2" onclick="checkQuizCh10(2, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) 72 m³</button>
                <button id="ch10-qbtn-2-3" onclick="checkQuizCh10(2, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) 144 m³</button>
              </div>
              <div id="ch10-qexp-2" class="hidden"></div>
            </div>

            <!-- Q4 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-emerald-700">प्रश्न ४</span>
                <span id="ch10-qbadge-3" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">२ घनमिटर ($2\\text{ m}^3$) आयतन भएको पानीको ट्याङ्कीमा कति लिटर पानी अट्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch10-qbtn-3-0" onclick="checkQuizCh10(3, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) २०० लिटर</button>
                <button id="ch10-qbtn-3-1" onclick="checkQuizCh10(3, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) १,००० लिटर</button>
                <button id="ch10-qbtn-3-2" onclick="checkQuizCh10(3, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) २,००० लिटर</button>
                <button id="ch10-qbtn-3-3" onclick="checkQuizCh10(3, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) २०,००० लिटर</button>
              </div>
              <div id="ch10-qexp-3" class="hidden"></div>
            </div>

            <!-- Q5 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-emerald-700">प्रश्न ५</span>
                <span id="ch10-qbadge-4" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">वृत्तको अर्धव्यास $14\\text{ cm}$ भए व्यास कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch10-qbtn-4-0" onclick="checkQuizCh10(4, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) 7 cm</button>
                <button id="ch10-qbtn-4-1" onclick="checkQuizCh10(4, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) 21 cm</button>
                <button id="ch10-qbtn-4-2" onclick="checkQuizCh10(4, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) 28 cm</button>
                <button id="ch10-qbtn-4-3" onclick="checkQuizCh10(4, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) 44 cm</button>
              </div>
              <div id="ch10-qexp-4" class="hidden"></div>
            </div>
          </div>
        </div>

      </div>
      <!-- ================= END CHAPTER 10 ================= -->
'''

# Insert ch10_view right before `</main>`
main_end_idx = html.find('</main>')
if main_end_idx != -1:
    html = html[:main_end_idx] + ch10_view + '\n    ' + html[main_end_idx:]
    print('Inserted chapter-view-10 before </main>!')
else:
    print('Error: </main> not found!')

# 3. Update switchChapter function
old_switch = '''      const b9 = document.getElementById('side-ch-9');
      const v1 = document.getElementById('chapter-view-1');'''

new_switch = '''      const b9 = document.getElementById('side-ch-9');
      const b10 = document.getElementById('side-ch-10');
      const v1 = document.getElementById('chapter-view-1');'''

html = html.replace(old_switch, new_switch)

old_switch_v = '''      const v9 = document.getElementById('chapter-view-9');

      const sideActive ='''

new_switch_v = '''      const v9 = document.getElementById('chapter-view-9');
      const v10 = document.getElementById('chapter-view-10');

      const sideActive ='''

html = html.replace(old_switch_v, new_switch_v)

old_side_b = '''      if (b9) b9.className = (chNum === 9) ? sideActive : sideInactive;

      if (v1)'''

new_side_b = '''      if (b9) b9.className = (chNum === 9) ? sideActive : sideInactive;
      if (b10) b10.className = (chNum === 10) ? sideActive : sideInactive;

      if (v1)'''

html = html.replace(old_side_b, new_side_b)

old_side_v = '''      if (v9) v9.classList.toggle('hidden', chNum !== 9);

      if (chNum === 1) {'''

new_side_v = '''      if (v9) v9.classList.toggle('hidden', chNum !== 9);
      if (v10) v10.classList.toggle('hidden', chNum !== 10);

      if (chNum === 1) {'''

html = html.replace(old_side_v, new_side_v)

old_switch_action = '''        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v9);
        }
      }'''

new_switch_action = '''        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v9);
        }
      } else if (chNum === 10) {
        setTabCh10('concepts');
        runCh10Calc();
        if (window.MathJax && window.MathJax.Hub && v10) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v10]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v10);
        }
      }'''

html = html.replace(old_switch_action, new_switch_action)

# 4. Add Chapter 10 JavaScript Logic
ch10_js = '''
    // ==========================================
    // CHAPTER 10: PERIMETER, AREA, VOLUME LOGIC
    // ==========================================
    let currentCh10Shape = 'rect';

    function setTabCh10(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch10-tab-' + t);
        const view = document.getElementById('ch10-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-emerald-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        runCh10Calc();
      }
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch10-view-' + tab));
      }
    }

    function setExerciseCh10(sec) {
      const secs = ['sec1', 'sec2', 'sec3', 'sec4'];
      secs.forEach(s => {
        const btn = document.getElementById('ch10-ex-btn-' + s);
        const view = document.getElementById('ch10-ex-' + s);
        if (btn && view) {
          if (s === sec) {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-emerald-600 text-white shadow-xs transition cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-600 hover:bg-slate-100 transition cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch10-ex-' + sec));
      }
    }

    function setCh10Shape(shape) {
      currentCh10Shape = shape;
      ['rect', 'sq', 'cuboid', 'cube'].forEach(s => {
        const b = document.getElementById('ch10-btn-' + s);
        if (b) {
          b.className = (s === (shape === 'square' ? 'sq' : shape)) ? 
            'px-3 py-1.5 rounded-lg bg-emerald-500 text-white transition cursor-pointer' : 
            'px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer';
        }
      });

      const boxB = document.getElementById('ch10-box-b');
      const boxH = document.getElementById('ch10-box-h');
      const lblL = document.getElementById('ch10-lbl-l');

      if (shape === 'rect') {
        if (lblL) lblL.textContent = 'लम्बाइ (Length - l):';
        if (boxB) boxB.classList.remove('hidden');
        if (boxH) boxH.classList.add('hidden');
      } else if (shape === 'square') {
        if (lblL) lblL.textContent = 'भुजाको लम्बाइ (Side - l):';
        if (boxB) boxB.classList.add('hidden');
        if (boxH) boxH.classList.add('hidden');
      } else if (shape === 'cuboid') {
        if (lblL) lblL.textContent = 'लम्बाइ (Length - l):';
        if (boxB) boxB.classList.remove('hidden');
        if (boxH) boxH.classList.remove('hidden');
      } else if (shape === 'cube') {
        if (lblL) lblL.textContent = 'किनाराको लम्बाइ (Edge - l):';
        if (boxB) boxB.classList.add('hidden');
        if (boxH) boxH.classList.add('hidden');
      }
      runCh10Calc();
    }

    function setCh10Preset(shape, l, b, h, unit) {
      setCh10Shape(shape);
      const inL = document.getElementById('ch10-in-l');
      const inB = document.getElementById('ch10-in-b');
      const inH = document.getElementById('ch10-in-h');
      const inUnit = document.getElementById('ch10-in-unit');
      if (inL) inL.value = l;
      if (inB) inB.value = b;
      if (inH) inH.value = h;
      if (inUnit) inUnit.value = unit;
      runCh10Calc();
    }

    function runCh10Calc() {
      const inL = document.getElementById('ch10-in-l');
      const inB = document.getElementById('ch10-in-b');
      const inH = document.getElementById('ch10-in-h');
      const inUnit = document.getElementById('ch10-in-unit');
      const res = document.getElementById('ch10-calc-res');
      if (!inL || !inUnit || !res) return;

      const l = parseFloat(inL.value);
      const b = inB ? parseFloat(inB.value) : l;
      const h = inH ? parseFloat(inH.value) : l;
      const unit = inUnit.value;

      if (isNaN(l) || l <= 0) {
        res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य लम्बाइ मान राख्नुहोस्।</span>';
        return;
      }

      let p = 0, a = 0, v = 0, sa = 0, liters = 0;
      let formulaText = "";
      let title = "";

      if (currentCh10Shape === 'rect') {
        if (isNaN(b) || b <= 0) {
          res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य चौडाइ मान राख्नुहोस्।</span>';
          return;
        }
        title = "आयत (Rectangle)";
        p = 2 * (l + b);
        a = l * b;
        formulaText = `• परिमिति: $P = 2(l + b) = 2(${l} + ${b}) = ${p.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}$<br>` +
                      `• क्षेत्रफल: $A = l \\times b = ${l} \\times ${b} = ${a.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}^2$`;
      } else if (currentCh10Shape === 'square') {
        title = "वर्ग (Square)";
        p = 4 * l;
        a = l * l;
        formulaText = `• परिमिति: $P = 4l = 4 \\times ${l} = ${p.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}$<br>` +
                      `• क्षेत्रफल: $A = l^2 = ${l}^2 = ${a.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}^2$`;
      } else if (currentCh10Shape === 'cuboid') {
        if (isNaN(b) || b <= 0 || isNaN(h) || h <= 0) {
          res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य चौडाइ र उचाइ मान राख्नुहोस्।</span>';
          return;
        }
        title = "षट्मुख (Cuboid)";
        v = l * b * h;
        sa = 2 * (l * b + b * h + l * h);
        if (unit === 'm') liters = v * 1000;
        else if (unit === 'cm') liters = v / 1000;
        else liters = v * 28.317; // ft^3 to liters approx
        formulaText = `• आयतन: $V = l \\times b \\times h = ${l} \\times ${b} \\times ${h} = ${v.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}^3$<br>` +
                      `• कुल सतह क्षेत्रफल: $A = 2(lb + bh + lh) = ${sa.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}^2$<br>` +
                      `• पानीको क्षमता: <strong>${liters.toFixed(2).replace(/\\.00$/, '')} लिटर</strong>`;
      } else if (currentCh10Shape === 'cube') {
        title = "घन (Cube)";
        v = l * l * l;
        sa = 6 * l * l;
        if (unit === 'm') liters = v * 1000;
        else if (unit === 'cm') liters = v / 1000;
        else liters = v * 28.317;
        formulaText = `• आयतन: $V = l^3 = ${l}^3 = ${v.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}^3$<br>` +
                      `• कुल सतह क्षेत्रफल: $A = 6l^2 = 6 \\times ${l}^2 = ${sa.toFixed(2).replace(/\\.00$/, '')}\\text{ ${unit}}^2$<br>` +
                      `• पानीको क्षमता: <strong>${liters.toFixed(2).replace(/\\.00$/, '')} लिटर</strong>`;
      }

      let resCards = '';
      if (currentCh10Shape === 'rect' || currentCh10Shape === 'square') {
        resCards = `
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">परिमिति (P)</span><span class="text-lg font-mono font-bold text-emerald-300">${p.toFixed(2).replace(/\\.00$/, '')} ${unit}</span></div>
          <div class="bg-teal-500/20 border border-teal-400/40 p-2.5 rounded-xl"><span class="text-xs text-teal-200 block">क्षेत्रफल (A)</span><span class="text-lg font-mono font-bold text-teal-300">${a.toFixed(2).replace(/\\.00$/, '')} ${unit}²</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">लम्बाइ (l)</span><span class="text-lg font-mono font-bold">${l} ${unit}</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">चौडाइ (b)</span><span class="text-lg font-mono font-bold">${currentCh10Shape === 'square' ? l : b} ${unit}</span></div>
        `;
      } else {
        resCards = `
          <div class="bg-cyan-500/20 border border-cyan-400/40 p-2.5 rounded-xl"><span class="text-xs text-cyan-200 block">आयतन (V)</span><span class="text-lg font-mono font-bold text-cyan-300">${v.toFixed(2).replace(/\\.00$/, '')} ${unit}³</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">पानी क्षमता</span><span class="text-lg font-mono font-bold text-emerald-300">${liters.toFixed(1).replace(/\\.0$/, '')} L</span></div>
          <div class="bg-purple-500/20 border border-purple-400/40 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">सतह क्षेत्रफल</span><span class="text-lg font-mono font-bold text-purple-300">${sa.toFixed(2).replace(/\\.00$/, '')} ${unit}²</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">नाप (l×b×h)</span><span class="text-sm font-mono font-bold">${l}×${currentCh10Shape==='cube'?l:b}×${currentCh10Shape==='cube'?l:h}</span></div>
        `;
      }

      res.innerHTML = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-emerald-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-bold text-xs border border-emerald-400/30">${title} प्रत्यक्ष गणना नतिजा</span>
          <span class="text-xs text-emerald-200">${unit} एकाइमा</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          ${resCards}
        </div>
        <div class="text-xs text-emerald-100 bg-white/5 p-3 rounded-xl mt-2 leading-relaxed">
          <strong>चरणबद्ध सूत्र तथा हिसाब:</strong><br>
          ${formulaText}
        </div>
      `;

      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(res);
      }
    }

    const ch10QuizData = [
      { correct: 1, exp: "$P = 2(l + b) = 2(8 + 5) = 2 \\times 13 = 26\\text{ cm}$ हुन्छ।" },
      { correct: 1, exp: "$A = l^2 = 9^2 = 81\\text{ cm}^2$ हुन्छ।" },
      { correct: 2, exp: "$V = l \\times b \\times h = 6 \\times 4 \\times 3 = 72\\text{ m}^3$ हुन्छ।" },
      { correct: 2, exp: "$1\\text{ m}^3 = 1,000\\text{ L} \\implies 2\\text{ m}^3 = 2,000\\text{ लिटर}$ हुन्छ।" },
      { correct: 2, exp: "व्यास अर्धव्यासको दोब्बर हुने भएकाले $d = 2 \\times 14 = 28\\text{ cm}$ हुन्छ।" }
    ];

    function checkQuizCh10(qIdx, selected) {
      const data = ch10QuizData[qIdx];
      const expBox = document.getElementById('ch10-qexp-' + qIdx);
      const badge = document.getElementById('ch10-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch10-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-emerald-50 border border-emerald-200 text-emerald-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(expBox);
        }
      }
    }

    function resetQuizCh10() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch10-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch10-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch10-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh10 = setTabCh10;
    window.setExerciseCh10 = setExerciseCh10;
    window.setCh10Shape = setCh10Shape;
    window.setCh10Preset = setCh10Preset;
    window.runCh10Calc = runCh10Calc;
    window.checkQuizCh10 = checkQuizCh10;
    window.resetQuizCh10 = resetQuizCh10;
'''

# Insert ch10_js right before `const urlParams`
urlparam_idx = html.find('const urlParams = new URLSearchParams')
if urlparam_idx != -1:
    html = html[:urlparam_idx] + ch10_js + '\n    ' + html[urlparam_idx:]
    print('Inserted Chapter 10 JS logic!')
else:
    print('Error: urlParams not found!')

# Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully written index.html!')

# Copy to offline files
shutil.copyfile('index.html', 'class6_math_offline.html')
shutil.copyfile('index.html', 'कक्षा_६_गणित_डिजिटल_साथी.html')
print('Successfully synchronized class6_math_offline.html and कक्षा_६_गणित_डिजिटल_साथी.html!')
