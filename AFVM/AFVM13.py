from PIL import Image
img = Image.open("image_niveaux_gris.png")
hauteur_image = img.height
largeur_image = img.width
valeur_seuil = 40
valeur_seuil = 2 * (valeur_seuil**2)
img2 = Image.new("RGB",(largeur_image,hauteur_image))
for y in range(hauteur_image):
	for x in range(largeur_image):


		
		norme = 40 * 40
		if norme > valeur_seuil:
			img2.putpixel
		else:
			img2.putpixel
img2.show()
