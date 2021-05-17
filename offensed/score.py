import pygame
pygame.init()
police_score = pygame.font.Font(None,50) #changer la taille de la police
from Player import * 
from Data import *
from Word import *

class Score:
    def __init__(self, num):
        self.score = 0
        self.score_str = str(self.score) #car l'affichage ne prend pas de int
        self.result = police_score.render(self.score_str, True, pygame.Color("#000000"))
        self.score_rect = self.result.get_rect() #On s'est rendu compte (trop tard) que l'on pouvait mettre get_rect() ici à la place de = None

        if num == 1:
            self.score_rect.x = 440
            self.score_rect.y = 140
        else:
            self.score_rect.x = 690
            self.score_rect.y = 140


