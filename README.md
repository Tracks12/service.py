# CustomServiceCommand
Interface Graphique de commande des Service Linux

<img src='https://raw.githubusercontent.com/Tracks12/CustomServiceCommand/master/ihm.png' />

> Une simple fenêtre Tkinter, à l'apparence d'un panneau de contrôle, offrant un raccourci directe aux services web linux installer sur la machine.

# Mode de lancement :
<ul>
<li>Lancement normal avec les commandes des services Apache2 et MySQL
  <pre>:~# python service.py</pre></li>

<li>Lancement en mode Tor ajoutant les commandes du service Tor si il est installer
<pre>:~# python service.py -t</pre>
<pre>:~# python service.py --tor</pre></li>
</ul>

# Pré-requis :

Lancement en mode administrateur, si le programme est lancer en utilisateur, un mot de passe administrateur sera demander.
<br /> Installation du module "tkinter" pour python sous le système linux.
