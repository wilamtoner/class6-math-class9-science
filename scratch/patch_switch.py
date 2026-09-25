import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add v6 to DOM elements extraction
html = html.replace("const v5 = document.getElementById('c9-view-5');",
                    "const v5 = document.getElementById('c9-view-5');\n  const v6 = document.getElementById('c9-view-6');")

# Add v6 hiding logic
html = html.replace("if (v5) v5.classList.add('hidden');",
                    "if (v5) v5.classList.add('hidden');\n  if (v6) v6.classList.add('hidden');")

# Change logic for showing v6
# The original logic handles u<=5 and placeholder for u>5
search_str = """  if (unitNum === 1 && v1) {
    v1.classList.remove('hidden');
    if (typeof initC9U1 === 'function') initC9U1();
  } else if (unitNum === 2 && v2) {
    v2.classList.remove('hidden');
    if (typeof initC9U2 === 'function') initC9U2();
  } else if (unitNum === 3 && v3) {
    v3.classList.remove('hidden');
    if (typeof initC9U3 === 'function') initC9U3();
  } else if (unitNum === 4 && v4) {
    v4.classList.remove('hidden');
    if (typeof initC9U4 === 'function') initC9U4();
  } else if (unitNum === 5 && v5) {
    v5.classList.remove('hidden');
    if (typeof initC9U5 === 'function') initC9U5();
  } else if (unitNum > 5 && vPlaceholder) {"""

replace_str = """  if (unitNum === 1 && v1) {
    v1.classList.remove('hidden');
    if (typeof initC9U1 === 'function') initC9U1();
  } else if (unitNum === 2 && v2) {
    v2.classList.remove('hidden');
    if (typeof initC9U2 === 'function') initC9U2();
  } else if (unitNum === 3 && v3) {
    v3.classList.remove('hidden');
    if (typeof initC9U3 === 'function') initC9U3();
  } else if (unitNum === 4 && v4) {
    v4.classList.remove('hidden');
    if (typeof initC9U4 === 'function') initC9U4();
  } else if (unitNum === 5 && v5) {
    v5.classList.remove('hidden');
    if (typeof initC9U5 === 'function') initC9U5();
  } else if (unitNum === 6 && v6) {
    v6.classList.remove('hidden');
    if (typeof initC9U6 === 'function') initC9U6();
  } else if (unitNum > 6 && vPlaceholder) {"""

if search_str in html:
    html = html.replace(search_str, replace_str)
else:
    print("Could not find the switch logic string to replace.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done patching switchGrade9Unit")
