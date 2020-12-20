from pygame.sprite import Group
import constant as CONSANT
import random
import time

class Pipe_Group(Group):
    """ 
    Pipe_group class to handle a pipe pair
    """
    def __init__(self) -> None:
        """
        constructor for pipe group
        """                
        random.seed(time.time())
        super().__init__()

    @staticmethod
    def gen_heights():
        """
        Return (height_top, height_bottom) of pipe pair

        Randomly generate pipe heights
        """
        h_top,h_bottom = 0,0
        while (h_top < CONSANT.min_pipe_height):
            h_top = random.uniform(0,1)*CONSANT.max_pipe_height
        
        h_bottom = CONSANT.canvas[0][1]-CONSANT.gap_height/2-h_top
        h_top = int(h_top)
        h_bottom = int(h_bottom)
        return h_top,h_bottom

    @staticmethod
    def height_test(N):
        """
        Test gen_height method
        N: number of iterations
        """
        for i in range(N):
            print('-'*25)
            h_top,h_bottom = Pipe_Group.gen_heights()
            print('heights = {}, {}'.format(h_top,h_bottom))
            print('Sum = {}'.format(h_top+h_bottom))
            print('-'*25)



if __name__ == "__main__":
    # run height test
    Pipe_Group.height_test(100)