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


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Music 

LoadSong =  os.path.join(RootPath, 'audio' , 'Happy Bird2.mp3')
pygame.mixer.music.load(LoadSong)
pygame.mixer.music.play(-1)

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

CollectibleImageLoad = os.path.join(RootPath, 'assets', 'Power.png') #power asset
CollectibleImage = pygame.image.load(CollectibleImageLoad)

CollectibleImageLoad = os.path.join(RootPath, 'assets', 'Power2.png') #power2 asset
CollectibleImage = pygame.image.load(CollectibleImageLoad)

OrangeImageLoad = os.path.join(RootPath, 'assets', 'Power.png') #power2 asset
OrangeCollectibleImage = pygame.image.load(OrangeImageLoad)
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
        self.gravity = 0.3
        self.jump_strength = -6
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
        self.speed = 1.5
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y= y
      
    
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x 
        if self.x < -self.width:
            self.x = 450
            self.y = 500
            self.image = pygame.transform.scale(PipeImage, (100 , random.randint(100,240)))
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect.y = self.y -20


class InvertedPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.flip(self.image,False, True)
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x 
        if self.x < -self.width:
            self.x = 450
            self.y = 0
            self.image = pygame.transform.scale(self.image, (100 , random.randint(100,240)))
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect = self.image.get_rect()
            self.rect.y = self.y - 20

class Pickup(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = CollectibleImage
        self.speed = 1

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x 
        if self.x < -self.width:
            self.x = 650
            self.y = random.randint(0,400)
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect = self.image.get_rect()
            self.rect.y = self.y
        
        
class OrangePower(Pickup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = OrangeCollectibleImage
        self.speed = 1
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x 
        if self.x < -self.width:
            self.x = 650
            self.y = random.randint(0,400)
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect = self.image.get_rect()
            self.rect.y = self.y

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

def pickup_obtained(bird,collectible,count):
    if bird.rect.colliderect(collectible):
        count += 2
        collectible.x = 450
def speedupobtained(bird,orange,pipe, speed):
    if bird.rect.colliderect(orange.rect):
        speed += 5
        orange.x = 500
        orange.y = random.randint(-100,500)
        print(pipe.speed)
def update_speed(score_counter, orange_count):
    base_speed = 2  
    speed = base_speed + (score_counter // 10) 
    speed += orange_count * 0.1 
    return speed

        
def speed_up(count, pipe):
    if count >= 20:
        pipe.speed == 10
    elif 20 >= count >= 10:
        pipe.speed == 6
    print(pipe.speed)

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
Collectibles = Pickup(500, random.randint(0,400))
Orange = OrangePower(500,random.randint(-30,340))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# - - - -Floor base position and speed - - -

base_speed = 3
base_x = 1

#- - - - - - - - - - - - - - - - - - - - - -


#Pygame application running 
running = True
score_counter = 0
orange_count = 0
speed_value =2
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

    pipe1.update()
    pipe2.update()
    Collectibles.update()
    Orange.update()
    
    base_x -= base_speed #Sets floor speed and position and moves it
    if base_x <= -WindowScreen.get_width():
        base_x = 0
    


    if pipe1.x == 450:        #--- workaround
            score_counter += 1 
            print(score_counter)
            print(f'{bird.x} + {pipe1.x}')
    if bird.rect.colliderect(Collectibles):
        score_counter+= 2
        print(score_counter)
    else:
        print('nothing') #debug 
        

    print(pipe1.x)

    show_text(score_counter)

    pickup_obtained(bird,Collectibles,score_counter)
    if bird.rect.colliderect(Orange):
        orange_count += 1
        Orange.x = 500
        Orange.y = random.randint(-100,500)

    pipe1.speed = update_speed(score_counter,orange_count)
    pipe2.speed = pipe1.speed
# #-------- speed up - - - - - - - - -
#     if score_counter in range(0,20):
#         speed_value += .0005
#     elif score_counter in range(21,40):
#         speed_value +=.0007
#     elif score_counter in range(41,60):
#         speed_value += .0008
#     else:
#         speed_value = speed_value
    # if score_counter >= 0:
    #  WindowScreen.blit(Night, (0, 0)) 
    # if score_counter >= 5:
    #     pipe1.speed = 3
    #     pipe2.speed = 3
    # if score_counter >= 10:
    #     pipe1.speed = 4
    #     pipe2.speed = 4
    #     WindowScreen.blit(Night, (0, 0)) 
    # if score_counter >= 15:
    #     pipe1.speed = 6
    #     pipe2.speed = 6
    # if score_counter >= 25:
    #     pipe1.speed = 7
    #     pipe2.speed = 7
    # if score_counter >= 40:
    #     pipe1.speed = 9
    #     pipe2.speed = 9
    #     WindowScreen.blit(Background, (0, 0)) 


    
    

    pipe1.update()
    pipe2.update()
    Collectibles.update()
    Orange.update()

        
        

#----- Setting Position of the background, player, and floor - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    WindowScreen.blit(Night, (0, 0)) 
    WindowScreen.blit(bird.image, (bird.x, bird.y)) 
    WindowScreen.blit(BaseFloor, (base_x, WindowScreen.get_height() - BaseFloor.get_height()))
    WindowScreen.blit(BaseFloor, (base_x + WindowScreen.get_width(), WindowScreen.get_height() - BaseFloor.get_height()))
    WindowScreen.blit(BaseFloor, (base_x + 300,608.8)) #Overlap
    WindowScreen.blit(BaseFloor, (base_x + 700,608.8)) #Overlap
    WindowScreen.blit(pipe1.image, (pipe1.x, pipe1.y))
    WindowScreen.blit(pipe2.image, (pipe2.x, pipe2.y))
    WindowScreen.blit(Collectibles.image, (Collectibles.x,Collectibles.y))
    WindowScreen.blit(Orange.image, (Orange.x,Orange.y))

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    pygame.display.update() #Updates the display

pygame.quit()


 