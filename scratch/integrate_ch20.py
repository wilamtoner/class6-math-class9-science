# -*- coding: utf-8 -*-
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sidebar button
old_sidebar_btn = """        <button onclick="alert('पाठ २० को विस्तृत नोट notes/20_tathyankashastra_statistics.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ २०: तथ्याङ्कशास्त्र</span>
          <span class="text-[10px] opacity-75">एकाइ ६</span>
        </button>"""

new_sidebar_btn = """        <button id="side-ch-20" onclick="switchChapter(20)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium cursor-pointer">
          <span>पाठ २०: तथ्याङ्कशास्त्र</span>
          <span class="text-[10px] bg-purple-100 text-purple-800 px-1.5 py-0.5 rounded font-bold">अन्तिम</span>
        </button>"""

if old_sidebar_btn not in html:
    print("ERROR: old_sidebar_btn not found!")
    sys.exit(1)

html = html.replace(old_sidebar_btn, new_sidebar_btn, 1)
print("1. Sidebar button replaced successfully.")

# 2. Insert Chapter 20 view
with open('scratch/ch20_view.html', 'r', encoding='utf-8') as f:
    ch20_view = f.read()

end_ch19_marker = "<!-- ================= END CHAPTER 19 ================= -->"
if end_ch19_marker not in html:
    print("ERROR: end_ch19_marker not found!")
    sys.exit(1)

html = html.replace(end_ch19_marker, end_ch19_marker + "\n\n" + ch20_view, 1)
print("2. Chapter 20 view inserted successfully.")

# 3. Update switchChapter function
old_b19 = "const b19 = document.getElementById('side-ch-19');"
new_b19 = "const b19 = document.getElementById('side-ch-19');\n      const b20 = document.getElementById('side-ch-20');"
html = html.replace(old_b19, new_b19, 1)

old_v19 = "const v19 = document.getElementById('chapter-view-19');"
new_v19 = "const v19 = document.getElementById('chapter-view-19');\n      const v20 = document.getElementById('chapter-view-20');"
html = html.replace(old_v19, new_v19, 1)

old_b19_class = "if (b19) b19.className = (chNum === 19) ? sideActive : sideInactive;"
new_b19_class = "if (b19) b19.className = (chNum === 19) ? sideActive : sideInactive;\n      if (b20) b20.className = (chNum === 20) ? sideActive : sideInactive;"
html = html.replace(old_b19_class, new_b19_class, 1)

old_v19_toggle = "if (v19) v19.classList.toggle('hidden', chNum !== 19);"
new_v19_toggle = "if (v19) v19.classList.toggle('hidden', chNum !== 19);\n      if (v20) v20.classList.toggle('hidden', chNum !== 20);"
html = html.replace(old_v19_toggle, new_v19_toggle, 1)

old_ch19_branch = """      } else if (chNum === 19) {
        if (typeof setTabCh19 === 'function') setTabCh19('concepts');
        if (typeof renderSymmetryShape === 'function') renderSymmetryShape();
        if (typeof renderTessellation === 'function') renderTessellation();
        if (window.MathJax && window.MathJax.Hub && v19) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v19]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v19);
        }
      }
    }"""

new_ch19_branch = """      } else if (chNum === 19) {
        if (typeof setTabCh19 === 'function') setTabCh19('concepts');
        if (typeof renderSymmetryShape === 'function') renderSymmetryShape();
        if (typeof renderTessellation === 'function') renderTessellation();
        if (window.MathJax && window.MathJax.Hub && v19) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v19]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v19);
        }
      } else if (chNum === 20) {
        if (typeof setTabCh20 === 'function') setTabCh20('concepts');
        if (typeof renderBarStudio === 'function') renderBarStudio();
        if (window.MathJax && window.MathJax.Hub && v20) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v20]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v20);
        }
      }
    }"""

if old_ch19_branch not in html:
    print("ERROR: old_ch19_branch not found!")
    sys.exit(1)

html = html.replace(old_ch19_branch, new_ch19_branch, 1)
print("3. switchChapter updated successfully.")

# 4. Insert Chapter 20 script
with open('scratch/ch20_script.js', 'r', encoding='utf-8') as f:
    ch20_script = f.read()

urlparams_marker = "const urlParams = new URLSearchParams(window.location.search);"
if urlparams_marker not in html:
    print("ERROR: urlparams_marker not found!")
    sys.exit(1)

html = html.replace(urlparams_marker, ch20_script + "\n\n    " + urlparams_marker, 1)
print("4. Chapter 20 script inserted successfully.")

# 5. Update router
old_router = """    const activeChParam = urlParams.get('ch') || '14';
    if (activeChParam === '19') {
      switchChapter(19);
      if (urlParams.get('tab')) {
        setTabCh19(urlParams.get('tab'));
      }
    } else if (activeChParam === '18') {"""

new_router = """    const activeChParam = urlParams.get('ch') || '14';
    if (activeChParam === '20') {
      switchChapter(20);
      if (urlParams.get('tab')) {
        setTabCh20(urlParams.get('tab'));
      }
    } else if (activeChParam === '19') {
      switchChapter(19);
      if (urlParams.get('tab')) {
        setTabCh19(urlParams.get('tab'));
      }
    } else if (activeChParam === '18') {"""

if old_router not in html:
    print("ERROR: old_router not found!")
    sys.exit(1)

html = html.replace(old_router, new_router, 1)
print("5. URL router updated successfully.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("ALL CHANGES WRITTEN TO index.html SUCCESSFULLY!")
