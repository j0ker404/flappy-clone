import pygame
import sys
from bird import Bird


WHITE = (255,255,255)
BLACK = (0,0,0)

def quit():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':

    pygame.init()
    res = (500,500)
    SCREEN = pygame.display.set_mode(res)
    pygame.display.set_caption('Flappy Clone')

    # sprites
    bird = Bird()
    x = bird.get_width()
    y = int(res[1]/2) - bird.get_height()/2
    # print('x = {}'.format(x))
    bird.update(x, y)

    # game loop:
    # - events
    # - update state
    # - draw
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
        SCREEN.fill(WHITE)
        SCREEN.blit(bird.image,bird.rect)
        pygame.display.update()

