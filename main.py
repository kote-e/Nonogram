import pygame, sys
from constantes import *
from enum import Enum
from Menu import Menu
from Niveles import Niveles
from Tablero import Tablero
from CrearPuzle import CrearPuzle
from Musica import Musica  # Asegúrate de tener la clase Musica importada

class Main:
    def __init__(self):
        self.main = self
        self.etapaJuego = self.Etapa.MENU
        self.menu = 0
        self.niveles = 0
        self.dibujo = 0
        self.tablero = 0
        self.musica = Musica("Lost-Woods-Legend-of-Zelda-Ocarina-of-Time-OST-Rema.mp3")

    class Etapa(Enum):
        MENU = 1
        NIVELES = 2
        TABLERO = 3
        CREAR = 4

    def cambiarEtapa(self, etapa):
        self.etapaJuego = etapa

    def crearTablero(self, nivel, screen, blockCant, matrizValoresBloques, matrizSolucion, nombre, pistas):
        """
        Aquí agregamos los parámetros nombre y pistas al crear el tablero
        """
        self.tablero = Tablero(self.main, nivel, screen, blockCant, matrizValoresBloques, matrizSolucion, nombre, pistas)
        self.tablero.grilla.drawGrid(screen)

    def iniciarJuego(self):
        global screen, clock, jugando
        pygame.init()
        clock = pygame.time.Clock()
        jugando = True
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.menu = Menu(self.main, screen)
        self.niveles = Niveles(self.main, screen)
        self.dibujo = CrearPuzle(self.main, screen)
        screen.fill(GREEN)
        self.musica.reproducir_musica()  # Reproducir música
        pygame.display.set_caption("Nonogram")

        while jugando:
            clock.tick(60)

            if self.etapaJuego == self.Etapa.MENU:
                self.menu.etapaMenu()
            elif self.etapaJuego == self.Etapa.NIVELES:
                self.niveles.etapaNiveles()
            elif self.etapaJuego == self.Etapa.TABLERO:
                self.tablero.etapaTablero()
            elif self.etapaJuego == self.Etapa.CREAR:
                self.dibujo.etapaDibujo()

            pygame.display.flip()
        self.musica.detener_musica()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main = Main()
    main.iniciarJuego()


