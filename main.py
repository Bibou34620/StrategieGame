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
        screen.blit(fc.card1, (100, 100))
    if piocher2 == 2:
        screen.blit(fc.card2, (100, 100))
    if piocher2 == 3:
        screen.blit(fc.card3, (100, 100))
    if piocher2 == 4:
        screen.blit(fc.card4, (100, 100))
    if piocher2 == 5:
        screen.blit(fc.card5, (100, 100))
    if piocher2 == 6:
        screen.blit(fc.card6, (100, 100))
    if piocher2 == 7:
        screen.blit(fc.card7, (100, 100))
    if piocher2 == 8:
        screen.blit(fc.card8, (100, 100))
    if piocher2 == 9:
        screen.blit(fc.card9, (100, 100))
    if piocher2 == 10:
        screen.blit(fc.card10, (100, 100))

    if piocher3 == 1:
        screen.blit(fc.card1, (100, 100))
    if piocher3 == 2:
        screen.blit(fc.card2, (100, 100))
    if piocher3 == 3:
        screen.blit(fc.card3, (100, 100))
    if piocher3 == 4:
        screen.blit(fc.card4, (100, 100))
    if piocher3 == 5:
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

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
