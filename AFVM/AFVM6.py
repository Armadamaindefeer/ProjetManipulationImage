from PIL import Image
img = Image.open("pomme.png")
hauteur_image = img.height
largeur_image = img.width
for y in range(hauteur_image):
 for x in range(largeur_image):
  r,v,b=img.getpixel((x,y))
  gris = (r+v+b) // 3
  img.putpixel((x,y), (gris,gris,gris))
img.save("output/pomme_niveaux_gris.png")
img.show()