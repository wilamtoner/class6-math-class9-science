# -*- coding: utf-8 -*-
with open('notes/06_pratishat_percentage.md', 'r', encoding='utf-8') as f:
    ch6_md = f.read()

with open('कक्षा_६_गणित_सम्पूर्ण_नोट्स.md', 'r', encoding='utf-8') as f:
    master = f.read()

start_marker = "## पाठ ६: प्रतिशत (Percentage)"
pos_start = master.find(start_marker)
if pos_start == -1:
    print("Error: start_marker not found!")
    exit(1)

# Backtrack to preceding "# एकाइ २: अङ्कगणित"
pos_unit = master.rfind("# एकाइ २: अङ्कगणित (Unit 2: Arithmetic)", 0, pos_start)
if pos_unit == -1:
    print("Warning: unit marker not found before start_marker, using pos_start")
    replace_start = pos_start
else:
    replace_start = pos_unit

end_marker = "## पाठ ७: नाफा र नोक्सान (Profit and Loss)"
pos_end = master.find(end_marker)
if pos_end == -1:
    print("Error: end_marker not found!")
    exit(1)

# Find the '\newpage' or '---' before pos_end
pos_cut = master.rfind("\\newpage", pos_start, pos_end)
if pos_cut == -1:
    pos_cut = master.rfind("---", pos_start, pos_end)

print(f"Replacing from index {replace_start} to {pos_cut}")

new_ch6_section = f"""# एकाइ २: अङ्कगणित (Unit 2: Arithmetic)
{ch6_md}
"""

new_master = master[:replace_start] + new_ch6_section + master[pos_cut:]

with open('कक्षा_६_गणित_सम्पूर्ण_नोट्स.md', 'w', encoding='utf-8') as f:
    f.write(new_master)

print("Updated कक्षा_६_गणित_सम्पूर्ण_नोट्स.md successfully! New size:", len(new_master.encode('utf-8')), "bytes")
