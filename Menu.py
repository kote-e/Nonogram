import pygame, sys
from constantes import *


class Menu():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen

    def manejarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()

                if mousePos[0] > (WINDOW_WIDTH - 20)//2 - 80 and mousePos[0] < (WINDOW_WIDTH - 20)//2 + 80 and mousePos[1] > (WINDOW_HEIGHT - 20)//2 and mousePos[1] < (WINDOW_HEIGHT - 20)//2 + 80:
                    self.main.cambiarEtapa(self.main.Etapa.NIVELES)
               
                
    def draw(self):
        self.screen.fill(DARK_BLUE)
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)

        pygame.font.init()
       
        fontTitulo = pygame.font.SysFont("Console", 80)
        fontTitulo.set_bold(True)
        fontBoton = pygame.font.SysFont("Console", 40)

        titulo = fontTitulo.render("Nonogram", True, BEIGE)
        tituloSombra = fontTitulo.render("Nonogram", True,DARK_BLUE)

        mousePos = pygame.mouse.get_pos()
        
        pygame.draw.rect(surface, DARK_GREEN, ((WINDOW_WIDTH - 20)//2 - 75 , (WINDOW_HEIGHT - 20)//2 + 8, 165, 83), 0)
       
        if mousePos[0] > (WINDOW_WIDTH - 20)//2 - 80 and mousePos[0] < (WINDOW_WIDTH - 20)//2 + 80 and mousePos[1] > (WINDOW_HEIGHT - 20)//2 and mousePos[1] < (WINDOW_HEIGHT - 20)//2 + 80:
            btnJugarTxt = fontBoton.render("Jugar", True, BEIGE)
            pygame.draw.rect(surface, (85, 88, 130), ((WINDOW_WIDTH - 20)//2 - 80 , (WINDOW_HEIGHT - 20)//2, 160, 80), 0)
        else:
            btnJugarTxt = fontBoton.render("Jugar", True, YELLOW)
            pygame.draw.rect(surface, DARK_BLUE, ((WINDOW_WIDTH - 20)//2 - 80 , (WINDOW_HEIGHT - 20)//2, 160, 80), 0)

    
        surface.blit(tituloSombra, (229, 68))
        surface.blit(titulo, (223, 62))
        surface.blit(btnJugarTxt, ((WINDOW_WIDTH - 20)//2 - 62 , (WINDOW_HEIGHT - 20)//2 + 14))
        self.screen.blit(surface, (10, 10))
       
        

    def etapaMenu(self):

        self.draw()
        self.manejarEventos()
        
        pygame.display.update()
    
    