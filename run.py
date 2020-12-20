import pygame
import sys
from bird import Bird
import constant as CONSTANT
from game_area import Game_Area
from pipe import Pipe
import colours
from state import State

def quit():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':

    pygame.init()
    SCREEN = pygame.display.set_mode(CONSTANT.game_res)
    pygame.display.set_caption(CONSTANT.game_title)

    # sprites
    bird = Bird()
    x = bird.get_width()
    y = int(CONSTANT.canvas[0][1]/2) - bird.get_height()/2
    # print('x = {}'.format(x))
    bird.update(x, y)

    # define game area
    game_area = Game_Area()

    # pipe test
    pipe = Pipe(250)
    # set pipe x position
    pipe.set_x(game_area.get_width()-Pipe.get_width()*2)
    # set pipe on bottom of area
    pipe.set_y(game_area.get_height() - pipe.get_height())

    # create State instance
    state = State(game_area=game_area,bird=bird,SCREEN=SCREEN,pipe=pipe)
    # game loop:
    # - update game state
    #      - events
    # - draw current game state
    SCREEN.fill(colours.BLACK)
    while True:
        
        # update game state
        state.update_state()
        # draw current game state
        state.draw()
        # update window
        state.update_display()


