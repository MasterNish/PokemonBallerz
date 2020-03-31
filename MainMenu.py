from pygame import *


class MainMenu(sprite.Sprite) :

    def __init__(self, player):
        sprite.Sprite.__init__(self)

        self.newFile = 