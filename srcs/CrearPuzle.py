
from time import sleep
import pygame, sys
from srcs.BotonBloque import BotonBloque
from srcs.constantes import *
from srcs.BotonTablero import BotonTablero

# Clase para dibujar la etapa donde se resuelve el puzle


class CrearPuzle():

    # matrizValoresBloques: contiene los valores de las columnas y filas para saber que boton esta marcado
    # matrizIndices: contiene los valores de los indices que indican los cuadros a marcar para resolver el puzzle

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.blockCant = 20
        self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
        self.grillaSize = 410
        self.grillaPos = (370, 120)
        self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)

        self.dibujarInicio = True # variable para dibujar una vez la grilla al meterse al tablero
        self.inputRect = pygame.Rect(70, 440, 200, 80)
        self.inputActive = False
        self.userText = ''
        self.btnSizeSelector = []

        
        for i in range(3):
            self.btnSizeSelector.append(pygame.Rect(460 + 60*i + 20, 25, 60, 50))

        self.drawGrid(self.screen)
        # self.grilla = Grid(blockCant, self.matrizValoresBloques, matrizSolucion)

    
    # metodo para ejecutar la etapa del tablero
    def etapaDibujo(self):
        
        if self.dibujarInicio:
            self.drawGrid(self.screen)
            self.dibujarInicio = False

        self.draw()
        self.manejarEventos(self.matrizValoresBloques)
        
        pygame.display.update()
    
    # metodo para manejar los eventos en el loop del juego 
    def manejarEventos(self, matrizValoresBloques):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN: 
  
                # Check for backspace 
                if event.key == pygame.K_BACKSPACE: 
    
                    # get text input from 0 to -1 i.e. end. 
                    if self.inputActive:
                        self.userText = self.userText[:-1] 
    
                # Unicode standard is used for string 
                # formation 
                else: 
                    if  self.inputActive and len(self.userText) < 16:
                        self.userText += event.unicode

            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                self.inputActive = False
                pos = pygame.mouse.get_pos()
                
                # si esta dentro de la grilla
                if (pos[0] > self.grillaPos[0] and pos[0] < self.grillaPos[0] + self.grillaSize) and (pos[1] > self.grillaPos[1] and pos[1] < self.grillaPos[1] + self.grillaSize): 
                 
                    col = int((pos[0] - self.grillaPos[0]) // (self.grillaSize // self.blockCant))
                    fi = int((pos[1] - self.grillaPos[1]) // (self.grillaSize // self.blockCant))
                
                    columna = col if col < self.blockCant else col - 1
                    fila = fi if fi < self.blockCant else fi - 1
                        
                    
                    if matrizValoresBloques[columna][fila] == 0:
                    
                        if pygame.mouse.get_pressed()[0] == 1:   # si no esta marcado marcarlo con value
                            self.matrizValoresBloques[columna][fila] = 1
                            
                       
                        elif pygame.mouse.get_pressed()[2] == 1:
                            self.matrizValoresBloques[columna][fila] = 2

                    else:
                        self.matrizValoresBloques[columna][fila] = 0  # si esta marcado desmarcarlo
                    
                
                # funcion para salir del tablero
                elif pos[0] > 33 and pos[0] < 95  and pos[1] > 25 and pos[1] < 65:
                    self.dibujarInicio = True
                    self.main.cambiarEtapa(self.main.Etapa.MENU)

                # funcion para resetear el tablero
                elif pos[0] > 110 and pos[0] < 200 and pos[1] > 25 and pos[1] < 65:
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)

                # funcion para guardar el tablero
                elif pos[0] > 230 and pos[0] < 310 and pos[1] > 25 and pos[1] < 65:
                    self.writeFile()

                elif self.btnSizeSelector[0].collidepoint(pos):
                    self.blockCant = 5
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)
                    self.drawGrid(self.screen)
                
                elif self.btnSizeSelector[1].collidepoint(pos): 
                    self.blockCant = 10
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)
                    self.drawGrid(self.screen)
                
                elif self.btnSizeSelector[2].collidepoint(pos):
                    self.blockCant = 20
                    self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
                    self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)
                    self.drawGrid(self.screen)



                # funcion para selecionar el input
                if self.inputRect.x < pos[0] < self.inputRect.x + self.inputRect.width and self.inputRect.y < pos[1] < self.inputRect.y + self.inputRect.height: 
                    self.inputActive = True
                else:
                    self.inputActive = False

                # dibujar el tablero
                self.drawGrid(self.screen)

    # metodo para dibujar la etapa del tablero
    def draw(self):        

        botonSalir = BotonTablero(self.screen, "salir", (33, 25, 62, 40))
        botonResetear = BotonTablero(self.screen, "reiniciar", (115, 25, 100, 40))
        botonGuardar = BotonTablero(self.screen, "guardar", (235, 25, 100, 40))
        botonSalir.draw()
        botonResetear.draw()
        botonGuardar.draw()

        # dibujar input texto
        pygame.font.init()
        font = pygame.font.SysFont("Console", 20)

        colorInput = BLUE if self.inputActive else DARK_BLUE
        pygame.draw.rect(self.screen, colorInput, self.inputRect, 0) 
           
        textUsuarioSuperficie = font.render(self.userText, True, BEIGE) 
        label = font.render("nombre:", True, BEIGE) 
        
        # render at position stated in arguments 
        self.screen.blit(label, (self.inputRect.x + 8, self.inputRect.y + 10)) 
        self.screen.blit(textUsuarioSuperficie, (self.inputRect.x + 8, self.inputRect.y + 40)) 
        
        # set width of textfield so that text cannot get 
        # outside of user's text input 
        

        if self.btnSizeSelector[0].collidepoint(pygame.mouse.get_pos()): # boton 5x5
            pygame.draw.rect(self.screen, BLUE, self.btnSizeSelector[0], 0)
        else:
            pygame.draw.rect(self.screen, DARK_BLUE, self.btnSizeSelector[0], 0)

        if self.btnSizeSelector[1].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, BLUE, self.btnSizeSelector[1], 0)
        else:
            pygame.draw.rect(self.screen, DARK_BLUE, self.btnSizeSelector[1], 0)

        if self.btnSizeSelector[2].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, BLUE, self.btnSizeSelector[2], 0)
        else:
            pygame.draw.rect(self.screen, DARK_BLUE, self.btnSizeSelector[2], 0)

        fontSelectSize = pygame.font.SysFont("Console", 15)
        text5x5 = fontSelectSize.render("5x5", True, BEIGE)
        text10x10 = fontSelectSize.render("10x10", True, BEIGE)
        text20x20 = fontSelectSize.render("20x20", True, BEIGE)

        text5x5Rect = text5x5.get_rect(center = self.btnSizeSelector[0].center)
        text10x10Rect = text10x10.get_rect(center = self.btnSizeSelector[1].center)
        text20x20Rect = text20x20.get_rect(center = self.btnSizeSelector[2].center)

        self.screen.blit(text5x5, text5x5Rect)
        self.screen.blit(text10x10, text10x10Rect)
        self.screen.blit(text20x20, text20x20Rect)
        
    def writeFile(self):

        name = self.userText.lower()
        name = name.replace(" ", "_")

        f = open(f"./Puzles/{self.blockCant}_{name}.txt", "w")
        f.write("False\n") #puzle Completado
        f.write("False\n") #puzle en progreso
        f.write(f"{self.blockCant}\n")
        if self.blockCant == 5:
            f.write("1\n")
        elif self.blockCant == 10:
            f.write("3\n")
        elif self.blockCant == 20:
            f.write("5\n")
        
        matrizTranspuesta = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                matrizTranspuesta[j][i] = self.matrizValoresBloques[i][j]
        
        for i in range(self.blockCant):
            for j in range(self.blockCant):
                f.write(f"{matrizTranspuesta[i][j]} ")

            f.write("\n")

        f.close()

        self.matrizValoresBloques = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]
        self.matrizBloques = self.inicializarMatrizBloques(self.matrizValoresBloques)
        self.userText = ''
        
    def drawGrid(self, screen):
    

        grilla = pygame.Surface((self.grillaSize, self.grillaSize))
        grilla.fill(GREEN)

        superficieImagen = pygame.Surface((240, 240))
        superficieImagenBorde = pygame.Surface((250, 250))

        superficieImagen.fill(BEIGE)
        superficieImagenBorde.fill(DARK_BEIGE)


        for x in range(0, self.blockCant):     # filas

            if x % 5 == 0 and x != 0: # lineas gruesas verticales
                x_pos = ( x*(self.blockSize + 1) + GRID_MARGIN*(x + 1) -2, 0)
                #y_pos = ( x*(self.blockSize + 1) + GRID_MARGIN*(x + 1) -2, self.grillaSize - 2)
                y_pos = ( x*(self.blockSize + 1) + GRID_MARGIN*(x + 1) -2, self.blockCant*(self.blockSize + 1) + GRID_MARGIN*(self.blockCant + 1) - 2)
                pygame.draw.line(grilla, (14, 13, 17 ),  x_pos, y_pos, 1)



            for y in range(0, self.blockCant): # columnas
                
                if y % 5 == 0 and y != 0:
                    x_pos = (0, y*(self.blockSize + 1) + GRID_MARGIN*(y + 1) - 2)
                    #y_pos = (self.grillaSize - 2, y*(self.blockSize + 1) + GRID_MARGIN*(y + 1) - 2)
                    y_pos = (self.blockCant*(self.blockSize + 1) + GRID_MARGIN*(self.blockCant + 1) - 2 - 2, y*(self.blockSize + 1) + GRID_MARGIN*(y + 1) - 2)
                    pygame.draw.line(grilla, (14, 13, 17), x_pos, y_pos, 1)

                # dibujar bloques
                button = self.matrizBloques[x][y]
                button.draw(grilla)

                bloqueImagenSize = 240//self.blockCant

                if self.matrizValoresBloques[x][y] == 1:
                    pygame.draw.rect(superficieImagen, DARK_BLUE, (bloqueImagenSize*x, bloqueImagenSize*y, bloqueImagenSize,bloqueImagenSize),0)

        
        screen.blit(grilla, self.grillaPos)
        screen.blit(superficieImagenBorde, (50, 155))
        screen.blit(superficieImagen, (55, 160))

        # dibujar bordes de la grilla


        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] - 11, self.grillaPos[1] - 6), (self.grillaPos[0] + self.grillaSize + 1, self.grillaPos[1] - 6)], 10)

        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] - 11, self.grillaPos[1] + self.grillaSize - 4), (self.grillaPos[0] + self.grillaSize + 1, self.grillaPos[1] + self.grillaSize - 4)], 10)


        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] - 7, self.grillaPos[1] - 6), (self.grillaPos[0] - 7, self.grillaPos[1] + self.grillaSize - 3) ], 10)
        
        pygame.draw.lines(self.screen, DARK_BLUE, True, [(self.grillaPos[0] + self.grillaSize - 4, self.grillaPos[1] - 5), (self.grillaPos[0] + self.grillaSize - 4, self.grillaPos[1] + self.grillaSize - 5)], 10)


    
    def inicializarMatrizBloques(self, matrizValoresBloques):
        
        matriz = [[0 for i in range(self.blockCant)] for j in range(self.blockCant)]

        self.blockSize = int((self.grillaSize - GRID_MARGIN*self.blockCant) / self.blockCant  - 1) 
        step = self.blockSize + GRID_MARGIN
        

        for x in range(0, self.blockCant):
            for y in range(0, self.blockCant):

                posX = x + GRID_MARGIN + step*x
                posY = y + GRID_MARGIN + step*y

                rect = pygame.Rect(posX, posY, self.blockSize, self.blockSize) # calcular la posicion de cada rectangulo

                button = BotonBloque(rect, x, y, matrizValoresBloques) # crear un boton para cada rectangulo
                matriz[x][y] = button # almacenar los botones en la matriz de botones

                
        return matriz