import CommandeClavierModule as ccm
from djitellopy import tello
from time import sleep

ccm.init()
objet1= tello.Tello()
objet1.connect()
print(objet1.get_battery())



def getClavierInput():
    gd, ar, hb, rot = 0,0,0,0
    ordre = 50

    if ccm.getClavier("LEFT"):
        lr = -ordre
    elif ccm.getClavier("RIGHT"):
        lr= ordre

    if ccm.getClavier("UP"):
        ar = ordre
    elif ccm.getClavier("DOWN"):
        ar = -ordre

    if ccm.getClavier("1"):
        hb = ordre
    elif ccm.getClavier("0"):
        hb = -ordre

    if ccm.getClavier("q"):
        rot = ordre
    elif ccm.getClavier("d"):
        rot = -ordre

    if ccm.getClavier("a"):
        objet1.land()
    if ccm.getClavier("v"):
        objet1.takeoff()

    return [gd, ar, hb, rot]




while True:
    valeur = getClavierInput()
    objet1.send_rc_control(valeur[0],valeur[1],valeur[2],valeur[3])
    sleep(0.05)