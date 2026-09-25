# -*- coding: utf-8 -*-
"""
Integrates Chapter 7 (Profit and Loss) into कक्षा_६_गणित_डिजिटल_साथी.html
and the artifact mirror interactive_math_guide.html.
"""
import os
import sys

# Ensure current dir is in sys.path
sys.path.insert(0, os.path.dirname(__file__))
from generate_ch7_html import get_ch7_html

with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar Chapter 7 button
old_btn = """<button onclick="alert('पाठ ७ को विस्तृत नोट notes/07_nafa_noksan_profit_loss.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ ७: नाफा र नोक्सान</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

new_btn = """<button id="side-ch-7" onclick="switchChapter(7)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium">
          <span>पाठ ७: नाफा र नोक्सान</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

if old_btn in html:
    html = html.replace(old_btn, new_btn)
    print("Replaced Chapter 7 sidebar button directly!")
else:
    pos_btn = html.find('पाठ ७: नाफा र नोक्सान')
    if pos_btn != -1:
        start_b = html.rfind('<button', 0, pos_btn)
        end_b = html.find('</button>', pos_btn) + 9
        print("Found existing button block:\n", html[start_b:end_b])
        html = html[:start_b] + new_btn + html[end_b:]
        print("Replaced via index slice!")
    else:
        print("Warning: Chapter 7 sidebar button not found!")

# 2. Insert Chapter 7 View HTML before </main> (after END OF CHAPTER 6 VIEW)
ch7_html = get_ch7_html()
end_ch6 = "<!-- ================= END OF CHAPTER 6 VIEW ================= -->"
if end_ch6 in html:
    pos_marker = html.find(end_ch6) + len(end_ch6)
    html = html[:pos_marker] + "\n" + ch7_html + html[pos_marker:]
    print("Inserted chapter-view-7 successfully!")
else:
    print("Error: END OF CHAPTER 6 VIEW marker not found!")
    sys.exit(1)

# 3. Update switchChapter function
old_switch_target = "const b6 = document.getElementById('side-ch-6');"
new_switch_b = "const b6 = document.getElementById('side-ch-6');\n      const b7 = document.getElementById('side-ch-7');"

old_view_target = "const v6 = document.getElementById('chapter-view-6');"
new_view_v = "const v6 = document.getElementById('chapter-view-6');\n      const v7 = document.getElementById('chapter-view-7');"

old_class_b = "if (b6) b6.className = (chNum === 6) ? sideActive : sideInactive;"
new_class_b = "if (b6) b6.className = (chNum === 6) ? sideActive : sideInactive;\n      if (b7) b7.className = (chNum === 7) ? sideActive : sideInactive;"

old_toggle_v = "if (v6) v6.classList.toggle('hidden', chNum !== 6);"
new_toggle_v = "if (v6) v6.classList.toggle('hidden', chNum !== 6);\n      if (v7) v7.classList.toggle('hidden', chNum !== 7);"

old_ch6_branch = """} else if (chNum === 6) {
        setTabCh6('concepts');
        if (window.MathJax && MathJax.Hub && v6) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v6]);
      }"""

new_ch7_branch = """} else if (chNum === 6) {
        setTabCh6('concepts');
        if (window.MathJax && MathJax.Hub && v6) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v6]);
      } else if (chNum === 7) {
        setTabCh7('concepts');
        runCh7Calc();
        if (window.MathJax && MathJax.Hub && v7) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v7]);
      }"""

html = html.replace(old_switch_target, new_switch_b, 1)
html = html.replace(old_view_target, new_view_v, 1)
html = html.replace(old_class_b, new_class_b, 1)
html = html.replace(old_toggle_v, new_toggle_v, 1)
html = html.replace(old_ch6_branch, new_ch7_branch, 1)
print("Updated switchChapter for Chapter 7!")

# 4. Add Chapter 7 JavaScript logic at the top level
ch7_js = """
    function setTabCh7(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch7-view-' + t);
        const btn = document.getElementById('ch7-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
      });
      const activeView = document.getElementById('ch7-view-' + tabName);
      const activeBtn = document.getElementById('ch7-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      if (window.MathJax && MathJax.Hub && activeView) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh7(secId) {
      ['sec1', 'sec2', 'sec3'].forEach(s => {
        const sec = document.getElementById('ch7-sec-' + s);
        const pill = document.getElementById('ch7-pill-' + s);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer';
      });
      const curSec = document.getElementById('ch7-sec-' + secId);
      const curPill = document.getElementById('ch7-pill-' + secId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap cursor-pointer';
      if (window.MathJax && MathJax.Hub && curSec) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, curSec]);
      }
    }

    function setCh7Preset(cp, exp, sp) {
      const inCp = document.getElementById('ch7-in-cp');
      const inExp = document.getElementById('ch7-in-exp');
      const inSp = document.getElementById('ch7-in-sp');
      if (inCp) inCp.value = cp;
      if (inExp) inExp.value = exp;
      if (inSp) inSp.value = sp;
      runCh7Calc();
    }

    function runCh7Calc() {
      const inCp = document.getElementById('ch7-in-cp');
      const inExp = document.getElementById('ch7-in-exp');
      const inSp = document.getElementById('ch7-in-sp');
      const res = document.getElementById('ch7-calc-res');
      if (!res) return;

      const cp = parseFloat(inCp ? inCp.value : 0) || 0;
      const exp = parseFloat(inExp ? inExp.value : 0) || 0;
      const sp = parseFloat(inSp ? inSp.value : 0) || 0;
      const totalCp = cp + exp;

      if (totalCp <= 0) {
        res.innerHTML = '<div class="text-amber-300 font-bold text-sm">कृपया मान्य खरिद मूल्य प्रविष्ट गर्नुहोस्।</div>';
        return;
      }

      let statusHtml = '';
      if (sp > totalCp) {
        const profit = sp - totalCp;
        const profitPct = (profit / totalCp) * 100;
        statusHtml = `
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-emerald-400/30 pb-3">
            <span class="px-3 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-bold text-xs border border-emerald-400/30">व्यापार स्थिति: नाफा (Profit)</span>
            <span class="text-xs text-blue-200">अवस्था: S.P. (${sp}) > C.P. (${totalCp})</span>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">जम्मा क्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${totalCp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">विक्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${sp}</span></div>
            <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">नाफा रकम</span><span class="text-lg font-mono font-bold text-emerald-300">+ रु. ${profit.toFixed(2).replace(/\\.00$/, '')}</span></div>
            <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">नाफा प्रतिशत</span><span class="text-lg font-mono font-bold text-emerald-300">+ ${profitPct.toFixed(2).replace(/\\.00$/, '')}%</span></div>
          </div>
          <p class="text-xs text-blue-100 bg-white/5 p-2 rounded-lg mt-2">
            <strong>गणना व्याख्या:</strong> नाफा = ${sp} - ${totalCp} = रु. ${profit.toFixed(2).replace(/\\.00$/, '')} | नाफा % = (${profit.toFixed(2).replace(/\\.00$/, '')} / ${totalCp}) × 100% = ${profitPct.toFixed(2).replace(/\\.00$/, '')}%
          </p>
        `;
      } else if (totalCp > sp) {
        const loss = totalCp - sp;
        const lossPct = (loss / totalCp) * 100;
        statusHtml = `
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-rose-400/30 pb-3">
            <span class="px-3 py-1 rounded-xl bg-rose-500/20 text-rose-300 font-bold text-xs border border-rose-400/30">व्यापार स्थिति: नोक्सान / घाटा (Loss)</span>
            <span class="text-xs text-blue-200">अवस्था: C.P. (${totalCp}) > S.P. (${sp})</span>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">जम्मा क्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${totalCp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">विक्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${sp}</span></div>
            <div class="bg-rose-500/20 border border-rose-400/40 p-2.5 rounded-xl"><span class="text-xs text-rose-200 block">नोक्सान रकम</span><span class="text-lg font-mono font-bold text-rose-300">- रु. ${loss.toFixed(2).replace(/\\.00$/, '')}</span></div>
            <div class="bg-rose-500/20 border border-rose-400/40 p-2.5 rounded-xl"><span class="text-xs text-rose-200 block">नोक्सान प्रतिशत</span><span class="text-lg font-mono font-bold text-rose-300">- ${lossPct.toFixed(2).replace(/\\.00$/, '')}%</span></div>
          </div>
          <p class="text-xs text-blue-100 bg-white/5 p-2 rounded-lg mt-2">
            <strong>गणना व्याख्या:</strong> नोक्सान = ${totalCp} - ${sp} = रु. ${loss.toFixed(2).replace(/\\.00$/, '')} | नोक्सान % = (${loss.toFixed(2).replace(/\\.00$/, '')} / ${totalCp}) × 100% = ${lossPct.toFixed(2).replace(/\\.00$/, '')}%
          </p>
        `;
      } else {
        statusHtml = `
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/20 pb-3">
            <span class="px-3 py-1 rounded-xl bg-slate-500/30 text-slate-200 font-bold text-xs border border-white/20">नाफा पनि छैन, नोक्सान पनि छैन</span>
            <span class="text-xs text-blue-200">C.P. (${totalCp}) = S.P. (${sp})</span>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">जम्मा क्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${totalCp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">विक्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${sp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">नाफा/नोक्सान</span><span class="text-lg font-mono font-bold">रु. ०</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">प्रतिशत</span><span class="text-lg font-mono font-bold">०%</span></div>
          </div>
        `;
      }
      res.innerHTML = statusHtml;
    }

    const ch7QuizData = [
      { correct: 1, exp: "विक्रय मूल्य क्रय मूल्यभन्दा बढी ($S.P. > C.P.$) भएको अवस्थामा नाफा हुन्छ।" },
      { correct: 2, exp: "नाफा $= 575 - 500 = 75$, नाफा प्रतिशत $= \\\\frac{75}{500} \\\\times 100\\\\% = 15\\\\%$।" },
      { correct: 0, exp: "१०% नोक्सान $= 1200 \\\\times 10\\\\% = 120$। विक्रय मूल्य $= 1200 - 120 = \\\\text{रु. } 1,080$।" },
      { correct: 1, exp: "जम्मा $C.P. = 3000 + 200 = 3200$। नाफा $= 3520 - 3200 = 320$। नाफा % $= \\\\frac{320}{3200} \\\\times 100\\\\% = 10\\\\%$।" },
      { correct: 1, exp: "१२ गोटाको $S.P. = 12 \\\\times 25 = 300$। नाफा $= 300 - 240 = \\\\text{रु. } 60$।" }
    ];

    function checkQuizCh7(qIdx, selected) {
      const data = ch7QuizData[qIdx];
      const expBox = document.getElementById('ch7-qexp-' + qIdx);
      const badge = document.getElementById('ch7-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch7-qbtn-' + qIdx + '-' + i);
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

    function resetQuizCh7() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch7-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch7-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch7-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh7 = setTabCh7;
    window.setExerciseCh7 = setExerciseCh7;
    window.setCh7Preset = setCh7Preset;
    window.runCh7Calc = runCh7Calc;
    window.checkQuizCh7 = checkQuizCh7;
    window.resetQuizCh7 = resetQuizCh7;
"""

# Place ch7_js before "const urlParams = new URLSearchParams"
pos_url = html.find('const urlParams = new URLSearchParams')
if pos_url != -1:
    html = html[:pos_url] + ch7_js + "\n    " + html[pos_url:]
    print("Added Chapter 7 JS functions at top level!")
else:
    print("Error: const urlParams not found!")
    sys.exit(1)

# 5. Add URL deep-linking and default chapter 7
old_url_chk = "const activeChParam = urlParams.get('ch') || '6';"
new_url_chk = """const activeChParam = urlParams.get('ch') || '7';
    if (activeChParam === '7') {
      switchChapter(7);
      if (urlParams.get('tab')) {
        setTabCh7(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh7(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh7(0, 1);
          checkQuizCh7(1, 2);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '6') {"""

if old_url_chk in html:
    html = html.replace(old_url_chk, new_url_chk)
    print("Added deep-linking and default chapter 7 successfully!")
else:
    print("Warning: old_url_chk not found!")

# Save to primary file
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved कक्षा_६_गणित_डिजिटल_साथी.html! Size:", len(html.encode('utf-8')), "bytes")

# Also save to artifact mirror
artifact_path = '/home/nepal/.gemini/antigravity/brain/6193a053-8fd9-40c5-8264-be982f512b93/interactive_math_guide.html'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved artifact mirror:", artifact_path)
