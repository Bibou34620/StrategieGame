import pygame
from Card import Card
from BotCard import BotCard
from options import Options
from instantiateCards import *
from cardPositions import *
from hideBotCards import *

pygame.init()

mouse_pressed = False
running = True
isPlayerTurn = True
isBotTurn = False
playerCardPlayed = 0
botCardPlayed = 0

definePositions()

print(fbc.piocher, " ", sbc.piocher , " ", tbc.piocher, " ", fobc.piocher, " ", fibc.piocher)
while running:

    # a garder sinon une autre carte en + apparaît
    op.screen.fill((0, 204, 102))

    #piocher toutes les cartes du joueur
    def piocheFirstCard():
        op.screen.blit(fc.card, (fc.x, fc.y))
    def piocheSecondCard():
        op.screen.blit(sc.card, (sc.x, sc.y))
    def piocheThirdCard():
        op.screen.blit(tc.card, (tc.x, tc.y))
    def piocheFourthCard():
        op.screen.blit(foc.card, (foc.x, foc.y))
    def piocheFifthCard():
        op.screen.blit(fic.card,(fic.x, fic.y))
            

    #piocher toutes les cartes du bot
    def piocheFirstBotCard():
        op.screen.blit(fbc.image, (fbc.x, fbc.y))
    def piocheSecondBotCard():
        op.screen.blit(sbc.image, (sbc.x, sbc.y))
    def piocheThirdBotCard():
        op.screen.blit(tbc.image, (tbc.x, tbc.y))
    def piocheFourthBotCard():
        op.screen.blit(fobc.image, (fobc.x, fobc.y))
    def piocheFifthBotCard():
        op.screen.blit(fibc.image,(fibc.x, fibc.y))

    def piocheAllPlayerCards():
        piocheFirstCard()
        piocheSecondCard()
        piocheThirdCard()
        piocheFourthCard()
        piocheFifthCard()

    def piocheAllBotCards():
        piocheFirstBotCard()
        piocheSecondBotCard()
        piocheThirdBotCard()
        piocheFourthBotCard()
        piocheFifthBotCard()


    piocheAllBotCards()
    piocheAllPlayerCards()
    hideBotCards()


    mouse = pygame.mouse.get_pos()


    if fc.rect.collidepoint(mouse) and mouse_pressed and isPlayerTurn == True and isBotTurn == False:
            fc.x = 350
            fc.y = 230
            playerCardPlayed = fc.piocher
            isPlayerTurn = False
            isBotTurn = True
               
    if sc.rect.collidepoint(mouse) and mouse_pressed and isPlayerTurn == True and isBotTurn == False:
            sc.x = 350
            sc.y = 230
            playerCardPlayed = fc.piocher
            isPlayerTurn = False
            isBotTurn = True

    if tc.rect.collidepoint(mouse) and mouse_pressed and isPlayerTurn == True and isBotTurn == False:
            tc.x = 350
            tc.y = 230
            playerCardPlayed = fc.piocher
            isPlayerTurn = False
            isBotTurn = True
            
    if foc.rect.collidepoint(mouse) and mouse_pressed and isPlayerTurn == True and isBotTurn == False:
            foc.x = 350
            tc.y = 230
            playerCardPlayed = fc.piocher
            isPlayerTurn = False
            isBotTurn = True
            
    if fic.rect.collidepoint(mouse) and mouse_pressed and isPlayerTurn == True and isBotTurn == False:
            fic.x = 350
            fic.y = 230
            playerCardPlayed = fc.piocher
            isPlayerTurn = False
            isBotTurn = True
    
    #logique du bot pour essayer de gagner
    if fbc.piocher > 7 and isPlayerTurn == False and isBotTurn == True:
        fbc.x = 450
        fbc.y = 230
        #mettre un sleep de 2 secondes et faire partir les cartes
        
    elif fbc.piocher < 7 and sbc.piocher > tbc.piocher and isPlayerTurn == False and isBotTurn == True:
        sbc.x = 450
        sbc.y = 230
        #mettre un sleep de 2 secondes et faire partir les cartes
        
    elif sbc.piocher < tbc.piocher and sbc.piocher > tbc.piocher and isPlayerTurn == False and isBotTurn == True:
        tbc.x = 450
        tbc.y = 230
        #mettre un sleep de 2 secondes et faire partir les cartes
        
    elif sbc.piocher < tbc.piocher and tbc.piocher > fobc.piocher and isPlayerTurn == False and isBotTurn == True:
        fobc.x = 450
        fobc.y = 230
        #mettre un sleep de 2 secondes et faire partir les cartes
        
    elif tbc.piocher < fobc.piocher and fobc.piocher > fibc.piocher and isPlayerTurn == False and isBotTurn == True:
        fibc.x = 450
        fibc.y = 230
        #mettre un sleep de 2 secondes et faire partir les cartes
        

    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()