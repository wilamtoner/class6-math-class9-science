# -*- coding: utf-8 -*-
import sys
import hashlib
import shutil

print("Starting enhanced integration of Unit 4...")

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

with open("scratch/c9u4_html.html", "r", encoding="utf-8") as f:
    c9u4_html = f.read()

with open("scratch/c9u4_js.js", "r", encoding="utf-8") as f:
    c9u4_js = f.read()

# 1. HTML Replacement
h_marker_start = '<!-- Grade 9 Unit 4: Evolution (जीवहरूको विकास) View -->'
if h_marker_start not in index_content:
    h_marker_start = '<div id="c9-view-4"'

h_start = index_content.find(h_marker_start)
h_end_marker = '<!-- Placeholder View for Units 5 to 19 -->'
h_end = index_content.find(h_end_marker)

if h_start == -1 or h_end == -1:
    print(f"ERROR: HTML markers not found! h_start={h_start}, h_end={h_end}")
    sys.exit(1)

# Keep the placeholder comment and preceding indentation
index_content = index_content[:h_start] + c9u4_html + "\n\n      " + index_content[h_end:]
print("Replaced Unit 4 HTML.")

# 2. JS Replacement
js_start_marker = '// =========================================================================\n// GRADE 9 UNIT 4: EVOLUTION'
if js_start_marker not in index_content:
    js_start_marker = '// GRADE 9 UNIT 4: EVOLUTION'
js_start = index_content.find(js_start_marker)
js_end_marker = 'const urlParams = new URLSearchParams(window.location.search);'
js_end = index_content.find(js_end_marker)

if js_start == -1 or js_end == -1:
    print(f"ERROR: JS markers not found! js_start={js_start}, js_end={js_end}")
    sys.exit(1)

index_content = index_content[:js_start] + c9u4_js.strip() + "\n\n  " + index_content[js_end:]
print("Replaced Unit 4 JS.")

# 3. Add initC9U4() to switchGrade9Unit if not present
old_u4_block = """  } else if (unitNum === 4) {
    if (v4) v4.classList.remove('hidden');
    setTabC9U4('concepts');
    setLabModeC9U4('anatomy');
    setAnatomySubModeC9U4('homology');"""

new_u4_block = """  } else if (unitNum === 4) {
    if (v4) v4.classList.remove('hidden');
    setTabC9U4('concepts');
    setLabModeC9U4('anatomy');
    setAnatomySubModeC9U4('homology');
    if (typeof initC9U4 === 'function') initC9U4();"""

if old_u4_block in index_content:
    index_content = index_content.replace(old_u4_block, new_u4_block)
    print("Added initC9U4() to switchGrade9Unit.")
else:
    print("Note: old_u4_block not found or already modified.")

# Double virama check
assert '\u094d\u094d' not in index_content, "Double virama detected!"

# Write updated index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
print("Updated index.html successfully.")

# Sync to all 4 bundle files
bundle_files = [
    "डिजिटल_गुरु.html",
    "कक्षा_६_गणित_डिजिटल_साथी.html",
    "class6_math_offline.html"
]

for bf in bundle_files:
    shutil.copyfile("index.html", bf)
    print(f"Synchronized {bf}")

# Check MD5 hashes
def get_md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

all_files = ["index.html"] + bundle_files
hashes = {bf: get_md5(bf) for bf in all_files}
print("\nMD5 Checksums:")
for bf, h in hashes.items():
    print(f"  {bf}: {h}")

unique_hashes = set(hashes.values())
if len(unique_hashes) == 1:
    print("\nSUCCESS: All 4 files are 100% byte-for-byte identical!")
else:
    print("\nERROR: MD5 mismatch detected!")
    sys.exit(1)
