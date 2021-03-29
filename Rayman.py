# Tutoriel que je suis (Graven) = https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR
# Site pour avoir pleins de sprites = https://www.spriters-resource.com/

import sys
import pygame 

pygame.init()

# Création d'une classe pour le joueur :

class Player(pygame.sprite.Sprite) :
	def __init__(self) :
# = Insertion de différents attributs concernant la classe "Player"

		super().__init__() 
		self.health = 3
		self.max_health = 5
		self.attack = 1
		self.speed = 5
		self.image = pygame.image.load('Persos/Joueur/NoRay.png') #Chargement de l'image du joueur
		self.rect = self.image.get_rect()
		
# Générer fenêtre de jeu :

pygame.display.set_caption("Rayman Rev1val")  # display = affichage, set_caption = titre(s)
screen = pygame.display.set_mode((1080, 720)) # set_mode = affichage de la fenêtre (taille)

# Importer images : 

background = pygame.image.load('Background/LotLD.jpg') # Attribution d'une image à la variable 'background'


running = True # running = Nom de la boucle while ? While ne marche pas toute seule, booléen strict minimum

while running == True :

	# Application image arrière-plan ( affichage ) :
	screen.blit(background, (0, 0))

    #Affichage joueur :
	screen.blit(Player.image, Player.rect)

	#MAJ ecran :
	pygame.display.flip()

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			running == False
			pygame.quit()   # Ferme la fenêtre lorsqu'on clique sur la croix (croix marche pas sans cette ligne)

 
