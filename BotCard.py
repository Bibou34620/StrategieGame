import pygame

class FirstBotCard(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.card1 = pygame.image.load('cards/card1.png')
		self.card2 = pygame.image.load('cards/card2.png')
		self.card3 = pygame.image.load('cards/card3.png')
		self.card4 = pygame.image.load('cards/card4.png')
		self.card5 = pygame.image.load('cards/card5.png')
		self.card6 = pygame.image.load('cards/card6.png')
		self.card7 = pygame.image.load('cards/card7.png')
		self.card8 = pygame.image.load('cards/card8.png')
		self.card9 = pygame.image.load('cards/card9.png')
		self.card10 = pygame.image.load('cards/card10.png')

		self.card1 = pygame.transform.scale(self.card1, (90, 130))
		self.card2 = pygame.transform.scale(self.card2, (90, 130))
		self.card3 = pygame.transform.scale(self.card3, (90, 130))
		self.card4 = pygame.transform.scale(self.card4, (90, 130))
		self.card5 = pygame.transform.scale(self.card5, (90, 130))
		self.card6 = pygame.transform.scale(self.card6, (90, 130))
		self.card7 = pygame.transform.scale(self.card7, (90, 130))
		self.card8 = pygame.transform.scale(self.card8, (90, 130))
		self.card9 = pygame.transform.scale(self.card9, (90, 130))
		self.card10 = pygame.transform.scale(self.card10, (90, 130))

		self.rect1 = self.card1.get_rect()
		self.rect2 = self.card2.get_rect()
		self.rect3 = self.card3.get_rect()
		self.rect4 = self.card4.get_rect()
		self.rect5 = self.card5.get_rect()
		self.rect6 = self.card6.get_rect()
		self.rect7 = self.card7.get_rect()
		self.rect8 = self.card8.get_rect()
		self.rect9 = self.card9.get_rect()
		self.rect10 = self.card10.get_rect()

		self.x1 = self.card1.get_rect().x
		self.x2 = self.card2.get_rect().x
		self.x3 = self.card3.get_rect().x
		self.x4 = self.card4.get_rect().x
		self.x5 = self.card5.get_rect().x
		self.x6 = self.card6.get_rect().x
		self.x7 = self.card7.get_rect().x
		self.x8 = self.card8.get_rect().x
		self.x9 = self.card9.get_rect().x
		self.x10 = self.card10.get_rect().x

		self.y1 = self.card1.get_rect().y
		self.y2 = self.card2.get_rect().y
		self.y3 = self.card3.get_rect().y
		self.y4 = self.card4.get_rect().y
		self.y5 = self.card5.get_rect().y
		self.y6 = self.card6.get_rect().y
		self.y7 = self.card7.get_rect().y
		self.y8 = self.card8.get_rect().y
		self.y9 = self.card9.get_rect().y
		self.y10 = self.card10.get_rect().y