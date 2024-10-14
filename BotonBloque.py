import pygame
from constantes import *

class BotonBloque():
    def __init__(self, rect, fila, columna, matrizValoresBloques):
        self.rect = rect
        self.fila = fila
        self.columna = columna
        self.matrizValoresBloques = matrizValoresBloques

     
    # 0 vacio, 1 marcado, 2 cruz
    def draw(self, grilla):
     
        valorEnMatriz = self.matrizValoresBloques[self.fila][self.columna]

        if valorEnMatriz == 1:         # color para indicar que esta marcado
            pygame.draw.rect(grilla, DARK_BLUE, self.rect) 
        
        elif valorEnMatriz == 2:       # color para indicar que esta tachado
            pygame.draw.rect(grilla, BEIGE, self.rect) 
            pygame.draw.lines(grilla, DARK_BEIGE, True, [(self.rect[0] + 5 ,self.rect[1] + 5),(self.rect[0] + self.rect[2] - 5, self.rect[1] + self.rect[3] - 5)], 3)
            pygame.draw.lines(grilla, DARK_BEIGE, True, [(self.rect[0] + 5, self.rect[1] + self.rect[3] - 5),(self.rect[0] + self.rect[2] - 5,self.rect[1] + 5)], 3)
        
        elif valorEnMatriz == 0:
            pygame.draw.rect(grilla, BEIGE, self.rect)

        pygame.display.update()
       


    
