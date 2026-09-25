with open('notes/20_tathyankashastra_statistics.md', 'r', encoding='utf-8') as f:
    ch20_notes = f.read().strip()

with open('कक्षा_६_गणित_सम्पूर्ण_नोट्स.md', 'r', encoding='utf-8') as f:
    master_content = f.read()

start_marker = '# एकाइ ६: तथ्याङ्कशास्त्र (Unit 6: Statistics)'
idx = master_content.find(start_marker)
assert idx != -1, 'Start marker not found in master notes!'

new_master = master_content[:idx] + ch20_notes + '\n'

with open('कक्षा_६_गणित_सम्पूर्ण_नोट्स.md', 'w', encoding='utf-8') as f:
    f.write(new_master)

print("कक्षा_६_गणित_सम्पूर्ण_नोट्स.md updated successfully with Chapter 20!")
