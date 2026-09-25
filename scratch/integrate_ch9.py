import re
import sys
from generate_ch9_html import get_ch9_html

print("Starting Chapter 9 Web App Integration...")

with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Chapter 9 sidebar button
new_side_btn = """<button id="side-ch-9" onclick="switchChapter(9)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium cursor-pointer">
          <span>पाठ ९: दूरी (Distance)</span>
          <span class="text-[10px] opacity-75">एकाइ ३</span>
        </button>"""

# Check if side-ch-9 is already there
if 'id="side-ch-9"' not in html:
    m = re.search(r'<button\s+onclick=\"alert\([^\)]*पाठ\s*९[^\)]*\)\"[^>]*>[\s\S]*?<\/button>', html)
    if m:
        html = html[:m.start()] + new_side_btn + html[m.end():]
        print("Replaced Chapter 9 sidebar button via regex!")
    else:
        print("Warning: Chapter 9 sidebar button pattern not found directly, checking text...")
        old_side = "<span>पाठ ९: दूरी</span>"
        pos = html.find(old_side)
        if pos != -1:
            btn_start = html.rfind('<button', 0, pos)
            btn_end = html.find('</button>', pos) + len('</button>')
            html = html[:btn_start] + new_side_btn + html[btn_end:]
            print("Replaced Chapter 9 sidebar button via position search!")
else:
    print("Chapter 9 sidebar button already present!")

# 2. Insert chapter-view-9 after chapter-view-8 if not present
if 'id="chapter-view-9"' not in html:
    ch8_end_tag = "<!-- ================= END OF CHAPTER 8 VIEW ================= -->"
    pos_ch8_end = html.find(ch8_end_tag)
    if pos_ch8_end != -1:
        insert_pos = pos_ch8_end + len(ch8_end_tag)
        ch9_html = get_ch9_html()
        html = html[:insert_pos] + "\n\n" + ch9_html + html[insert_pos:]
        print("Inserted chapter-view-9 successfully!")
    else:
        print("Error: END OF CHAPTER 8 VIEW marker not found!")
        sys.exit(1)
else:
    print("chapter-view-9 already present!")

# 3. Update switchChapter(chNum)
old_switch_decl = "const b8 = document.getElementById('side-ch-8');\n      const v1 = document.getElementById('chapter-view-1');"
new_switch_decl = "const b8 = document.getElementById('side-ch-8');\n      const b9 = document.getElementById('side-ch-9');\n      const v1 = document.getElementById('chapter-view-1');"

old_switch_v8 = "const v8 = document.getElementById('chapter-view-8');\n\n      const sideActive ="
new_switch_v8 = "const v8 = document.getElementById('chapter-view-8');\n      const v9 = document.getElementById('chapter-view-9');\n\n      const sideActive ="

old_b8_line = "if (b8) b8.className = (chNum === 8) ? sideActive : sideInactive;\n\n      if (v1)"
new_b8_line = "if (b8) b8.className = (chNum === 8) ? sideActive : sideInactive;\n      if (b9) b9.className = (chNum === 9) ? sideActive : sideInactive;\n\n      if (v1)"

old_v8_toggle = "if (v8) v8.classList.toggle('hidden', chNum !== 8);\n\n      if (chNum === 1)"
new_v8_toggle = "if (v8) v8.classList.toggle('hidden', chNum !== 8);\n      if (v9) v9.classList.toggle('hidden', chNum !== 9);\n\n      if (chNum === 1)"

old_ch8_block = """if (chNum === 8) {
        setTabCh8('concepts');
        runCh8Calc();
        if (window.MathJax && window.MathJax.Hub && v8) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v8]);
      }
    }"""

new_ch8_block = """if (chNum === 8) {
        setTabCh8('concepts');
        runCh8Calc();
        if (window.MathJax && window.MathJax.Hub && v8) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v8]);
      } else if (chNum === 9) {
        setTabCh9('concepts');
        runCh9Convert();
        if (window.MathJax && window.MathJax.Hub && v9) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v9]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v9);
        }
      }
    }"""

if old_switch_decl in html: html = html.replace(old_switch_decl, new_switch_decl, 1)
if old_switch_v8 in html: html = html.replace(old_switch_v8, new_switch_v8, 1)
if old_b8_line in html: html = html.replace(old_b8_line, new_b8_line, 1)
if old_v8_toggle in html: html = html.replace(old_v8_toggle, new_v8_toggle, 1)
if old_ch8_block in html:
    html = html.replace(old_ch8_block, new_ch8_block, 1)
    print("Updated switchChapter for Chapter 9 successfully!")
else:
    print("Warning: old_ch8_block pattern not matched directly in switchChapter")

# 4. Add Chapter 9 JS functions if not present
if 'function setTabCh9' not in html:
    ch9_js = """
    // ==========================================
    // CHAPTER 9: DISTANCE (दूरी) INTERACTIVE LOGIC
    // ==========================================
    function setTabCh9(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch9-tab-' + t);
        const view = document.getElementById('ch9-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        runCh9Convert();
      }
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch9-view-' + tab));
      }
    }

    function setExerciseCh9(sec) {
      const secs = ['sec1', 'sec2', 'sec3'];
      secs.forEach(s => {
        const btn = document.getElementById('ch9-ex-btn-' + s);
        const view = document.getElementById('ch9-ex-' + s);
        if (btn && view) {
          if (s === sec) {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-xs transition cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-600 hover:bg-slate-100 transition cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch9-ex-' + sec));
      }
    }

    function setCh9Preset(val, fromUnit, toUnit) {
      const inVal = document.getElementById('ch9-in-val');
      const inFrom = document.getElementById('ch9-in-from');
      const inTo = document.getElementById('ch9-in-to');
      if (inVal) inVal.value = val;
      if (inFrom) inFrom.value = fromUnit;
      if (inTo) inTo.value = toUnit;
      runCh9Convert();
    }

    function runCh9Convert() {
      const inVal = document.getElementById('ch9-in-val');
      const inFrom = document.getElementById('ch9-in-from');
      const inTo = document.getElementById('ch9-in-to');
      const res = document.getElementById('ch9-calc-res');
      if (!inVal || !inFrom || !inTo || !res) return;

      const val = parseFloat(inVal.value);
      const from = inFrom.value;
      const to = inTo.value;

      if (isNaN(val)) {
        res.innerHTML = '<span class="text-amber-300 text-xs">कृपया संख्यात्मक मान राख्नुहोस्।</span>';
        return;
      }

      // Direct CDC Formula calculation
      let targetVal = 0;
      let formulaStr = "";
      const key = from + "->" + to;

      if (from === to) {
        targetVal = val;
        formulaStr = "उही एकाइ भएकोले कुनै परिवर्तन आवश्यक छैन ($" + val + " " + from + "$)।";
      } else if (key === "m->cm") { targetVal = val * 100; formulaStr = "$" + val + " \\\\times 100 = " + targetVal + "\\\\text{ cm}$ (ठूलो $\\\\to$ सानो = गुणन)"; }
      else if (key === "cm->m") { targetVal = val / 100; formulaStr = "$" + val + " \\\\div 100 = " + targetVal + "\\\\text{ m}$ (सानो $\\\\to$ ठूलो = भाग)"; }
      else if (key === "m->ft") { targetVal = val * 3.28; formulaStr = "$" + val + " \\\\times 3.28 = " + targetVal.toFixed(3).replace(/\\\\.?0+$/, '') + "\\\\text{ ft}$"; }
      else if (key === "ft->m") { targetVal = val / 3.28; formulaStr = "$" + val + " \\\\div 3.28 = " + targetVal.toFixed(3).replace(/\\\\.?0+$/, '') + "\\\\text{ m}$"; }
      else if (key === "m->in") { targetVal = val * 39.37; formulaStr = "$" + val + " \\\\times 39.37 = " + targetVal.toFixed(2) + "\\\\text{ in}$"; }
      else if (key === "in->m") { targetVal = val / 39.37; formulaStr = "$" + val + " \\\\div 39.37 = " + targetVal.toFixed(3).replace(/\\\\.?0+$/, '') + "\\\\text{ m}$"; }
      else if (key === "ft->in") { targetVal = val * 12; formulaStr = "$" + val + " \\\\times 12 = " + targetVal + "\\\\text{ in}$ (१ फिट = १२ इन्च)"; }
      else if (key === "in->ft") { targetVal = val / 12; formulaStr = "$" + val + " \\\\div 12 = " + targetVal.toFixed(3).replace(/\\\\.?0+$/, '') + "\\\\text{ ft}$"; }
      else if (key === "in->cm") { targetVal = val * 2.54; formulaStr = "$" + val + " \\\\times 2.54 = " + targetVal.toFixed(2) + "\\\\text{ cm}$"; }
      else if (key === "cm->in") { targetVal = val / 2.54; formulaStr = "$" + val + " \\\\div 2.54 = " + targetVal.toFixed(2) + "\\\\text{ in}$"; }
      else if (key === "ft->cm") { targetVal = val * 30.48; formulaStr = "$" + val + " \\\\times 30.48 = " + targetVal.toFixed(2) + "\\\\text{ cm}$"; }
      else if (key === "cm->ft") { targetVal = val / 30.48; formulaStr = "$" + val + " \\\\div 30.48 = " + targetVal.toFixed(2) + "\\\\text{ ft}$"; }
      else if (key === "km->m") { targetVal = val * 1000; formulaStr = "$" + val + " \\\\times 1000 = " + targetVal + "\\\\text{ m}$"; }
      else if (key === "m->km") { targetVal = val / 1000; formulaStr = "$" + val + " \\\\div 1000 = " + targetVal + "\\\\text{ km}$"; }
      else if (key === "cm->mm") { targetVal = val * 10; formulaStr = "$" + val + " \\\\times 10 = " + targetVal + "\\\\text{ mm}$"; }
      else if (key === "mm->cm") { targetVal = val / 10; formulaStr = "$" + val + " \\\\div 10 = " + targetVal + "\\\\text{ cm}$"; }
      else {
        // Multi-step conversion via base meter
        let base_m = (from === 'm') ? val : (from === 'cm') ? val / 100 : (from === 'mm') ? val / 100 : (from === 'km') ? val * 1000 : (from === 'ft') ? val / 3.28 : (val * 2.54) / 100;
        targetVal = (to === 'm') ? base_m : (to === 'cm') ? base_m * 100 : (to === 'mm') ? base_m * 1000 : (to === 'km') ? base_m / 1000 : (to === 'ft') ? base_m * 3.28 : base_m * 39.37;
        formulaStr = "पहिले आधार एकाइ मिटरमा ($" + base_m.toFixed(3) + "\\\\text{ m}$) लगेर इच्छित एकाइमा रूपान्तरण गर्दा।";
      }

      // Compute across all other units for rich preview
      let bm = (from === 'm') ? val : (from === 'cm') ? val / 100 : (from === 'mm') ? val / 1000 : (from === 'km') ? val * 1000 : (from === 'ft') ? val / 3.28 : (val * 2.54) / 100;
      let all_m = bm.toFixed(2);
      let all_cm = (bm * 100).toFixed(2);
      let all_ft = (bm * 3.28).toFixed(2);
      let all_in = (bm * 39.37).toFixed(2);

      let statusHtml = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-indigo-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-indigo-500/20 text-indigo-300 font-bold text-xs border border-indigo-400/30">दूरी रूपान्तरण प्रत्यक्ष नतिजा</span>
          <span class="text-xs text-blue-200">${val} ${from} $\\\\rightarrow$ ${to}</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">सुरुवाती नाप</span><span class="text-lg font-mono font-bold">${val} ${from}</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">नतिजा (${to})</span><span class="text-lg font-mono font-bold text-emerald-300">${targetVal.toFixed(2).replace(/\\\\.00$/, '')} ${to}</span></div>
          <div class="bg-blue-500/20 border border-blue-400/40 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">फिट समतुल्य</span><span class="text-lg font-mono font-bold text-blue-300">${all_ft} ft</span></div>
          <div class="bg-purple-500/20 border border-purple-400/40 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">इन्च समतुल्य</span><span class="text-lg font-mono font-bold text-purple-300">${all_in} in</span></div>
        </div>
        <p class="text-xs text-blue-100 bg-white/5 p-2.5 rounded-lg mt-2 leading-relaxed">
          <strong>चरणबद्ध रूपान्तरण विधि:</strong> ${formulaStr}
        </p>
      `;
      res.innerHTML = statusHtml;
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(res);
      }
    }

    const ch9QuizData = [
      { correct: 1, exp: "मेट्रिक प्रणाली अनुसार $1\\\\text{ m} = 100\\\\text{ cm}$ हुन्छ।" },
      { correct: 0, exp: "$1\\\\text{ in} = 2.54\\\\text{ cm}$ हुन्छ।" },
      { correct: 2, exp: "पाठ्यक्रम अनुसार $1\\\\text{ m} = 3.28\\\\text{ ft}$ मानिन्छ।" },
      { correct: 1, exp: "१ फिटमा १२ इन्च हुने भएकाले $6\\\\text{ ft} = 6 \\\\times 12 = 72\\\\text{ in}$ हुन्छ।" },
      { correct: 1, exp: "सानो एकाइलाई ठूलो एकाइमा रूपान्तरण गर्दा रूपान्तरण दरले भाग ($\\\\div$) गर्नुपर्छ।" }
    ];

    function checkQuizCh9(qIdx, selected) {
      const data = ch9QuizData[qIdx];
      const expBox = document.getElementById('ch9-qexp-' + qIdx);
      const badge = document.getElementById('ch9-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch9-qbtn-' + qIdx + '-' + i);
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
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(expBox);
        }
      }
    }

    function resetQuizCh9() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch9-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch9-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch9-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh9 = setTabCh9;
    window.setExerciseCh9 = setExerciseCh9;
    window.setCh9Preset = setCh9Preset;
    window.runCh9Convert = runCh9Convert;
    window.checkQuizCh9 = checkQuizCh9;
    window.resetQuizCh9 = resetQuizCh9;
"""
    pos_url = html.find('const urlParams = new URLSearchParams')
    if pos_url != -1:
        html = html[:pos_url] + ch9_js + "\n    " + html[pos_url:]
        print("Added Chapter 9 JS functions at top level!")

# 5. Add URL deep-linking and default chapter 9
old_url_chk = """const activeChParam = urlParams.get('ch') || '8';
    if (activeChParam === '8') {"""

new_url_chk = """const activeChParam = urlParams.get('ch') || '9';
    if (activeChParam === '9') {
      switchChapter(9);
      if (urlParams.get('tab')) {
        setTabCh9(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh9(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh9(0, 1);
          checkQuizCh9(1, 0);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '8') {"""

if old_url_chk in html:
    html = html.replace(old_url_chk, new_url_chk, 1)
    print("Added deep-linking and default chapter 9 successfully!")
else:
    print("Warning: old_url_chk not found!")

# Save to primary file
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved कक्षा_६_गणित_डिजिटल_साथी.html! Size:", len(html.encode('utf-8')), "bytes")

# Save to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved index.html!")

# Save to class6_math_offline.html
with open('class6_math_offline.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved class6_math_offline.html!")

# Save to artifact mirror
artifact_path = '/home/nepal/.gemini/antigravity/brain/6193a053-8fd9-40c5-8264-be982f512b93/interactive_math_guide.html'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved artifact mirror:", artifact_path)

print("Chapter 9 integration completed successfully!")
