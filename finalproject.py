#Authors: Bryan Soares & Elijah Avri


import os
import sys
from pathlib import Path


#Importing pygame
import pygame
pygame.init()

#Calling path 
FolderPath = os.path.abspath(sys.argv[0])
RootPath = os.path.dirname(FolderPath)

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
    WindowScreen.blit(Background, (0,0))
      