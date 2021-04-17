#import
import test_de_tire
import pygame
import boutton
#import
JEU = True
pygame.init()


#jeu 
while JEU:
	for event in pygame.event.get():          
            if event.type == pygame.QUIT:
                var_lance_jeu = False 
                pygame.quit()
                sys.exit()
	pygame.display.update()
#jeu