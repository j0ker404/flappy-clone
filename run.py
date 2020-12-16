import pygame
import sys
from bird import Bird
import constant as CONSTANT
from game_area import Game_Area
from pipe import Pipe

WHITE = (255,255,255)
BLACK = (0,0,0)

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
    pipe.set_x(game_area.get_width()-Pipe.get_width()*2)

    # game loop:
    # - events
    # - update state
    # - draw
    SCREEN.fill(BLACK)
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
                elif event.key == pygame.K_SPACE:
                    # jump
                    pass


        # add background colour
        game_area.fill(WHITE)
        game_area.blit(bird.image,bird.rect)
        game_area.blit(pipe.image,(pipe.get_x(), pipe.get_y()))
        SCREEN.blit(game_area,game_area.get_coords())
        pygame.display.update()

