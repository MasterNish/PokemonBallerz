from pygame import *
from random import *
from glob import *
# from Camera import *

class Character(sprite.Sprite):

    def __init__(self, animations, x, y):
        sprite.Sprite.__init__(self)

        self.animations = animations
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = None
        self.count = 0
        self.anirate = 0
        self.direction = "down"
        self.speeds = {"walk": 0.45, "run": 0.75, "idle": 0}
        self.action = "walk"

    def animate(self):

        self.anirate += 1
        if self.anirate % 10 == 0:  # frame rate
            self.count += 1
        animation = self.animations[self.action]
        self.image = animation[self.count % len(animation)]

    def move(self):

        if self.direction == "down":
            self.rect.y += self.speeds[self.action]
        if self.direction == "right":
            self.rect.x += self.speeds[self.action]
        if self.direction == "up":
            self.rect.y -= self.speeds[self.action]
        if self.direction == "left":
            self.rect.x -= self.speeds[self.action]


width, height = 800, 600
screen = display.set_mode((width, height))
running = True

clock = time.Clock()

mp = image.load("maps/map.png")
mp1 = image.load("maps/map1.png")
map = transform.smoothscale(mp, (800, 600))

direction = ["left", "right", "down", "up"]
walk = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\Player\\walking\\" + d + "\\*.png")] for d in
        direction}
run = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\Player\\running\\" + d + "\\*.png")] for d in
       direction}  # accesses all the pics from each direction folder and changes its size

t1 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t1\\" + d + "\\*.png")] for d in
      direction}
t2 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t2\\" + d + "\\*.png")] for d in
      direction}
t3 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t3\\" + d + "\\*.png")] for d in
      direction}
t4 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t4\\" + d + "\\*.png")] for d in
      direction}
t5 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t5\\" + d + "\\*.png")] for d in
      direction}
t6 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t6\\" + d + "\\*.png")] for d in
      direction}
t7 = {d: [transform.smoothscale(image.load(i), (18, 21)) for i in glob("sprites\\t7\\" + d + "\\*.png")] for d in
      direction}

# print(walk)
# print(run)

mapgrid = [[]]
count = 0
anime = 0
di = "down"
posx, posy = 200, 200
rs = 0.75
ws = 0.45
action = "walk"
actions = {"walk": walk, "run": run}

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

    speed = ws
    if g[K_LSHIFT] or g[K_RSHIFT]:
        action = "run"
        speed = rs
    else:
        action = "walk"

    # if action == "run":
    #     speed = rs

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


    print(actions[action])

    screen.blit((actions[action][di][count % 3]), (posx, posy))

    display.flip()

quit()