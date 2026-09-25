const fs = require('fs');

const tab1 = fs.readFileSync('scratch/c9u1_tab1.html', 'utf8');
const tab2 = fs.readFileSync('scratch/c9u1_tab2.html', 'utf8');
const tab3 = fs.readFileSync('scratch/c9u1_tab3.html', 'utf8');
const tab4 = fs.readFileSync('scratch/c9u1_tab4.html', 'utf8');

const viewHtml = `
<!-- ================= CLASS 9 UNIT 1 CONTAINER ================= -->
<div id="c9-view-1" class="flex-1 min-w-0 flex flex-col">
  <!-- Unit Header Banner -->
  <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-4">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-100 text-cyan-800 border border-cyan-200">
          कक्षा ९ विज्ञान तथा प्रविधि | एकाइ १
        </span>
        <span class="text-xs text-slate-400">•</span>
        <span class="text-xs text-slate-500 font-medium">पाठ्यपुस्तक पृष्ठ १–१६</span>
      </div>
      <h2 class="text-2xl md:text-3xl font-black text-slate-900 tracking-tight">
        एकाइ १: वैज्ञानिक अध्ययन (Scientific Study)
      </h2>
      <p class="text-xs md:text-sm text-slate-500 mt-1">
        वैज्ञानिक सिकाइका चरणहरू, विज्ञानका क्षेत्रहरू र अन्तरसम्बन्ध, मेट्रिक उपसर्ग, न्यूनतम नाप, वैज्ञानिक सङ्केतन र प्रयोगशाला सुरक्षा
      </p>
    </div>
    <div class="flex items-center gap-2">
      <span class="inline-flex items-center px-3 py-1 rounded-xl text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
        ✓ सम्पूर्ण पाठ्यपुस्तक अभ्यास तथा क्रियाकलाप समावेश
      </span>
    </div>
  </div>

  <!-- 4-Tab Navigation Bar -->
  <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
    <button onclick="setTabC9U1('concepts')" id="c9u1-tab-concepts" class="px-5 py-2.5 rounded-xl bg-cyan-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
      १. सैद्धान्तिक अवधारणा तथा भर्चुअल विज्ञान ल्याब
    </button>
    <button onclick="setTabC9U1('exercises')" id="c9u1-tab-exercises" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      २. सम्पूर्ण अभ्यास समाधान (१ देखि २ र क्रियाकलाप)
    </button>
    <button onclick="setTabC9U1('tiers')" id="c9u1-tab-tiers" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
    </button>
    <button onclick="setTabC9U1('quiz')" id="c9u1-tab-quiz" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
      ४. स्वमूल्याङ्कन क्विज (१० प्रश्न)
    </button>
  </div>

  <!-- Tab Contents -->
  ${tab1}
  ${tab2}
  ${tab3}
  ${tab4}
</div>
`;

fs.writeFileSync('scratch/c9u1_view.html', viewHtml);
console.log('Assembled scratch/c9u1_view.html successfully. Size:', viewHtml.length);
