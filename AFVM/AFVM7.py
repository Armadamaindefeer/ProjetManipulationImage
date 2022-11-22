from PIL import Image
def AFVM_7():
	img = Image.open("pomme.png")
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b=img.getpixel((x,y))
			gris = (r+v+b) // 3
			inversed = 255-gris
			img.putpixel((x,y), (inversed,inversed,inversed))
	img.save("output/pomme_négatif.png")
	img.show()
