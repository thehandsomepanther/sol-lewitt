import itertools
import random
import math

DIMENSION = 1000
NUM_LINES_PER_POINT = 10
LINE_MIN_LENGTH = 300
LINE_MAX_LENGTH = 1000

ANGLE_VARIANCE = .1

size(DIMENSION, DIMENSION)

# corners
MIN_ANGLE = 0
MAX_ANGLE = math.pi/2
stroke(74/255, 131/255, 178/255, 1)
for point in list(itertools.product([0, DIMENSION], repeat=2)):
    for i in range(NUM_LINES_PER_POINT):
        angle = (MAX_ANGLE - MIN_ANGLE) * i/NUM_LINES_PER_POINT + MIN_ANGLE + random.uniform(0, ANGLE_VARIANCE)
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

# sides
MIN_ANGLE = 0
MAX_ANGLE = math.pi
stroke(184/255, 103/255, 113/255, 1)
for point in [[DIMENSION/2, 0], [0, DIMENSION/2], [DIMENSION, DIMENSION/2], [DIMENSION/2, DIMENSION]]:
    for i in range(NUM_LINES_PER_POINT):
        angle = (MAX_ANGLE - MIN_ANGLE) * i/NUM_LINES_PER_POINT + MIN_ANGLE + random.uniform(0, ANGLE_VARIANCE)
        length = random.uniform(LINE_MIN_LENGTH, LINE_MAX_LENGTH)
    
        if point[0] == 0 and point[1] == DIMENSION/2:
            angle -= math.pi/2
        elif point[0] == DIMENSION and point[1] == DIMENSION/2:
            angle += math.pi/2
        elif point[0] == DIMENSION/2 and point[1] == DIMENSION:
            angle += math.pi
            
        dest = (point[0] + math.cos(angle) * length, point[1] + math.sin(angle) * length)    
        
        newPath()
        moveTo(tuple(point))
        lineTo(dest)
        closePath()
        drawPath()

# center
MAX_ANGLE = 0
MIN_ANGLE = math.pi * 2
stroke(249/255, 227/255, 8/255, 1)
NUM_LINES_PER_POINT = 20
point = [DIMENSION/2, DIMENSION/2]
for i in range(NUM_LINES_PER_POINT):
    angle = (MAX_ANGLE - MIN_ANGLE) * i/NUM_LINES_PER_POINT + MIN_ANGLE + random.uniform(0, ANGLE_VARIANCE)
    length = random.uniform(LINE_MIN_LENGTH, LINE_MAX_LENGTH)
    dest = (point[0] + math.cos(angle) * length, point[1] + math.sin(angle) * length)    
        
    newPath()
    moveTo(tuple(point))
    lineTo(dest)
    closePath()
    drawPath()
