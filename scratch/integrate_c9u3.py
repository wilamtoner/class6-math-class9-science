# -*- coding: utf-8 -*-
import sys

print("Reading index.html, c9u3_html.html, and c9u3_js.js ...")

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

with open("scratch/c9u3_html.html", "r", encoding="utf-8") as f:
    c9u3_html = f.read()

with open("scratch/c9u3_js.js", "r", encoding="utf-8") as f:
    c9u3_js = f.read()

# 1. Target location for HTML insertion
target_html_marker = "<!-- Placeholder View for Units 3 to 19 -->"
if target_html_marker not in index_content:
    print("ERROR: target_html_marker not found!")
    sys.exit(1)

# Replacement for placeholder
new_placeholder_comment = "<!-- Placeholder View for Units 4 to 19 -->"
new_placeholder_desc = "यस एकाइको अध्ययन सामग्री तथा अभ्यास समाधान तयारीमा छ। हाल एकाइ १, एकाइ २ र एकाइ ३ पूर्ण रूपमा उपलब्ध छन्।"

index_content = index_content.replace(
    '<p id="c9-placeholder-desc" class="text-xs md:text-sm text-slate-500 mt-1 max-w-md">यस एकाइको अध्ययन सामग्री तथा अभ्यास समाधान तयारीमा छ। हाल एकाइ १ र एकाइ २ पूर्ण रूपमा उपलब्ध छन्।</p>',
    f'<p id="c9-placeholder-desc" class="text-xs md:text-sm text-slate-500 mt-1 max-w-md">{new_placeholder_desc}</p>'
)

# Insert c9u3_html before placeholder view
index_content = index_content.replace(target_html_marker, f"{c9u3_html}\n\n      {new_placeholder_comment}")

# 2. Target location for JS insertion
target_js_marker = "const urlParams = new URLSearchParams(window.location.search);"
if target_js_marker not in index_content:
    print("ERROR: target_js_marker not found!")
    sys.exit(1)

index_content = index_content.replace(target_js_marker, f"{c9u3_js}\n\n  {target_js_marker}")

# 3. Update switchGrade9Unit to include v3
old_switch_code = """  const v1 = document.getElementById('c9-view-1');
  const v2 = document.getElementById('c9-view-2');
  const vPlaceholder = document.getElementById('c9-placeholder-view');

  if (v1) v1.classList.add('hidden');
  if (v2) v2.classList.add('hidden');
  if (vPlaceholder) vPlaceholder.classList.add('hidden');

  if (unitNum === 1) {
    if (v1) v1.classList.remove('hidden');
    setTabC9U1('concepts');
    calculateScientificNotation();
    selectC9U1Instrument('ruler');
  } else if (unitNum === 2) {
    if (v2) v2.classList.remove('hidden');
    setTabC9U2('concepts');
    setLabModeC9U2('kingdom');
    selectKingdomC9U2('monera');
  } else {"""

new_switch_code = """  const v1 = document.getElementById('c9-view-1');
  const v2 = document.getElementById('c9-view-2');
  const v3 = document.getElementById('c9-view-3');
  const vPlaceholder = document.getElementById('c9-placeholder-view');

  if (v1) v1.classList.add('hidden');
  if (v2) v2.classList.add('hidden');
  if (v3) v3.classList.add('hidden');
  if (vPlaceholder) vPlaceholder.classList.add('hidden');

  if (unitNum === 1) {
    if (v1) v1.classList.remove('hidden');
    setTabC9U1('concepts');
    calculateScientificNotation();
    selectC9U1Instrument('ruler');
  } else if (unitNum === 2) {
    if (v2) v2.classList.remove('hidden');
    setTabC9U2('concepts');
    setLabModeC9U2('kingdom');
    selectKingdomC9U2('monera');
  } else if (unitNum === 3) {
    if (v3) v3.classList.remove('hidden');
    setTabC9U3('concepts');
    setLabModeC9U3('anatomy');
    setAnatomySubModeC9U3('external');
  } else {"""

if old_switch_code not in index_content:
    print("ERROR: old_switch_code not found in index_content!")
    sys.exit(1)

index_content = index_content.replace(old_switch_code, new_switch_code)

# Backup current index.html before overwriting
with open("index.html.bak_before_c9u3", "w", encoding="utf-8") as f:
    with open("index.html", "r", encoding="utf-8") as orig:
        f.write(orig.read())

# Write updated index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print(f"Successfully integrated C9U3 into index.html! New length: {len(index_content)} bytes")
