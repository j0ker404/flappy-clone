import pygame


class Block:

    def __init__(self):
        self._x = 0
        self._y = 0
        
    
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    
    def set_y(self,y):
        self._y = y
