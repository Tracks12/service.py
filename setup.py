#!/usr/bin/python2
# -*- coding: utf8 -*-

"""
	----------------------
	 Autor   : Anarchy
	 Date    : 16/02/2019
	 Name    : setup.py
	 Version : 0.0.8-a
	----------------------
"""

import sys, os
from cx_Freeze import setup, Executable

if(False in ["build" in sys.argv]):
	os.system("python2 setup.py build")
	exit(1)

properties = {
	"binpathincludes": [],
	"includeFiles": [
		'assets/',
		'conf.json'
	],
	"includes": [
		'core',
	],
	"excludes": [],
	"packages": []
}

if(sys.platform == "win32"):
	pass
elif(sys.platform == "linux2"):
	properties["binpathincludes"].append("/usr/lib")
	pass
else:
	pass

for i, txt in enumerate(properties):
	print("{}\t: {} element(s)".format(txt, len(properties[txt])))
	for output in properties[txt]:
		print(" [*] {}".format(output))

options = {
	"path": sys.path,
	"includes": properties["includes"],
	"excludes": properties["excludes"],
	"packages": properties["packages"],
	"include_files": properties["includeFiles"],
	"bin_path_includes": properties["binpathincludes"],
	"optimize": 0,
	"silent": False
}

base, pic = None, None
if(sys.platform == "win32"):
	base = "Win32GUI" # "Win32GUI". Graph | "Console". Shell
	pic = "icone.ico"
	options["include_msvcr"] = True

app = [
	Executable(
		script = "service.py",
		base = base,
		icon = pic
	)
]

confirm = raw_input("\n>>> Confirm ? [Y/n] ")
if(confirm in ['Y', 'y']):
	setup(
		name = "service.exe",
		version = "0.0.8-a",
		description = "Outils d'interface d'accès aux Services Web Linux",
		author = "Anarchy",
		options = { "build_exe": options },
		executables = [app[0]]
	)
	
	print(" [ INFO ] - Compilation Finished\n")
else:
	print(" [ INFO ] - Compilation Aborted\n")

"""
	-----
	 END
	-----
"""
