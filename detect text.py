import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\SALLE 6\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# stocker l'image avec texte
img = cv2.imread('denzel.jpg')

# Conversion du format GBR vers RVB pour pytesseract
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Afficher en console les caracteres detecter par tesseract dans la console sans les traiter
"""print(pytesseract.image_to_string(img))"""

# Afficher en console les caracteres detecter par tesseract dans la console en les isolant
"""print(pytesseract.image_to_boxes(img))"""

### Detection des caracteres
hImg, wImg,_= img.shape

# cong = r'--oem 3 --psm 6 outputbase digits'
#stock dans un tableau les element detecter et les affiches
tableau = pytesseract.image_to_boxes(img) #, config=cong)
for t in tableau.splitlines():
    #print(t)
    ## on separe les elements du tableau pour obtenir des liste pour chaque caracteres
    t = t.split(' ')
    print (t)
    # ici on attribut les coordonées et taille a x,y,w,h
    x,y,w,h = int(t[1]),int(t[2]),int(t[3]),int(t[4])

    # A l'aide des coordonée on cree le rectangle (nom img, (position),(taille box),(couleur), epaisseur lignes)
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)

    #On ajoute du texte en dessous de chaque case signifiant la lettre detecter par
    cv2.putText(img,t[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)




# emploi de imshow pour afficher l'image (test)
cv2.imshow('Resultat', img)
# Attends evenement clavier pour quitter
cv2.waitKey(0)
