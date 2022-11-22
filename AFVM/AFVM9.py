from PIL import Image
img = Image.open("pomme.png")
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.save("output/pomme_symetrique_h.png")
img.show()
