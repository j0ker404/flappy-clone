from pygame.sprite import Group
import constant as CONSANT
import random

class Pipe_group(Group):
    """ 
    Pipe_group class to handle a pipe pair
    """
    def __init__(self) -> None:
        """
        constructor for pipe group
        """                
        super().__init__()

    @staticmethod
    def gen_heights():
        """
        Return (height_top, height_bottom) of pipe pair

        Randomly generate pipe heights
        """
        pass

