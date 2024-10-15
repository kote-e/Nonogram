import pygame, sys

from traitlets import This
from constantes import *
from enum import Enum
from Tablero import Tablero
import os


class Lectura:
    def __init__(self, archivoPuzle):
        self.archivoPuzle = archivoPuzle

    def leer_matriz(self):
        tamaño = 0
        matriz_solucion = []
        matriz_usuario = []
        completado = False
        progreso = False

        try:
            if os.path.exists(self.archivoPuzle):
                with open(self.archivoPuzle, 'r') as file:
                    completado = file.readline().strip() == 'True'  # si está completo
                    progreso = file.readline().strip() == 'True'  # si hay progreso
                    tamaño = int(file.readline().strip())  # Lee el tamaño
                    # matriz de solución
                    for _ in range(tamaño):
                        fila_solucion = list(map(int, file.readline().split()))
                        matriz_solucion.append(fila_solucion)
                    # matriz de progreso del usuario
                    for _ in range(tamaño):
                        fila_usuario = list(map(int, file.readline().split()))
                        matriz_usuario.append(fila_usuario)
            else:
                print(f"Error: El archivo {self.archivoPuzle} no existe.")
        except Exception as e:
            print(f"Error al leer el archivo {self.archivoPuzle}: {e}")


        if not progreso and not completado:
            matriz_usuario = [[0 for _ in range(tamaño)] for _ in range(tamaño)]
            
        return tamaño, matriz_solucion, matriz_usuario, completado, progreso

    def guardar_matriz(self, matriz, completado, progreso):
        try:
            with open(self.archivoPuzle, 'r') as file:
                lineas = file.readlines()[3:]
            file.close()
            with open(self.archivoPuzle, 'w') as file:
                file.write(f"{'True' if completado else 'False'}\n")
                file.write(f"{'True' if progreso else 'False'}\n")
                file.write(f"{len(matriz)}\n")

                for i in range(len(matriz)): # Escribir la matriz de solución
                    file.write(lineas[i])

                for fila in matriz: # Escribir la matriz de progreso
                    file.write(' '.join(map(str, fila)) + '\n')
            
            file.close()
        except Exception as e:
            print(f"Error al escribir el archivo {self.archivoPuzle}: {e}")
        


    def cargar_tablero(self, tablero):
        matriz_solucion, matriz_usuario, progreso, completado = self.leer_matriz()
        if matriz_solucion and matriz_usuario:
            tablero.set_matriz(matriz_usuario)
            print("Tablero cargado con éxito.")
        else:
            print("No se pudo cargar el tablero.")