with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    c = f.read()

bad_part = """    function resetQuizCh5() {
      for (let q = 0; q < 4; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch5-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium';
          }
        }"""

good_part = """    function resetQuizCh5() {
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
    }"""

if bad_part in c:
    c = c.replace(bad_part, good_part, 1)
    print("Replaced successfully!")
else:
    print("Could not find bad_part!")

with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('/home/nepal/.gemini/antigravity/brain/6193a053-8fd9-40c5-8264-be982f512b93/interactive_math_guide.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Saved files!")
