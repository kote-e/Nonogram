import pygame, sys
from constantes import *


def main():
    global screen, clock, jugando
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(BACKGROUND_COLOR)
    
    jugando = True

    while jugando:
        clock.tick(60)
        # Manejar eventos en el juego en cada funcion por separado
        pygame.display.flip()
        
    

main()
