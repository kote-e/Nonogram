
import pygame, sys
from constantes import *
from Grid import Grid
from BotonTablero import BotonTablero

class Tablero():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, main, screen, blockCant, matrizValoresBloques, matrizIndices):
        self.main = main
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

                if (pos[0] > grillaPos[0] and pos[0] < 800) and (pos[1] > grillaPos[1] and pos[1] < 520): # si esta dentro de la grilla
                 
                    col = int((pos[0] - grillaPos[0]) // (self.grilla.getGridSize() // self.blockCant))
                    fi = int((pos[1] - grillaPos[1]) // (self.grilla.getGridSize() // self.blockCant))
                
                    columna = col if col < self.blockCant else col - 1
                    fila = fi if fi < self.blockCant else fi - 1
                        
                        
                    
                    if matrizValoresBloques[columna][fila] == 0:
                    
                        if pygame.mouse.get_pressed()[0] == 1:   # si no esta marcado marcarlo con value
                            self.matrizValoresBloques[columna][fila] = 1
                        elif pygame.mouse.get_pressed()[2] == 1:
                            self.matrizValoresBloques[columna][fila] = 2
                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # si esta marcado desmarcarlo


                # funcion para salir del tablero
                elif pos[0] > 10 and pos[0] < 72 and pos[1] > 10 and pos[1] < 50:
                    print("cambiando a niveles")
                    self.main.cambiarEtapa(self.main.Etapa.NIVELES)


                # funcion para resetear el tablero
                elif pos[0] > 82 and pos[0] < 172 and pos[1] > 10 and pos[1] < 50:
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.grilla = Grid(self.blockCant, self.matrizValoresBloques, self.matrizIndices)

    def draw(self):

        botonSalir = BotonTablero(self.screen, "SALIR", pygame.Rect(10, 10, 62, 40))
        botonResetear = BotonTablero(self.screen, "RESETEAR", pygame.Rect(82, 10, 90, 40))
        botonSalir.draw()
        botonResetear.draw()

    def etapaTablero(self):

        self.draw()
    
        self.grilla.drawGrid(self.screen)
        self.manejarEventos(self.matrizValoresBloques)
        
        pygame.display.update()



