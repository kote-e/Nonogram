import pygame
from constantes import *
from BotonBloque import BotonBloque

class Grid():

    initialized = False # variables estaticas para inicializar la matriz una sola vez por tablero
    # matriz de botones

    def __init__(self, blockCant, matrizValoresBloques, matrizIndices):
        self.blockCant = blockCant
        self.blockSize = 0
        self.grillaSize = 410
        self.grillaPos = (390, 110) # posicion de la grilla en la pantalla
        self.matrizBloques = self.inicializarMatrizBloques(matrizValoresBloques)
        self.matrizIndices = matrizIndices
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

        superficieColumnas = pygame.Surface((410, 95))
        superficieFilas = pygame.Surface((95, 410))

        superficieColumnas.fill(GREEN)
        superficieFilas.fill(GREEN)

        pygame.font.init()
        numberSize = 14
        font = pygame.font.SysFont("Comic Sans", numberSize)

        for x in range(0, self.blockCant):     # filas

            # dibujar fondo indices
            pygame.draw.rect(superficieColumnas, YELLOW, (x*(self.blockSize + 1) + GRID_MARGIN*(x + 1), 0, self.blockSize, 95), 0)
            pygame.draw.rect(superficieFilas, YELLOW, (0, x*(self.blockSize + 1) + GRID_MARGIN*(x + 1), 115, self.blockSize), 0) 

            for y in range(0, self.blockCant): # columnas
                
                # dibujar bloques
                button = self.matrizBloques[x][y]
                button.draw(grilla)

               
                # dibujar indices
                if y < len(self.matrizIndices[0][x]):
                    text = font.render(str(self.matrizIndices[0][x][y]), True, DARK_BLUE)
                    superficieColumnas.blit(text, (13 + x*(self.blockSize + 1) + GRID_MARGIN*(x + 1), 6 + (numberSize + 3)*y))

                if y < len(self.matrizIndices[1][x]):
                    text = font.render(str(self.matrizIndices[1][x][y]), True, DARK_BLUE)
                    superficieFilas.blit(text, (10 + (numberSize + 3)*y , 13 + x*(self.blockSize + 1) + GRID_MARGIN*(x + 1)))
        
        screen.blit(superficieColumnas, (390, 10))
        screen.blit(superficieFilas, (290, 110))
        screen.blit(grilla, self.grillaPos)
    
    def getBlockSize(self):
        return self.blockSize   
     
    def getGridPos(self):
        return self.grillaPos

    def getGridSize(self):  
        return self.grillaSize

    


       
        

