import pygame, sys
from constantes import *
from enum import Enum
from tablero import etapaTablero

class Etapa(Enum):
    INICIO = 1
    NIVELES = 2
    TABLERO = 3


# Valores temporales para probar el tablero
blockCant = 10
matrizValoresBloques = [[0 for i in range(blockCant)] for j in range(blockCant)]
matrizIndices = [ [[1, 2, 2, 0, 0],[3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], 
                   [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0]], # columnas
                  [[1, 2, 2, 0, 0],[3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], 
                   [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0], [3, 4, 5, 6, 0]]] # filas

def main():
    global screen, clock, jugando
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(GREEN)
    jugando = True
    etapaJuego = Etapa.TABLERO

    tablero = Tablero(screen, blockCant, matrizValoresBloques, matrizIndices) # inicializar cada vez que se entra a un puzle distinto

    while jugando:
        clock.tick(60)
        # Manejar eventos en el juego en cada funcion por separado

        if etapaJuego == Etapa.TABLERO:
            tablero.etapaTablero() # eventos, dibujar, actualizar son manejados internamente


        pygame.display.flip()
        


    

main()
