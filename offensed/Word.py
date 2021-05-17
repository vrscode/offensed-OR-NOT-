# from pygame import Rect
import pygame
pygame.init()
police = pygame.font.Font(None,20)

class Word:

    def __init__(self, name, category, genre): 
        self.name = name
        self.txt = police.render(name,True,pygame.Color("#000000"))
        self.category = category
        self.genre = genre
        self.score = 1
        self.rect = None
        if self.rect == None: 
            pass
        else: # sinon si le rect n'est pas créer un bug se fait puisque rect.x n'est pas possible avec None
            self.rect.x = 0 
            self.rect.y = 0
            self.width = self.rect.width
            


        
        

    def __str__(self):
        return self.name
