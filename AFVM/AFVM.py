#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PIL import Image
from lib.cmdUtils.cmdUtils import CmdHandler

log = CmdHandler([], "IMAGE_EDITOR")
# uncomment to toggle debug
#log.isDebug = True 

OUTPUT_DIR = "output/"
DEFAULT_FILE_PATH = "lib/picture_backups/pomme.png"
DEFAULT_PONT_SOUPIR = "lib/picture_backups/pont-soupirs.bmp"
DEFAULT_SOUVENIR_VACANCES = "lib/picture_backups/souvenir-vacances.bmp"
DEFAULT_TABLEAU	= "lib/picture_backups/tableau.bmp"

def check_file(img : Image.Image, file_path):
	if img != None:
		log.debug(f"Ouverture de l'image {file_path} réussi")
	else:
		log.debug(f"Echec de l'ouverture de l'image à {file_path}")


def AFVM_1(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction donnant les valeurs RVB du pixel y:235 x:252 d'une image donnée
	Entrées : objet Image de la bibliothèque PIL (img)
	"""
	img = Image.open(file_path)
	check_file(img, file_path)
	r,v,b=img.getpixel((235,252))
	log.info(f"Image : {file_path} Pixel: (235,252) canal rouge : {r} canal vert : {v} canal bleu : {b}")

def AFVM_2(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction donnant les valeurs RVB du pixel y:271 x:142 d'une image donnée
	Entrées : objet Image de la bibliothèque PIL (img)
	"""
	img = Image.open(file_path)
	check_file(img, file_path)
	r,v,b=img.getpixel((271,142))
	log.info(f"Image : {file_path} Pixel: (271,142) canal rouge : {r} canal vert : {v} canal bleu : {b}")

#DEFAULT_FILE_PATH
#f"{OUTPUT_DIR}AFVM3_out.png"
def AFVM_3(img : Image.Image) -> Image.Image :
	"""
	Fonction changeant le pixel y:250 x:250 en rouge d'une image donnée
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	img.putpixel((250,250), (255,0,0))
	img.show()
	return img

#DEFAULT_FILE_PATH
#"{OUTPUT_DIR}AFVM4_out.png"
def AFVM_4(img : Image.Image) -> Image.Image:
	"""
	Fonction changeant le pixel y:100 x:250 en bleu d'une image donnée
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	img.putpixel((100,250), (0,0,255))
	img.show()
	return img

#DEFAULT_FILE_PATH
#"{OUTPUT_DIR}AFVM5_out.png"
def AFVM_5(img : Image.Image) -> Image.Image:
	"""
	Fonction changeant les pixels du rectangle y:200 x:250 à y:260 x:295 en rouge d'une image donnée
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	for y in range(200, 250):
		for x in range(260, 295):
			img.putpixel((x,y), (255,0,0))
	img.show()
	return img

#DEFAULT_FILE_PATH
#"{OUTPUT_DIR}AFVM6_out.png"
def AFVM_6(img : Image.Image) -> Image.Image:
	"""
	Fonction transformant une image d'origine en image en niveaux de gris (en utilisant la moyenne des couleurs)
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""	
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b=img.getpixel((x,y))
			gris = (r+v+b) // 3
			img.putpixel((x,y), (gris,gris,gris))
	img.show()
	return img

#DEFAULT_FILE_PATH
#"{OUTPUT_DIR}AFVM7_out.png"
def AFVM_7(img : Image.Image) -> Image.Image:
	"""
	Fonction transformant une image d'origine en image en niveaux de gris (en utilisant la moyenne des couleurs) puis inversant les couleurs
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b=img.getpixel((x,y))
			gris = (r+v+b) // 3
			inversed = 255-gris
			img.putpixel((x,y), (inversed,inversed,inversed))
	img.show()
	return img

#DEFAULT_FILE_PATH
#"{OUTPUT_DIR}AFVM8_out.png"
def AFVM_8(img : Image.Image) -> Image.Image:
	"""
	Fonction transformant une image d'origine en son symétrique suivant un axe vertical
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	img = img.transpose(Image.FLIP_LEFT_RIGHT)
	img.show()
	return img

#DEFAULT_FILE_PATH
#"{OUTPUT_DIR}AFVM9_out.png"
def AFVM_9(img : Image.Image) -> Image.Image:
	"""
	Fonction transformant une image d'origine en son symétrique suivant un axe horizontal
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	img = img.transpose(Image.FLIP_TOP_BOTTOM)
	img.show()
	return img

#DEFAULT_FILE_PATH
#"{OUTPUT_DIR}AFVM10_out.png"
def AFVM_10(img : Image.Image) -> Image.Image:
	"""
	Fonction applicant une rotation de 90° dans le sens horaire d'une image donnée
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	img = img.transpose(Image.ROTATE_270)
	img.show()
	return img

#DEFAULT_FILE_PATH
#f"{OUTPUT_DIR}AFVM11_out.png"
def AFVM_11(img : Image.Image) -> Image.Image:
	"""
	Fonction applicant une rotation désirée dans le sens horaire d'une image donnée
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img) modifié par la fonction
	"""
	while True:
		answer = int(input("Quelle rotation doit-être appliqué ?\n[1]: 90°\n[2]: 180°\n[3]: 270°\n[1|2|3]:"))
		if answer==1 or answer == 2 or answer == 3:
			if answer==1:
				img = img.transpose(Image.ROTATE_90)
			if answer==2:
				img = img.transpose(Image.ROTATE_180)
			if answer==3:
				img = img.transpose(Image.ROTATE_270)
			img.show()
			return img
		print("Réponse incorrecte, ressayez")

#AFVM_12 -> explication du afvm13
def AFVM_13(img_1 : Image.Image, seuil : int=27) -> Image.Image:
	"""
	Fonction  trace le contour d'une image en fonction d'un seuil
	Entrées : objet Image de la bibliothèque PIL (img) et un entier représentant à partir de quand un pixel est considérer contour
	Sortie : objet Image de la bibliothèque PIL (img_1) modifiée par la fonction
	"""	
	width, height = img_1.size
	seuil = 2 * (seuil**2)
	img_2 = Image.new('RGB', (width, height))
	for x in range(width - 1):
		for y in range(height - 1):
			r1, g1, b1 = img_1.getpixel((x - 1, y + 1))
			gris1 = (r1 + g1 + b1) // 3
			r2, g2, b2 = img_1.getpixel((x + 1, y + 1))
			gris2 = (r2 + g2 + b2) // 3
			r3, g3, b3 = img_1.getpixel((x - 1, y - 1))
			gris3 = (r3 + g3 + b3) // 3
			r4, g4, b4 = img_1.getpixel((x + 1, y - 1))
			gris4 = (r4 + g4 + b4) // 3
			p14 = (gris1 - gris4) ** 2
			p23 = (gris2 - gris3) ** 2
			pt = p14 + p23
			if pt > seuil:
				img_2.putpixel((x, y), (0, 0, 0))
			else:
				img_2.putpixel((x, y), (255, 255, 255))
	img_2.show()
	return img_2

#AFVM_14 -> Programme qui rassemble tout

#DEFAULT_FILE_PATH int=128
#"{OUTPUT_DIR}noirEtBlanc.png"
def noirEtBlanc(img : Image.Image, seuil : int=128 ) -> Image.Image :
	"""
	Fonction  converti l'image en pixel noir et blanc en fonction de la moyenne des couleurs du pixel (par défaut : moyenne couleur > 128 -> pixel noir sinon pixel blanc)
	Entrées : objet Image de la bibliothèque PIL (img) et un entier représentant à partir de quand un pixel est considérer noir
	Sortie : objet Image de la bibliothèque PIL (img_1) modifiée par la fonction
	"""		
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b = img.getpixel((x,y))
			noir = (r+v+b) // 3
			if noir > seuil:
				img.putpixel((x,y), (255,255,255))
			else:
				img.putpixel((x,y), (0,0,0))
	img.show()
	return img


#DEFAULT_PONT_SOUPIR int=0b11110000
#"{OUTPUT_DIR}mise_a_zero_bit_faible.bmp")
def mise_a_zero_bit_faible(img : Image.Image, mask : int=0b11110000) -> Image.Image :
	"""
	Fonction  mets a zéro les 4 bits de poids faible de chaque couleur de chaque pixel de l'image
	Entrées : objet Image de la bibliothèque PIL (img) et un entier représentant un masque binaire afficher par la fonction
	Sortie : objet Image de la bibliothèque PIL (img_1) modifiée par la fonction
	"""
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b = img.getpixel((x,y))
			r = r & mask
			v = v & mask
			b = b & mask
			img.putpixel((x,y), (r,v,b))
	return img

#DEFAULT_TABLEAU
#"{OUTPUT_DIR}decalage4BitsVersLaDroite.bmp"
def decalage4BitsVersLaDroite(img : Image.Image) -> Image.Image :
	"""
	Fonction décale les 4 bits de poids fort de 4 vers la droite, pour chaque couleur de chaque pixel de l'image
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img_1) modifiée par la fonction
	"""	
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b = img.getpixel((x,y))
			r = r >> 4
			v = v >> 4
			b = b >> 4
			img.putpixel((x,y), (r,v,b))
	return img

#AFVM_18
#DEFAULT_PONT_SOUPIR DEFAULT_TABLEAU
#f"{OUTPUT_DIR}stegano.bmp"
def stegano(img_1 : Image.Image, img_2 : Image.Image) -> Image.Image :
	"""
	Fonction cache une image (img_2) à l'intérieur d'une autre image (img_1) 
	Entrées : 2 objet Image de la bibliothèque PIL (img_1,img_2) où img_2 sera l'image cacher
	Sortie : objet Image de la bibliothèque PIL (img_1) modifiée par la fonction
	"""		
	img_1 = mise_a_zero_bit_faible(img_1, 0b11110000)
	img_2 = decalage4BitsVersLaDroite(img_2)
	hauteur_image = img_1.height
	largeur_image = img_1.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r_1, v_1, b_1 = img_1.getpixel((x,y))
			r_2, v_2, b_2 = img_2.getpixel((x,y))
			r_1 = r_1 | r_2
			v_1 = v_1 | v_2
			b_1 = b_1 | b_2	
			img_1.putpixel((x,y), (r_1,v_1,b_1))
	img_1.show()
	return img_1

#AFVM19
#DEFAULT_SOUVENIR_VACANCES
#"{OUTPUT_DIR}defaire.bmp"
def defaire(img_1 : Image.Image ) -> Image.Image : 
	"""
	Fonction extrait une image (img_2) cacher dans l'image img_1 par la fonction stegano
	Entrées : objet Image de la bibliothèque PIL (img)
	Sortie : objet Image de la bibliothèque PIL (img_2) extrait par la fonction
	"""
	height = img_1.height
	width = img_1.width
	img_2 = Image.new("RGB",(width,height))
	for y in range(height):
		for x in range(width):
			r_1, v_1, b_1 = img_1.getpixel((x,y))
			r_2 = (r_1 & 0b00001111) << 4
			v_2 = (v_1 & 0b00001111) << 4
			b_2 = (b_1 & 0b00001111) << 4
			img_2.putpixel((x,y), (r_2,v_2,b_2))
	img_1.show()
	img_2.show()
	return img_2
