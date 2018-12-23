#!/usr/bin/python2
# -*- coding: utf-8 -*-

# (c) 2017 - Copyright by 4N4RCHY. All rights is reserved.

# --------------------------------------
#  Program >>> service.py
#  Function >>> Show & Control Services
#  Version >>> 0.0.2-a
# --------------------------------------

import os, platform, sys, warnings
from Tkinter import *

class color:
	BOLD	= '\033[1m'
	ITALIC	= '\033[3m'
	
	RED	= '\033[31m'
	GREEN	= '\033[32m'
	YELLOW	= '\033[33m'
	PURPLE	= '\033[35m'
	
	B_GREEN	= '\033[42m'
	
	END	= '\033[0m'

def madeButton(panel, act):
	for i, txt in enumerate(["START", "STOP", "RESTART"]):
		Button(panel, text=txt, command=act[i]).pack(side=LEFT, padx=6, pady=4)
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

def editApache():
	print("> " + color.YELLOW + "Editing Apache2 Configuration File_" + color.END)
	os.system("nano /etc/apache2/apache2.conf")
	check()

def editMysql():
	print("> " + color.YELLOW + "Editing MySQL Configuration File_" + color.END)
	os.system("nano /etc/mysql/my.cnf")
	check()
	
def editTor():
	print("> " + color.YELLOW + "Editing Tor Configuration File_" + color.END)
	os.system("nano /etc/tor/torsocks.conf")
	check()

def apacheAccess(): os.system("cat /var/log/apache2/access.log")
def apacheError(): os.system("cat /var/log/apache2/error.log")

def torLog(): os.system("cat /var/log/tor/log")

def apacheStart(): os.system(apacheService+'start'); check()
def apacheRestart(): os.system(apacheService+'restart'); check()
def apacheStop(): os.system(apacheService+'stop'); check()

def mysqlStart(): os.system(mysqlService+'start'); check()
def mysqlRestart(): os.system(mysqlService+'restart'); check()
def mysqlStop(): os.system(mysqlService+'stop'); check()

def torStart(): os.system(torService+'start'); check()
def torRestart(): os.system(torService+'restart'); check()
def torStop(): os.system(torService+'stop'); check()

def startAll():
	apacheStart();
	mysqlStart();
	if(tor): torStart()

def restartAll():
	apacheRestart()
	mysqlRestart()
	if(tor): torRestart()

def stopAll():
	apacheStop()
	mysqlStop()
	if(tor): torStop()

def check(): print("> Action:\t\t\t\t[" + color.B_GREEN + " TERMINATED " + color.END + "]")

def listProject():
	racine = "/var/www/html"; output = ""
	
	print("> Listing Project in " + color.ITALIC + racine + color.END + "\n")
	for i, txt in enumerate(os.listdir(racine)):
		s = ""
		if("." in txt): col = color.PURPLE;
		else: col = color.BOLD + color.GREEN; s = "/"
		
		if(("index.php" == txt) or ("index.html" == txt)): col = color.BOLD + color.PURPLE; s = " <- Index File"
		elif(".htaccess" == txt): col = color.BOLD + color.YELLOW; s = " <- Apache Configuration File"
		
		output += "\t./" + col + txt + color.END + s + "\n"
	
	print(output)

def about():
	print("> " + color.YELLOW + "Show more info_" + color.END)
	aboutus = Tk()
	aboutus.title('Service { ABOUT }')
	aboutus.resizable(width=FALSE, height=FALSE)
	
	content0 = Frame(aboutus, bd=0)
	content0.pack(padx=25, pady=50, side=TOP)
	madeLabel(content0, [
		version,
		"Ce programme a été écrit en python2",
		"github.com/Tracks12/CustomServiceCommand"
	])
	Label(aboutus, text="Anarchy").pack(padx=25, pady=10, side=BOTTOM)
	
	aboutus.mainloop()

def helper():
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
	print("> " + color.GREEN + "Runing Service Command GRAPH mod_" + color.END)
	if(tor): print("> " + color.YELLOW + "Tor mod enabled_" + color.END)
	print("")
	os.system("screenfetch")
	print("")
	
	global apacheService, mysqlService, torService
	apacheService = "sudo /etc/init.d/apache2 "
	mysqlService = "sudo /etc/init.d/mysql "
	if(tor): torService = "sudo /etc/init.d/tor "
	
	service = Tk()
	service.title('Service { COMMAND PANEL }')
	service.resizable(width=FALSE, height=FALSE)
	
	""" Menu """
	menubar = Menu(service, bd=0)
	
	menu0 = Menu(menubar, tearoff=0)
	menu0.add_command(label="Quitter", command=service.quit)
	menubar.add_cascade(label="Fichier", menu=menu0)
	
	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Démarrer Apache2", command=apacheStart)
	menu1.add_command(label="Démarrer MySQL", command=mysqlStart)
	menu1.add_separator()
	menu1.add_command(label="Configurer Apache2", command=editApache)
	menu1.add_command(label="Configurer MySQL", command=editMysql)
	menu1.add_separator()
	menu1.add_command(label="Voir Access.log", command=apacheAccess)
	menu1.add_command(label="Voir Error.log", command=apacheError)
	menu1.add_separator()
	menu1.add_command(label="Lister les Projets", command=listProject)
	menubar.add_cascade(label="Serveur", menu=menu1)
	
	if(tor):
		menu2 = Menu(menubar, tearoff=0)
		menu2.add_command(label="Démarrer Tor", command=torStart)
		menu2.add_separator()
		menu2.add_command(label="Configurer Tor", command=editTor)
		menu2.add_separator()
		menu2.add_command(label="Voir Tor.log", command=torLog)
		menubar.add_cascade(label="Tor", menu=menu2)
	
	menu3 = Menu(menubar, tearoff=0)
	menu3.add_command(label="Aide", command=helper)
	menu3.add_command(label="A propos du soft", command=about)
	menubar.add_cascade(label="Plus", menu=menu3)
	""" ---------------------------------------------------------------------------------- """
	
	""" General Control COMMAND """
	madePanel(service, "General Service", [startAll, stopAll, restartAll])
	""" ---------------------------------------------------------------------------------- """
	
	""" Main Panel """
	panel1 = Frame(service, bd=1, relief=GROOVE)
	panel1.pack(side=TOP, padx=8, pady=8)
	
	# Apache2 Service COMMAND
	madePanel(panel1, "Service Apache2", [apacheStart, apacheStop, apacheRestart])
	
	# MySQL Service COMMAND
	madePanel(panel1, "Service MySQL", [mysqlStart, mysqlStop, mysqlRestart])
	
	#Tor Service COMMAND
	if(tor): madePanel(panel1, "Service Tor", [torStart, torStop, torRestart])
	""" ---------------------------------------------------------------------------------- """
	
	Button(service, text="Lister les Projets", command=listProject).pack(side=LEFT, padx=8, pady=8)
	Button(service, text="QUIT", command=service.quit).pack(side=RIGHT, padx=8, pady=8)
	
	service.config(menu=menubar)
	service.mainloop()
	print("> " + color.RED + "Quitting_" + color.END)
	service.destroy()

global version, tor
version = "v_0.0.2-a"
tor = False

arg = [
	["-h" in sys.argv, "-?" in sys.argv, "--help" in sys.argv],
	["-v" in sys.argv, "--version" in sys.argv],
	["-t" in sys.argv, "--tor" in sys.argv]
]

if(True in arg[0]):
	print(" python2 service.py\n")
	print(" Option         Option longue GNU       Description")
	print(" -h, -?         --help                  Affiche ce message")
	print(" -v             --version               Affiche la version du soft")
	print(" -t             --tor                   Lancement en mod Tor")

elif(True in arg[1]):
	print(" Version: " + version + "\n")

else:
	if(platform.system() == "Linux"):
		if(True in arg[2]): tor = True
		program()
	else: print(" [ " + color.RED + "ERROR" + color.END + " ] - Operating System wasn't support\n")

# -----
#  END
# -----
