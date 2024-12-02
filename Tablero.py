from time import sleep
import pygame, sys
from constantes import *
from Grid import Grid
from BotonTablero import BotonTablero

class Tablero:
    def __init__(self, main, nivel, screen, blockCant, matrizValoresBloques, matrizSolucion, nombre, pistas):
        self.main = main
        self.screen = screen
        self.nivel = nivel
        self.blockCant = blockCant
        self.matrizValoresBloques = matrizValoresBloques
        self.matrizSolucion = matrizSolucion
        self.pistas = pistas
        self.grilla = Grid(blockCant, matrizValoresBloques, matrizSolucion)
        self.nombre = nombre

        self.dibujarInicio = True
        self.dibujarNuevamenteEnSiguienteClick = False

        # Variables para tiempo en pantalla de puzle completado
        self.puzleCompletado = False
        self.tiempoPuzleCompletado = 0
        self.contadorPuzleCompletado = 0
        self.porcentajestr = "{:.0f}%".format(
            (self.grilla.getPorcentajeCompletado(self.grilla.getMatrizTranspuesta(self.matrizValoresBloques), self.matrizSolucion)) * 100
        )

        # Variables para animar pista
        self.animandoPista = False
        self.coordenadasPista = None
        self.tiempoInicioPista = 0
        self.contadorTiempoPista = 0

        # Cargar el sonido
        pygame.mixer.init()
        self.sonido_click = pygame.mixer.Sound("sonido.mp3")

    def etapaTablero(self):
        if self.dibujarInicio:
            self.grilla.drawGrid(self.screen)
            self.dibujarInicio = False

        if self.animandoPista:
            self.animarPista(self.coordenadasPista)

        if not self.puzleCompletado:
            self.draw()
            self.manejarEventos(self.matrizValoresBloques)
        else:
            self.ejecutarPuzleCompletado()

        pygame.display.update()

    def manejarEventos(self, matrizValoresBloques):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pistaUsada = None
                pos = pygame.mouse.get_pos()
                grillaPos = self.grilla.getGridPos()
                grillaSize = self.grilla.getGridSize()

                # Si está dentro de la grilla
                if (grillaPos[0] < pos[0] < grillaPos[0] + grillaSize) and \
                        (grillaPos[1] < pos[1] < grillaPos[1] + grillaSize):
                    col = int((pos[0] - grillaPos[0]) // (self.grilla.getGridSize() // self.blockCant))
                    fila = int((pos[1] - grillaPos[1]) // (self.grilla.getGridSize() // self.blockCant))
                    columna = col if col < self.blockCant else col - 1
                    fila = fila if fila < self.blockCant else fila - 1

                    if matrizValoresBloques[columna][fila] == 0:
                        if pygame.mouse.get_pressed()[0]:  # Clic izquierdo
                            self.matrizValoresBloques[columna][fila] = 1
                            self.sonido_click.play()  # Reproducir sonido
                            self.puzleCompletado = self.grilla.comprobarSolucionTablero(
                                self.grilla.getMatrizTranspuesta(self.matrizValoresBloques))
                            self.grilla.comprobarTachar(fila, columna)
                            self.porcentajestr = "{:.0f}%".format(
                                (self.grilla.getPorcentajeCompletado(
                                    self.grilla.getMatrizTranspuesta(self.matrizValoresBloques), self.matrizSolucion)) * 100)
                            self.drawPorcentaje()
                        elif pygame.mouse.get_pressed()[2]:  # Clic derecho
                            self.matrizValoresBloques[columna][fila] = 2
                            self.sonido_click.play()  # Reproducir sonido
                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # Desmarcar
                        self.sonido_click.play()  # Reproducir sonido
                        self.puzleCompletado = self.grilla.comprobarSolucionTablero(
                            self.grilla.getMatrizTranspuesta(self.matrizValoresBloques))
                        self.grilla.comprobarTachar(fila, columna)
                        self.porcentajestr = "{:.0f}%".format(
                            (self.grilla.getPorcentajeCompletado(
                                self.grilla.getMatrizTranspuesta(self.matrizValoresBloques), self.matrizSolucion)) * 100)
                        self.drawPorcentaje()

                # Otras acciones como salir, resetear, obtener pista
                elif pos[0] > 33 and pos[0] < 95 and pos[1] > 25 and pos[1] < 65:
                    self.dibujarInicio = True
                    self.nivel.lector.guardar_matriz(self.matrizValoresBloques, self.puzleCompletado, True, self.pistas)
                    self.nivel.actualizarProgresoCompletado(self.puzleCompletado, True)
                    self.main.cambiarEtapa(self.main.Etapa.NIVELES)
                elif pos[0] > 110 and pos[0] < 200 and pos[1] > 25 and pos[1] < 65:
                    self.matrizValoresBloques = [[0 for _ in range(self.blockCant)] for _ in range(self.blockCant)]
                    self.grilla = Grid(self.blockCant, self.matrizValoresBloques, self.grilla.matrizSolucion)
                    self.pistas = {5: 1, 10: 3, 20: 5}[self.blockCant]
                    self.porcentajestr = "{:.0f}%".format(
                        (self.grilla.getPorcentajeCompletado(
                            self.grilla.getMatrizTranspuesta(self.matrizValoresBloques), self.matrizSolucion)) * 100)
                    self.drawPorcentaje()
                elif pos[0] > 240 and pos[0] < 350 and pos[1] > 25 and pos[1] < 65 and self.pistas > 0:
                    pistaUsada = self.grilla.getPista()
                    self.puzleCompletado = self.grilla.comprobarSolucionTablero(
                        self.grilla.getMatrizTranspuesta(self.matrizValoresBloques))
                    self.porcentajestr = "{:.0f}%".format(
                        (self.grilla.getPorcentajeCompletado(
                            self.grilla.getMatrizTranspuesta(self.matrizValoresBloques), self.matrizSolucion)) * 100)
                    self.drawPorcentaje()
                    if self.puzleCompletado:
                        self.ejecutarPuzleCompletado()
                    self.pistas -= 1

                if self.dibujarNuevamenteEnSiguienteClick:
                    self.dibujarInicio = True
                    self.dibujarNuevamenteEnSiguienteClick = False

                self.grilla = Grid(self.blockCant, self.matrizValoresBloques, self.grilla.matrizSolucion)
                self.grilla.drawGrid(self.screen)

                if pistaUsada is not None:
                    if self.animandoPista:
                        self.resetVariablesAnimacionPista()
                    self.animarPista(pistaUsada)

    def draw(self):
        botonSalir = BotonTablero(self.screen, "salir", (33, 25, 62, 40))
        botonResetear = BotonTablero(self.screen, "reiniciar", (115, 25, 100, 40))
        botonPista = BotonTablero(self.screen, f"pistas ({self.pistas})", (240, 25, 110, 40))
        botonSalir.draw()
        botonResetear.draw()
        botonPista.draw()

        pygame.font.init()
        fontExplicacion = pygame.font.SysFont("Console", 14)
        self.screen.blit(fontExplicacion.render("Click izquierdo para marcar,", True, DARK_BLUE), (42, 120))
        self.screen.blit(fontExplicacion.render("Click derecho para tachar.", True, DARK_BLUE), (45, 140))
        self.screen.blit(fontExplicacion.render("Se guarda automáticamente", True, DARK_BLUE), (53, 500))
        self.screen.blit(fontExplicacion.render("al salir", True, DARK_BLUE), (128, 510))
        self.drawPorcentaje()

    def drawPorcentaje(self):
        pygame.draw.rect(self.screen, GREEN, (42, 450, 250, 20), 0)
        pygame.font.init()
        fontExplicacion = pygame.font.SysFont("Console", 14)
        porcentaje = fontExplicacion.render("Porcentaje completado: " + self.porcentajestr, True, DARK_BLUE)
        self.screen.blit(porcentaje, (42, 450))