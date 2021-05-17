import pygame
pygame.init()

from Player import *
from Game import *
from Data import *


first = 0
turn = 2
###### CRÉATION DE LA CLASS JEU -------LE JEU-------- #######
class Game:

    def __init__(self):
        #jeu play or off
        self.is_playing = False
        
        self.player = Player("Joe",first)
    
        self.player2 = Player("Kev",first)
            
    def update(self, screen, i, j):
        #application de l'img du joueur
        screen.blit(self.player.image, self.player.rect)
        screen.blit(self.player2.image, self.player2.rect)
        
        
        while j < len(genre[i]): #pour faire apparaitre uniquement la premiere liste grace au compteur i
            screen.blit(genre[i][j].txt, genre[i][j].rect) ###impossible de trouver comment afficher une seule liste puis l'autre correctement.
            j += 1
            if j < len(genre[i]): 
                pass
            else:
                break

       
         
        print("i :", i ,"j :",j)
            
        for words in phrasej1: #faire apparaître chaque nom dans la liste phrasej1
                screen.blit(words.txt, words.rect) 

        for words2 in phrasej2: #faire apparaître chaque nom dans la liste phrasej2
            screen.blit(words2.txt, words2.rect)
            # screen.blit(texte, texte_rect)