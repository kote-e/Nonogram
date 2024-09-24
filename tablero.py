
import pygame, sys
from constantes import *
from BotonBloque import BotonBloque
from Grid import Grid


def manejarEventos(self, blockSize, matrizValoresBloques):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                grillaPos = self.grilla.getGridPos()

                if (pos[0] > grillaPos[0] and pos[0] < 800) and (pos[1] > grillaPos[1] and pos[1] < 520):

                    print("pos: ", pos)
                    columna = int((pos[0] - grillaPos[0]) / (blockSize + MARGIN))
                    fila = int ((pos[1] - grillaPos[1]) / (blockSize + MARGIN))

                    if fila == 10 : fila = 9
                    if columna == 10: columna = 9
                     
                    print("fila: ", fila, " columna: ", columna)

                    if matrizValoresBloques[columna][fila] == 0:
                    
                        if pygame.mouse.get_pressed()[0] == 1:   # si no esta marcado marcarlo con value
                            self.matrizValoresBloques[columna][fila] = 1
                        elif pygame.mouse.get_pressed()[2] == 1:
                            self.matrizValoresBloques[columna][fila] = 2
                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # si esta marcado desmarcarlo


def etapaTablero(screen, blockCant, matriz):
    pygame.display.set_caption('Tablero')
   
    
    drawGrid(screen, blockCant, matriz)


    manejarEventos(screen, blockCant, matriz)
    
    pygame.display.update()



