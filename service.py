#!/usr/bin/python2
# -*- coding: utf-8 -*-

# ----------------------
#  Autor   : Anarchy
#  Date    : 20/01/2019
#  Name    : service.py
#  Version : 0.0.3-a
# ----------------------

import os, platform, sys
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
		Button(panel, text=txt, command=act[i]).grid(row=i, column=1, padx=6, pady=4, sticky=W)
		i += 1

def madeLabel(panel, labels):
	for i, txt in enumerate(labels):
		Label(panel, text=txt).grid(pady=1)
		i += 1

def madePanel(panel, panelName, r, act):
	subpanel = Frame(panel, bd=1, relief=GROOVE)
	subpanel.grid(row=r, column=0, padx=8, pady=8)
	Label(subpanel, text=panelName).grid(row=0, column=0, padx=5, pady=2)
	madeButton(subpanel, act)

def editApache():
	print(name + "> " + color.YELLOW + "Editing Apache2 Configuration File_" + color.END)
	os.system("nano /etc/apache2/apache2.conf")
	check()

def editMysql():
	print(name + "> " + color.YELLOW + "Editing MySQL Configuration File_" + color.END)
	os.system("nano /etc/mysql/my.cnf")
	check()
	
def editTor():
	print(name + "> " + color.YELLOW + "Editing Tor Configuration File_" + color.END)
	os.system("nano /etc/tor/torsocks.conf")
	check()

def apacheAccess(): os.system("cat /var/log/apache2/access.log")
def apacheError(): os.system("cat /var/log/apache2/error.log")

def torLog(): os.system("cat /var/log/tor/log")

def apacheStart(): os.system(service[0]+'start'); check()
def apacheRestart(): os.system(service[0]+'restart'); check()
def apacheStop(): os.system(service[0]+'stop'); check()

def mysqlStart(): os.system(service[1]+'start'); check()
def mysqlRestart(): os.system(service[1]+'restart'); check()
def mysqlStop(): os.system(service[1]+'stop'); check()

def torStart(): os.system(service[2]+'start'); check()
def torRestart(): os.system(service[2]+'restart'); check()
def torStop(): os.system(service[2]+'stop'); check()

def startAll():
	apacheStart()
	mysqlStart()
	if(tor): torStart()

def restartAll():
	apacheRestart()
	mysqlRestart()
	if(tor): torRestart()

def stopAll():
	apacheStop()
	mysqlStop()
	if(tor): torStop()

def check(): print(name + "> Action:\t\t\t\t[" + color.B_GREEN + " TERMINATED " + color.END + "]")

def listProject():
	racine = "/var/www/html"; output = ""
	
	print(name + "> " + color.YELLOW + "Listing Project in " + color.END + color.ITALIC + racine + color.END + "\n")
	for i, txt in enumerate(os.listdir(racine)):
		s = ""
		if("." in txt): col = color.PURPLE;
		else: col = color.BOLD + color.GREEN; s = "/"
		
		if(("index.php" == txt) or ("index.html" == txt)): col = color.BOLD + color.PURPLE; s = " <- Index File"
		elif(".htaccess" == txt): col = color.BOLD + color.YELLOW; s = " <- Apache Configuration File"
		
		output += "\t./" + col + txt + color.END + s + "\n"
	
	print(output)

def about():
	print(name + "> " + color.YELLOW + "Show more info_" + color.END)
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
	print(name + "> " + color.YELLOW + "Show helper_" + color.END)
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
	global name, service, tor, version
	
	os.system("clear")
	print(name + "> " + color.GREEN + "Runing Service Command GRAPH mod_" + color.END)
	if(tor): print(name + "> " + color.YELLOW + "Tor mod enabled_" + color.END)
	print("")
	os.system("screenfetch")
	print("")
	
	service = [
		"sudo /etc/init.d/apache2 ",
		"sudo /etc/init.d/mysql ",
		"sudo /etc/init.d/tor "
	]
	
	window = Tk()
	window.title('Service { COMMAND PANEL }')
	window.resizable(width=FALSE, height=FALSE)
	
	""" Menu """
	menubar = Menu(window, bd=0)
	
	menu0 = Menu(menubar, tearoff=0)
	menu0.add_command(label="Quitter", command=window.quit)
	menubar.add_cascade(label="Fichier", menu=menu0)
	
	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Démarrer Apache2", command=apacheStart)
	menu1.add_command(label="Redémarrer Apache2", command=apacheRestart)
	menu1.add_command(label="Arrêter Apache2", command=apacheStop)
	menu1.add_separator()
	menu1.add_command(label="Configurer Apache2", command=editApache)
	menu1.add_separator()
	menu1.add_command(label="Voir Access.log", command=apacheAccess)
	menu1.add_command(label="Voir Error.log", command=apacheError)
	menu1.add_separator()
	menu1.add_command(label="Lister les Projets", command=listProject)
	menubar.add_cascade(label="Serveur", menu=menu1)
	
	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="Démarrer MySQL", command=mysqlStart)
	menu2.add_command(label="Redémarrer MySQL", command=mysqlRestart)
	menu2.add_command(label="Arrêter MySQL", command=mysqlStop)
	menu2.add_separator()
	menu2.add_command(label="Configurer MySQL", command=editMysql)
	menubar.add_cascade(label="Base de Données", menu=menu2)
	
	if(tor):
		menu3 = Menu(menubar, tearoff=0)
		menu3.add_command(label="Démarrer Tor", command=torStart)
		menu3.add_command(label="Configurer Tor", command=editTor)
		menu3.add_separator()
		menu3.add_command(label="Voir Tor.log", command=torLog)
		menubar.add_cascade(label="Tor", menu=menu3)
	
	menu4 = Menu(menubar, tearoff=0)
	menu4.add_command(label="Aide", command=helper)
	menu4.add_command(label="A propos du soft", command=about)
	menubar.add_cascade(label="Plus", menu=menu4)
	""" ---------------------------------------------------------------------------------- """
	
	""" General Control COMMAND """
	madePanel(window, "General Service", 0, [startAll, stopAll, restartAll])
	""" ---------------------------------------------------------------------------------- """
	
	""" Main Panel """
	panel1 = Frame(window, bd=1, relief=GROOVE)
	panel1.grid(row=0, column=1, padx=8, pady=8)
	
	# Apache2 Service COMMAND
	madePanel(panel1, "Service Apache2", 0, [apacheStart, apacheStop, apacheRestart])
	
	# MySQL Service COMMAND
	madePanel(panel1, "Service MySQL", 1, [mysqlStart, mysqlStop, mysqlRestart])
	
	#Tor Service COMMAND
	if(tor): madePanel(panel1, "Service Tor", 2, [torStart, torStop, torRestart])
	""" ---------------------------------------------------------------------------------- """
	
	Button(window, text="Lister les Projets", command=listProject).grid(row=1, column=0, padx=8, pady=8)
	Button(window, text="QUIT", command=window.quit).grid(row=1, column=1, padx=8, pady=8, sticky=E)
	
	window.config(menu=menubar)
	window.mainloop()
	window.destroy()
	
	print(name + "> " + color.RED + "Quitting_" + color.END)

name = 'Service'
tor = False
version = "v_0.0.3-a"

arg = [
	["-h" in sys.argv, "-?" in sys.argv, "--help" in sys.argv],
	["-l" in sys.argv, "--list" in sys.argv],
	["-t" in sys.argv, "--tor" in sys.argv],
	["-v" in sys.argv, "--version" in sys.argv]
]

if(True in arg[0]):
	print(" python2 service.py\n")
	print(" Option         Option longue GNU       Description")
	print(" -h, -?         --help                  Affiche ce message")
	print(" -l             --list                  Liste tous le repertoire du serveur")
	print(" -t             --tor                   Lancement en mod Tor")
	print(" -v             --version               Affiche la version du soft\n")

elif(True in arg[1]): listProject()
elif(True in arg[3]): print(" Version: " + version + "\n")

else:
	if(platform.system() == "Linux"):
		if(True in arg[2]): tor = True
		program()
	else: print(" [ " + color.RED + "ERROR" + color.END + " ] - Operating System wasn't support\n")

# -----
#  END
# -----
