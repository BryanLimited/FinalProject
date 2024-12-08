#Authors: Bryan Soares & Elijah Avril



#Importing pygame
import pygame
pygame.init()



#Importing to call Paths
import os
import sys
from pathlib import Path
import random


#Calling folder path 
FolderPath = os.path.abspath(sys.argv[0])
RootPath = os.path.dirname(FolderPath)


#Window screen setup 
WindowScreen = pygame.display.set_mode((480,720))
pygame.display.set_caption("Flappy Bird")


## - - - - - - - - - - - -Assets/Images calling  - - - - - - - - - - - - - - - - - - - - -

LoadImage = os.path.join(RootPath, 'assets' , 'SkyAsset.png') #SkyAsset
Background = pygame.image.load(LoadImage)

NightImage = os.path.join(RootPath, 'assets' , 'NightAsset.png') #NightAsset
Night = pygame.image.load(NightImage)

LoadPLayer = os.path.join(RootPath, 'assets', 'PlayerBird.png') #Player bird asset
Player = pygame.image.load(LoadPLayer)

PipeImageLoad = os.path.join(RootPath, 'assets', 'NewPipe1.png') #Pipe asset
PipeImage = pygame.image.load(PipeImageLoad)

BaseImageLoad = os.path.join(RootPath, 'assets', 'base.png') #Floor asset 
BaseFloor = pygame.image.load(BaseImageLoad)

#- - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



# - - - - - - - - - - - - - - - - - - - Image/Assets setup - - - - - - - - - - - - - - - - - - - - - - - -

class Bird():
    WIDTH = HEIGHT = 32
    def __init__(self): #Scales player image, sets the position and gravity, velocity, etc.
        self.image = pygame.transform.scale(Player, (50, 35))
        self.x = 20
        self.y = WindowScreen.get_height() / 2 - self.image.get_height() / 2
        self.rect = self.image.get_rect() 
        self.rect.x = 20
        self.rect.y = WindowScreen.get_height() / 2 - self.image.get_height() / 2
        self.gravity = 0.5 
        self.jump_strength = -8
        self.velocity = 0
    
    def update(self): # Updates position to apply the correct gravity and velocity on player
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect = self.image.get_rect()
        self.rect.y = self.y
        
        if self.y > WindowScreen.get_height() - BaseFloor.get_height() - self.image.get_height():
            self.y = WindowScreen.get_height() - BaseFloor.get_height() - self.image.get_height()
            self.velocity = 0
            
        if self.y < 0:
            self.y = 0

    

class Pipe(): 
    def __init__(self, x, y):
        self.image = pygame.transform.scale(PipeImage, (100 , 200))
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y= y
      
    
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x -10
        if self.x < -self.width:
            self.x = 450
            self.y = 500
            self.rect.y = self.y -10
            self.image = pygame.transform.scale(PipeImage, (100 , random.randint(100,240)))
            self.width = self.image.get_width()
            self.height = self.image.get_height()


class InvertedPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.flip(self.image,False, True)
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x -10
        if self.x < -self.width:
            self.x = 450
            self.y = 0
            self.image = pygame.transform.scale(self.image, (100 , random.randint(100,240)))
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect = self.image.get_rect()
            self.rect.y = self.y - 10 
        
        
        


def game_over():
    font = pygame.font.SysFont('Arial', 36)
    text = font.render("Game Over!", True, (255, 0, 0))
    WindowScreen.blit(text, (WindowScreen.get_width() // 3, WindowScreen.get_height() // 3))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()


def check_collision(bird, pipe): 
    if bird.rect.colliderect(pipe):
        game_over()
        
def speed_up(count, pipe):
    if count >= 10:
        pipe.speed == 4
    elif count >= 20:
        pipe.speed == 6
        
def show_text(count):
    font = pygame.font.SysFont('Arial', 36)
    text = font.render(str(count), True, (255,0,0))
    textRect = text.get_rect()
    textRect.center = (250, 250)
    WindowScreen.blit(text,textRect)
    pygame.display.update()

bird = Bird() 
pipe1 = Pipe(300, 400)
pipe2 = InvertedPipe(300,0)




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# - - - -Floor base position and speed - - -

base_speed = 3
base_x = 1

#- - - - - - - - - - - - - - - - - - - - - -


#Pygame application running 
running = True
score_counter = 0
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN: #User inputs and what happens when you press space
            if event.key == pygame.K_SPACE:
                bird.velocity = bird.jump_strength

    bird.update() # Updates position of player
    # if bird.y ==  WindowScreen.get_height() - BaseFloor.get_height() - bird.image.get_height():
    #     game_over()
    check_collision(bird, pipe1)
    check_collision(bird,pipe2)
    base_x -= base_speed #Sets floor speed and position and moves it
    if base_x <= -WindowScreen.get_width():
        base_x = 0


    if bird.x == pipe1.x: 
            score_counter += 1 
            print(score_counter)
            print(f'{bird.x} + {pipe1.x}')
        
    show_text(score_counter)

    if score_counter >= 0: 
        WindowScreen.blit(Background, (0, 0)) 
    if score_counter >= 3:
        pipe1.speed = 2
        pipe2.speed = 2
    if score_counter >= 5:
        pipe1.speed = 3
        pipe2.speed = 3
        WindowScreen.blit(Night, (0,0))
    if score_counter >= 5:
        pipe1.speed = 5
        pipe2.speed = 5
    if score_counter >= 10:
        pipe1.speed = 6
        pipe2.speed = 6
        WindowScreen.blit(Night, (0,0))
    
   

    pipe1.update()
    pipe2.update()

        
        

#----- Setting Position of the background, player, and floor - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    WindowScreen.blit(bird.image, (bird.x, bird.y)) 
    WindowScreen.blit(BaseFloor, (base_x, WindowScreen.get_height() - BaseFloor.get_height()))
    WindowScreen.blit(BaseFloor, (base_x + WindowScreen.get_width(), WindowScreen.get_height() - BaseFloor.get_height()))
    WindowScreen.blit(BaseFloor, (base_x + 300,608.8)) #Overlap
    WindowScreen.blit(BaseFloor, (base_x + 700,608.8)) #Overlap
    WindowScreen.blit(pipe1.image, (pipe1.x, pipe1.y))
    WindowScreen.blit(pipe2.image, (pipe2.x, pipe2.y))
    

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    pygame.display.update() #Updates the display

pygame.quit()
 