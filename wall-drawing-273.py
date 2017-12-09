import itertools
import random
import math

DIMENSION = 500
NUM_LINES_PER_POINT = 10
LINE_MIN_LENGTH = 150
LINE_MAX_LENGTH = 500

size(DIMENSION, DIMENSION)

for point in list(itertools.product([0, DIMENSION], repeat=2)):
    stroke(1, 0, 0, 1)
    for i in range(NUM_LINES_PER_POINT):
        angle = random.uniform(0, math.pi/2)
        length = random.uniform(LINE_MIN_LENGTH, LINE_MAX_LENGTH)
    
        if point[0] == 0 and point[1] == DIMENSION:
            angle -= math.pi/2
        elif point[0] == DIMENSION and point[1] == DIMENSION:
            angle -= math.pi
        elif point[0] == DIMENSION and point[1] == 0:
            angle += math.pi/2
            
        dest = (point[0] + math.cos(angle) * length, point[1] + math.sin(angle) * length)    
        
        newPath()
        moveTo(tuple(point))
        lineTo(dest)
        closePath()
        drawPath()
        print point, dest