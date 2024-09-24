#Authors: Bryan Soares & Elijah Avri

#importing os
import os


#Importing pygame
import pygame
pygame.init()

#setting root path for Python 
home_directory = os.path.expanduser("~")


#Window screen setup 
WindowScreen = pygame.display.set_mode((480,720))
pygame.display.set_caption("Final project - Flappy Bird")

print("Current Working Directory:", os.getcwd())

#Background Image Setup
Background = pygame.image.load(os.path.join(home_directory, 'Downloads','FinalProject-main.zip', 'FinalProject-main', 'assets', 'SkyAsset.png'))
#Example to get the lazy way -- -- -- -- C:\Users\Bryan\Downloads\FinalProject-main.zip\FinalProject-main\assets





#Setting mouse cursor
pygame.mouse.set_cursor(*pygame.cursors.arrow)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      

      
      pygame.display.update()

