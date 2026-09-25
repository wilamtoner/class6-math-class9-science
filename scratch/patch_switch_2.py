import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

search_str = """  } else if (unitNum === 5) {
    if (v5) v5.classList.remove('hidden');
    setTabC9U5('concepts');
    setLabModeC9U5('tissues');
    if (typeof initC9U5 === 'function') initC9U5();
  } else {"""

replace_str = """  } else if (unitNum === 5) {
    if (v5) v5.classList.remove('hidden');
    setTabC9U5('concepts');
    setLabModeC9U5('tissues');
    if (typeof initC9U5 === 'function') initC9U5();
  } else if (unitNum === 6) {
    if (v6) v6.classList.remove('hidden');
    if (typeof initC9U6 === 'function') initC9U6();
  } else {"""

if search_str in html:
    html = html.replace(search_str, replace_str)
else:
    print("Could not find search string.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done patching index.html again")
