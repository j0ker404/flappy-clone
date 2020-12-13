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
    pygame.display.set_caption('Block Runner')

    # sprites
    bird = Bird()
    bird.update(int(res[0]/2), int(res[0]/2))

    # game loop
    while True:
        SCREEN.fill(WHITE)
        SCREEN.blit(bird.image,bird.rect)
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


        pygame.display.update()

