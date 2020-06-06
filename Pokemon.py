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


musics = ["Music/Music.mp3", "Music/Battle.mp3"]   #music list
inc = 0.1   #volume for music

init()

mixer.music.load(musics[0])  # music plays infintely as the program runs
mixer.music.play(-1)
mixer.music.set_volume(inc)


width, height = 800, 600
screen = display.set_mode((width, height))
RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)             #colours
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
AQUA = (3, 252, 182)
BEIGE = (250, 245, 112)

startWall = [Rect(188, 162, 417, 0), Rect(188, 489, 417, 0), Rect(188, 162, 1, 327), Rect(605, 152, 1, 327)]
wallsMap1 = [Rect(0, 0, 358, 75), Rect(0, 75, 50, 600), Rect(0, 450, 340, 175), Rect(315, 480, 600, 600),
             Rect(750, 0, 90, 601), Rect(450, 0, 1000, 75), Rect(460, 280, 200, 150), Rect(0, 0, 800, 1)]
wallsMap2 = [Rect(400, 0, 500, 121), Rect(680, 0, 300, 384), Rect(0, 550, 1000, 1000), Rect(0, 0, 65, 1000),            #These are walls used to block off locations it the game
             Rect(0, 410, 511, 48), Rect(146, 338, 400, 28),
             Rect(0, 0, 115, 100), Rect(115, 0, 135, 75), Rect(230, 265, 279, 30), Rect(730, 300, 1000, 300),
             Rect(200, 110, 72, 80), Rect(232, 190, 111, 38), Rect(232, 190, 350, 20),
             Rect(64, 302, 12, 14), Rect(602, 349, 11, 17), Rect(0, 442, 648, 0), Rect(200, 157, 800, 0),
             Rect(656, 415, 1, 50)]
wallsMap3 = [Rect(0, 0, 400, 200), Rect(0, 0, 90, 1000), Rect(0, 0, 430, 100), Rect(0, 550, 1000, 100),
             Rect(0, 0, 1000, 80), Rect(710, 0, 1000, 1000), Rect(340, 200, 75, 80), Rect(400, 0, 60, 250)]                 #These are walls used to block off locations it the game
nWall = [Rect(203, 197, 412, 1), Rect(203, 197, 1, 306), Rect(203, 462, 412, 1), Rect(615, 197, 1, 412),
         Rect(247, 275, 8, 13), Rect(202, 428, 412, 1)]
martWall = [Rect(129, 129, 545, 1), Rect(129, 450, 545, 1), Rect(129, 129, 1, 321), Rect(674, 129, 1, 321),
            Rect(281, 193, 232, 67)]
downWall = [Rect(213, 144, 377, 1), Rect(213, 392, 377, 1), Rect(213, 144, 1, 248), Rect(591, 144, 1, 248),
            Rect(330, 280, 9, 15)]
wallsMapboss1 = [Rect(0, 166, 800, 0), Rect(0, 442, 800, 0), Rect(92, 140, 25, 129), Rect(0, 272, 800, 45),
                 Rect(333, 246, 27, 30), Rect(334, 150, 30, 61), Rect(438, 149, 30, 120), Rect(544, 151, 30, 300),              #These are walls used to block off locations it the game
                 Rect(620, 150, 30, 93),
                 Rect(620, 207, 102, 36), Rect(757, 207, 100, 38), Rect(378, 321, 25, 60), Rect(351, 347, 57, 30),
                 Rect(184, 321, 60, 31), Rect(213, 347, 98, 33)]
wallsMapboss2 = [Rect(145, 138, 510, 319)]
battleWall = [Rect(0, 0, 800, 0), Rect(0, 0, 0, 600), Rect(800, 0, 0, 600), Rect(0, 600, 800, 0)]
test101 = [Rect(1, 1, 1, 1)]
introRect=[Rect(0,0,800,0),Rect(0,0,0,600),Rect(0,600,800,0),Rect(800,0,0,600)]

ledge2 = [Rect(80, 270, 140, 20), Rect(354, 230, 147, 3), Rect(656, 454, 150, 1), Rect(154, 498, 154, 3),
          Rect(360, 498, 500, 1),Rect(10,194,240,0)]                                                                            #These are ledges which a player can only walk one direction on. The other way is blocked

inside = False


def drawScene(screen, player, walls):
    # screen.fill(0)
    # draw.rect(screen,GREEN,player)                        #This function draws the walls

    for w in walls:   #each wall in the list
        draw.rect(screen, RED, w)
    display.flip()


def movePlayer(player, mywalls, myledge):
    #This function checks to see if the player is hitting a wall or a ledge (via the function "hitwalls") if not it will move the player
    g = key.get_pressed()

    if (g[K_DOWN] or g[K_s]) and hitwalls(pos[X], pos[Y] + 5, mywalls) == -1:  #upwards walk
        pos[Y] += ws
    elif (g[K_UP] or g[K_w]) and hitwalls(pos[X], pos[Y] - 5, mywalls) == -1 and hitwalls(pos[X], pos[Y] - 5,myledge) == -1:   #downwards walk
        pos[Y] -= ws
    elif (g[K_LEFT] or g[K_a]) and hitwalls(pos[X] - 5, pos[Y], mywalls) == -1:     #walking in the left direction
        pos[X] -= ws
    elif (g[K_RIGHT] or g[K_d]) and hitwalls(pos[X] + 5, pos[Y], mywalls) == -1:    #walking in the right direction
        pos[X] += ws

    if (g[K_DOWN] or g[K_s]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X], pos[Y] + 5, mywalls) == -1:    #running upwards
        pos[Y] += rs
    elif (g[K_UP] or g[K_w]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X], pos[Y] - 5,mywalls) == -1 and hitwalls(pos[X],pos[Y] - 5,myledge) == -1:    #running downwards
        pos[Y] -= rs
    elif (g[K_LEFT] or g[K_a]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X] - 5, pos[Y], mywalls) == -1:   #running to the left
        pos[X] -= rs
    elif (g[K_RIGHT] or g[K_d]) and (g[K_LSHIFT] or g[K_RSHIFT]) and hitwalls(pos[X] + 5, pos[Y], mywalls) == -1:  #running to the right
        pos[X] += rs


def hitwalls(x, y, mywalls):
    'Checks if the player makes contact with the walls'
    playerRect = Rect(x, y, 25, 25)
    return playerRect.collidelist(mywalls)

#te following are rectangles used to enter new places
FirstMap = Rect(360, 15, 90, 0)   #1st to 2nd map
FirstMapReverse = Rect(358, 545, 80, 1)  #2nd to first map
SecondMap = Rect(280, 66, 90, 0)   #2nd to third map
neighbour = Rect(500, 220, 60, 0)   #go inside neigbour's house
neighbourexit = Rect(345, 417, 55, 1)   #exiting neighbours house
martbox = Rect(544, 344, 40, 0)    #entering mart
martboxexit = Rect(373, 437, 55, 1)    #exiting mart
downtoout = Rect(373, 384, 59, 1)    #down stairs of home to out
mapzero = Rect(493, 270, 1, 44)     
doc_to_out = Rect(493, 270, 1, 44)      #doctor house to out
house_up = Rect(517, 198, 1, 28) 
downtoup = Rect(516, 197, 1, 23)
out_in = Rect(192, 210, 34, 1)
back_one = Rect(360, 529, 80, 1)

health = 1000   #player health
opphealth = 400    #oponent health
totaldamage=0    
opptotaldamage=0

downbox = Rect(215, 450, 40, 0)    
downbox2 = Rect(290, 450, 40, 0)
downbox3 = Rect(500, 278, 1, 6)

boss1 = Rect(500, 100, 100, 0)#ntering the boss map
tele1 = Rect(57, 187, 1, 8)  # short form for teleport1. Used for teleporation in boss lab
tele2 = Rect(279, 323, 1, 5)
tele3 = Rect(396, 186, 1, 6)
tele4 = Rect(768, 184, 1, 4)

battleRect = Rect(0, 453, 649, 0)    #first fight
battleRect2 = Rect(270, 171, 800, 0)   #second fight
attack1 = Rect(0, 475, 250, 200)   #attack/move 1
attack2 = Rect(200, 475, 250, 200) #attack/move 2
attack3 = Rect(400, 475, 250, 200) #attack/move 3
attack4 = Rect(600, 475, 250, 200) #attack/move 4

#the following are rects for character to player communication
t1Rect = Rect(593, 343, 35, 35)
t2Rect = Rect(393, 198, 35, 85)
t3Rect = Rect(58, 293, 35, 35)
t4Rect = Rect(293, 415, 35, 35)
t5Rect = Rect(318, 268, 35, 35)
t6Rect = Rect(233, 264, 35, 35)
t7Rect = Rect(383, 393, 35, 35)
t8Rect = Rect(318, 268, 35, 35)
t9Rect = Rect(318, 268, 35, 35)


restartRect=Rect(73,444,647,89)  #rectangle to restart game when you lose

keyRect = Rect(270, 440, 25, 25) #This is the key rectangle. You have to collect the key to enter the boss lab

running = True

clock = time.Clock()
level = 15   #this is the level for the intro
#the following are images for the game
mp = image.load("maps/map.png").convert()
mp1 = image.load("maps/map1.png").convert()
mp2 = image.load("maps/map6.png").convert()
neig = image.load("maps/neighbourWithBlack.png").convert()
pokemart = image.load("maps/pokecenterwithblack.png").convert()
housedownstairs = image.load("maps/downstairswithblack.png").convert()
bossmap1withblack = image.load("maps/bosswithblack1.png").convert()
bossmapwithblack = image.load("maps/bosswithblackfinal.png").convert()
battle1 = image.load("maps/battle.png").convert()
bedroom1 = image.load("maps/bedroom.png").convert()

attack1image = image.load("sprites/Attacks/atkbutton.png").convert()
attack2image = image.load("sprites/Attacks/ambbutton.png").convert()
attack3image = image.load("sprites/Attacks/chanbutton.png").convert()
attack4image = image.load("sprites/Attacks/healbutton.png").convert()

abraimage = image.load("sprites/ABRA/ABRA0.png").convert()
charimage = image.load("sprites/CHARMANDER/CHARMANDER00.png").convert()
mewtwoimage = image.load("sprites/MEWTWO/MEWTWO.png").convert()
pidgeyimage = image.load("sprites/PIDGEY/PIDGEY0.png").convert()

finalbattletitle_og = image.load("sprites/GameOver/pokefinal.png").convert()

loss_original = image.load("sprites/GameOver/endofgame.png").convert()
winoriginal=image.load("maps/win.png").convert

#the following are the same images cropped
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
finalbattletitle = transform.smoothscale(finalbattletitle_og, (800, 600))
lossoriginal = transform.smoothscale(loss_original, (800, 600))
mewtwo = transform.smoothscale(mewtwoimage, (120, 100))
pidgey = transform.smoothscale(pidgeyimage, (120, 100))
#win1 = transform.smoothscale(winoriginal, (800, 600))

atk1 = transform.smoothscale(attack1image, (150, 75))
atk2 = transform.smoothscale(attack2image, (150, 75))     #------images for the attack buttons
atk3 = transform.smoothscale(attack3image, (150, 75))
atk4 = transform.smoothscale(attack4image, (150, 75))

direction = ["left", "right", "down", "up"]   #direction for walking and running
walk = {d: [transform.smoothscale(image.load(i), (20, 24)) for i in glob("sprites\\Player\\walking\\" + d + "\\*.png")]
        for d in
        direction}
run = {d: [transform.smoothscale(image.load(i), (20, 24)) for i in glob("sprites\\Player\\running\\" + d + "\\*.png")]
       for d in direction}  # accesses all the pics from each direction folder and changes its size

throw = [transform.smoothscale(image.load(i), (125, 125)) for i in glob("sprites\\Player\\throwing\\*.png")]   #throwing animation
fire = [transform.smoothscale(image.load(i), (50, 50)) for i in glob("sprites\\Attacks\\fire\\*.png")]   #fire animation for battle
heart = [transform.smoothscale(image.load(i), (50, 50)) for i in glob("sprites\\Attacks\\heart\\*.png")]    #heal animation for battle

#these are the images for the side characters
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

#this is the text for the side characters
t6text = transform.smoothscale(image.load("sprites/dialog/t6/t61.png"), (350, 150))
t61text = transform.smoothscale(image.load("sprites/dialog/t6/t62.png"), (350, 150))
t2text = transform.smoothscale(image.load("sprites/dialog/t2/t21.png"), (350, 150))
t7text = transform.smoothscale(image.load("sprites/dialog/t7/t71.png"), (350, 150))
t4text = transform.smoothscale(image.load("sprites/dialog/t4/t41.png"), (350, 150))
t1text = transform.smoothscale(image.load("sprites/dialog/t1/t11.png"), (350, 150))
t3text = transform.smoothscale(image.load("sprites/dialog/t3/t31.png"), (350, 150))
t5text = transform.smoothscale(image.load("sprites/dialog/t5/t51.png"), (350, 150))
t8text = transform.smoothscale(image.load("sprites/dialog/t8/t81.png"), (350, 150))
t9text = transform.smoothscale(image.load("sprites/dialog/t9/t91.png"), (350, 150))
keytext = transform.smoothscale(image.load("sprites/dialog/key.png"), (300, 100))

grass1 = image.load("start/instructions1.png")  
grass2 = image.load("start/instructions.png")

pokemon = ["CHARMANDER"]    #This is the players pokemon
# _________________________________-
#these are different variables used throughout the game
bag = []
count = 0
background = 7   #used to identify which background a.k.a map it is
build = 0           #used to identify which building it is
anime=0  #frame rate between pictures
count=0
charbag = 0     #used to makes sure the player has a charzard before entering the next map
battlenum = 0   #used to find out which of the three battles is going on 
# __________________________________
#this is the throwing animation at the start of the game
throwani = -1
ani = 0
tw = False
# ___________________________________
#this is the fire animation at the start of the game
fireani = -1
anim = 0
fe = False
changex, changey = 410, 325
# ___________________________________
#this is the heal animation at the start of the game
heartani = -1
an = 0
ht = False
changeX, changeY = 525, 225
changeXx, changeYy = 290, 300
# ____________________________________
attack = 0   #variable for which attack it is
turn = 1    #variable for whos turn it is
angle = 210     #variable for which attack it is
restart=0   #variable for restarting the game if it equals 1
# __________________________________
key1 = 0   #variable for the key to the lab
# ________________________________
di = "down"   #direction starts as down
X = 0
Y = 1
pos = [320,108] #starting position           #[360, 400]
# ___________________________________
rs = 1.25   #running speed
ws = 0.75  # walking speed
action = "walk"
actions = {"walk": walk, "run": run}
blitted = False

# -----------------------------
a = 0
b = 1
c = 2
y = 500
# a b  c
g1 = [0, 0, 600]   #list to access during the scrolling
g2 = [0, -600, 600] #list to access during the scrolling

runtime = 0
bosstimer_1 = 0
bosstimer_2 = 0
losstimer=0
scrollspeed = 3  #speed for scroll (intro)

ak1=20
x=0

#The following is the words at the intro. (instruction storyline etc.)
l1 = "Pokémon Ballerz brought to you by Nishanth and Rishi"             #---------------------
l2 = "Coroger, the leader of Team Galactic needs to be defeated"
l3 = "before he enslaves all Pokémon! Get advice and tips from"
l4 = "various side characters and train and evolve your Pokémon"
l5 = "through battle to become powerful enough to stop Coroger!"
l6 = "You will need to locate a special key to be able to enter"        #----------------------
l7 = "the Research Center; so make sure to search every inch"
l8 = "of every building! "
l9 = "Controls and Movement"                                            #----------------------
l10 = "You can use the arrow keys or “w (up), a (left), s (down),"
l11 = "d (right) to walk around. Holding the shift button while"
l12 = "walking allows your character to sprint."
l13 = "The Battle"                                                      #----------------------
l14 = "The objective of a battle is to get the opposing Pokémon’s"
l15 = "health points to zero through a series of attacks."
l16 = "You have 4 moves to use in battle:"
l17 = "Attack: a consistent but mild attack"
l18 = "Ambush: a surprise attack deals a random amount of damage"
l19 = "Chance: does tons of damage or it heals the opponent fully"
l20 = "Heal: increases your health"
l21 = "After each battle won all 4 of these moves will become"
l22 = "more powerful. But if you lose in a battle you will be"
l23 = "sent back to your house so you can try again!"
l24 = "Buildings"                                                       #----------------------
l25 = "1 main function in this game. It's to give you information,"
l26 = "guide and help you through the game."
l27 = "Coroger’s Laboratory"                                            #----------------------
l28 = "The final destination of the game. Entering this stage will"
l29 = "require collecting a special key hidden in a building. If"
l30 = "your strong and smart enough, you will be able to protect"
l31 = "the Pokémon World from Coroger’s twisted plans!"
l32 = "Good Luck Trainer!"                                              #----------------------




#The following is blitting the intor words
font.init()
mytext = font.SysFont("Arial", 30)
mytext1 = mytext.render(l1, True, BLACK)
mytext2 = mytext.render(l2, True, BLACK)
mytext3 = mytext.render(l3, True, BLACK)
mytext4 = mytext.render(l4, True, BLACK)
mytext5 = mytext.render(l5, True, BLACK)
mytext6 = mytext.render(l6, True, BLACK)
mytext7 = mytext.render(l7, True, BLACK)
mytext8 = mytext.render(l8, True, BLACK)
mytext9 = mytext.render(l9, True, BLACK)
mytext10 = mytext.render(l10, True, BLACK)
mytext11 = mytext.render(l11, True, BLACK)
mytext12 = mytext.render(l12, True, BLACK)
mytext13 = mytext.render(l13, True, BLACK)
mytext14 = mytext.render(l14, True, BLACK)
mytext15 = mytext.render(l15, True, BLACK)
mytext16 = mytext.render(l16, True, BLACK)
mytext17 = mytext.render(l17, True, BLACK)
mytext18 = mytext.render(l18, True, BLACK)
mytext19 = mytext.render(l19, True, BLACK)
mytext20 = mytext.render(l20, True, BLACK)
mytext21 = mytext.render(l21, True, BLACK)
mytext22 = mytext.render(l22, True, BLACK)
mytext23 = mytext.render(l23, True, BLACK)
mytext24 = mytext.render(l24, True, BLACK)
mytext25 = mytext.render(l25, True, BLACK)
mytext26 = mytext.render(l26, True, BLACK)
mytext27 = mytext.render(l27, True, BLACK)
mytext28 = mytext.render(l28, True, BLACK)
mytext29 = mytext.render(l29, True, BLACK)
mytext30 = mytext.render(l30, True, BLACK)
mytext31 = mytext.render(l31, True, BLACK)
mytext32 = mytext.render(l32, True, BLACK)



def drawScene():
    'draws the intro/ infinite scroll feature'
    screen.blit(grass1, (g1[a], g1[b]))
    screen.blit(grass2, (g2[a], g2[b]))
    # background scrolling
    g1[b] = g1[b] + scrollspeed
    if g1[b] + scrollspeed > g1[c]:
        g1[b] = -g2[c]
    g2[b] = g2[b] + scrollspeed
    if g2[b] + scrollspeed > g2[c]:
        g2[b] = -g1[c]
    # print("first y=", g1[b], "second y=", g2[b])


myClock = time.Clock()
while running:
    click = False
    g = key.get_pressed()
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                click = True

    screen.fill(0)
    col = GREEN
    clock.tick(60)

    if turn == 3:
        mixer.music.load(musics[0])  # music plays infintely as the program runs
        mixer.music.play(-1)
    # introIn += 1

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

    oppcharacter=[abra, pidgey, mewtwo]   #enemy pokemons



    # ____________________________________________________________________________________________________________________________________________________________________________________________________________
#the following check to see if certain variables match up which leads to specific map walls beings drawn.
    if level == 6 and inside == False:   #upstairs home
        movePlayer(walk, startWall, [])    

    if build == 8 :                         #upstairs for other houses
        movePlayer(walk, startWall, [])

    if level == 7 and inside == False:    #downstairs home
        movePlayer(walk, downWall, [])

    if build == 1:
        movePlayer(walk, nWall, [])     #neighbour map

    if level == 1 and inside == False:      #first map (player and neighbour house)
        movePlayer(walk, wallsMap1, [])

    elif level == 2 and inside == False:    #second map (forest)
        movePlayer(walk, wallsMap2, ledge2)

    elif level == 3 and inside == False:      #third map (city)
        movePlayer(walk, wallsMap3, [])

    elif build == 2:    #pokemart
        movePlayer(walk, martWall, [])

    elif build == 3:        #downstairs for other houses (1st on last map)
        movePlayer(walk, downWall, [])

    elif build == 4:     #downstairs for other houses (2nd on last map)
        movePlayer(walk, downWall, [])

    elif level == 4 and inside == False:     #boss map lobby
        movePlayer(walk, wallsMapboss1, [])

    elif level == 5 and inside == False:     #boss map final
        movePlayer(walk, wallsMapboss2, [])

    elif build == 5:     #during battle
        movePlayer(walk, battleWall, [])
    elif level ==15:          #during intro to let the player roam around and get used to the character
        movePlayer(walk,introRect,[])

    # ____________________________________________________________________________________________________________________________
#The following check which attacks or power gets selected during combat
    if mb[0] == 1 and attack1.collidepoint(mx, my):
        attack = "1"
    if mb[0] == 1 and attack2.collidepoint(mx, my):
        attack = "2"
    if mb[0] == 1 and attack3.collidepoint(mx, my):
        attack = "3"
    if mb[0] == 1 and attack4.collidepoint(mx, my):
        attack = "4"
    if mb[0]==1 and restartRect.collidepoint(mx,my):
       restart="1"

    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if g[K_UP] or g[K_w]:
        di = "up"

    elif g[K_LEFT] or g[K_a]:
        di = "left"
                                                #this is what direction the player faces
    elif g[K_DOWN] or g[K_s]:
        di = "down"

    elif g[K_RIGHT] or g[K_d]:
        di = "right"

    else:
        count = 0

    print(mx, "x value", my, "y value")

    playerRect = Rect(pos[X], pos[Y], 18, 21)
    draw.rect(screen, col, playerRect, 1)
    # __________________________________________________________________________________________________________________________________________________________________________________________________
    playerRect = Rect(pos[X], pos[Y], 21, 26)     #draws the hitbox around the main player

    if background == 7:     #intro infinite scroll screen
        level=15
        if runtime <= 2:    #2175
            runtime += 1

            drawScene()
            #The following is the words that is visible 
            screen.blit(mytext1, (35, y))           #----------------------
            screen.blit(mytext2, (15, y + 80))
            screen.blit(mytext3, (15, y + 120))
            screen.blit(mytext4, (15, y + 160))
            screen.blit(mytext5, (15, y + 200))
            screen.blit(mytext6, (15, y + 260))     #----------------------
            screen.blit(mytext7, (15, y + 300))
            screen.blit(mytext8, (15, y + 340))
            screen.blit(mytext9, (15, y + 420))     #----------------------
            screen.blit(mytext10, (15, y + 480))
            screen.blit(mytext11, (15, y + 520))
            screen.blit(mytext12, (15, y + 560))
            screen.blit(mytext13, (15, y + 640))     #----------------------
            screen.blit(mytext14, (15, y + 700))
            screen.blit(mytext15, (15, y + 740))
            screen.blit(mytext16, (15, y + 800))    #----------------------
            screen.blit(mytext17, (15, y + 840))
            screen.blit(mytext18, (15, y + 880))
            screen.blit(mytext19, (15, y + 920))
            screen.blit(mytext20, (15, y + 960))
            screen.blit(mytext21, (15, y + 1020))    #----------------------
            screen.blit(mytext22, (15, y + 1060))
            screen.blit(mytext23, (15, y + 1100))
            screen.blit(mytext24, (15, y + 1180))   #----------------------
            screen.blit(mytext25, (15, y + 1240))
            screen.blit(mytext26, (15, y + 1280))
            screen.blit(mytext27, (15, y + 1360))   #----------------------
            screen.blit(mytext28, (15, y + 1420))
            screen.blit(mytext29, (15, y + 1460))
            screen.blit(mytext30, (15, y + 1500))
            screen.blit(mytext31, (15, y + 1540))
            screen.blit(mytext32, (250, y + 1620))       #----------------------


            y -= 1
            screen.blit((actions[action][di][count % 3]), (pos[X], pos[Y]))
            display.flip()
            myClock.tick(60)
            print(runtime)
        else:
            background = 0
            pos[X]=400
            pos[Y]=300

    if background == 0:
        level = 6
        screen.blit(bedroom, (0, 0))
        for wm in startWall:
            draw.rect(screen, RED, wm, 1)
        draw.rect(screen, AQUA, mapzero)

    if playerRect.colliderect(mapzero) and background == 0:
        # print(level)
        background = 5
        level = 7
        pos[X] = 527
        pos[Y] = 222
    if background == 5:
        for wm in downWall:
            draw.rect(screen, RED, wm, 1)
        screen.blit(down, (0, 0))
        draw.rect(screen, BEIGE, downtoup)
        draw.rect(screen, BEIGE, out_in)
        draw.rect(screen, BEIGE, t5Rect, 1)
        screen.blit(t5, (325, 275))
        if playerRect.colliderect(t5Rect):
            screen.blit(t5text, (225, 425))

    if playerRect.colliderect(downtoup) and background == 5:
        background = 0
        pos[X] = 469
        pos[Y] = 293

    if playerRect.colliderect(out_in) and background == 6:
        background = 5
        pos[X] = 402
        pos[Y] = 345
        level = 7

    if playerRect.colliderect(downtoout) and background == 5:
        # print(level)
        background = 6
        level = 1
        # pos[X]=235
        # pos[Y]=275
        pos[X] = 210
        pos[Y] = 232
    if background == 6:
        screen.blit(map, (0, 0))
        for wm in wallsMap1:
            draw.rect(screen, RED, wm, 1)
        draw.rect(screen, AQUA, FirstMap)
        draw.rect(screen, AQUA, neighbour)

    # print(actions[action])

    # screen.blit((actions[action][di][count % 3]), (posx, posy))

    if playerRect.colliderect(neighbour) and background == 6 and build == 0:
        build = 1
        pos[X] = 309
        pos[Y] = 396
        inside = True

    if background == 6 and build == 1:
        screen.blit(neigbourInside, (0, 0))
        for wm in nWall:
            draw.rect(screen, RED, wm, 2)
        # print("bye")
        screen.blit(t6, (240, 270))
        draw.rect(screen, BEIGE, t6Rect, 1)
        draw.rect(screen, BEIGE, neighbourexit)
        blitted = False
        if playerRect.colliderect(t6Rect):
            screen.blit(t6text, (225, 425))
            blitted = True
            bag.append("CHARMANDER")
            charbag = 1
        if blitted == False and "CHARMANDER" in bag:
            screen.blit(t61text, (250, 425))

    if playerRect.colliderect(neighbourexit) and background == 6 and build == 1:
        build = 0
        pos[X] = 500
        pos[Y] = 230
        inside = False

    # print(bag)

    if playerRect.colliderect(FirstMap) and charbag == 1:
        background = 1
        level = 2
        # print("level 22222")
        # pos[X]=378
        # pos[Y]=522
        pos[X] = 399
        pos[Y] = 509

    if background == 1:
        screen.blit(map1, (0, 0))
        screen.blit(t1, (600, 350))
        draw.rect(screen, BEIGE, t1Rect, 1)
        if playerRect.colliderect(t1Rect):
            screen.blit(t1text, (225, 425))
        screen.blit(t3, (65, 300))
        draw.rect(screen, BEIGE, t3Rect, 1)
        if playerRect.colliderect(t3Rect):
            screen.blit(t3text, (225, 425))
        for wm in wallsMap2:
            draw.rect(screen, RED, wm, 2)
        for ledge in ledge2:
            draw.rect(screen, BLUE, ledge, 2)
        # print("hi")

        # print(background, " issss background",build, "isssss build",level,"isss level")
        draw.rect(screen, BEIGE, SecondMap)
        draw.rect(screen, BEIGE, FirstMapReverse)
        draw.rect(screen, GREEN, battleRect)
        draw.rect(screen, GREEN, battleRect2)

    if playerRect.colliderect(FirstMapReverse) and background == 1:
        background = 6
        level = 1
        pos[X] = 395
        pos[Y] = 40

    
    if playerRect.colliderect(SecondMap) and background == 1:
        col = BLACK
        level = 3
        background = 2
        build=0
        turn=0
        
        print("background......",background,"level.........",level,"Build...............",build)
        pos[X] = 644
        pos[Y] = 409


    if background == 2 and build == 0:
        print(background, " issss background",build, "isssss build",level,"isss level")
        for wm in wallsMap3:
            draw.rect(screen, RED, wm, 3)
        screen.blit(map2, (0, 0))
        # playerRect=Rect(pos[X],pos[Y],16,22)

        draw.rect(screen, BEIGE, martbox)
        draw.rect(screen, BEIGE, downbox)
        draw.rect(screen, BEIGE, downbox2)
        draw.rect(screen, BEIGE, downbox2)
        draw.rect(screen, BEIGE, boss1)

    if playerRect.colliderect(martbox) and background == 2 and build == 0:
        build = 2

        pos[X] = 394
        pos[Y] = 406
        inside = True
    if playerRect.colliderect(martboxexit) and background == 2 and build == 2:
        background = 2
        build = 0
        pos[X] = 560
        pos[Y] = 353
        inside = False

    if build == 2 and background == 2:
        # print(22)
        screen.blit(mart, (0, 0))
        screen.blit(t2, (400, 205))
        draw.rect(screen, BEIGE, t2Rect, 1)
        if playerRect.colliderect(t2Rect):
            screen.blit(t2text, (225, 425))
        for wm in martWall:
            draw.rect(screen, RED, wm, 3)
    # _______________________________________________________________________________________________________________________________________

    if build == 3 and background == 2:
        # print("32")

        level = 7
        screen.blit(down, (0, 0))
        screen.blit(t8, (325, 275))
        draw.rect(screen, BEIGE, t8Rect, 1)
        if playerRect.colliderect(t8Rect):
            screen.blit(t8text, (225, 425))
        for wm in downWall:
            draw.rect(screen, RED, wm, 3)
        draw.rect(screen, GREEN, downtoout)
        # draw.rect(screen,AQUA,house_out)
        inside = True

    if playerRect.colliderect(downbox) and background == 2 and build == 0:  # Go inside
        build = 3

        pos[X] = 353
        pos[Y] = 358

    if playerRect.colliderect(downtoout) and background == 2 and build == 3:  # Downstairs to out
        # print(level)
        background = 2
        build = 0
        level = 3
        battlenum=0
        inside=False

      #  pos[X] = 229
    #    pos[Y] = 458

    if playerRect.colliderect(house_up) and background == 2 and build == 3:  # downstairs to upstairs
        # print(level)

        build = 8
        level = 8
        pos[X] = 459
        pos[Y] = 295
        inside=True



    if background == 2 and build == 8:  # upstairs
        #level = 8
        screen.blit(bedroom, (0, 0))
        draw.rect(screen, BEIGE, keyRect, 1)
        if playerRect.colliderect(keyRect):
            blitted = True
            screen.blit(keytext, (250, 493))
        if blitted == True:
            key1 = 1
        # print(key1)

        #print(level, "......level", background, "......background", build, "........build")
        for wm in startWall:
            draw.rect(screen, RED, wm, 1)
        draw.rect(screen, AQUA, doc_to_out)

    if playerRect.colliderect(doc_to_out) and background==2 and build==8:    #upstairs to downstairs
        # print(level)
        background=2
        build=3
        level=7
        
        pos[X]=554
        pos[Y]=224



    # _____________________________________________________________________________________________________________

    if build == 4 and background == 2:
        # print("42")
        level = 7
        screen.blit(down, (0, 0))
        screen.blit(down, (0, 0))
        screen.blit(t9, (325, 275))
        draw.rect(screen, BEIGE, t9Rect, 1)
        if playerRect.colliderect(t9Rect):
            screen.blit(t9text, (225, 425))
        for wm in downWall:
            draw.rect(screen, RED, wm, 3)
        draw.rect(screen, BEIGE, downtoout)

    if playerRect.colliderect(downbox2) and background == 2 and build == 0:
        build = 4
        pos[X] = 353
        pos[Y] = 338

    if playerRect.colliderect(downtoout) and background == 2 and build == 4:
        # print("HELLLLLLLLLLLLO")
        background = 2
        build = 0
        level = 3
        inside = False
        pos[X] = 306
        pos[Y] = 455

    if background == 3 and key1 == 1:
        # print("52")
        screen.blit(boss1map, (0, 0))
        screen.blit(t4, (300, 422))
        draw.rect(screen, BEIGE, t4Rect, 1)
        if playerRect.colliderect(t4Rect):
            screen.blit(t4text, (225, 425))
        for wm in wallsMapboss1:
            draw.rect(screen, RED, wm, 3)

        draw.rect(screen, BEIGE, tele1)
        draw.rect(screen, BEIGE, tele2)
        draw.rect(screen, BEIGE, tele3)
        draw.rect(screen, BEIGE, tele4)

    if playerRect.colliderect(boss1) and background == 2:
        level = 4
        background = 3

        pos[X] = 34
        pos[Y] = 232

    if playerRect.colliderect(tele4) and background == 3:
        level = 5
        background = 4

        pos[X] = 397
        pos[Y] = 421

    if background == 4:

        screen.blit(boss2map, (0, 0))
        screen.blit(t7, (390, 400))
        draw.rect(screen, BEIGE, t7Rect, 1)
        opphealth=1000
        for wm in wallsMapboss2:
            draw.rect(screen, RED, wm, 3)
        if playerRect.colliderect(t7Rect):
            screen.blit(t7text, (225, 425))
            if bosstimer_1 < 125:
                bosstimer_1 += 1
                # print(bosstimer_1)

            else:
                screen.blit(finalbattletitle, (0, 0))
                # pos[X]=800
                # pos[Y]=600
                battlenum = 3
                if battlenum == 3:
                    mixer.music.load(musics[1])  # music plays infintely as the program runs
                    mixer.music.play(-1)

                if bosstimer_2 < 125:
                    bosstimer_2 += 1
                else:
                    build = 5
                    background = 1



        

    # _______________________________________________________________________________________

    if playerRect.colliderect(tele1) and background == 3:
        pos[X] = 151
        pos[Y] = 395

    if playerRect.colliderect(tele2) and background == 3:
        pos[X] = 150
        pos[Y] = 206

    if playerRect.colliderect(tele3) and background == 3:
        pos[X] = 590
        pos[Y] = 244
    # _________________________________________________________________________________________

    if playerRect.colliderect(battleRect) and background == 1:
        pos[X] = 590
        pos[Y] = 244
        opphealth = 600

        build=5
        turn=1
        battlenum=1
        if battlenum == 1:
            mixer.music.load(musics[1])  # music plays infintely as the program runs
            mixer.music.play(-1)

 
    if playerRect.colliderect(battleRect2) and background == 1:
        pos[X] = 590
        pos[Y] = 244
        # health = 600
        opphealth = 800

        build = 5
        turn = 1
        battlenum = 2
        if battlenum == 2:
            mixer.music.load(musics[1])  # music plays infintely as the program runs
            mixer.music.play(-1)


    #build = 5
    #background = 1
##    build=5
##    background=1
##    battlenum=1
    if build == 5 and background == 1:
        if not tw:
            throwani = 0
        tw = True

        screen.blit(battle, (0, 0))

        pos[X] = 850
        pos[Y] = 650

        for wm in battleWall:
            draw.rect(screen, RED, wm, 3)
        draw.rect(screen, RED, attack1)
        draw.rect(screen, BLUE, attack2)
        draw.rect(screen, GREEN, attack3)
        draw.rect(screen, YELLOW, attack4)

        screen.blit(atk1, (25, 500))
        screen.blit(atk2, (225, 500))
        screen.blit(atk3, (424, 500))
        screen.blit(atk4, (629, 500))

        if battlenum==1:

            screen.blit(oppcharacter[0],(485,263))
            pos[X]=651
            pos[Y]=351
            print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")


        elif battlenum==2:
            screen.blit(oppcharacter[1],(483,263))
            pos[X]=612
            pos[Y]=128


        elif battlenum==3:
            screen.blit(oppcharacter[2],(283,263))
            print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

        screen.blit(char, (220, 325))

        scoreText=mytext.render('Health: ' + str(health), 1, (GREEN))
        screen.blit(scoreText,(15,15))

        scoreText1=mytext.render('Enemy Health: ' + str(opphealth), 1, (GREEN))
        screen.blit(scoreText1,(450,15))




        if throwani != -1:
            # print(True)
            screen.blit(throw[throwani], (150, 330))
            ani += 1
            if ani % 15 == 0:
                throwani += 1
            if throwani == 5:
                throwani = -1
            # print(throwani)
#______________________________________________________________________________________________________________________________

            

    # ___________________________________________________________________________________________________________

    if health >= 0 or opphealth >= 0:

        if turn == 1:
            time.wait(10)

            if attack == "1" and click == True:  # standard attack

                opphealth -= ak1
                # print(opphealth,"............opp health...........")

                changey -= 5
                if changey == 305:
                    changey = 325

                changex += 15
                if changex == 470:
                    changex = 410

                if not fe:
                    fireani = 0
                fe = True

                if fireani != -1:
                    screen.blit(transform.rotate(fire[fireani], angle), (changex, changey))
                    # print(True)

                    anim += 1
                    if anim % 1 == 0:
                        fireani += 1
                    if fireani == 4:
                        fireani = 0
                    # print(fireani)

                click = False

                if health <= 0 or opphealth <= 0:
                    turn = 3
                else:
                    turn = 2



            elif attack == "2" and click == True:  # risky range attack

                a2 = randint(0, 40)
                opphealth = opphealth - a2

                changey -= 5
                if changey == 305:
                    changey = 325

                changex += 15
                if changex == 470:
                    changex = 410

                if not fe:
                    fireani = 0
                fe = True

                if fireani != -1:
                    screen.blit(transform.rotate(fire[fireani], angle), (changex, changey))
                    # print(True)

                    anim += 1
                    if anim % 1 == 0:
                        fireani += 1
                    if fireani == 4:
                        fireani = 0
                    # print(fireani)

                # print(opphealth,"............opp health...........")
                click = False
                if health <= 0 or opphealth <= 0:
                    turn = 3
                else:
                    turn = 2



            elif attack == "3" and click == True:  # extreme risk attack

                a3 = randint(1, 2)
                if a3 == 1:
                    if opphealth <= 1250:
                        opphealth += 250

                    if not ht:
                        heartani = 0
                    ht = True

                    if heartani != -1:
                        screen.blit(heart[heartani], (changeX, changeY))
                        # print(True)

                        an += 1
                        if an % 1 == 0:
                            heartani += 1
                        if heartani == 4:
                            heartani = 0
                        # print(heartani)

                elif a3 == 2:
                    opphealth -= 100

                    changey -= 5
                    if changey == 305:
                        changey = 325

                    changex += 15
                    if changex == 470:
                        changex = 410

                    if not fe:
                        fireani = 0
                    fe = True

                    if fireani != -1:
                        screen.blit(transform.rotate(fire[fireani], angle), (changex, changey))
                        # print(True)

                        anim += 1
                        if anim % 1 == 0:
                            fireani += 1
                        if fireani == 4:
                            fireani = 0
                        # print(fireani)

                # print(opphealth,"............opp health...........")
                click = False
                if health <= 0 or opphealth <= 0:
                    turn = 3
                else:
                    turn = 2


            elif attack == "4" and click == True:  # heal

                if health <= 1585:
                    health += 15
                # print(health, "............player health...........")

                if not ht:
                    heartani = 0
                ht = True

                if heartani != -1:
                    screen.blit(heart[heartani], (changeXx, changeYy))
                    # print(True)

                    an += 1
                    if an % 1 == 0:
                        heartani += 1
                    if heartani == 4:
                        heartani = 0
                    # print(heartani)

                click = False


        elif turn == 2:
            time.wait(100)
            time.wait(3)
            oppattack = randint(0,40)
            health = health - oppattack
            if health <= 0 or opphealth <= 0:
                turn = 3
            else:
                turn = 1
            # print(health, "............player health...........")



        if turn == 3:
            time.wait(10)

            if health <= 0:
                screen.blit(lossoriginal,(0,0))
                time.delay(40)
                background=11
                if restart == "1":
                    background=0
                    charbag=1
                    level=6
                    build=0
                    health=1000
                    pos[X]=350
                    pos[Y]=350
                    mixer.music.load(musics[0])  # music plays infintely as the program runs
                    mixer.music.play(-1)
                    # print(background,level,build)
                
                
            elif opphealth <= 0:
                level=2
                background=1
                build=0

                    
    # _________________________________________________________________________________________________________________________________________________________________________________________
    draw.rect(screen, col, playerRect, 1)
    screen.blit((actions[action][di][count % 3]), (pos[X], pos[Y]))
    # print (pos[X],"x value",pos[Y],"y value")

    display.flip()
    myClock.tick(60)

quit()
