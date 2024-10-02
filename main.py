
import pygame, sys

from traitlets import This
from constantes import *
from enum import Enum
from Tablero import Tablero


# Valores temporales para probar el tablero
blockCant = 10
matrizValoresBloques = [[0 for i in range(blockCant)] for j in range(blockCant)]
matrizIndices = [ [[1, 1, 1, 1, 1],[1, 2, 1, 1, 1], [1, 3, 1, 1, 1], [1, 1, 4, 1, 1], [1, 1, 5, 1, 1], 
                   [1, 1, 6, 1, 1], [1, 1, 7, 1, 1], [1, 1, 8, 1, 1], [1, 1, 9, 1, 1], [1, 1, 10, 1, 1]], # columnas
                  [[9, 6, 9, 9, 9],[9, 7, 9, 9, 9], [9, 8, 9, 9, 9], [9, 9, 9, 9, 9], [9, 10, 9, 9, 9], 
                   [9, 11, 9, 9, 9], [9, 12, 9, 9, 9], [9, 13, 9, 9, 9], [9, 14, 9, 9, 9], [9, 15, 9, 9, 9]]] # filas
matrizSolucion =[
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1],
    [0,1,0,0,0,0,0,0,1,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0]
] #Solución temporal, una carita feliz

class Main():

    def __init__(self):
        self.main = self
        self.etapaJuego = self.Etapa.INICIO
        self.tablero = 0
        pass

    class Etapa(Enum):
        INICIO = 1
        NIVELES = 2
        TABLERO = 3

    def cambiarEtapa(self, etapa):
        self.etapaJuego = etapa

    def iniciarJuego(self):

        global screen, clock, jugando
        pygame.init()
        clock = pygame.time.Clock()
        jugando = True
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.tablero = Tablero(self.main, screen, blockCant, matrizValoresBloques, matrizIndices, matrizSolucion)
        self.etapaJuego = self.Etapa.TABLERO

        screen.fill(GREEN)
        pygame.display.set_caption("Nonogram")
        screen.fill(GREEN)
        pygame.display.set_caption("Nonogram")

        while jugando:
            
            clock.tick(60)
            
            
            if self.etapaJuego == self.Etapa.TABLERO:
                self.tablero.etapaTablero() # eventos, dibujar, actualizar son manejados internamente
                
       
        while jugando:
            
            clock.tick(60)
            
            
            if self.etapaJuego == self.Etapa.TABLERO:
                self.tablero.etapaTablero() # eventos, dibujar, actualizar son manejados internamente
                
       


            pygame.display.flip()
        


if __name__ == "__main__":
    main = Main()
    main.iniciarJuego()

    


