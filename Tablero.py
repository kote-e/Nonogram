
import pygame, sys
from constantes import *
from Grid import Grid
from BotonTablero import BotonTablero

class Tablero():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, main, screen, blockCant, matrizValoresBloques, matrizIndices,matrizSolucion):
        self.main = main
        self.screen = screen
        self.blockCant = blockCant
        self.matrizValoresBloques = matrizValoresBloques
        self.matrizIndices = matrizIndices
        self.matrizSolucion = matrizSolucion
        self.grilla = Grid(blockCant, matrizValoresBloques, matrizIndices)

    def manejarEventos(self, matrizValoresBloques):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                grillaPos = self.grilla.getGridPos()

                if (pos[0] > grillaPos[0] and pos[0] < 800) and (pos[1] > grillaPos[1] and pos[1] < 520): # si esta dentro de la grilla
                 
                    col = int((pos[0] - grillaPos[0]) // (self.grilla.getGridSize() // self.blockCant))
                    fi = int((pos[1] - grillaPos[1]) // (self.grilla.getGridSize() // self.blockCant))
                
                    columna = col if col < self.blockCant else col - 1
                    fila = fi if fi < self.blockCant else fi - 1
                        
                        
                    
                    if matrizValoresBloques[columna][fila] == 0:
                    
                        if pygame.mouse.get_pressed()[0] == 1:   # si no esta marcado marcarlo con value
                            self.matrizValoresBloques[columna][fila] = 1
                            self.comprobarTablero() # Comprobamos si al marcarlo se resuelve el tablero
                            self.comprobarTachar(fila, columna)
                        elif pygame.mouse.get_pressed()[2] == 1:
                            self.matrizValoresBloques[columna][fila] = 2
                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # si esta marcado desmarcarlo
                        self.comprobarTablero() # Comprobamos si al desmarcarlo se resuelve el tablero
                        self.comprobarTachar(fila, columna)
                # funcion para salir del tablero
                elif pos[0] > 33 and pos[0] < 95  and pos[1] > 25 and pos[1] < 65:
                    
                    self.main.cambiarEtapa(self.main.Etapa.NIVELES)


                # funcion para resetear el tablero
                elif pos[0] > 110 and pos[0] < 200 and pos[1] > 25 and pos[1] < 65:
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.grilla = Grid(self.blockCant, self.matrizValoresBloques, self.matrizIndices)

    def draw(self):

        botonSalir = BotonTablero(self.screen, "salir", (33, 25, 62, 40))
        botonResetear = BotonTablero(self.screen, "reiniciar", (115, 25, 100, 40))
        botonSalir.draw()
        botonResetear.draw()

        pygame.font.init()
        fontExplicacion = pygame.font.SysFont("Console", 14)

        explicacion1 = fontExplicacion.render("Click izquierdo para marcar,", True, DARK_BLUE)
        explicacion2 = fontExplicacion.render("Click derecho para tachar.", True, DARK_BLUE)
        
        # pygame.draw.rect(self.screen, BEIGE, (33, 110, 240,100),0)
        self.screen.blit(explicacion1,(42, 120))
        self.screen.blit(explicacion2,(45, 140))
       

       

    def etapaTablero(self):

        self.draw()
    
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
                if matrizTranspuesta[j][i] == 2: #Para evitar errores, matrizTranspuesta solo tendra 0 y 1
                    matrizTranspuesta[j][i] = 0
        if matrizTranspuesta[numFila] == self.matrizSolucion[numFila]:
            return True
        else:
            return False
    def comprobarColumna(self, numColumna): # numColumna es un entero que indica la columna de matrizValoresBloques a comprobar
        matrizTranspuesta = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)] #Por el mismo motivo que en comprobarTablero
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                matrizTranspuesta[j][i] = self.matrizValoresBloques[i][j]
                if matrizTranspuesta[j][i] == 2: #Para evitar errores, matrizTranspuesta solo tendra 0 y 1
                    matrizTranspuesta[j][i] = 0
        if [matrizTranspuesta[i][numColumna] for i in range(self.blockCant)] == [self.matrizSolucion[i][numColumna] for i in range(self.blockCant)]:
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
        if self.comprobarFila(numFila):
            self.tacharFila(numFila)
        if self.comprobarColumna(numColumna):
            self.tacharColumna(numColumna)