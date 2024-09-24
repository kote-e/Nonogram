
import pygame, sys
from constantes import *
from BotonBloque import BotonBloque
        

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



