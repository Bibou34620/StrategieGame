import pygame
import random

class BotCard(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.piocher = random.randint(1, 10)

		piocher_to_str = str(self.piocher)

		self.card = pygame.image.load(str('cards/card' + piocher_to_str + '.png'))

		self.hidedCard = pygame.image.load('cards/card_hided.png')

		self.hidedCard = pygame.transform.scale(self.hidedCard, (90, 130))

		self.card = pygame.transform.scale(self.card, (90, 130))
	
		self.image = self.hidedCard

		self.rect = self.card.get_rect()

		self.x = self.card.get_rect().x

		self.y = self.card.get_rect().y