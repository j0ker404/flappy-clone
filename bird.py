from pygame.sprite import Sprite
import pygame
import os

class Bird(Sprite):
    # load image
    # __asurf = pygame.image.load(os.path.join('data', './assets/bird.png'))
    __asurf = pygame.image.load('./assets/bird.png')

    def __init__(self) -> None:
        super().__init__()
        # update image of sprite
        self.image  = Bird.__asurf
        # update rect of sprite
        self.rect   = self.image.get_rect()

    # update position of sprite
    # accepted key-value: x, y
    def update(self, *args, **kwargs) -> None:
        x,y = -1,-1
        try:
            x,y = args
            self.rect.x = x
            self.rect.y = y
        except:
            print('error with bitd update')

