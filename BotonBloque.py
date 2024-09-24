import pygame
from constantes import *
import numpy as np

class BotonBloque():
    def __init__(self, rect, fila, columna, matrizValoresBloques):
        self.rect = rect
        self.clicked = False
        self.fila = fila
        self.columna = columna
        self.matrizValoresBloques = matrizValoresBloques

     
    # 0 vacio, 1 marcado, 2 cruz
    def draw(self, grilla):
     
        valorEnMatriz = self.matrizValoresBloques[self.fila][self.columna]

        if valorEnMatriz == 1:         # color para indicar que esta marcado
            pygame.draw.rect(grilla, DARK_BLUE, self.rect) 
        
        elif valorEnMatriz == 2:       # color para indicar que esta tachado
            pygame.draw.rect(grilla, DARK_BEIGE, self.rect) 
        
        elif valorEnMatriz == 0:
            pygame.draw.rect(grilla, BEIGE, self.rect)

        pygame.display.update()
       


    