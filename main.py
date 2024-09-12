import pygame, sys
from constantes import *
from enum import Enum
from tablero import etapaTablero

class Etapa(Enum):
    INICIO = 1
    NIVELES = 2
    TABLERO = 3


# Matriz temporal para probar el tablero
matrizSize = 10
matriz = [[0 for i in range(matrizSize)] for j in range(matrizSize)]


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
            etapaTablero(screen, matrizSize, matriz) # eventos, dibujar, actualizar son manejados internamente


        pygame.display.flip()
        


    

main()
