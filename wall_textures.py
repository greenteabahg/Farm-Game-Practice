import pygame
import random 
from spritemechs import Spritesheet

pygame.init()

Hite = 480
Width = 640
FPS = 60

FramePerSec = pygame.time.Clock()

canvas = pygame.Surface((Width, Hite))
displaysurf = pygame.display.set_mode((Width, Hite))

running = True


######developing background of game#######
backdrop = Spritesheet('New Piskel.png')
corner = backdrop.get_sprite(0,0,32,32)
wall_BOT = backdrop.get_sprite(0,32,32,32)
floor = backdrop.get_sprite(32,64,32,32) 

elements = (corner, wall_BOT, floor)
#background making function##

def get_back():
    y = 0
    x = 0
    placehold = pygame.Surface((Width, Hite))
    while y < Hite and x < Width:
        while y < Hite:
            placehold.blit(random.choice(elements), (x,y))
            y += 32
            if y == Hite:
                x += 32
                y = 0
                break
    return placehold
##Movement??##

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,33,33))
        self.rect = self.surf.get_rect()
         

   

back = get_back()
P1 = Player() 


#####Game Loop##########
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    canvas.fill((0,0,0))
    canvas.blit(back, (0,0))
    displaysurf.blit(canvas, (0,0))
    
    pygame.display.update()