from .AFVM import *
import lib.cmdUtils.cmdUtils as cutils

"""
 "FUNCTIONNAME"	:	[function_ptr,argumentQuantity,(opt)argumentMaxQuantity,usage]
	"PRINT"	: [print,-1,0,"usage"], # Print
	"HELP"	: [help_func,1,"usage"]
	"FUNCTIONNAME" can be anything that isn't  \" or \\ and equivalent
 argumentQuantity is a number greater or equal to -1, it's the number of argument an command require (-1 mean no limitation)
 if argumentQuantity >= -1, argumentMaxQuantity should be written, it represent the max quantity an command require (0 or less mean no limitation)
 usage is always the last parameter it's a str who detail function arg and use
"""
def f_help(func=None) -> None :
	func_list = list(f_list.keys())
	if func==None or not (func in f_list):
		print(f"Commandes disponible : {func_list}")
		cutils.info("Essayez d'utiliser une fonction help")
	else:
		cutils.info(f_list[func][-1])
	#for commands in func_list:
	#	print(f"{commands} : \n{f_list[commands][-1]}")

def f_exit(exit_code : int=0) -> None :
	if cutils.validate("Quitter le logiciel ?"):
		exit(exit_code)
	else:
		cutils.info("Annulé.")



SIZE_WARNING = "La fonction est prévu pour fonctionner avec une image de 500 par 500 pixel, tout autre format fournit via l'argument file_path pourrais mener a des résultats inconnu" 
SAVE_MESSAGE = "le sauvegarde dans le ficher output/ sous le nom AFVM_"


f_list = {

"afvm1"			: [AFVM_1,-1,1,"afvm1 (file_path)\nRetourne les valeurs des différents canaux du pixel (235,252)\n" + SIZE_WARNING],
"afvm2"			: [AFVM_2,-1,1,"afvm2 (file_path)\nRetourne les valeurs des différents canaux du pixel (271,142)\n" + SIZE_WARNING],
"afvm3"			: [AFVM_3,-1,1,"afvm3 (file_path)\nRemplace le pixel au coordonnées (250,250) par un pixel rouge et " + SAVE_MESSAGE + "3_out.png\n" + SIZE_WARNING],
"afvm4"			: [AFVM_4,-1,1,"afvm4 (file_path)\nRemplace le pixel au coordonnées (100,250) par un pixel bleu et " + SAVE_MESSAGE + "4_out.png\n" + SIZE_WARNING],
"afvm5"			: [AFVM_5,-1,1,"afvm5 (file_path)\nCrée un rectangle rouge entre les pixel (260,200) et (295,250) et " + SAVE_MESSAGE + "5_out.png\n" + SIZE_WARNING],
"afvm6"			: [AFVM_6,-1,1,"afvm6 (file_path)\nModifie l'image pour créer un version en niveau de gris et "+ SAVE_MESSAGE + "6_out.png"],
"afvm7"			: [AFVM_7,-1,1,"afvm7 (file_path)\nDonne le negatif d'une image et "+ SAVE_MESSAGE + "7_out.png"],
"afvm8"			: [AFVM_8,-1,1,"afvm8 (file_path)\nDonne la symmétrie verticale d'une image et "+ SAVE_MESSAGE + "8_out.png"],
"afvm9"			: [AFVM_9,-1,1,"afvm9 (file_path)\nDonne la symmétrie horizontale d'une image et "+ SAVE_MESSAGE + "9_out.png"],
"afvm10"		: [AFVM_10,-1,1,"afvm10 (file_path)\nApplique une rotation des aiguille d'une montre sur l'image et "+ SAVE_MESSAGE + "10_out.png"],
"afvm11"		: [AFVM_11,-1,1,"afvm10 (file_path)\nPermet de choisir une rotation a appliquer sur l'image et "+ SAVE_MESSAGE + "11_out.png"],
"afvm13"		: [AFVM_13,-1,1,"afvm13 (file_path)"],
"noirEtBlanc"	: [noirEtBlanc,-1,2,"noirEtBlanc (file_path) (seuil)"],
"miseAZero"		: [mise_a_zero_bit_faible,-1,2,"miseAZero (file_path) (mask)"],
"decalage"		: [decalage4BitsVersLaDroite,-1,1,"decalage (file_path)"],
"stegano"		: [stegano,-1,2,"stegano (file_path_1) (file_path_2)"],
"defaire"		: [defaire,-1,1,"usage"],
"help"			: [f_help,-1,1,"help (fonction)"],
"exit"			: [f_exit,-1,1,"usage"]

}
