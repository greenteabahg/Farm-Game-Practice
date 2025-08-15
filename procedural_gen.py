
import numpy as np 
from numpy import random


##################################################################################
#########################                       ##################################
#########################   |LN | N |RN |       ##################################
#########################   | L | X | R |       ##################################
#########################   |LS | S |RS |       ##################################
#########################                       ##################################
#########################   GRID ASSIGNMENTS    ##################################
#########################                       ##################################
##################################################################################
def rules(background):
    for index_y, row in enumerate(background):
        y = index_y
        for index, element in enumerate(row):
        
            x = index
        
            #################
            ## Grid Coords ##
            LN = (y - 1, x - 1)
            N = (y - 1, x)
            RN = (y - 1, x + 1)
            L = (y, x - 1) 
            R = (y, x + 1)
            LS = (y + 1, x - 1)
            S = (y + 1, x)
            RS = (y + 1, x + 1)
            ##################
            ##################

            if x == 1 and 14 > y > 0:
                background[L] = 4
            if x == 18 and 14 > y > 0:
                background[R] = 3

            if element == 0:
                if 14 > y > 1:
                    background[N] = random.choice((0,2,7,8), p=(0.7,0.2,0.05,0.05))
                    background[S] = random.choice((0,2,7,8), p=(0.7,0.2,0.05,0.05))
                #if x < 18:
                   # if x == 18:
                   # background[R] = 3 background[R] = random.choice((0,3,5,8), weights = (0.70, 0.2, 0.5,0.5), k=1)
                
                

            if element == 1:
                if y == 0:
                    background[y,x] = random.choice((2,3,4,7,8,9,0))
                else:
                    if x > 0:
                        background[L] = random.choice((1,5))
                    if x < 19:
                        background[R] = random.choice((1,6))
            
            if element == 2:
                if x > 0:
                    background[L] = random.choice((2,8))
                if x < 19:
                    background[R] = random.choice((2,7))
                if y < 14:
                    background[S] = 0

            if element == 3:
                if x > 0:
                    background[L] = 0
                if x < 19:
                    background[R] = random.choice((4,9))
                if y < 14:
                    background[S] = random.choice((3,8))
            
            if element == 4:
                if x > 0:
                    background[L] = random.choice((3,9))       
                if x < 19:
                    background[R] = 0
                if y < 14:
                    background[S] = random.choice((4,9,7))
        
            if element == 5:
                if x > 0:
                    background[L] = 0
                if x < 19:
                    background[R] = random.choice((1,9,6))
                if y < 14:
                    background[S] = random.choice((3,9,8))

            if element == 6:
                if x > 0:
                    background[L] = random.choice((1,5,9))
                if x < 19:
                    background[R] = 0
                if y < 14:
                    background[S] = random.choice((4,7,9))
            if element == 7:
                if x > 0:
                    background[L] = random.choice((2,8))
                if x < 19:
                    background[R] = 0
                    if y < 14:
                        background[RS] = 0
                if y < 14:
                    background[S] = 0
            
            if element == 8:
                if x > 0:
                    background[L] = 0
                    if y > 14:
                        background[LS] = 0
                if x < 19:
                    background[R] = random.choice((2,7))
                if y > 14:
                    background[S] = 0 
    return background

def mat_gen():
    
    background = random.randint(9, size=(15, 20))
    print(background)
    x = 0
    y = 0 
    LN = (y - 1, x - 1)
    N = (y - 1, x)
    RN = (y - 1, x + 1)
    L = (y, x - 1) 
    R = (y, x + 1)
    LS = (y + 1, x - 1)
    S = (y + 1, x)
    RS = (y + 1, x + 1)
   
    ## Generating a full map from random spawn ##
    
    
    background = rules(background) 
        
    ## Setting sides correctly
    for index_y, row in enumerate(background):
        y = index_y
        for index, element in enumerate(row):
            x = index
            if x == 1 and y == 0 or 14:
                background[L] = 9
            if x == 1 and 0 > y > 14:
                background[L] = 4
            if x == 13 and y == 0 or 14:
                background[R] = 9
            if x == 13 and 0 > y > 14:
                background[R] = 3
   
            ## I need to find a way to make sure there is a path of 0's from one side
            ##  to the other 

            ## I think the way to solve the above issue is to have a randomly generated
            ## function that defines an x,y pos and makes it 0
            ## So first, a random map is generated. Then it is polished by rules. 
            ## Then the edges are defined, and an entry point.
            ## When an entry point is determined, thats the starting point of the function (k)
            ## Func would look something like x + k = y 
            ##
            ## you replace the nums in the background with (y,x), not (x,y)
            ## this is because the matrix is made first with the rows (15), then the 
            ## amount of elements in each row (20)
            
            
       
    return background


