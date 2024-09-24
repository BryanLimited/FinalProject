#Authors: Bryan Soares & Elijah Avri

#importing os
import os


#Importing pygame
import pygame
pygame.init()

#setting root path for Python 

RootPath = os.path.join(os.path.dirname(os.path.abspath(__file__)))


#Window screen setup 
WindowScreen = pygame.display.set_mode((480,720))
pygame.display.set_caption("Final project - Flappy Bird")

print("Current Working Directory:", os.getcwd())

#Background Image Setup
Background = pygame.image.load(os.path.join(RootPath, 'SkyAsset.png'))

#Setting mouse cursor
pygame.mouse.set_cursor(*pygame.cursors.arrow)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      

      
      pygame.display.update()

