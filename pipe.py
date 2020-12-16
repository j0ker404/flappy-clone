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

        self.rect = self.image.get_rect()

        self.__type = type
    

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


    def get_y(self):
        """
            return y(top-left) of pipe
        """
        return self.rect.y

    
    @staticmethod
    def get_colour():
        """
            return pipe's colour as a RGB tuple
        """
        return Pipe.__pipe_colour


    @staticmethod
    def get_width():
        """
        return width of pip
        """
        return Pipe.__pipe_width
 
