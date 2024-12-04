import pygame, os, sys
from srcs.constantes import *
from srcs.BotonNivel import BotonNivel

class Niveles():

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen

        self.pagina  = 0  # cual conjunto de niveles se muestra al mismo tiempo, 10 por pagina
        self.listaBotones = []
        self.cantidadNiveles = 0
        self.listaNiveles = [] # arreglo con nombres de archivos

        self.crearListaNiveles()
        self.crearBotonesNiveles()
    
    def etapaNiveles(self):
        self.draw()
        self.manejarEventos()
        pygame.display.update()
    
    
    def crearListaNiveles(self):
        self.cantidadNiveles = 0
        self.listaNiveles.clear()

        for root, dirs, files in os.walk("./Puzles"):
            for file in files:
                if file.endswith(".txt"):
                    self.listaNiveles.append(f"{root}/{file}")
                    self.cantidadNiveles += 1

        self.listaNiveles.sort()


    # Funcion que crea los botones de los niveles y los agrega a la lista de botones
    def crearBotonesNiveles(self):
        self.listaBotones.clear()

        for i in range (8):
            btn = 0
            if i < 4 and i + self.pagina*8 < self.cantidadNiveles:
                btn = BotonNivel(self.main, self.screen, (90 + i*175, 180, 150, 100), self.listaNiveles[i + self.pagina*8])
            
            elif i >= 4 and i + self.pagina*8 < self.cantidadNiveles:
                btn = BotonNivel(self.main, self.screen, (90 + (i-4)*175, 320, 150, 100), self.listaNiveles[i + self.pagina*8])
            else:
                break

            self.listaBotones.append(btn)      
            
    def manejarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:

                botonesPorComprobar = 8 if len(self.listaBotones) >= 8 else len(self.listaBotones)
               
                # botonNivel
                for i in range(botonesPorComprobar):
                    mousePos = pygame.mouse.get_pos()
                    
                    if self.cantidadNiveles > i + self.pagina*8: # ver si esta dentro del rango de la lista
                        rect = pygame.Rect(self.listaBotones[i].rect)
                        if rect.collidepoint(mousePos):
                            self.listaBotones[i].cargarTablero()
                    else:
                        break

                # Boton de retorno
                if mousePos[0] > WINDOW_WIDTH - 175 + 10 and mousePos[0] < WINDOW_WIDTH - 175 + 90 and mousePos[1] > 40 and mousePos[1] < 100:
                    
                    self.main.cambiarEtapa(self.main.Etapa.MENU)

     
                # botones Pagina
                if  mousePos[1] > 460 and mousePos[1] < 520:

                    if mousePos[0] > WINDOW_WIDTH//2 - 60 and mousePos[0] < WINDOW_WIDTH//2 :
       
                        self.cambiarPagina(False)
                    elif mousePos[0] > WINDOW_WIDTH//2 + 20  and mousePos[0] < WINDOW_WIDTH//2 + 80:
                  
                        self.cambiarPagina(True)

    def draw(self):
        self.screen.fill(DARK_BLUE)
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)

        # botonRetorno = BotonTablero(surface, "salir", (WINDOW_WIDTH - 175, 30, 80, 60))
        # botonRetorno.draw()

        self.crearBotonRetorno(surface)
        self.crearBotonesPasarPagina(surface)
    
        pygame.font.init()
        fontTitulo = pygame.font.SysFont("Console", 60)
        fontTitulo.set_bold(True)

        titulo = fontTitulo.render("Niveles", True, BEIGE)
        tituloSombra = fontTitulo.render("Niveles", True,DARK_BLUE)

        surface.blit(tituloSombra, (86, 36))
        surface.blit(titulo, (83, 32))
        self.screen.blit(surface, (10, 10))


        # dibujar los botones de los niveles
        for i in range (8):
            if i + self.pagina*8 < self.cantidadNiveles:
                btn = self.listaBotones[i]
                btn.draw()
            else:
                break

        pygame.display.update()     
        
    def cambiarPagina(self, valor):
        if not valor and self.pagina > 0:
            self.pagina -= 1
        elif valor and (self.pagina + 1)*8 + 1 <= self.cantidadNiveles:
            self.pagina += 1
           
        self.crearBotonesNiveles()
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

    def crearBotonesPasarPagina(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        botonPagPrev = pygame.Rect((WINDOW_WIDTH//2 - 70, 450, 60, 60))
        botonPagSig = pygame.Rect((WINDOW_WIDTH//2 + 10, 450, 60, 60))
       
        if mouse_pos[0] > botonPagPrev.x + 10 and mouse_pos[0] < botonPagPrev.x + 10 + botonPagPrev.width and mouse_pos[1] > botonPagPrev.y +10 and mouse_pos[1] < botonPagPrev.y + botonPagPrev.height+10:
            pygame.draw.rect(surface, BLUE, botonPagPrev, 0)
        else:
            pygame.draw.rect(surface, DARK_BLUE, botonPagPrev, 0)

        if mouse_pos[0] > botonPagSig.x + 10 and mouse_pos[0] < botonPagSig.x + 10 + botonPagSig.width and mouse_pos[1] > botonPagSig.y +10 and mouse_pos[1] < botonPagSig.y + botonPagSig.height+10:
            pygame.draw.rect(surface, BLUE, botonPagSig, 0)
        else:
            pygame.draw.rect(surface, DARK_BLUE, botonPagSig, 0)

        
        pygame.font.init()

        font = pygame.font.SysFont("Console", 35)
        # font.set_bold(True)
        textPagPrev = font.render("<", True, BEIGE)
        textPagSig = font.render(">", True, BEIGE)
        textRectPagPrev = textPagPrev.get_rect(center = botonPagPrev.center)
        textRectPagSig = textPagSig.get_rect(center = botonPagSig.center)

        surface.blit(textPagPrev, textRectPagPrev)
        surface.blit(textPagSig, textRectPagSig)

    