from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('assets/fonts/preeti.otf', 32)
# test printable ascii from 33 to 126 and high ascii
chars = [chr(i) for i in range(33, 127)]
im = Image.new('RGB', (len(chars) * 35, 70), (255, 255, 255))
d = ImageDraw.Draw(im)
for i, c in enumerate(chars):
    d.text((i * 35 + 5, 5), c, font=font, fill=(0, 0, 0))
    d.text((i * 35 + 5, 45), f"{c} {ord(c)}", fill=(255, 0, 0))
im.save('scratch/all_preeti_ascii.png')
print('Done. Total characters rendered:', len(chars))
