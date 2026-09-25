from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('assets/fonts/preeti.otf', 40)
im = Image.new('RGB', (260, 60), (255, 255, 255))
d = ImageDraw.Draw(im)
d.text((20, 10), 'kf7 !M ;d"x', font=font, fill=(0, 0, 0)) # पाठ १: समूह
im.save('scratch/test_preeti_m_colon.png')
print('Saved scratch/test_preeti_m_colon.png')
