import itertools
import random
import math

DIMENSION = 1000
LINE_MIN_LENGTH = 300
LINE_MAX_LENGTH = 1000
FRAMES = 50
ANGLE_VARIANCE = .1
LINES = []

# corners
MIN_ANGLE = 0
MAX_ANGLE = math.pi/2
NUM_LINES_PER_POINT = 10
COLOR_BLUE = (74/255, 131/255, 178/255, 1)
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
        
        LINES.append({
            'origin': tuple(point),
            'angle': angle,
            'length': length,
            'color': COLOR_BLUE,
            'offset': random.uniform(0, FRAMES)
        })

# sides
MIN_ANGLE = 0
MAX_ANGLE = math.pi
COLOR_RED = (184/255, 103/255, 113/255, 1)
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
            
        LINES.append({
            'origin': tuple(point),
            'angle': angle,
            'length': length,
            'color': COLOR_RED,
            'offset': random.uniform(0, FRAMES)
        })

# center
MAX_ANGLE = 0
MIN_ANGLE = math.pi * 2
COLOR_YELLOW = (249/255, 227/255, 8/255, 1)
NUM_LINES_PER_POINT = 20
point = [DIMENSION/2, DIMENSION/2]
for i in range(NUM_LINES_PER_POINT):
    angle = (MAX_ANGLE - MIN_ANGLE) * i/NUM_LINES_PER_POINT + MIN_ANGLE + random.uniform(0, ANGLE_VARIANCE)
    length = random.uniform(LINE_MIN_LENGTH, LINE_MAX_LENGTH)
    
    LINES.append({
        'origin': tuple(point),
        'angle': angle,
        'length': length,
        'color': COLOR_YELLOW,
        'offset': random.uniform(0, FRAMES)
    })

pluck = lambda dict, *args: (dict[arg] for arg in args)
LENGTH_VARIANCE = 50
COLOR_WHITE = (240/255, 240/255, 240/255)
for frame in range(FRAMES):
    newPage(DIMENSION, DIMENSION)
    fill(*COLOR_WHITE)
    rect(0, 0, width(), height())
    frameDuration(1/20)
    save()
    for line in LINES:
        origin, angle, length, color, offset = pluck(line, 'origin', 'angle', 'length', 'color', 'offset')
        stroke(*color)
        theta = (frame/FRAMES + offset) * math.pi * 2

        length += math.cos(theta) * LENGTH_VARIANCE

        newPath()
        moveTo(origin)
        dest = (origin[0] + math.cos(angle) * length, origin[1] + math.sin(angle) * length)    
        lineTo(dest)
        closePath()
        drawPath()
    restore()
    
saveImage('wall-drawing-273.gif')