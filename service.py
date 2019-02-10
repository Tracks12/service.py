#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	----------------------
	 Autor   : Anarchy
	 Date    : 10/02/2019
	 Name    : service.py
	 Version : 0.0.7-a
	----------------------
"""

import os, platform, sys, time
try: from Tkinter import *
except: from tkinter import *

python = "Python {}.{}.{}".format(sys.version_info[0], sys.version_info[1], sys.version_info[2])
button, label, date = [], [], ['10 avr 2017', '10 fev 2019']
dev, name, prog, tor, version = 'Anarchy', 'service.py', "python", False, "v_0.0.7-a"

class color:
	BOLD	= '\033[1m'
	ITALIC	= '\033[3m'
	
	RED	= '\033[31m'
	GREEN	= '\033[32m'
	BLUE	= '\033[34m'
	YELLOW	= '\033[33m'
	PURPLE	= '\033[35m'
	WHITE	= '\033[37m'
	
	END	= '\033[0m'

def madeButton(panel, act, r):
	global button, label
	button.append([])
	
	for i, txt in enumerate(['START', 'RESTART', 'CONFIG']):
		button[r].append(Button(panel, text=txt, font=['Ubuntu', 9], command=act[i], width=8, state=NORMAL))
		button[r][i].grid(row=i+1, column=0, padx=6, pady=4, sticky=W)

def madeLabel(panel, labels, _font):
	for i, txt in enumerate(labels):
		Label(panel, text=txt, font=_font).grid(row=i+1, column=0, pady=1, sticky=W)

def madePanel(panel, panelName, r, act):
	subpanel = LabelFrame(panel, bd=1, relief=GROOVE, text=panelName, font=['Ubuntu Light', 12])
	subpanel.grid(row=1, column=r, padx=8, pady=8)
	
	label.append(Label(subpanel, text='ARRÊTER', font=["Ubuntu", 10], bg="#AA0000", fg="#000000", height=2, width=10))
	label[r].grid(row=0, column=0, padx=6, pady=4)
	madeButton(subpanel, act, r)

def serv(s, x):
	global button, label
	
	if(s == 'apache'): msg = ['Serveur Apache', 'apache2', 0]
	elif(s == 'mysql'): msg = ['Base de données MySQL', 'mysql', 1]
	elif(s == 'tor'): msg = ['Service Tor', 'tor', 2]
	
	if(x == 1):
		line = ['start', '{} lancer'.format(msg[0])]
		label[msg[2]].config(text='LANCER', bg="#00AA00")
		button[msg[2]][0].config(text='STOP', command=lambda:serv(s, 0))
	
	elif(x == 2):
		line = ['restart', '{} relancer'.format(msg[0])]
		label[msg[2]].config(text='LANCER', bg="#00AA00")
	elif(x == 0):
		line = ['stop', '{} arrêter'.format(msg[0])]
		label[msg[2]].config(text='ARRÊTER', bg="#AA0000")
		button[msg[2]][0].config(text='START', command=lambda:serv(s, 1))
	
	os.system("/etc/init.d/{} {}".format(msg[1], line[0]))
	check(line[1])

def servAll(x):
	serv('apache', x)
	serv('mysql', x)
	if(tor): serv('tor', x)

def check(act):
	global step
	step.set(act)
	print(" [ {}FINISHED{} ]".format(color.BOLD+color.GREEN, color.END))

def verify():
	checked, DIR, services, stop = [], os.listdir('/etc/init.d/'), ['apache2', 'mysql'], False
	if(tor): services.append('tor')
	
	time.sleep(.5)
	print("{}> {}Checking installed services{}_".format(name, color.YELLOW, color.END))
	for txt in services:
		if(txt in DIR): checked.append([txt, True])
		elif(not txt in DIR): checked.append([txt, False])
	
	for i, txt in enumerate(checked):
		time.sleep(.1)
		if(False in checked[i]):
			stop = True
			print(" [ {}NOT FOUND{} ] - {}".format(color.RED, color.END, checked[i][0]))
	
	if(stop): return False
	else: print(" [ {}OK{} ] - No missing services\n".format(color.GREEN, color.END))
	return True

def splash():
	time.sleep(.5)
	screen = [
		"\n{}     ____               O             ___".format(color.BOLD+color.YELLOW),
		"    | ___|----.---,-.--.-.----.----. | _ \_ __",
		"    |___ | -__| .-| |  | |  __| -__| | ,_/\` /",
		"    |____|____|_| |___/|_|____|____|.|_|  / /\t{}".format(color.RED+version),
		"             {}Take a easier control       {}/_/\t{}By {}\n".format(color.BOLD+color.WHITE, color.BOLD+color.YELLOW, color.PURPLE, dev+color.END)
	]
	
	for txt in screen:
		print(txt)
		time.sleep(.1)

def listProject():
	def sort(content):
		for j, raw in enumerate(content):
			stick = W
			if(not j): stick = ""
			Label(panel[0], text=raw, font=["monospace", 9]).grid(row=i, column=j, padx=5, sticky=stick)
	
	global step
	info = [
		"/var/www/html",
		['o', 'ko', 'Mo', 'Go', 'To']
	]
	
	print("{}> {}Listing Project in{} {}_".format(name, color.YELLOW, color.END, color.ITALIC+info[0]+color.END))
	try: step.set("Analyse du répertoire de projets {}".format(info[0]))
	except: """ """
	
	dirProject = Tk()
	dirProject.title("Liste des Projets")
	dirProject.resizable(height=False, width=False)
	
	Label(dirProject, text="{}/".format(info[0]), font=["Ubuntu", 18]).grid(row=0, padx=15, pady=10, sticky=W)
	
	panel = [Frame(dirProject)]
	panel[0].grid(row=1, column=0, pady=10)
	
	for i, txt in enumerate(['*', 'Name', 'Size', 'Type', 'Dernière MàJ']):
		Label(panel[0], text=txt, font=["Ubuntu", 10]).grid(row=0, column=i, padx=15)
	
	for i, txt in enumerate(os.listdir(info[0])):
		path = "{}/{}".format(info[0], txt)
		i += 1
		
		try:
			with open(path, "r") as content:
				ba = [0, len(content.read()), ""]
				content.close()
				
				while(ba[1] > 1000): ba = [ba[0] + 1, ba[1] / 1000.0, ""]
				if(txt in ['.htaccess', 'index.php', 'index.html']): ba[2] = "*"
				
				sort([ba[2], txt, "{} {}".format(ba[1], info[1][ba[0]]), ".{}".format(txt.split('.')[1]), time.ctime(os.path.getctime(path))])
		except:
			ba = len(os.listdir(path))
			sort(["", "{}/".format(txt), "{} elements".format(ba), "folder", time.ctime(os.path.getctime(path))])
	
	scroll = Scrollbar(panel[0])
	scroll.grid(row=1, column=5, rowspan=i, sticky=NS)
	
	Label(dirProject, text="{} Elements Trouvés".format(i), font=["Ubuntu Light", 9]).grid(row=2, column=0, padx=5, pady=2, sticky=E)
	print(" [ {}INFO{} ] - {} Elements found !\n".format(color.BLUE, color.END, i))
	
	dirProject.mainloop()
	dirProject.quit()

def edit(serv):	
	def save():
		conf = open("/etc/{}".format(msg[1]), "w")
		conf.write(area.get("1.0", END))
		conf.close()
		
		check('Modification de {}'.format(msg[1]))
		config.destroy()
	
	if(serv == 'apache'): msg = ['Apache2', 'apache2/apache2.conf']
	elif(serv == 'mysql'): msg = ['MySQL', 'mysql/my.cnf']
	elif(serv == 'tor'): msg = ['Tor', 'tor/torsocks.conf']
	
	conf = open("/etc/{}".format(msg[1]), "r")
	content = conf.read()
	conf.close()
	
	print("{}> {}Editing {} configuration file{}_".format(name, color.YELLOW, msg[0], color.END))
	
	config = Tk()
	config.title("Edition Configuration {}".format(msg[0]))
	config.resizable(height=FALSE, width=FALSE)
	
	panel = [Frame(config)]
	panel[0].grid(row=0, column=0)
	
	scroll = Scrollbar(panel[0])
	scroll.grid(row=0, column=1, pady=1, sticky=NS)
	area = Text(panel[0], font=["Monospace", 9], height=40, width=81, wrap=WORD)
	area.insert(END, content)
	area.grid(row=0, column=0)
	area.config(yscrollcommand=scroll.set)
	scroll.config(command=area.yview)
	
	Button(config, text="Enregistrer", font=["Ubuntu", 10], command=lambda:save()).grid(row=1, column=0, sticky=E)
	Button(config, text="Fermer", font=["Ubuntu", 10], command=config.destroy).grid(row=1, column=0, sticky=W)
	
	config.mainloop()
	config.quit()

def viewLog(serv, log):
	global step
	
	if(serv == 'apache'): path = 'apache2/'
	elif(serv == 'tor'): path = 'tor/'
	
	print("{}> {}Show {} {} file{}_".format(name, color.YELLOW, serv, log, color.END))
	step.set("Affichage du fichier {} {}".format(serv, log))
	
	logFile = open("/var/log/{}".format(path+log), "r")
	content = logFile.read()
	logFile.close()
	
	viewer = Tk()
	viewer.title("Logs de {}".format(log))
	viewer.resizable(height=False, width=False)
	
	panel = [Frame(viewer)]
	panel[0].grid(row=0, column=0)
	
	scroll = Scrollbar(panel[0])
	scroll.grid(row=0, column=1, pady=1, sticky=NS)
	area = Text(panel[0], font=["Monospace", 9], height=30, width=81, wrap=WORD)
	area.insert(END, content)
	area.grid(row=0, column=0)
	area.config(yscrollcommand=scroll.set)
	scroll.config(command=area.yview)
	
	Button(viewer, text="Fermer", font=["Ubuntu", 10], command=viewer.destroy).grid(row=1, column=0)
	
	viewer.mainloop()
	viewer.quit()

def shell():
	global step
	print("{}> {}Opening shell{}_".format(name, color.YELLOW, color.END))
	step.set("Ouverture du shell")
	
	term = Tk()
	term.title("{} Shell".format(name.capitalize()))
	term.resizable(height=False, width=False)
	
	panel = [Frame(term, height=330, width=560)]
	panel[0].grid()
	console = panel[0].winfo_id()
	os.system("xterm -into {} -geometry 90x25 -sb &".format(console))
	
	term.mainloop()
	term.quit()

def about():
	print("{}> {}Show more info{}_".format(name, color.YELLOW, color.END))
	aboutus = Tk()
	aboutus.title("A propos de {}".format(name.capitalize()))
	aboutus.resizable(width=FALSE, height=FALSE)
	
	panel = [Frame(aboutus, bd=0)]
	panel[0].grid(row=0, column=0, padx=25, pady=30)
	Label(panel[0], text=name.capitalize(), font=['Ubuntu', 20]).grid(row=0, pady=20, sticky=W)
	madeLabel(panel[0], [
		"Ecrit le\t\t: {}".format(date[0]),
		"Mis à Jour le\t: {}".format(date[1]),
		"Version\t\t: {}".format(version),
		"\nCe programme a été écrit en python",
		"https://tracks12.github.io/service.py/"
	], ['Ubuntu', 11])
	Label(aboutus, text="By {}".format(dev), font=['Ubuntu', 9]).grid(row=1, pady=5)
	
	aboutus.mainloop()
	aboutus.quit()

def helper():
	print("{}> {}Show helper{}_".format(name, color.YELLOW, color.END))
	helper = Tk()
	helper.title("{} Aide".format(name.capitalize()))
	
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
	global step
	print("{}> {}Initializing IHM{}_".format(name, color.GREEN, color.END))
	
	window = Tk()
	window.title(name.capitalize())
	window.resizable(width=FALSE, height=FALSE)
	
	step = StringVar()
	
	""" Menu """
	menubar = Menu(window, bd=0)
	
	menuContent = [
		[ # Menu Principale
			'Fichier', Menu(menubar, tearoff=0),
			['Terminal', 'Quitter'],
			[lambda:shell(), window.quit]
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
			['Aide', 'A propos'],
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
			if(True in [(not i) and (not j), (i == 1) and (j in [2, 3, 5]), (i == 2) and (j == 2), tor and (i == 3) and (j in [2, 3])]):
				menuContent[i][1].add_separator()
		
		menubar.add_cascade(label=menuContent[i][0], font=['Ubuntu Light', 10], menu=menuContent[i][1])
	""" ---------------------------------------------------------------------------------- """
	
	Label(window, text=name.capitalize(), font=['Ubuntu', 20]).grid(row=0, column=0, columnspan=2, padx=20, pady=8, sticky=W)
	
	panel = [
		LabelFrame(window, bd=1, relief=GROOVE, text=" General ", font=['Ubuntu Light', 12]),
		Frame(window, bd=1, relief=GROOVE),
		Frame(window)
	]
	
	""" General Control COMMAND """
	panel[0].grid(row=1, column=0, padx=8, pady=0, sticky=N)
	
	Button(panel[0], text='START', font=['Ubuntu', 9], command=lambda:servAll(1), width=8).grid(row=0, column=0, padx=6, pady=4, sticky=W)
	Button(panel[0], text='STOP', font=['Ubuntu', 9], command=lambda:servAll(0), width=8).grid(row=1, column=0, padx=6, pady=4, sticky=W)
	Button(panel[0], text='RESTART', font=['Ubuntu', 9], command=lambda:servAll(2), width=8).grid(row=2, column=0, padx=6, pady=4, sticky=W)
	""" ---------------------------------------------------------------------------------- """
	
	""" Main Panel """
	panel[1].grid(row=1, column=1, padx=8, pady=10)
	
	# Apache2 Service COMMAND
	madePanel(panel[1], " Apache2 ", 0, [lambda:serv('apache', 1), lambda:serv('apache', 2), lambda:edit('apache')])
	
	# MySQL Service COMMAND
	madePanel(panel[1], " MySQL ", 1, [lambda:serv('mysql', 1), lambda:serv('mysql', 2), lambda:edit('mysql')])
	
	# Tor Service COMMAND
	if(tor): madePanel(panel[1], " Tor ", 2, [lambda:serv('tor', 1), lambda:serv('tor', 2), lambda:edit('tor')])
	""" ---------------------------------------------------------------------------------- """
	
	""" Anexe Panel """
	panel[2].grid(row=2, column=0, columnspan=2, pady=8, sticky=W)
	
	Button(panel[2], text="Terminal", font=['Ubuntu', 10], command=lambda:shell()).grid(row=0, column=0, padx=4)
	Button(panel[2], text="Lister les Projets", font=['Ubuntu', 10], command=listProject).grid(row=0, column=1, padx=4)
	""" ---------------------------------------------------------------------------------- """
	
	Label(window, textvariable=step, font=['Monospace', 8]).grid(row=3, column=0, columnspan=2, padx=2, sticky=W)
	
	servAll(1)
	step.set("Lancement avec {} Prêt".format(python))
	
	window.config(menu=menubar)
	window.mainloop()
	window.quit()
	
	print("{}> {}Quitting{}_".format(name, color.RED, color.END))

arg, helpArg, aboutUs = [
	["-h" in sys.argv, "-?" in sys.argv, "--help" in sys.argv],
	["-l" in sys.argv, "--list" in sys.argv],
	["-t" in sys.argv, "--tor" in sys.argv],
	["-v" in sys.argv, "--version" in sys.argv],
	["-a" in sys.argv, "--about" in sys.argv],
	["-c" in sys.argv, "--check" in sys.argv]
], [
	" python {}\n".format(name),
	" Option         Option longue GNU       Description",
	" -a             --about                 A propos du soft",
	" -c             --check                 Vérifie l'existance des services Web",
	" -h, -?         --help                  Affiche ce message",
	" -l             --list                  Liste tous le repertoire du serveur",
	" -t             --tor                   Lancement en mod Tor",
	" -v             --version               Affiche la version du soft\n"
], [
	" {}".format(color.BOLD+color.YELLOW+name.capitalize()+color.END),
	" Running with {}".format(python),
	"\n Writed\t\t: {}".format(date[0]),
	" Last Update\t: {}".format(date[1]),
	" Version\t: {}".format(color.BOLD+color.RED+version+color.END),
	"\n This program was writed in python",
	" {}https://tracks12.github.io/service.py/{}".format(color.YELLOW, color.END),
	"\n {}By {}\n".format(color.BOLD+color.PURPLE, dev+color.END)
]

if(True in arg[0]):
	for txt in helpArg: print(txt)

elif(True in arg[1]): listProject()
elif(True in arg[3]): print(" {}\n".format(color.BOLD+color.RED+version+color.END))
elif(True in arg[4]):
	for txt in aboutUs: print(txt)

elif(True in arg[5]): verify()
else:
	if((platform.system() == "Linux") and (os.environ["USER"] == "root")):
		print("Launching with {}".format(python))
		splash()
		if(True in arg[2]):
			tor = True
			print("{}> {}Tor mod enabled{}_".format(name, color.YELLOW, color.END))
		
		if(verify()): main()
		print("Bye :)\n")
	
	elif(os.environ["USER"] != "root"):
		sys.argv.append("")
		if(sys.version_info[0] == 2): prog = "python2"
		elif(sys.version_info[0] == 3): prog = "python3"
		os.system("sudo {} service.py {}".format(prog, sys.argv[1]))
	elif(platform.system() != "Linux"): print(" [ {}ERROR{} ] - Operating System wasn't support\n".format(color.BOLD+color.RED, color.END))

"""
	-----
	 END
	-----
"""
