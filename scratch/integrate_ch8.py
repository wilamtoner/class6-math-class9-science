# -*- coding: utf-8 -*-
"""
Integrates Chapter 8 (Unitary Method) into कक्षा_६_गणित_डिजिटल_साथी.html,
index.html, and interactive_math_guide.html.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from generate_ch8_html import get_ch8_html

with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar Chapter 8 button
old_btn = """<button onclick="alert('पाठ ८ को विस्तृत नोट notes/08_aikik_niyam_unitary_method.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ ८: ऐकिक नियम</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

new_btn = """<button id="side-ch-8" onclick="switchChapter(8)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium cursor-pointer">
          <span>पाठ ८: ऐकिक नियम</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

if old_btn in html:
    html = html.replace(old_btn, new_btn)
    print("Replaced Chapter 8 sidebar button directly!")
else:
    pos_btn = html.find('पाठ ८: ऐकिक नियम')
    if pos_btn != -1:
        start_b = html.rfind('<button', 0, pos_btn)
        end_b = html.find('</button>', pos_btn) + 9
        html = html[:start_b] + new_btn + html[end_b:]
        print("Replaced via index slice!")
    else:
        print("Warning: Chapter 8 sidebar button not found!")

# 2. Insert Chapter 8 View HTML before </main> (after END OF CHAPTER 7 VIEW)
ch8_html = get_ch8_html()
end_ch7 = "<!-- ================= END OF CHAPTER 7 VIEW ================= -->"
if end_ch7 in html:
    pos_marker = html.find(end_ch7) + len(end_ch7)
    html = html[:pos_marker] + "\n" + ch8_html + html[pos_marker:]
    print("Inserted chapter-view-8 successfully!")
else:
    print("Error: END OF CHAPTER 7 VIEW marker not found!")
    sys.exit(1)

# 3. Update switchChapter function
old_switch_target = "const b7 = document.getElementById('side-ch-7');"
new_switch_b = "const b7 = document.getElementById('side-ch-7');\n      const b8 = document.getElementById('side-ch-8');"

old_view_target = "const v7 = document.getElementById('chapter-view-7');"
new_view_v = "const v7 = document.getElementById('chapter-view-7');\n      const v8 = document.getElementById('chapter-view-8');"

old_class_b = "if (b7) b7.className = (chNum === 7) ? sideActive : sideInactive;"
new_class_b = "if (b7) b7.className = (chNum === 7) ? sideActive : sideInactive;\n      if (b8) b8.className = (chNum === 8) ? sideActive : sideInactive;"

old_toggle_v = "if (v7) v7.classList.toggle('hidden', chNum !== 7);"
new_toggle_v = "if (v7) v7.classList.toggle('hidden', chNum !== 7);\n      if (v8) v8.classList.toggle('hidden', chNum !== 8);"

old_ch7_branch = """} else if (chNum === 7) {
        setTabCh7('concepts');
        runCh7Calc();
        if (window.MathJax && window.MathJax.Hub && v7) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v7]);
      }"""

new_ch8_branch = """} else if (chNum === 7) {
        setTabCh7('concepts');
        runCh7Calc();
        if (window.MathJax && window.MathJax.Hub && v7) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v7]);
      } else if (chNum === 8) {
        setTabCh8('concepts');
        runCh8Calc();
        if (window.MathJax && window.MathJax.Hub && v8) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v8]);
      }"""

html = html.replace(old_switch_target, new_switch_b, 1)
html = html.replace(old_view_target, new_view_v, 1)
html = html.replace(old_class_b, new_class_b, 1)
html = html.replace(old_toggle_v, new_toggle_v, 1)
html = html.replace(old_ch7_branch, new_ch8_branch, 1)
print("Updated switchChapter for Chapter 8!")

# 4. Add Chapter 8 JavaScript logic at the top level
ch8_js = """
    function setTabCh8(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch8-view-' + t);
        const btn = document.getElementById('ch8-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
      });
      const activeView = document.getElementById('ch8-view-' + tabName);
      const activeBtn = document.getElementById('ch8-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh8(secId) {
      ['sec1', 'sec2', 'sec3'].forEach(s => {
        const sec = document.getElementById('ch8-sec-' + s);
        const pill = document.getElementById('ch8-pill-' + s);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer';
      });
      const curSec = document.getElementById('ch8-sec-' + secId);
      const curPill = document.getElementById('ch8-pill-' + secId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap cursor-pointer';
      if (window.MathJax && window.MathJax.Hub && curSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, curSec]);
      }
    }

    function setCh8Preset(q1, c1, q2) {
      const inQ1 = document.getElementById('ch8-in-q1');
      const inC1 = document.getElementById('ch8-in-c1');
      const inQ2 = document.getElementById('ch8-in-q2');
      if (inQ1) inQ1.value = q1;
      if (inC1) inC1.value = c1;
      if (inQ2) inQ2.value = q2;
      runCh8Calc();
    }

    function runCh8Calc() {
      const inQ1 = document.getElementById('ch8-in-q1');
      const inC1 = document.getElementById('ch8-in-c1');
      const inQ2 = document.getElementById('ch8-in-q2');
      const res = document.getElementById('ch8-calc-res');
      if (!res) return;

      const q1 = parseFloat(inQ1 ? inQ1.value : 0) || 0;
      const c1 = parseFloat(inC1 ? inC1.value : 0) || 0;
      const q2 = parseFloat(inQ2 ? inQ2.value : 0) || 0;

      if (q1 <= 0) {
        res.innerHTML = '<div class="text-amber-300 font-bold text-sm">कृपया सुरुवाती वस्तुको मान्य सङ्ख्या (१ वा सोभन्दा बढी) प्रविष्ट गर्नुहोस्।</div>';
        return;
      }

      const unitCost = c1 / q1;
      const totalCost2 = unitCost * q2;

      const statusHtml = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-indigo-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-indigo-500/20 text-indigo-300 font-bold text-xs border border-indigo-400/30">ऐकिक नियम प्रत्यक्ष गणना नतिजा</span>
          <span class="text-xs text-blue-200">१ एकाइको दर = रु. ${unitCost.toFixed(2).replace(/\\\\.00$/, '')}</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">सुरुवाती परिमाण (Q₁)</span><span class="text-lg font-mono font-bold">${q1}</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">सुरुवाती मूल्य (C₁)</span><span class="text-lg font-mono font-bold">रु. ${c1}</span></div>
          <div class="bg-blue-500/20 border border-blue-400/40 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">१ एकाइको मूल्य (दर)</span><span class="text-lg font-mono font-bold text-blue-300">रु. ${unitCost.toFixed(2).replace(/\\\\.00$/, '')}</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">माग परिमाण (${q2}) को मूल्य</span><span class="text-lg font-mono font-bold text-emerald-300">रु. ${totalCost2.toFixed(2).replace(/\\\\.00$/, '')}</span></div>
        </div>
        <p class="text-xs text-blue-100 bg-white/5 p-2.5 rounded-lg mt-2 leading-relaxed">
          <strong>चरणबद्ध समाधान विधि:</strong><br>
          १. भाग क्रिया (१ एकाइको मान निकाल्ने): ${q1} वटाको मूल्य = रु. ${c1} $\\\\Rightarrow$ १ वटाको मूल्य = $\\\\frac{${c1}}{${q1}} =$ <strong>रु. ${unitCost.toFixed(2).replace(/\\\\.00$/, '')}</strong><br>
          २. गुणन क्रिया (${q2} वटाको मान निकाल्ने): ${q2} वटाको मूल्य = ${unitCost.toFixed(2).replace(/\\\\.00$/, '')} $\\\\times$ ${q2} = <strong>रु. ${totalCost2.toFixed(2).replace(/\\\\.00$/, '')}</strong>
        </p>
      `;
      res.innerHTML = statusHtml;
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      }
    }

    const ch8QuizData = [
      { correct: 2, exp: "१ ओटाको मूल्य $= \\\\frac{75}{5} = \\\\text{रु. } 15$।" },
      { correct: 0, exp: "१ दर्जन $= 12$ ओटा, १ ओटाको $= \\\\frac{480}{12} = 40$, ८ ओटाको $= 40 \\\\times 8 = \\\\text{रु. } 320$।" },
      { correct: 1, exp: "१ ओटा ब्याटको $= \\\\frac{900}{6} = 150$, ४ ओटाको $= 150 \\\\times 4 = \\\\text{रु. } 600$।" },
      { correct: 2, exp: "१ ओटा कुर्सीको $= \\\\frac{4800}{4} = 1200$, ७ ओटाको $= 1200 \\\\times 7 = \\\\text{रु. } 8,400$।" },
      { correct: 1, exp: "ऐकिक नियममा पहिले भाग गरी १ एकाइको मान निकालिन्छ र त्यसपछि गुणन गरी माग गरिएको सङ्ख्याको मान निकालिन्छ।" }
    ];

    function checkQuizCh8(qIdx, selected) {
      const data = ch8QuizData[qIdx];
      const expBox = document.getElementById('ch8-qexp-' + qIdx);
      const badge = document.getElementById('ch8-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch8-qbtn-' + qIdx + '-' + i);
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
        }
      }
    }

    function resetQuizCh8() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch8-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch8-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch8-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh8 = setTabCh8;
    window.setExerciseCh8 = setExerciseCh8;
    window.setCh8Preset = setCh8Preset;
    window.runCh8Calc = runCh8Calc;
    window.checkQuizCh8 = checkQuizCh8;
    window.resetQuizCh8 = resetQuizCh8;
"""

# Place ch8_js before "const urlParams = new URLSearchParams"
pos_url = html.find('const urlParams = new URLSearchParams')
if pos_url != -1:
    html = html[:pos_url] + ch8_js + "\n    " + html[pos_url:]
    print("Added Chapter 8 JS functions at top level!")
else:
    print("Error: const urlParams not found!")
    sys.exit(1)

# 5. Add URL deep-linking and default chapter 8
old_url_chk = "const activeChParam = urlParams.get('ch') || '7';"
new_url_chk = """const activeChParam = urlParams.get('ch') || '8';
    if (activeChParam === '8') {
      switchChapter(8);
      if (urlParams.get('tab')) {
        setTabCh8(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh8(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh8(0, 2);
          checkQuizCh8(1, 0);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '7') {"""

if old_url_chk in html:
    html = html.replace(old_url_chk, new_url_chk, 1)
    print("Added deep-linking and default chapter 8 successfully!")
else:
    print("Warning: old_url_chk not found!")

# Save to primary file
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved कक्षा_६_गणित_डिजिटल_साथी.html! Size:", len(html.encode('utf-8')), "bytes")

# Also save to index.html and artifact mirror
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved index.html!")

artifact_path = '/home/nepal/.gemini/antigravity/brain/6193a053-8fd9-40c5-8264-be982f512b93/interactive_math_guide.html'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved artifact mirror:", artifact_path)
