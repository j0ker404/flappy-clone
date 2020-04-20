import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)

def quit():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':

    pygame.init()
    res = (500,500)
    SCREEN = pygame.display.set_mode(res)
    pygame.display.set_caption('Block Runner')

    # game loop
    while True:
        SCREEN.fill(WHITE)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()


        pygame.display.update()

