import pygame
from instantiateCards import *

def definePositions():

	#Cartes joueur x
	fc.x = 100
	sc.x = 250
	tc.x = 400
	foc.x = 550
	fic.x = 700

	fc.rect.x = fc.x
	sc.rect.x = sc.x
	tc.rect.x = tc.x
	foc.rect.x = foc.x
	fic.rect.x = fic.x

	#Cartes joueur y
	fc.y = 495
	sc.y = 495
	tc.y = 495
	foc.y = 495
	fic.y = 495

	fc.rect.y = fc.y
	sc.rect.y = sc.y
	tc.rect.y = tc.y
	foc.rect.y = foc.y
	fic.rect.y = fic.y

	#Cartes bot x
	fbc.x = 100
	sbc.x = 250
	tbc.x = 400
	fobc.x = 550
	fibc.x = 700

	#Cartes bot y
	fbc.y = -15
	sbc.y = -15
	tbc.y = -15
	fobc.y = -15
	fibc.y = -15