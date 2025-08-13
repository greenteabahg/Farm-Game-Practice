import pygame
import random 
from spritemechs import Spritesheet
from procedural_gen import mat_gen 

pygame.init()

Hite = 480
Width = 640
FPS = 60

FramePerSec = pygame.time.Clock()

canvas = pygame.Surface((Width, Hite))
displaysurf = pygame.display.set_mode((Width, Hite), pygame.SCALED)

running = True

########################################################################################
####################                   #################################################
####################     BACKGROUND    #################################################
####################                   #################################################
########################################################################################
##   NOTES: 
##      Below I am pulling all of my background sprites from 'New Piskel.png' using the 
##      class Spritesheet I put in spritemechs.py 
##      There is only one corner pixel image, so I rotated the other three to create the
##      the rest.
##
##      Now, I am trying to make a procedural generator that will take a matrix for 
##      the screen (20 32x32 tiles by 15 32x32 tiles) and by assigning each type of
##      tile a number, generating the background based off of that. These could be static
##      and then scaled for the screen. (So no matter what, the ratio is always 20x15)

#           All background sprites
backdrop = Spritesheet('EZ_Piskel.png')

wall_TOP = backdrop.get_sprite(64,0,32,32)
wall_BOT = backdrop.get_sprite(0,32,32,32)
wall_LEFT = backdrop.get_sprite(32,32,32,32)
wall_RIGHT = backdrop.get_sprite(64,32,32,32)

wall_FULL = backdrop.get_sprite(32,0,32,32)


floor = backdrop.get_sprite(32,64,32,32) 

corner_RN = backdrop.get_sprite(0,0,32,32)
corner_LN = pygame.transform.rotate(corner_RN, 90)
corner_LS = pygame.transform.rotate(corner_RN, 180)
corner_RS = pygame.transform.rotate(corner_RN, 270)



elements = (floor, wall_TOP, wall_BOT, wall_LEFT, wall_RIGHT, corner_LN, corner_RN,
 corner_RS, corner_LS, wall_FULL)


#background making function##

def parse_mat():
    mat = mat_gen()
    
    x = 0
    y = 0
    placehold = pygame.Surface((Width, Hite))
    #print(mat)
    for index_y, row in enumerate(mat): 
        y = index_y
        for index_x, num in enumerate(row):
            x = index_x
            
            placehold.blit(elements[num], (x*32, y*32))
    return placehold

        


#########################################################################################
####################        End Background      #########################################
#########################################################################################



##Movement??##

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,33,33))
        self.rect = self.surf.get_rect()
         

   

back = parse_mat() 
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