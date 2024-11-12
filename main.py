
import pygame, sys

from traitlets import This
from constantes import *
from enum import Enum
from Menu import Menu
from Niveles import Niveles
from Menu import Menu
from Niveles import Niveles
from Tablero import Tablero
from CrearPuzle import CrearPuzle
from CrearPuzle import CrearPuzle
from Musica import Musica

# Valores temporales para probar el tablero

class Main():

    def __init__(self):
        self.main = self
        self.etapaJuego = self.Etapa.MENU
        self.menu = 0
        self.niveles = 0
        self.dibujo = 0
        self.tablero = 0
        self.musica = Musica("Nonogram/Lost-Woods-Legend-of-Zelda-Ocarina-of-Time-OST-Rema.mp3")

    class Etapa(Enum):
     
        MENU = 1
        NIVELES = 2
        TABLERO = 3
        CREAR = 4


    def cambiarEtapa(self, etapa):
        self.etapaJuego = etapa

    def crearTablero(self, nivel, screen, blockCant, matrizValoresBloques, matrizSolucion, nombre, pistas):
        self.tablero = Tablero(self.main, nivel, screen, blockCant, matrizValoresBloques, matrizSolucion, nombre, pistas)
        self.tablero.grilla.drawGrid(screen)


    def iniciarJuego(self):

        global screen, clock, jugando
        pygame.init()
        clock = pygame.time.Clock()
        jugando = True
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        programIcon = pygame.image.load('icono_gato.jpg')
        pygame.display.set_icon(programIcon)

        self.menu = Menu(self.main, screen)
        self.niveles = Niveles(self.main, screen)
        self.dibujo = CrearPuzle(self.main, screen)
        # self.etapaJuego = self.Etapa.TABLERO
        screen.fill(GREEN)
        self.musica.reproducir_musica()
        pygame.display.set_caption("Nonogram")
        
        
        while jugando:
            
            clock.tick(60)
            
            
            if self.etapaJuego == self.Etapa.MENU:
                self.menu.etapaMenu() # eventos, dibujar, actualizar son manejados internamente
            if self.etapaJuego == self.Etapa.MENU:
                self.menu.etapaMenu() # eventos, dibujar, actualizar son manejados internamente
                
            elif self.etapaJuego == self.Etapa.NIVELES:
                self.niveles.etapaNiveles() # eventos, dibujar, actualizar son manejados internamente
            
            elif self.etapaJuego == self.Etapa.TABLERO:
                self.tablero.etapaTablero() # eventos, dibujar, actualizar son manejados internamente
            
            elif self.etapaJuego == self.Etapa.CREAR:
                self.dibujo.etapaDibujo()
            
            elif self.etapaJuego == self.Etapa.CREAR:
                self.dibujo.etapaDibujo()

            pygame.display.flip()
        self.musica.detener_musica()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main = Main()
    main.iniciarJuego()

    


