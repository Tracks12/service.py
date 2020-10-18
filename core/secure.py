#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	---------------------
	 Name    : secure.py
	---------------------
"""

import sys

def authentic(inf):
	truth = {
		"author": "Anarchy",
		"repository": "https://tracks12.github.io/service.py/",
		"size": [21090, 21050]
	}

	if(sys.version_info[0] == 2): x = 0
	elif(sys.version_info[0] == 3): x = 1

	checking = True
	if(inf[1] != truth['author']): checking = False
	if(inf[4] != truth['repository']): checking = False
	if(len(open("{}/{}".format(inf[6], inf[2]), 'r').read()) != truth['size'][x]): checking = False

	return checking
