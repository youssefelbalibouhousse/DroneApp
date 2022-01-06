import cv2
import numpy as np



def findFace(cap):
    faceCascade = \
        cv2.CascadeClassifier('C:\\Users\\SALLE 6\\AppData\\Local\\Programs\\Python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    imgGris = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGris, scaleFactor = 1.2,minNeighbors=8)

    myFaceList = []
    myFaceListArea = []

    for (x, y, w,h) in faces:
        cv2.rectangle(img, (x,y), (x + w, y+h), (0,0,255), 2)


cap = cv2.imread('denzel.jpg')

while True :
    #_, img = cap.read()
    findFace(cap)
    cv2.imshow("Sortie",cap)
    cv2.waitKey(1)