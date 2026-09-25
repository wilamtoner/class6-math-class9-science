# -*- coding: utf-8 -*-
import os
from generate_ch5_html import get_ch5_html

with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar Chapter 5 button
old_btn = """<button onclick="alert('पाठ ५ को विस्तृत नोट notes/05_dashamlav_decimals.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ ५: दशमलव</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

new_btn = """<button id="side-ch-5" onclick="switchChapter(5)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium">
          <span>पाठ ५: दशमलव</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

if old_btn in html:
    html = html.replace(old_btn, new_btn)
    print("Replaced sidebar button successfully!")
else:
    print("Warning: old_btn not found directly, checking partial...")
    # Find button containing 'पाठ ५'
    pos_btn = html.find('पाठ ५')
    start_b = html.rfind('<button', 0, pos_btn)
    end_b = html.find('</button>', pos_btn) + 9
    print("Found button:\n", html[start_b:end_b])
    html = html[:start_b] + new_btn + html[end_b:]
    print("Replaced via index slice!")

# 2. Insert Chapter 5 View HTML before </main>
ch5_html = get_ch5_html()
end_marker = "<!-- ================= END OF CHAPTER 4 VIEW ================= -->"
if end_marker in html:
    pos_marker = html.find(end_marker) + len(end_marker)
    html = html[:pos_marker] + "\n" + ch5_html + html[pos_marker:]
    print("Inserted chapter-view-5 successfully!")
else:
    print("Error: END OF CHAPTER 4 VIEW marker not found!")

# 3. Update switchChapter function
old_switch = """function switchChapter(chNum) {
      const b1 = document.getElementById('side-ch-1');
      const b2 = document.getElementById('side-ch-2');
      const b3 = document.getElementById('side-ch-3');
      const b4 = document.getElementById('side-ch-4');
      const v1 = document.getElementById('chapter-view-1');
      const v2 = document.getElementById('chapter-view-2');
      const v3 = document.getElementById('chapter-view-3');
      const v4 = document.getElementById('chapter-view-4');

      const sideActive = 'w-full text-left px-3.5 py-2.5 rounded-xl transition flex items-center justify-between text-xs md:text-sm bg-blue-600 text-white font-bold shadow-sm';
      const sideInactive = 'w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium';

      if (b1) b1.className = (chNum === 1) ? sideActive : sideInactive;
      if (b2) b2.className = (chNum === 2) ? sideActive : sideInactive;
      if (b3) b3.className = (chNum === 3) ? sideActive : sideInactive;
      if (b4) b4.className = (chNum === 4) ? sideActive : sideInactive;

      if (v1) v1.classList.toggle('hidden', chNum !== 1);
      if (v2) v2.classList.toggle('hidden', chNum !== 2);
      if (v3) v3.classList.toggle('hidden', chNum !== 3);
      if (v4) v4.classList.toggle('hidden', chNum !== 4);

      if (chNum === 1) {
        setTab('concepts');
        if (window.MathJax && MathJax.Hub && v1) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v1]);
      } else if (chNum === 2) {
        setTabCh2('concepts');
        if (window.MathJax && MathJax.Hub && v2) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v2]);
      } else if (chNum === 3) {
        setTabCh3('concepts');
        if (window.MathJax && MathJax.Hub && v3) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v3]);
      } else if (chNum === 4) {
        setTabCh4('concepts');
        if (window.MathJax && MathJax.Hub && v4) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v4]);
      }
    }"""

new_switch = """function switchChapter(chNum) {
      const b1 = document.getElementById('side-ch-1');
      const b2 = document.getElementById('side-ch-2');
      const b3 = document.getElementById('side-ch-3');
      const b4 = document.getElementById('side-ch-4');
      const b5 = document.getElementById('side-ch-5');
      const v1 = document.getElementById('chapter-view-1');
      const v2 = document.getElementById('chapter-view-2');
      const v3 = document.getElementById('chapter-view-3');
      const v4 = document.getElementById('chapter-view-4');
      const v5 = document.getElementById('chapter-view-5');

      const sideActive = 'w-full text-left px-3.5 py-2.5 rounded-xl transition flex items-center justify-between text-xs md:text-sm bg-blue-600 text-white font-bold shadow-sm';
      const sideInactive = 'w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium';

      if (b1) b1.className = (chNum === 1) ? sideActive : sideInactive;
      if (b2) b2.className = (chNum === 2) ? sideActive : sideInactive;
      if (b3) b3.className = (chNum === 3) ? sideActive : sideInactive;
      if (b4) b4.className = (chNum === 4) ? sideActive : sideInactive;
      if (b5) b5.className = (chNum === 5) ? sideActive : sideInactive;

      if (v1) v1.classList.toggle('hidden', chNum !== 1);
      if (v2) v2.classList.toggle('hidden', chNum !== 2);
      if (v3) v3.classList.toggle('hidden', chNum !== 3);
      if (v4) v4.classList.toggle('hidden', chNum !== 4);
      if (v5) v5.classList.toggle('hidden', chNum !== 5);

      if (chNum === 1) {
        setTab('concepts');
        if (window.MathJax && MathJax.Hub && v1) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v1]);
      } else if (chNum === 2) {
        setTabCh2('concepts');
        if (window.MathJax && MathJax.Hub && v2) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v2]);
      } else if (chNum === 3) {
        setTabCh3('concepts');
        if (window.MathJax && MathJax.Hub && v3) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v3]);
      } else if (chNum === 4) {
        setTabCh4('concepts');
        if (window.MathJax && MathJax.Hub && v4) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v4]);
      } else if (chNum === 5) {
        setTabCh5('concepts');
        if (window.MathJax && MathJax.Hub && v5) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v5]);
      }
    }"""

if old_switch in html:
    html = html.replace(old_switch, new_switch)
    print("Updated switchChapter successfully!")
else:
    print("Error: old_switch not found!")

# 4. Add setTabCh5, setExerciseCh5, quiz functions
ch5_js = """
    function setTabCh5(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch5-view-' + t);
        const btn = document.getElementById('ch5-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch5-view-' + tabName);
      const activeBtn = document.getElementById('ch5-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && MathJax.Hub && activeView) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh5(exId) {
      const allEx = ['ex5_1', 'ex5_2', 'ex5_3'];
      allEx.forEach(e => {
        const sec = document.getElementById('ch5-sec-' + e);
        const pill = document.getElementById('ch5-pill-' + e);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap';
      });
      const curSec = document.getElementById('ch5-sec-' + exId);
      const curPill = document.getElementById('ch5-pill-' + exId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap';
      if (window.MathJax && MathJax.Hub && curSec) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, curSec]);
      }
    }

    const ch5QuizData = [
      { correct: 1, exp: "हरमा १०० (२ वटा शून्य) भएकाले दायाँबाट २ स्थान बायाँ बिन्दु बस्छ: $\\\\frac{7}{100} = 0.07$।" },
      { correct: 1, exp: "१० ले गुणन गर्दा दशमलव बिन्दु १ स्थान दायाँ सर्दछ: $३.४५ \\\\times १० = ३४.५$।" },
      { correct: 0, exp: "१०० ले भाग गर्दा दशमलव बिन्दु २ स्थान बायाँ सर्दछ: $२५.४ \\\\div १०० = ०.२५४$।" },
      { correct: 0, exp: "दशमलव बेवास्ता गरी गुणन गर्दा $५ \\\\times २ = १०$, कुल २ अङ्क अघि बिन्दु राख्दा $०.१० = ०.१$।" }
    ];

    function checkQuizCh5(qIdx, selected) {
      const data = ch5QuizData[qIdx];
      const expBox = document.getElementById('ch5-qexp-' + qIdx);
      const badge = document.getElementById('ch5-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch5-qbtn-' + qIdx + '-' + i);
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
        if (window.MathJax && MathJax.Hub) {
          MathJax.Hub.Queue(["Typeset", MathJax.Hub, expBox]);
        }
      }
    }

    function resetQuizCh5() {
      for (let q = 0; q < 4; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch5-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium';
          }
        }
        const badge = document.getElementById('ch5-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch5-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }
"""

pos_quiz4 = html.find('function resetQuizCh4()')
if pos_quiz4 != -1:
    pos_end_fn = html.find('}', html.find('}', pos_quiz4) + 1) + 1
    html = html[:pos_end_fn] + "\n" + ch5_js + html[pos_end_fn:]
    print("Added Chapter 5 JS functions successfully!")
else:
    print("Warning: function resetQuizCh4 not found directly, appending before URLParams...")
    pos_url = html.find('const urlParams = new URLSearchParams')
    html = html[:pos_url] + ch5_js + "\n    " + html[pos_url:]
    print("Inserted before urlParams!")

# 5. Add URL deep-linking support for Chapter 5
old_url_chk = "const urlParams = new URLSearchParams(window.location.search);\n    if (urlParams.get('ch') === '4') {"
new_url_chk = """const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('ch') === '5') {
      switchChapter(5);
      if (urlParams.get('tab')) {
        setTabCh5(urlParams.get('tab'));
      }
      if (urlParams.get('ex')) {
        setExerciseCh5(urlParams.get('ex'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh5(0, 1);
          checkQuizCh5(1, 1);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (urlParams.get('ch') === '4') {"""

if old_url_chk in html:
    html = html.replace(old_url_chk, new_url_chk)
    print("Added deep-linking for ch=5 successfully!")
else:
    print("Warning: old_url_chk not found!")

# Save to both primary and mirrored files
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(html)

art_path = '/home/nepal/.gemini/antigravity/brain/fc1605f3-8b2b-459a-809e-54639da37eba/interactive_math_guide.html'
with open(art_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved both files successfully! New file size:", len(html), "bytes")
