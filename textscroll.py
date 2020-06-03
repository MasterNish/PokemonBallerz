from pygame import*

width, height = 800, 600
screen = display.set_mode((width, height))
RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
font.init()

mytext = font.SysFont("Arial", 30)
mytext1 = mytext.render("HELLO", True, YELLOW)
mytext2 = mytext.render("Massey", True, YELLOW)

y = 500
running = True

myclock = time.Clock()
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    screen.fill(0)
    screen.blit(mytext1, (200, y))
    screen.blit(mytext2, (200, y + 50))
    y -= 1
    display.flip()
    myclock.tick(60)

quit()