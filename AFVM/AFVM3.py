from PIL import Image
img = Image.open("pomme.png")
img.putpixel((250,250), (255,0,0))
img.show()