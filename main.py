import pygame, sys
from constantes import *
from enum import Enum

class Etapa(Enum):
    INICIO = 1
    NIVELES = 2
    TABLERO = 3


def main():
    global screen, clock, jugando
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(BACKGROUND_COLOR)
    
    jugando = True
    etapaJuego = Etapa.TABLERO


    while jugando:
        clock.tick(60)
        # Manejar eventos en el juego en cada funcion por separado

        if etapaJuego == Etapa.TABLERO:
            pass

        pygame.display.flip()
        


    

main()
