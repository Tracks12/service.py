#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect, json, os

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
with open("{}/../conf.json".format(path), 'r') as conf:
	color = json.load(conf)['color']
	conf.close()

class color:
	if(color):
		BOLD       = '\033[1m'
		ITALIC     = '\033[3m'
		
		GRAY       = '\033[30m'
		RED        = '\033[31m'
		GREEN      = '\033[32m'
		YELLOW     = '\033[33m'
		BLUE       = '\033[34m'
		PURPLE     = '\033[35m'
		CYAN       = '\033[36m'
		WHITE      = '\033[37m'
		CRIMSON    = '\033[38m'
		
		RED_HL     = '\033[41m'
		GREEN_HL   = '\033[42m'
		BROWN_HL   = '\033[43m'
		BLUE_HL    = '\033[44m'
		PURPLE_HL  = '\033[45m'
		CYAN_HL    = '\033[46m'
		GRAY_HL    = '\033[47m'
		WHITE_HL   = '\033[48m'
		
		END        = '\033[0m'
	
	else:
		BOLD = ITALIC = END = ''
		GRAY = RED = GREEN = YELLOW = BLUE = PURPLE = CYAN = WHITE = CRIMSON = ''
		RED_HL = GREEN_HL = BROWN_HL = BLUE_HL = PURPLE_HL = CYAN_HL = GRAY_HL = WHITE_HL = ''

"""
	-----
	 END
	-----
"""
