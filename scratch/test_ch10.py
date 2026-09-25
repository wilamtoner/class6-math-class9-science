from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('assets/fonts/preeti.otf', 40)
im = Image.new('RGB', (320, 60), (255, 255, 255))
d = ImageDraw.Draw(im)
d.text((20, 10), 'kf7 !)M kl/ldlt', font=font, fill=(0, 0, 0)) # पाठ १०: परिमिति
im.save('scratch/test_preeti_ch10.png')
print('Saved scratch/test_preeti_ch10.png')
