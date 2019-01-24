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
		Label(panel, text=txt, font=['Ubuntu', 11]).grid(pady=1, sticky=W)
		i += 1

def madePanel(panel, panelName, r, act):
	subpanel = LabelFrame(panel, bd=1, relief=GROOVE, text=panelName, font=['Ubuntu Light', 12])
	subpanel.grid(row=1, column=r, padx=8, pady=8)
	madeButton(subpanel, act)

def edit(serv):
	if(serv == 'apache'): msg = ['Apache2', 'apache2/apache2.conf']
	elif(serv == 'mysql'): msg = ['MySQL', 'mysql/my.cnf']
	elif(serv == 'tor'): msg = ['Tor', 'tor/torsocks.conf']
	
	print(name + "> " + color.YELLOW + "Editing " + msg[0] + " Configuration File_" + color.END)
	os.system("nano /etc/" + msg[1])
	check('Modification de ' + msg[1])

def viewLog(serv, log):
	if(serv == 'apache'): path = 'apache2/'
	elif(serv == 'tor'): path = 'tor/'
	
	os.system("cat /var/log/" + path + log)

def serv(serv, x):
	if(serv == 'apache'): msg = ['Serveur Apache ', 'sudo /etc/init.d/apache2 ']
	elif(serv == 'mysql'): msg = ['Base de données MySQL ', 'sudo /etc/init.d/mysql ']
	elif(serv == 'tor'): msg = ['Service Tor ', 'sudo /etc/init.d/tor ']
	
	if(x == 1): line = ['start', msg[0]+'lancer']
	elif(x == 2): line = ['restart', msg[0]+'relancer']
	elif(x == 0): line = ['stop', msg[0]+'arrêter']
	
	os.system(msg[1]+line[0])
	check(line[1])

def servAll(x):
	serv('apache', x)
	serv('mysql', x)
	if(tor): serv('tor', x)

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
	Label(content0, text=name, font=['Ubuntu', 20]).grid(row=0, pady=20, sticky=W)
	madeLabel(content0, [
		"Dernière Mise à Jour : " + date[1],
		"Version : " + version,
		"Ce programme a été écrit en python2",
		"github.com/Tracks12/CustomServiceCommand"
	])
	Label(aboutus, text="Anarchy", font=['Ubuntu', 10]).grid(row=1)
	
	aboutus.mainloop()
	aboutus.quit()

def helper():
	print(name + "> " + color.YELLOW + "Show helper_" + color.END)
	helper = Tk()
	helper.title('Aide')
	
	Label(helper, text="Aide aux fonctionnalités", font=['Ubuntu', 12]).pack(padx=30, pady=20)
	
	article0 = Frame(helper)
	article0.pack(padx=30, pady=10)
	madeLabel(article0, [
		"START : Démarre le service concerné",
		"STOP : Arrête le service concerné",
		"RESTART : Redémarre le service concerné\n"
	])
	
	helper.mainloop()
	helper.quit()

def program():
	global name, step, tor, version
	
	os.system("clear")
	print(name + "> " + color.GREEN + "Runing Service Command GRAPH mod_" + color.END)
	if(tor): print(name + "> " + color.YELLOW + "Tor mod enabled_" + color.END)
	print("")
	os.system("screenfetch")
	print("")
	
	window = Tk()
	window.title('Service ' + version)
	window.resizable(width=FALSE, height=FALSE)
	
	step = StringVar()
	
	""" Menu """
	menubar = Menu(window, bd=0)
	
	menuContent = [
		[
			'Fichier', Menu(menubar, tearoff=0),
			['Quitter'],
			[window.quit]
		],
		[
			'Serveur', Menu(menubar, tearoff=0),
			['Démarrer Apache2', 'Redémarrer Apache2', 'Arrêter Apache2', 'Configurer Apache2', 'Voir Access.log', 'Voir Error.log', 'Lister les Projets'],
			[lambda:serv('apache', 1), lambda:serv('apache', 2), lambda:serv('apache', 0), lambda:edit('apache'), lambda:viewLog('apache', 'access.log'), lambda:viewLog('apache', 'error.log'), listProject]
		],
		[
			'Base de Données', Menu(menubar, tearoff=0),
			['Démarrer MySQL', 'Redémarrer MySQL', 'Arrêter MySQL', 'Configurer MySQL'],
			[lambda:serv('mysql', 1), lambda:serv('mysql', 2), lambda:serv('mysql', 0), lambda:edit('mysql')]
		],
		[
			'Plus', Menu(menubar, tearoff=0),
			['Aide', 'A propos du soft'],
			[helper, about]
		]
	]
	
	if(tor):
		menuContent.append([])
		menuContent[len(menuContent)-1] = menuContent[len(menuContent)-2]
		menuContent[len(menuContent)-2] = [
			'Tor', Menu(menubar, tearoff=0),
			['Démarrer Tor', 'Redémarrer Tor', 'Arrêter Tor', 'Configurer Tor', 'Voir Tor.log'],
			[lambda:serv('tor', 1), lambda:serv('tor', 2), lambda:serv('tor', 0), lambda:edit('tor'), lambda:viewLog('tor', 'log')]
		]
	
	for i in range(0, len(menuContent)):
		for j, txt in enumerate(menuContent[i][2]):
			menuContent[i][1].add_command(label=txt, font=['Ubuntu Light', 10], command=menuContent[i][3][j])
			if(True in [(i == 1) and (j in [2, 3, 5]), (i == 2) and (j == 2), tor and (i == 3) and (j in [2, 3])]):
				menuContent[i][1].add_separator()
		
		menubar.add_cascade(label=menuContent[i][0], font=['Ubuntu Light', 10], menu=menuContent[i][1])
	""" ---------------------------------------------------------------------------------- """
	
	Label(window, text=name, font=['Ubuntu', 20]).grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky=W)
	
	""" General Control COMMAND """
	madePanel(window, "General", 0, [lambda:servAll(1), lambda:servAll(0), lambda:servAll(2)])
	""" ---------------------------------------------------------------------------------- """
	
	""" Main Panel """
	panel0 = Frame(window, bd=1, relief=GROOVE)
	panel0.grid(row=1, column=1, padx=8, pady=8)
	
	# Apache2 Service COMMAND
	madePanel(panel0, "Apache2", 0, [lambda:serv('apache', 1), lambda:serv('apache', 0), lambda:serv('apache', 2)])
	
	# MySQL Service COMMAND
	madePanel(panel0, "MySQL", 1, [lambda:serv('mysql', 1), lambda:serv('mysql', 0), lambda:serv('mysql', 2)])
	
	#Tor Service COMMAND
	if(tor): madePanel(panel0, "Tor", 2, [lambda:serv('tor', 1), lambda:serv('tor', 0), lambda:serv('tor', 2)])
	""" ---------------------------------------------------------------------------------- """
	
	Button(window, text="Lister les Projets", font=['Ubuntu', 10], command=listProject).grid(row=2, column=0, padx=8, pady=8)
	Button(window, text="Quitter", font=['Ubuntu', 10], command=window.quit).grid(row=2, column=1, padx=8, pady=8, sticky=E)
	Label(window, textvariable=step, font=['Monospace', 8]).grid(row=3, column=0, columnspan=2, padx=5, sticky=W)
	
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
