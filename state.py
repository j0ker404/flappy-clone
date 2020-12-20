import colours
import pygame

class State:

    def __init__(self, game_area,bird,SCREEN,pipe, pipe_group=None):
        """ 
        game_area: Game_Area instance
        pipe_group: Pipe_group instance
        bird: bird instance
        SCREEN: Display Surface area 
        """
        self.game_area = game_area  
        self.bird = bird
        self.SCREEN = SCREEN
        self.pipe = pipe
        self.pipe_group = pipe_group
    
    def draw(self):
        """
        draw state
        """
        # draw current state on game screen
        # add background colour
        self.game_area.fill(colours.WHITE)
        self.game_area.blit(self.bird.image,self.bird.rect)
        self.game_area.blit(self.pipe.image,(self.pipe.get_x(), self.pipe.get_y()))

        # draw game screen on APP window
        self.SCREEN.blit(self.game_area,self.game_area.get_coords())

    def update_state(self):
        """
        update current state on game area
        """
        pass

    def update(self):
        """ 
            Update display
        """
        pygame.display.update()