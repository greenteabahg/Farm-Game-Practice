import pygame
import random 
import sys
from spritemechs import Spritesheet
#from procedural_gen import mat_gen 
from maps import home_map
from pygame.locals import *

pygame.init()

Hite = 480
Width = 640
FPS = 30
dt = 1/FPS

FramePerSec = pygame.time.Clock()

canvas = pygame.Surface((640, 480))
displaysurf = pygame.display.set_mode((160, 128), pygame.SCALED)




#vector for movement
vec = pygame.math.Vector2
ACC = 0.5


running = True

########################################################################################
####################                   #################################################
####################     BACKGROUND    #################################################
####################                   #################################################
########################################################################################
##   NOTES: 
##      Below I am pulling all of my background sprites from 'Test_Background.png' using 
##      the class Spritesheet I put in spritemechs.py 
##      There is only one corner pixel image, so I rotated the other three to create the
##      the rest.
##
##      As of 08/15: The proc gen is not gonna happen just yet
##      Now, I am trying to make a procedural generator that will take a matrix for 
##      the screen (20 32x32 tiles by 15 32x32 tiles) and by assigning each type of
##      tile a number, generating the background based off of that. These could be static
##      and then scaled for the screen. (So no matter what, the ratio is always 20x15)
##      :::IDEAS::: 
##      Maybe the proc gen could use a function to create a map. Specifically, certain
##      functions might work well for at least the path (0's) through the map
##      The only problem is it has to be continous, that is for every f(x) = y, 
##      f'1(x'1) = y'1 is reachable from the last (x,y)
##
##      My next task is to build a background class that defines the inputs from the matrix
##      in order to set the colision of the background sprites 
#           All background sprites
backdrop = Spritesheet('Test_Background.png')

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

def parse_mat(mat):
    
    
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

        
back = parse_mat(home_map)

#########################################################################################
####################        End Background      #########################################
#########################################################################################



##Movement??##

########################################################################################
####################                   #################################################
####################     PLAYER        #################################################
####################                   #################################################
########################################################################################

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = P1_base ## For test only !! 
        self.rect = self.surf.get_rect()

        self.pos = vec((10,10))

    def move(self):
        p_keys = pygame.key.get_pressed()
        if p_keys[K_s]:
            self.pos.y += 10
        if p_keys[K_w]:
            self.pos.y += -10
        if p_keys[K_a]:
            self.pos.x += -10
        if p_keys[K_d]:
            self.pos.x += 10

        self.rect.center = self.pos

    ##This creates the window around the player
    ## I'm basically bliting an area of the canvas that is equal to a 160 by 128 rectangle
    ##around the player
    ## the if statements are a clever way of keeping the camera from leaving the canvas
    ## edges. Essentially, if the x pos of the player is less than half the window size (160),
    ## then the area taken from the left side of the rect is 0. It is half the window size
    ## because the player is depicted in the center of the window
    ## same applies for the y value
    ## conversely, if the x value approaches halfway between the rightmost canvas edge, then
    ## the left side of the area taken from the canvas is exactly 160 less than the full canvas size

    def P_view(self):
        player_view = pygame.surface.Surface((160,128))
        offset_x = self.pos.x - (160/2)
        offset_y = self.pos.y - (128/2)
        if self.pos.x < 160/2:
            offset_x = 0
        if self.pos.y < 128/2:
            offset_y = 0
        if self.pos.x > 640-80: ## I might should change these to varibles in the future
            offset_x = 640-160
        if self.pos.y > 480-64:
            offset_y = 480-128
        player_pos = (offset_x, offset_y, 160, 128) 

        player_view.blit(canvas, (0,0), player_pos)
        return player_view

P1_Sprites = Spritesheet('test_player.png')
P1_base = P1_Sprites.get_sprite(0,0,32,32)
P1 = Player()

## Creating a segment that follows the player





#####Game Loop##########
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    canvas.fill((0,0,0))
    P1.move() 
    
    canvas.blit(back, (0,0))
    canvas.blit(P1.surf, P1.rect)

    player_view = P1.P_view()
    displaysurf.blit(player_view, (0,0))

    FramePerSec.tick(FPS)
    pygame.display.update()