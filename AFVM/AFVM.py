from PIL import Image
from lib.cmdUtils.cmdUtils import info, debug, warn, error, fatal

OUTPUT_DIR = "output/"
DEFAULT_FILE_PATH = "lib/picture_backups/pomme.png"
DEFAULT_PONT_SOUPIR = "lib/picture_backups/pont-soupirs.bmp"
DEFAULT_SOUVENIR_VACANCES = "lib/picture_backups/souvenir-vacances.bmp"
DEFAULT_TABLEAU	= "lib/picture_backups/tableau.bmp"

def AFVM_1(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction donnant les valeurs RVB du pixel y:235 x:252 d'une image donnée
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	r,v,b=img.getpixel((235,252))
	info(f"Image : {file_path} Pixel: (235,252) canal rouge : {r} canal vert : {v} canal bleu : {b}")

def AFVM_2(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction donnant les valeurs RVB du pixel y:271 x:142 d'une image donnée
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	r,v,b=img.getpixel((271,142))
	info(f"Image : {file_path} Pixel: (271,142) canal rouge : {r} canal vert : {v} canal bleu : {b}")

def AFVM_3(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction changeant le pixel y:250 x:250 en rouge d'une image donnée
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	img.putpixel((250,250), (255,0,0))
	img.save(f"{OUTPUT_DIR}AFVM3_out.png")
	img.show()

def AFVM_4(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction changeant le pixel y:100 x:250 en bleu d'une image donnée
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	img.putpixel((100,250), (0,0,255))
	img.save(f"{OUTPUT_DIR}AFVM4_out.png")
	img.show()

def AFVM_5(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction changeant les pixels du rectangle y:200 x:250 à y:260 x:295 en rouge d'une image donnée
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	for y in range(200, 250):
		for x in range(260, 295):
			img.putpixel((x,y), (255,0,0))
	img.save(f"{OUTPUT_DIR}AFVM5_out.png")
	img.show()

def AFVM_6(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction transformant une image d'origine en image en niveaux de gris (en utilisant la moyenne des couleurs)
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b=img.getpixel((x,y))
			gris = (r+v+b) // 3
			img.putpixel((x,y), (gris,gris,gris))
	img.save(f"{OUTPUT_DIR}AFVM6_out.png")
	img.show()

def AFVM_7(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction transformant une image d'origine en image en niveaux de gris (en utilisant la moyenne des couleurs) puis inversant les couleurs
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b=img.getpixel((x,y))
			gris = (r+v+b) // 3
			inversed = 255-gris
			img.putpixel((x,y), (inversed,inversed,inversed))
	img.save(f"{OUTPUT_DIR}AFVM7_out.png")
	img.show()

def AFVM_8(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction transformant une image d'origine en son symétrique suivant un axe vertical
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	img = img.transpose(Image.FLIP_LEFT_RIGHT)
	img.save(f"{OUTPUT_DIR}AFVM8_out.png")
	img.show()

def AFVM_9(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction transformant une image d'origine en son symétrique suivant un axe horizontal
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	img = img.transpose(Image.FLIP_TOP_BOTTOM)
	img.save(f"{OUTPUT_DIR}AFVM9_out.png")
	img.show()

def AFVM_10(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction applicant une rotation de 90° dans le sens horaire d'une image donnée
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	img = img.transpose(Image.ROTATE_270)
	img.save(f"{OUTPUT_DIR}AFVM10_out.png")
	img.show()

def AFVM_11(file_path : str = DEFAULT_FILE_PATH) -> None:
	"""
	Fonction applicant une rotation désirée dans le sens horaire d'une image donnée
	Entrées : Emplacement de l'image
	"""
	img = Image.open(file_path)
	while True:
		answer = int(input("Quelle rotation doit-être appliqué ?\n[1]: 90°\n[2]: 180°\n[3]: 270°\n[1|2|3]:"))
		if answer==1 or answer == 2 or answer == 3:
			if answer==1:
				img = img.transpose(Image.ROTATE_90)
			if answer==2:
				img = img.transpose(Image.ROTATE_180)
			if answer==3:
				img = img.transpose(Image.ROTATE_270)
			img.save(f"{OUTPUT_DIR}AFVM11_out.png")
			img.show()
			return
		print("Réponse incorrecte, ressayez")

#AFVM_12 -> explication

def AFVM_13():
	pass

#AFVM_14 -> Programme qui rassemble tout

#AFVM_15
def noirEtBlanc(file_path : str=DEFAULT_FILE_PATH, seuil : int=128) -> None :	
	img = Image.open(file_path)
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b = img.getpixel((x,y))
			gris = (r+v+b) // 3
			if gris > seuil:
				img.putpixel((x,y), (255,255,255))
			else:
				img.putpixel((x,y), (0,0,0))
	img.save(f"{OUTPUT_DIR}noirEtBlanc.png")
	img.show()


def stegano_mask(file_path : str, mask : int=0b11110000) :	
	img = Image.open(file_path)
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


#AFVM_16
def mise_a_zero_bit_faible(file_path : str=DEFAULT_PONT_SOUPIR, mask : int=0b11110000) -> None :	
	img = stegano_mask(file_path, mask)
	img.save(f"{OUTPUT_DIR}mise_a_zero_bit_faible.bmp")
	img.show()


def stegano_bitshift(file_path : str) :
	img = Image.open(file_path)
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


#AFVM17
def decalage4BitsVersLaDroite(file_path : str=DEFAULT_TABLEAU) -> None :
	img = stegano_bitshift(file_path)
	img.save(f"{OUTPUT_DIR}decalage4BitsVersLaDroite.bmp")
	img.show()


#AFVM_18
def stegano(file_path_1 : str=DEFAULT_PONT_SOUPIR, file_path_2 : str=DEFAULT_TABLEAU) -> None :	
	img_1 = stegano_mask(file_path_1, 0b11110000)
	img_2 = stegano_bitshift(file_path_2)
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
	img_1.save(f"{OUTPUT_DIR}stegano.bmp")
	img_1.show()


#AFVM19
def defaire(file_path : str=DEFAULT_SOUVENIR_VACANCES) -> None :
	img_1 = Image.open(file_path)
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
	img_2.save(f"{OUTPUT_DIR}defaire.bmp")
	img_1.show()
	img_2.show()

