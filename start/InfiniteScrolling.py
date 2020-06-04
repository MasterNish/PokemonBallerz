#Infinite scrolling effect
from pygame import *

init()
size = 800, 600
screen=display.set_mode(size)
RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

a=0
b=1
c=2
runtime = 0

grass1 = image.load("instructions1.png")
grass2 = image.load("instructions.png")

font.init()

mytext = font.SysFont("Arial", 30)
mytext1 = mytext.render("HEY", True, BLACK)
mytext2 = mytext.render("Rishi", True, BLACK)

y = 500

      #a b  c
g1 = [0,0,600]
g2=[0,-600,600]

speed = 3

def drawScene():
    screen.blit(grass1, (g1[a],g1[b]))
    screen.blit(grass2, (g2[a],g2[b]))
    # background scrolling
    g1[b] = g1[b] + speed
    if g1[b] + speed > g1[c]:
        g1[b] = -g2[c]
    g2[b] = g2[b] + speed
    if g2[b] + speed > g2[c]:
        g2[b] = -g1[c]
    print("first y=",g1[b],"second y=",g2[b])
    # display.flip()

myClock=time.Clock()   
running = True
while running:              

    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False

    if runtime <= 1000:
        runtime += 1
        drawScene()

        screen.blit(mytext1, (200, y))
        screen.blit(mytext2, (200, y + 50))
        y -= 1
        display.flip()
        myClock.tick(60)

        print(runtime)
    else:
        quit()
