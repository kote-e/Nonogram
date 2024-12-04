import pygame, sys
from srcs.constantes import *


class Menu():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.btnJugarRect = pygame.Rect((WINDOW_WIDTH - 20)//2 - 80 , (WINDOW_HEIGHT - 20)//2 - 40, 160, 80)
        self.btnCrearPuzleRect = pygame.Rect((WINDOW_WIDTH - 20)//2 - 80 , (WINDOW_HEIGHT - 20)//2 + 75, 165, 83)

    def manejarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()

                if self.btnJugarRect.collidepoint(mousePos):
                    self.main.cambiarEtapa(self.main.Etapa.NIVELES)
                elif self.btnCrearPuzleRect.collidepoint(mousePos):

                    self.screen.fill(DARK_BLUE)
                    surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
                    surface.fill(GREEN)
                    self.screen.blit(surface, (10, 10))
                    self.main.cambiarEtapa(self.main.Etapa.CREAR)
               
                
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

        fontCreditos = pygame.font.SysFont("Console", 14)
        creditos = fontCreditos.render("Creado por: Valeria Quiroga, Ariel Cisternas y Maria José San Martín",True, BEIGE )

        mousePos = pygame.mouse.get_pos()

        
        btnJugarSombraRect = ( self.btnJugarRect.x + 10, self.btnJugarRect.y + 8, self.btnJugarRect.width, self.btnJugarRect.height + 3)
        btnCrearPuzleSombraRect = ( self.btnCrearPuzleRect.x + 10, self.btnCrearPuzleRect.y + 8, self.btnCrearPuzleRect.width, self.btnCrearPuzleRect.height + 3)
        pygame.draw.rect(surface, DARK_GREEN, btnJugarSombraRect, 0)
        pygame.draw.rect(surface, DARK_GREEN, btnCrearPuzleSombraRect, 0)
       
        # if mousePos[0] > (WINDOW_WIDTH - 20)//2 - 80 and mousePos[0] < (WINDOW_WIDTH - 20)//2 + 80 and mousePos[1] > (WINDOW_HEIGHT - 20)//2 and mousePos[1] < (WINDOW_HEIGHT - 20)//2 + 80:

        btnJugarTxt = 0
        btnCrearPuzleTxt = 0
        if self.btnJugarRect.collidepoint(mousePos):
            btnJugarTxt = fontBoton.render("Jugar", True, BEIGE)
            pygame.draw.rect(surface, BLUE, self.btnJugarRect, 0)
        else:
            btnJugarTxt = fontBoton.render("Jugar", True, YELLOW)
            pygame.draw.rect(surface, DARK_BLUE, self.btnJugarRect, 0)

        if self.btnCrearPuzleRect.collidepoint(mousePos):
            btnCrearPuzleTxt = fontBoton.render("Crear", True, BEIGE)
            pygame.draw.rect(surface, BLUE, self.btnCrearPuzleRect, 0)
        else:  
            btnCrearPuzleTxt = fontBoton.render("Crear", True, YELLOW)
            pygame.draw.rect(surface, DARK_BLUE, self.btnCrearPuzleRect, 0)
    

        surface.blit(creditos, (150, 500)) 
        surface.blit(tituloSombra, (229, 68))
        surface.blit(titulo, (223, 62))
        surface.blit(btnJugarTxt, (self.btnJugarRect.x + 18, self.btnJugarRect.y + 16))
        surface.blit(btnCrearPuzleTxt, (self.btnCrearPuzleRect.x + 20, self.btnCrearPuzleRect.y + 16))
        self.screen.blit(surface, (10, 10))
       

    def etapaMenu(self):

        self.draw()
        self.manejarEventos()
        
        pygame.display.update()
    
    