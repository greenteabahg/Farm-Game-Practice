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


FramePerSec = pygame.time.Clock()

canvas = pygame.Surface((640, 480))
displaysurf = pygame.display.set_mode((160, 128), pygame.SCALED)




#vector for movement
vec = pygame.math.Vector2



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

class Background:
    def __init__(self, filename):
        self.spritesheet = Spritesheet(filename)
        self.wall_TOP = self.spritesheet.get_sprite(64,0,32,32)
        self.wall_BOT = self.spritesheet.get_sprite(0,32,32,32)
        self.wall_LEFT = self.spritesheet.get_sprite(32,32,32,32)
        self.wall_RIGHT = self.spritesheet.get_sprite(64,32,32,32)
        self.wall_FULL = self.spritesheet.get_sprite(32,0,32,32)

        self.floor = self.spritesheet.get_sprite(32,64,32,32)

        self.corner_RN = self.spritesheet.get_sprite(0,0,32,32)
        self.corner_LN = pygame.transform.rotate(self.corner_RN, 90)
        self.corner_LS = pygame.transform.rotate(self.corner_RN, 180)
        self.corner_RS = pygame.transform.rotate(self.corner_RN, 270)

        self.elements = (self.floor, self.wall_TOP, self.wall_BOT, self.wall_LEFT, self.wall_RIGHT, 
                self.corner_LN, self.corner_RN, self.corner_RS, self.corner_LS, self.wall_FULL)
        #All wall sprites
        self.group_wall = pygame.sprite.Group()

        #Specific wall sprites
        self.group_wall_top = pygame.sprite.Group()#1
        self.group_wall_bot = pygame.sprite.Group() #2
        self.group_wall_left = pygame.sprite.Group() #3
        self.group_wall_right = pygame.sprite.Group() #4
        self.group_wall_corner_LN = pygame.sprite.Group() #5
        self.group_wall_corner_RN = pygame.sprite.Group() #6
        self.group_wall_corner_RS = pygame.sprite.Group() #7
        self.group_wall_corner_LS = pygame.sprite.Group() #8
        
        


    def parse_mat(self, matrix):
        x = 0
        y = 0
        placehold = pygame.Surface((Width, Hite))
    
        #print(matrix)
        for index_y, row in enumerate(matrix): 
            y = index_y
            for index_x, num in enumerate(row):
                x = index_x
            
                placehold.blit(self.elements[num], (x*32, y*32))   

            ## I think I have to make a class for the background lol
        return placehold

    def collide_map(self, matrix):
        x = 0
        y = 0
        map = []
        for index_y, row in enumerate(matrix):
            y = index_y
            for index_x, num in enumerate(row):
                x = index_x
                if num != 0:
                    rect_hold = pygame.Rect(x*32,y*32, 32, 32)
                    map.append(rect_hold)
                    sprite_hold = pygame.sprite.Sprite()
                    sprite_hold.rect = rect_hold
                    self.group_wall.add(sprite_hold)
                    if num == 1:
                        self.group_wall_top.add(sprite_hold)
                    if num == 2:
                        self.group_wall_bot.add(sprite_hold)
                    if num == 3:
                        self.group_wall_left.add(sprite_hold)
                    if num == 4:
                        self.group_wall_right.add(sprite_hold)
                    if num == 5:
                        self.group_wall_corner_LN.add(sprite_hold)
                    if num == 6:
                        self.group_wall_corner_RN.add(sprite_hold)
                    if num == 7:
                        self.group_wall_corner_RS.add(sprite_hold)
                        print(sprite_hold.rect.x)
                    if num == 8:
                        self.group_wall_corner_LS.add(sprite_hold)
                    
        return map 



holla = Background('Test_Background.png')


yolo = holla.parse_mat(home_map)
yolo_map = holla.collide_map(home_map)
print(holla.group_wall)

#old background stuff
"""
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
        

            ## I think I have to make a class for the background lol
    return placehold

def collide_map(mat):
    
    x = 0
    y = 0
    map = []
    for index_y, row in enumerate(mat):
        y = index_y
        for index_x, num in enumerate(row):
            x = index_x
            if num != 0:
                rect_hold = pygame.Rect(x*32,y*32, 32, 32)
                map.append(rect_hold)
    return map 
"""

#makes the c_map into sprites to work for collision ? 
#17/08 - Dont think the sprites are the way to go but maybe later i could turn the walls
# into a class?
"""class Walls(pygame.sprite.Sprite):
    def __init__(self):
        pass"""
"""
def c_map_sprites(map):
    placeholder = pygame.sprite.Group()
    for item in map:
        item = pygame.sprite.Sprite
        placeholder.add(item)
    return placeholder
"""

# A part of old background stuff
"""
back = parse_mat(home_map)

c_map = collide_map(home_map)
union_c_map = pygame.rect.Rect(-32, 0,10,10)
union_c_map.unionall(c_map)
"""

#See note 17/08
"""
wall_map = pygame.sprite.Group()
wall_map = c_map_sprites(c_map)
"""

#########################################################################################
####################        End Background      #########################################
#########################################################################################

########################################################################################
####################                   #################################################
####################     COLLISION     #################################################
####################                   #################################################
########################################################################################




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

        self.pos = vec((100,100))

    def move(self):
        p_keys = pygame.key.get_pressed()
        if p_keys[K_s]:
            self.pos.y += 10
        if p_keys[K_w]:
            self.pos.y += -10
        if p_keys[K_a]:
            self.pos.x += -10
            self.surf = P1_left
        if p_keys[K_d]:
            self.pos.x += 10
            self.surf = P1_base
        ## This doesnt allow the player sprite out of bounds
        if self.pos.x < 10:
            self.pos.x = 10
        if self.pos.y < 5:
            self.pos.y = 5
        if self.pos.x > 635:
            self.pos.x = 635
        if self.pos.y > 465:
            self.pos.y = 465

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
    
    def c_test(self):
        T = pygame.sprite.spritecollide(P1, holla.group_wall_top, False)  
        if T:
            self.pos.y = T[0].rect.top - 20

        B = pygame.sprite.spritecollide(P1, holla.group_wall_bot, False)
        if B:
            self.pos.y = B[0].rect.bottom + 11

        L = pygame.sprite.spritecollide(P1, holla.group_wall_left, False)
        if L:
            self.pos.x = L[0].rect.left - 11

        R = pygame.sprite.spritecollide(P1, holla.group_wall_right, False)
        if R:
            self.pos.x = R[0].rect.right + 11
        LN = pygame.sprite.spritecollide(P1, holla.group_wall_corner_LN, False)
        if LN:
            if LN and self.pos.x < LN[0].rect.x:
                self.pos.x = LN[0].rect.left - 11
            if LN and self.pos.x >= LN[0].rect.x:
                self.pos.y = LN[0].rect.top - 20
        
        RN = pygame.sprite.spritecollide(P1, holla.group_wall_corner_RN, False)
        if RN:
            if RN and self.pos.x > RN[0].rect.x + 32:
                self.pos.x = RN[0].rect.right + 11
            if RN and self.pos.x <= RN[0].rect.x + 32:
                self.pos.y = RN[0].rect.top - 20
        
        LS = pygame.sprite.spritecollide(P1, holla.group_wall_corner_LS, False)
        if LS:
            if LS and self.pos.x <= LS[0].rect.x:
                self.pos.x = LS[0].rect.left - 11
            if LS and self.pos.x > LS[0].rect.x:
                self.pos.y = LS[0].rect.bottom + 11
        
        RS = pygame.sprite.spritecollide(P1, holla.group_wall_corner_RS, False)
        if RS:
            if RS and self.pos.x > RS[0].rect.x + 32:
                self.pos.x = RS[0].rect.right + 11
            if RS and self.pos.x <=RS[0].rect.x + 32:
                self.pos.y = RS[0].rect.bottom + 11
            #The problem is that my movement makes it so that i move 10 pixels per key press,
            # so everytime there is an wall, I still can move 10 blocks into it

        
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
    ## To be done latah 
    


P1_Sprites = Spritesheet('test_player_2.png')
P1_base = P1_Sprites.get_sprite(0,0,32,32)
P1_left = P1_Sprites.get_sprite(32,0,32,32)
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

    P1.c_test()
    
    canvas.blit(yolo, (0,0))
    canvas.blit(P1.surf, P1.rect)
    
    player_view = P1.P_view()
    displaysurf.blit(player_view, (0,0))

    FramePerSec.tick(FPS)
    pygame.display.update()