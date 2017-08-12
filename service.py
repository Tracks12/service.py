#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017 - Copyright by 4N4RCHY. All rights is reserved.

# ----------------------------
#  Program >>> service.py
#  Function >>> Show Services
# ----------------------------

import os, sys
import warnings
from Tkinter import *

class color:
	RED	= '\033[31m'
	GREEN	= '\033[32m'
	YELLOW	= '\033[33m'
	END	= '\033[0m'

def program():
	print("> " + color.GREEN + "Runing Service Command GRAPH mod_" + color.END)
	service = Tk()
	service.title('Service { COMMAND PANEL }')
	service.resizable(width=FALSE, height=FALSE)
	
	menubar = Menu(service)
	menu0 = Menu(menubar, tearoff=0)
	menu0.add_command(label="Quitter", command=service.quit)
	menubar.add_cascade(label="Fichier", menu=menu0)
	
	""" Apache2 Service COMMAND """
	panel0 = Frame(service, borderwidth=1, relief=GROOVE)
	panel0.pack(side=TOP, padx=8, pady=8)
	Label(panel0, text="Service Apache2").pack(padx=5, pady=2)
	
	Button(panel0, text="START", command=apache2_start).pack(side=LEFT, padx=4, pady=4)
	Button(panel0, text="RESTART", command=apache2_restart).pack(side=LEFT, padx=4, pady=4)
	Button(panel0, text="STOP", command=apache2_stop).pack(side=LEFT, padx=4, pady=4)
	""" ---------------------------------------------------------------------------------- """
	
	""" MySQL Service COMMAND """
	panel1 = Frame(service, borderwidth=1, relief=GROOVE)
	panel1.pack(side=TOP, padx=8, pady=8)
	Label(panel1, text="Service MySQL").pack(padx=5, pady=2)
	
	Button(panel1, text="START", command=mysql_start).pack(side=LEFT, padx=4, pady=4)
	Button(panel1, text="RESTART", command=mysql_restart).pack(side=LEFT, padx=4, pady=4)
	Button(panel1, text="STOP", command=mysql_stop).pack(side=LEFT, padx=4, pady=4)
	""" ---------------------------------------------------------------------------------- """
	
	""" Tor Service COMMAND """
	panel2 = Frame(service, borderwidth=1, relief=GROOVE)
	panel2.pack(side=TOP, padx=8, pady=8)
	Label(panel2, text="Service Tor").pack(padx=5, pady=2)
	
	Button(panel2, text="START", command=tor_start).pack(side=LEFT, padx=4, pady=4)
	Button(panel2, text="RESTART", command=tor_restart).pack(side=LEFT, padx=4, pady=4)
	Button(panel2, text="STOP", command=tor_stop).pack(side=LEFT, padx=4, pady=4)
	""" ---------------------------------------------------------------------------------- """
	
	Button(service, text="QUIT", command=service.quit).pack(side=RIGHT, padx=8, pady=8)
	
	service.config(menu=menubar)
	service.mainloop()
	print("> " + color.RED + "Quitting_" + color.END)
	exit(1)

def apache2_start(): os.system('sudo /etc/init.d/apache2 start'); check()
def apache2_restart(): os.system('sudo /etc/init.d/apache2 restart'); check()
def apache2_stop(): os.system('sudo /etc/init.d/apache2 stop'); check()

def mysql_start(): os.system('sudo /etc/init.d/mysql start'); check()
def mysql_restart(): os.system('sudo /etc/init.d/mysql restart'); check()
def mysql_stop(): os.system('sudo /etc/init.d/mysql stop'); check()

def tor_start(): os.system('sudo /etc/init.d/tor start'); check()
def tor_restart(): os.system('sudo /etc/init.d/tor restart'); check()
def tor_stop(): os.system('sudo /etc/init.d/tor stop'); check()

def check(): print("> Action:\t\t\t\t\t\t\t\t[ " + color.YELLOW + "TERMINATED" + color.END + " ]")

program()

# -----
#  END
# -----
