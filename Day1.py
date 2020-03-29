from pygame import *
from random import *
from glob import *

width, height = 800, 600
screen = display.set_mode((width, height))

running = True

clock = time.Clock()

mp = image.load("maps/map.png")
map = transform.smoothscale(mp, (800, 600))


direction = ["left", "right", "down", "up"]
walk = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\walking\\" + d + "\\*.png")] for d in direction}
run = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\running\\" + d + "\\*.png")] for d in direction}   #accesses all the pics from each direction folder and changes its size

t1 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t1\\" + d + "\\*.png")] for d in direction}
t2 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t2\\" + d + "\\*.png")] for d in direction}
t3 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t3\\" + d + "\\*.png")] for d in direction}
t4 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t4\\" + d + "\\*.png")] for d in direction}
t5 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t5\\" + d + "\\*.png")] for d in direction}
t6 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t6\\" + d + "\\*.png")] for d in direction}
t7 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t7\\" + d + "\\*.png")] for d in direction}

# print(walk)
# print(run)
print("bit tity")
count = 0
anime = 0
di = "up"
posx, posy = 200, 200
rs = 0.75
ws = 0.45
action = "walk"
actions = {"walk": walk,"run": run}

while running:


    g = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            running = False

    screen.fill(0)
    clock.tick(60)

    anime += 1
    if anime % 10 == 0:  # speed of transition between pics
        count += 1

    if g[K_LSHIFT] or g[K_RSHIFT]:
        action = "run"
    else:
        action = "walk"

    speed=ws
    if action == "run":
        speed = rs

    if g[K_UP] or g[K_w]:
        di = "up"
        posy -= speed
    elif g[K_LEFT] or g[K_a]:
        di = "left"
        posx -= speed
    elif g[K_DOWN] or g[K_s]:
        di = "down"
        posy += speed
    elif g[K_RIGHT] or g[K_d]:
        di = "right"
        posx += speed
    else:
        count = 0

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    screen.blit(map, (0, 0))

    screen.blit((actions[action][di][count % 3]), (posx, posy))

    display.flip()

quit()
