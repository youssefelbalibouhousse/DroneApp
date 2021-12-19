from djitellopy import tello
from time import sleep

#on cree un objet pour tester
objet1  = tello.Tello()

#connexion via la bibliotheque
objet1.connect()

#Affichage du niveau batterie
print(objet1.get_battery())

# via les parametre on donne un ordre de mouvement (g/d, a/r, h/b, rotation)
objet1.send_rc_control(0,50,0,0)
#Puis on lui integre un arret de 2 s
sleep(2)
# et enfin on atteri
objet1.land()
