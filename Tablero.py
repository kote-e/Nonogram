
import pygame, sys
from constantes import *
from Grid import Grid
from BotonTablero import BotonTablero

class Tablero():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, screen, blockCant, matrizValoresBloques, matrizIndices):
        self.screen = screen
        self.blockCant = blockCant
        self.matrizValoresBloques = matrizValoresBloques
        self.matrizIndices = matrizIndices
        self.grilla = Grid(blockCant, matrizValoresBloques, matrizIndices)


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
                        elif pygame.mouse.get_pressed()[2] == 1:
                            self.matrizValoresBloques[columna][fila] = 2
                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # si esta marcado desmarcarlo


                if pos[0] > 10 and pos[0] < 72 and pos[1] > 10 and pos[1] < 50:
                    pass # funcion para salir del tablero

                if pos[0] > 82 and pos[0] < 172 and pos[1] > 10 and pos[1] < 50:
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.grilla = Grid(self.blockCant, self.matrizValoresBloques, self.matrizIndices)
                    # funcion para resetear el tablero

    def draw(self):

        botonSalir = BotonTablero(self.screen, "SALIR", pygame.Rect(10, 10, 62, 40))
        botonResetear = BotonTablero(self.screen, "RESETEAR", pygame.Rect(82, 10, 90, 40))
        botonSalir.draw()
        botonResetear.draw()

    def etapaTablero(self):

        pygame.display.set_caption('Tablero')
        self.draw()
    
        #drawNumberIndicators(screen, blockCant, matrizIndices)
        self.grilla.drawGrid(self.screen)

        self.manejarEventos(self.matrizValoresBloques)
        
        pygame.display.update()


