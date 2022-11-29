import pygame
import random
from FirstCard import FirstCard
from SecondCard import SecondCard
from ThirdCard import ThirdCard
from FourthCard import FourthCard
from FifthCard import FifthCard
pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("PyStrat")

piocher1 = random.randint(1, 10)
piocher2 = random.randint(1, 10)
piocher3 = random.randint(1, 10)
piocher4 = random.randint(1, 10)
piocher5 = random.randint(1, 10)

mouse_pressed = False

print(piocher1)
print(piocher2)
print(piocher3)
print(piocher4)
print(piocher5)

fc = FirstCard()
sc = SecondCard()
tc = ThirdCard()
foc = FourthCard()
fic = FifthCard()

running = True


while running:

    # a garder sinon une autre carte en + apparaît
    screen.fill((0, 204, 102))

    def piocheFirstCard():
        if piocher1 == 1:
            screen.blit(fc.card1, (fc.x1, fc.y1))
            fc.x1 = 100
            fc.rect1.x = fc.x1
        if piocher1 == 2:
            screen.blit(fc.card2, (fc.x2, fc.y2))
            fc.x2 = 100
            fc.rect2.x = fc.x2
        if piocher1 == 3:
            screen.blit(fc.card3, (fc.x3, fc.y3))
            fc.x3 = 100
            fc.rect3.x = fc.x3
        if piocher1 == 4:
            screen.blit(fc.card4, (fc.x4, fc.y4))
            fc.x4 = 100
            fc.rect4.x = fc.x4
        if piocher1 == 5:
            screen.blit(fc.card5, (fc.x5, fc.y5))
            fc.x5 = 100
            fc.rect5.x = fc.x5
        if piocher1 == 6:
            screen.blit(fc.card6, (fc.x6, fc.y6))
            fc.x6 = 100
            fc.rect6.x = fc.x6
        if piocher1 == 7:
            screen.blit(fc.card7, (fc.x7, fc.y7))
            fc.x7 = 100
            fc.rect7.x = fc.x7
        if piocher1 == 8:
            screen.blit(fc.card8, (fc.x8, fc.y8))
            fc.x8 = 100
            fc.rect8.x = fc.x8
        if piocher1 == 9:
            screen.blit(fc.card9, (fc.x9, fc.y9))
            fc.x9 = 100
            fc.rect9.x = fc.x9
        if piocher1 == 10:
            screen.blit(fc.card10, (fc.x10, fc.y10))
            fc.x10 = 100
            fc.rect10.x = fc.x10

    def piocheSecondCard():
        if piocher2 == 1:
            screen.blit(sc.card1, (sc.x1, sc.y1))
            sc.x1 = 250
            sc.rect1.x = sc.x1
        if piocher2 == 2:
            screen.blit(sc.card2, (sc.x2, sc.y2))
            sc.x2 = 250
            sc.rect2.x = sc.x2
        if piocher2 == 3:
            screen.blit(sc.card3, (sc.x3, sc.y3))
            sc.x3 = 250
            sc.rect3.x = sc.x3
        if piocher2 == 4:
            screen.blit(sc.card4, (sc.x4, sc.y4))
            sc.x4 = 250
            sc.rect4.x = sc.x4
        if piocher2 == 5:
            screen.blit(sc.card5, (sc.x5, sc.y5))
            sc.x5 = 250
            sc.rect5.x = sc.x5
        if piocher2 == 6:
            screen.blit(sc.card6, (sc.x6, sc.y6))
            sc.x6 = 250
            sc.rect6.x = sc.x6
        if piocher2 == 7:
            screen.blit(sc.card7, (sc.x7, sc.y7))
            sc.x7 = 250
            sc.rect7.x = sc.x7
        if piocher2 == 8:
            screen.blit(sc.card8, (sc.x8, sc.y8))
            sc.x8 = 250
            sc.rect8.x = sc.x8
        if piocher2 == 9:
            screen.blit(sc.card9, (sc.x9, sc.y9))
            sc.x9 = 250
            sc.rect9.x = sc.x9
        if piocher2 == 10:
            screen.blit(sc.card10, (sc.x10, sc.y10))
            sc.x10 = 250
            sc.rect10.x = sc.x10

    def piocheThirdCard():
        if piocher3 == 1:
            screen.blit(tc.card1, (tc.x1, tc.y1))
            tc.x1 = 400
            tc.rect1.x = tc.x1
        if piocher3 == 2:
            screen.blit(tc.card2, (tc.x2, tc.y2))
            tc.x2 = 400
            tc.rect2.x = tc.x2
        if piocher3 == 3:
            screen.blit(tc.card3, (tc.x3, tc.y3))
            tc.x3 = 400
            tc.rect3.x = tc.x3
        if piocher3 == 4:
            screen.blit(tc.card4, (tc.x4, tc.y4))
            tc.x4 = 400
            tc.rect4.x = tc.x4
        if piocher3 == 5:
            screen.blit(tc.card5, (tc.x5, tc.y5))
            tc.x5 = 400
            tc.rect5.x = tc.x5
        if piocher3 == 6:
            screen.blit(tc.card6, (tc.x6, tc.y6))
            tc.x6 = 400
            tc.rect6.x = tc.x6
        if piocher3 == 7:
            screen.blit(tc.card7, (tc.x7, tc.y7))
            tc.x7 = 400
            tc.rect7.x = tc.x7
        if piocher3 == 8:
            screen.blit(tc.card8, (tc.x8, tc.y8))
            tc.x8 = 400
            tc.rect8.x = tc.x8
        if piocher3 == 9:
            screen.blit(tc.card9, (tc.x9, tc.y9))
            tc.x9 = 400
            tc.rect9.x = tc.x9
        if piocher3 == 10:
            screen.blit(tc.card10, (tc.x10, tc.y10))
            tc.x10 = 400
            tc.rect10.x = tc.x10

    def piocheFourthCard():
        if piocher4 == 1:
            screen.blit(foc.card1, (foc.x1, foc.y1))
            foc.x1 = 550
            foc.rect1.x = foc.x1
        if piocher4 == 2:
            screen.blit(foc.card2, (foc.x2, foc.y2))
            foc.x2 = 550
            foc.rect2.x = foc.x2
        if piocher4 == 3:
            screen.blit(foc.card3, (foc.x3, foc.y3))
            foc.x3 = 550
            foc.rect3.x = foc.x3
        if piocher4 == 4:
            screen.blit(foc.card4, (foc.x4, foc.y4))
            foc.x4 = 550
            foc.rect4.x = foc.x4
        if piocher4 == 5:
            screen.blit(foc.card5, (foc.x5, foc.y5))
            foc.x5 = 550
            foc.rect5.x = foc.x5
        if piocher4 == 6:
            screen.blit(foc.card6, (foc.x6, foc.y6))
            foc.x6 = 550
            foc.rect6.x = foc.x6
        if piocher4 == 7:
            screen.blit(foc.card7, (foc.x7, foc.y7))
            foc.x7 = 550
            foc.rect7.x = foc.x7
        if piocher4 == 8:
            screen.blit(foc.card8, (foc.x8, foc.y8))
            foc.x8 = 550
            foc.rect8.x = foc.x8
        if piocher4 == 9:
            screen.blit(foc.card9, (foc.x9, foc.y9))
            foc.x9 = 550
            foc.rect9.x = foc.x9
        if piocher4 == 10:
            screen.blit(foc.card10, (foc.x10, foc.y10))
            foc.x10 = 550
            foc.rect10.x = foc.x10
    
    def piocheFifthCard():
        if piocher5 == 1:
            screen.blit(fic.card1, (fic.x1, fic.y1))
            fic.x1 = 700
            fic.rect1.x = fic.x1
        if piocher5 == 2:
            screen.blit(fic.card2, (fic.x2, fic.y2))
            fic.x2 = 700
            fic.rect2.x = fic.x2
        if piocher5 == 3:
            screen.blit(fic.card3, (fic.x3, fic.y3))
            fic.x3 = 700
            fic.rect3.x = fic.x3
        if piocher5 == 4:
            screen.blit(fic.card4, (fic.x4, fic.y4))
            fic.x4 = 700
            fic.rect4.x = fic.x4
        if piocher5 == 5:
            screen.blit(fic.card5, (fic.x5, fic.y5))
            fic.x5 = 700
            fic.rect5.x = fic.x5
        if piocher5 == 6:
            screen.blit(fic.card6, (fic.x6, fic.y6))
            fic.x6 = 700
            fic.rect6.x = fic.x6
        if piocher5 == 7:
            screen.blit(fic.card7, (fic.x7, fic.y7))
            fic.x7 = 700
            fic.rect7.x = fic.x7
        if piocher5 == 8:
            screen.blit(fic.card8, (fic.x8, fic.y8))
            fic.x8 = 700
            fic.rect8.x = fic.x8
        if piocher5 == 9:
            screen.blit(fic.card9, (fic.x9, fic.y9))
            fic.x9 = 700
            fic.rect9.x = fic.x9
        if piocher5 == 10:
            screen.blit(fic.card10, (fic.x10, fic.y10))
            fic.x10 = 700

    def piocheAllCards():
        piocheFirstCard()
        piocheSecondCard()
        piocheThirdCard()
        piocheFourthCard()
        piocheFifthCard()

    piocheAllCards()

    mouse = pygame.mouse.get_pos()

    def checkIfMouseOnCard1():
        if fc.rect1.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect2.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect3.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect4.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect5.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect6.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect7.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect8.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect9.collidepoint(mouse) and mouse_pressed:
               print("hi")
        if fc.rect10.collidepoint(mouse) and mouse_pressed:
               print("hi")

    def checkIfMouseOnCard2():
        if sc.rect1.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect2.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect3.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect4.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect5.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect6.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect7.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect8.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect9.collidepoint(mouse) and mouse_pressed:
               print("ok2")
        if sc.rect10.collidepoint(mouse) and mouse_pressed:
               print("ok2")

    def checkIfMouseOnCard3():
        if tc.rect1.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect2.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect3.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect4.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect5.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect6.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect7.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect8.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect9.collidepoint(mouse) and mouse_pressed:
               print("ok3")
        if tc.rect10.collidepoint(mouse) and mouse_pressed:
               print("ok3")

    def checkIfMouseOnCard4():
        if foc.rect1.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect2.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect3.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect4.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect5.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect6.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect7.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect8.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect9.collidepoint(mouse) and mouse_pressed:
               print("ok4")
        if foc.rect10.collidepoint(mouse) and mouse_pressed:
               print("ok4")

    def checkIfMouseOnCard5():
        if fic.rect1.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect2.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect3.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect4.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect5.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect6.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect7.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect8.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect9.collidepoint(mouse) and mouse_pressed:
               print("ok5")
        if fic.rect10.collidepoint(mouse) and mouse_pressed:
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