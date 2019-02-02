# Aperçu

<img src='https://raw.githubusercontent.com/Tracks12/CustomServiceCommand/master/ihm.png' />

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
 -h, -?         --help                  Affiche ce message
 -l             --list                  Liste tous le repertoire du serveur
 -t             --tor                   Lancement en mod Tor
 -v             --version               Affiche la version du soft</pre>

# Pré-requis :
<ul>
  <li>Installation de Python 2 ou 3</li>
  <li>Installation du module "Tkinter" pour python2 ou "tkinter" pour python3</li>
  <li>Lancement en mode administrateur (Demande un mot de passe lors du lancement du service dans le shell)</li>
  <li>Compatible uniquement sous Linux</li>
</ul>

# Téléchargement
<ul>
  <li><a href="https://github.com/Tracks12/service.py/archive/0.0.5-a.zip">v_0.0.5-a Service.zip</a></li>
  <li><a href="https://github.com/Tracks12/service.py/archive/0.0.5-a.tar.gz">v_0.0.5-a Service.tar.gz</a></li>
</ul>
