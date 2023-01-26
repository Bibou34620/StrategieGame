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
playerCardPlayed = 0
botCardPlayed = 0
fbc.piocher = 10

definePositions()


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
    isPlayerTurn = True



    if fc.rect.collidepoint(mouse) and mouse_pressed:
            fc.x = 350
            fc.y = 230
            playerCardPlayed = fc.piocher
            isPlayerTurn = False
            print(isPlayerTurn)
               
    def checkIfMouseOnCard2():
        if sc.rect.collidepoint(mouse) and mouse_pressed:
               print("ok2")

    def checkIfMouseOnCard3():
        if tc.rect.collidepoint(mouse) and mouse_pressed:
            print("ok3")
    def checkIfMouseOnCard4():
        if foc.rect.collidepoint(mouse) and mouse_pressed:
               print("ok4")
    def checkIfMouseOnCard5():
        if fic.rect.collidepoint(mouse) and mouse_pressed:
               print("ok5")

    checkIfMouseOnCard2()
    checkIfMouseOnCard3()
    checkIfMouseOnCard4()
    checkIfMouseOnCard5()
    
    #logique du bot pour essayer de gagner
    if fbc.piocher > sbc.piocher and fbc.piocher > tbc.piocher and fbc.piocher > fobc.piocher and fbc.piocher > fibc.piocher and isPlayerTurn == False:
        fbc.x = 450
        fbc.y = 230

    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()