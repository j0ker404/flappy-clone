from pygame.sprite import Sprite
import pygame

class Pipe(Sprite):
    '''
        Class that defines a pipe(either top or bottom)
    '''
    __pipe_colour = 111, 232, 95
    __pipe_width = 60


    def __init__(self,height, type=True):
        '''
            type: Specifiy if bottom or top pipe
                bottom  = true
                top     = false
        '''
        super().__init__()

        self.image = pygame.Surface([Pipe.__pipe_width, height])
        self.image.fill(Pipe.__pipe_colour)
        self.height = height
        self.rect = self.image.get_rect()

        self.__type = type

    
    def update(self,x, y, height):
        """
        update x,y, height of pipe
        """
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)
    

    def get_type(self):
        """
        type: Specifiy if bottom or top pipe
                bottom  = true
                top     = false
        """
        return self.__type


    def get_x(self):
        """
            return x(left) of pipe
        """
        return self.rect.x


    def set_x(self, x):
        """
            set the pipe x(left) value
        """
        self.rect.x = x

    def set_y(self, y):
        """
            set the pipe y(top) value
        """
        self.rect.y = y


    def get_y(self):
        """
            return y(top-left) of pipe
        """
        return self.rect.y

    def get_height(self):
        """
        return height of pipe
        """
        return self.height    
    
    def set_height(self, height):
        """
        return height of pipe
        """
        self.height = height    

    @staticmethod
    def get_colour():
        """
            return pipe's colour as a RGB tuple
        """
        return Pipe.__pipe_colour


    @staticmethod
    def get_width():
        """
        return width of pipe
        """
        return Pipe.__pipe_width
 
