import pygame, sys



# Paleta de colores: (si quieren cambiarla esta bien)
# 244, 241, 222: Beige
# 224, 122, 95: Salmon
# 61, 64, 91: Dark Blue
# 129, 178, 154: Green
# 242, 204, 143: Yellow

BACKGROUND_COLOR = (129, 178, 154)
LETTER_COLOR = (61, 64, 91)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800


def main():
    global screen, clock, jugando
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(BACKGROUND_COLOR)
    
    jugando = True

    while jugando:
        clock.tick(60)


        pygame.display.flip()
        
        


main()
