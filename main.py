import pygame, sys

from traitlets import This
from constantes import *
from enum import Enum
from Menu import Menu
from Niveles import Niveles
from Tablero import Tablero


# Valores temporales para probar el tablero
blockCant3 = 5
matrizValoresBloques3 = [[0 for i in range(blockCant3)] for j in range(blockCant3)]
matrizIndices3 = [ [[1, 1, 1, 1, 1],[1, 2, 1, 1, 1], [1, 3, 1, 1, 1], [1, 1, 4, 1, 1], [1, 1, 5, 1, 1]], # columnas
                  [[9, 6, 9, 9, 9],[9, 7, 9, 9, 9], [9, 8, 9, 9, 9], [9, 9, 9, 9, 9], [9, 10, 9, 9, 9]]] # filas


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

blockCant2 = 20
matrizValoresBloques2 = [[0 for i in range(blockCant2)] for j in range(blockCant2)]
matrizIndices2 = [ [[1, 1, 1, 1, 1],[1, 2, 1, 1, 1], [1, 3, 1, 1, 1], [1, 1, 4, 1, 1], [1, 1, 5, 1, 1], [1, 1, 1, 1, 1],[1, 2, 1, 1, 1], [1, 3, 1, 1, 1], [1, 1, 4, 1, 1], [1, 1, 5, 1, 1],
                   [1, 1, 6, 1, 1], [1, 1, 7, 1, 1], [1, 1, 8, 1, 1], [1, 1, 9, 1, 1], [1, 1, 10, 1, 1], [1, 1, 1, 1, 1],[1, 2, 1, 1, 1], [1, 3, 1, 1, 1], [1, 1, 4, 1, 1], [1, 1, 5, 1, 1] ],# columnas
                  [[9, 6, 9, 9, 9],[9, 7, 9, 9, 9], [9, 8, 9, 9, 9], [9, 9, 9, 9, 9], [9, 10, 9, 9, 9], 
                   [9, 11, 9, 9, 9], [9, 12, 9, 9, 9], [9, 13, 9, 9, 9], [9, 14, 9, 9, 9], [9, 15, 9, 9, 9],
                   [9, 6, 9, 9, 9],[9, 7, 9, 9, 9], [9, 8, 9, 9, 9], [9, 9, 9, 9, 9], [9, 10, 9, 9, 9], 
                   [9, 11, 9, 9, 9], [9, 12, 9, 9, 9], [9, 13, 9, 9, 9], [9, 14, 9, 9, 9], [9, 15, 9, 9, 9]]] # filas




class Main():

    def __init__(self):
        self.main = self
        self.etapaJuego = self.Etapa.MENU
        self.tablero = 0

    class Etapa(Enum):
        MENU = 1
        NIVELES = 2
        TABLERO = 3

    def cambiarEtapa(self, etapa):
        self.etapaJuego = etapa

    def crearTablero(self, blockCant, matrizValoresBloques, matrizSolucion):
        self.tablero = Tablero((self.main, screen, blockCant, matrizValoresBloques, matrizIndices, matrizSolucion))

    def iniciarJuego(self):

        global screen, clock, jugando
        pygame.init()
        clock = pygame.time.Clock()
        jugando = True
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.menu = Menu(self.main, screen)
        self.niveles = Niveles(self.main, screen)
        self.tablero = Tablero(self.main, screen, blockCant, matrizValoresBloques, matrizSolucion)

        # self.etapaJuego = self.Etapa.TABLERO
        screen.fill(GREEN)
        pygame.display.set_caption("Nonogram")
        
        while jugando:
            
            clock.tick(60)
            
            
            if self.etapaJuego == self.Etapa.MENU:
                self.menu.etapaMenu() # eventos, dibujar, actualizar son manejados internamente
                
            elif self.etapaJuego == self.Etapa.NIVELES:
                self.niveles.etapaNiveles() # eventos, dibujar, actualizar son manejados internamente
            
            elif self.etapaJuego == self.Etapa.TABLERO:
                self.tablero.etapaTablero() # eventos, dibujar, actualizar son manejados internamente
            
       
            pygame.display.flip()
        


if __name__ == "__main__":
    main = Main()
    main.iniciarJuego()

    


