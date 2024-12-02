import pygame
from constantes import *

class BotonBloque:
    def __init__(self, rect, fila, columna, matrizValoresBloques, sonido_click=None):
        self.rect = rect                     # pygame.Rect(x, y, width, height)
        self.fila = fila
        self.columna = columna
        self.matrizValoresBloques = matrizValoresBloques
        self.sonido_click = sonido_click  # Nuevo: sonido asociado al bloque


    def draw(self, grilla):
        valorEnMatriz = self.matrizValoresBloques[self.fila][self.columna]

        if valorEnMatriz == 1:  # color para indicar que está marcado
            pygame.draw.rect(grilla, DARK_BLUE, self.rect)

        elif valorEnMatriz == 2:  # color para indicar que está tachado
            pygame.draw.rect(grilla, BEIGE, self.rect)
            pygame.draw.lines(grilla, DARK_BEIGE, True,[(self.rect[0] + 5, self.rect[1] + 5),(self.rect[0] + self.rect[2] - 5, self.rect[1] + self.rect[3] - 5)], 3)
            pygame.draw.lines(grilla, DARK_BEIGE, True,[(self.rect[0] + 5, self.rect[1] + self.rect[3] - 5),(self.rect[0] + self.rect[2] - 5, self.rect[1] + 5)], 3)

        elif valorEnMatriz == 0:  # color para indicar que está vacío
            pygame.draw.rect(grilla, BEIGE, self.rect)

        pygame.display.update()

    def getRect(self):
        return self.rect


    def reproducir_sonido(self):
        if self.sonido_click:
            self.sonido_click.play()