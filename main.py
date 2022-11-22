#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#made by Simon Poulet-Alligand and Mathias Briolet
import AFVM.index
import lib.cmdUtils.cmdUtils

def main():
	log = lib.cmdUtils.cmdUtils.CmdHandler(AFVM.index.f_list, "MAIN")
	#log.isDebug = True #Uncomment to toggle debug
	log.debug("Teste")
	log.info("Teste info")
	log.error("Teste ERror")
	log.warn("Teste WArn")
	log.fatal("Teste Fatal")
	log.handle_input()


if __name__ == "__main__":

	main()
