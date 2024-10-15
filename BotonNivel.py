import pygame
from constantes import *
from lectura import Lectura

class BotonNivel():
    
    def __init__(self, main, screen, rect, archivoId):
        self.main = main
        self.screen = screen
        self.rect = rect
        self.id = archivoId     
        self.lector = Lectura(archivoId)
        self.size, x1, x2, self.progreso, self.completado = self.lector.leer_matriz()


    def draw(self):
        x_pos = self.rect[0]
        y_pos = self.rect[1]
        width = self.rect[2]
        height = self. rect[3]


        mouse_pos = pygame.mouse.get_pos()

        shadeBoxRect = pygame.Rect(self.rect)
        shadeBoxRect.x += 8
        shadeBoxRect.y += 8

        pygame.draw.rect(self.screen, DARK_BLUE, shadeBoxRect, 0)

        # cambiar de color al pasar el mouse por encima
        if mouse_pos[0] > x_pos and mouse_pos[0] < x_pos + width and mouse_pos[1] > y_pos and mouse_pos[1] < y_pos + height:
            
            pygame.draw.rect(self.screen, DARK_BEIGE, self.rect, 0)
               
        else:
            pygame.draw.rect(self.screen, BEIGE, self.rect, 0)

        pygame.font.init()
        font = pygame.font.SysFont("Console", 18)
        fontSubtitulo = pygame.font.SysFont("Console", 15)

        r = pygame.Rect(self.rect)
        sizeText = font.render(f"{self.size} x {self.size}", True, DARK_BLUE)
        sizeTextRect = sizeText.get_rect(center = r.center)

        # imprimir los estados del nivel
        if self.completado:
            subText = fontSubtitulo.render("completado", True, (97, 135, 70))
            subTextRect = sizeText.get_rect(centerx = r.centerx - 8, centery = r.centery + 18)
            self.screen.blit(subText, subTextRect)
            
        elif self.progreso:
            subText = fontSubtitulo.render("en progreso", True, RED)
            subTextRect = sizeText.get_rect(centerx = r.centerx - 12, centery = r.centery + 18)
            self.screen.blit(subText, subTextRect)
            
        elif self.size == 0:
            sizeText = font.render(f"BLOQUEADO", True, BEIGE, DARK_BLUE)
            sizeTextRect.centerx -= 20
        


        self.screen.blit(sizeText, sizeTextRect)
        

    def actualizarProgresoCompletado(self, completado, progreso):
            self.completado = completado
            self.progreso = progreso


    def cargarTablero(self):
        self.screen.fill(DARK_BLUE)
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)
        self.screen.blit(surface, (10, 10))

        ## llamar a funcion para leer matriz de archivo y pasarselo a tablero como argumento.

        tamaño, matrizSolucion, matrizUsuario, x1, x2 = self.lector.leer_matriz()

        self.main.crearTablero(self, self.screen, tamaño, matrizUsuario, matrizSolucion)
        self.main.cambiarEtapa(self.main.Etapa.TABLERO)
        
