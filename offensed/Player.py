import pygame
pygame.init()


class Player(pygame.sprite.Sprite):

    def __init__(self, name, first):
        super().__init__()
        self.score = 0        
        if name == "Joe":
            self.proud = "pet"
            self.complexe = "style"
            self.image =pygame.transform.scale(pygame.image.load("./Assets/perso-1.png"), (136,208)) #création le l'image perso
                                                                                                    #taille du perso
            

        elif name == "Kev":
            self.proud = "style"
            self.complexe = "word"
            self.image =pygame.transform.scale(pygame.image.load("./Assets/perso-2.png"), (126,195)) 

        self.rect = self.image.get_rect()
        

        if name == "Joe":
            self.rect.x = 440
            self.rect.y = 257
        if name == "Kev":
            self.rect.x = 550
            self.rect.y = 172