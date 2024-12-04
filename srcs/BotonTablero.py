import pygame
from srcs.constantes import *
    

class BotonTablero:
    def __init__(self, screen, text, rect):
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.text = text
        

    def draw(self):
        x_pos = self.rect[0]
        y_pos = self.rect[1]
        width = self.rect[2]
        height = self. rect[3]

        # dibujar el boton de salir
        mouse_pos = pygame.mouse.get_pos()

       
        if mouse_pos[0] > x_pos and mouse_pos[0] < x_pos + width and mouse_pos[1] > y_pos and mouse_pos[1] < y_pos + height:
            
            pygame.draw.rect(self.screen, BLUE, self.rect, 0)
               
        else:
            pygame.draw.rect(self.screen, DARK_BLUE, self.rect, 0)

        pygame.font.init()
        font = pygame.font.SysFont("Console", 16)
        text = font.render(self.text, True, BEIGE)
        text_rect = text.get_rect(center = self.rect.center)

        self.screen.blit(text, text_rect)
