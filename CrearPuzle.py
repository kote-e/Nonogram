from time import sleep
import pygame, sys
from BotonBloque import BotonBloque
from constantes import *
from BotonTablero import BotonTablero

# Clase para dibujar la etapa donde se resuelve el puzle
class CrearPuzle:
    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.blockCant = 20
        self.matrizValoresBloques = [[0 for _ in range(self.blockCant)] for _ in range(self.blockCant)]
        self.grillaSize = 410
        self.grillaPos = (370, 120)

        # Cargar sonido para clic
        pygame.mixer.init()
        self.sonido_click = pygame.mixer.Sound("sonido.mp3")

        self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)
        self.dibujarInicio = True
        self.inputRect = pygame.Rect(70, 440, 200, 80)
        self.inputActive = False
        self.userText = ''
        self.btnSizeSelector = []

        for i in range(3):
            self.btnSizeSelector.append(pygame.Rect(460 + 60 * i + 20, 25, 60, 50))

        print("Antes de invocar drawGrid")
        self.drawGrid(self.screen)
        print("Después de invocar drawGrid")

    def drawGrid(self, screen):
        """
        Dibuja la grilla inicial en la pantalla con los bloques definidos.
        """
        print("Dibujando la grilla...")
        grilla_surface = pygame.Surface((self.grillaSize, self.grillaSize))
        grilla_surface.fill(GREEN)

        for x in range(self.blockCant):
            for y in range(self.blockCant):
                button = self.matrizBloques[x][y]
                button.draw(grilla_surface)

        screen.blit(grilla_surface, self.grillaPos)
        pygame.display.update()

    def etapaDibujo(self):
        if self.dibujarInicio:
            self.drawGrid(self.screen)
            self.dibujarInicio = False

        self.draw()
        self.manejarEventos(self.matrizValoresBloques)
        pygame.display.update()

    def manejarEventos(self, matrizValoresBloques):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and self.inputActive:
                    self.userText = self.userText[:-1]
                elif self.inputActive and len(self.userText) < 16:
                    self.userText += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.inputActive = False
                pos = pygame.mouse.get_pos()

                if (self.grillaPos[0] < pos[0] < self.grillaPos[0] + self.grillaSize) and \
                        (self.grillaPos[1] < pos[1] < self.grillaPos[1] + self.grillaSize):
                    col = int((pos[0] - self.grillaPos[0]) // (self.grillaSize // self.blockCant))
                    fila = int((pos[1] - self.grillaPos[1]) // (self.grillaSize // self.blockCant))

                    columna = col if col < self.blockCant else col - 1
                    fila = fila if fila < self.blockCant else fila - 1

                    if matrizValoresBloques[columna][fila] == 0:
                        if pygame.mouse.get_pressed()[0]:  # clic izquierdo
                            matrizValoresBloques[columna][fila] = 1
                            self.matrizBloques[columna][fila].reproducir_sonido()
                        elif pygame.mouse.get_pressed()[2]:  # clic derecho
                            matrizValoresBloques[columna][fila] = 2
                            self.matrizBloques[columna][fila].reproducir_sonido()
                    else:
                        matrizValoresBloques[columna][fila] = 0

                elif pos[0] > 33 and pos[0] < 95 and pos[1] > 25 and pos[1] < 65:  # Salir
                    self.dibujarInicio = True
                    self.main.cambiarEtapa(self.main.Etapa.MENU)

                elif pos[0] > 110 and pos[0] < 200 and pos[1] > 25 and pos[1] < 65:  # Reiniciar
                    self.matrizValoresBloques = [[0 for _ in range(self.blockCant)] for _ in range(self.blockCant)]
                    self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)

                elif pos[0] > 230 and pos[0] < 310 and pos[1] > 25 and pos[1] < 65:  # Guardar
                    self.writeFile()

                for i, selector in enumerate(self.btnSizeSelector):
                    if selector.collidepoint(pos):
                        self.blockCant = [5, 10, 20][i]
                        self.matrizValoresBloques = [[0 for _ in range(self.blockCant)] for _ in range(self.blockCant)]
                        self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)
                        self.drawGrid(self.screen)

                if self.inputRect.collidepoint(pos):  # Input seleccionado
                    self.inputActive = True

                self.drawGrid(self.screen)

    def draw(self):
        botonSalir = BotonTablero(self.screen, "salir", (33, 25, 62, 40))
        botonResetear = BotonTablero(self.screen, "reiniciar", (115, 25, 100, 40))
        botonGuardar = BotonTablero(self.screen, "guardar", (235, 25, 100, 40))
        botonSalir.draw()
        botonResetear.draw()
        botonGuardar.draw()

        pygame.font.init()
        font = pygame.font.SysFont("Console", 20)

        colorInput = BLUE if self.inputActive else DARK_BLUE
        pygame.draw.rect(self.screen, colorInput, self.inputRect, 0)

        textUsuarioSuperficie = font.render(self.userText, True, BEIGE)
        label = font.render("nombre:", True, BEIGE)
        self.screen.blit(label, (self.inputRect.x + 8, self.inputRect.y + 10))
        self.screen.blit(textUsuarioSuperficie, (self.inputRect.x + 8, self.inputRect.y + 40))

        fontSelectSize = pygame.font.SysFont("Console", 15)
        opciones = ["5x5", "10x10", "20x20"]
        for i, rect in enumerate(self.btnSizeSelector):
            color = BLUE if rect.collidepoint(pygame.mouse.get_pos()) else DARK_BLUE
            pygame.draw.rect(self.screen, color, rect, 0)
            text = fontSelectSize.render(opciones[i], True, BEIGE)
            self.screen.blit(text, text.get_rect(center=rect.center))


        text5x5Rect = text5x5.get_rect(center = self.btnSizeSelector[0].center)
        text10x10Rect = text10x10.get_rect(center = self.btnSizeSelector[1].center)
        text20x20Rect = text20x20.get_rect(center = self.btnSizeSelector[2].center)

        self.screen.blit(text5x5, text5x5Rect)
        self.screen.blit(text10x10, text10x10Rect)
        self.screen.blit(text20x20, text20x20Rect)

    def writeFile(self):

        name = self.userText.lower()
        name = name.replace(" ", "_")

        f = open(f"./Puzles/{self.blockCant}_{name}.txt", "w")
        f.write("False\n") #puzle Completado
        f.write("False\n") #puzle en progreso
        f.write(f"{self.blockCant}\n")
        if self.blockCant == 5:
            f.write("1\n")
        elif self.blockCant == 10:
            f.write("3\n")
        elif self.blockCant == 20:
            f.write("5\n")

        matrizTranspuesta = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                matrizTranspuesta[j][i] = self.matrizValoresBloques[i][j]

        for i in range(self.blockCant):
            for j in range(self.blockCant):
                f.write(f"{matrizTranspuesta[i][j]} ")

            f.write("\n")

        f.close()

        self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
        self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)
        self.userText = ''

    def drawGrid(self, screen):


        grilla = pygame.Surface((self.grillaSize, self.grillaSize))
        grilla.fill(GREEN)

        superficieImagen = pygame.Surface((240, 240))
        superficieImagenBorde = pygame.Surface((250, 250))

        superficieImagen.fill(BEIGE)
        superficieImagenBorde.fill(DARK_BEIGE)


        for x in range(0, self.blockCant):     # filas

            if x % 5 == 0 and x != 0: # lineas gruesas verticales
                x_pos = ( x*(self.blockSize + 1) + GRID_MARGIN*(x + 1) -2, 0)
                #y_pos = ( x*(self.blockSize + 1) + GRID_MARGIN*(x + 1) -2, self.grillaSize - 2)
                y_pos = ( x*(self.blockSize + 1) + GRID_MARGIN*(x + 1) -2, self.blockCant*(self.blockSize + 1) + GRID_MARGIN*(self.blockCant + 1) - 2)
                pygame.draw.line(grilla, (14, 13, 17 ),  x_pos, y_pos, 1)



            for y in range(0, self.blockCant): # columnas

                if y % 5 == 0 and y != 0:
                    x_pos = (0, y*(self.blockSize + 1) + GRID_MARGIN*(y + 1) - 2)
                    #y_pos = (self.grillaSize - 2, y*(self.blockSize + 1) + GRID_MARGIN*(y + 1) - 2)
                    y_pos = (self.blockCant*(self.blockSize + 1) + GRID_MARGIN*(self.blockCant + 1) - 2 - 2, y*(self.blockSize + 1) + GRID_MARGIN*(y + 1) - 2)
                    pygame.draw.line(grilla, (14, 13, 17), x_pos, y_pos, 1)

                # dibujar bloques
                button = self.matrizBloques[x][y]
                button.draw(grilla)

                bloqueImagenSize = 240//self.blockCant

                if self.matrizValoresBloques[x][y] == 1:
                    pygame.draw.rect(superficieImagen, DARK_BLUE, (bloqueImagenSize*x, bloqueImagenSize*y, bloqueImagenSize,bloqueImagenSize),0)


        screen.blit(grilla, self.grillaPos)
        screen.blit(superficieImagenBorde, (50, 155))
        screen.blit(superficieImagen, (55, 160))

        # dibujar bordes de la grilla


        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] - 11, self.grillaPos[1] - 6), (self.grillaPos[0] + self.grillaSize + 1, self.grillaPos[1] - 6)], 10)

        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] - 11, self.grillaPos[1] + self.grillaSize - 4), (self.grillaPos[0] + self.grillaSize + 1, self.grillaPos[1] + self.grillaSize - 4)], 10)


        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] - 7, self.grillaPos[1] - 6), (self.grillaPos[0] - 7, self.grillaPos[1] + self.grillaSize - 3) ], 10)

        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] + self.grillaSize - 4, self.grillaPos[1] - 5), (self.grillaPos[0] + self.grillaSize - 4, self.grillaPos[1] + self.grillaSize - 5)], 10)


    def inicializarMatrizBloques(self, matrizValoresBloques):
        matriz = [[0 for _ in range(self.blockCant)] for _ in range(self.blockCant)]
        self.blockSize = int((self.grillaSize - GRID_MARGIN * self.blockCant) / self.blockCant - 1)
        step = self.blockSize + GRID_MARGIN

        for x in range(self.blockCant):
            for y in range(self.blockCant):
                posX = x + GRID_MARGIN + step * x
                posY = y + GRID_MARGIN + step * y
                rect = pygame.Rect(posX, posY, self.blockSize, self.blockSize)
                button = BotonBloque(rect, x, y, matrizValoresBloques, self.sonido_click)
                matriz[x][y] = button

        return matriz