#!/usr/bin/python2
# -*- coding: utf-8 -*-

# ----------------------
#  Autor   : Anarchy
#  Date    : 21/01/2019
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
		Button(panel, text=txt, font=['Ubuntu', 9], command=act[i], width=8).grid(row=i, column=0, padx=6, pady=4, sticky=W)
		i += 1

def madeLabel(panel, labels):
	for i, txt in enumerate(labels):
		Label(panel, text=txt, font=['Ubuntu', 12]).grid(pady=1, sticky=W)
		i += 1

def madePanel(panel, panelName, r, act):
	subpanel = LabelFrame(panel, bd=1, relief=GROOVE, text=panelName, font=['Ubuntu', 12])
	subpanel.grid(row=1, column=r, padx=8, pady=8)
	madeButton(subpanel, act)

def editApache():
	print(name + "> " + color.YELLOW + "Editing Apache2 Configuration File_" + color.END)
	os.system("nano /etc/apache2/apache2.conf")
	check('Modification de apache2.conf')

def editMysql():
	print(name + "> " + color.YELLOW + "Editing MySQL Configuration File_" + color.END)
	os.system("nano /etc/mysql/my.cnf")
	check('Modification de my.cnf')
	
def editTor():
	print(name + "> " + color.YELLOW + "Editing Tor Configuration File_" + color.END)
	os.system("nano /etc/tor/torsocks.conf")
	check('Modification de torsocks.conf')

def apacheAccess(): os.system("cat /var/log/apache2/access.log")
def apacheError(): os.system("cat /var/log/apache2/error.log")

def torLog(): os.system("cat /var/log/tor/log")

def apacheStart(): os.system(service[0]+'start'); check('Serveur Apache lancer')
def apacheRestart(): os.system(service[0]+'restart'); check('Serveur Apache relancer')
def apacheStop(): os.system(service[0]+'stop'); check('Serveur Apache arrêter')

def mysqlStart(): os.system(service[1]+'start'); check('Base de données MySQL lancer')
def mysqlRestart(): os.system(service[1]+'restart'); check('Base de données MySQL relancer')
def mysqlStop(): os.system(service[1]+'stop'); check('Base de données MySQL arrêter')

def torStart(): os.system(service[2]+'start'); check('Service Tor lancer')
def torRestart(): os.system(service[2]+'restart'); check('Service Tor relancer')
def torStop(): os.system(service[2]+'stop'); check('Service Tor arrêter')

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

def check(act):
	global step
	step.set(act)
	print(name + "> Action:\t\t\t\t[" + color.B_GREEN + " TERMINATED " + color.END + "]")

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
	aboutus.title('A Propos')
	aboutus.resizable(width=FALSE, height=FALSE)
	
	content0 = Frame(aboutus, bd=0)
	content0.grid(row=0, column=0, padx=25, pady=30)
	Label(content0, text=name, font=['Ubuntu', 24]).grid(row=0, column=0, padx=0, pady=20, sticky=W)
	madeLabel(content0, [
		"Dernière Mise à Jour : " + date[1],
		"Version : " + version,
		"Ce programme a été écrit en python2",
		"github.com/Tracks12/CustomServiceCommand"
	])
	Label(aboutus, text="Anarchy", font=['Ubuntu', 10]).grid(row=1, column=0)
	
	aboutus.mainloop()

def helper():
	print(name + "> " + color.YELLOW + "Show helper_" + color.END)
	helper = Tk()
	helper.title('Aide')
	
	Label(helper, text="Aide aux fonctionnalités", font=['Ubuntu', 12]).pack(padx=30, pady=20)
	
	article0 = Frame(helper, bd=0)
	article0.pack(padx=50, pady=20)
	madeLabel(article0, [
		"START : Démarre le service concerné",
		"STOP : Arrête le service concerné",
		"RESTART : Redémarre le service concerné"
	])
	
	helper.mainloop()

def program():
	global name, service, step, tor, version
	
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
	window.title('Service ' + version)
	window.resizable(width=FALSE, height=FALSE)
	
	step = StringVar()
	
	""" Menu """
	menubar = Menu(window, bd=0)
	
	menu0 = Menu(menubar, tearoff=0)
	menu0.add_command(label="Quitter", font=['Ubuntu', 10], command=window.quit)
	menubar.add_cascade(label="Fichier", font=['Ubuntu', 10], menu=menu0)
	
	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Démarrer Apache2", font=['Ubuntu', 10], command=apacheStart)
	menu1.add_command(label="Redémarrer Apache2", font=['Ubuntu', 10], command=apacheRestart)
	menu1.add_command(label="Arrêter Apache2", font=['Ubuntu', 10], command=apacheStop)
	menu1.add_separator()
	menu1.add_command(label="Configurer Apache2", font=['Ubuntu', 10], command=editApache)
	menu1.add_separator()
	menu1.add_command(label="Voir Access.log", font=['Ubuntu', 10], command=apacheAccess)
	menu1.add_command(label="Voir Error.log", font=['Ubuntu', 10], command=apacheError)
	menu1.add_separator()
	menu1.add_command(label="Lister les Projets", font=['Ubuntu', 10], command=listProject)
	menubar.add_cascade(label="Serveur", font=['Ubuntu', 10], menu=menu1)
	
	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="Démarrer MySQL", font=['Ubuntu', 10], command=mysqlStart)
	menu2.add_command(label="Redémarrer MySQL", font=['Ubuntu', 10], command=mysqlRestart)
	menu2.add_command(label="Arrêter MySQL", font=['Ubuntu', 10], command=mysqlStop)
	menu2.add_separator()
	menu2.add_command(label="Configurer MySQL", font=['Ubuntu', 10], command=editMysql)
	menubar.add_cascade(label="Base de Données", font=['Ubuntu', 10], menu=menu2)
	
	if(tor):
		menu3 = Menu(menubar, tearoff=0)
		menu3.add_command(label="Démarrer Tor", font=['Ubuntu', 10], command=torStart)
		menu3.add_command(label="Configurer Tor", font=['Ubuntu', 10], command=editTor)
		menu3.add_separator()
		menu3.add_command(label="Voir Tor.log", font=['Ubuntu', 10], command=torLog)
		menubar.add_cascade(label="Tor", font=['Ubuntu', 10], menu=menu3)
	
	menu4 = Menu(menubar, tearoff=0)
	menu4.add_command(label="Aide", font=['Ubuntu', 10], command=helper)
	menu4.add_command(label="A propos du soft", font=['Ubuntu', 10], command=about)
	menubar.add_cascade(label="Plus", font=['Ubuntu', 10], menu=menu4)
	""" ---------------------------------------------------------------------------------- """
	
	Label(window, text=name, font=['Ubuntu', 20]).grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky=W)
	
	""" General Control COMMAND """
	madePanel(window, "General", 0, [startAll, stopAll, restartAll])
	""" ---------------------------------------------------------------------------------- """
	
	""" Main Panel """
	panel1 = Frame(window, bd=1, relief=GROOVE)
	panel1.grid(row=1, column=1, padx=8, pady=8)
	
	# Apache2 Service COMMAND
	madePanel(panel1, "Apache2", 0, [apacheStart, apacheStop, apacheRestart])
	
	# MySQL Service COMMAND
	madePanel(panel1, "MySQL", 1, [mysqlStart, mysqlStop, mysqlRestart])
	
	#Tor Service COMMAND
	if(tor): madePanel(panel1, "Tor", 2, [torStart, torStop, torRestart])
	""" ---------------------------------------------------------------------------------- """
	
	Button(window, text="Lister les Projets", font=['Ubuntu', 10], command=listProject).grid(row=2, column=0, padx=8, pady=8)
	Button(window, text="Quitter", font=['Ubuntu', 10], command=window.quit).grid(row=2, column=1, padx=8, pady=8, sticky=E)
	Label(window, textvariable=step, font=['Monospace', 8]).grid(row=3, column=0, columnspan=2, padx=4, sticky=W)
	
	step.set("Prêt")
	
	window.config(menu=menubar)
	window.mainloop()
	window.quit()
	
	print(name + "> " + color.RED + "Quitting_" + color.END)

date = ['10 avr 2017', '20 janv 2019']
name = 'Service.py'
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
