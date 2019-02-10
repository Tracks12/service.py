# Aperçu

<img src='https://raw.githubusercontent.com/Tracks12/service.py/master/screenshots/ihm.png' />

> Une simple fenêtre Tkinter, à l'apparence d'un panneau de contrôle, offrant un raccourci directe aux services web linux installer sur la machine, à la fois compatible avec python2 et python3.

# Mode de lancement :
<ul>
  <li>
    Lancement normal avec les commandes des services Apache2 et MySQL
    <pre>:~# python service.py</pre>
  </li><br />
  <li>
    Lancement en mode Tor ajoutant les commandes du service Tor si il est installer
    <pre>:~# python service.py -t
:~# python service.py --tor</pre>
  </li>
</ul>

# Arguments :
Syntax pour afficher la liste des arguments :
<pre>:~# python service -h
:~# python service -?
:~# python service --help</pre>

Liste des arguments :
<pre> python service.py

 Option         Option longue GNU       Description
 -a             --about                 A propos du soft
 -c             --check                 Vérifie l'existance des services Web
 -h, -?         --help                  Affiche ce message
 -l             --list                  Liste tous le repertoire du serveur
 -t             --tor                   Lancement en mod Tor
 -v             --version               Affiche la version du soft</pre>

# Gestion des Ressources & Configurations :
Dès le démarrage de l'app, une analyse rapide des services présents sur la machine s'éxecute afin de voir si les services Apache2, MySQL et Tor sont bien installé, l'app ne démarrera qu'une fois les 3 services détecter sur la machine.

Un accès direct au fichier de configuration du service avec le bouton "CONFIG", une fois le panneau d'édition ouvert, vous pouvez modifier les paramètres dès que vous avez terminer l'édition.

<img src='https://raw.githubusercontent.com/Tracks12/service.py/master/screenshots/conf.png' />

L'accès direct au fichier log d'erreur et d'accès au serveur apache est aussi accessible dans le menu contextuel de l'app.

<img src='https://raw.githubusercontent.com/Tracks12/service.py/master/screenshots/log.png' />

Si jamais vous auriez besoin de faire plus que l'app vous propose, vous pouvez accéder au shell depuis l'app en cliquant sur le bouton "Terminal", une console s'ouvrira en mode admin.

# Pré-requis :
<ul>
  <li>Installation de Python 2 ou 3</li>
  <li>Installation du module "Tkinter" pour python2 ou "tkinter" pour python3</li>
  <li>Lancement en mode administrateur (Demande un mot de passe lors du lancement de l'app dans le shell)</li>
  <li>Compatible uniquement sous Linux</li>
</ul>

# Téléchargement
<ul>
  <li><a href="https://github.com/Tracks12/service.py/releases/download/0.0.7-a/service.zip">service.zip</a></li>
  <li><a href="https://github.com/Tracks12/service.py/archive/0.0.7-a.zip">Code Source zip</a></li>
  <li><a href="https://github.com/Tracks12/service.py/archive/0.0.7-a.tar.gz">Code Source tar.gz</a></li>
</ul>
