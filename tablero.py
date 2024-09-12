
import pygame, sys
from constantes import *
        


class blockButton():
    def __init__(self, rect, fila, columna, blockMatrix):
        self.rect = rect
        self.clicked = False
        self.fila = fila
        self.columna = columna
        self.blockMatrix = blockMatrix
       # self.value = 1 # 1 marcado, 2 cruz

    def marcar(self, value):
        pos = pygame.mouse.get_pos()
        posAjustada = (pos[0] - 300, pos[1] - 110)          # ajuste de posicion para que el mouse este en la grilla
                             

        if(self.rect.collidepoint(posAjustada)):

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: 
                self.clicked = True

                if self.blockMatrix[self.fila][self.columna] == 0: # si no esta marcado marcarlo con value
                
                    self.blockMatrix[self.fila][self.columna] = value
                else:
                    self.blockMatrix[self.fila][self.columna] = 0  # si esta marcado desmarcarlo

            elif pygame.mouse.get_pressed()[2] == 1 and self.clicked == False: 
                self.clicked = True

                if self.blockMatrix[self.fila][self.columna] == 0: # si no esta marcado marcarlo con value
                
                    self.blockMatrix[self.fila][self.columna] = 2
                else:
                    self.blockMatrix[self.fila][self.columna] = 0  # si esta marcado desmarcarlo
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False 
    
    def draw(self, grilla, value):


        self.marcar(value)
        
        # value: 0 vacio, 1 marcado, 2 cruz
        valorEnMatriz = self.blockMatrix[self.fila][self.columna]

        if valorEnMatriz == 1:         # color para indicar que esta marcado
            pygame.draw.rect(grilla, LETTER_COLOR, self.rect) 
        
        elif valorEnMatriz == 2:       # color para indicar que esta tachado
            pygame.draw.rect(grilla, (230, 218, 195), self.rect) 
        
        elif valorEnMatriz == 0:
            pygame.draw.rect(grilla, (244, 241, 222), self.rect)

        pygame.display.update()
       



def etapaTablero(screen, blockCant, matriz):
    pygame.display.set_caption('Tablero')
   
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    



