from pygame import *
from math import *

init()
size = width, height = 600, 450
screen = display.set_mode(size)

backPic = image.load("maps/map.png")  # 800x600
bPic = transform.smoothscale(backPic, (800, 600))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

X = 0
Y = 1
W = 2
H = 3

# X #Y
v = [0, 0]
# X Y  W  H
p = Rect(0, 190, 20, 20)


##guy=[0,170,0]
##X=0
##Y=1
##VY=2

def drawScene(screen, p):
    screen.blit(bPic, (-p[X], -p[Y]))
    draw.rect(screen, (255, 255, 0), (300, 225, 15, 15))
    display.flip()

def moveGuy(p):
    'moving the player'
    keys = key.get_pressed()

    if keys[K_RIGHT] and p[X] < 700:
        v[X] = 10
    elif keys[K_LEFT] and p[X] > -300:
        v[X] = -10
    elif keys[K_DOWN] and p[Y] < 360:
        v[Y] = 10
    elif keys[K_UP] and p[Y] > -225:
        v[Y] = -10
    else:
        v[Y] = 0
        v[X] = 0
    # move p

def check(p):
    'checks if the player "lands"'
    p[Y] += v[Y]  # falling down
    if p[Y] + p[H] >= height:  # if the player attempts to fall below the ground
        p[Y] = height - p[H]
        v[Y] = 0  # stop falling
    p[X] += v[X]  # falling down
    if p[X] + p[H] >= height:  # if the player attempts to fall below the ground
        p[X] = height - p[H]
        v[X] = 0  # stop falling
    print(p, v)


running = True
myClock = time.Clock()
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    screen.fill((0, 0, 0))
    moveGuy(p)
    drawScene(screen, p)
    check(p)
    myClock.tick(60)
quit()