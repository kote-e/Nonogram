import pygame
from srcs.constantes import *
from srcs.lectura import Lectura

class BotonNivel():
    
    def __init__(self, main, screen, rect, archivoId):
        self.main = main
        self.screen = screen
        self.rect = rect
        self.id = archivoId     
        self.lector = Lectura(archivoId)
        self.size, self.matrizSolucion, self.matrizUsuario, self.completado, self.progreso, self.nombre, self.pistas = self.lector.leer_matriz()

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
        self.screen.blit(sizeText, sizeTextRect)

    
        # imprimir los estados del nivel
        subText = None
        if self.completado:
            subText = fontSubtitulo.render("completado", True, (97, 135, 70))
        elif self.progreso:
            subText = fontSubtitulo.render("en progreso", True, RED)

        if subText != None:
            subTextRect = subText.get_rect(center = r.center)
            subTextRect.y += 18
            self.screen.blit(subText, subTextRect)

        
    def actualizarProgresoCompletado(self, completado, progreso):
            self.completado = completado
            self.progreso = progreso

    # def actualizarMatriz(self, matriz):
    #     self.matrizUsuario = matriz
    
    # def actualizarPistas(self, pistas):
    #     self.pistas = pistas

    def cargarTablero(self):
        self.screen.fill(DARK_BLUE)
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)
        self.screen.blit(surface, (10, 10))

        # leer info de archivo
        self.size, self.matrizSolucion, self.matrizUsuario, self.completado, self.progreso, self.nombre, self.pistas = self.lector.leer_matriz()


        self.main.crearTablero(self, self.screen, self.size, self.matrizUsuario, self.matrizSolucion, self.nombre, self.pistas)
        self.main.cambiarEtapa(self.main.Etapa.TABLERO)
        
