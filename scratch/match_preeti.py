import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Find system devanagari font
deva_fonts = [
    '/usr/share/fonts/noto/NotoSansDevanagari-Regular.ttf',
    '/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf',
    '/usr/share/fonts/opentype/noto/NotoSansDevanagari-Regular.otf'
]
deva_path = None
for p in deva_fonts:
    if os.path.exists(p):
        deva_path = p
        break

if not deva_path:
    # search using find
    import subprocess
    out = subprocess.check_output(['find', '/usr/share/fonts', '-name', '*Devanagari*.ttf']).decode()
    if out.strip():
        deva_path = out.strip().split('\n')[0]

print('Devanagari font:', deva_path)

preeti_font = ImageFont.truetype('assets/fonts/preeti.otf', 40)
# Let's render 'झ' with devanagari font
if deva_path:
    df = ImageFont.truetype(deva_path, 40)
    im_jha = Image.new('L', (50, 50), 255)
    d = ImageDraw.Draw(im_jha)
    d.text((5, 5), 'झ', font=df, fill=0)
    im_jha.save('scratch/unicode_jha.png')

# Now let's see which chars in preeti look like jha or other consonants
candidates = list(range(33, 127)) + [161, 162, 163, 165, 167, 170, 171, 176, 177, 180, 182, 191, 197, 198, 203, 204, 205, 206, 210, 214, 216, 217, 218, 219, 220, 221, 222, 223, 229, 230, 231, 247]
# Create a grid image of all Preeti chars to inspect
cols = 16
rows = (len(candidates) + cols - 1) // cols
grid_im = Image.new('RGB', (cols * 60, rows * 60), (255, 255, 255))
d = ImageDraw.Draw(grid_im)

for idx, code in enumerate(candidates):
    c = chr(code)
    x = (idx % cols) * 60
    y = (idx // cols) * 60
    d.rectangle([x, y, x+58, y+58], outline=(220, 220, 220))
    d.text((x + 10, y + 5), c, font=preeti_font, fill=(0, 0, 0))
    d.text((x + 5, y + 42), f"{c}({code})", fill=(150, 0, 0))

grid_im.save('scratch/preeti_char_grid.png')
print('Saved scratch/preeti_char_grid.png')
