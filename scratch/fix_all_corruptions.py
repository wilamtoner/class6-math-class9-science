import re
import os

files_to_fix = [
    'index.html',
    'class6_math_offline.html',
    'कक्षा_६_गणित_डिजिटल_साथी.html',
    'कक्षा_६_गणित_सम्पूर्ण_नोट्स.md',
    'notes/04_bhinna_fractions.md',
    'notes/07_nafa_noksan_profit_loss.md',
    'notes/14_rekha_ra_konharu_lines_angles.md',
    'solutions/unit14_rekha_ra_konharu_solutions.md',
    'solutions/unit13_samikaran_asamanata_solutions.md',
    'solutions/unit7_nafa_noksan_solutions.md',
    'solutions/unit4_bhinna_solutions.md'
]

for path in files_to_fix:
    if not os.path.exists(path):
        continue
    with open(path, 'rb') as f:
        data = f.read()

    orig_len = len(data)
    
    # 1. \x07ngle -> \angle (or if just \x07 followed by ngle)
    data = data.replace(b'\x07ngle', b'\\angle ')
    data = data.replace(b'\x07', b'\\angle ')
    
    # 2. \x0crac -> \frac
    data = data.replace(b'\x0crac', b'\\frac')
    data = data.replace(b'\x0c', b'\\frac')
    
    # 3. \x08ecause -> \because
    data = data.replace(b'\x08ecause', b'\\because')
    data = data.replace(b'\x08', b'\\because')
    
    # 4. \x09heta or tab+heta -> \theta
    # Look for \t followed by heta
    data = data.replace(b'\thetat', b'\\theta')
    data = data.replace(b'\theta', b'\\theta')
    
    # Also check any remaining ' heta' in math context
    data = re.sub(rb'([0-9^\\]+)\s+heta', rb'\1 \\theta', data)

    # In index.html, specific line 12138:
    if 'html' in path:
        # Replace telephone or \angle AOB in the live bar with clean Unicode ∠AOB
        data = data.replace(b'$\\angle AOB = $ <span id="ch14-live-math-deg"', b'<span class="text-base font-bold text-amber-300">\xe2\x88\xa0AOB = </span><span id="ch14-live-math-deg"')
        data = data.replace(b'$ \\angle  AOB = $ <span id="ch14-live-math-deg"', b'<span class="text-base font-bold text-amber-300">\xe2\x88\xa0AOB = </span><span id="ch14-live-math-deg"')

    with open(path, 'wb') as f:
        f.write(data)
    
    print(f"Fixed {path}: {orig_len} bytes -> {len(data)} bytes")

