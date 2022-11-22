from PIL import Image
def AFVM_9():
	img = Image.open("pomme.png")
	img = img.transpose(Image.FLIP_TOP_BOTTOM)
	img.save("output/pomme_symetrique_h.png")
	img.show()
