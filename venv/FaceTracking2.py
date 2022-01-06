import cv2

face_cascade = cv2.CascadeClassifier("Ressources/haarcascade_frontalface_alt2.xml")
img = cv2.imread('denzel.jpg') #connexion camera ou image dans ressources

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray,1.2,8)

print(*face)

# while True :
#     ret, frame = cap.read() #Lecture de l'image webcam avec 2 valeurs de retour (ret et frame)
#     tickmark = cv2.getTickCount()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     face = face_cascade.detectMultiScale(1.2,8)
#
#     for x, y, w, h in face:
#         cv2.rectangle(frame,(x,y), (x+w, y+h), (255,0,0),2)
#     if cv2.waitKey(1)==ord('g'):
#         break
#     fps =cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)