import cv2
from djitellopy import Tello

objet1 = Tello.Tello()
objet1.connect()

objet1.streamon()
frame_read = objet1.get_frame_read()

objet1.takeoff()
cv2.imwrite("picture.png", frame_read.frame)

objet1.land()