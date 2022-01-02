import math

import CommandeClavierModule as ccm
from djitellopy import tello
import numpy as np #calul matriciel
import cv2
from time import sleep

##PARAMETRAGE##
arSpeed = 117/10 # vitesse d'avance en cm/s (15cm/s)
angSpeed = 360/10 #vitesse angulaire en degre° par seconde
cycle = 0.25

arCycle = arSpeed*cycle
angCycle = angSpeed*cycle

##########################################



#objet, connexion, batterie affichage

x,y= 500,500
a = 0
yaw = 0


ccm.init()
objet1= tello.Tello()
objet1.connect()
print(objet1.get_battery())

points = [(0,0),(0,0)]




def getClavierInput():
    gd, ar, hb, rot = 0,0,0,0
    ordre = 15 #metre par seconde
    d = 0
    ordreRot = 50
    global yaw, x,y,a


    if ccm.getClavier("LEFT"):
        lr = ordre
        d = arCycle
        a = -180
    elif ccm.getClavier("RIGHT"):
        lr= ordre
        d = -arCycle
        a = 180

    if ccm.getClavier("UP"):
        ar = ordre
        d = arCycle
        a = 270

    elif ccm.getClavier("DOWN"):
        ar = -ordre
        d = -arCycle
        a = -90

    if ccm.getClavier("h"):
        hb = ordre
    elif ccm.getClavier("b"):
        hb = -ordre

    if ccm.getClavier("d"):
        rot = ordreRot
        yaw -= angCycle
    elif ccm.getClavier("q"):
        rot = -ordreRot
        yaw += angCycle

    if ccm.getClavier("a"):
        objet1.land()
    if ccm.getClavier("v"):
        objet1.takeoff()

    sleep(cycle)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [gd, ar, hb, rot,x ,y]

def trace(img,points):
    for point in points:
        cv2.circle( img , point, 5,(0,0,255),cv2.FILLED)

    cv2.circle(img, points[-1], 10, (0, 255, 0), cv2.FILLED) # Point vert pour discriminer la position du drone
    cv2.putText(img,f'({(points[-1][0]- 500)/100},{(points[-1][1]- 500)/100})m',(points[-1][0]+10, points[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)



while True:
    valeur = getClavierInput()
    objet1.send_rc_control(valeur[0],valeur[1],valeur[2],valeur[3])

    img = np.zeros((1000, 1000, 3), np.uint8)

    if (points[-1][0] != valeur[4] or points[-1][1] != valeur[5]):
        points.append((valeur[4],valeur[5]))

    trace(img,points)

    cv2.imshow("carte", img)
    cv2.waitKey(1)
