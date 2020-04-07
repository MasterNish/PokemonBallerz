from pygame import *


class MainMenu(sprite.Sprite) :

    def __init__(self, player):
        sprite.Sprite.__init__(self)

        load = image.load("pics/white.jpg")
        loadFile = transform.smoothscale(load, (300, 400))
        loadSelect = Rect(100, 200, 300, 400)
        if
        self.newFile = draw.rect