#Authors: Bryan Soares & Elijah Avri

#importing os
import os


#Importing pygame
import pygame
pygame.init()

#setting root path for Python 
RootPath = os.path.join(os.path.dirname(os.path.realpath(__file__)))
#Window screen setup 
WindowScreen = pygame.display.set_mode((480,720))
pygame.display.set_caption("Bootleg Flappy")


#Background Image Setup
Background = pygame.image.load(os.path.join(RootPath,'Download','assets', 'SkyAsset.png'))



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      

      
      pygame.display.update()


