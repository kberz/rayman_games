# Tutoriel que je suis (Graven) = https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR
# Site pour avoir pleins de sprites = https://www.spriters-resource.com/

import sys
import pygame
from pygame.locals import *

pygame.init()
# Création d'une classe pour le joueur :


"""  					La class ne marche pas pour l'instant, 
				le sprite du perso a été injectée en dehors de la class
				   				  Class = Objets 
"""

class Player(pygame.sprite.Sprite) :
	def __init__(self) :
# = Insertion de différents attributs concernant la classe "Player"

		super().__init__() 
		self.health = 3
		self.max_health = 5
		self.attack = 1
		self.speed = 5
		self.image = pygame.image.load('Persos/Joueur/NoRay/NoRay.png') #Chargement de l'image du joueur
		self.rect = self.image.get_rect()
		
# Générer fenêtre de jeu :

pygame.display.set_caption("Rayman Rev1val")  # display = affichage, set_caption = titre(s)
screen = pygame.display.set_mode((1280, 520)) # set_mode = affichage de la fenêtre (taille)

# Importer images : 

background = pygame.image.load('Background/LotLD.jpg').convert() # Attribution d'une image à la variable 'background'

# Application image arrière-plan ( affichage ) :
screen.blit(background, (0, 0))

perso1 = pygame.image.load('Persos/Joueur/NoRay/NoRay.png') # déclaration image du perso

running = True # running = Nom de la boucle while ? While ne marche pas toute seule, booléen strict minimum

while running == True :

	#Affichage joueur :
	screen.blit(pygame.transform.scale(perso1,(90,90)), (120,370))

	# blit() = afficher image,         
	#(pygame.transform.scale(NomImage, (Taille, blit)), (, convertion) = changer taille et 

	#MAJ ecran :
	pygame.display.flip()

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			running == False
			pygame.quit()   # Ferme la fenêtre lorsqu'on clique sur la croix (croix marche pas sans cette ligne)

 
