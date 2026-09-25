# -*- coding: utf-8 -*-
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Target block around resetQuizCh5
target_broken = """    function resetQuizCh5() {
      for (let q = 0; q < 4; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch5-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium';
          }
        }

    function setTabCh6(tabName) {"""

fixed_reset_ch5 = """    function resetQuizCh5() {
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

    function setTabCh6(tabName) {"""

if target_broken in html:
    html = html.replace(target_broken, fixed_reset_ch5)
    print("Fixed resetQuizCh5 header successfully!")
else:
    print("Error: target_broken not found!")
    exit(1)

# Remove the dangling ch5 footer at lines 6236-6247
target_dangling = """        const badge = document.getElementById('ch5-qbadge-' + q);
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
    }"""

if target_dangling in html:
    html = html.replace(target_dangling, "")
    print("Removed dangling ch5 footer successfully!")
else:
    print("Error: target_dangling not found!")
    exit(1)

# Add explicit window bindings right before urlParams
explicit_bindings = """
    // Explicit global bindings for interactive handlers
    window.setTabCh6 = setTabCh6;
    window.setExerciseCh6 = setExerciseCh6;
    window.updateCh6Visualizer = updateCh6Visualizer;
    window.runCh6Calc1 = runCh6Calc1;
    window.runCh6Calc2 = runCh6Calc2;
    window.checkQuizCh6 = checkQuizCh6;
    window.resetQuizCh6 = resetQuizCh6;
    window.switchChapter = switchChapter;
    window.setTabCh5 = setTabCh5;
    window.setExerciseCh5 = setExerciseCh5;
    window.checkQuizCh5 = checkQuizCh5;
    window.resetQuizCh5 = resetQuizCh5;
"""

pos_url = html.find('const urlParams = new URLSearchParams')
html = html[:pos_url] + explicit_bindings + "\n    " + html[pos_url:]
print("Added explicit window bindings!")

with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('/home/nepal/.gemini/antigravity/brain/6193a053-8fd9-40c5-8264-be982f512b93/interactive_math_guide.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved both HTML files successfully!")
