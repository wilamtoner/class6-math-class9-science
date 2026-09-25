# -*- coding: utf-8 -*-
import os

html_tab1 = r'''
<!-- ================= CHAPTER 20: TAB 1 (CONCEPTS & INTERACTIVE LAB) ================= -->
<div id="ch20-view-concepts" class="space-y-8">
  <!-- Key Concept Cards Grid -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <!-- Card 1: Data & Frequency -->
    <div class="bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-100 rounded-2xl p-6 shadow-sm">
      <div class="flex items-center gap-3 mb-3">
        <span class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-black text-lg">१</span>
        <div>
          <h3 class="font-extrabold text-lg text-slate-900">तथ्याङ्क, बारम्बारता र मिलान चिह्न (Data & Tally Marks)</h3>
          <span class="text-xs text-blue-700 font-semibold">कोरा आँकडालाई पाँच-पाँचको समूहमा व्यवस्थित गर्ने कला</span>
        </div>
      </div>
      <div class="text-sm text-slate-700 space-y-2 leading-relaxed">
        <p>कुनै उद्देश्यका लागि सङ्कलन गरिएका सङ्ख्यात्मक सूचनाहरूलाई <strong>तथ्याङ्क (Data)</strong> भनिन्छ। अव्यवस्थित सुरुवाती तथ्याङ्कलाई <strong>कोरा तथ्याङ्क (Raw Data)</strong> भनिन्छ।</p>
        <ul class="list-disc list-inside space-y-1.5 text-xs md:text-sm text-slate-600 bg-white/70 p-3.5 rounded-xl border border-blue-100">
          <li><strong>बारम्बारता (Frequency - $f$):</strong> तथ्याङ्कमा कुनै मान कति पटक दोहोरिएको छ भन्ने सङ्ख्या।</li>
          <li><strong>मिलान चिह्न (Tally Mark):</strong> गणना गर्दा प्रयोग गरिने ठाडो धर्सा ($|$) र चार धर्सापछि पाँचौँले छड्के काट्ने ($||||\mkern-12mu/$) नियम। यसले गर्दा ठूला सङ्ख्याहरू ५-५ को समूहमा छिटो गन्न सकिन्छ।</li>
          <li><strong>प्राथमिक तथ्याङ्क:</strong> आफैँले स्थलगत रूपमा सङ्कलन गरेको मौलिक तथ्याङ्क।</li>
          <li><strong>द्वितीयक तथ्याङ्क:</strong> अरूले पहिले नै प्रकाशित गरेको स्रोतबाट लिइएको तथ्याङ्क।</li>
        </ul>
      </div>
    </div>

    <!-- Card 2: Bar Diagram Rules -->
    <div class="bg-gradient-to-br from-emerald-50 to-teal-50 border border-teal-100 rounded-2xl p-6 shadow-sm">
      <div class="flex items-center gap-3 mb-3">
        <span class="w-10 h-10 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-lg">२</span>
        <div>
          <h3 class="font-extrabold text-lg text-slate-900">साधारण स्तम्भ चित्र (Simple Bar Diagram)</h3>
          <span class="text-xs text-teal-700 font-semibold">आयताकार खम्बाहरूबाट दृश्य तुलना गर्ने वैज्ञानिक विधि</span>
        </div>
      </div>
      <div class="text-sm text-slate-700 space-y-2 leading-relaxed">
        <p>तथ्याङ्कलाई समान चौडाइ भएका आयताकार स्तम्भ (खम्बा) हरूको उचाइद्वारा दृश्य रूपमा प्रस्तुत गर्ने चित्रलाई <strong>स्तम्भ चित्र</strong> भनिन्छ।</p>
        <div class="bg-white/80 p-3.5 rounded-xl border border-teal-100 text-xs md:text-sm text-slate-700 space-y-1.5">
          <div class="font-bold text-teal-900 flex items-center gap-1.5">
            <svg style="width: 18px; height: 18px; min-width: 18px; display: inline-block; vertical-align: middle;" class="text-teal-600 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
            स्तम्भ चित्रका ४ सुनौला अनिवार्य नियमहरू (पृष्ठ २२९):
          </div>
          <ol class="list-decimal list-inside space-y-1 pl-2 text-xs text-slate-600">
            <li><strong>अक्षहरू:</strong> तेर्सो $X$-अक्षमा विषय/शीर्षक र ठाडो $Y$-अक्षमा बारम्बारता स्पष्ट कोर्नुपर्छ।</li>
            <li><strong>शीर्षक (Title):</strong> स्तम्भ चित्रको स्पष्ट शीर्षक अनिवार्य लेख्नुपर्छ।</li>
            <li><strong>समान चौडाइ:</strong> सबै स्तम्भहरूको चौडाइ ठ्याक्कै <strong>बराबर</strong> हुनुपर्छ।</li>
            <li><strong>समान खाली दूरी:</strong> दुई स्तम्भबिचको दूरी सधैँ <strong>समान</strong> छोड्नुपर्छ।</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <!-- Tally Marks Reference & Bar Diagram Construction Guide -->
  <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
      <div>
        <h4 class="font-black text-slate-900 text-base md:text-lg flex items-center gap-2">
          <span>📊 मिलान चिह्न (Tally Marks) र मानहरूको प्रदर्शन तालिका</span>
        </h4>
        <p class="text-xs text-slate-500">पाँच-पाँचको समूहमा तथ्याङ्क सङ्कलन गर्ने मानक विधि</p>
      </div>
      <span class="text-xs bg-blue-100 text-blue-900 font-bold px-3 py-1 rounded-xl">पाठ्यपुस्तक पृष्ठ २२६ तालिका</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-3 text-center text-xs">
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
        <span class="text-slate-400 block text-[10px]">सङ्ख्या १</span>
        <span class="font-mono text-base font-black text-blue-600">|</span>
        <span class="text-[10px] text-slate-500 block">१ धर्सा</span>
      </div>
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
        <span class="text-slate-400 block text-[10px]">सङ्ख्या २</span>
        <span class="font-mono text-base font-black text-blue-600">||</span>
        <span class="text-[10px] text-slate-500 block">२ धर्सा</span>
      </div>
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
        <span class="text-slate-400 block text-[10px]">सङ्ख्या ३</span>
        <span class="font-mono text-base font-black text-blue-600">|||</span>
        <span class="text-[10px] text-slate-500 block">३ धर्सा</span>
      </div>
      <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
        <span class="text-slate-400 block text-[10px]">सङ्ख्या ४</span>
        <span class="font-mono text-base font-black text-blue-600">||||</span>
        <span class="text-[10px] text-slate-500 block">४ ठाडो धर्सा</span>
      </div>
      <div class="bg-emerald-50 p-2.5 rounded-xl border border-emerald-200">
        <span class="text-emerald-700 block text-[10px] font-bold">सङ्ख्या ५</span>
        <span class="font-mono text-base font-black text-emerald-600"><s>||||</s></span>
        <span class="text-[10px] text-emerald-700 block font-bold">१ पूरा बण्डल (५)</span>
      </div>
      <div class="bg-emerald-50 p-2.5 rounded-xl border border-emerald-200">
        <span class="text-emerald-700 block text-[10px] font-bold">सङ्ख्या १०</span>
        <span class="font-mono text-base font-black text-emerald-600"><s>||||</s> <s>||||</s></span>
        <span class="text-[10px] text-emerald-700 block font-bold">२ पूरा बण्डल</span>
      </div>
    </div>
  </div>

  <!-- INTERACTIVE LAB CONTAINER -->
  <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl text-white space-y-6">
    <!-- Lab Header & Mode Selector -->
    <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-800 pb-5">
      <div>
        <div class="flex items-center gap-2 text-xs font-bold text-cyan-400 mb-1">
          <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
          पाठ २० अन्तरक्रियात्मक प्रयोगशाला (Interactive Statistics Lab)
        </div>
        <h3 class="text-xl md:text-2xl font-black text-white">तथ्याङ्क र स्तम्भ चित्र स्टुडियो (Statistics & Bar Studio)</h3>
      </div>

      <!-- Mode Selector Pills -->
      <div class="flex items-center gap-2 bg-slate-800/80 p-1.5 rounded-2xl border border-slate-700">
        <button onclick="switchCh20Lab('barStudio')" id="ch20-lab-btn-barStudio" class="px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-md transition">
          १. स्तम्भ चित्र निर्माता
        </button>
        <button onclick="switchCh20Lab('tallyLab')" id="ch20-lab-btn-tallyLab" class="px-4 py-2 rounded-xl text-xs font-bold text-slate-300 hover:text-white transition">
          २. ट्याली मार्क जेनेरेटर
        </button>
        <button onclick="switchCh20Lab('readerLab')" id="ch20-lab-btn-readerLab" class="px-4 py-2 rounded-xl text-xs font-bold text-slate-300 hover:text-white transition">
          ३. स्तम्भ चित्र पठन क्विज
        </button>
      </div>
    </div>

    <!-- ================= LAB MODE 1: DYNAMIC BAR CHART STUDIO ================= -->
    <div id="ch20-lab-mode-barStudio" class="space-y-6">
      <!-- Dataset Selector Controls -->
      <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-800/60 p-3.5 rounded-2xl border border-slate-700">
        <div class="flex flex-wrap items-center gap-2">
          <span class="text-xs font-bold text-slate-400 mr-1">नमुना तथ्याङ्क छान्नुहोस्:</span>
          <button onclick="loadBarPreset('absent')" id="btn-bar-absent" class="bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white">अनुपस्थित विद्यार्थी (६ दिन)</button>
          <button onclick="loadBarPreset('subjects')" id="btn-bar-subjects" class="bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600">सौरभको परीक्षा प्राप्ताङ्क</button>
          <button onclick="loadBarPreset('population')" id="btn-bar-population" class="bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600">सहरको जनसङ्ख्या वृद्धि</button>
          <button onclick="loadBarPreset('expenses')" id="btn-bar-expenses" class="bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600">परिवारको वार्षिक खर्च</button>
          <button onclick="loadBarPreset('animals')" id="btn-bar-animals" class="bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600">पशु फार्मको तथ्याङ्क</button>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-xs text-slate-400">रङ थिम:</span>
          <select id="ch20-bar-theme" onchange="renderBarStudio()" class="bg-slate-900 text-xs text-slate-200 px-3 py-1.5 rounded-xl border border-slate-700 focus:outline-none focus:border-cyan-500">
            <option value="indigo">इन्डिगो र निलो (Indigo-Blue)</option>
            <option value="emerald">समुन्द्री हरियो (Emerald-Teal)</option>
            <option value="amber">सुनौलो अम्बर (Amber-Gold)</option>
            <option value="multi">बहुरङ्गी स्तम्भ (Multi-color)</option>
          </select>
        </div>
      </div>

      <!-- Canvas and Metric Summary -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        <!-- SVG Canvas -->
        <div class="lg:col-span-8 flex flex-col justify-center items-center bg-slate-950 p-4 rounded-2xl border border-slate-800 relative overflow-hidden">
          <div id="bar-chart-title" class="text-sm font-extrabold text-cyan-300 mb-2">
            अनुपस्थित विद्यार्थी सङ्ख्या सम्बन्धी साधारण स्तम्भ चित्र
          </div>
          <svg id="ch20-bar-svg" viewBox="0 0 540 340" class="w-full max-w-[560px] h-[320px]">
            <rect x="0" y="0" width="540" height="340" fill="#090d16" rx="16" />
            <!-- Rendered dynamically via JS -->
            <g id="bar-grid-group"></g>
            <g id="bar-elements-group"></g>
            <g id="bar-axes-group"></g>
            <g id="bar-labels-group"></g>
          </svg>

          <!-- Floating Scale Badge -->
          <div class="absolute top-5 right-6 bg-slate-900/90 backdrop-blur px-3 py-1.5 rounded-xl border border-slate-700 text-[11px] text-amber-300 font-semibold flex items-center gap-1.5">
            <span>📏 स्केल (Scale):</span>
            <span id="bar-scale-text">Y-अक्ष: १ से.मि. = ५ एकाइ</span>
          </div>
        </div>

        <!-- Metric & Analysis Cards -->
        <div class="lg:col-span-4 space-y-3">
          <div class="bg-slate-800/80 p-4 rounded-2xl border border-slate-700 space-y-2.5 text-xs">
            <h4 class="font-bold text-sm text-cyan-400 border-b border-slate-700 pb-1.5 flex items-center justify-between">
              <span>📈 तथ्याङ्क विश्लेषण सारांश</span>
              <span id="bar-items-count" class="text-[11px] text-slate-400">६ वटा स्तम्भ</span>
            </h4>
            
            <div class="flex justify-between items-center bg-slate-900/60 p-2.5 rounded-xl border border-slate-800">
              <span class="text-slate-400">सर्वोच्च मान (Maximum):</span>
              <span id="bar-metric-max" class="font-black text-emerald-400 text-sm">२५</span>
            </div>

            <div class="flex justify-between items-center bg-slate-900/60 p-2.5 rounded-xl border border-slate-800">
              <span class="text-slate-400">न्यूनतम मान (Minimum):</span>
              <span id="bar-metric-min" class="font-black text-rose-400 text-sm">५</span>
            </div>

            <div class="flex justify-between items-center bg-slate-900/60 p-2.5 rounded-xl border border-slate-800">
              <span class="text-slate-400">कुल योग (Total Sum):</span>
              <span id="bar-metric-sum" class="font-black text-cyan-300 text-sm">६५</span>
            </div>

            <div class="flex justify-between items-center bg-slate-900/60 p-2.5 rounded-xl border border-slate-800">
              <span class="text-slate-400">औसत मान (Average / Mean):</span>
              <span id="bar-metric-avg" class="font-bold text-amber-300 text-sm">१०.८३</span>
            </div>
          </div>

          <div class="bg-blue-950/40 p-3.5 rounded-2xl border border-blue-800/40 text-[11px] text-blue-200 leading-relaxed">
            💡 <strong>स्मरण रहोस्:</strong> प्रत्येक स्तम्भको चौडाइ र दुई स्तम्भबिचको दूरी ठ्याक्कै समान छ, जसले गर्दा खम्बाहरूको उचाइबाट सीधै तुलना गर्न सकिन्छ।
          </div>
        </div>
      </div>
    </div>

    <!-- ================= LAB MODE 2: TALLY MARKS & FREQUENCY GENERATOR ================= -->
    <div id="ch20-lab-mode-tallyLab" class="hidden space-y-6">
      <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-800/60 p-3.5 rounded-2xl border border-slate-700">
        <div class="flex flex-wrap items-center gap-2">
          <span class="text-xs font-bold text-slate-400 mr-1">नमुना कोरा तथ्याङ्क:</span>
          <button onclick="loadTallyPreset('scores')" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 hover:bg-slate-600 text-slate-200 transition">गणित प्राप्ताङ्क (३० जना)</button>
          <button onclick="loadTallyPreset('heights')" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 hover:bg-slate-600 text-slate-200 transition">विद्यार्थी उचाइ (३२ जना)</button>
          <button onclick="loadTallyPreset('transport')" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 hover:bg-slate-600 text-slate-200 transition">यातायातका साधन (४० जना)</button>
          <button onclick="loadTallyPreset('dice')" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 hover:bg-slate-600 text-slate-200 transition">पासा फ्याँक्दा (२५ पटक)</button>
        </div>
        <div class="flex items-center gap-2">
          <input type="text" id="tally-custom-item" placeholder="नयाँ मान थप्नुहोस्..." class="bg-slate-900 text-xs text-slate-200 px-3 py-1.5 rounded-xl border border-slate-700 focus:outline-none focus:border-cyan-500 w-36">
          <button onclick="addTallyItem()" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition flex items-center gap-1">
            <span>+ थप्नुहोस्</span>
          </button>
        </div>
      </div>

      <!-- Tally Table Dynamic Display -->
      <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
          <h4 id="tally-dataset-title" class="font-extrabold text-sm md:text-base text-cyan-300">
            कक्षा ६ का ३० जना विद्यार्थीहरूको गणित प्राप्ताङ्कको बारम्बारता तालिका
          </h4>
          <span id="tally-total-count" class="text-xs bg-blue-500/20 text-blue-300 font-bold px-3 py-1 rounded-xl border border-blue-500/30">कुल सङ्ख्या N = ३०</span>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs md:text-sm border-collapse">
            <thead>
              <tr class="bg-slate-900 text-slate-300 font-bold border-b border-slate-800">
                <th class="p-3 w-16 text-center">क्र.सं.</th>
                <th class="p-3">मान / शीर्षक (Value)</th>
                <th class="p-3">मिलान चिह्न (Tally Mark)</th>
                <th class="p-3 w-32 text-center">बारम्बारता ($f$)</th>
              </tr>
            </thead>
            <tbody id="tally-table-body" class="divide-y divide-slate-800/80 text-slate-300">
              <!-- Rendered dynamically via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ================= LAB MODE 3: BAR CHART READER LAB ================= -->
    <div id="ch20-lab-mode-readerLab" class="hidden space-y-6">
      <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-800/60 p-3.5 rounded-2xl border border-slate-700">
        <div class="text-xs text-slate-300 font-semibold">
          स्तम्भ चित्र हेरेर सोधिएका प्रश्नहरूको सही उत्तर पत्ता लगाउनुहोस् र तत्काल पृष्ठपोषण पाउनुहोस्।
        </div>
        <button onclick="nextReaderQuestion()" class="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition flex items-center gap-1.5">
          <span>🔄 अर्को प्रश्न हेर्नुहोस्</span>
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        <!-- Interactive Chart Viewer -->
        <div class="lg:col-span-7 flex flex-col items-center justify-center bg-slate-950 p-4 rounded-2xl border border-slate-800 relative">
          <div id="reader-chart-title" class="text-xs font-bold text-cyan-300 mb-2">
            कक्षा ६ देखि १२ सम्मका विद्यार्थीहरूको सङ्ख्या
          </div>
          <svg id="ch20-reader-svg" viewBox="0 0 460 300" class="w-full max-w-[480px] h-[280px]">
            <rect x="0" y="0" width="460" height="300" fill="#090d16" rx="16" />
            <g id="reader-svg-elements"></g>
          </svg>
        </div>

        <!-- Question Card -->
        <div class="lg:col-span-5 space-y-4">
          <div class="bg-slate-800/80 p-5 rounded-2xl border border-slate-700 space-y-4 text-xs">
            <div class="flex items-center justify-between border-b border-slate-700 pb-2">
              <span id="reader-q-num" class="font-bold text-xs text-blue-400">प्रश्न १ / ५</span>
              <span id="reader-score-badge" class="px-2.5 py-0.5 rounded-full text-[11px] font-black bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">अङ्क: ० / ५</span>
            </div>

            <p id="reader-q-text" class="font-extrabold text-sm text-slate-100 leading-relaxed">
              कुन कक्षामा सबैभन्दा धेरै विद्यार्थीहरू अध्ययनरत छन्?
            </p>

            <div id="reader-options-container" class="space-y-2">
              <!-- Rendered via JS -->
            </div>

            <div id="reader-feedback" class="p-3 rounded-xl bg-slate-900/80 border border-slate-800 text-xs font-semibold text-slate-400 min-h-[36px]">
              विकल्प छानेर आफ्नो उत्तर परीक्षण गर्नुहोस्!
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- ================= END TAB 1 ================= -->
'''

with open('scratch/ch20_tab1.html', 'w', encoding='utf-8') as f:
    f.write(html_tab1.strip() + '\n')

print("scratch/ch20_tab1.html created successfully!")
