import pygame
from Player import *
from Data import *
from Word import *
from Game import *
from score import *
import math
pygame.init()


#generer fenêtre

pygame.display.set_caption("offensed(OR NOT)")
screen = pygame.display.set_mode((1080, 720))


#importer le background

background = pygame.image.load('./Assets/background_intro.jpg')
background = pygame.transform.scale(background, (1080,720))

backgroundGame = pygame.image.load("./Assets/background_game.jpg")
backgroundGame = pygame.transform.scale(backgroundGame, (1080,720))

#import bannière

banner = pygame.image.load("./Assets/tittle.png")
# banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 6.66)
banner_rect.y = math.ceil(screen.get_height() / 5)


#importer bouton

play_button = pygame.image.load("./Assets/play.png")
# play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/4)
play_button_rect.y = math.ceil(screen.get_height()/1.7)




#charger les scores

score1 = Score(1)
score2 = Score(2)



#charger le jeu
game = Game()

#appararition des mots pour jouer
i = 0 #compteur d'apparition des listes
j = 0
x = 100 ##placer le début des mots sur x
y = 550 ## sur y
xbis = 100
for liste in genre:
    for word in liste:# faire apparaire tout les mots de la liste.
        word.rect = word.txt.get_rect()
        word.rect.x =  x
        word.rect.y =  y
        x += 200
        if xbis * 8 < x: #faire des lignes de mots
            x = 100
            y += 30
            if y > 639:
                y = 550

#maintenir la fenêtre

running = True

while running:
    
     # modifier pour bouger l'image dans la fenêtre x,y
    
    
    #playing verif
    if game.is_playing:
        #application de la fenêtre du jeu
        
        screen.blit(backgroundGame, (0,0))
        game.update(screen, i, j)
        screen.blit(score1.result, score1.score_rect)
        screen.blit(score2.result, score2.score_rect)
        

    else:
        #application des backgrounds et bouton play en écran d'accueil
        screen.blit(background, (0,0))
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)


    #screen refresh
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #savoir si la souris touche le bouton jouer.
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True
            
            
            for liste in genre:
                # while count < i:
                    for word in liste:
                        if word.rect.collidepoint(event.pos):
                            turn +=1
                            if turn%2 == 0:
                                i +=1
   
                            if countPlayer%2 != 0 :
                                countPlayer += 1
                                phrasej1.append(Word(word.name, word.genre, word.category)) #afficher mots dans la liste phrasej1
                                liste.remove(word) 
                                for words in phrasej1:
                                # print("avant: x1", x1, "y1", y1)
                                    if words.rect == None:
                                        words.rect = words.txt.get_rect() #création du rect pour chaque mot
                                        words.rect.x = x1  + total1 #placement en prenant compte de la taille du dernier mot
                                        words.rect.y = y1
                                        words.width = words.rect.width
                                        x1 += 5
                                        
                                        total1 +=  words.width #addition du total des width pour placement des mots
                                        if x1bis < x1:
                                            x1 = 100
                                            y1 += 20
                                            total1 = 0
                                    else:
                                        pass
                                    # print("après: x1", x1, "y1", y1)
                                    # print("j1",phrasej1)
                            else:
                                
                                phrasej2.append(Word(word.name, word.genre, word.category))
                                liste.remove(word)
                                countPlayer += 1
                                for words in phrasej2:
                                # print("avant: x1", x1, "y1", y1)
                                    if words.rect == None:
                                        words.rect = words.txt.get_rect()
                                        words.rect.x = x2  + total2
                                        words.rect.y = y2
                                        words.width = words.rect.width
                                        x2 += 5
                                        
                                        total2 +=  words.width
                                        if x2bis < x2:
                                            x2 = 650
                                            y2 += 20
                                            total2 = 0
                                    else:
                                        pass
                                    # print("après: x1", x1, "y1", y1)
                                    # print("j2",phrasej2)
                            
                            screen.blit(words.txt, words.rect)
                            

            #calcul du score des joueurs
            if phrasej1 == []:
                pass
            else:
                for word in phrasej1:
                    if word.category == game.player.proud: #si le joueur écrit une phrase en rapport avec sa fierté ce dernier voit son score multiplier par 1.5
                        score1.score += word.score * 1.5
                    elif word.category == game.player.complexe: #si le joueur écrit une phrase en rapport avec sa fierté ce dernier voit son score multiplier par 2
                        score1.score += word.score * 2
                    else:
                        score1.score += word.score
                
            if phrasej2 == []:
                pass
            else:
                for word in phrasej2:

                    if word.category == game.player2.proud:
                        score2.score += word.score * 1.5
                    elif word.category == game.player2.complexe:
                        score2.score += word.score * 2
                    else:
                        score2.score += word.score    
                
                #     count += 1
                # i +=1
                            
