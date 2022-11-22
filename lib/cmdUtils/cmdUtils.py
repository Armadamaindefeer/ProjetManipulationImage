#>>-----------Import----------------<<

import os
import json
import sys
import cmd
import datetime
import I10n

#>>-----------Constants-------------<<

DEBUG = -1
INFO = 0
WARM = 1
ERROR = 2
CRITICAL = 3
#debug = False

#>>-----------Exemple---------------<<
cmd_list_exemple = {
#	"FUNCTIONNAME"	:	[function_ptr,argumentQuantity,(opt)argumentMaxQuantity,usage]
#	"PRINT"	: [print,-1,0,"usage"], # Print
#	"HELP"	: [help_func,1,"usage"]
# "FUNCTIONNAME" can be anything that isn't  \" or \ and equivalent
# argumentQuantity is a number greater or equal to -1, it's the number of argument an command require (-1 mean no limitation)
# if argumentQuantity >= -1, argumentMaxQuantity should be wrote, it represent the max quantity an command require (0 or less mean no limitation)
# usage is always the las parameter it's a str who detail function arg and use
}



#>>-----------Function--------------<<

#>>-----------Utils------------------<<

def validate(output):
	log("WARN", output, "MAIN", "")
	answer = input(' [Y/n]\n')
	return answer == 'Y' or answer == 'y' or answer == 'o' or answer == 'O' or answer == ""

def log(level, content, source,pend='\n'):
	now = datetime.datetime.now()
	hour = '{:02d}'.format(now.hour)
	minute = '{:02d}'.format(now.minute)
	second = '{:02d}'.format(now.second)
	print(f'\r[{hour}:{minute}:{second}][{str(source)}/{level}] {str(content)}',end=pend)

def getline():
	cmd_input = input("\n$ ").strip()
	output = []
	temp = ""
	dont_interpret = False
	parenthezis = False
	for i in cmd_input:
		if dont_interpret:
			temp += i
			continue
		if i == "\\":
			temp += i
			dont_interpret = True
			continue

		if i == "\"":
			if parenthezis:
				parenthezis = False
			else:
				parenthezis = True
			continue
		if parenthezis:
			temp += i
			continue
		if i == " ":
			output += [temp]
			temp = ""
			continue
		temp += i
	output += [temp]
	return output

def debug(message):
	log("DEBUG", message, "MAIN")

def info(message):
	log("INFO", message, "MAIN")

def warn(message):
	log("WARN", message, "MAIN")

def error(message):
	log("ERROR", message, "MAIN")

def fatal(message):
	log("FATAL", message, "MAIN")

#Petite triche pour bloquer les input
class InputDisable:

	def start(self):
		self.on = True

	def stop(self):
		self.on = False

	def __init__(self):
		self.on = False
		if sys.platform.startswith('win') :
			import msvcrt as inputDisable
		else: 
			import getch as inputDisable

	def __call__(self): 
		pass


#>>-----------COMMANDS-----------------<<

#Revoir le format d'enregistrement des commandes
class Commands:
	def __init__(self, function , usage, argument=None) -> None:
		self.function = function
		self.usage = usage
		self.argument = argument
		self.argQte = 0
		if not (argument == None):
			for i in argument :
				self.argQte += 1

def f_help():
	pass

command_help = Commands(f_help, "Lorem ipsum")

#>>-----------HANDLER------------------<<

class CmdHandler:
	def __init__(self, cmd_list, source) -> None:
		self.cmd_list = cmd_list
		self.source = source
		self.format = ""

	def log(self, level, content, source):
		now = datetime.datetime.now()
		hour = '{:02d}'.format(now.hour)
		minute = '{:02d}'.format(now.minute)
		second = '{:02d}'.format(now.second)
		print(f'\r[{hour}:{minute}:{second}][{str(source)}/{level}] {str(content)}')

	def debug(self, message):
		log("DEBUG", message, self.source)

	def info(self, message):
		log("INFO", message, self.source)

	def warn(self, message):
		log("WARN", message, self.source)

	def error(self, message):
		log("ERROR", message, self.source)

	def fatal(self, message):
		log("FATAL", message, self.source)

	def handle_input(self):
		cmd_input = getline()
		if not cmd_input[0] in self.cmd_list:
			self.warn("Unrecognized commands")
			if "HELP" in self.cmd_list: self.cmd_list["HELP"][0]()
			return
		# cmd_list[x][1] represent quantity of arguments needed where -1 is infinite
		if self.cmd_list[cmd_input[0]][1] != -1:
			if (len(cmd_input) - 1) > self.cmd_list[cmd_input[0]][1]:
				self.warn(f'Extra parameter for {cmd_input[0]}')
				print(self.cmd_list[cmd_input[0]][-1])
				return
			if (len(cmd_input) - 1) < self.cmd_list[cmd_input[0]][1]:
				self.warn(f'Missing parameter for {cmd_input[0]}')
				print(self.cmd_list[cmd_input[0]][-1])
				return
		elif self.cmd_list[cmd_input[0]][1] == -1:
			if (len(cmd_input) - 1) > self.cmd_list[cmd_input[0]][2] and not self.cmd_list[cmd_input[0]][2] <= 0:
				self.warn(f'Extra parameter for {cmd_input[0]}')
				print(self.cmd_list[cmd_input[0]][-1])
				return
		# cmd_list[x][0] represent function pointer
		self.cmd_list[cmd_input[0]][0](*cmd_input[1:])

	def __futur_handle_input(self):
		cmd_input = getline()
		if not cmd_input[0] in self.cmd_list:
			self.warn("Unrecognized commands")
			return
