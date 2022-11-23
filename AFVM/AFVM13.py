from PIL import Image
img = Image.open("image_niveaux_gris.png")
hauteur_image = img.height
largeur_image = img.width
valeur_seuil = 40
valeur_seuil = valeur_seuil*valeur_seuil+valeur_seuil*valeur_seuil
img2 = Image.new("RGB",(largeur_image,hauteur_image))
for y in range(hauteur_image):
    for x in range(largeur_image):
        diff_hg = img.getpixel(x-1,y-1) - img.getpixel(x+1,y+1)
        diff_hg = diff_hg * diff_hg
        diff_hd = img.getpixel(x+1,y-1) - img.getpixel(x-1,y+1)
        diff_hd = diff_hd * diff_hd
        norme = 40 * 40
        if norme > valeur_seuil:
        img2.putpixel...
        else:
        img2.putpixel...
img2.show()
