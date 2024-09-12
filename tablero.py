
import pygame, sys
        



def etapaTablero(screen, blockCant, matriz):
    pygame.display.set_caption('Tablero')
   
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    



