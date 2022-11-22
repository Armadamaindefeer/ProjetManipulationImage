from .AFVM import *

#	"FUNCTIONNAME"	:	[function_ptr,argumentQuantity,(opt)argumentMaxQuantity,usage]
#	"PRINT"	: [print,-1,0,"usage"], # Print
#	"HELP"	: [help_func,1,"usage"]
# "FUNCTIONNAME" can be anything that isn't  \" or \ and equivalent
# argumentQuantity is a number greater or equal to -1, it's the number of argument an command require (-1 mean no limitation)
# if argumentQuantity >= -1, argumentMaxQuantity should be written, it represent the max quantity an command require (0 or less mean no limitation)
# usage is always the last parameter it's a str who detail function arg and use

def f_help(func=None):
	func_list = list(f_list.keys())
	if func==None or not (func in f_list):
		print(f"Commandes disponible : {func_list}\nEssayez d'utiliser une fonction help")
	else:
		print(f_list[func][-1])
	#for commands in func_list:
	#	print(f"{commands} : \n{f_list[commands][-1]}")

f_list = {

"1" : [AFVM_1,-1,1,"usage"],
"2" : [AFVM_2,-1,1,"usage"],
"3" : [AFVM_3,-1,1,"usage"],
"4" : [AFVM_4,-1,1,"usage"],
"5" : [AFVM_5,-1,1,"usage"],
"6" : [AFVM_6,-1,1,"usage"],
"7" : [AFVM_7,-1,1,"usage"],
"8" : [AFVM_8,-1,1,"usage"],
"9" : [AFVM_9,-1,1,"usage"],
"10" : [AFVM_10,-1,1,"usage"],
"11" : [AFVM_1,-1,1,"usage"],
"13" : [AFVM_1,-1,1,"usage"],
"noirEtBlanc" : [AFVM_1,"usage"],
"miseAZero" : [AFVM_1,"usage"],
"decalage" : [AFVM_1,"usage"],
"stegano" : [AFVM_1,"usage"],
"help" : [f_help,-1,1,"usage"],

}
