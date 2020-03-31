from pygame import *
from settings import *

class Camera:
    '''A class to hold the important methods for the camera to display elements with an offset relative to the player, to keep things on screen '''

    def __init__(self, width, height):
        self.rect = Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        '''Applies the offset to a sprite'''
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        '''Applies the offset to a rect. '''
        return rect.move(self.camera.topleft)

    def update(self, target):
        '''Updates the offset based on the position of the target. '''
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(x, -(self.width - WIDTH))
        y = max(y, -(self.height - HEIGHT))

        self.camera = Rect(x, y, self.width, self.height)