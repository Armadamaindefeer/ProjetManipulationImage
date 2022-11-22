#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# cmdUtils made by Simon Poulet-Alligand
# Version de développement impliquand fonction non-utilisable

#>>-----------Import----------------<<

import os
import json
import sys
import cmd
import datetime

#>>-----------Constants-------------<<

DEBUG = -1
INFO = 0
WARM = 1
ERROR = 2
CRITICAL = 3
#debug = False
RESET_COLOR = "\033[m"
DEFAULT_COLOR = "\033[38;5;97m"
DEBUG_COLOR = "\033[38;5;240m"
FATAL_COLOR = "\033[38;5;160m"
ERROR_COLOR = "\033[38;5;166m"
WARN_COLOR = "\033[38;5;11m"
INFO_COLOR = "\033[38;5;248m"


#>>-----------Exemple---------------<<
cmd_list_exemple = {
#	"FUNCTIONNAME"	:	[function_ptr,argumentQuantity,(opt)argumentMaxQuantity,usage]
#	"PRINT"	: [print,-1,0,"usage"], # Print
#	"HELP"	: [help_func,1,"usage"]
# "FUNCTIONNAME" can be anything that isn't  \" or \ and equivalent
# argumentQuantity is a number greater or equal to -1, it's the number of argument an command require (-1 mean no limitation)
# if argumentQuantity >= -1, argumentMaxQuantity should be written, it represent the max quantity an command require (0 or less mean no limitation)
# usage is always the las parameter it's a str who detail function arg and use
}



#>>-----------Function--------------<<

#>>-----------Utils------------------<<

def validate(output):
	log("WARN", output, "MAIN", "")
	answer = input(' [Y/n]\n')
	return answer == 'Y' or answer == 'y' or answer == 'o' or answer == 'O' or answer == ""

def log(level, content, source,color=RESET_COLOR,pend='\n'):
	now = datetime.datetime.now()
	hour = '{:02d}'.format(now.hour)
	minute = '{:02d}'.format(now.minute)
	second = '{:02d}'.format(now.second)
	print(f'\r{color}[{hour}:{minute}:{second}][{str(source)}/{level}] {str(content)}{RESET_COLOR}',end=pend)

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

def debug(message, source="MAIN"):
	log("DEBUG", message, source, color=DEBUG_COLOR)

def info(message, source="MAIN"):
	log("INFO", message, source, color=INFO_COLOR)

def warn(message, source="MAIN"):
	log("WARN", message, source, color=WARN_COLOR)

def error(message, source="MAIN"):
	log("ERROR", message, source, color=ERROR_COLOR)

def fatal(message, source="MAIN"):
	log("FATAL", message, source, color=FATAL_COLOR)

#>>-----------COMMANDS-----------------<<
#Revoir le format d'enregistrement des commandes
#Non-tester -> ne pas utiliser

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
	def __init__(self, cmd_list , source : str, debug : bool = False ) -> None:
		self.cmd_list = cmd_list
		self.source = source
		self.format = ""
		self.isDebug = debug

	def debug(self, message):
		if self.isDebug :
			debug(message, self.source)

	def info(self, message):
		info(message, self.source)

	def warn(self, message):
		warn(message, self.source)

	def error(self, message):
		error(message, self.source)

	def fatal(self, message):
		fatal(message, self.source)

	def handle_input(self):
		cmd_input = getline()
		if not cmd_input[0] in self.cmd_list:
			self.warn("Unrecognized commands")
			if "help" in self.cmd_list: self.cmd_list["help"][0]()
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
