from PIL import Image
img = Image.open("pomme.png")
img.putpixel((100,250), (0,0,255))
img.show()