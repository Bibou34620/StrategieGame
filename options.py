import pygame

class Options:
	def __init__(self):
		self.screen = pygame.display.set_mode((1000, 600))
		self.title = pygame.display.set_caption("PyStrat")