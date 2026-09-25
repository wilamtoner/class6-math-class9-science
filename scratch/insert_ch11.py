import shutil

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar
old_side = '''        <button onclick="alert('पाठ ११ को विस्तृत नोट notes/11_ghatanka_indices.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ ११: घाताङ्क</span>
          <span class="text-[10px] opacity-75">एकाइ ४</span>
        </button>'''

new_side = '''        <button id="side-ch-11" onclick="switchChapter(11)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium cursor-pointer">
          <span>पाठ ११: घाताङ्क</span>
          <span class="text-[10px] opacity-75">एकाइ ४</span>
        </button>'''

html = html.replace(old_side, new_side)

# 2. Build Chapter 11 HTML view
ch11_view = '''
      <!-- ================= CHAPTER 11: INDICES (घाताङ्क) ================= -->
      <div id="chapter-view-11" class="hidden space-y-6">

        <!-- Chapter Header Banner -->
        <div class="p-6 md:p-8 rounded-3xl bg-gradient-to-r from-violet-50 via-purple-50 to-fuchsia-50 border border-purple-200/80 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-purple-700 mb-1">एकाइ ४: बीजगणित (Unit 4: Algebra — पहिलो पाठ)</div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ ११: घाताङ्क (Indices)</h2>
          </div>
          <div class="flex flex-wrap items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ १२८–१३०</span>
            <span class="text-xs bg-purple-100 text-purple-800 font-bold px-3 py-1 rounded-xl border border-purple-200">अभ्यास ११.० तथा परियोजना कार्य</span>
          </div>
        </div>

        <!-- Chapter 11 Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button id="ch11-tab-concepts" onclick="setTabCh11('concepts')" class="px-5 py-2.5 rounded-xl bg-purple-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
            १. अवधारणा र घाताङ्क ल्याब
          </button>
          <button id="ch11-tab-exercises" onclick="setTabCh11('exercises')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            २. सम्पूर्ण अभ्यास समाधान (अभ्यास ११.०)
          </button>
          <button id="ch11-tab-tiers" onclick="setTabCh11('tiers')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
          </button>
          <button id="ch11-tab-quiz" onclick="setTabCh11('quiz')" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ४. आत्म-मूल्याङ्कन क्विज
          </button>
        </div>

        <!-- ================= CH11 TAB 1: CONCEPTS ================= -->
        <div id="ch11-view-concepts" class="space-y-6">

          <!-- Core Concepts Grid -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- Card 1: Definition -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">१</span>
                <h3 class="font-bold text-slate-800 text-base">घाताङ्क भनेको के हो?</h3>
              </div>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                कुनै सङ्ख्या वा चल राशिलाई सोही सङ्ख्याले कति पटक गुणन गरियो भन्ने सङ्केत नै <strong>घाताङ्क</strong> हो।
              </p>
              <div class="p-3 bg-purple-50 border border-purple-200 rounded-xl space-y-1 text-xs">
                <div>• $a^n = a \\times a \\times \\dots \\times a$ ($n$ पटक)</div>
                <div>• <strong>आधार (Base):</strong> $a$ | <strong>घाताङ्क (Power):</strong> $n$</div>
                <div>• उदा: $2^4 = 2 \\times 2 \\times 2 \\times 2 = 16$</div>
              </div>
            </div>

            <!-- Card 2: Product & Quotient Laws -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">२</span>
                <h3 class="font-bold text-slate-800 text-base">गुणन र भागको नियम</h3>
              </div>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                समान आधार भएका घाताङ्कीय पदहरूमा गुणन गर्दा घात जोडिन्छ, भाग गर्दा घटाइन्छ:
              </p>
              <div class="p-3 bg-indigo-50 border border-indigo-200 rounded-xl space-y-1 text-xs">
                <div>• <strong>गुणन नियम:</strong> $a^m \\times a^n = a^{m+n}$</div>
                <div>• <strong>भाग नियम:</strong> $a^m \\div a^n = a^{m-n}$</div>
                <div>• उदा: $x^3 \\times x^2 = x^5$, $y^7 \\div y^4 = y^3$</div>
              </div>
            </div>

            <!-- Card 3: Power of Power & Zero Exponent -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-pink-100 text-pink-700 flex items-center justify-center font-bold text-sm">३</span>
                <h3 class="font-bold text-slate-800 text-base">घातको घात र शून्य घाताङ्क</h3>
              </div>
              <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                घातमाथि घात हुँदा गुणन हुन्छ। शून्यबाहेक कुनै पनि आधारको घात ० भए मान १ हुन्छ:
              </p>
              <div class="p-3 bg-pink-50 border border-pink-200 rounded-xl space-y-1 text-xs">
                <div>• <strong>घातको घात:</strong> $(a^m)^n = a^{mn}$</div>
                <div>• <strong>शून्य घाताङ्क:</strong> $a^0 = 1$ ($a \\neq 0$)</div>
                <div>• उदा: $(2^3)^2 = 2^6 = 64$, $(100)^0 = 1$</div>
              </div>
            </div>
          </div>

          <!-- Master Formula Table -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <h3 class="font-bold text-slate-800 text-sm md:text-base flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-purple-600"></span>
              घाताङ्कका मुख्य नियमहरूको तालिका (Laws of Indices Master Table)
            </h3>
            <div class="grid grid-cols-2 md:grid-cols-5 gap-3 text-xs md:text-sm">
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">गुणन नियम</span>
                <span class="font-bold text-slate-900 font-mono text-sm">$a^m \\times a^n = a^{m+n}$</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">भाग नियम</span>
                <span class="font-bold text-slate-900 font-mono text-sm">$a^m \\div a^n = a^{m-n}$</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">घातको घात</span>
                <span class="font-bold text-slate-900 font-mono text-sm">$(a^m)^n = a^{mn}$</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
                <span class="block text-slate-500 font-medium text-xs">शून्य घाताङ्क</span>
                <span class="font-bold text-slate-900 font-mono text-sm">$a^0 = 1$</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center col-span-2 md:col-span-1">
                <span class="block text-slate-500 font-medium text-xs">संयुक्त आधार</span>
                <span class="font-bold text-slate-900 font-mono text-sm">$(ab)^n = a^n b^n$</span>
              </div>
            </div>
          </div>

          <!-- Interactive Exponent Simulator -->
          <div class="p-5 md:p-6 bg-gradient-to-br from-purple-950 via-indigo-900 to-slate-900 text-white rounded-3xl shadow-xl space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-3 border-b border-white/15 pb-4">
              <div>
                <span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-400 text-slate-950 inline-block mb-1">प्रत्यक्ष डिजिटल ल्याब</span>
                <h3 class="text-lg md:text-xl font-black">घाताङ्क प्रत्यक्ष सिमुलेटर (Interactive Exponent Lab)</h3>
              </div>
              <div class="flex items-center gap-1 bg-white/10 p-1 rounded-xl text-xs font-bold">
                <button id="ch11-btn-single" onclick="setCh11Mode('single')" class="px-3 py-1.5 rounded-lg bg-purple-500 text-white transition cursor-pointer">एकल घात ($a^n$)</button>
                <button id="ch11-btn-prod" onclick="setCh11Mode('product')" class="px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer">गुणन नियम</button>
                <button id="ch11-btn-quot" onclick="setCh11Mode('quotient')" class="px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer">भाग नियम</button>
                <button id="ch11-btn-powpow" onclick="setCh11Mode('powpow')" class="px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer">घातको घात</button>
              </div>
            </div>

            <!-- Dynamic Inputs -->
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
              <div>
                <label id="ch11-lbl-base" class="block text-xs text-purple-200 mb-1 font-semibold">आधार (Base - a):</label>
                <input id="ch11-in-base" type="text" value="2" oninput="runCh11Calc()" class="w-full bg-white/10 border border-white/20 rounded-xl px-3.5 py-2 text-white font-mono font-bold focus:outline-none focus:ring-2 focus:ring-purple-400 text-base">
              </div>
              <div>
                <label id="ch11-lbl-m" class="block text-xs text-purple-200 mb-1 font-semibold">पहिलो घात (Power - m):</label>
                <input id="ch11-in-m" type="number" step="1" value="5" oninput="runCh11Calc()" class="w-full bg-white/10 border border-white/20 rounded-xl px-3.5 py-2 text-white font-mono font-bold focus:outline-none focus:ring-2 focus:ring-purple-400 text-base">
              </div>
              <div id="ch11-box-n" class="hidden">
                <label id="ch11-lbl-n" class="block text-xs text-purple-200 mb-1 font-semibold">दोस्रो घात (Power - n):</label>
                <input id="ch11-in-n" type="number" step="1" value="3" oninput="runCh11Calc()" class="w-full bg-white/10 border border-white/20 rounded-xl px-3.5 py-2 text-white font-mono font-bold focus:outline-none focus:ring-2 focus:ring-purple-400 text-base">
              </div>
              <div class="flex items-end">
                <button onclick="runCh11Calc()" class="w-full bg-purple-600 hover:bg-purple-500 text-white font-bold py-2.5 px-4 rounded-xl text-sm transition cursor-pointer">गणना गर्नुहोस्</button>
              </div>
            </div>

            <!-- Presets -->
            <div class="flex flex-wrap items-center gap-2 pt-1 text-xs">
              <span class="text-purple-200 font-semibold">द्रुत नमुनाहरू:</span>
              <button onclick="setCh11Preset('single', '2', 5, 0)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">२⁵ = ३२</button>
              <button onclick="setCh11Preset('single', '3', 4, 0)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">३⁴ = ८१</button>
              <button onclick="setCh11Preset('single', '11', 3, 0)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">११³ = १३३१ (घन)</button>
              <button onclick="setCh11Preset('product', 'x', 3, 4)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">x³ × x⁴ = x⁷</button>
              <button onclick="setCh11Preset('quotient', '5', 6, 4)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">५⁶ ÷ ५⁴ = २५</button>
              <button onclick="setCh11Preset('powpow', '2', 3, 2)" class="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/20 transition cursor-pointer">(२³)² = ६४</button>
            </div>

            <!-- Result Box -->
            <div id="ch11-calc-res" class="bg-black/30 border border-white/15 rounded-2xl p-4 space-y-3">
              <!-- Dynamically populated by runCh11Calc() -->
            </div>
          </div>

        </div>

        <!-- ================= CH11 TAB 2: EXERCISES ================= -->
        <div id="ch11-view-exercises" class="hidden space-y-6">

          <!-- Section 1: Q1 & Q2 -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Q1 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3 text-xs md:text-sm">
              <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                <h4 class="font-bold text-slate-900 text-sm md:text-base">प्रश्न १: घाताङ्कका रूपमा लेख्नुहोस्</h4>
                <span class="text-xs bg-purple-100 text-purple-800 font-bold px-2 py-0.5 rounded">६ उप-प्रश्नहरू</span>
              </div>
              <div class="space-y-2 text-slate-700">
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(क)</strong> $3 \\times 3 \\times 3 = $ <strong class="text-purple-700 font-mono text-base">3³</strong> (वा २७)</div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(ख)</strong> $5 \\times 5 \\times 5 \\times 5 = $ <strong class="text-purple-700 font-mono text-base">5⁴</strong> (वा ६२५)</div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(ग)</strong> $a \\times a \\times a \\times a \\times a = $ <strong class="text-purple-700 font-mono text-base">a⁵</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(घ)</strong> $2 \\times 2 \\times 3 \\times 3 \\times 3 \\times 3 = $ <strong class="text-purple-700 font-mono text-base">2² × 3⁴</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(ङ)</strong> $x \\times x \\times x \\times y \\times y = $ <strong class="text-purple-700 font-mono text-base">x³ y²</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(च)</strong> $a \\times a \\times a \\times a \\times b \\times b \\times b = $ <strong class="text-purple-700 font-mono text-base">a⁴ b³</strong></div>
              </div>
            </div>

            <!-- Q2 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3 text-xs md:text-sm">
              <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                <h4 class="font-bold text-slate-900 text-sm md:text-base">प्रश्न २: विस्तारित रूप (Expanded Form)</h4>
                <span class="text-xs bg-indigo-100 text-indigo-800 font-bold px-2 py-0.5 rounded">७ उप-प्रश्नहरू</span>
              </div>
              <div class="space-y-2 text-slate-700">
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(क)</strong> $b^4 = $ <strong class="text-purple-700 font-mono">b × b × b × b</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(ख)</strong> $C^3 \\times C^2 = $ <strong class="text-purple-700 font-mono">C × C × C × C × C</strong> (वा $C^5$)</div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(ग)</strong> $l^2 = $ <strong class="text-purple-700 font-mono">l × l</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(घ)</strong> $a^2 \\times b^2 = $ <strong class="text-purple-700 font-mono">a × a × b × b</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(ङ)</strong> $y^2 \\times y^2 \\times p = $ <strong class="text-purple-700 font-mono">y × y × y × y × p</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(च)</strong> $l^3 \\times b^2 \\times h^2 = $ <strong class="text-purple-700 font-mono">l × l × l × b × b × h × h</strong></div>
                <div class="p-2.5 bg-slate-50 rounded-xl"><strong>(छ)</strong> $z \\times z^3 \\times z^2 = $ <strong class="text-purple-700 font-mono">z × z × z × z × z × z</strong> (वा $z^6$)</div>
              </div>
            </div>
          </div>

          <!-- Section 2: Q3 & Q4 -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-4">
            <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">प्रश्न ३ र प्रश्न ४ (गुणन नियम र ज्यामितीय प्रयोग)</h4>
            
            <!-- Q3 Row -->
            <div class="p-4 bg-purple-50/50 rounded-xl border border-purple-200 space-y-2 text-xs md:text-sm">
              <strong class="text-purple-950 block">प्रश्न ३: घाताङ्कका रूपमा लेख्नुहोस् (गुणन नियम प्रयोग):</strong>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div class="bg-white p-3 rounded-lg border border-purple-100">
                  <strong>(क)</strong> $4x^2 \\times x^2 = 4 \\times x^{2+2} = $ <strong class="text-purple-700 font-mono">4x⁴</strong>
                </div>
                <div class="bg-white p-3 rounded-lg border border-purple-100">
                  <strong>(ख)</strong> $x^5 \\times x^2 = x^{5+2} = $ <strong class="text-purple-700 font-mono">x⁷</strong>
                </div>
                <div class="bg-white p-3 rounded-lg border border-purple-100">
                  <strong>(ग)</strong> $3x^3 \\times 6x^3 = (3 \\times 6) \\times x^{3+3} = $ <strong class="text-purple-700 font-mono">18x⁶</strong>
                </div>
              </div>
            </div>

            <!-- Q4 Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs md:text-sm">
              <!-- Q4 (क) -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <strong class="text-slate-900 block border-b border-slate-200 pb-1">प्रश्न ४ (क): क्षेत्रफल</strong>
                <p>• (अ) लम्बाइ $x$, चौडाइ $y$: $A = $ <strong class="text-purple-700 font-mono">xy</strong> वर्ग एकाइ</p>
                <p>• (आ) दुवै $y$ भए: $A = y \\times y = $ <strong class="text-purple-700 font-mono">y²</strong> वर्ग एकाइ</p>
                <p>• (इ) $y = 8$ भए: $A = 8^2 = $ <strong class="text-purple-700 font-mono">64</strong> वर्ग एकाइ</p>
              </div>

              <!-- Q4 (ख) -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <strong class="text-slate-900 block border-b border-slate-200 pb-1">प्रश्न ४ (ख): आयतन</strong>
                <p>• (अ) लम्बाइ $a$, चौडाइ $b$, उचाइ $c$: $V = $ <strong class="text-purple-700 font-mono">abc</strong> घन एकाइ</p>
                <p>• (आ) सबै 'a' भए: $V = a \\times a \\times a = $ <strong class="text-purple-700 font-mono">a³</strong> घन एकाइ</p>
                <p>• (इ) $a = 11\\text{ cm}$ भए: $V = 11^3 = $ <strong class="text-purple-700 font-mono">1,331 cm³</strong></p>
              </div>

              <!-- Q4 (ग) -->
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <strong class="text-slate-900 block border-b border-slate-200 pb-1">प्रश्न ४ (ग): ठोस वस्तुको आयतन</strong>
                <p>• लम्बाइ $= 8a$, चौडाइ $= 4a$, उचाइ $= a$</p>
                <p>• $V = 8a \\times 4a \\times a$</p>
                <p>• $= (8 \\times 4 \\times 1) \\times a^3 = $ <strong class="text-purple-700 font-mono text-base">32a³</strong> घन एकाइ</p>
              </div>
            </div>

            <!-- Project Work -->
            <div class="p-4 bg-purple-50 rounded-xl border border-purple-200 text-xs md:text-sm">
              <strong class="text-purple-950 block mb-1">परियोजना कार्य प्रतिवेदन (Project Work):</strong>
              २ को घात तालिका: $2^1 = 2$, $2^2 = 4$, $2^3 = 8$, $2^4 = 16$, $2^5 = 32$, $2^6 = 64$, $2^7 = 128$, $2^8 = 256$, $2^{10} = 1024$ (१ किलोबाइट)। कम्प्युटर मेमोरी र मोबाइल स्टोरेज क्षमतामा घाताङ्कको व्यापक प्रयोग हुन्छ।
            </div>
          </div>

        </div>

        <!-- ================= CH11 TAB 3: TIERS ================= -->
        <div id="ch11-view-tiers" class="hidden space-y-4">
          <!-- Tier 1 -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">तह १: ज्ञान तथा बोध तह (Knowledge & Understanding)</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१. घाताङ्क परिभाषा:</strong> सङ्ख्यालाई सोही सङ्ख्याले कति पटक गुणन गरियो भन्ने जनाउने संक्षिप्त सङ्केत घाताङ्क हो।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>२. आधार र घाताङ्क:</strong> $x^5$ मा $x$ आधार (Base) र ५ घाताङ्क (Power) हो।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>३. गुणन नियम:</strong> समान आधार भए घाताङ्क जोडिन्छन्: $a^m \\times a^n = a^{m+n}$।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>४. भाग नियम:</strong> समान आधार भए घाताङ्क घटाइन्छन्: $a^m \\div a^n = a^{m-n}$।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>५. शून्य घाताङ्क:</strong> शून्यबाहेक जुनसुकै आधारको घात शून्य भए मान सधैँ $1$ हुन्छ ($a^0 = 1$)।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>६. घातको घात:</strong> $(2^3)^2 = 2^{3 \\times 2} = 2^6 = 64$।
              </div>
            </div>
          </div>

          <!-- Tier 2 -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">तह २: बोध तथा प्रयोग तह (Understanding & Application)</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>७. $2^4 \\times 2^3$:</strong> $2^{4+3} = 2^7 =$ <strong class="text-purple-700">128</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>८. $5^6 \\div 5^4$:</strong> $5^{6-4} = 5^2 =$ <strong class="text-purple-700">25</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>९. $5x^2 \\times 3x^4$:</strong> $(5 \\times 3) \\times x^{2+4} =$ <strong class="text-purple-700">15x⁶</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१०. $7^0 + (12)^0 - 2^2$:</strong> $1 + 1 - 4 =$ <strong class="text-purple-700">-2</strong>
              </div>
            </div>
          </div>

          <!-- Tier 3 -->
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
            <h4 class="font-bold text-slate-900 border-b border-slate-100 pb-2 text-sm md:text-base">तह ३: उच्च दक्षता बहु-चरणीय समस्याहरू (Higher Ability)</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs md:text-sm">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१३. बहु-आधार सरलीकरण:</strong> $\\frac{2^5 \\times 3^4 \\times 2^3}{2^6 \\times 3^2} = 2^{8-6} \\times 3^{4-2} = 4 \\times 9 =$ <strong class="text-purple-700">36</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१४. घातको घात सरलीकरण:</strong> $\\frac{(x^3)^4 \\times (y^2)^5 \\times x^2}{(x^2 y^3)^3} = \\frac{x^{14} y^{10}}{x^6 y^9} =$ <strong class="text-purple-700">x⁸ y</strong>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१५. घन र षट्मुख आयतन तुलना:</strong> घन $(2x)^3 = 8x^3$, षट्मुख $4x \\times 2x \\times x = 8x^3$। दुवै बाकसको आयतन <strong class="text-purple-700">बराबर</strong> छ।
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong>१६. घाताङ्कीय समीकरण:</strong> $2^{x+2} = 32 = 2^5 \\implies x + 2 = 5 \\implies x =$ <strong class="text-purple-700">3</strong>
              </div>
            </div>
          </div>
        </div>

        <!-- ================= CH11 TAB 4: QUIZ ================= -->
        <div id="ch11-view-quiz" class="hidden space-y-4">
          <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
            <div>
              <h4 class="font-bold text-slate-900 text-sm md:text-base">पाठ ११ आत्म-मूल्याङ्कन क्विज</h4>
              <p class="text-xs text-slate-500">५ ओटा वस्तुगत बहुवैकल्पिक प्रश्नहरू</p>
            </div>
            <button onclick="resetQuizCh11()" class="px-3.5 py-1.5 rounded-xl border border-slate-300 text-xs font-bold text-slate-700 hover:bg-slate-50 cursor-pointer">पुनः सुरु गर्नुहोस्</button>
          </div>

          <div class="space-y-3">
            <!-- Q1 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-purple-700">प्रश्न १</span>
                <span id="ch11-qbadge-0" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">$2 \\times 2 \\times 2 \\times 2 \\times 2$ लाई घाताङ्कका रूपमा लेख्दा कुन हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch11-qbtn-0-0" onclick="checkQuizCh11(0, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) 5²</button>
                <button id="ch11-qbtn-0-1" onclick="checkQuizCh11(0, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) 2⁵</button>
                <button id="ch11-qbtn-0-2" onclick="checkQuizCh11(0, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) 10</button>
                <button id="ch11-qbtn-0-3" onclick="checkQuizCh11(0, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) 2 × 5</button>
              </div>
              <div id="ch11-qexp-0" class="hidden"></div>
            </div>

            <!-- Q2 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-purple-700">प्रश्न २</span>
                <span id="ch11-qbadge-1" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">$x^3 \\times x^4$ को मान कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch11-qbtn-1-0" onclick="checkQuizCh11(1, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) x⁷</button>
                <button id="ch11-qbtn-1-1" onclick="checkQuizCh11(1, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) x¹²</button>
                <button id="ch11-qbtn-1-2" onclick="checkQuizCh11(1, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) x¹</button>
                <button id="ch11-qbtn-1-3" onclick="checkQuizCh11(1, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) 2x⁷</button>
              </div>
              <div id="ch11-qexp-1" class="hidden"></div>
            </div>

            <!-- Q3 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-purple-700">प्रश्न ३</span>
                <span id="ch11-qbadge-2" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">$(15)^0$ को मान कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch11-qbtn-2-0" onclick="checkQuizCh11(2, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) ०</button>
                <button id="ch11-qbtn-2-1" onclick="checkQuizCh11(2, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) १५</button>
                <button id="ch11-qbtn-2-2" onclick="checkQuizCh11(2, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) १</button>
                <button id="ch11-qbtn-2-3" onclick="checkQuizCh11(2, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) अनन्त</button>
              </div>
              <div id="ch11-qexp-2" class="hidden"></div>
            </div>

            <!-- Q4 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-purple-700">प्रश्न ४</span>
                <span id="ch11-qbadge-3" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">$a^8 \\div a^3$ लाई सरल गर्दा कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch11-qbtn-3-0" onclick="checkQuizCh11(3, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) a¹¹</button>
                <button id="ch11-qbtn-3-1" onclick="checkQuizCh11(3, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) a⁵</button>
                <button id="ch11-qbtn-3-2" onclick="checkQuizCh11(3, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) a²⁴</button>
                <button id="ch11-qbtn-3-3" onclick="checkQuizCh11(3, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) a⁸/³</button>
              </div>
              <div id="ch11-qexp-3" class="hidden"></div>
            </div>

            <!-- Q5 -->
            <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-purple-700">प्रश्न ५</span>
                <span id="ch11-qbadge-4" class="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600">हल हुन बाँकी</span>
              </div>
              <p class="text-sm font-bold text-slate-800">किनारा $11\\text{ cm}$ भएको घनको आयतन कति हुन्छ?</p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                <button id="ch11-qbtn-4-0" onclick="checkQuizCh11(4, 0)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(A) 33 cm³</button>
                <button id="ch11-qbtn-4-1" onclick="checkQuizCh11(4, 1)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(B) 121 cm³</button>
                <button id="ch11-qbtn-4-2" onclick="checkQuizCh11(4, 2)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(C) 1,331 cm³</button>
                <button id="ch11-qbtn-4-3" onclick="checkQuizCh11(4, 3)" class="w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer">(D) 1,221 cm³</button>
              </div>
              <div id="ch11-qexp-4" class="hidden"></div>
            </div>
          </div>
        </div>

      </div>
      <!-- ================= END CHAPTER 11 ================= -->
'''

# Insert ch11_view right before `</main>`
main_end_idx = html.find('</main>')
if main_end_idx != -1:
    html = html[:main_end_idx] + ch11_view + '\n    ' + html[main_end_idx:]
    print('Inserted chapter-view-11 before </main>!')
else:
    print('Error: </main> not found!')

# 3. Update switchChapter function
old_switch = '''      const b10 = document.getElementById('side-ch-10');
      const v1 = document.getElementById('chapter-view-1');'''

new_switch = '''      const b10 = document.getElementById('side-ch-10');
      const b11 = document.getElementById('side-ch-11');
      const v1 = document.getElementById('chapter-view-1');'''

html = html.replace(old_switch, new_switch)

old_switch_v = '''      const v10 = document.getElementById('chapter-view-10');

      const sideActive ='''

new_switch_v = '''      const v10 = document.getElementById('chapter-view-10');
      const v11 = document.getElementById('chapter-view-11');

      const sideActive ='''

html = html.replace(old_switch_v, new_switch_v)

old_side_b = '''      if (b10) b10.className = (chNum === 10) ? sideActive : sideInactive;

      if (v1)'''

new_side_b = '''      if (b10) b10.className = (chNum === 10) ? sideActive : sideInactive;
      if (b11) b11.className = (chNum === 11) ? sideActive : sideInactive;

      if (v1)'''

html = html.replace(old_side_b, new_side_b)

old_side_v = '''      if (v10) v10.classList.toggle('hidden', chNum !== 10);

      if (chNum === 1) {'''

new_side_v = '''      if (v10) v10.classList.toggle('hidden', chNum !== 10);
      if (v11) v11.classList.toggle('hidden', chNum !== 11);

      if (chNum === 1) {'''

html = html.replace(old_side_v, new_side_v)

old_switch_action = '''        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v10);
        }
      }'''

new_switch_action = '''        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v10);
        }
      } else if (chNum === 11) {
        setTabCh11('concepts');
        runCh11Calc();
        if (window.MathJax && window.MathJax.Hub && v11) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v11]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v11);
        }
      }'''

html = html.replace(old_switch_action, new_switch_action)

# 4. Add Chapter 11 JavaScript Logic
ch11_js = '''
    // ==========================================
    // CHAPTER 11: INDICES (घाताङ्क) LOGIC
    // ==========================================
    let currentCh11Mode = 'single';

    function setTabCh11(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch11-tab-' + t);
        const view = document.getElementById('ch11-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-purple-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        runCh11Calc();
      }
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch11-view-' + tab));
      }
    }

    function setCh11Mode(mode) {
      currentCh11Mode = mode;
      ['single', 'prod', 'quot', 'powpow'].forEach(m => {
        const b = document.getElementById('ch11-btn-' + m);
        if (b) {
          b.className = (m === (mode === 'product' ? 'prod' : mode === 'quotient' ? 'quot' : mode)) ? 
            'px-3 py-1.5 rounded-lg bg-purple-500 text-white transition cursor-pointer' : 
            'px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer';
        }
      });

      const boxN = document.getElementById('ch11-box-n');
      const lblM = document.getElementById('ch11-lbl-m');
      const lblN = document.getElementById('ch11-lbl-n');

      if (mode === 'single') {
        if (boxN) boxN.classList.add('hidden');
        if (lblM) lblM.textContent = 'घाताङ्क (Power - n):';
      } else if (mode === 'product') {
        if (boxN) boxN.classList.remove('hidden');
        if (lblM) lblM.textContent = 'पहिलो घात (Power - m):';
        if (lblN) lblN.textContent = 'दोस्रो घात (Power - n):';
      } else if (mode === 'quotient') {
        if (boxN) boxN.classList.remove('hidden');
        if (lblM) lblM.textContent = 'अंशको घात (Numerator Power - m):';
        if (lblN) lblN.textContent = 'हरको घात (Denominator Power - n):';
      } else if (mode === 'powpow') {
        if (boxN) boxN.classList.remove('hidden');
        if (lblM) lblM.textContent = 'भित्री घात (Inner Power - m):';
        if (lblN) lblN.textContent = 'बाहिरी घात (Outer Power - n):';
      }
      runCh11Calc();
    }

    function setCh11Preset(mode, base, m, n) {
      setCh11Mode(mode);
      const inBase = document.getElementById('ch11-in-base');
      const inM = document.getElementById('ch11-in-m');
      const inN = document.getElementById('ch11-in-n');
      if (inBase) inBase.value = base;
      if (inM) inM.value = m;
      if (inN) inN.value = n;
      runCh11Calc();
    }

    function runCh11Calc() {
      const inBase = document.getElementById('ch11-in-base');
      const inM = document.getElementById('ch11-in-m');
      const inN = document.getElementById('ch11-in-n');
      const res = document.getElementById('ch11-calc-res');
      if (!inBase || !inM || !res) return;

      const baseStr = inBase.value.trim() || '2';
      const m = parseInt(inM.value, 10);
      const n = inN ? parseInt(inN.value, 10) : 0;

      if (isNaN(m)) {
        res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य घाताङ्क मान राख्नुहोस्।</span>';
        return;
      }

      const isNumeric = !isNaN(parseFloat(baseStr)) && isFinite(baseStr);
      const numBase = parseFloat(baseStr);

      let title = "";
      let exprTeX = "";
      let stepTeX = "";
      let finalForm = "";
      let finalValStr = "";

      if (currentCh11Mode === 'single') {
        title = `एकल घाताङ्क ($${baseStr}^{${m}}$)`;
        exprTeX = `${baseStr}^{${m}}`;
        if (m === 0) {
          stepTeX = "शून्य घाताङ्क नियम अनुसार कुनै पनि आधार ($a \\neq 0$) को घात ० हुँदा मान १ हुन्छ।";
          finalForm = "1";
          finalValStr = "1";
        } else if (m > 0 && m <= 15) {
          let expandedArr = [];
          for (let i = 0; i < m; i++) expandedArr.push(baseStr);
          stepTeX = `विस्तारित रूप: $${expandedArr.join(' \\times ')}$`;
          if (isNumeric) {
            let val = Math.pow(numBase, m);
            finalForm = `${baseStr}^{${m}}`;
            finalValStr = val.toLocaleString();
          } else {
            finalForm = `${baseStr}^{${m}}`;
            finalValStr = `${baseStr}^{${m}}`;
          }
        } else {
          stepTeX = `विस्तारित रूप: $${baseStr}$ लाई $${m}$ पटक गुणन गरिएको।`;
          finalForm = `${baseStr}^{${m}}`;
          finalValStr = isNumeric ? Math.pow(numBase, m).toExponential(3) : `${baseStr}^{${m}}`;
        }
      } else if (currentCh11Mode === 'product') {
        title = `गुणनको नियम ($${baseStr}^{${m}} \\times ${baseStr}^{${n}}$)`;
        exprTeX = `${baseStr}^{${m}} \\times ${baseStr}^{${n}}`;
        const sumPower = m + n;
        stepTeX = `समान आधार भएकाले घातहरू जोडिन्छन्: $${baseStr}^{${m}+${n}} = ${baseStr}^{${sumPower}}$`;
        finalForm = `${baseStr}^{${sumPower}}`;
        if (isNumeric && sumPower >= 0 && sumPower <= 20) {
          finalValStr = Math.pow(numBase, sumPower).toLocaleString();
        } else {
          finalValStr = `${baseStr}^{${sumPower}}`;
        }
      } else if (currentCh11Mode === 'quotient') {
        title = `भागको नियम ($${baseStr}^{${m}} \\div ${baseStr}^{${n}}$)`;
        exprTeX = `\\frac{${baseStr}^{${m}}}{${baseStr}^{${n}}}`;
        const diffPower = m - n;
        stepTeX = `समान आधार भएकाले घातहरू घटाइन्छन्: $${baseStr}^{${m}-${n}} = ${baseStr}^{${diffPower}}$`;
        finalForm = `${baseStr}^{${diffPower}}`;
        if (diffPower === 0) {
          finalValStr = "1";
        } else if (isNumeric && diffPower > 0 && diffPower <= 20) {
          finalValStr = Math.pow(numBase, diffPower).toLocaleString();
        } else {
          finalValStr = `${baseStr}^{${diffPower}}`;
        }
      } else if (currentCh11Mode === 'powpow') {
        title = `घातको घात नियम ($(${baseStr}^{${m}})^{${n}}$)`;
        exprTeX = `(${baseStr}^{${m}})^{${n}}`;
        const prodPower = m * n;
        stepTeX = `घातमाथि घात भएकाले आपसमा गुणन हुन्छ: $${baseStr}^{${m} \\times ${n}} = ${baseStr}^{${prodPower}}$`;
        finalForm = `${baseStr}^{${prodPower}}`;
        if (isNumeric && prodPower >= 0 && prodPower <= 20) {
          finalValStr = Math.pow(numBase, prodPower).toLocaleString();
        } else {
          finalValStr = `${baseStr}^{${prodPower}}`;
        }
      }

      res.innerHTML = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-purple-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-purple-500/20 text-purple-300 font-bold text-xs border border-purple-400/30">${title} नतिजा</span>
          <span class="text-xs text-purple-200">आधार: ${baseStr}</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">अभिव्यञ्जन</span><span class="text-base font-mono font-bold">$${exprTeX}$</span></div>
          <div class="bg-purple-500/20 border border-purple-400/40 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">घाताङ्कीय रूप</span><span class="text-lg font-mono font-bold text-purple-300">$${finalForm}$</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">संख्यात्मक मान</span><span class="text-lg font-mono font-bold text-emerald-300">${finalValStr}</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">नियम</span><span class="text-xs font-sans font-semibold">${currentCh11Mode === 'single' ? 'परिभाषा' : currentCh11Mode === 'product' ? 'गुणन ($a^{m+n}$)' : currentCh11Mode === 'quotient' ? 'भाग ($a^{m-n}$)' : 'घातको घात ($a^{mn}$)'}</span></div>
        </div>
        <div class="text-xs text-purple-100 bg-white/5 p-3 rounded-xl mt-2 leading-relaxed">
          <strong>चरणबद्ध व्याख्या:</strong><br>
          ${stepTeX}
        </div>
      `;

      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(res);
      }
    }

    const ch11QuizData = [
      { correct: 1, exp: "२ लाई ५ पटक दोहोर्‍याएर गुणन गर्दा $2^5$ हुन्छ।" },
      { correct: 0, exp: "गुणनको नियम अनुसार आधार समान भए घाताङ्क जोडिन्छ: $x^{3+4} = x^7$।" },
      { correct: 2, exp: "शून्यबाहेक जुनसुकै आधारको घात शून्य हुँदा मान सधैँ $1$ हुन्छ: $(15)^0 = 1$।" },
      { correct: 1, exp: "भागको नियम अनुसार आधार समान भए घाताङ्क घटाइन्छ: $a^{8-3} = a^5$।" },
      { correct: 2, exp: "घनको आयतन $V = l^3 = 11^3 = 11 \\times 11 \\times 11 = 1,331\\text{ cm}^3$ हुन्छ।" }
    ];

    function checkQuizCh11(qIdx, selected) {
      const data = ch11QuizData[qIdx];
      const expBox = document.getElementById('ch11-qexp-' + qIdx);
      const badge = document.getElementById('ch11-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch11-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-purple-500 bg-purple-50 text-purple-900 font-bold';
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
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-purple-50 border border-purple-200 text-purple-900';
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

    function resetQuizCh11() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch11-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch11-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch11-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh11 = setTabCh11;
    window.setCh11Mode = setCh11Mode;
    window.setCh11Preset = setCh11Preset;
    window.runCh11Calc = runCh11Calc;
    window.checkQuizCh11 = checkQuizCh11;
    window.resetQuizCh11 = resetQuizCh11;
'''

# Insert ch11_js right before `const urlParams`
urlparam_idx = html.find('const urlParams = new URLSearchParams')
if urlparam_idx != -1:
    html = html[:urlparam_idx] + ch11_js + '\n    ' + html[urlparam_idx:]
    print('Inserted Chapter 11 JS logic!')
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
