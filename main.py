#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#made by Simon Poulet-Alligand and Mathias Briolet
import AFVM.index
import lib.cmdUtils.cmdUtils as cutils


def main():
	log = cutils.CmdHandler(AFVM.index.f_list, "MAIN")
	# uncomment to toggle debug
	#log.isDebug = True 
	log.info("Bienvenu dans le programme de manipulation d'image")
	log.info("Pour connaitre la liste des commandes disponibles, ecrivez \"help\" puis ENTRÉE")
	log.info("Pour plus d'info, veuilliez lire le fichier README.txt")
	running = True
	while running:
		try:
			log.handle_input()
		except KeyboardInterrupt:
			if cutils.validate("Quitter le logiciel ?"):
				exit()


if __name__ == "__main__":
	main()
