# -*- coding: utf-8 -*-
import os

html_tab3 = r'''
<!-- ================= CHAPTER 20: TAB 3 (TIERED MODEL QUESTIONS) ================= -->
<div id="ch20-view-tiers" class="hidden space-y-8">
  <div class="border-b border-slate-200 pb-4 flex flex-wrap items-center justify-between gap-3">
    <div>
      <h3 class="text-xl md:text-2xl font-black text-slate-900">पाठ २०: तीन तहका स्तरीकृत नमुना प्रश्नोत्तर (Tiered Model Q&A)</h3>
      <p class="text-xs text-slate-500">CDC विशिष्टीकरण तालिका अनुसार ज्ञानात्मक, बोधात्मक र उच्च दक्षतायुक्त १६ प्रश्नहरू</p>
    </div>
    <div class="flex items-center gap-2">
      <span class="text-xs bg-blue-100 text-blue-800 font-bold px-3 py-1 rounded-xl">५ ज्ञानात्मक</span>
      <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-3 py-1 rounded-xl">६ बोधात्मक</span>
      <span class="text-xs bg-purple-100 text-purple-800 font-bold px-3 py-1 rounded-xl">५ उच्च दक्षता</span>
    </div>
  </div>

  <!-- TIER 1: KNOWLEDGE & RECALL (5 Questions) -->
  <div class="space-y-4">
    <div class="flex items-center gap-2 text-blue-700 font-black text-base border-b border-blue-200 pb-2">
      <span class="w-7 h-7 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-bold">T1</span>
      <h4>तह १: ज्ञानात्मक तथा आधारभूत प्रश्नहरू (Knowledge & Recall — ५ प्रश्न)</h4>
    </div>

    <!-- Q1 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न १: तथ्याङ्क (Data) र कोरा तथ्याङ्क (Raw Data) भनेको के हो?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">१ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-blue-400">
        <strong>उत्तर:</strong> निश्चित उद्देश्यका लागि सङ्कलन गरिएका संख्यात्मक सूचनाहरूको व्यवस्थित सङ्ग्रहलाई <strong>तथ्याङ्क (Data)</strong> भनिन्छ। सुरुमा सङ्कलन गरिएका तर कुनै क्रमबद्ध तालिका वा समूहमा नराखिएका अव्यवस्थित आँकडाहरूलाई <strong>कोरा तथ्याङ्क (Raw Data)</strong> भनिन्छ।
      </p>
    </div>

    <!-- Q2 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न २: बारम्बारता (Frequency) भनेको के हो? उदाहरण दिनुहोस्।</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">१ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-blue-400">
        <strong>उत्तर:</strong> कुनै तथ्याङ्कमा कुनै विशेष मान, सङ्ख्या वा वस्तु कति पटक दोहोरिएको छ, त्यो दोहोरिने सङ्ख्यालाई त्यसको <strong>बारम्बारता (Frequency - $f$)</strong> भनिन्छ। जस्तै: परीक्षामा १५ अङ्क पाउने विद्यार्थी ४ जना छन् भने १५ को बारम्बारता ४ हुन्छ।
      </p>
    </div>

    <!-- Q3 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ३: सङ्ख्याहरू ५, ९, १३ र १७ का लागि मिलान चिह्न (Tally marks) कसरी लेखिन्छ?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">१ अङ्क</span>
      </div>
      <div class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-blue-400 space-y-1">
        <div>• ५ = <s>||||</s> (४ ठाडो धर्सालाई पाँचौँले छड्के काट्ने)</div>
        <div>• ९ = <s>||||</s> ||||</div>
        <div>• १३ = <s>||||</s> <s>||||</s> |||</div>
        <div>• १७ = <s>||||</s> <s>||||</s> <s>||||</s> ||</div>
      </div>
    </div>

    <!-- Q4 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ४: साधारण स्तम्भ चित्र बनाउँदा $X$-अक्ष र $Y$-अक्षमा के-के राखिन्छ?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">१ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-blue-400">
        <strong>उत्तर:</strong> तेर्सो $X$-अक्षमा अध्ययन गरिने विषय वा शीर्षकहरू (जस्तै: दिन, कक्षा, विषय, साधन) राखिन्छ र ठाडो $Y$-अक्षमा तिनीहरूको बारम्बारता वा परिमाण राखिन्छ।
      </p>
    </div>

    <!-- Q5 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ५: स्तम्भ चित्रमा सबै स्तम्भहरूको चौडाइ किन समान हुनुपर्छ?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">१ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-blue-400">
        <strong>उत्तर:</strong> स्तम्भको मान त्यसको उचाइले मात्र प्रतिनिधित्व गर्ने भएकाले चौडाइ फरक परेमा दृश्य तुलनामा भ्रम हुन सक्छ। त्यसैले सही र निष्पक्ष तुलनाका लागि सबै स्तम्भको चौडाइ समान हुनुपर्छ।
      </p>
    </div>
  </div>

  <!-- TIER 2: UNDERSTANDING & APPLICATION (6 Questions) -->
  <div class="space-y-4">
    <div class="flex items-center gap-2 text-emerald-700 font-black text-base border-b border-emerald-200 pb-2">
      <span class="w-7 h-7 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-bold">T2</span>
      <h4>तह २: बोधात्मक तथा मध्यम स्तरका प्रश्नहरू (Understanding & Application — ६ प्रश्न)</h4>
    </div>

    <!-- Q6 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ६: प्राथमिक तथ्याङ्क र द्वितीयक तथ्याङ्क बीचको भिन्नता उदाहरणसहित स्पष्ट पार्नुहोस्।</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">२ अङ्क</span>
      </div>
      <div class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-emerald-400 space-y-1">
        <p>• <strong>प्राथमिक तथ्याङ्क:</strong> अनुसन्धानकर्ता आफैँले स्थलगत सोधपुछ वा अवलोकन गरी सङ्कलन गरेको मौलिक तथ्याङ्क (जस्तै: कक्षाका साथीहरूको उचाइ आफैँले नाप्नु)।</p>
        <p>• <strong>द्वितीयक तथ्याङ्क:</strong> अरू कसैले पहिले नै प्रकाशित गरेको स्रोतबाट लिइएको तथ्याङ्क (जस्तै: विद्यालयको हाजिरी खाता वा जनगणना प्रतिवेदनबाट लिइएको विवरण)।</p>
      </div>
    </div>

    <!-- Q7 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ७: स्तम्भ चित्रमा स्केल (Scale) किन आवश्यक पर्छ? उदाहरणसहित प्रष्ट पार्नुहोस्।</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">२ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-emerald-400 leading-relaxed">
        <strong>उत्तर:</strong> यदि तथ्याङ्कमा मानहरू ५० वा १०० छन् भने ग्राफ पेपरमा ५० वा १०० से.मि. को रेखा कोर्न सम्भव हुँदैन। त्यसैले ठूला मानहरूलाई ग्राफमा अटाउन $1\text{ cm} = 10\text{ units}$ जस्ता समानुपातिक स्केल मान्नुपर्छ जसले गर्दा १० से.मि. को उचाइले १०० को मान प्रतिनिधित्व गर्न सक्छ।
      </p>
    </div>

    <!-- Q8 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ८: एउटा स्तम्भ चित्रमा गणितको स्तम्भ ९ से.मि. अग्लो छ र स्केल $1\text{ cm} = 10\text{ marks}$ छ भने प्राप्ताङ्क कति हुन्छ?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">२ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-emerald-400">
        <strong>समाधान:</strong> \(\text{प्राप्ताङ्क} = \text{स्तम्भको उचाइ} \times \text{स्केल} = 9\text{ cm} \times 10 = \mathbf{90\text{ अङ्क}}\)।
      </p>
    </div>

    <!-- Q9 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ९: मिलान चिह्नमा पाँचौँ गणनालाई चारवटा धर्सामाथि छड्के काट्नुको वैज्ञानिक फाइदा के हो?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">२ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-emerald-400">
        <strong>उत्तर:</strong> पाँच-पाँचको समूह बनाउँदा ठूलो तथ्याङ्कलाई एक-एक गरी गन्नुको सट्टा ५, १०, १५, २० भन्दै छिटो, सहज र बिना कुनै गल्ती तुरुन्त जोड्न सकिन्छ।
      </p>
    </div>

    <!-- Q10 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न १०: बारम्बारता तालिका र स्तम्भ चित्र बीचको मुख्य भिन्नता के हो?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">२ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-emerald-400">
        <strong>उत्तर:</strong> बारम्बारता तालिकामा तथ्याङ्कलाई सङ्ख्यात्मक रूपमा प्रस्तुत गरिन्छ भने स्तम्भ चित्रमा सोही तथ्याङ्कलाई आयताकार खम्बाहरूको उचाइको माध्यमबाट दृश्य रूपमा (Visually) देखाइन्छ, जसले गर्दा हेर्नासाथ तुलना गर्न धेरै सजिलो हुन्छ।
      </p>
    </div>

    <!-- Q11 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-2">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न ११: साधारण स्तम्भ चित्र बनाउँदा ध्यान दिनुपर्ने ४ वटा अनिवार्य नियमहरू के-के हुन्?</span>
        <span class="text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-mono">२ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-emerald-400">
        <strong>उत्तर:</strong> १. स्पष्ट X-अक्ष र Y-अक्ष कोर्नु, २. मुख्य शीर्षक लेख्नु, ३. प्रत्येक स्तम्भको चौडाइ बराबर बनाउनु, र ४. दुई स्तम्भबिचको खाली दूरी सधैँ बराबर राख्नु।
      </p>
    </div>
  </div>

  <!-- TIER 3: HIGHER ABILITY & PROBLEM SOLVING (5 Questions) -->
  <div class="space-y-4">
    <div class="flex items-center gap-2 text-purple-700 font-black text-base border-b border-purple-200 pb-2">
      <span class="w-7 h-7 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs font-bold">T3</span>
      <h4>तह ३: उच्च दक्षता तथा समस्या समाधान (Higher Ability — ५ प्रश्न)</h4>
    </div>

    <!-- Q12 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न १२: वार्षिक खर्च स्तम्भ चित्र प्रतिशत विश्लेषण समस्या (पाठ्यपुस्तक पृष्ठ २३३)</span>
        <span class="text-[11px] bg-purple-100 text-purple-700 px-2 py-0.5 rounded font-mono">४ अङ्क</span>
      </div>
      <div class="text-xs md:text-sm text-slate-700 pl-4 border-l-2 border-purple-500 space-y-1.5">
        <p>एउटा परिवारको वार्षिक खर्च: खाना ५० हजार, कपडा १५ हजार, स्वास्थ्य १५ हजार, शिक्षा २० हजार, घरभाडा ३० हजार, अन्य १५ हजार छ।</p>
        <p>• <strong>कुल खर्च:</strong> \(50 + 15 + 15 + 20 + 30 + 15 = 140\text{ हजार (१ लाख ४० हजार रू.)}\)</p>
        <p>• <strong>खानामा खर्च प्रतिशत:</strong> \(\frac{50}{140} \times 100\% = \frac{5}{14} \times 100\% = \mathbf{35.71\%}\)</p>
        <p>• <strong>शिक्षामा खर्च प्रतिशत:</strong> \(\frac{20}{140} \times 100\% = \frac{1}{7} \times 100\% = \mathbf{14.29\%}\)</p>
      </div>
    </div>

    <!-- Q13 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न १३: गलत स्तम्भ चित्रमा त्रुटि पहिचान र सुधार विधि</span>
        <span class="text-[11px] bg-purple-100 text-purple-700 px-2 py-0.5 rounded font-mono">३ अङ्क</span>
      </div>
      <div class="text-xs md:text-sm text-slate-700 pl-4 border-l-2 border-purple-500 space-y-1">
        <p><strong>समस्या:</strong> रमेशले बनाएको स्तम्भ चित्रमा स्तम्भ १ को चौडाइ २ से.मि., स्तम्भ २ को चौडाइ ३.५ से.मि. छ र दुई स्तम्भबिचको दूरी फरक-फरक छ।</p>
        <p><strong>त्रुटिहरू:</strong> १. स्तम्भहरूको चौडाइ असमान छ। २. स्तम्भबिचको खाली ठाउँ असमान छ।</p>
        <p><strong>सुधार:</strong> सबै स्तम्भहरूको चौडाइ बराबर (जस्तै समान २ से.मि.) बनाउनुपर्छ र सबै स्तम्भहरू बिचको दूरी समान (जस्तै १ से.मि.) छोड्नुपर्छ।</p>
      </div>
    </div>

    <!-- Q14 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न १४: खेलकुद प्राथमिकता सर्वेक्षण र स्केल निर्धारण</span>
        <span class="text-[11px] bg-purple-100 text-purple-700 px-2 py-0.5 rounded font-mono">३ अङ्क</span>
      </div>
      <div class="text-xs md:text-sm text-slate-700 pl-4 border-l-2 border-purple-500 space-y-1">
        <p>५० जना विद्यार्थीमा: फुटबल २०, क्रिकेट १५, भलिबल १० र ब्याडमिन्टन ५ जना छन्।</p>
        <p>• ब्याडमिन्टनको बारम्बारता $= 50 - (20 + 15 + 10) = 5$ जना।</p>
        <p>• अधिकतम मान २० भएकाले $Y$-अक्षमा <strong>१ से.मि. = ५ जना</strong> को स्केल राख्दा खम्बाहरू १ से.मि. देखि ४ से.मि. सम्मका स्पष्ट बन्दछन्।</p>
      </div>
    </div>

    <!-- Q15 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न १५: सहरको जनसङ्ख्या वृद्धि दर तुलना (पृष्ठ २३२)</span>
        <span class="text-[11px] bg-purple-100 text-purple-700 px-2 py-0.5 rounded font-mono">४ अङ्क</span>
      </div>
      <div class="text-xs md:text-sm text-slate-700 pl-4 border-l-2 border-purple-500 space-y-1">
        <p>२०७० मा ३५ लाख, २०७१ मा ४० लाख, २०७२ मा ५० लाख, २०७३ मा ६५ लाख, २०७४ मा ९० लाख, २०७५ मा १०० लाख।</p>
        <p>• २०७१ मा वृद्धि: $40 - 35 = 5$ लाख (सबैभन्दा थोरै वृद्धि ✓)</p>
        <p>• २०७४ मा वृद्धि: $90 - 65 = 25$ लाख (सबैभन्दा धेरै वृद्धि)</p>
        <p>• ६ वर्षको कुल जनसङ्ख्या वृद्धि $= 100 - 35 = 65$ लाख।</p>
      </div>
    </div>

    <!-- Q16 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3">
      <div class="font-bold text-slate-800 text-sm flex items-center justify-between">
        <span>प्रश्न १६: प्राथमिक तथ्याङ्क सङ्कलनको स्थलगत विधि र विश्वसनीयता</span>
        <span class="text-[11px] bg-purple-100 text-purple-700 px-2 py-0.5 rounded font-mono">२ अङ्क</span>
      </div>
      <p class="text-xs md:text-sm text-slate-600 pl-4 border-l-2 border-purple-500">
        <strong>उत्तर:</strong> प्राथमिक तथ्याङ्क सङ्कलन गर्दा: १. उद्देश्यको स्पष्टता, २. तटस्थता र पूर्वाग्रहरहित प्रश्न सोध्नु, र ३. संकलित आँकडालाई तत्कालै ट्याली मार्कको सहायताले अभिलेख राख्नुपर्छ ताकि कुनै सूचना नछुटोस्।
      </p>
    </div>
  </div>
</div>
<!-- ================= END TAB 3 ================= -->
'''

html_tab4 = r'''
<!-- ================= CHAPTER 20: TAB 4 (SELF-ASSESSMENT QUIZ) ================= -->
<div id="ch20-view-quiz" class="hidden space-y-6">
  <!-- Quiz Top Score Banner -->
  <div class="bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-800 rounded-3xl p-6 text-white shadow-xl flex flex-wrap items-center justify-between gap-4">
    <div>
      <div class="flex items-center gap-2 text-xs font-bold text-cyan-300 mb-1">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
        अध्याय २० स्वमूल्याङ्कन परीक्षा (Self-Assessment Quiz)
      </div>
      <h3 class="text-xl md:text-2xl font-black">तथ्याङ्कशास्त्र वस्तुगत बहुवैकल्पिक परीक्षा (१० प्रश्न)</h3>
      <p class="text-xs text-blue-100 mt-1">प्रत्येक प्रश्नको सही उत्तर छानेर तुरुन्त पृष्ठपोषण र अङ्क प्राप्त गर्नुहोस्</p>
    </div>

    <div class="flex items-center gap-4 bg-white/10 backdrop-blur px-5 py-3 rounded-2xl border border-white/20">
      <div class="text-right">
        <span class="text-[11px] text-blue-200 block font-bold">तपाईंको प्राप्ताङ्क</span>
        <span id="ch20-quiz-score" class="text-2xl md:text-3xl font-black text-cyan-300">० / १०</span>
      </div>
      <button onclick="resetCh20Quiz()" class="px-3.5 py-2 rounded-xl bg-white/20 hover:bg-white/30 text-xs font-bold transition flex items-center gap-1.5 border border-white/30 cursor-pointer">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        पुनः सुरु गर्नुहोस्
      </button>
    </div>
  </div>

  <!-- Quiz Questions Container -->
  <div id="ch20-quiz-container" class="space-y-4">
    <!-- Rendered dynamically via ch20_script.js -->
  </div>
</div>
<!-- ================= END TAB 4 ================= -->
'''

with open('scratch/ch20_tab3.html', 'w', encoding='utf-8') as f:
    f.write(html_tab3.strip() + '\n')

with open('scratch/ch20_tab4.html', 'w', encoding='utf-8') as f:
    f.write(html_tab4.strip() + '\n')

print("scratch/ch20_tab3.html and scratch/ch20_tab4.html created successfully!")
