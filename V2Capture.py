import CommandeClavierModule as ccm
from djitellopy import tello
import time
import cv2

ccm.init()
objet1= tello.Tello()
objet1.connect()
print(objet1.get_battery())
global image

objet1.streamon()



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

    if ccm.getClavier("e"):
        cv2.imwrite(f'Ressources/Images/{time.time()}.jpg',image)
        time.sleep(0.3)


    return [gd, ar, hb, rot]




while True:
    valeurs = getClavierInput()
    objet1.send_rc_control(valeurs[0], valeurs[1], valeurs[2], valeurs[3])
    image = objet1.get_frame_read().frame
    image = cv2.resize(image,(360,240))
    cv2.imshow("Image",image)
    cv2.waitKey(1)