from PIL import Image
img = Image.open("pomme.png")
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.save("output/pomme_symetrique_v.png")
img.show()
