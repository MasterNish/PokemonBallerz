#Infinite scrolling effect
from pygame import *
init()
size = 800,600
screen=display.set_mode(size)
X=0
Y=1
H=2
galaxy1 = image.load("instructions1.png")
galaxy2 = image.load("instructions.png")

      #X Y  H
g1 = [0,0,600]
g2=[0,-600,600]

speed = 3

def drawScene():
    screen.blit(galaxy1, (g1[X],g1[Y]))
    screen.blit(galaxy2, (g2[X],g2[Y]))
    # background scrolling
    g1[Y] = g1[Y] + speed
    if g1[Y] + speed > g1[H]: 
        g1[Y] = -g2[H]
    g2[Y] = g2[Y] + speed
    if g2[Y] + speed > g2[H]:
        g2[Y] = -g1[H]
    print("first y=",g1[Y],"second y=",g2[Y])
    display.flip()                   

myClock=time.Clock()   
running = True
while running:              

    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False

    drawScene()
    myClock.tick(60)

quit()