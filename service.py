#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
	----------------------
	 Autor   : Anarchy
	 Date    : 21/01/2019
	 Name    : service.py
	 Version : 0.0.4-a
	----------------------
"""

import os, platform, sys, time
from Tkinter import *

date = ['10 avr 2017', '28 janv 2019']
dev = 'Anarchy'
name = 'service.py'
tor = False
version = "v_0.0.4-a"

class color:
	BOLD	= '\033[1m'
	ITALIC	= '\033[3m'
	
	RED	= '\033[31m'
	GREEN	= '\033[32m'
	YELLOW	= '\033[33m'
	PURPLE	= '\033[35m'
	WHITE	= '\033[37m'
	
	B_GREEN	= '\033[42m'
	
	END	= '\033[0m'

def madeButton(panel, act, r):
	global button
	
	for i, txt in enumerate(['START', 'RESTART', 'CONFIG']):
		button[r][i] = Button(panel, text=txt, font=['Ubuntu', 9], command=act[i], width=8, state=NORMAL)
		button[r][i].grid(row=i, column=0, padx=6, pady=4, sticky=W)

def madeLabel(panel, labels, _font):
	for i, txt in enumerate(labels):
		Label(panel, text=txt, font=_font).grid(pady=1, sticky=W)

def madePanel(panel, panelName, r, act):
	subpanel = LabelFrame(panel, bd=1, relief=GROOVE, text=panelName, font=['Ubuntu Light', 12])
	subpanel.grid(row=1, column=r, padx=8, pady=8)
	madeButton(subpanel, act, r)

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

def serv(s, x):
	global button
	
	if(s == 'apache'): msg = ['Serveur Apache ', 'sudo /etc/init.d/apache2 ', 0]
	elif(s == 'mysql'): msg = ['Base de données MySQL ', 'sudo /etc/init.d/mysql ', 1]
	elif(s == 'tor'): msg = ['Service Tor ', 'sudo /etc/init.d/tor ', 2]
	
	if(x == 1):
		line = ['start', msg[0]+'lancer']
		button[msg[2]][0].config(text='STOP', command=lambda:serv(s, 0))
	
	elif(x == 2): line = ['restart', msg[0]+'relancer']
	
	elif(x == 0):
		line = ['stop', msg[0]+'arrêter']
		button[msg[2]][0].config(text='START', command=lambda:serv(s, 1))
	
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
	info = ["/var/www/html", ""]
	
	print(name + "> " + color.YELLOW + "Listing Project in " + color.END + color.ITALIC + info[0] + color.END + "\n")
	for i, txt in enumerate(os.listdir(info[0])):
		s = ""
		if("." in txt): col = color.PURPLE;
		else: col = color.BOLD + color.GREEN; s = "/"
		
		if(("index.php" == txt) or ("index.html" == txt)): col = color.BOLD + color.PURPLE; s = " <- Index File"
		elif(".htaccess" == txt): col = color.BOLD + color.YELLOW; s = " <- Apache Configuration File"
		
		info[1] += "\t./" + col + txt + color.END + s + "\n"
	
	print(info[1])

def screen():
	print("\n" + color.BOLD + color.YELLOW + "     ____               O  ___        ___")
	print("    | ___|----.---,-.--.-./ __|----. | _ \_ __")
	print("    |___ | -__| .-| |  | | (__| -__| | ,_/\` /")
	print("    |____|____|_| |___/|_|\___|____|.|_|  / /  " + color.RED + version)
	print("             " + color.WHITE + "Take a easier control       " + color.BOLD + color.YELLOW + "/_/\n" + color.END)
	time.sleep(1)

def about():
	print(name + "> " + color.YELLOW + "Show more info_" + color.END)
	aboutus = Tk()
	aboutus.title('A Propos')
	aboutus.resizable(width=FALSE, height=FALSE)
	
	content = Frame(aboutus, bd=0)
	content.grid(row=0, column=0, padx=25, pady=30)
	Label(content, text=name.capitalize(), font=['Ubuntu', 20]).grid(row=0, pady=20, sticky=W)
	madeLabel(content, [
		"Ecrit le : " + date[0],
		"Dernière Mise à Jour : " + date[1],
		"Version : " + version,
		"\nCe programme a été écrit en python2",
		"https://tracks12.github.io/service.py/"
	], ['Ubuntu', 11])
	Label(aboutus, text=dev, font=['Ubuntu', 9]).grid(row=1, pady=5)
	
	aboutus.mainloop()
	aboutus.quit()

def helper():
	print(name + "> " + color.YELLOW + "Show helper_" + color.END)
	helper = Tk()
	helper.title('Aide')
	
	Label(helper, text="Aide aux fonctionnalités", font=['Ubuntu', 20]).grid(row=0, pady=20)
	
	article = [Frame(helper), Frame(helper)]
	
	article[0].grid(row=1, padx=20, pady=10, sticky=W)
	Label(article[0], text="Commande :", font=['Ubuntu', 14]).grid(row=0, pady=10, sticky=W)
	madeLabel(article[0], [
		"START\t : Démarre le service concerné",
		"STOP\t : Arrête le service concerné",
		"RESTART\t : Redémarre le service concerné",
		"CONFIG\t : Modifie le fichier de configuration du service concerné avec l'éditeur de texte local"
	], ['Ubuntu light', 10])
	
	article[1].grid(row=2, padx=20, pady=10, sticky=W)
	Label(article[1], text="Lancement :", font=['Ubuntu', 14]).grid(row=0, pady=10, sticky=W)
	madeLabel(article[1], helpArg, ['Monospace', 9])
	
	helper.mainloop()
	helper.quit()

def main():
	global name, step, tor, version
	
	print(name + "> " + color.GREEN + "Initializing IHM Service Command_" + color.END)
	if(tor): print(name + "> " + color.YELLOW + "Tor mod enabled_" + color.END)
	
	window = Tk()
	window.title(name.capitalize())
	window.resizable(width=FALSE, height=FALSE)
	
	step = StringVar()
	
	""" Menu """
	menubar = Menu(window, bd=0)
	
	menuContent = [
		[ # Menu Principale
			'Fichier', Menu(menubar, tearoff=0),
			['Quitter'],
			[window.quit]
		],
		[ # Menu Apache2
			'Serveur', Menu(menubar, tearoff=0),
			['Démarrer Apache2', 'Redémarrer Apache2', 'Arrêter Apache2', 'Configurer Apache2', 'Voir Access.log', 'Voir Error.log', 'Lister les Projets'],
			[lambda:serv('apache', 1), lambda:serv('apache', 2), lambda:serv('apache', 0), lambda:edit('apache'), lambda:viewLog('apache', 'access.log'), lambda:viewLog('apache', 'error.log'), listProject]
		],
		[ # Menu MySQL
			'Base de Données', Menu(menubar, tearoff=0),
			['Démarrer MySQL', 'Redémarrer MySQL', 'Arrêter MySQL', 'Configurer MySQL'],
			[lambda:serv('mysql', 1), lambda:serv('mysql', 2), lambda:serv('mysql', 0), lambda:edit('mysql')]
		],
		[ # Menu d'Information
			'Plus', Menu(menubar, tearoff=0),
			['Aide', 'A propos du soft'],
			[helper, about]
		]
	]
	
	if(tor):
		menuContent.append([])
		menuContent[len(menuContent)-1] = menuContent[len(menuContent)-2]
		menuContent[len(menuContent)-2] = [ # Menu Tor
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
	
	Label(window, text=name.capitalize(), font=['Ubuntu', 20]).grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky=W)
	
	panel = [
		LabelFrame(window, bd=1, relief=GROOVE, text="General", font=['Ubuntu Light', 12]),
		Frame(window, bd=1, relief=GROOVE)
	]
	
	""" General Control COMMAND """
	# General Service COMMAND
	panel[0].grid(row=1, column=0, padx=8, pady=8)
	Button(panel[0], text='START', font=['Ubuntu', 9], command=lambda:servAll(1), width=8).grid(row=0, column=0, padx=6, pady=4, sticky=W)
	Button(panel[0], text='STOP', font=['Ubuntu', 9], command=lambda:servAll(0), width=8).grid(row=1, column=0, padx=6, pady=4, sticky=W)
	Button(panel[0], text='RESTART', font=['Ubuntu', 9], command=lambda:servAll(2), width=8).grid(row=2, column=0, padx=6, pady=4, sticky=W)
	""" ---------------------------------------------------------------------------------- """
	
	""" Main Panel """
	panel[1].grid(row=1, column=1, padx=8, pady=8)
	
	# Apache2 Service COMMAND
	madePanel(panel[1], "Apache2", 0, [lambda:serv('apache', 1), lambda:serv('apache', 2), lambda:edit('apache')])
	
	# MySQL Service COMMAND
	madePanel(panel[1], "MySQL", 1, [lambda:serv('mysql', 1), lambda:serv('mysql', 2), lambda:edit('mysql')])
	
	#Tor Service COMMAND
	if(tor): madePanel(panel[1], "Tor", 2, [lambda:serv('tor', 1), lambda:serv('tor', 2), lambda:edit('tor')])
	""" ---------------------------------------------------------------------------------- """
	
	Button(window, text="Lister les Projets", font=['Ubuntu', 10], command=listProject).grid(row=2, column=0, padx=8, pady=8)
	Button(window, text="Quitter", font=['Ubuntu', 10], command=window.quit).grid(row=2, column=1, padx=8, pady=8, sticky=E)
	Label(window, textvariable=step, font=['Monospace', 8]).grid(row=3, column=0, columnspan=2, padx=5, sticky=W)
	
	step.set("Prêt")
	
	window.config(menu=menubar)
	window.mainloop()
	window.quit()
	
	print(name + "> " + color.RED + "Quitting_" + color.END)

button = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]

arg = [
	["-h" in sys.argv, "-?" in sys.argv, "--help" in sys.argv],
	["-l" in sys.argv, "--list" in sys.argv],
	["-t" in sys.argv, "--tor" in sys.argv],
	["-v" in sys.argv, "--version" in sys.argv],
	["-a" in sys.argv, "--about" in sys.argv]
]

helpArg = [
	" python2 " + name + "\n",
	" Option         Option longue GNU       Description",
	" -a             --about                 A propos du soft",
	" -h, -?         --help                  Affiche ce message",
	" -l             --list                  Liste tous le repertoire du serveur",
	" -t             --tor                   Lancement en mod Tor",
	" -v             --version               Affiche la version du soft\n"
]

if(True in arg[0]):
	for i, txt in enumerate(helpArg):
		print(txt)

elif(True in arg[1]): listProject()
elif(True in arg[3]): print(" " + version + "\n")
elif(True in arg[4]):
	print(" " + name.capitalize())
	print("\n Writed      : " + date[0])
	print(" Last Update : " + date[1])
	print(" Version     : " + version)
	print("\n This program was writed in python2")
	print(" https://tracks12.github.io/service.py/")
	print("\n " + dev + "\n")

else:
	if(platform.system() == "Linux"):
		print("Running...")
		time.sleep(.5)
		screen()
		if(True in arg[2]): tor = True
		main()
		print("Bye :)\n")
	
	else: print(" [ " + color.RED + "ERROR" + color.END + " ] - Operating System wasn't support\n")

# -----
#  END
# -----
