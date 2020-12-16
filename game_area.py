from pygame import Surface
import constant as CONSTANT

class Game_Area(Surface):
    

    def __init__(self):
        """
        Construtor
        """
        super().__init__(CONSTANT.canvas[0])
        self.x, self.y = 0,0
        x,y = CONSTANT.canvas[1]
        self.set_x(x)
        self.set_y(y)

    

    def get_x(self):
        """
            return x(left) of pipe
        """
        return self.x


    def set_x(self, x):
        """
            set the x(left) value
        """
        if x + self.get_width()-1 < CONSTANT.game_res[0]:
            self.x = x
        else:
            print('out of bounds x')

    def set_y(self, y):
        """
            set the y(left) value
        """
        if y + self.get_height()-1 < CONSTANT.game_res[1]:
            self.y = y
        else:
            print('out of bounds y')


    def get_y(self):
        """
            return y(top-left) of pipe
        """
        return self.y

    def get_coords(self):
        return self.get_x(),self.get_y()
