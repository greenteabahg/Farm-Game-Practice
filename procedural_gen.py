
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


def mat_gen():
    background = np.zeros((15,20), dtype=int)
    background[0,] = random.randint(9, size=(1, 20))
    print(background)
    x = 0
    y = 0 

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

    ##Polishing first row so everything can generate from it##
    for index, element in enumerate(background[0]):
        y = 0
        x = index
        print(background[L])
        if element == 1:
            background[y, x] = random.choice((2,3,4,7,8,9,0))
        if element == 2 and background[y, x-1] != 2 or 8 and index != 0:
                background[y, x-1] = random.choice((2,8))
            
                


    for index_y, row in enumerate(background):
        y = index_y
        for index_x, element in enumerate(row):
            x = index_x 
            ## The 0 element (Floor)
            ## I need to find a way to make sure there is a path of 0's from one side
            ##  to the other
            ##
            ## you replace the nums in the background with (y,x), not (x,y)
            ## this is because the matrix is made first with the rows (15), then the 
            ## amount of elements in each row (20)
            
            if element == 0:
                pass
            ## 1 Element (wall_up)
            
    print(background)   
    print(background[0]) 
    print(background[L])     
    return background


mat = mat_gen()