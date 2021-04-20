#import
import test_de_tire
import pygame
import boutton
import main_var
import liste_entite
#import

#mise en place jeu
JEU = True
pygame.init()
screen = pygame.display.set_mode(main_var.size)
background = pygame.image.load("font.png")
screen.fill(main_var.color)
background = pygame.transform.scale(background,main_var.size)
screen.blit(background,(0,0))
pygame.font.init() 
myfont = pygame.font.SysFont('comicsans', 30)
attaquant_trouve  = False 
defensseur_trouve = False
#mise en place jeu

#boutton simulation
boutton_simuler=boutton.button(main_var.color,465,750,270,50,"simuler")
#boutton simulation

#boutton uniter
FW=boutton.button(main_var.color,100,100,100,40,"fire warrior")
MARINES=boutton.button(main_var.color,220,100,100,40,"space marines")
CULTIST=boutton.button(main_var.color,340,100,100,40,"cultist")
HAMMERHEAD=boutton.button(main_var.color,460,100,100,40,"hammerhead")
#boutton uniter

#test de selection des uniter
attack = myfont.render(str("attaquant"), False, (0, 0, 0))
screen.blit(attack,(1000,740))
defensseur = myfont.render(str("defensseur"), False, (0, 0, 0))
screen.blit(defensseur,(1000,840))
if attaquant_trouve:
        pygame.draw.circle(screen,main_var.green,(1120,730),10)
else:
        pygame.draw.circle(screen,main_var.red,(1120,730),10)   
if defensseur_trouve:
        pygame.draw.circle(screen,main_var.green,(1120,830),10)
else:
        pygame.draw.circle(screen,main_var.red,(1120,830),10)
#test de selection des uniter
                        
#jeu 
while JEU:
        #boutton DRAW
        boutton_simuler.draw(screen, (1,200,0))
        FW.draw(screen, (1,200,0))
        MARINES.draw(screen, (1,200,0))
        CULTIST.draw(screen, (1,200,0))
        HAMMERHEAD.draw(screen, (1,200,0))
        #boutton DRAW

        for event in pygame.event.get():          
                #quittez le logiciel
                if event.type == pygame.QUIT:
                        var_lance_jeu = False 
                        pygame.quit()
                        sys.exit()       
                #test de position souris
                position_souris = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        #choix attaquant et defense
                        #FW
                        if FW.isOver(position_souris):
                                if attaquant_trouve:
                                        e,svg,nb_pv_def,nb_defenseur = liste_entite.FW(attaquant_trouve)
                                        defensseur_trouve = True
                                else:
                                        nb_de_tire,nb_tireur,ct,f,pa = liste_entite.FW(attaquant_trouve)
                                        attaquant_trouve = True
                        #MARINES
                        if MARINES.isOver(position_souris):
                                if attaquant_trouve:
                                        e,svg,nb_pv_def,nb_defenseur = liste_entite.FW(attaquant_trouve)
                                        defensseur_trouve = True
                                else:
                                        nb_de_tire,nb_tireur,ct,f,pa = liste_entite.FW(attaquant_trouve)
                                        attaquant_trouve = True
                        #CULTIST
                        if CULTIST.isOver(position_souris):
                                if attaquant_trouve:
                                        e,svg,nb_pv_def,nb_defenseur = liste_entite.FW(attaquant_trouve)
                                        defensseur_trouve = True
                                else:
                                        nb_de_tire,nb_tireur,ct,f,pa = liste_entite.FW(attaquant_trouve)
                                        attaquant_trouve = True
                        #HAMMERHEAD
                        if HAMMERHEAD.isOver(position_souris):
                                if attaquant_trouve:
                                        e,svg,nb_pv_def,nb_defenseur = liste_entite.FW(attaquant_trouve)
                                        defensseur_trouve = True
                                else:
                                        nb_de_tire,nb_tireur,ct,f,pa = liste_entite.FW(attaquant_trouve)
                                        attaquant_trouve = True
                        #choix attaquant et defense
                        
                        #test de selection des uniter
                        attack = myfont.render(str("attaquant"), False, (0, 0, 0))
                        screen.blit(attack,(1000,740))
                        defensseur = myfont.render(str("defensseur"), False, (0, 0, 0))
                        screen.blit(defensseur,(1000,840))
                        if attaquant_trouve:
                                pygame.draw.circle(screen,main_var.green,(1120,730),10)
                        else:
                                pygame.draw.circle(screen,main_var.red,(1120,730),10)   
                        if defensseur_trouve:
                                pygame.draw.circle(screen,main_var.green,(1120,830),10)
                        else:
                                pygame.draw.circle(screen,main_var.red,(1120,830),10)
                        #test de selection des uniter
                        
                        #simulation
                        if boutton_simuler.isOver(position_souris):
                                if attaquant_trouve and defensseur_trouve:
                                        nb_defenseur,reste = test_de_tire.test_de_tire_fonc_v2 (e,svg,nb_pv_def,nb_defenseur,nb_de_tire,nb_tireur,ct,f,pa)
                                        attaquant_trouve  = False 
                                        defensseur_trouve = False
                                        pygame.draw.rect(screen,(255,255,255),(400,820,500,890))
                                        textsurface = myfont.render(str(reste), False, (0, 0, 0))
                                        textsurface2 = myfont.render(str(nb_defenseur), False, (0, 0, 0))
                                        screen.blit(textsurface,(465,840))
                                        screen.blit(textsurface2,(550,840))
        pygame.display.update()
#jeu
pygame.quit()
