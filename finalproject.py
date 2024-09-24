#Authors: Bryan Soares & Elijah Avri

#importing os
import os


#Importing pygame
import pygame
pygame.init()

#setting root path

RootPath = os.path.dirname(__file__)

#Window screen setup 

WindowScreen = pygame.display.set_mode((480,720))
pygame.display.set_caption("Bootleg Flappy")


#Background Image Setup
LoadImage = os.path.join(RootPath, 'assets' , 'SkyAsset.png')
Background = pygame.image.load(LoadImage)



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.display.update()


