import pygame
from constantes import *
from BotonBloque import BotonBloque

class Grid():

    initialized = False # variables estaticas para inicializar la matriz una sola vez por tablero
    # matriz de botones

    def __init__(self, blockCant, matrizValoresBloques):
        self.blockCant = blockCant
        self.blockSize = 0
        self.grillaSize = 410
        self.grillaPos = (390, 110) # posicion de la grilla en la pantalla
        self.matrizBloques = self.inicializarMatrizBloques(matrizValoresBloques)
            
       # self.value = 1 # 1 marcado, 2 cruz

    def inicializarMatrizBloques(self, matrizValoresBloques):
        
        matriz = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]

        self.blockSize = int((self.grillaSize - GRID_MARGIN*self.blockCant) / self.blockCant  - 1) 
        step = self.blockSize + GRID_MARGIN
        

        for x in range(0, self.blockCant):
            for y in range(0, self.blockCant):

                posX = x + GRID_MARGIN + step*x
                posY = y + GRID_MARGIN + step*y

                rect = pygame.Rect(posX, posY, self.blockSize, self.blockSize) # calcular la posicion de cada rectangulo

                button = BotonBloque(rect, x, y, matrizValoresBloques) # crear un boton para cada rectangulo
                matriz[x][y] = button # almacenar los botones en la matriz de botones

                
        return matriz
                

    def drawGrid(self, screen):
        
        grilla = pygame.Surface((self.grillaSize, self.grillaSize))
        grilla.fill(GREEN)

        for x in range(0, self.blockCant):
            for y in range(0, self.blockCant):

                button = self.matrizBloques[x][y]
                button.draw(grilla)
        
        
        screen.blit(grilla, self.grillaPos)
    
    def getBlockSize(self):
        return self.blockSize   
     
    def getGridPos(self):
        return self.grillaPos


    def drawIndices(screen, blockCant, matriz):

        superficieColumnas = pygame.Surface((410, 95))
        superficieFilas = pygame.Surface((115, 410))

        superficieColumnas.fill(GREEN)
        superficieFilas.fill(GREEN)

        anchoColumna = (410 - GRID_MARGIN*blockCant)/ blockCant  - 1
        anchoFila = (410 - GRID_MARGIN*blockCant)/ blockCant  - 1
        
        
        for x in range(blockCant): # dibujar numeros
            for y in range(blockCant):
                posC = x + GRID_MARGIN + (anchoColumna + GRID_MARGIN)*x
                posF = y + GRID_MARGIN + (anchoFila + GRID_MARGIN)*y
                
                # dibujar columnas
                rect = pygame.Rect(posC, 0, anchoColumna, 95)
                pygame.draw.rect(superficieColumnas, YELLOW, rect)

                for i in range(len(matriz[0][x])):
                    font = pygame.font.Font(None, 20)
                    text = font.render(str(matriz[0][x][i]), True, DARK_BLUE)
                    superficieColumnas.blit(text, (posC - GRID_MARGIN + anchoColumna/2, i*20))


                # dibujar filas
                rect = pygame.Rect(0, posF, 115, anchoFila)
                pygame.draw.rect(superficieFilas, YELLOW, rect)

                # font = pygame.font.Font(None, 36)
                # text = font.render(str(x), True, DARK_BLUE)
                # superficieColumnas.blit(text, (x*40, 0))


        screen.blit(superficieColumnas, (390, 10))
        screen.blit(superficieFilas, (270, 110))
        

