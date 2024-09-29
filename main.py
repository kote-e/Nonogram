import pygame, sys
from constantes import *
from enum import Enum
from Tablero import Tablero

class Etapa(Enum):
    INICIO = 1
    NIVELES = 2
    TABLERO = 3


# Valores temporales para probar el tablero
blockCant = 10
matrizValoresBloques = [[0 for i in range(blockCant)] for j in range(blockCant)]
matrizIndices = [ [[1, 1, 1, 1, 1],[1, 2, 1, 1, 1], [1, 3, 1, 1, 1], [1, 1, 4, 1, 1], [1, 1, 5, 1, 1], 
                   [1, 1, 6, 1, 1], [1, 1, 7, 1, 1], [1, 1, 8, 1, 1], [1, 1, 9, 1, 1], [1, 1, 10, 1, 1]], # columnas
                  [[9, 6, 9, 9, 9],[9, 7, 9, 9, 9], [9, 8, 9, 9, 9], [9, 9, 9, 9, 9], [9, 10, 9, 9, 9], 
                   [9, 11, 9, 9, 9], [9, 12, 9, 9, 9], [9, 13, 9, 9, 9], [9, 14, 9, 9, 9], [9, 15, 9, 9, 9]]] # filas

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
