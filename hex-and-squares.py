# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:27:15 2022

@author: olist
"""

import math
import random



sprinkler_tally = 0
height_tally = 0
n = 0
squarelist = []
hexlist = []




def square_pattern(area,ar):
    global sprinklers
    no_wide = math.ceil(width/math.sqrt(2))
    no_tall = math.ceil(height/math.sqrt(2))
    sprinklers = no_wide * no_tall
    print(sprinklers , "sprinklers needed when using a square pattern")
    sqpoint = [area,ar,sprinklers]
    return sqpoint
        
def hexagonal_pattern(area,ar):    
    global sprinkler_tally
    global width
    global height_tally
    global n
    
    n +=1
    
    if n % 2 == 1:
        height_tally += 1 
        no_wide = math.ceil(width/math.sqrt(3))
   
    if n % 2 == 0:
        height_tally += 2
        no_wide = math.ceil((width + 1)/math.sqrt(3))
    sprinkler_tally += no_wide
    
    if height_tally >= height:
        print("You need", sprinkler_tally, "sprinklers when using a hexagonal pattern")
    
    else:
        hexagonal_pattern(area,ar)
    hexpoint = [area,ar,sprinkler_tally]
    return hexpoint


for x in range(1,10):
    height = round(random.uniform(0.5,30.0),1)
    width = round(random.uniform(0.5,30.0),1)
    sprinkler_tally = 0
    height_tally = 0
    n = 0
    
    area = round(height * width,1)
    if height >= width:
        ar = round(height/width,1)
    else:
        ar = round(width/height,1)
    sqpoint = square_pattern(area, ar)
    squarelist.append(sqpoint)

    hexpoint = hexagonal_pattern(area,ar) 
    hexlist.append(hexpoint)
print('square list: ', squarelist)
print('hexagon list: ', hexlist)


