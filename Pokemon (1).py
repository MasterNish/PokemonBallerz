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
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
AQUA=(3, 252, 182)
BEIGE=(250, 245, 112)

wallsMap1=[Rect(0,0,358,75),Rect(0,75,50,600),Rect(0,450,340,175),Rect(315,480,600,600),Rect(750,0,90,601),Rect(450,0,1000,75),Rect(460,280,200,150)]
wallsMap2=[Rect(400,0,500,121),Rect(680,0,300,384),Rect(0,550,1000,1000),Rect(0,0,65,1000),Rect(0,410,650,66),Rect(146,338,400,28),
           Rect(0,0,250,100),Rect(230,260,210,30),Rect(730,300,1000,300),Rect(200,110,72,80),Rect(232,190,111,43),Rect(232,190,350,20)]
wallsMap3=[Rect(0,0,400,200),Rect(0,0,90,1000),Rect(0,0,430,100),Rect(0,550,1000,100),Rect(0,0,1000,80),Rect(710,0,1000,1000),Rect(340,200,75,80),Rect(400,0,60,250)]
nWall=[Rect(203,156,412,1),Rect(203,156,1,306),Rect(203,462,412,1),Rect(615,156,1,412)]
martWall=[Rect(129,129,545,1),Rect(129,450,545,1),Rect(129,129,1,321),Rect(674,129,1,321)]
downWall=[Rect(213,144,377,1),Rect(213,392,377,1),Rect(213,144,1,248),Rect(591,144,1,248)]
wallsMapboss1=[Rect(500,100,100,100)]

ledge2=[Rect(150,250,50,20)]

inside=False


def drawScene(screen,player,walls):
    #screen.fill(0)  
    #draw.rect(screen,GREEN,player)


    
    for w in walls:
        draw.rect(screen,RED,w) 
    display.flip()

def movePlayer(player,mywalls,myledge):
    keys = key.get_pressed()
    if keys[K_DOWN] and hitwalls(pos[X],pos[Y]+5,mywalls)==-1:
        pos[Y] += 5                                          
    elif keys[K_UP] and hitwalls(pos[X],pos[Y]-5,mywalls)==-1 and hitwalls(pos[X],pos[Y]-5,myledge)==-1:                                                             
        pos[Y] -= 5
    if keys[K_LEFT] and hitwalls(pos[X]-5,pos[Y],mywalls)==-1:                                                            
        pos[X] -= 5
    elif keys[K_RIGHT] and hitwalls(pos[X]+5,pos[Y],mywalls)==-1:                                                               
        pos[X] += 5


    

def hitwalls(x,y,mywalls):
    playerRect = Rect(x,y,25,25)  
    print(playerRect.collidelist(mywalls)) 
    return playerRect.collidelist(mywalls)

FirstMap=Rect(360,15,90,0)
SecondMap=Rect(280,75,90,0)
neighbour=Rect(500,220,60,0)
martbox=Rect(140,340,40,0)

downbox=Rect(215,450,40,0)
downbox2=Rect(290,450,40,0)

boss1=Rect(500,100,100,0)

running = True

clock = time.Clock()
level=1
mp = image.load("maps/map.png")
mp1 = image.load("maps/map1.png")
mp2 = image.load("maps/map6.png")
neig = image.load("maps/neighbourWithBlack.png")
pokemart = image.load("maps/pokecenterwithblack.png")
housedownstairs = image.load("maps/downstairswithblack.png")
bossmap1withblack = image.load("maps/bosswithblack1.png")

map = transform.smoothscale(mp, (800, 600))
map1 = transform.smoothscale(mp1, (800, 600))
map2 = transform.smoothscale(mp2, (800, 600))
neigbourInside = transform.smoothscale(neig, (800, 600))
mart = transform.smoothscale(pokemart, (800, 600))
down = transform.smoothscale(housedownstairs, (800, 600))
boss1map = transform.smoothscale(bossmap1withblack, (800, 600))

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



mapgrid = [[]]
count = 0
background=0
build=0
map2origin=0
anime = 0
di = "down"
X=0
Y=1
pos=[370,50]
rs = 0.75
ws = 0.45
action = "walk"
actions = {"walk": walk, "run": run}

font.init()
comicFont=font.SysFont("Comic Sans MS",11)

while running:

    g = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            running = False

    screen.fill(0)
    col=GREEN
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

#____________________________________________________________________________________________________________________________________________________________________________________________________________
    if build==1:
        movePlayer(walk,nWall,[])
        

    if level==1 and inside==False:
        movePlayer(walk,wallsMap1,[])
        #print("moving")
    
        
    elif level==2:
        movePlayer(walk,wallsMap2,ledge2)

    elif level==3 and inside==False:
        movePlayer(walk,wallsMap3,[])

    elif build==2:
        movePlayer(walk,martWall,[])
        

    elif build==3:
        movePlayer(walk,downWall,[])

    elif build==4:
        movePlayer(walk,downWall,[])

    elif level==4 and inside==False:
        movePlayer(walk,wallsMapboss1,[])
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        
    if g[K_UP] or g[K_w]:
        di = "up"
        #pos[Y] -= speed
    elif g[K_LEFT] or g[K_a]:
        di = "left"
        #pos[X] -= speed
    elif g[K_DOWN] or g[K_s]:
        di = "down"
        #pos[Y] += speed
    elif g[K_RIGHT] or g[K_d]:
        di = "right"
        #pos[X] += speed
    else:
        count = 0

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    print(mx, "x value",my,"yvalue")
    
    playerRect=Rect(pos[X],pos[Y],18,21)
                                                           
#__________________________________________________________________________________________________________________________________________________________________________________________________
    screen.blit(map, (0, 0))
    for wm in wallsMap1:
        draw.rect(screen,RED,wm,2)
    draw.rect(screen,AQUA,FirstMap)
    draw.rect(screen,AQUA,neighbour)


    #print(actions[action])

    #screen.blit((actions[action][di][count % 3]), (posx, posy))
    draw.rect(screen,col,playerRect,1)

    if playerRect.colliderect(neighbour) and background==0 and build==0:
        build=1
        pos[X]=300
        pos[Y]=200
        inside=True
        

    if background==0 and build==1:
        screen.blit(neigbourInside, (0, 0))
        for wm in nWall:
            draw.rect(screen,RED,wm,2)
        
        

    if playerRect.colliderect(FirstMap):
        col=BLACK
        background=1
        level=2
        print("level 22222")
        
        
    if background==1:
        screen.blit(map1, (0, 0))
        for wm in wallsMap2:
            draw.rect(screen,RED,wm,2)
        for ledge in ledge2:
            draw.rect(screen,BLUE,ledge,2)

        
        draw.rect(screen,BEIGE,SecondMap)

    if playerRect.colliderect(SecondMap) and background==1:
        col=BLACK
        level=3
        background=2
        print("aaaaa")
        pos[X]=93
        pos[Y]=223
        
    if background==2:
        screen.blit(map2, (0, 0))
        for wm in wallsMap3:
            draw.rect(screen,RED,wm,3)
        #playerRect=Rect(pos[X],pos[Y],16,22)

        draw.rect(screen,BEIGE,martbox)
        draw.rect(screen,BEIGE,downbox)
        draw.rect(screen,BEIGE,downbox2)
        draw.rect(screen,BEIGE,downbox2)
        draw.rect(screen,BEIGE,boss1)

    if playerRect.colliderect(martbox) and background==2 and build==0:
        build=2
        
        
        
        pos[X]=93
        pos[Y]=223
        inside=True

    if build==2 and background==2:
        #print(22)
        screen.blit(mart, (0, 0))
        for wm in martWall:
            draw.rect(screen,RED,wm,3)

    if build==3 and background==2:
        #print("32")
        screen.blit(down, (0, 0))
        for wm in downWall:
            draw.rect(screen,RED,wm,3)

    if playerRect.colliderect(downbox) and background==2 and build==0:
        build=3
        
        
        pos[X]=93
        pos[Y]=223

    if build==4 and background==2:
        #print("42")
        screen.blit(down, (0, 0))
        for wm in downWall:
            draw.rect(screen,RED,wm,3)

    if playerRect.colliderect(downbox2) and background==2 and build==0:
        build=4
        
        
        pos[X]=93
        pos[Y]=223

    if background==3:
        #print("52")
        screen.blit(boss1map, (0, 0))
        for wm in wallsMapboss1:
            draw.rect(screen,RED,wm,3)

    if playerRect.colliderect(boss1) and background==2:
        level=4
        background=3
        
        
        pos[X]=93
        pos[Y]=223
        
     
        
#_________________________________________________________________________________________________________________________________________________________________________________________        
    draw.rect(screen,col,playerRect,1)
    screen.blit((actions[action][di][count % 3]), (pos[X], pos[Y]))
    #print (pos[X],"x value",pos[Y],"y value")
    
    display.flip()

quit()
