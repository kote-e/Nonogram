import pygame, sys
from constantes import *
from BotonNivel import BotonNivel

class Niveles():

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.cantNiveles = 4
        self.pagina  = 0  # cual conjunto de niveles se muestra al mismo tiempo, 10 por pagina
        self.listaBotones = []
        self.listaNivelId = [0,0,0,0,0,0,0] # arreglo con nombres de archivos de matrices para iniciar tablero

        # Crear los botones para los niveles existentes 
        for i in range (8):
            if i < 4 and i + self.pagina*8 < len(self.listaNivelId):
                btn = BotonNivel(main, screen, (90 + i*175, 180, 150, 100), i)
                self.listaBotones.append(btn)
            elif i >= 4 and i + self.pagina*8 < len(self.listaNivelId):
                btn2 = BotonNivel(main, screen, (90 + (i-4)*175, 320, 150, 100), i)
                self.listaBotones.append(btn2)
            else:
                break
            
            # valores temporales para mostrar los distintos estados
            if i == 1:
                btn.size = 10
                btn.progreso = True
            elif i == 2: 
                btn.size = 10
                btn.completado = True
            elif i == 0:
                btn.size = 20


    def manejarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:

                botonesPorComprobar = 8 if len(self.listaBotones) >= 8 else len(self.listaBotones)
                for i in range(botonesPorComprobar):
                    mousePos = pygame.mouse.get_pos()

                    # checkear si el mouse hace click sobre algun boton
                    rect = pygame.Rect(self.listaBotones[i + self.pagina*8].rect)
                    if rect.collidepoint(mousePos):
                        self.listaBotones[i + self.pagina*8].cargarTablero()

                if mousePos[0] > WINDOW_WIDTH - 175 + 10 and mousePos[0] < WINDOW_WIDTH - 175 + 90 and mousePos[1] > 40 and mousePos[1] < 100:

                    self.main.cambiarEtapa(self.main.Etapa.MENU)
                
    def draw(self):
        self.screen.fill(DARK_BLUE)
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)

        # botonRetorno = BotonTablero(surface, "salir", (WINDOW_WIDTH - 175, 30, 80, 60))
        # botonRetorno.draw()

        self.crearBotonRetorno(surface)
        self.crearBotonesPasarPagina()
    
        pygame.font.init()
        fontTitulo = pygame.font.SysFont("Console", 60)
        fontTitulo.set_bold(True)

        titulo = fontTitulo.render("Niveles", True, BEIGE)
        tituloSombra = fontTitulo.render("Niveles", True,DARK_BLUE)

        surface.blit(tituloSombra, (86, 36))
        surface.blit(titulo, (83, 32))
        self.screen.blit(surface, (10, 10))

      
        for i in range (8):
            if len(self.listaBotones) > i + self.pagina*8:
                btn = self.listaBotones[i + self.pagina*8]
                btn.draw()

        
    def cambiarPagina(self, valor):
        if not valor and self.pagina > 0:
            self.pagina -= 1
        elif valor and (self.pagina + 1)*8 < len(self.listaBotones):
            self.pagina += 1

    def etapaNiveles(self):

        self.draw()
        self.manejarEventos()
        pygame.display.update()
    
    def crearBotonRetorno(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        botonRetornoRect = pygame.Rect((WINDOW_WIDTH - 175, 30, 80, 60))
       
        if mouse_pos[0] > botonRetornoRect.x + 10 and mouse_pos[0] < botonRetornoRect.x + 10 + botonRetornoRect.width and mouse_pos[1] > botonRetornoRect.y +10 and mouse_pos[1] < botonRetornoRect.y + botonRetornoRect.height+10:
            pygame.draw.rect(surface, BLUE, botonRetornoRect, 0)
        else:
            pygame.draw.rect(surface, DARK_BLUE, botonRetornoRect, 0)

        
        pygame.font.init()

        font = pygame.font.SysFont("Console", 16)
        text = font.render("salir", True, BEIGE)
        text_rect = text.get_rect(center = botonRetornoRect.center)

        surface.blit(text, text_rect)


    def crearBotonesPasarPagina(self):
        pass