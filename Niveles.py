import pygame, sys
from constantes import *


class Niveles():

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen

    def manejarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                pass 
                
    def draw(self):
        self.screen.fill(DARK_BLUE)
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)
        pygame.font.init()
       
        fontTitulo = pygame.font.SysFont("Console", 60)
        fontTitulo.set_bold(True)
       

        titulo = fontTitulo.render("Niveles", True, BEIGE)
        tituloSombra = fontTitulo.render("Niveles", True,DARK_BLUE)

        surface.blit(tituloSombra, (86, 36))
        surface.blit(titulo, (83, 32))

        self.screen.blit(surface, (10, 10))
           
        

    def etapaNiveles(self):

        self.draw()
        self.manejarEventos()
        
        pygame.display.update()
    
    