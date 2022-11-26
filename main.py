import pygame
import random
from FirstCard import FirstCard
from SecondCard import SecondCard
from ThirdCard import ThirdCard
from FourthCard import FourthCard
from FifthCard import FifthCard
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyStrat")

piocher1 = random.randint(1, 10)
piocher2 = random.randint(1, 10)
piocher3 = random.randint(1, 10)
piocher4 = random.randint(1, 10)
piocher5 = random.randint(1, 10)

fc = FirstCard()
sc = SecondCard()
tc = ThirdCard()
foc = FourthCard()
fic = FifthCard()

running = True


while running:

    if piocher1 == 1:
        screen.blit(fc.card1, (100, 100))
    if piocher1 == 2:
        screen.blit(fc.card2, (100, 100))
    if piocher1 == 3:
        screen.blit(fc.card3, (100, 100))
    if piocher1 == 4:
        screen.blit(fc.card4, (100, 100))
    if piocher1 == 5:
        screen.blit(fc.card5, (100, 100))
    if piocher1 == 6:
        screen.blit(fc.card6, (100, 100))
    if piocher1 == 7:
        screen.blit(fc.card7, (100, 100))
    if piocher1 == 8:
        screen.blit(fc.card8, (100, 100))
    if piocher1 == 9:
        screen.blit(fc.card9, (100, 100))
    if piocher1 == 10:
        screen.blit(fc.card10, (100, 100))

    if piocher2 == 1:
        screen.blit(sc.card1, (250, 100))
    if piocher2 == 2:
        screen.blit(sc.card2, (250, 100))
    if piocher2 == 3:
        screen.blit(sc.card3, (250, 100))
    if piocher2 == 4:
        screen.blit(sc.card4, (250, 100))
    if piocher2 == 5:
        screen.blit(sc.card5, (250, 100))
    if piocher2 == 6:
        screen.blit(sc.card6, (250, 100))
    if piocher2 == 7:
        screen.blit(sc.card7, (250, 100))
    if piocher2 == 8:
        screen.blit(sc.card8, (250, 100))
    if piocher2 == 9:
        screen.blit(sc.card9, (250, 100))
    if piocher2 == 10:
        screen.blit(sc.card10, (250, 100))

    if piocher3 == 1:
        screen.blit(tc.card1, (400, 100))
    if piocher3 == 2:
        screen.blit(tc.card2, (400, 100))
    if piocher3 == 3:
        screen.blit(tc.card3, (400, 100))
    if piocher3 == 4:
        screen.blit(tc.card4, (400, 100))
    if piocher3 == 5:
        screen.blit(tc.card5, (400, 100))
    if piocher3 == 6:
        screen.blit(tc.card6, (400, 100))
    if piocher3 == 7:
        screen.blit(tc.card7, (400, 100))
    if piocher3 == 8:
        screen.blit(tc.card8, (400, 100))
    if piocher3 == 9:
        screen.blit(tc.card9, (400, 100))
    if piocher3 == 10:
        screen.blit(tc.card10, (400, 100))

    if piocher4 == 1:
        screen.blit(foc.card1, (550, 100))
    if piocher4 == 2:
        screen.blit(foc.card2, (550, 100))
    if piocher4 == 3:
        screen.blit(foc.card3, (550, 100))
    if piocher4 == 4:
        screen.blit(foc.card4, (550, 100))
    if piocher4 == 5:
        screen.blit(foc.card5, (550, 100))
    if piocher4 == 6:
        screen.blit(foc.card6, (550, 100))
    if piocher4 == 7:
        screen.blit(foc.card7, (550, 100))
    if piocher4 == 8:
        screen.blit(foc.card8, (550, 100))
    if piocher4 == 9:
        screen.blit(foc.card9, (550, 100))
    if piocher4 == 10:
        screen.blit(foc.card10, (550, 100))

    if piocher5 == 1:
        screen.blit(fic.card1, (700, 100))
    if piocher5 == 2:
        screen.blit(fic.card2, (700, 100))
    if piocher5 == 3:
        screen.blit(fic.card3, (700, 100))
    if piocher5 == 4:
        screen.blit(fic.card4, (700, 100))
    if piocher5 == 5:
        screen.blit(fic.card5, (700, 100))
    if piocher5 == 6:
        screen.blit(fic.card6, (700, 100))
    if piocher5 == 7:
        screen.blit(fic.card7, (700, 100))
    if piocher5 == 8:
        screen.blit(fic.card8, (700, 100))
    if piocher5 == 9:
        screen.blit(fic.card9, (700, 100))
    if piocher5 == 10:
        screen.blit(fic.card10, (700, 100))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
