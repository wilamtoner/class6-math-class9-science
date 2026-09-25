# -*- coding: utf-8 -*-
"""
Integrate Class 9 Unit 7 (Force and Motion) into index.html
and synchronize tracked bundle HTML files.
"""
import sys
import hashlib

print("Reading index.html, scratch/c9u7_html.html, and scratch/c9u7_js.js ...")

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

with open("scratch/c9u7_html.html", "r", encoding="utf-8") as f:
    c9u7_html = f.read()

with open("scratch/c9u7_js.js", "r", encoding="utf-8") as f:
    c9u7_js = f.read()

# 1. Target location for HTML insertion
target_html_marker = "<!-- Placeholder View for Units 7 to 19 -->"
if target_html_marker not in index_content:
    print("ERROR: target_html_marker not found in index.html!")
    sys.exit(1)

new_placeholder_comment = "<!-- Placeholder View for Units 8 to 19 -->"
new_placeholder_desc = "यस एकाइको अध्ययन सामग्री तथा अभ्यास समाधान तयारीमा छ। हाल एकाइ १ देखि एकाइ ७ सम्म पूर्ण रूपमा उपलब्ध छन्।"

index_content = index_content.replace(
    '<p id="c9-placeholder-desc" class="text-xs md:text-sm text-slate-500 mt-1 max-w-md">यस एकाइको अध्ययन सामग्री तथा अभ्यास समाधान तयारीमा छ। हाल एकाइ १ देखि एकाइ ६ सम्म पूर्ण रूपमा उपलब्ध छन्।</p>',
    f'<p id="c9-placeholder-desc" class="text-xs md:text-sm text-slate-500 mt-1 max-w-md">{new_placeholder_desc}</p>'
)

# Insert c9u7_html before placeholder view
index_content = index_content.replace(target_html_marker, f"{c9u7_html}\n\n      {new_placeholder_comment}")

# 2. Target location for JS insertion
target_js_marker = "const urlParams = new URLSearchParams(window.location.search);"
if target_js_marker not in index_content:
    print("ERROR: target_js_marker not found in index.html!")
    sys.exit(1)

index_content = index_content.replace(target_js_marker, f"{c9u7_js}\n\n  {target_js_marker}")

# 3. Update switchGrade9Unit to include v7
old_switch_code = """  const v1 = document.getElementById('c9-view-1');
  const v2 = document.getElementById('c9-view-2');
  const v3 = document.getElementById('c9-view-3');
  const v4 = document.getElementById('c9-view-4');
  const v5 = document.getElementById('c9-view-5');
  const v6 = document.getElementById('c9-view-6');
  const vPlaceholder = document.getElementById('c9-placeholder-view');

  if (v1) v1.classList.add('hidden');
  if (v2) v2.classList.add('hidden');
  if (v3) v3.classList.add('hidden');
  if (v4) v4.classList.add('hidden');
  if (v5) v5.classList.add('hidden');
  if (v6) v6.classList.add('hidden');
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
  } else if (unitNum === 4) {
    if (v4) v4.classList.remove('hidden');
    setTabC9U4('concepts');
    setLabModeC9U4('anatomy');
    setAnatomySubModeC9U4('homology');
    if (typeof initC9U4 === 'function') initC9U4();
  } else if (unitNum === 5) {
    if (v5) v5.classList.remove('hidden');
    setTabC9U5('concepts');
    setLabModeC9U5('tissues');
    if (typeof initC9U5 === 'function') initC9U5();
  } else if (unitNum === 6) {
    if (v6) v6.classList.remove('hidden');
    setTabC9U6('concepts');
    setLabModeC9U6('ecosystem');
    if (typeof initC9U6 === 'function') initC9U6();
  } else {"""

new_switch_code = """  const v1 = document.getElementById('c9-view-1');
  const v2 = document.getElementById('c9-view-2');
  const v3 = document.getElementById('c9-view-3');
  const v4 = document.getElementById('c9-view-4');
  const v5 = document.getElementById('c9-view-5');
  const v6 = document.getElementById('c9-view-6');
  const v7 = document.getElementById('c9-view-7');
  const vPlaceholder = document.getElementById('c9-placeholder-view');

  if (v1) v1.classList.add('hidden');
  if (v2) v2.classList.add('hidden');
  if (v3) v3.classList.add('hidden');
  if (v4) v4.classList.add('hidden');
  if (v5) v5.classList.add('hidden');
  if (v6) v6.classList.add('hidden');
  if (v7) v7.classList.add('hidden');
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
  } else if (unitNum === 4) {
    if (v4) v4.classList.remove('hidden');
    setTabC9U4('concepts');
    setLabModeC9U4('anatomy');
    setAnatomySubModeC9U4('homology');
    if (typeof initC9U4 === 'function') initC9U4();
  } else if (unitNum === 5) {
    if (v5) v5.classList.remove('hidden');
    setTabC9U5('concepts');
    setLabModeC9U5('tissues');
    if (typeof initC9U5 === 'function') initC9U5();
  } else if (unitNum === 6) {
    if (v6) v6.classList.remove('hidden');
    setTabC9U6('concepts');
    setLabModeC9U6('ecosystem');
    if (typeof initC9U6 === 'function') initC9U6();
  } else if (unitNum === 7) {
    if (v7) v7.classList.remove('hidden');
    setTabC9U7('concepts');
    setLabModeC9U7('kinematics');
    if (typeof initC9U7 === 'function') initC9U7();
  } else {"""

if old_switch_code not in index_content:
    print("ERROR: old_switch_code not found in index.html!")
    sys.exit(1)

index_content = index_content.replace(old_switch_code, new_switch_code)

# Write updated index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Successfully written to index.html!")

# Synchronize tracked bundle target: कक्षा_६_गणित_डिजिटल_साथी.html
bundle_target = "कक्षा_६_गणित_डिजिटल_साथी.html"
with open(bundle_target, "w", encoding="utf-8") as f:
    f.write(index_content)
print(f"Updated {bundle_target}!")

print("\nVerifying MD5 checksums:")
md5_index = hashlib.md5(open("index.html", "rb").read()).hexdigest()
md5_bundle = hashlib.md5(open(bundle_target, "rb").read()).hexdigest()
print(f"index.html: {md5_index}")
print(f"{bundle_target}: {md5_bundle}")

if md5_index == md5_bundle:
    print("\nSUCCESS: 100% byte-for-byte parity confirmed across both bundle files!")
else:
    print("\nERROR: MD5 mismatch detected!")
    sys.exit(1)
