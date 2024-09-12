
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
        posAjustada = (pos[0] - 390, pos[1] - 110)          # ajuste de posicion para que el mouse este en la grilla
                             

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
            pygame.draw.rect(grilla, DARK_BLUE, self.rect) 
        
        elif valorEnMatriz == 2:       # color para indicar que esta tachado
            pygame.draw.rect(grilla, DARK_BEIGE, self.rect) 
        
        elif valorEnMatriz == 0:
            pygame.draw.rect(grilla, BEIGE, self.rect)

        pygame.display.update()
       


def drawGrid(screen, blockCant, matriz):
    
    grillaSize = 410
    grilla = pygame.Surface((grillaSize, grillaSize))
    grilla.fill(GREEN)


    margin = 2

    blockSize = int((grillaSize - margin*blockCant)/ blockCant  - 1) 
    step = blockSize + margin
    

    for x in range(0, blockCant):
        for y in range(0,blockCant):

            posX = x + margin + step*x
            posY = y + margin + step*y

            rect = pygame.Rect(posX, posY, blockSize, blockSize)
            button = blockButton(rect, x, y, matriz)

            button.draw(grilla, 1)
            
    
    screen.blit(grilla, (390, 110))
    


def drawNumberIndicators(screen, blockCant, matriz):

    superficieColumnas = pygame.Surface((410, 95))
    superficieFilas = pygame.Surface((115, 410))

    superficieColumnas.fill(GREEN)
    superficieFilas.fill(GREEN)

    margin = 2
    anchoColumna = (410 - margin*blockCant)/ blockCant  - 1
    anchoFila = (410 - margin*blockCant)/ blockCant  - 1

    
    
    for x in range(blockCant): # dibujar numeros
        for y in range(blockCant):
            posC = x + margin + (anchoColumna + margin)*x
            posF = y + margin + (anchoFila + margin)*y
            
            # dibujar columnas
            rect = pygame.Rect(posC, 0, anchoColumna, 95)
            pygame.draw.rect(superficieColumnas, SALMON, rect)

            font = pygame.font.Font(None, 36)
            text = font.render(str(x), True, DARK_BLUE)
            superficieColumnas.blit(text, (x*40, 0))


            # dibujar filas
            rect = pygame.Rect(0, posF, 115, anchoFila)
            pygame.draw.rect(superficieFilas, YELLOW, rect)

            # font = pygame.font.Font(None, 36)
            # text = font.render(str(x), True, DARK_BLUE)
            # superficieColumnas.blit(text, (x*40, 0))


    screen.blit(superficieColumnas, (390, 10))
    screen.blit(superficieFilas, (270, 110))
    


def etapaTablero(screen, blockCant, matriz):
    pygame.display.set_caption('Tablero')
   
    drawNumberIndicators(screen, blockCant, matriz)
    drawGrid(screen, blockCant, matriz)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()



