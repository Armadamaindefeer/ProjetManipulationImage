#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#made by Simon Poulet-Alligand and Mathias Briolet
import AFVM.index
import lib.cmdUtils.cmdUtils as cutils

def main():
	log = cutils.CmdHandler(AFVM.index.f_list, "MAIN")
	#log.isDebug = True # uncomment to toggle debug
	log.debug("Teste")
	log.info("Teste info")
	log.error("Teste ERror")
	log.warn("Teste WArn")
	log.fatal("Teste Fatal")
	running = True
	while running:
		try:
			log.handle_input()
		except KeyboardInterrupt:
			if cutils.validate("Quitter le logiciel ?"):
				exit()


if __name__ == "__main__":
	main()
