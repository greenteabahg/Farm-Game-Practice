import pygame
import random 
import sys
from spritemechs import Spritesheet
#from procedural_gen import mat_gen 
from maps import home_map
from pygame.locals import *
#thigns to do:
# Update Movement (Eventually)

pygame.init()

Hite = 480
Width = 640
FPS = 30

#Time shit
FramePerSec = pygame.time.Clock()

animation_cooldown = 500

canvas = pygame.Surface((640, 480))
displaysurf = pygame.display.set_mode((160, 128), pygame.SCALED)

#Inventory Surface





#vector for movement
vec = pygame.math.Vector2
 #music
back_mus = pygame.mixer.music.load('Stefano Vita - Once Upon A Time.mp3')
pygame.mixer.music.play(-1)


running = True
#trying to implement pausing
paused = False
global inv_paused
inv_paused = False
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

#I need to change these names lol
holla = Background('Test_Background.png')

yolo = holla.parse_mat(home_map)
yolo_map = holla.collide_map(home_map)

#########################################################################################
####################        End Background      #########################################
#########################################################################################

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
        self.update_time = pygame.time.get_ticks()
        self.frame = 0

        #health?
        self.health = 100
        self.damage = False

    def move(self):
        p_keys = pygame.key.get_pressed()
        
        #added animation frames and shi
        if not any(p_keys):
            self.surf = P1_base
        if p_keys[K_s]:
            self.pos.y += 10
        if p_keys[K_w]:
            self.pos.y += -10
        if p_keys[K_a]:
            self.pos.x += -10
            
        if p_keys[K_d]:
            self.pos.x += 10
            if self.frame == 8:
                self.frame = 0
            if current_time - self.update_time >= 100: #150 = ani cooldown
                self.surf = walking_right_animation[self.frame]
                self.frame += 1
                self.update_time = current_time
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


    #makes the player hit walls
    
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

    
    # This creates the window around teh player
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
    


P1_Sprites = Spritesheet('farmer.png')
P1_base = P1_Sprites.get_sprite(0,0,32,32)

#Walking right animation
P1_WR_Frame1 = P1_Sprites.get_sprite(32,0,32,32)
P1_WR_Frame2 = P1_Sprites.get_sprite(64,0,32,32)
P1_WR_Frame3 = P1_Sprites.get_sprite(0,32,32,32)
P1_WR_Frame4 = P1_Sprites.get_sprite(64,0,32,32)
P1_WR_Frame5 = P1_Sprites.get_sprite(32,0,32,32)
P1_WR_Frame6 = P1_Sprites.get_sprite(0,64,32,32)
P1_WR_Frame7 = P1_Sprites.get_sprite(32,64,32,32)
P1_WR_Frame8 = P1_Sprites.get_sprite(0,64,32,32)

walking_right_animation = (P1_WR_Frame1, P1_WR_Frame2, P1_WR_Frame3, P1_WR_Frame4, P1_WR_Frame5, 
P1_WR_Frame6, P1_WR_Frame7, P1_WR_Frame8)
P1 = Player()



# For animations

########################################################################################
####################                   #################################################
####################     UI            #################################################
####################                   #################################################
########################################################################################

ui_sprites = Spritesheet('UI items.png')
2

class UI:
    def __init__(self):
        self.inv_chest_surf = ui_sprites.get_sprite(13, 5, 17, 13)
        self.inv_block_surf = ui_sprites.get_sprite(0, 5, 13, 13)
        self.heart_full_surf = ui_sprites.get_sprite(0, 20, 10, 8)
        self.heart_empty_surf = ui_sprites.get_sprite(10, 20, 10, 8)

        self.inv_chest_surf_mouse = ui_sprites.get_sprite(13, 37, 20, 15)

        self.heart_full_surf_Big = ui_sprites.get_sprite(0, 52, 10, 9)
        self.health_num = P1.health/10
        self.health_num = int(self.health_num)

    def show(self):
        if mouse_pos_x < 140 or mouse_pos_y < 113:
            displaysurf.blit(self.inv_chest_surf, (140,113))
        else:
            displaysurf.blit(self.inv_chest_surf_mouse, (140,113))

        #Healthbar
        #Eventually i'll add the healthbar animation from the UI items.png
        if not P1.damage: 
            for i in range(self.health_num):
                displaysurf.blit(self.heart_full_surf, (i*8, 0))
            for i in range(10):
                displaysurf.blit(self.heart_empty_surf, ((i*8 + 1) , 0))
        else:
            pass

    def inventory(self):

       

        inv_surf_border = pygame.surface.Surface((130,98))
        inv_surf = pygame.surface.Surface((128,96))
        inv_surf_border.fill((10,0,0))
        inv_surf.fill((209,200,200)) #off white

        inv_surf_border.blit(inv_surf, (1,1))

        #getting center of inv for screen
        inv_surf_rect = inv_surf_border.get_rect()
        center_p = player_view.get_rect()
        inv_surf_rect.center = center_p.center
        (x,y) = inv_surf_rect.x, inv_surf_rect.y

        #Exit Button
        inv_exit = Button(25,12 , (10,10,10), "Exit", (100,100,100), (100,80))
        inv_exit.show(inv_surf_border)
        displaysurf.blit(inv_surf_border, (x,y) )
        inv_return = False 
        inv_return = inv_exit.pressed()
        if inv_return == True:
            print(mouse_pos)
            inv_paused = False
            
        

       
            
            
UI = UI() 

class Button:
    def __init__(self, x, y, color, words, word_color, position):
        #allowing program to define button size/color
        self.surf = pygame.surface.Surface((x,y))
        self.rect = self.surf.get_rect()
        self.color = self.surf.fill((color))

        self.text_size = x * y / 20
        self.text_size = int(self.text_size)
        
        #button font + text
        self.font = pygame.font.SysFont('freesans', self.text_size)
        self.text = self.font.render(words, False, word_color)
        
        #position args
        self.pos = position
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.x = x 
        self.y = y
        
    def show(self, location):
        #Find center of button and text surf
        #Tbh text looks godawful at this scale lol
        
        center_find = self.text.get_rect() 
        center_find.center = self.rect.center
        (x,y) = center_find.x, center_find.y
        self.surf.blit(self.text,(x,y))
        #Put text on button
        location.blit(self.surf, self.pos)
        #for pressed
        
        
    def pressed(self):
        if mouse_pos_x <= self.pos_x + self.x and mouse_pos_x > self.pos_x and mouse_pos_y <= self.pos_y + self.y and mouse_pos_y > self.pos_y and pygame.mouse.get_pressed()[0]:
            return True
            
#####Game Loop##########

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Used for animating
    current_time = pygame.time.get_ticks()

    #Mouse pos
    #the prob w mouse pos is that it is for the screen. i need a function to determine the
    #ultimate pos of the mouse within the actual surface
    mouse_pos = pygame.mouse.get_pos() 
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]

    if mouse_pos_x > 140 and mouse_pos_y > 113:
            if pygame.mouse.get_pressed()[0]:
                
                inv_paused = True 

    # Normal Game essentially
    if not inv_paused:
            canvas.fill((0,0,0))
            P1.move()

            P1.c_test()
    
    
            canvas.blit(yolo, (0,0))
            canvas.blit(P1.surf, P1.rect)
    #test
    #canvas.blit(UI.heart_full_surf_Big, (0,0))
    
            player_view = P1.P_view()
            displaysurf.blit(player_view, (0,0))
            UI.show() 
            
    #Game paused for inventory
    if inv_paused:
        UI.inventory()
        
    FramePerSec.tick(FPS)
    pygame.display.update()