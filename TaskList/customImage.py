from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (400, 200), color='skyblue')
d = ImageDraw.Draw(img)
d.text((100, 90), "My Custom Image", fill=(0, 0, 0))
img.save('custom_image.png')
