
import pygame, sys
from constantes import *
from BotonBloque import BotonBloque
from Grid import Grid

class Tablero():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, main, screen, blockCant, matrizValoresBloques, matrizIndices, matrizSolucion):
        self.screen = screen
        self.blockCant = blockCant
        self.matrizValoresBloques = matrizValoresBloques
        self.matrizIndices = matrizIndices
        self.matrizSolucion = matrizSolucion
        self.grilla = Grid(blockCant, matrizValoresBloques)


    def manejarEventos(self, matrizValoresBloques):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                grillaPos = self.grilla.getGridPos()

                if (pos[0] > grillaPos[0] and pos[0] < 800) and (pos[1] > grillaPos[1] and pos[1] < 520):

                   
                    columna = int((pos[0] - grillaPos[0]) / (self.grilla.getGridSize() / self.blockCant))
                    fila = int ((pos[1] - grillaPos[1]) / (self.grilla.getGridSize() / self.blockCant))

                    if fila == 10 : fila = 9
                    if columna == 10: columna = 9
                     
                    
                    if matrizValoresBloques[columna][fila] == 0:
                    
                        if pygame.mouse.get_pressed()[0] == 1:   # si no esta marcado marcarlo con value
                            self.matrizValoresBloques[columna][fila] = 1
                            self.comprobarTablero() # Comprobamos si al marcarlo se resuelve el tablero
                        elif pygame.mouse.get_pressed()[2] == 1:
                            self.matrizValoresBloques[columna][fila] = 2
                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # si esta marcado desmarcarlo
                        self.comprobarTablero() # Comprobamos si al desmarcarlo se resuelve el tablero

    def etapaTablero(self):

        pygame.display.set_caption('Tablero')
    
        #drawNumberIndicators(screen, blockCant, matrizIndices)
        self.grilla.drawGrid(self.screen)

        self.manejarEventos(self.matrizValoresBloques)
        
        pygame.display.update()
    
    def comprobarTablero(self):
        # Cuando se marca un cuadro, las columnas y filas estan invertidas en matrizValoresBloques, por lo que transponemos la matriz
        matrizTranspuesta = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                matrizTranspuesta[j][i] = self.matrizValoresBloques[i][j]
        """
        Para ver la matriz impresa
        for i in range(self.blockCant):
            print(self.matrizValoresBloques[i])
        for i in range(self.blockCant):
            print(matrizTranspuesta[i])
        """
        if matrizTranspuesta == self.matrizSolucion:
            print("Tablero resuelto")
            
    def comprobarFila(self, numFila): # numFila es un entero que indica la fila de matrizValoresBloques a comprobar
        matrizTranspuesta = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)] #Por el mismo motivo que en comprobarTablero
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                matrizTranspuesta[j][i] = self.matrizValoresBloques[i][j]
        if matrizTranspuesta[numFila] == self.matrizSolucion[numFila]:
            return True
        else:
            return False
    def comprobarColumna(self, numColumna): # numColumna es un entero que indica la columna de matrizValoresBloques a comprobar
        matrizTranspuesta = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)] #Por el mismo motivo que en comprobarTablero
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                matrizTranspuesta[j][i] = self.matrizValoresBloques[i][j]
        if [matrizTranspuesta[i][numColumna] for i in range(self.blockCant)] == [self.matrizSolucion[i][numColumna] for i in range(self.blockCant)]:
            return True
        else:
            return False
