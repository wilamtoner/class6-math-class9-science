import sys
import os
import scratch.generate_ch4_html as gen4

portal_path = "/run/media/nepal/Backup1/class 6 maths/कक्षा_६_गणित_डिजिटल_साथी.html"
mirror_path = "/home/nepal/.gemini/antigravity/brain/fc1605f3-8b2b-459a-809e-54639da37eba/interactive_math_guide.html"

with open(portal_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Sidebar button for Chapter 4
old_side_btn = '''        <button onclick="alert('पाठ ४ को विस्तृत नोट notes/04_bhinna_fractions.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ ४: भिन्न</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>'''

new_side_btn = '''        <button id="side-ch-4" onclick="switchChapter(4)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium">
          <span>पाठ ४: भिन्न</span>
          <span class="text-[10px] opacity-75">एकाइ २</span>
        </button>'''

if old_side_btn in html:
    html = html.replace(old_side_btn, new_side_btn)
    print("Sidebar button updated successfully")
else:
    print("WARNING: Sidebar button not found")

# 2. Insert Chapter 4 HTML view after Chapter 3
ch3_end_marker = "      <!-- ================= END OF CHAPTER 3 VIEW ================= -->"
ch4_html = gen4.get_ch4_html()

if ch3_end_marker in html:
    html = html.replace(ch3_end_marker, ch3_end_marker + "\n" + ch4_html)
    print("Chapter 4 HTML inserted successfully")
else:
    print("ERROR: Chapter 3 end marker not found")

# 3. Update JavaScript logic
js_switch_old = '''    function switchChapter(chNum) {
      const b1 = document.getElementById('side-ch-1');
      const b2 = document.getElementById('side-ch-2');
      const b3 = document.getElementById('side-ch-3');
      const v1 = document.getElementById('chapter-view-1');
      const v2 = document.getElementById('chapter-view-2');
      const v3 = document.getElementById('chapter-view-3');

      const sideActive = 'w-full text-left px-3.5 py-2.5 rounded-xl transition flex items-center justify-between text-xs md:text-sm bg-blue-600 text-white font-bold shadow-sm';
      const sideInactive = 'w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium';

      if (b1) b1.className = (chNum === 1) ? sideActive : sideInactive;
      if (b2) b2.className = (chNum === 2) ? sideActive : sideInactive;
      if (b3) b3.className = (chNum === 3) ? sideActive : sideInactive;

      if (v1) v1.classList.toggle('hidden', chNum !== 1);
      if (v2) v2.classList.toggle('hidden', chNum !== 2);
      if (v3) v3.classList.toggle('hidden', chNum !== 3);

      if (chNum === 1) {
        setTab('concepts');
        if (window.MathJax && MathJax.Hub && v1) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v1]);
      } else if (chNum === 2) {
        setTabCh2('concepts');
        if (window.MathJax && MathJax.Hub && v2) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v2]);
      } else if (chNum === 3) {
        setTabCh3('concepts');
        if (window.MathJax && MathJax.Hub && v3) MathJax.Hub.Queue(["Typeset", MathJax.Hub, v3]);
      }
    }'''

js_switch_new = '''    function switchChapter(chNum) {
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
    }

    function setTabCh4(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch4-view-' + t);
        const btn = document.getElementById('ch4-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch4-view-' + tabName);
      const activeBtn = document.getElementById('ch4-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && MathJax.Hub && activeView) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh4(exId) {
      const allEx = ['ex4_1', 'ex4_2', 'ex4_3', 'ex4_4_1', 'ex4_4_2', 'ex4_5'];
      allEx.forEach(e => {
        const sec = document.getElementById('ch4-sec-' + e);
        const pill = document.getElementById('ch4-pill-' + e);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap';
      });
      const curSec = document.getElementById('ch4-sec-' + exId);
      const curPill = document.getElementById('ch4-pill-' + exId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap';
      if (window.MathJax && MathJax.Hub && curSec) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, curSec]);
      }
    }

    const ch4QuizData = [
      { correct: 2, exp: "उचित भिन्नमा अंश हरभन्दा सानो ($4 < 7$) हुन्छ र मान १ भन्दा कम हुन्छ।" },
      { correct: 1, exp: "हरहरूको ल.स. ६ हो: $\\\\frac{2}{6} + \\\\frac{1}{6} = \\\\frac{3}{6} = \\\\frac{1}{2}$।" },
      { correct: 0, exp: "अंश र हर गुणन गर्दा: $\\\\frac{3 \\\\times 10}{5 \\\\times 9} = \\\\frac{30}{45} = \\\\frac{2}{3}$।" },
      { correct: 1, exp: "व्युत्क्रम भिन्नले गुणन गर्दा: $\\\\frac{4}{7} \\\\times \\\\frac{7}{2} = \\\\frac{4}{2} = 2$।" }
    ];

    function checkQuizCh4(qIdx, selected) {
      const data = ch4QuizData[qIdx];
      const expBox = document.getElementById('ch4-qexp-' + qIdx);
      const badge = document.getElementById('ch4-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch4-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-2.5 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-2.5 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-2.5 rounded-xl border border-slate-200 text-slate-500 opacity-60';
          }
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs';
          expBox.innerHTML = '<strong>✓ सही उत्तर!</strong> ' + data.exp;
          if (badge) {
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-800';
            badge.innerText = 'सही (Correct)';
          }
        } else {
          expBox.className = 'p-3 rounded-xl bg-rose-50 border border-rose-200 text-rose-900 text-xs';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही उत्तर विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। ' + data.exp;
          if (badge) {
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-800';
            badge.innerText = 'गलत (Incorrect)';
          }
        }
        if (window.MathJax && MathJax.Hub) MathJax.Hub.Queue(["Typeset", MathJax.Hub, expBox]);
      }
    }'''

if js_switch_old in html:
    html = html.replace(js_switch_old, js_switch_new)
    print("JS logic updated successfully")
else:
    print("ERROR: JS switchChapter block not found")

# 4. Deep linking in script
deep_old = "    if (urlParams.get('ch') === '3') {"
deep_new = '''    if (urlParams.get('ch') === '4') {
      switchChapter(4);
      if (urlParams.get('tab')) {
        setTabCh4(urlParams.get('tab'));
      }
      if (urlParams.get('ex')) {
        setExerciseCh4(urlParams.get('ex'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh4(0, 2);
          checkQuizCh4(1, 1);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (urlParams.get('ch') === '3') {'''

if deep_old in html:
    html = html.replace(deep_old, deep_new)
    print("Deep linking updated successfully")
else:
    print("ERROR: Deep linking condition not found")

# Write to portal and mirror
with open(portal_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated {portal_path} ({len(html)} bytes)")

with open(mirror_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated mirror {mirror_path} ({len(html)} bytes)")
