# -*- coding: utf-8 -*-
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sidebar button
old_sidebar_btn = """        <button onclick="alert('पाठ १९ को विस्तृत नोट notes/19_samamiti_ra_tessellation.md मा उपलब्ध छ।')" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700">
          <span>पाठ १९: सममिति र टेसेलेसन</span>
          <span class="text-[10px] opacity-75">एकाइ ५</span>
        </button>"""

new_sidebar_btn = """        <button id="side-ch-19" onclick="switchChapter(19)" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium cursor-pointer">
          <span>पाठ १९: सममिति र टेसेलेसन</span>
          <span class="text-[10px] bg-emerald-100 text-emerald-800 px-1.5 py-0.5 rounded font-bold">नयाँ</span>
        </button>"""

if old_sidebar_btn not in html:
    print("ERROR: old_sidebar_btn not found!")
    sys.exit(1)

html = html.replace(old_sidebar_btn, new_sidebar_btn, 1)
print("1. Sidebar button replaced successfully.")

# 2. Insert Chapter 19 view
with open('scratch/ch19_view.html', 'r', encoding='utf-8') as f:
    ch19_view = f.read()

end_ch18_marker = "<!-- ================= END CHAPTER 18 ================= -->"
if end_ch18_marker not in html:
    print("ERROR: end_ch18_marker not found!")
    sys.exit(1)

html = html.replace(end_ch18_marker, end_ch18_marker + "\n\n" + ch19_view, 1)
print("2. Chapter 19 view inserted successfully.")

# 3. Update switchChapter function
old_b18 = "const b18 = document.getElementById('side-ch-18');"
new_b18 = "const b18 = document.getElementById('side-ch-18');\n      const b19 = document.getElementById('side-ch-19');"
html = html.replace(old_b18, new_b18, 1)

old_v18 = "const v18 = document.getElementById('chapter-view-18');"
new_v18 = "const v18 = document.getElementById('chapter-view-18');\n      const v19 = document.getElementById('chapter-view-19');"
html = html.replace(old_v18, new_v18, 1)

old_b18_class = "if (b18) b18.className = (chNum === 18) ? sideActive : sideInactive;"
new_b18_class = "if (b18) b18.className = (chNum === 18) ? sideActive : sideInactive;\n      if (b19) b19.className = (chNum === 19) ? sideActive : sideInactive;"
html = html.replace(old_b18_class, new_b18_class, 1)

old_v18_toggle = "if (v18) v18.classList.toggle('hidden', chNum !== 18);"
new_v18_toggle = "if (v18) v18.classList.toggle('hidden', chNum !== 18);\n      if (v19) v19.classList.toggle('hidden', chNum !== 19);"
html = html.replace(old_v18_toggle, new_v18_toggle, 1)

old_ch18_branch = """      } else if (chNum === 18) {
        if (typeof setTabCh18 === 'function') setTabCh18('concepts');
        if (typeof renderCartesianGrid === 'function') renderCartesianGrid();
        if (typeof plotPoint === 'function') plotPoint(3, 4);
        if (window.MathJax && window.MathJax.Hub && v18) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v18]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v18);
        }
      }
    }"""

new_ch18_branch = """      } else if (chNum === 18) {
        if (typeof setTabCh18 === 'function') setTabCh18('concepts');
        if (typeof renderCartesianGrid === 'function') renderCartesianGrid();
        if (typeof plotPoint === 'function') plotPoint(3, 4);
        if (window.MathJax && window.MathJax.Hub && v18) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v18]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v18);
        }
      } else if (chNum === 19) {
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

if old_ch18_branch not in html:
    print("ERROR: old_ch18_branch not found!")
    sys.exit(1)

html = html.replace(old_ch18_branch, new_ch18_branch, 1)
print("3. switchChapter updated successfully.")

# 4. Insert Chapter 19 script
with open('scratch/ch19_script.js', 'r', encoding='utf-8') as f:
    ch19_script = f.read()

urlparams_marker = "const urlParams = new URLSearchParams(window.location.search);"
if urlparams_marker not in html:
    print("ERROR: urlparams_marker not found!")
    sys.exit(1)

html = html.replace(urlparams_marker, ch19_script + "\n\n    " + urlparams_marker, 1)
print("4. Chapter 19 script inserted successfully.")

# 5. Update router
old_router = """    const activeChParam = urlParams.get('ch') || '14';
    if (activeChParam === '18') {
      switchChapter(18);
      if (urlParams.get('tab')) {
        setTabCh18(urlParams.get('tab'));
      }
    } else if (activeChParam === '17') {"""

new_router = """    const activeChParam = urlParams.get('ch') || '14';
    if (activeChParam === '19') {
      switchChapter(19);
      if (urlParams.get('tab')) {
        setTabCh19(urlParams.get('tab'));
      }
    } else if (activeChParam === '18') {
      switchChapter(18);
      if (urlParams.get('tab')) {
        setTabCh18(urlParams.get('tab'));
      }
    } else if (activeChParam === '17') {"""

if old_router not in html:
    print("ERROR: old_router not found!")
    sys.exit(1)

html = html.replace(old_router, new_router, 1)
print("5. URL router updated successfully.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("ALL CHANGES WRITTEN TO index.html SUCCESSFULLY!")
