#!/usr/bin/python2
# -*- coding: utf-8 -*-

# (c) 2017 - Copyright by 4N4RCHY. All rights is reserved.

# --------------------------------------
#  Program >>> service.py
#  Function >>> Show & Control Services
#  Version >>> 0.0.2-a
# --------------------------------------

import os, platform, sys
import warnings
from Tkinter import *

class color:
	RED	= '\033[31m'
	GREEN	= '\033[32m'
	YELLOW	= '\033[33m'
	END	= '\033[0m'

def madeButton(panel, act):
	for i, txt in enumerate(["START", "RESTART", "STOP"]):
		Button(panel, text=txt, command=act[i]).pack(side=LEFT, padx=4, pady=4)
		i += 1

def madeLabel(panel, labels):
	for i, txt in enumerate(labels):
		Label(panel, text=txt).pack(pady=1)
		i += 1

def madePanel(panel, panelName, act):
	subpanel = Frame(panel, bd=1, relief=GROOVE)
	subpanel.pack(side=TOP, padx=8, pady=8)
	Label(subpanel, text=panelName).pack(padx=5, pady=2)
	madeButton(subpanel, act)

def apache2Start(): os.system(apacheService+'start'); check()
def apache2Restart(): os.system(apacheService+'restart'); check()
def apache2Stop(): os.system(apacheService+'stop'); check()

def mysqlStart(): os.system(mysqlService+'start'); check()
def mysqlRestart(): os.system(mysqlService+'restart'); check()
def mysqlStop(): os.system(mysqlService+'stop'); check()

def torStart(): os.system(torService+'start'); check()
def torRestart(): os.system(torService+'restart'); check()
def torStop(): os.system(torService+'stop'); check()

def startAll():
	apache2Start();
	mysqlStart();
	if(tor): torStart()

def restartAll():
	apache2Restart()
	mysqlRestart()
	if(tor): torRestart()

def stopAll():
	apache2Stop()
	mysqlStop()
	if(tor): torStop()

def check(): print("> Action:\t\t\t[ " + color.YELLOW + "TERMINATED" + color.END + " ]")

def about():
	print("> " + color.YELLOW + "Show more info_" + color.END)
	aboutus = Tk()
	aboutus.title('Service { ABOUT }')
	aboutus.resizable(width=FALSE, height=FALSE)
	
	content0 = Frame(aboutus, bd=0)
	content0.pack(padx=25, pady=50, side=TOP)
	madeLabel(content0, [
		version,
		"Ce programme a été écrit en python",
		"github.com/Tracks12/CustomServiceCommand"
	])
	Label(aboutus, text="Anarchy").pack(padx=25, pady=10, side=BOTTOM)
	
	aboutus.mainloop()

def help():
	print("> " + color.YELLOW + "Show helper_" + color.END)
	helper = Tk()
	helper.title('Service { HELPER }')
	
	Label(helper, text="Aide aux fonctionnalités").pack(padx=30, pady=20)
	
	article0 = Frame(helper, bd=0)
	article0.pack(padx=50, pady=20)
	madeLabel(article0, [
		"START : Démarre le service concerné",
		"STOP : Arrête le service concerné",
		"RESTART : Redémarre le service concerné"
	])
	
	helper.mainloop()

def program():
	os.system("clear")
	print("> " + color.GREEN + "Runing Service Command GRAPH mod_" + color.END + "\n")
	os.system("screenfetch")
	print("")
	
	global apacheService, mysqlService, torService
	apacheService = "sudo /etc/init.d/apache2 "
	mysqlService = "sudo /etc/init.d/mysql "
	if(tor): torService = "sudo /etc/init.d/tor "
	
	service = Tk()
	service.title('Service { COMMAND PANEL }')
	service.resizable(width=FALSE, height=FALSE)
	
	menubar = Menu(service, bd=0)
	menu0 = Menu(menubar, tearoff=0)
	menu0.add_command(label="Quitter", command=service.quit)
	menubar.add_cascade(label="Fichier", menu=menu0)
	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Aide", command=help)
	menu1.add_command(label="A propos du soft", command=about)
	menubar.add_cascade(label="Plus", menu=menu1)
	
	""" General Control COMMAND """
	madePanel(service, "General Service", [startAll, restartAll, stopAll])
	""" ---------------------------------------------------------------------------------- """
	
	""" Main Panel """
	panel1 = Frame(service, bd=1, relief=GROOVE)
	panel1.pack(side=TOP, padx=8, pady=8)
	
	# Apache2 Service COMMAND
	madePanel(panel1, "Service Apache2", [apache2Start, apache2Restart, apache2Stop])
	
	# MySQL Service COMMAND
	madePanel(panel1, "Service MySQL", [mysqlStart, mysqlRestart, mysqlStop])
	
	#Tor Service COMMAND
	if(tor): madePanel(panel1, "Service Tor", [torStart, torRestart, torStop])
	""" ---------------------------------------------------------------------------------- """
	
	Button(service, text="QUIT", command=service.quit).pack(side=RIGHT, padx=8, pady=8)
	
	service.config(menu=menubar)
	service.mainloop()
	print("> " + color.RED + "Quitting_" + color.END)
	service.destroy()

global version, tor
version = "v_0.0.2-a"
tor = False

if("-h" in sys.argv):
	print("")
elif("-V" in sys.argv): print("Version: " + version + "\n")
else:
	if(platform.system() == "Linux"):
		if("-t" in sys.argv): tor = True
		program()
	else: print(" [ " + color.RED + "ERROR" + color.END + " ] - Operating System wasn't support\n")

# -----
#  END
# -----

