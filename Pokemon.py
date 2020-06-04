from pygame import *
from random import *
from glob import *

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


musics = ["Music/Music.mp3"]
mInd = 0
inc = 0.7

init()

mixer.music.load(musics[mInd])  # music plays infintely as the program runs
mixer.music.play(-1)

mixer.music.set_volume(inc)

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

startWall=[Rect(188,162,417,0),Rect(188,489,417,0),Rect(188,162,1,327),Rect(605,152,1,327)]
wallsMap1=[Rect(0,0,358,75),Rect(0,75,50,600),Rect(0,450,340,175),Rect(315,480,600,600),Rect(750,0,90,601),Rect(450,0,1000,75),Rect(460,280,200,150),Rect(0,0,800,1)]
wallsMap2=[Rect(400,0,500,121),Rect(680,0,300,384),Rect(0,550,1000,1000),Rect(0,0,65,1000),Rect(0,410,650,66),Rect(146,338,400,28),
           Rect(0,0,250,100),Rect(230,265,210,30),Rect(730,300,1000,300),Rect(200,110,72,80),Rect(232,190,111,38),Rect(232,190,350,20),
           Rect(64,302,12,14),Rect(602,349,11,17),Rect(0,396,800,0),Rect(0,157,800,0)]
wallsMap3=[Rect(0,0,400,200),Rect(0,0,90,1000),Rect(0,0,430,100),Rect(0,550,1000,100),Rect(0,0,1000,80),Rect(710,0,1000,1000),Rect(340,200,75,80),Rect(400,0,60,250)]
nWall=[Rect(203,156,412,1),Rect(203,156,1,306),Rect(203,462,412,1),Rect(615,156,1,412)]
martWall=[Rect(129,129,545,1),Rect(129,450,545,1),Rect(129,129,1,321),Rect(674,129,1,321)]
downWall=[Rect(213,144,377,1),Rect(213,392,377,1),Rect(213,144,1,248),Rect(591,144,1,248)]
wallsMapboss1=[Rect(0,166,800,0),Rect(0,442,800,0),Rect(92,140,25,129),Rect(0,272,800,45),Rect(333,246,27,30),Rect(334,150,30,61),Rect(438,149,30,120),Rect(544,151,30,300),Rect(620,150,30,93),
               Rect(620,207,102,36),Rect(757,207,100,38),Rect(378,321,25,60),Rect(351,347,57,30),Rect(184,321,60,31),Rect(213,347,98,33)]
wallsMapboss2=[Rect(145,138,510,319)]
battleWall=[Rect(0,0,800,0),Rect(0,0,0,600),Rect(800,0,0,600),Rect(0,600,800,0)]
test101=[Rect(1,1,1,1)]

ledge2=[Rect(80,270,140,20)]

inside=False


def drawScene(screen,player,walls):
    #screen.fill(0)  
    #draw.rect(screen,GREEN,player)


    
    for w in walls:
        draw.rect(screen,RED,w) 
    display.flip()

def movePlayer(player,mywalls,myledge):
    g = key.get_pressed()

    if (g[K_DOWN] or g[K_s]) and hitwalls(pos[X],pos[Y]+5,mywalls)==-1:
        pos[Y] += ws
    elif (g[K_UP] or g[K_w]) and hitwalls(pos[X],pos[Y]-5,mywalls)==-1 and hitwalls(pos[X],pos[Y]-5,myledge)==-1:
        pos[Y] -= ws
    elif (g[K_LEFT] or g[K_a]) and hitwalls(pos[X]-5,pos[Y],mywalls) == -1:
        pos[X] -= ws
    elif (g[K_RIGHT] or g[K_d]) and hitwalls(pos[X]+5,pos[Y],mywalls) == -1:
        pos[X] += ws

    if (g[K_DOWN] or g[K_s]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X],pos[Y]+5,mywalls) == -1:
        pos[Y] += rs
    elif (g[K_UP] or g[K_w]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X],pos[Y]-5,mywalls) == -1 and hitwalls(pos[X],pos[Y]-5,myledge) == -1:
        pos[Y] -= rs
    elif (g[K_LEFT] or g[K_a]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X]-5,pos[Y],mywalls) == -1:
        pos[X] -= rs
    elif (g[K_RIGHT] or g[K_d]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X]+5,pos[Y],mywalls) == -1:
        pos[X] += rs

def hitwalls(x,y,mywalls):
    playerRect = Rect(x,y,25,25)
    print(playerRect.collidelist(mywalls)) 
    return playerRect.collidelist(mywalls)


FirstMap=Rect(360,15,90,0)
SecondMap=Rect(280,75,90,0)
neighbour=Rect(500,220,60,0)
neighbourexit=Rect(345,417,55,1)
martbox=Rect(544,344,40,0)
martboxexit=Rect(373,437,55,1)
downtoout=Rect(373,384,59,1)
mapzero=Rect(493,270,1,44)
downtoup=Rect(516,197,1,23)
out_in=Rect(192,210,34,1)
back_one=Rect(360,529,80,1)

health=400
opphealth=400

downbox=Rect(215,450,40,0)
downbox2=Rect(290,450,40,0)
downbox3=Rect(500,278,1,6)

boss1=Rect(500,100,100,0)
tele1=Rect(57,187,1,8)    #short form for teleport
tele2=Rect(279,323,1,5)
tele3=Rect(396,186,1,6)
tele4=Rect(768,184,1,4)

battleRect=Rect(0,400,800,0)
battleRect2=Rect(0,171,800,0)
attack1=Rect(0,475,250,200)
attack2=Rect(200,475,250,200)
attack3=Rect(400,475,250,200)
attack4=Rect(600,475,250,200)
healthRect=(149,100,health,10)
opphealthRect=(149,70,opphealth,10)

t1Rect = Rect(593, 343, 35, 35)
t2Rect = Rect(393, 198, 35, 85)
t3Rect = Rect(58, 293, 35, 35)
t4Rect = Rect(293, 415, 35, 35)
t5Rect = Rect(318, 268, 35, 35)
t6Rect = Rect(233, 264, 35, 35)
t7Rect = Rect(383, 393, 35, 35)
t8Rect = Rect(318, 268, 35, 35)
t9Rect = Rect(318, 268, 35, 35)

running = True

clock = time.Clock()
level=0
mp = image.load("maps/map.png").convert()
mp1 = image.load("maps/map1.png").convert()
mp2 = image.load("maps/map6.png").convert()
neig = image.load("maps/neighbourWithBlack.png").convert()
pokemart = image.load("maps/pokecenterwithblack.png").convert()
housedownstairs = image.load("maps/downstairswithblack.png").convert()
bossmap1withblack = image.load("maps/bosswithblack1.png").convert()
bossmapwithblack = image.load("maps/bosswithblackfinal.png").convert()
battle1= image.load("maps/battle.png").convert()
bedroom1= image.load("maps/bedroom.png").convert()


attack1image= image.load("sprites/Attacks/atkbutton.png").convert()
attack2image= image.load("sprites/Attacks/ambbutton.png").convert()
attack3image= image.load("sprites/Attacks/chanbutton.png").convert()
attack4image= image.load("sprites/Attacks/healbutton.png").convert()

abraimage=image.load("sprites/ABRA/ABRA0.png").convert()
charimage= image.load("sprites/CHARMANDER/CHARMANDER00.png").convert()

map = transform.smoothscale(mp, (800, 600))
map1 = transform.smoothscale(mp1, (800, 600))
map2 = transform.smoothscale(mp2, (800, 600))
neigbourInside = transform.smoothscale(neig, (800, 600))
mart = transform.smoothscale(pokemart, (800, 600))
down = transform.smoothscale(housedownstairs, (800, 600))
boss1map = transform.smoothscale(bossmap1withblack, (800, 600))
boss2map = transform.smoothscale(bossmapwithblack, (800, 600))
battle = transform.smoothscale(battle1, (800, 600))
bedroom = transform.smoothscale(bedroom1, (800, 600))
abra = transform.smoothscale(abraimage, (120, 100))
char = transform.smoothscale(charimage, (170, 140))

atk1 = transform.smoothscale(attack1image, (150, 75))
atk2 = transform.smoothscale(attack2image, (150, 75))
atk3 = transform.smoothscale(attack3image, (150, 75))
atk4 = transform.smoothscale(attack4image, (150, 75))



direction = ["left", "right", "down", "up"]
walk = {d: [transform.smoothscale(image.load(i), (20, 24)) for i in glob("sprites\\Player\\walking\\" + d + "\\*.png")] for d in
        direction}
run = {d: [transform.smoothscale(image.load(i), (20, 24)) for i in glob("sprites\\Player\\running\\" + d + "\\*.png")] for d in
       direction}  # accesses all the pics from each direction folder and changes its size
throw = [transform.smoothscale(image.load(i), (125, 125)) for i in glob("sprites\\Player\\throwing\\*.png")]
fire = [transform.smoothscale(image.load(i), (100, 100)) for i in glob("sprites\\Attacks\\fire\\*.png")]
heart = [transform.smoothscale(image.load(i), (100, 100)) for i in glob("sprites\\Attacks\\heart\\*.png")]

t1 = transform.smoothscale(image.load("sprites/t1/down/1down1.png"), (23, 27))
t2 = transform.smoothscale(image.load("sprites/t2/down/2down1.png"), (23, 27))
t3 = transform.smoothscale(image.load("sprites/t3/right/3right1.png"), (23, 27))
t4 = transform.smoothscale(image.load("sprites/t4/up/4up1.png"), (23, 27))
t5 = transform.smoothscale(image.load("sprites/t5/down/5down1.png"), (23, 27))
t6 = transform.smoothscale(image.load("sprites/t6/down/6down1.png"), (23, 27))
t7 = transform.smoothscale(image.load("sprites/t7/down/7down1.png"), (23, 27))
t8 = transform.smoothscale(image.load("sprites/t8/down/8down2.png"), (23, 27))
t9 = transform.smoothscale(image.load("sprites/t9/down/9down2.png"), (23, 27))
t10 = transform.smoothscale(image.load("sprites/t10/down/10down2.png"), (23, 27))

t6text = transform.smoothscale(image.load("sprites/dialog/t6/t61.png"), (300, 100))
t61text = transform.smoothscale(image.load("sprites/dialog/t6/t62.png"), (300, 100))
t2text = transform.smoothscale(image.load("sprites/dialog/t2/t21.png"), (300, 100))
t7text = transform.smoothscale(image.load("sprites/dialog/t7/t71.png"), (300, 100))
t4text = transform.smoothscale(image.load("sprites/dialog/t4/t41.png"), (300, 100))
t1text = transform.smoothscale(image.load("sprites/dialog/t1/t11.png"), (300, 100))
t3text = transform.smoothscale(image.load("sprites/dialog/t3/t31.png"), (300, 100))
t5text = transform.smoothscale(image.load("sprites/dialog/t5/t51.png"), (300, 100))
t8text = transform.smoothscale(image.load("sprites/dialog/t8/t81.png"), (300, 100))
t9text = transform.smoothscale(image.load("sprites/dialog/t9/t91.png"), (300, 100))

grass1 = image.load("start/instructions1.png")
grass2 = image.load("start/instructions.png")

pokemon = ["CHARMANDER"]
#_________________________________--
bag = []
count = 0
background = 7
build=0
map2origin=0
anime = 0
charbag=0
battlenum=0
#___________________________________
throwani = -1
ani = 0
tw = False
#___________________________________
fireani = -1
anim = 0
fe = False
#____________________________________
attack=0
turn=1
#__________________________________
di = "down"
X=0

Y=1
pos=[360,400]
rs = 1
ws = 0.55
action = "walk"
actions = {"walk": walk, "run": run}
blitted = False

# -----------------------------
a=0
b=1
c=2
y=500
      #a b  c
g1 = [0,0,600]
g2=[0,-600,600]

runtime = 0
scrollspeed = 3

font.init()
mytext = font.SysFont("Arial", 30)
mytext1 = mytext.render("HEY", True, BLACK)
mytext2 = mytext.render("Rishi", True, BLACK)

def drawScene():
    screen.blit(grass1, (g1[a],g1[b]))
    screen.blit(grass2, (g2[a],g2[b]))
    # background scrolling
    g1[b] = g1[b] + scrollspeed
    if g1[b] + scrollspeed > g1[c]:
        g1[b] = -g2[c]
    g2[b] = g2[b] + scrollspeed
    if g2[b] + scrollspeed > g2[c]:
        g2[b] = -g1[c]
    print("first y=",g1[b],"second y=",g2[b])

click = False

myClock=time.Clock()
while running:
    g = key.get_pressed()
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                click = True

    screen.fill(0)
    col=GREEN
    clock.tick(60)


    anime += 1
    if anime % 7 == 0:  # speed of transition between pics
        count += 1

    speed = ws
    if g[K_LSHIFT] or g[K_RSHIFT]:
        action = "run"
        speed = rs
    else:
        action = "walk"

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    # if action == "run":
    #     speed = rs

#____________________________________________________________________________________________________________________________________________________________________________________________________________
    if level==6 and inside==False:
        movePlayer(walk,startWall,[])

    if level==7 and inside==False:
        movePlayer(walk,downWall,[])
        

    if build==1:
        movePlayer(walk,nWall,[])
        

    if level==1 and inside==False:
        movePlayer(walk,wallsMap1,[])
        
    elif level==2 and inside==False:
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

    elif level==5 and inside==False:
        movePlayer(walk,wallsMapboss2,[])

    elif build==5:
        movePlayer(walk,battleWall,[])


#____________________________________________________________________________________________________________________________

    if mb[0]==1 and attack1.collidepoint(mx,my):
        attack="1"
    if mb[0]==1 and attack2.collidepoint(mx,my):
        attack="2"
    if mb[0]==1 and attack3.collidepoint(mx,my):
        attack="3"
    if mb[0]==1 and attack4.collidepoint(mx,my):
        attack="4"


#_______________________________________________________________________________
        
    if health>=0 or opphealth>=0:
        if turn==1:
            time.wait(10)
            
            if attack == "1" and click == True:    #standard attack

                opphealth-=10
                #print(opphealth,"............opp health...........")

                if not fe:
                    fireani = 0
                fe = True

                if fireani != -1:
                    # print(True)
                    screen.blit(fire[fireani], (450, 263))
                    anim += 1
                    if anim % 10 == 0:
                        fireani += 1
                    if fireani == 4:
                        fireani = -1
                    print(fireani)

                click = False
                
                if health<=0 or opphealth<=0:
                    turn=3
                else:
                    turn=2

                draw.rect(screen,YELLOW,healthRect)
                draw.rect(screen,YELLOW,opphealthRect)
   
            elif attack=="2" and click==True:     #risky range attack

                a2=randint(0,22)
                opphealth=opphealth-a2
                #print(opphealth,"............opp health...........")
                click=False
                if health<=0 or opphealth<=0:
                    turn=3
                else:
                    turn=2
                

                draw.rect(screen,YELLOW,healthRect)
                draw.rect(screen,YELLOW,opphealthRect)        

            elif attack=="3" and click==True:   #extreme risk attack

                a3=randint(1,2)
                if a3==1:
                    opphealth+=10
                elif a3==2:
                   opphealth-=30
                #print(opphealth,"............opp health...........")
                click=False
                if health<=0 or opphealth<=0:
                    turn=3
                else:
                    turn=2

                draw.rect(screen,YELLOW,healthRect)
                draw.rect(screen,YELLOW,opphealthRect)
            elif attack=="4" and click==True:      #heal

                health+=15
                #print(health, "............player health...........")
                click=False

                draw.rect(screen,YELLOW,healthRect)
                draw.rect(screen,YELLOW,opphealthRect)                 
        elif turn==2:
            time.wait(100)
            time.wait(3)
            oppattack=randint(0,10)
            health=health-oppattack
            if health<=0 or opphealth<=0:
                turn=3
            else:
                turn=1
            #print(health, "............player health...........")
 
            draw.rect(screen,YELLOW,healthRect)
            draw.rect(screen,YELLOW,opphealthRect)

        if turn==3:
            time.wait(10)
            
            if health<=0:
                print('l')
            elif opphealth<=0:
                
                level=2
                background=1
                build=0
                opphealth=400
                if battlenum==1:
                    pos[X]=651
                    pos[Y]=357
                if battlenum==2:
                    pos[X]=612
                    pos[Y]=128
   
        
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


    #print(mx, "x value",my,"y value")
    
    playerRect=Rect(pos[X],pos[Y],18,21)
    draw.rect(screen,col,playerRect,1)                              
#__________________________________________________________________________________________________________________________________________________________________________________________________
    playerRect = Rect(pos[X],pos[Y],21,26)

    if background == 7:
        if runtime <= 500:
            runtime += 1

            drawScene()

            screen.blit(mytext1, (200, y))
            screen.blit(mytext2, (200, y + 50))
            y -= 1
            display.flip()
            myClock.tick(60)
            print(runtime)
        else:
            background = 0

  
    if background==0:
        level=6
        screen.blit(bedroom, (0, 0))
        for wm in startWall:
            draw.rect(screen,RED,wm,1)
        draw.rect(screen,AQUA,mapzero)
        


    if playerRect.colliderect(mapzero) and background==0:
        #print(level)
        background=5
        level=7
        pos[X]=527
        pos[Y]=222
    if background==5:
        for wm in downWall:
          draw.rect(screen,RED,wm,1)
        screen.blit(down, (0, 0))
        draw.rect(screen,BEIGE,downtoup)
        draw.rect(screen,BEIGE,out_in)
        draw.rect(screen, BEIGE, t5Rect, 1)
        screen.blit(t5, (325,275))
        if playerRect.colliderect(t5Rect):
            screen.blit(t5text, (250, 450))
        

    if playerRect.colliderect(downtoup) and background==5:
        background=0
        pos[X]=469
        pos[Y]=293

    if playerRect.colliderect(out_in) and background==6:
        background=5
        pos[X]=402
        pos[Y]=365
        level=7

    



        


    if playerRect.colliderect(downtoout) and background==5:
        #print(level)
        background=6
        level=1
        #pos[X]=235
        #pos[Y]=275
        pos[X]=210
        pos[Y]=232 
    if background==6:
        screen.blit(map, (0, 0))
        for wm in wallsMap1:
        
            draw.rect(screen,RED,wm,1)
        draw.rect(screen,AQUA,FirstMap)
        draw.rect(screen,AQUA,neighbour)
        

        



    #print(actions[action])

    #screen.blit((actions[action][di][count % 3]), (posx, posy))
   

    if playerRect.colliderect(neighbour) and background==6 and build==0:
        build=1
        pos[X]=300
        pos[Y]=200
        inside=True
        

    if background==6 and build==1:
        screen.blit(neigbourInside, (0, 0))
        for wm in nWall:
            draw.rect(screen, RED, wm, 2)
        #print("bye")
        screen.blit(t6, (240, 270))
        draw.rect(screen, BEIGE, t6Rect, 1)
        draw.rect(screen, BEIGE, neighbourexit)
        blitted = False
        if playerRect.colliderect(t6Rect):
            screen.blit(t6text, (250, 450))
            blitted = True
            bag.append("CHARMANDER")
            charbag=1
        if blitted == False and "CHARMANDER" in bag:
            screen.blit(t61text, (250, 450))

    if playerRect.colliderect(neighbourexit) and background==6 and build==1:
        build=0
        pos[X]=500
        pos[Y]=230
        inside=False
        

    #print(bag)

        
        

    if playerRect.colliderect(FirstMap) and charbag==1:
        background=1
        level=2
        #print("level 22222")
        #pos[X]=378
        #pos[Y]=522
        pos[X]=400
        pos[Y]=300
        
        
    if background==1:
        screen.blit(map1, (0, 0))
        screen.blit(t1, (600, 350))
        draw.rect(screen, BEIGE, t1Rect, 1)
        if playerRect.colliderect(t1Rect):
            screen.blit(t1text, (250, 450))
        screen.blit(t3, (65, 300))
        draw.rect(screen, BEIGE, t3Rect, 1)
        if playerRect.colliderect(t3Rect):
            screen.blit(t3text, (250, 450))
        for wm in wallsMap2:
            draw.rect(screen,RED,wm,2)
        for ledge in ledge2:
            draw.rect(screen,BLUE,ledge,2)
        #print("hi")

        #print(background, " issss background",build, "isssss build",level,"isss level")
        draw.rect(screen,BEIGE,SecondMap)
        draw.rect(screen,GREEN,battleRect)
        draw.rect(screen,GREEN,battleRect2)

    if playerRect.colliderect(SecondMap) and background == 1:

        col=BLACK
        level=3
        background=2
        #print("aaaaa")
        pos[X]=543
        pos[Y]=530

    if playerRect.colliderect(SecondMap) and background == 1:

        col=BLACK
        level=3
        background=2
        #print("aaaaa")
        pos[X]=543
        pos[Y]=530
        
    if background==2 and build==0:
        #print(background, " issss background",build, "isssss build",level,"isss level")
        for wm in wallsMap3:
            draw.rect(screen,RED,wm,3)
        screen.blit(map2, (0, 0))
        #playerRect=Rect(pos[X],pos[Y],16,22)

        draw.rect(screen,BEIGE,martbox)
        draw.rect(screen,BEIGE,downbox)
        draw.rect(screen,BEIGE,downbox2)
        draw.rect(screen,BEIGE,downbox2)
        draw.rect(screen,BEIGE,boss1)

    if playerRect.colliderect(martbox) and background==2 and build==0:
        build=2
        
        
        
        pos[X]=394
        pos[Y]=406
        inside=True
    if playerRect.colliderect(martboxexit) and background==2 and build==2:
        background=2
        build=0
        pos[X]=560
        pos[Y]=353
        inside=False

    if build==2 and background==2:
        # print(22)
        screen.blit(mart, (0, 0))
        screen.blit(t2, (400, 205))
        draw.rect(screen, BEIGE, t2Rect, 1)
        if playerRect.colliderect(t2Rect):
            screen.blit(t2text, (250, 450))
        for wm in martWall:
            draw.rect(screen,RED,wm,3)

    if build==3 and background==2:
        #print("32")
        level=7
        screen.blit(down, (0, 0))
        screen.blit(t8, (325, 275))
        draw.rect(screen, BEIGE, t8Rect, 1)
        if playerRect.colliderect(t8Rect):
            screen.blit(t8text, (250, 450))
        for wm in downWall:
            draw.rect(screen,RED,wm,3)
        draw.rect(screen,BEIGE,downtoout)

    if playerRect.colliderect(downbox) and background==2 and build==0:
        build=3

        
        pos[X]=353
        pos[Y]=338

    if playerRect.colliderect(downtoout) and background==2 and build==3:
        print(level)
        background=2
        build=0
        level=3
        inside=False
        pos[X]=229
        pos[Y]=458

    if build==4 and background==2:
        #print("42")
        level=7
        screen.blit(down, (0, 0))
        screen.blit(down, (0, 0))
        screen.blit(t9, (325, 275))
        draw.rect(screen, BEIGE, t9Rect, 1)
        if playerRect.colliderect(t9Rect):
            screen.blit(t9text, (250, 450))
        for wm in downWall:
            draw.rect(screen,RED,wm,3)
        draw.rect(screen,BEIGE,downtoout)


    if playerRect.colliderect(downbox2) and background==2 and build==0:
        build=4
        pos[X]=353
        pos[Y]=338

    if playerRect.colliderect(downtoout) and background==2 and build==4:
        print(level)
        background=2
        build=0
        level=3
        inside=False
        pos[X]=306
        pos[Y]=455

    if background==3:
        #print("52")
        screen.blit(boss1map, (0, 0))
        screen.blit(t4, (300, 422))
        draw.rect(screen, BEIGE, t4Rect, 1)
        if playerRect.colliderect(t4Rect):
            screen.blit(t4text, (250, 450))
        for wm in wallsMapboss1:
            draw.rect(screen,RED,wm,3)

        draw.rect(screen,BEIGE,tele1)
        draw.rect(screen,BEIGE,tele2)
        draw.rect(screen,BEIGE,tele3)
        draw.rect(screen,BEIGE,tele4)

    if playerRect.colliderect(boss1) and background==2:
        level=4
        background=3
        
        pos[X]=34
        pos[Y]=232

    if playerRect.colliderect(tele4) and background==3:
        level=5
        background=4
        
        pos[X]=397
        pos[Y]=421

    if background==4:
        
        screen.blit(boss2map, (0, 0))
        screen.blit(t7, (390, 400))
        draw.rect(screen, BEIGE, t7Rect, 1)
        if playerRect.colliderect(t7Rect):
            screen.blit(t7text, (250, 450))
        for wm in wallsMapboss2:
            draw.rect(screen,RED,wm,3)



#_______________________________________________________________________________________

    if playerRect.colliderect(tele1) and background==3:
        pos[X]=151
        pos[Y]=395

    if playerRect.colliderect(tele2) and background==3:
        pos[X]=150
        pos[Y]=206

    if playerRect.colliderect(tele3) and background==3:
        pos[X]=590
        pos[Y]=244
#_________________________________________________________________________________________

    if playerRect.colliderect(battleRect) and background==1:
        pos[X]=590
        pos[Y]=244

        build=5
        battlenum=1
    if playerRect.colliderect(battleRect2) and background==1:
        pos[X]=590
        pos[Y]=244
        health=600
        opphealth=600

        build=5
        turn=1
        battlenum=2

    build = 5
    background = 1

    if build==5 and background==1:
        if not tw:
            throwani = 0
        tw = True
        #print("52")
        screen.blit(battle, (0, 0))

        #print(throwani)

        for wm in battleWall:
            draw.rect(screen,RED,wm,3)
        draw.rect(screen,RED,attack1)
        draw.rect(screen,BLUE,attack2)
        draw.rect(screen,GREEN,attack3)
        draw.rect(screen,YELLOW,attack4)

        screen.blit(atk1,(25,500))
        screen.blit(atk2,(225,500))
        screen.blit(atk3,(424,500))
        screen.blit(atk4,(629,500))
        screen.blit(abra,(485,263))
        screen.blit(char,(220,325))

        if throwani != -1:
            # print(True)
            screen.blit(throw[throwani], (150, 330))
            ani += 1
            if ani % 10 == 0:
                throwani += 1
            if throwani == 5:
                throwani = -1
            # print(throwani)

#_________________________________________________________________________________________________________________________________________________________________________________________        
    draw.rect(screen,col,playerRect,1)
    screen.blit((actions[action][di][count % 3]), (pos[X], pos[Y]))
    #print (pos[X],"x value",pos[Y],"y value")
    
    display.flip()
    myClock.tick(60)

quit()
