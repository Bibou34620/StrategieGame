from BotCard import BotCard
from instantiateCards import *

def hideBotCards():
    if fbc.x == 100 and fbc.y == -15:
        fbc.image = fbc.hidedCard
    else:
        fbc.image = fbc.card

    if sbc.x == 250 and sbc.y == -15:
        sbc.image = sbc.hidedCard
    else:
        sbc.image = sbc.card 

    if tbc.x == 400 and tbc.y == -15:
        tbc.image = tbc.hidedCard
    else:
        fbc.image = tbc.card 

    if fobc.x == 550 and fobc.y == -15:
        fobc.image = fobc.hidedCard
    else:
        fobc.image = fobc.card

    if fibc.x == 700 and fibc.y == -15:
        fibc.image = fibc.hidedCard
    else:
        fibc.image = fibc.card  

