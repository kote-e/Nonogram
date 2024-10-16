from time import sleep
from time import sleep
import pygame, sys
from constantes import *
from Grid import Grid
from BotonTablero import BotonTablero

# Clase para dibujar la etapa donde se resuelve el puzle
# Clase para dibujar la etapa donde se resuelve el puzle
class Tablero():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, main, nivel, screen, blockCant, matrizValoresBloques, matrizSolucion):
        self.main = main
        self.screen = screen
        self.nivel = nivel
        self.blockCant = blockCant
        self.matrizValoresBloques = matrizValoresBloques
        self.matrizSolucion = matrizSolucion
        self.grilla = Grid(blockCant, matrizValoresBloques, matrizSolucion)

        self.dibujarInicio = True # variable para dibujar una vez la grilla al meterse al tablero

        # variables para calcular tiempo en pantalla de puzle completado
        self.puzleCompletado = False
        self.tiempoPuzleCompletado = 0
        self.contadorPuzleCompletado = 0

        

    
    # metodo para ejecutar la etapa del tablero
    def etapaTablero(self):

        if self.dibujarInicio:
            self.grilla.drawGrid(self.screen)
            self.dibujarInicio = False
        
        if not self.puzleCompletado:
            self.draw()
            self.manejarEventos(self.matrizValoresBloques)

        else:
            self.ejecutarPuzleCompletado()
        
        pygame.display.update()
    
    # metodo para manejar los eventos en el loop del juego 
        self.grilla = Grid(blockCant, matrizValoresBloques, matrizSolucion)

        self.dibujarInicio = True # variable para dibujar una vez la grilla al meterse al tablero

        # variables para calcular tiempo en pantalla de puzle completado
        self.puzleCompletado = False
        self.tiempoPuzleCompletado = 0
        self.contadorPuzleCompletado = 0

        

    
    # metodo para ejecutar la etapa del tablero
    def etapaTablero(self):

        if self.dibujarInicio:
            self.grilla.drawGrid(self.screen)
            self.dibujarInicio = False
        
        if not self.puzleCompletado:
            self.draw()
            self.manejarEventos(self.matrizValoresBloques)

        else:
            self.ejecutarPuzleCompletado()
        
        pygame.display.update()
    
    # metodo para manejar los eventos en el loop del juego 
    def manejarEventos(self, matrizValoresBloques):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                grillaPos = self.grilla.getGridPos()
                grillaSize = self.grilla.getGridSize()
                # si esta dentro de la grilla
                if ( grillaPos[0] < pos[0] < grillaPos[0] + grillaSize) and (grillaPos[1] < pos[1] < grillaPos[1] + grillaSize): 
                 
                    col = int((pos[0] - grillaPos[0]) // (self.grilla.getGridSize() // self.blockCant))
                    fi = int((pos[1] - grillaPos[1]) // (self.grilla.getGridSize() // self.blockCant))
                
                    columna = col if col < self.blockCant else col - 1
                    fila = fi if fi < self.blockCant else fi - 1
                        
                        
                grillaSize = self.grilla.getGridSize()
                # si esta dentro de la grilla
                if ( grillaPos[0] < pos[0] < grillaPos[0] + grillaSize) and (grillaPos[1] < pos[1] < grillaPos[1] + grillaSize): 
                 
                    col = int((pos[0] - grillaPos[0]) // (self.grilla.getGridSize() // self.blockCant))
                    fi = int((pos[1] - grillaPos[1]) // (self.grilla.getGridSize() // self.blockCant))
                
                    columna = col if col < self.blockCant else col - 1
                    fila = fi if fi < self.blockCant else fi - 1
                        
                        
                    
                    if matrizValoresBloques[columna][fila] == 0:
                    
                        if pygame.mouse.get_pressed()[0] == 1:   # si no esta marcado marcarlo con value
                            self.matrizValoresBloques[columna][fila] = 1
                            self.puzleCompletado = self.grilla.comprobarSolucionTablero(self.grilla.getMatrizTranspuesta(self.matrizValoresBloques)) # Comprobamos si al marcarlo se resuelve el tablero
                            self.grilla.comprobarTachar(fila, columna)
                       
                            self.puzleCompletado = self.grilla.comprobarSolucionTablero(self.grilla.getMatrizTranspuesta(self.matrizValoresBloques)) # Comprobamos si al marcarlo se resuelve el tablero
                            self.grilla.comprobarTachar(fila, columna)
                       
                        elif pygame.mouse.get_pressed()[2] == 1:
                            self.matrizValoresBloques[columna][fila] = 2


                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # si esta marcado desmarcarlo
                        self.puzzleCompletado = self.grilla.comprobarSolucionTablero(self.grilla.getMatrizTranspuesta(self.matrizValoresBloques)) # Comprobamos si al desmarcarlo se resuelve el tablero
                        self.grilla.comprobarTachar(fila, columna)

                
                        self.puzzleCompletado = self.grilla.comprobarSolucionTablero(self.grilla.getMatrizTranspuesta(self.matrizValoresBloques)) # Comprobamos si al desmarcarlo se resuelve el tablero
                        self.grilla.comprobarTachar(fila, columna)

                
                # funcion para salir del tablero
                elif pos[0] > 33 and pos[0] < 95  and pos[1] > 25 and pos[1] < 65:
                    self.dibujarInicio = True
                    self.nivel.lector.guardar_matriz(self.matrizValoresBloques, self.puzleCompletado, True)
                    self.nivel.actualizarProgresoCompletado(self.puzleCompletado, True)
                    self.main.cambiarEtapa(self.main.Etapa.NIVELES)


                # funcion para resetear el tablero
              
                elif pos[0] > 110 and pos[0] < 200 and pos[1] > 25 and pos[1] < 65:
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.grilla = Grid(self.blockCant, self.matrizValoresBloques, self.grilla.matrizSolucion)


                self.grilla.drawGrid(self.screen)  # redibujar la grilla


    # metodo para dibujar la etapa del tablero
                self.grilla = Grid(self.blockCant, self.matrizValoresBloques, self.grilla.matrizSolucion)


                self.grilla.drawGrid(self.screen)  # redibujar la grilla


    # metodo para dibujar la etapa del tablero
    def draw(self):

        botonSalir = BotonTablero(self.screen, "salir", (33, 25, 62, 40))
        botonResetear = BotonTablero(self.screen, "reiniciar", (115, 25, 100, 40))
        botonSalir = BotonTablero(self.screen, "salir", (33, 25, 62, 40))
        botonResetear = BotonTablero(self.screen, "reiniciar", (115, 25, 100, 40))
        botonSalir.draw()
        botonResetear.draw()

        pygame.font.init()
        fontExplicacion = pygame.font.SysFont("Console", 14)

        explicacion1 = fontExplicacion.render("Click izquierdo para marcar,", True, DARK_BLUE)
        explicacion2 = fontExplicacion.render("Click derecho para tachar.", True, DARK_BLUE)
        explicacion3 = fontExplicacion.render("Se guarda automáticamente", True, DARK_BLUE)
        explicacion4 = fontExplicacion.render("al salir", True, DARK_BLUE)
        
        # pygame.draw.rect(self.screen, BEIGE, (33, 110, 240,100),0)
        self.screen.blit(explicacion1,(42, 120))
        self.screen.blit(explicacion2,(45, 140))
        self.screen.blit(explicacion3,(53, 480))
        self.screen.blit(explicacion4,(128, 490))

    # metodo para dibujar la pantalla de puzle completado
    def ejecutarPuzleCompletado(self):

        # manejar salida del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # dibujar fondo
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)

        # dibujar imagen creada
        superficieImagen = pygame.Surface((350, 350))
        superficieImagenBorde = pygame.Surface((370, 370))
        superficieImagenBorde.fill(DARK_BEIGE)
        superficieImagen.fill(BEIGE)
        bloqueImagenSize = 350//self.blockCant

        for x in range(0, self.blockCant):     # filas
            for y in range(0, self.blockCant): # columnas
                if self.matrizSolucion[x][y] == 1:
                    pygame.draw.rect(superficieImagen, DARK_BLUE, (bloqueImagenSize*y, bloqueImagenSize*x, bloqueImagenSize,bloqueImagenSize),0)

        surface.blit(superficieImagenBorde, (250, 155))
        surface.blit(superficieImagen, (260, 165))  
        
        # dibujar mensaje       
        pygame.font.init()
        mensajeRect = pygame.Rect(((WINDOW_WIDTH - 20)//2 - 200, (WINDOW_HEIGHT -20)//2 - 380, 400, 300))
        fontMensaje = pygame.font.SysFont("Console", 60)
        fontMensaje.set_bold(True)

        
        # crear animacion 
        if self.contadorPuzleCompletado % 2 == 0:
            mensaje1 = fontMensaje.render("¡¡HAS GANADO!!", True, DARK_BLUE)
            mensaje2 = fontMensaje.render("¡¡HAS GANADO!!", True, BEIGE)
        else:
            mensaje1 = fontMensaje.render("¡¡HAS GANADO!!", True, BEIGE)
            mensaje2 = fontMensaje.render("¡¡HAS GANADO!!", True, DARK_BLUE) 
        
        mensaje1Rect = mensaje1.get_rect(center = mensajeRect.center)
        mensaje2Rect = mensaje1.get_rect(center = mensajeRect.center) 
        mensaje2Rect.x = mensaje2Rect.x + 6
        mensaje2Rect.y = mensaje2Rect.y + 6    
        surface.blit(mensaje1, mensaje1Rect)
        surface.blit(mensaje2, mensaje2Rect)
        self.screen.blit(surface, (10,10))
        pygame.font.init()
        fontExplicacion = pygame.font.SysFont("Console", 14)

        explicacion1 = fontExplicacion.render("Click izquierdo para marcar,", True, DARK_BLUE)
        explicacion2 = fontExplicacion.render("Click derecho para tachar.", True, DARK_BLUE)
        explicacion3 = fontExplicacion.render("Se guarda automáticamente", True, DARK_BLUE)
        explicacion4 = fontExplicacion.render("al salir", True, DARK_BLUE)
        
        # pygame.draw.rect(self.screen, BEIGE, (33, 110, 240,100),0)
        self.screen.blit(explicacion1,(42, 120))
        self.screen.blit(explicacion2,(45, 140))
        self.screen.blit(explicacion3,(53, 480))
        self.screen.blit(explicacion4,(128, 490))

    # metodo para dibujar la pantalla de puzle completado
    def ejecutarPuzleCompletado(self):

        # manejar salida del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # dibujar fondo
        surface = pygame.Surface((WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        surface.fill(GREEN)

        # dibujar imagen creada
        superficieImagen = pygame.Surface((350, 350))
        superficieImagenBorde = pygame.Surface((370, 370))
        superficieImagenBorde.fill(DARK_BEIGE)
        superficieImagen.fill(BEIGE)
        bloqueImagenSize = 350//self.blockCant

        for x in range(0, self.blockCant):     # filas
            for y in range(0, self.blockCant): # columnas
                if self.matrizSolucion[x][y] == 1:
                    pygame.draw.rect(superficieImagen, DARK_BLUE, (bloqueImagenSize*y, bloqueImagenSize*x, bloqueImagenSize,bloqueImagenSize),0)

        surface.blit(superficieImagenBorde, (250, 155))
        surface.blit(superficieImagen, (260, 165))  
        
        # dibujar mensaje       
        pygame.font.init()
        mensajeRect = pygame.Rect(((WINDOW_WIDTH - 20)//2 - 200, (WINDOW_HEIGHT -20)//2 - 380, 400, 300))
        fontMensaje = pygame.font.SysFont("Console", 60)
        fontMensaje.set_bold(True)

        
        # crear animacion 
        if self.contadorPuzleCompletado % 2 == 0:
            mensaje1 = fontMensaje.render("¡¡HAS GANADO!!", True, DARK_BLUE)
            mensaje2 = fontMensaje.render("¡¡HAS GANADO!!", True, BEIGE)
        else:
            mensaje1 = fontMensaje.render("¡¡HAS GANADO!!", True, BEIGE)
            mensaje2 = fontMensaje.render("¡¡HAS GANADO!!", True, DARK_BLUE) 
        
        mensaje1Rect = mensaje1.get_rect(center = mensajeRect.center)
        mensaje2Rect = mensaje1.get_rect(center = mensajeRect.center) 
        mensaje2Rect.x = mensaje2Rect.x + 6
        mensaje2Rect.y = mensaje2Rect.y + 6    
        surface.blit(mensaje1, mensaje1Rect)
        surface.blit(mensaje2, mensaje2Rect)
        self.screen.blit(surface, (10,10))
        pygame.display.update()

        # actualizar variables de tiempo
        currentTime = pygame.time.get_ticks()    
        
        if (currentTime - self.tiempoPuzleCompletado) > 500: #  si ha pasado medio segundo desde el ultimo cambio de color
            self.tiempoPuzleCompletado = currentTime
            self.contadorPuzleCompletado += 1
 
        if  self.contadorPuzleCompletado > 8  :  # si han pasado 4 segundos en esta pantalla, salir a niveles
            
            self.nivel.actualizarProgresoCompletado(True, False)
            self.nivel.lector.guardar_matriz(self.matrizValoresBloques, True, False)
            self.main.cambiarEtapa(self.main.Etapa.NIVELES)

            # reiniciar variables
            self.contadorPuzleCompletado = 0
            self.tiempoPuzleCompletado = 0

       