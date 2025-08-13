import pygame

pygame.init()

Hite = 500
Width = 500
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurf = pygame.display.set_mode((Width, Hite))

running = True


### Vector for Entry into Room ?? ###
entry = pygame.math.Vector2
 

##Character Cube##

##Movement??##

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,33,33))
        self.rect = self.surf.get_rect()
        self.pos = entry(0,0) 

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pass  
        if keys[pygame.K_s]:
            self.pos.y += -1
        if keys[pygame.K_d]:
            self.pos.x += 1
        if keys[pygame.K_a]:
            self.pos.x += -1


P1 = Player() 


#####Game Loop##########
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    displaysurf.fill((0,0,0))

     
    P1.move() 

    displaysurf.blit(P1.surf, P1.rect) 
     
    pygame.display.update()
