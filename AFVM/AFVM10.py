from PIL import Image
def AFVM_10():
	img = Image.open("pomme.png")
	img = img.transpose(Image.ROTATE_270)
	img.save("output/pomme_90_degrés_r.png")
	img.show()
