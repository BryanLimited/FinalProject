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
pygame.display.set_caption("Flappy Bird")


## - - - - - - - - - - - -Image Class Setup - - - - - - - - - - - - - - - - - - - - -

LoadImage = os.path.join(RootPath, 'assets' , 'SkyAsset.png')
Background = pygame.image.load(LoadImage)

LoadPLayer = os.path.join(RootPath, 'assets', 'PlayerBird.png')
Player = pygame.image.load(LoadPLayer)

PipeImageLoad = os.path.join(RootPath, 'assets', 'Pipe.png')
PipeImage = pygame.image.load(PipeImageLoad)

BaseImageLoad = os.path.join(RootPath, 'assets', 'base.png')
BaseFloor = pygame.image.load(BaseImageLoad)

#- - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - Image Classes - - - - - - - - - - - - - - - - - - - - - - - -

class Bird:
    def __init__(self):
        self.image = pygame.transform.scale(Player, (50, 35))
        self.x = 50  
        self.y = WindowScreen.get_height() / 2 - self.image.get_height() / 2
        self.gravity = 0.5
        self.jump_strength = -10
        self.velocity = 0
    
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        
        if self.y > WindowScreen.get_height() - BaseFloor.get_height() - self.image.get_height():
            self.y = WindowScreen.get_height() - BaseFloor.get_height() - self.image.get_height()
            self.velocity = 0
            
        if self.y < 0:
            self.y = 0

bird = Bird()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - -Foor base position and speeed - - -
base_speed = 2
base_x = 0
#- - - - - - - - - - - - - - - - - - - - - -

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.velocity = bird.jump_strength

    bird.update()

    base_x -= base_speed
    if base_x <= -WindowScreen.get_width():
        base_x = 0

    WindowScreen.blit(Background, (0, 0))
    WindowScreen.blit(bird.image, (bird.x, bird.y))
    WindowScreen.blit(BaseFloor, (base_x, WindowScreen.get_height() - BaseFloor.get_height()))
    WindowScreen.blit(BaseFloor, (base_x + WindowScreen.get_width(), WindowScreen.get_height() - BaseFloor.get_height()))

    pygame.display.update()

pygame.quit()