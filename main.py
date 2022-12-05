import pygame
from Card import Card
from options import Options
from instantiateCards import *
from cardPositions import *

pygame.init()

mouse_pressed = False

running = True

definePositions()


while running:

    # a garder sinon une autre carte en + apparaît
    op.screen.fill((0, 204, 102))

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
            

    def piocheAllPlayerCards():
        piocheFirstCard()
        piocheSecondCard()
        piocheThirdCard()
        piocheFourthCard()
        piocheFifthCard()

    piocheAllPlayerCards()

    mouse = pygame.mouse.get_pos()

    def checkIfMouseOnCard1():
        if fc.rect.collidepoint(mouse) and mouse_pressed:
        	   print("ok1")

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

    checkIfMouseOnCard1()
    checkIfMouseOnCard2()
    checkIfMouseOnCard3()
    checkIfMouseOnCard4()
    checkIfMouseOnCard5()

    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()