# -*- coding: utf-8 -*-
wt_path = "/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66/walkthrough.md"
with open(wt_path, "r", encoding="utf-8") as f:
    wt = f.read()

new_sim_details = """
---

### ५. पेपर्ड मथ प्राकृतिक छनोट सिमुलेटर पूर्ण कार्यान्वयन (Peppered Moth Simulator Implementation)

प्रयोगकर्ताको अनुरोध अनुसार **पेपर्ड मथ प्राकृतिक छनोट सिमुलेटर (Peppered Moth Natural Selection Simulator)** लाई पूर्ण रूपमा दृश्यमान, अन्तरक्रियात्मक र जीवित बनाइएको छ:

1. **यथार्थपरक भेक्टर ट्रङ्क र १२ पेपर्ड मथहरू (Realistic SVG Trunk & 12 Moths):**
   - **सफा वातावरण (Clean Lichen Bark):** हल्का हरियो-क्रिम रङका प्राकृतिक लाइकेन (Lichen) पत्रहरूले ढाकिएको काण्ड। यसमा १० ओटा सेता मथहरू पूर्ण छलावरण (Camouflage) मिली लुक्छन् भने २ ओटा कालो मथहरू प्रस्ट देखिन्छन्।
   - **प्रदूषित औद्योगिक क्षेत्र (Sooty Bark):** कोइला र धुवाँको कालो मुस्लो (Soot) ले ढाकिएको काण्ड। यसमा १० ओटा काला मथहरू छलावरण मिली लुक्छन् भने २ ओटा सेता मथहरू प्रस्ट देखिन्छन्।
   - पेपर्ड मथको शारीरिक संरचना (Forewings, Hindwings, Peppered speckles, segmented body, feathery antennae) दुरुस्त SVG मा बनाइएको।

2. **अन्तरक्रियात्मक शिकारी चराको खेल (Click-to-Hunt Mechanics & Audio Synthesis):**
   - कुनै पनि मथमा क्लिक गर्दा शिकारी चराले झम्टेको रातो स्ट्राइक रिङ र `+१ शिकार!` एनिमेसन देखा पर्छ।
   - ब्राउजरको नेटिभ `Web Audio API` मार्फत कुनै बाह्य इन्टरनेट वा अडियो फाइलविना नै सफ्टवेयर सिन्थेसाइज्ड चाइम र स्वीप साउन्ड उत्पादन हुन्छ (१००% अफलाइन)।
   - **१० सेकेन्ड शिकार चुनौती (10s Predator Challenge):** १० सेकेन्डको काउन्टडाउनमा विद्यार्थीले आफैँ शिकारी चरा बनेर मथहरू शिकार गर्न सक्छन्। समय सकिएपछि कति ओटा प्रस्ट देखिने र कति ओटा छलावरण मिलेका मथ शिकार भए भन्ने वैज्ञानिक विश्लेषण प्रस्तुत हुन्छ।

3. **पुस्तागत विकासक्रम (Next Generation ➔ & Population Evolution):**
   - 'अर्को पुस्ता' थिच्दा चराको छायाँ काण्डमा उडेर गएको एनिमेसन र स्वीप साउन्ड आउँछ।
   - प्रस्ट देखिने मथहरू शिकार भएर घट्छन् र बाँचेका अनुकूलित मथहरूले सन्तान वृद्धि गर्छन्।
   - पुस्तागत विकासक्रम ट्रयाक (Timeline Dots १ देखि १०) मा क्रमिक रूपमा अगाडि बढ्छ।

4. **अस्थिपञ्जर समधर्मिता र उत्परिवर्तनका गतिशील रेखाचित्रहरू (Dynamic SVGs):**
   - **Mode 1 (Homology):** मानिस, चीता/बिरालो, ह्वेल, चमेरो र घोडाको अग्रअङ्गका समधर्मी हाडहरू (Humerus, Radius, Ulna, Carpals, Phalanges) को गतिशील SVG प्रस्तुति।
   - **Mode 3 (Mutation):** पोलिड्याक्टिली (हातमा ६ औँला), सिकल सेल आरबीसी, अल्बिनिजम, र ह्युगो डी भ्रिजको इभनिङ प्रिमरोजको गतिशील तुलनात्मक SVG रेखाचित्रहरू।

---

### ६. नयाँ स्क्रिनसट प्रमाणहरू (Updated Visual Artifacts)

- **पेपर्ड मथ सिमुलेटर - प्रदूषित औद्योगिक वातावरण (कालो मथ अनुकूलित):**
  `shot_c9u4_selection_working.png`
  ![Polluted Sooty Bark Simulator](/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66/shot_c9u4_selection_working.png)

- **पेपर्ड मथ सिमुलेटर - सफा वातावरण (सेतो मथ अनुकूलित):**
  `shot_c9u4_selection.png`
  ![Clean Lichen Bark Simulator](/home/nepal/.gemini/antigravity/brain/8ff01837-428e-469e-90c5-2e5217c89f66/shot_c9u4_selection.png)
"""

wt = wt.replace("a302d48670945412f4499e71f8e1bc6b", "77f3a1857b5af43858e6e126b62f1e6a")
wt = wt + new_sim_details

# Verify no double virama
assert '\u094d\u094d' not in wt

with open(wt_path, "w", encoding="utf-8") as f:
    f.write(wt)

print("Updated walkthrough.md successfully.")
