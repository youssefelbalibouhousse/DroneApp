from djitellopy import tello
from time import sleep
import cv2

#on cree un objet pour tester
objet1  = tello.Tello()

#connexion via la bibliotheque
objet1.connect()

#Affichage du niveau batterie
print(objet1.get_battery())

objet1.streamon()

while True:
    image = objet1.get_frame_read().frame
    image = cv2.resize(image,(1000,1000))
    cv2.imshow("Image",image)
    cv2.waitKey(1)