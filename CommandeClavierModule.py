"""Classe appeler par les autre pour un retour d'ordre via le clavier
Pygame servant d'interface d'attente d'evenement clavier et poster les requetes"""

import pygame


#Fenetre creation
def init():
    pygame.init()
    fenetre = pygame.display.set_mode((400,400))

#Recuperation de la lettre taper sur le clavier
def getClavier(lettre):
    rep = False
    for eve in pygame.event.get():
        pass
    lettreInput = pygame.key.get_pressed()
    myLettre = getattr(pygame,'K_{}'.format(lettre)) #format attendu K_{} par consencus
    if lettreInput[myLettre]:
        rep=True
    pygame.display.update()

    return rep

def main():
    if getClavier("LEFT"):
        print("Gauche")
    if getClavier("RIGHT"):
        print("Droite")

if __name__ =='__main__':
    init()
    while True:
        main()