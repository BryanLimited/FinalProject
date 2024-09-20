#Authors: Bryan Soares & Elijah Avri


#Importing pygame
import pygame
pygame.init()



#Window screen setup 
WindowScreen = pygame.display.set_mode((1980,1080))
pygame.display.set_caption("Bootleg Flappy")



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

