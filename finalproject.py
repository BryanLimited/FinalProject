#Authors: Bryan Soares & Elijah Avri


#Importing pygame
import pygame
pygame.init()



#Window screen setup 
WindowScreen = pygame.display.set_mode((480,720))
pygame.display.set_caption("Bootleg Flappy")


#Background Image Setup
Background = pygame.image.load(r'assets/SkyAsset.png')



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

      WindowScreen.blit(Background, (0, 0))
      
      pygame.display.update()


