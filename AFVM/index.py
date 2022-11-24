#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from .AFVM import *
import lib.cmdUtils.cmdUtils as cutils

log = cutils.CmdHandler([], "INDEX")
# uncomment to toggle debug
#log.isDebug = True 

def f_help(func=None) -> None :
	func_list = list(f_list.keys())
	if func==None or not (func in f_list):
		log.info(f"Commandes disponible : {func_list}")
		log.info("Utilisez la commande help <nom_commande> pour obtenir plus d'info sur une commande")
	else:
		log.info(f_list[func][-1])

def f_exit(exit_code : int=0) -> None :
	if cutils.validate("Quitter le logiciel ?"):
		exit(exit_code)
	else:
		log.info("Annulé.")

def check_file(img : Image.Image, file_path):
	if img != None:
		log.debug(f"Ouverture de l'image {file_path} réussi")
	else:
		log.debug(f"Echec de l'ouverture de l'image à {file_path}")

#Créer des pointer vers des fonctions AFVM formatté : rajout de la sauvegarde de l'image
def wrapper_base(func,default_input,default_output,*func_arg) -> object : # function
	log.debug(f"Wrapping {func}")
	def tmp(file_path=default_input):
		img = Image.open(file_path)
		check_file(img,file_path)		
		img = func(img, *func_arg)
		log.info(f"Sauvegarde du fichier dans {default_output}")
		img.save(default_output)
	return tmp

#Modification pour la fonction particulières stegano qui prends deux fichiers par défaut
def wrapper_stegano(func,default_input_1,default_input_2,default_output,*func_arg) -> object :
	log.debug(f"Wrapping {func}")
	def tmp(file_path_1=default_input_1,file_path_2=default_input_2):
		img_1 = Image.open(file_path_1)
		img_2 = Image.open(file_path_1)
		check_file(img_1,file_path_1)
		check_file(img_2,file_path_2)
		img_1 = func(img_1, img_2, *func_arg)
		log.info(f"Sauvegarde du fichier dans {default_output}")
		img_1.save(default_output)
	return tmp


SIZE_WARNING = "La fonction est prévu pour fonctionner avec une image de 500 par 500 pixel, tout autre format fournit via l'argument file_path pourrais mener a des résultats inconnu" 
FORMAT_WARNING = "La fonction est prévu pour opérer sur des fichier .bmp et similaire\nL'emploi de format comme JEPG donne des résultat indéfinissable"
SAVE_MESSAGE = "la sauvegarde dans le ficher output/ sous le nom "
OUTPUT_DIR = "output/"

"""
 "FUNCTIONNAME"	:	[function_ptr,argumentQuantity,(opt)argumentMaxQuantity,usage]
	"PRINT"	: [print,-1,0,"usage"], # Print
	"HELP"	: [help_func,1,"usage"]
	"FUNCTIONNAME" can be anything that isn't  \" or \\ and equivalent
 argumentQuantity is a number greater or equal to -1, it's the number of argument an command require (-1 mean no limitation)
 if argumentQuantity >= -1, argumentMaxQuantity should be written, it represent the max quantity an command require (0 or less mean no limitation)
 usage is always the last parameter it's a str who detail function arg and use
"""

f_list = {
"afvm1"			: [AFVM_1,-1,1,"FORMAT: afvm1 (file_path)\nRetourne les valeurs des différents canaux du pixel (235,252)\n" + SIZE_WARNING],
"afvm2"			: [AFVM_2,-1,1,"FORMAT: afvm2 (file_path)\nRetourne les valeurs des différents canaux du pixel (271,142)\n" + SIZE_WARNING],
"afvm3"			: [wrapper_base(AFVM_3,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM3_out.png"),-1,1,"FORMAT: afvm3 (file_path)\nRemplace le pixel au coordonnées (250,250) par un pixel rouge et " + SAVE_MESSAGE + "AFVM3_out.png\n" + SIZE_WARNING],
"afvm4"			: [wrapper_base(AFVM_4,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM4_out.png"),-1,1,"FORMAT: afvm4 (file_path)\nRemplace le pixel au coordonnées (100,250) par un pixel bleu et " + SAVE_MESSAGE + "AFVM4_out.png\n" + SIZE_WARNING],
"afvm5"			: [wrapper_base(AFVM_5,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM5_out.png"),-1,1,"FORMAT: afvm5 (file_path)\nCrée un rectangle rouge entre les pixel (260,200) et (295,250) et " + SAVE_MESSAGE + "AFVM5_out.png\n" + SIZE_WARNING],
"afvm6"			: [wrapper_base(AFVM_6,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM6_out.png"),-1,1,"FORMAT: afvm6 (file_path)\nModifie l'image pour créer un version en niveau de gris et "+ SAVE_MESSAGE + "AFVM6_out.png"],
"afvm7"			: [wrapper_base(AFVM_7,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM7_out.png"),-1,1,"FORMAT: afvm7 (file_path)\nDonne le negatif d'une image et "+ SAVE_MESSAGE + "AFVM7_out.png"],
"afvm8"			: [wrapper_base(AFVM_8,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM8_out.png"),-1,1,"FORMAT: afvm8 (file_path)\nDonne la symétrie verticale d'une image et "+ SAVE_MESSAGE + "AFVM8_out.png"],
"afvm9"			: [wrapper_base(AFVM_9,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM9_out.png"),-1,1,"FORMAT: afvm9 (file_path)\nDonne la symétrie horizontale d'une image et "+ SAVE_MESSAGE + "AFVM9_out.png"],
"afvm10"		: [wrapper_base(AFVM_10,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM10_out.png"),-1,1,"FORMAT: afvm10 (file_path)\nApplique une rotation des aiguille d'une montre sur l'image et "+ SAVE_MESSAGE + "AFVM10_out.png"],
"afvm11"		: [wrapper_base(AFVM_11,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM11_out.png"),-1,1,"FORMAT: afvm11 (file_path)\nPermet de choisir une rotation a appliquer sur l'image et "+ SAVE_MESSAGE + "AFVM11_out.png"],
"afvm13"		: [wrapper_base(AFVM_13,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}AFVM13_out.png"),-1,2,"FORMAT: afvm10 (file_path) (seuil)\n"+ SAVE_MESSAGE + "AFVM13_out.png"],
"noirEtBlanc"	: [wrapper_base(noirEtBlanc,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}noirEtBlanc_out.png"),-1,2,"FORMAT: noirEtBlanc (file_path) (seuil)\nConverti une image en noir et blanc selon un seuil [default:128]et "+ SAVE_MESSAGE + "noirEtBlanc.bmp\n" + FORMAT_WARNING],
"miseAZero"		: [wrapper_base(mise_a_zero_bit_faible,DEFAULT_FILE_PATH,f"{OUTPUT_DIR}mise_a_zero_bit_faible_out.bmp"),-1,1,"FORMAT: miseAZero (file_path)\nSupprime les 4 bits de poids faible de chaque couleur de chaque pixel de l'image et "+ SAVE_MESSAGE + "mise_a_zero_bit_faible.bmp\n" + FORMAT_WARNING],
"decalage"		: [wrapper_base(decalage4BitsVersLaDroite,DEFAULT_TABLEAU,f"{OUTPUT_DIR}decalage4BitsVersLaDroite_out.bmp"),-1,1,"FORMAT: decalage (file_path)\nDécale les bits vers la droite de 4 de chaque couleur de chaque pixel de l'image et "+ SAVE_MESSAGE + "decalage4BitsVersLaDroite.bmp\n" + FORMAT_WARNING],
"stegano"		: [wrapper_stegano(stegano,DEFAULT_PONT_SOUPIR,DEFAULT_TABLEAU,f"{OUTPUT_DIR}stegano_out.bmp"),-1,2,"FORMAT: stegano (file_path_1) (file_path_2)\nCache une image (file_path_2) a l'intérieur d'une autre (file_path_1) à l'aide des fonction decalage et miseAZero puis " + SAVE_MESSAGE + "stegano.bmp\n" + FORMAT_WARNING],
"defaire"		: [wrapper_base(defaire,DEFAULT_SOUVENIR_VACANCES,f"{OUTPUT_DIR}defaire_out.bmp"),-1,1,"FORMAT: defaire (file_path)\nExtrait une image cacher par la fonction stegano puis " + SAVE_MESSAGE + "defaire.bmp\n" + FORMAT_WARNING],
"help"			: [f_help,-1,1,"FORMAT: help (fonction)\n"],
"exit"			: [f_exit,-1,1,"FORMAT: exit (exit_code)\n"],
}
