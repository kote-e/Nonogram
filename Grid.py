import pygame
from constantes import *
from BotonBloque import BotonBloque


class Grid():

    initialized = False # variables estaticas para inicializar la matriz una sola vez por tablero
    # matriz de botones

    def __init__(self, blockCant, matrizValoresBloques, matrizSolucion):
        self.blockCant = blockCant
        self.blockSize = 0
        self.grillaSize = 410
        self.grillaPos = (405, 130) # posicion de la grilla en la pantalla
        self.matrizBloques = self.inicializarMatrizBloques(matrizValoresBloques)
        self.matrizValoresBloques = matrizValoresBloques
        self.matrizSolucion = matrizSolucion
        self.matrizIndices = self.getIndicesSolución()
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

        superficieImagen = pygame.Surface((240, 240))
        superficieImagenBorde = pygame.Surface((250, 250))

        superficieImagen.fill(BEIGE)
        superficieImagenBorde.fill(DARK_BEIGE)

        superficieColumnas = pygame.Surface((410, 95))
        superficieFilas = pygame.Surface((95, 410))

        superficieColumnas.fill(GREEN)
        superficieFilas.fill(GREEN)

        pygame.font.init()
        numberSize = 14
        if self.blockCant == 20:
            numberSize = 12
            
        font = pygame.font.SysFont("Comic Sans", numberSize)
        font.set_bold(True)

        for x in range(0, self.blockCant):     # filas

            # dibujar fondo indices
            pygame.draw.rect(superficieColumnas, DARK_BLUE, (x*(self.blockSize + 1) + GRID_MARGIN*(x + 1), 0, self.blockSize, 95), 0)
            pygame.draw.rect(superficieFilas, DARK_BLUE, (0, x*(self.blockSize + 1) + GRID_MARGIN*(x + 1), 115, self.blockSize), 0) 

            for y in range(0, self.blockCant): # columnas
                
                # dibujar bloques
                button = self.matrizBloques[x][y]
                button.draw(grilla)

                paddingColumna = GRID_MARGIN + self.blockSize//2 - numberSize//2
                paddingFila = self.blockSize//2 - numberSize//2

                # dibujar indices
                if y < len(self.matrizIndices[0][x]):
                    text = font.render(str(self.matrizIndices[0][x][y]), True, BEIGE)
                    superficieColumnas.blit(text, (paddingColumna + x*(self.blockSize + 1) + GRID_MARGIN*(x + 1), 6 + (numberSize + 3)*y))

                if y < len(self.matrizIndices[1][x]):
                    text = font.render(str(self.matrizIndices[1][x][y]), True, BEIGE)
                    superficieFilas.blit(text, (10 + (numberSize + 3)*y , paddingFila + x*(self.blockSize + 1) + GRID_MARGIN*(x + 1)))

                bloqueImagenSize = 240//self.blockCant

                if self.matrizValoresBloques[x][y] == 1:
                    pygame.draw.rect(superficieImagen, DARK_BLUE, (bloqueImagenSize*x, bloqueImagenSize*y, bloqueImagenSize,bloqueImagenSize),0)


        screen.blit(superficieColumnas, (self.grillaPos[0], self.grillaPos[1] - 105))
        screen.blit(superficieFilas, (self.grillaPos[0] - 105, self.grillaPos[1]))
        screen.blit(grilla, self.grillaPos)
        screen.blit(superficieImagenBorde, (30, 195))
        screen.blit(superficieImagen, (35, 200))

    def comprobarSolucionTablero(self, matriz):
        if matriz == self.matrizSolucion:
            return True
        else:
            return False
        
    def tacharFila(self, numFila):
        for i in range(self.blockCant):
            if self.matrizValoresBloques[i][numFila] == 0:
                self.matrizValoresBloques[i][numFila] = 2

    def tacharColumna(self, numColumna):
        for i in range(self.blockCant):
            if self.matrizValoresBloques[numColumna][i] == 0:
                self.matrizValoresBloques[numColumna][i] = 2

    def comprobarTachar(self, numFila, numColumna):
        if (self.getMatrizTranspuesta(self.matrizValoresBloques)[numFila] == self.matrizSolucion[numFila]):
            self.tacharFila(numFila)
        if ([self.getMatrizTranspuesta(self.matrizValoresBloques)[i][numColumna] for i in range(self.blockCant)] == [self.matrizSolucion[i][numColumna] for i in range(self.blockCant)]):
            self.tacharColumna(numColumna)
    def listaAIndice(self,fila):
        indices = []
        count = 0
        for i in range(self.blockCant):
            if fila[i] == 1:
                count += 1
                if (i < self.blockCant-1 and fila[i+1] == 0) or (i == self.blockCant-1 and fila[i] == 1):
                    indices.append(count)
            elif fila[i] == 0:
                count = 0
        return indices
    def contarBloquesIguales(self, matriz1, matriz2):
        count = 0
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                if matriz1[i][j] == 1 and matriz2[i][j] == 1:
                    count += 1
        return count
    def contarBloquesMarcados(self, matriz):
        count = 0
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                if matriz[i][j] == 1:
                    count += 1
        return count
    def getPorcentajeCompletado(self, matriz, matrizSolucion):
        return self.contarBloquesIguales(matriz, matrizSolucion)/self.contarBloquesMarcados(matrizSolucion)
    
    def getBlockSize(self):
        return self.blockSize   
     
    def getGridPos(self):
        return self.grillaPos

    def getGridSize(self):  
        return self.grillaSize
    
    def getMatrizTranspuesta(self, matriz):
        matrizTranspuesta = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                matrizTranspuesta[j][i] = matriz[i][j]
                if matrizTranspuesta[j][i] == 2:
                    matrizTranspuesta[j][i] = 0
        return matrizTranspuesta
    
    def getIndicesSolución(self):
        indicesColumnas = []
        indicesFilas = []
        for i in range(self.blockCant):
            indicesFilas.append(self.listaAIndice(self.matrizSolucion[i]))
            columna = [self.matrizSolucion[j][i] for j in range(self.blockCant)]
            indicesColumnas.append(self.listaAIndice(columna))
        return [indicesColumnas, indicesFilas]