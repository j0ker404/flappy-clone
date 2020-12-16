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
        self.__width = self.image.get_width()
        self.__height = self.image.get_height()


    def update(self, x,y):
        """
        update position of sprite
        accepted key-value: x, y
        """
        # x,y = -1,-1
        self.rect.x = x
        self.rect.y = y
        # try:
        #     x,y = args
        # except:
        #     print('error with bird update')


    def get_width(self):
        """
        return width of sprite
        """
        return self.__width
    
    def get_height(self):
        """
        return height of sprite
        """
        return self.__height