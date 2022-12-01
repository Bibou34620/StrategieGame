import pygame
import random
from FirstCard import FirstCard
from SecondCard import SecondCard
from ThirdCard import ThirdCard
from FourthCard import FourthCard
from FifthCard import FifthCard
from FirstBotCard import FirstBotCard
from SecondBotCard import SecondBotCard
from ThirdBotCard import ThirdBotCard
from FourthBotCard import FourthBotCard
from FifthBotCard import FifthBotCard
from options import Options

pygame.init()

piocher1 = random.randint(1, 10)
piocher2 = random.randint(1, 10)
piocher3 = random.randint(1, 10)
piocher4 = random.randint(1, 10)
piocher5 = random.randint(1, 10)

piocher1bot = random.randint(1, 10)
piocher2bot = random.randint(1, 10)
piocher3bot = random.randint(1, 10)
piocher4bot = random.randint(1, 10)
piocher5bot = random.randint(1, 10)


mouse_pressed = False

print(piocher1)
print(piocher2)
print(piocher3)
print(piocher4)
print(piocher5)

# instanciation des classes
op = Options()
fc = FirstCard()
sc = SecondCard()
tc = ThirdCard()
foc = FourthCard()
fic = FifthCard()
fbc = FirstBotCard()
sbc = SecondBotCard()
tbc = ThirdBotCard()
fobc = FourthBotCard()
fibc = FifthBotCard()

running = True


while running:

    # a garder sinon une autre carte en + apparaît
    op.screen.fill((0, 204, 102))

    def piocheFirstCard():
        if piocher1 == 1:
            op.screen.blit(fc.card1, (fc.x1, fc.y1))
            fc.x1 = 100
            fc.rect1.x = fc.x1
        if piocher1 == 2:
            op.screen.blit(fc.card2, (fc.x2, fc.y2))
            fc.x2 = 100
            fc.rect2.x = fc.x2
        if piocher1 == 3:
            op.screen.blit(fc.card3, (fc.x3, fc.y3))
            fc.x3 = 100
            fc.rect3.x = fc.x3
        if piocher1 == 4:
            op.screen.blit(fc.card4, (fc.x4, fc.y4))
            fc.x4 = 100
            fc.rect4.x = fc.x4
        if piocher1 == 5:
            op.screen.blit(fc.card5, (fc.x5, fc.y5))
            fc.x5 = 100
            fc.rect5.x = fc.x5
        if piocher1 == 6:
            op.screen.blit(fc.card6, (fc.x6, fc.y6))
            fc.x6 = 100
            fc.rect6.x = fc.x6
        if piocher1 == 7:
            op.screen.blit(fc.card7, (fc.x7, fc.y7))
            fc.x7 = 100
            fc.rect7.x = fc.x7
        if piocher1 == 8:
            op.screen.blit(fc.card8, (fc.x8, fc.y8))
            fc.x8 = 100
            fc.rect8.x = fc.x8
        if piocher1 == 9:
            op.screen.blit(fc.card9, (fc.x9, fc.y9))
            fc.x9 = 100
            fc.rect9.x = fc.x9
        if piocher1 == 10:
            op.screen.blit(fc.card10, (fc.x10, fc.y10))
            fc.x10 = 100
            fc.rect10.x = fc.x10

    def piocheSecondCard():
        if piocher2 == 1:
            op.screen.blit(sc.card1, (sc.x1, sc.y1))
            sc.x1 = 250
            sc.rect1.x = sc.x1
        if piocher2 == 2:
            op.screen.blit(sc.card2, (sc.x2, sc.y2))
            sc.x2 = 250
            sc.rect2.x = sc.x2
        if piocher2 == 3:
            op.screen.blit(sc.card3, (sc.x3, sc.y3))
            sc.x3 = 250
            sc.rect3.x = sc.x3
        if piocher2 == 4:
            op.screen.blit(sc.card4, (sc.x4, sc.y4))
            sc.x4 = 250
            sc.rect4.x = sc.x4
        if piocher2 == 5:
            op.screen.blit(sc.card5, (sc.x5, sc.y5))
            sc.x5 = 250
            sc.rect5.x = sc.x5
        if piocher2 == 6:
            op.screen.blit(sc.card6, (sc.x6, sc.y6))
            sc.x6 = 250
            sc.rect6.x = sc.x6
        if piocher2 == 7:
            op.screen.blit(sc.card7, (sc.x7, sc.y7))
            sc.x7 = 250
            sc.rect7.x = sc.x7
        if piocher2 == 8:
            op.screen.blit(sc.card8, (sc.x8, sc.y8))
            sc.x8 = 250
            sc.rect8.x = sc.x8
        if piocher2 == 9:
            op.screen.blit(sc.card9, (sc.x9, sc.y9))
            sc.x9 = 250
            sc.rect9.x = sc.x9
        if piocher2 == 10:
            op.screen.blit(sc.card10, (sc.x10, sc.y10))
            sc.x10 = 250
            sc.rect10.x = sc.x10

    def piocheThirdCard():
        if piocher3 == 1:
            op.screen.blit(tc.card1, (tc.x1, tc.y1))
            tc.x1 = 400
            tc.rect1.x = tc.x1
        if piocher3 == 2:
            op.screen.blit(tc.card2, (tc.x2, tc.y2))
            tc.x2 = 400
            tc.rect2.x = tc.x2
        if piocher3 == 3:
            op.screen.blit(tc.card3, (tc.x3, tc.y3))
            tc.x3 = 400
            tc.rect3.x = tc.x3
        if piocher3 == 4:
            op.screen.blit(tc.card4, (tc.x4, tc.y4))
            tc.x4 = 400
            tc.rect4.x = tc.x4
        if piocher3 == 5:
            op.screen.blit(tc.card5, (tc.x5, tc.y5))
            tc.x5 = 400
            tc.rect5.x = tc.x5
        if piocher3 == 6:
            op.screen.blit(tc.card6, (tc.x6, tc.y6))
            tc.x6 = 400
            tc.rect6.x = tc.x6
        if piocher3 == 7:
            op.screen.blit(tc.card7, (tc.x7, tc.y7))
            tc.x7 = 400
            tc.rect7.x = tc.x7
        if piocher3 == 8:
            op.screen.blit(tc.card8, (tc.x8, tc.y8))
            tc.x8 = 400
            tc.rect8.x = tc.x8
        if piocher3 == 9:
            op.screen.blit(tc.card9, (tc.x9, tc.y9))
            tc.x9 = 400
            tc.rect9.x = tc.x9
        if piocher3 == 10:
            op.screen.blit(tc.card10, (tc.x10, tc.y10))
            tc.x10 = 400
            tc.rect10.x = tc.x10

    def piocheFourthCard():
        if piocher4 == 1:
            op.screen.blit(foc.card1, (foc.x1, foc.y1))
            foc.x1 = 550
            foc.rect1.x = foc.x1
        if piocher4 == 2:
            op.screen.blit(foc.card2, (foc.x2, foc.y2))
            foc.x2 = 550
            foc.rect2.x = foc.x2
        if piocher4 == 3:
            op.screen.blit(foc.card3, (foc.x3, foc.y3))
            foc.x3 = 550
            foc.rect3.x = foc.x3
        if piocher4 == 4:
            op.screen.blit(foc.card4, (foc.x4, foc.y4))
            foc.x4 = 550
            foc.rect4.x = foc.x4
        if piocher4 == 5:
            op.screen.blit(foc.card5, (foc.x5, foc.y5))
            foc.x5 = 550
            foc.rect5.x = foc.x5
        if piocher4 == 6:
            op.screen.blit(foc.card6, (foc.x6, foc.y6))
            foc.x6 = 550
            foc.rect6.x = foc.x6
        if piocher4 == 7:
            op.screen.blit(foc.card7, (foc.x7, foc.y7))
            foc.x7 = 550
            foc.rect7.x = foc.x7
        if piocher4 == 8:
            op.screen.blit(foc.card8, (foc.x8, foc.y8))
            foc.x8 = 550
            foc.rect8.x = foc.x8
        if piocher4 == 9:
            op.screen.blit(foc.card9, (foc.x9, foc.y9))
            foc.x9 = 550
            foc.rect9.x = foc.x9
        if piocher4 == 10:
            op.screen.blit(foc.card10, (foc.x10, foc.y10))
            foc.x10 = 550
            foc.rect10.x = foc.x10
    
    def piocheFifthCard():
        if piocher5 == 1:
            op.screen.blit(fic.card1, (fic.x1, fic.y1))
            fic.x1 = 700
            fic.rect1.x = fic.x1
        if piocher5 == 2:
            op.screen.blit(fic.card2, (fic.x2, fic.y2))
            fic.x2 = 700
            fic.rect2.x = fic.x2
        if piocher5 == 3:
            op.screen.blit(fic.card3, (fic.x3, fic.y3))
            fic.x3 = 700
            fic.rect3.x = fic.x3
        if piocher5 == 4:
            op.screen.blit(fic.card4, (fic.x4, fic.y4))
            fic.x4 = 700
            fic.rect4.x = fic.x4
        if piocher5 == 5:
            op.screen.blit(fic.card5, (fic.x5, fic.y5))
            fic.x5 = 700
            fic.rect5.x = fic.x5
        if piocher5 == 6:
            op.screen.blit(fic.card6, (fic.x6, fic.y6))
            fic.x6 = 700
            fic.rect6.x = fic.x6
        if piocher5 == 7:
            op.screen.blit(fic.card7, (fic.x7, fic.y7))
            fic.x7 = 700
            fic.rect7.x = fic.x7
        if piocher5 == 8:
            op.screen.blit(fic.card8, (fic.x8, fic.y8))
            fic.x8 = 700
            fic.rect8.x = fic.x8
        if piocher5 == 9:
            op.screen.blit(fic.card9, (fic.x9, fic.y9))
            fic.x9 = 700
            fic.rect9.x = fic.x9
        if piocher5 == 10:
            op.screen.blit(fic.card10, (fic.x10, fic.y10))
            fic.x10 = 700
            fic.rect10.x = fic.x10

    def piocheAllPlayerCards():
        piocheFirstCard()
        piocheSecondCard()
        piocheThirdCard()
        piocheFourthCard()
        piocheFifthCard()

    piocheAllPlayerCards()

    def piocheFirstCardBot():
        if piocher1bot == 1:
            op.screen.blit(fbc.card1, (fbc.x1, fbc.y1))
            fbc.x1 = 100
            fbc.y1 = 300
            fbc.rect1.x = fbc.x1
        if piocher1bot == 2:
            op.screen.blit(fbc.card2, (fbc.x2, fbc.y2))
            fbc.x2 = 100
            fbc.y2 = 300
            fbc.rect2.x = fbc.x2
        if piocher1bot == 3:
            op.screen.blit(fbc.card3, (fbc.x3, fbc.y3))
            fbc.x3 = 100
            fbc.y3 = 300
            fbc.rect3.x = fbc.x3
        if piocher1bot == 4:
            op.screen.blit(fbc.card4, (fbc.x4, fbc.y4))
            fbc.x4 = 100
            fbc.y4 = 300
            fbc.rect4.x = fbc.x4
        if piocher1bot == 5:
            op.screen.blit(fbc.card5, (fbc.x5, fbc.y5))
            fbc.x5 = 100
            fbc.y5 = 300
            fbc.rect5.x = fbc.x5
        if piocher1bot == 6:
            op.screen.blit(fbc.card6, (fbc.x6, fbc.y6))
            fbc.x6 = 100
            fbc.y6 = 300
            fbc.rect6.x = fbc.x6
        if piocher1bot == 7:
            op.screen.blit(fbc.card7, (fbc.x7, fbc.y7))
            fbc.x7 = 100
            fbc.y7 = 300
            fbc.rect7.x = fbc.x7
        if piocher1bot == 8:
            op.screen.blit(fbc.card8, (fbc.x8, fbc.y8))
            fbc.x8 = 100
            fbc.y8 = 300
            fbc.rect8.x = fbc.x8
        if piocher1bot == 9:
            op.screen.blit(fbc.card9, (fbc.x9, fbc.y9))
            fbc.x9 = 100
            fbc.y9 = 300
            fbc.rect9.x = fbc.x9
        if piocher1bot == 10:
            op.screen.blit(fbc.card10, (fbc.x10, fbc.y10))
            fbc.x10 = 100
            fbc.y10 = 300
            fbc.rect10.x = fbc.x10

    def piocheSecondCardBot():
        if piocher2bot == 1:
            op.screen.blit(sbc.card1, (sbc.x1, sbc.y1))
            sbc.x1 = 250
            sbc.y1 = 300
            sbc.rect1.x = sbc.x1
        if piocher2bot == 2:
            op.screen.blit(sbc.card2, (sbc.x2, sbc.y2))
            sbc.x2 = 250
            sbc.y2 = 300
            sbc.rect2.x = sbc.x2
        if piocher2bot == 3:
            op.screen.blit(sbc.card3, (sbc.x3, sbc.y3))
            sbc.x3 = 250
            sbc.y3 = 300
            sbc.rect3.x = sbc.x3
        if piocher2bot == 4:
            op.screen.blit(sbc.card4, (sbc.x4, sbc.y4))
            sbc.x4 = 250
            sbc.y4 = 300
            sbc.rect4.x = sbc.x4
        if piocher2bot == 5:
            op.screen.blit(sbc.card5, (sbc.x5, sbc.y5))
            sbc.x5 = 250
            sbc.y5 = 300
            sbc.rect5.x = sbc.x5
        if piocher2bot == 6:
            op.screen.blit(sbc.card6, (sbc.x6, sbc.y6))
            sbc.x6 = 250
            sbc.y6 = 300
            sbc.rect6.x = sbc.x6
        if piocher2bot == 7:
            op.screen.blit(sbc.card7, (sbc.x7, sbc.y7))
            sbc.x7 = 250
            sbc.y7 = 300
            sbc.rect7.x = sbc.x7
        if piocher2bot == 8:
            op.screen.blit(sbc.card8, (sbc.x8, sbc.y8))
            sbc.x8 = 250
            sbc.y8 = 300
            sbc.rect8.x = sbc.x8
        if piocher2bot == 9:
            op.screen.blit(sbc.card9, (sbc.x9, sbc.y9))
            sbc.x9 = 250
            sbc.y9 = 300
            sbc.rect9.x = sbc.x9
        if piocher2bot == 10:
            op.screen.blit(sbc.card10, (sbc.x10, sbc.y10))
            sbc.x10 = 250
            sbc.y10 = 300
            sbc.rect10.x = sbc.x10

    def piocheThirdCardBot():
        if piocher3bot == 1:
            op.screen.blit(tbc.card1, (tbc.x1, tbc.y1))
            tbc.x1 = 400
            tbc.y1 = 300
            tbc.rect1.x = tbc.x1
        if piocher3bot == 2:
            op.screen.blit(tbc.card2, (tbc.x2, tbc.y2))
            tbc.x2 = 400
            tbc.y2 = 300
            tbc.rect2.x = tbc.x2
        if piocher3bot == 3:
            op.screen.blit(tbc.card3, (tbc.x3, tbc.y3))
            tbc.x3 = 400
            tbc.y3 = 300
            tbc.rect3.x = tbc.x3
        if piocher3bot == 4:
            op.screen.blit(tbc.card4, (tbc.x4, tbc.y4))
            tbc.x4 = 400
            tbc.y4 = 300
            tbc.rect4.x = tbc.x4
        if piocher3bot == 5:
            op.screen.blit(tbc.card5, (tbc.x5, tbc.y5))
            tbc.x5 = 400
            tbc.y5 = 300
            tbc.rect5.x = tbc.x5
        if piocher3bot == 6:
            op.screen.blit(tbc.card6, (tbc.x6, tbc.y6))
            tbc.x6 = 400
            tbc.y6 = 300
            tbc.rect6.x = tbc.x6
        if piocher3bot == 7:
            op.screen.blit(tbc.card7, (tbc.x7, tbc.y7))
            tbc.x7 = 400
            tbc.y7 = 300
            tbc.rect7.x = tbc.x7
        if piocher3bot == 8:
            op.screen.blit(tbc.card8, (tbc.x8, tbc.y8))
            tbc.x8 = 400
            tbc.y8 = 300
            tbc.rect8.x = tbc.x8
        if piocher3bot == 9:
            op.screen.blit(tbc.card9, (tbc.x9, tbc.y9))
            tbc.x9 = 400
            tbc.y9 = 300
            tbc.rect9.x = tbc.x9
        if piocher3bot == 10:
            op.screen.blit(tbc.card10, (tbc.x10, tbc.y10))
            tbc.x10 = 400
            tbc.y10 = 300
            tbc.rect10.x = tbc.x10

    def piocheFourthCardBot():
        if piocher4bot == 1:
            op.screen.blit(fobc.card1, (fobc.x1, fobc.y1))
            fobc.x1 = 550
            fobc.y1 = 300
            fobc.rect1.x = fobc.x1
        if piocher4bot == 2:
            op.screen.blit(fobc.card2, (fobc.x2, fobc.y2))
            fobc.x2 = 550
            fobc.y2 = 300
            fobc.rect2.x = fobc.x2
        if piocher4bot == 3:
            op.screen.blit(fobc.card3, (fobc.x3, fobc.y3))
            fobc.x3 = 550
            fobc.y3 = 300
            fobc.rect3.x = fobc.x3
        if piocher4bot == 4:
            op.screen.blit(fobc.card4, (fobc.x4, fobc.y4))
            fobc.x4 = 550
            fobc.y4 = 300
            fobc.rect4.x = fobc.x4
        if piocher4bot == 5:
            op.screen.blit(fobc.card5, (fobc.x5, fobc.y5))
            fobc.x5 = 550
            fobc.y5 = 300
            fobc.rect5.x = fobc.x5
        if piocher4bot == 6:
            op.screen.blit(fobc.card6, (fobc.x6, fobc.y6))
            fobc.x6 = 550
            fobc.y6 = 300
            fobc.rect6.x = fobc.x6
        if piocher4bot == 7:
            op.screen.blit(fobc.card7, (fobc.x7, fobc.y7))
            fobc.x7 = 550
            fobc.y7 = 300
            fobc.rect7.x = fobc.x7
        if piocher4bot == 8:
            op.screen.blit(fobc.card8, (fobc.x8, fobc.y8))
            fobc.x8 = 550
            fobc.y8 = 300
            fobc.rect8.x = fobc.x8
        if piocher4bot == 9:
            op.screen.blit(fobc.card9, (fobc.x9, fobc.y9))
            fobc.x9 = 550
            fobc.y9 = 300
            fobc.rect9.x = fobc.x9
        if piocher4bot == 10:
            op.screen.blit(fobc.card10, (fobc.x10, fobc.y10))
            fobc.x10 = 550
            fobc.y10 = 300
            fobc.rect10.x = fobc.x10
    
    def piocheFifthCardBot():
        if piocher5bot == 1:
            op.screen.blit(fibc.card1, (fibc.x1, fibc.y1))
            fibc.x1 = 700
            fibc.y1 = 300
            fibc.rect1.x = fibc.x1
        if piocher5bot == 2:
            op.screen.blit(fibc.card2, (fibc.x2, fibc.y2))
            fibc.x2 = 700
            fibc.y2 = 300
            fibc.rect2.x = fibc.x2
        if piocher5bot == 3:
            op.screen.blit(fibc.card3, (fibc.x3, fibc.y3))
            fibc.x3 = 700
            fibc.y3 = 300
            fibc.rect3.x = fibc.x3
        if piocher5bot == 4:
            op.screen.blit(fibc.card4, (fibc.x4, fibc.y4))
            fibc.x4 = 700
            fibc.y4 = 300
            fibc.rect4.x = fibc.x4
        if piocher5bot == 5:
            op.screen.blit(fibc.card5, (fibc.x5, fibc.y5))
            fibc.x5 = 700
            fibc.y5 = 300
            fibc.rect5.x = fibc.x5
        if piocher5bot == 6:
            op.screen.blit(fibc.card6, (fibc.x6, fibc.y6))
            fibc.x6 = 700
            fibc.y6 = 300
            fibc.rect6.x = fibc.x6
        if piocher5bot == 7:
            op.screen.blit(fibc.card7, (fibc.x7, fibc.y7))
            fibc.x7 = 700
            fibc.y7 = 300
            fibc.rect7.x = fibc.x7
        if piocher5bot == 8:
            op.screen.blit(fibc.card8, (fibc.x8, fibc.y8))
            fibc.x8 = 700
            fibc.y8 = 300
            fibc.rect8.x = fibc.x8
        if piocher5bot == 9:
            op.screen.blit(fibc.card9, (fibc.x9, fibc.y9))
            fibc.x9 = 700
            fibc.y9 = 300
            fibc.rect9.x = fibc.x9
        if piocher5bot == 10:
            op.screen.blit(fibc.card10, (fibc.x10, fibc.y10))
            fibc.x10 = 700
            fibc.y1 = 300
            fibc.rect10.x = fibc.x10

    def piocheAllBotCards():
    	piocheFirstCardBot()
    	piocheSecondCardBot()
    	piocheThirdCardBot()
    	piocheFourthCardBot()
    	piocheFifthCardBot()

    piocheAllBotCards()

    mouse = pygame.mouse.get_pos()

    def checkIfMouseOnCard1():
        if fc.rect1.collidepoint(mouse) and mouse_pressed:
        	   fc.x1 = 800
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