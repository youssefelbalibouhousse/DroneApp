"""
    auteur : Youss.D.El
    date : 05/12/21

"""

import CommandeClavierModule as ccm
from djitellopy import tello
import time



import cv2

ccm.init()
objet1= tello.Tello()
objet1.connect()
print(objet1.get_battery())

objet1.streamon()

objet1.flip_back()



def getClavierInput():
    gd, ar, hb, rot = 0,0,0,0
    ordre = 50

    if ccm.getClavier("LEFT"):
        gd = -ordre
    elif ccm.getClavier("RIGHT"):
        gd= ordre

    if ccm.getClavier("UP"):
        ar = ordre
    elif ccm.getClavier("DOWN"):
        ar = -ordre

    if ccm.getClavier("h"):
        hb = ordre
    elif ccm.getClavier("b"):
        hb = -ordre

    if ccm.getClavier("q"):
        rot = ordre
    elif ccm.getClavier("d"):
        rot = -ordre

    if ccm.getClavier("a"):
        objet1.land()
    if ccm.getClavier("v"):
        objet1.takeoff()
    if ccm.getClavier("f"):
        objet1.flip_back()

    # if ccm.getClavier("e"):
    #     objet1.flip_back()
        # cv2.imwrite(f'Ressources/Images')

    return [gd, ar, hb, rot]




while True:
    valeur = getClavierInput()
    objet1.send_rc_control(valeur[0],valeur[1],valeur[2],valeur[3])
    image = objet1.get_frame_read().frame
    image = cv2.resize(image,(360,240))
    cv2.imshow("Image",image)
    cv2.waitKey(1)
