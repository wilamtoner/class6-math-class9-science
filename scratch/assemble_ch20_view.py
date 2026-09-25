# -*- coding: utf-8 -*-
import os

with open('scratch/ch20_tab1.html', 'r', encoding='utf-8') as f:
    tab1 = f.read()

with open('scratch/ch20_tab2.html', 'r', encoding='utf-8') as f:
    tab2 = f.read()

with open('scratch/ch20_tab3.html', 'r', encoding='utf-8') as f:
    tab3 = f.read()

with open('scratch/ch20_tab4.html', 'r', encoding='utf-8') as f:
    tab4 = f.read()

banner_and_tabs = r'''
      <!-- ================= CHAPTER 20 VIEW CONTAINER ================= -->
      <div id="chapter-view-20" class="flex-1 flex flex-col hidden">
        <!-- Top Chapter Banner -->
        <div class="border-b border-slate-100 pb-5 mb-6 flex flex-wrap items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2 text-xs font-bold text-blue-600 mb-1">
              एकाइ ६: तथ्याङ्कशास्त्र (Unit 6: Statistics — अन्तिम एकाइ तथा अन्तिम पाठ)
            </div>
            <h2 class="text-2xl md:text-3xl font-black text-slate-900">पाठ २०: तथ्याङ्कशास्त्र (Statistics)</h2>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs bg-slate-100 text-slate-700 font-semibold px-3 py-1 rounded-xl border border-slate-200">पाठ्यपुस्तक पृष्ठ २२४–२३३</span>
            <span class="text-xs bg-emerald-100 text-emerald-700 font-semibold px-3 py-1 rounded-xl border border-emerald-200">अभ्यास २०.१, २०.२ र एकाइ ६ मिश्रित अभ्यास</span>
          </div>
        </div>

        <!-- Navigation Tabs -->
        <div class="flex border-b border-slate-200 gap-2 mb-6 overflow-x-auto pb-1 text-sm font-bold">
          <button onclick="setTabCh20('concepts')" id="ch20-tab-concepts" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer">
            १. अवधारणा र तथ्याङ्क-स्तम्भचित्र ल्याब
          </button>
          <button onclick="setTabCh20('exercises')" id="ch20-tab-exercises" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            २. सम्पूर्ण अभ्यास समाधान (२०.१, २०.२ र मिश्रित)
          </button>
          <button onclick="setTabCh20('tiers')" id="ch20-tab-tiers" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ३. तीन तहका नमुना प्रश्नहरू (१६ प्रश्न)
          </button>
          <button onclick="setTabCh20('quiz')" id="ch20-tab-quiz" class="px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer">
            ४. स्वमूल्याङ्कन क्विज (१० प्रश्न)
          </button>
        </div>
'''

footer = r'''
      </div>
      <!-- ================= END CHAPTER 20 ================= -->
'''

full_view = banner_and_tabs + '\n' + tab1 + '\n' + tab2 + '\n' + tab3 + '\n' + tab4 + '\n' + footer

with open('scratch/ch20_view.html', 'w', encoding='utf-8') as f:
    f.write(full_view.strip() + '\n')

print("scratch/ch20_view.html assembled successfully! Size:", len(full_view), "bytes")
