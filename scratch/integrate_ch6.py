# -*- coding: utf-8 -*-
import os
from generate_ch6_html import get_ch6_html

with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar Chapter 6 button
old_btn = """<button onclick="alert('पाठ ६ को विस्तृत नोट notes/06_pratishat_percentage.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ ६: प्रतिशत</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

new_btn = """<button id="side-ch-6" onclick="switchChapter(6)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium">
          <span>पाठ ६: प्रतिशत</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>"""

if old_btn in html:
    html = html.replace(old_btn, new_btn)
    print("Replaced Chapter 6 sidebar button directly!")
else:
    print("Finding Chapter 6 button via index search...")
    pos_btn = html.find('पाठ ६: प्रतिशत')
    start_b = html.rfind('<button', 0, pos_btn)
    end_b = html.find('</button>', pos_btn) + 9
    print("Found existing button block:\n", html[start_b:end_b])
    html = html[:start_b] + new_btn + html[end_b:]
    print("Replaced via index slice!")

# 2. Insert Chapter 6 View HTML before </main> (after END OF CHAPTER 5 VIEW)
ch6_html = get_ch6_html()
end_ch5 = "<!-- ================= END OF CHAPTER 5 VIEW ================= -->"
if end_ch5 in html:
    pos_marker = html.find(end_ch5) + len(end_ch5)
    html = html[:pos_marker] + "\n" + ch6_html + html[pos_marker:]
    print("Inserted chapter-view-6 successfully!")
else:
    print("Error: END OF CHAPTER 5 VIEW marker not found!")
    exit(1)

# 3. Update switchChapter function
old_switch = """function switchChapter(chNum) {
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

new_switch = """function switchChapter(chNum) {
      const b1 = document.getElementById('side-ch-1');
      const b2 = document.getElementById('side-ch-2');
      const b3 = document.getElementById('side-ch-3');
      const b4 = document.getElementById('side-ch-4');
      const b5 = document.getElementById('side-ch-5');
      const b6 = document.getElementById('side-ch-6');
      const v1 = document.getElementById('chapter-view-1');
      const v2 = document.getElementById('chapter-view-2');
      const v3 = document.getElementById('chapter-view-3');
      const v4 = document.getElementById('chapter-view-4');
      const v5 = document.getElementById('chapter-view-5');
      const v6 = document.getElementById('chapter-view-6');

      const sideActive = 'w-full text-left px-3.5 py-2.5 rounded-xl transition flex items-center justify-between text-xs md:text-sm bg-blue-600 text-white font-bold shadow-sm';
      const sideInactive = 'w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium';

      if (b1) b1.className = (chNum === 1) ? sideActive : sideInactive;
      if (b2) b2.className = (chNum === 2) ? sideActive : sideInactive;
      if (b3) b3.className = (chNum === 3) ? sideActive : sideInactive;
      if (b4) b4.className = (chNum === 4) ? sideActive : sideInactive;
      if (b5) b5.className = (chNum === 5) ? sideActive : sideInactive;
      if (b6) b6.className = (chNum === 6) ? sideActive : sideInactive;

      if (v1) v1.classList.toggle('hidden', chNum !== 1);
      if (v2) v2.classList.toggle('hidden', chNum !== 2);
      if (v3) v3.classList.toggle('hidden', chNum !== 3);
      if (v4) v4.classList.toggle('hidden', chNum !== 4);
      if (v5) v5.classList.toggle('hidden', chNum !== 5);
      if (v6) v6.classList.toggle('hidden', chNum !== 6);

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
      } else if (chNum === 6) {
        setTabCh6('concepts');
        if (window.MathJax && MathJax.Hub && v6) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v6]);
      }
    }"""

if old_switch in html:
    html = html.replace(old_switch, new_switch)
    print("Updated switchChapter successfully!")
else:
    print("Error: old_switch not found in html!")
    exit(1)

# 4. Add Chapter 6 JS logic: tab switcher, exercise switcher, visualizer, calculators, quiz
ch6_js = """
    function setTabCh6(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch6-view-' + t);
        const btn = document.getElementById('ch6-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch6-view-' + tabName);
      const activeBtn = document.getElementById('ch6-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && MathJax.Hub && activeView) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh6(secId) {
      ['sec1', 'sec2', 'sec3'].forEach(s => {
        const sec = document.getElementById('ch6-sec-' + s);
        const pill = document.getElementById('ch6-pill-' + s);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap';
      });
      const curSec = document.getElementById('ch6-sec-' + secId);
      const curPill = document.getElementById('ch6-pill-' + secId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap';
      if (window.MathJax && MathJax.Hub && curSec) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, curSec]);
      }
    }

    function gcd(a, b) {
      return b === 0 ? a : gcd(b, a % b);
    }

    function updateCh6Visualizer(val) {
      val = parseInt(val) || 0;
      val = Math.max(0, Math.min(100, val));
      const badge = document.getElementById('ch6-vis-val-badge');
      const pbar = document.getElementById('ch6-progress-bar');
      const pText = document.getElementById('ch6-vis-pct');
      const dText = document.getElementById('ch6-vis-dec');
      const fText = document.getElementById('ch6-vis-frac');

      if (badge) badge.textContent = val + '%';
      if (pbar) {
        pbar.style.width = val + '%';
        pbar.textContent = val > 5 ? val + '%' : '';
      }
      if (pText) pText.textContent = val + '%';
      if (dText) dText.textContent = (val / 100).toFixed(2);
      if (fText) {
        if (val === 0) {
          fText.textContent = '0/1';
        } else {
          const g = gcd(val, 100);
          fText.textContent = (val / g) + '/' + (100 / g);
        }
      }
    }

    function runCh6Calc1() {
      const q = parseFloat(document.getElementById('calc1-qty').value) || 0;
      const p = parseFloat(document.getElementById('calc1-pct').value) || 0;
      const ans = (q * p) / 100;
      const res = document.getElementById('calc1-res');
      if (res) {
        res.innerHTML = 'उत्तर: <strong>' + q + ' को ' + p + '% = ' + ans + '</strong> (' + q + ' &times; ' + p + '/100 = ' + ans + ')';
      }
    }

    function runCh6Calc2() {
      const n = parseFloat(document.getElementById('calc2-num').value) || 0;
      const d = parseFloat(document.getElementById('calc2-den').value) || 1;
      const pct = (n / d) * 100;
      const dec = n / d;
      const res = document.getElementById('calc2-res');
      if (res) {
        res.innerHTML = 'उत्तर: <strong>' + n + '/' + d + ' = ' + pct.toFixed(2).replace(/\\.00$/, '') + '%</strong> (दशमलव: ' + dec.toFixed(4).replace(/0+$/, '').replace(/\\.$/, '') + ')';
      }
    }

    const ch6QuizData = [
      { correct: 2, exp: "$\\\\frac{3}{5} \\\\times 100\\\\% = 3 \\\\times 20\\\\% = 60\\\\%$।" },
      { correct: 0, exp: "रु. ८०० को १५% $= 800 \\\\times \\\\frac{15}{100} = 8 \\\\times 15 = \\\\text{रु. } 120$।" },
      { correct: 1, exp: "१०० ले गुणन गर्दा दशमलव बिन्दु २ स्थान दायाँ सर्दछ: $0.06 \\\\times 100\\\\% = 6\\\\%$।" },
      { correct: 1, exp: "फुटबल मन नपराउने विद्यार्थी $= 500 - 200 = 300$, प्रतिशत $= \\\\frac{300}{500} \\\\times 100\\\\% = 60\\\\%$।" }
    ];

    function checkQuizCh6(qIdx, selected) {
      const data = ch6QuizData[qIdx];
      const expBox = document.getElementById('ch6-qexp-' + qIdx);
      const badge = document.getElementById('ch6-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch6-qbtn-' + qIdx + '-' + i);
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

    function resetQuizCh6() {
      for (let q = 0; q < 4; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch6-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium';
          }
        }
        const badge = document.getElementById('ch6-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch6-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }
"""

pos_quiz5 = html.find('function resetQuizCh5()')
if pos_quiz5 != -1:
    pos_end_fn = html.find('}', html.find('}', pos_quiz5) + 1) + 1
    html = html[:pos_end_fn] + "\n" + ch6_js + html[pos_end_fn:]
    print("Added Chapter 6 JS functions successfully!")
else:
    print("Warning: function resetQuizCh5 not found, appending before URLParams...")
    pos_url = html.find('const urlParams = new URLSearchParams')
    html = html[:pos_url] + ch6_js + "\n    " + html[pos_url:]

# 5. Add URL deep-linking support for Chapter 6
old_url_chk = "const urlParams = new URLSearchParams(window.location.search);\n    if (urlParams.get('ch') === '5') {"
new_url_chk = """const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('ch') === '6') {
      switchChapter(6);
      if (urlParams.get('tab')) {
        setTabCh6(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh6(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh6(0, 2);
          checkQuizCh6(1, 0);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (urlParams.get('ch') === '5') {"""

if old_url_chk in html:
    html = html.replace(old_url_chk, new_url_chk)
    print("Added deep-linking for ch=6 successfully!")
else:
    print("Warning: old_url_chk not found!")

# Save to primary file
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved कक्षा_६_गणित_डिजिटल_साथी.html successfully! New file size:", len(html.encode('utf-8')), "bytes")
