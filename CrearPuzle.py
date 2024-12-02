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