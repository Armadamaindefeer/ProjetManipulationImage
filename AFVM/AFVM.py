from PIL import Image

OUTPUT_DIR = "output/"
DEFAULT_FILE_PATH = "lib/picture_backups/pomme.png"

def AFVM_1(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	r,v,b=img.getpixel((235,252))
	print("canal rouge : ",r,"canal vert : ",v,"canal bleu : ",b)

def AFVM_2(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	r,v,b=img.getpixel((271,142))
	print("canal rouge : ",r,"canal vert : ",v,"canal bleu : ",b)

def AFVM_3(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	img.putpixel((250,250), (255,0,0))
	img.save(OUTPUT_DIR + "AFVM3_out.png")
	img.show()

def AFVM_4(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	img.putpixel((100,250), (0,0,255))
	img.save(OUTPUT_DIR + "AFVM4_out.png")
	img.show()

def AFVM_5(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	for y in range(200, 250):
		for x in range(260, 295):
			img.putpixel((x,y), (255,0,0))
	img.save(OUTPUT_DIR + "AFVM5_out.png")
	img.show()

def AFVM_6(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b=img.getpixel((x,y))
			gris = (r+v+b) // 3
			img.putpixel((x,y), (gris,gris,gris))
	img.save(OUTPUT_DIR + "AFVM6_out.png")
	img.show()

def AFVM_7(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	hauteur_image = img.height
	largeur_image = img.width
	for y in range(hauteur_image):
		for x in range(largeur_image):
			r,v,b=img.getpixel((x,y))
			gris = (r+v+b) // 3
			inversed = 255-gris
			img.putpixel((x,y), (inversed,inversed,inversed))
	img.save(OUTPUT_DIR + "AFVM7_out.png")
	img.show()

def AFVM_8(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	img = img.transpose(Image.FLIP_LEFT_RIGHT)
	img.save(OUTPUT_DIR + "AFVM8_out.png")
	img.show()

def AFVM_9(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	img = img.transpose(Image.FLIP_TOP_BOTTOM)
	img.save(OUTPUT_DIR + "AFVM9_out.png")
	img.show()

def AFVM_10(file_path : str = DEFAULT_FILE_PATH):
	img = Image.open(file_path)
	img = img.transpose(Image.ROTATE_270)
	img.save(OUTPUT_DIR + "AFVM10_out.png")
	img.show()
