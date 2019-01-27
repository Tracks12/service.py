# Aperçu

<img src='https://raw.githubusercontent.com/Tracks12/CustomServiceCommand/master/ihm.png' />

> Une simple fenêtre Tkinter, à l'apparence d'un panneau de contrôle, offrant un raccourci directe aux services web linux installer sur la machine.

# Mode de lancement :
<ul>
  <li>
    Lancement normal avec les commandes des services Apache2 et MySQL
    <pre>:~# python2 service.py</pre>
  </li>
  <li>
    Lancement en mode Tor ajoutant les commandes du service Tor si il est installer
    <pre>
      :~# python2 service.py -t
      :~# python2 service.py --tor
    </pre>
  </li>
</ul>

# Arguments :
Syntax pour afficher la liste des arguments :
<pre>
  :~# python2 service -h
  :~# python2 service -?
  :~# python2 service --help
</pre>

Liste des arguments :
<pre> python2 service.py

 Option         Option longue GNU       Description
 -a             --about                 A propos du soft
 -h, -?         --help                  Affiche ce message
 -l             --list                  Liste tous le repertoire du serveur
 -t             --tor                   Lancement en mod Tor
 -v             --version               Affiche la version du soft</pre>

# Pré-requis :
<ul>
  <li>Installation de Python2</li>
  <li>Installation du module "Tkinter" pour python2</li>
  <li>Lancement en mode administrateur</li>
  <li>Compatible uniquement sous Linux</li>
</ul>
