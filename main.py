#import
import test_de_tire
import pygame
import boutton
#import
JEU = True
pygame.init()
screen = pygame.display.set_mode(800,600)
background = pygame.image.load("carte_couleur.png")

boutton_passer_tour=boutton.button((255,1,1),915,715,270,50,"Passer tours")


#jeu 
while JEU:
        boutton_passer_tour.draw(screen, (1,200,0))
        for event in pygame.event.get():          
                if event.type == pygame.QUIT:
                        var_lance_jeu = False 
                        pygamenhgffxdx.quit()
                        sys.exit()
                position_souris = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if boutton_passer_tour.isOver(position_souris):
                                varPA = 5
                                peut_attaquer = True
        pygame.display.update()
#jeu
