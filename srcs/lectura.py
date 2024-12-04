import pygame, sys

from traitlets import This
from srcs.constantes import *
from enum import Enum
from srcs.Tablero import Tablero
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
        pistas = 0

        try:
            if os.path.exists(self.archivoPuzle):
                with open(self.archivoPuzle, 'r') as file:
                    completado = file.readline().strip() == 'True'  # si está completo
                    progreso = file.readline().strip() == 'True'  # si hay progreso
                    tamaño = int(file.readline().strip())  # Lee el tamaño
                    pistas = int(file.readline().strip())  # cantidad de pistas
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


        nombre = self.archivoPuzle.split("\\")[-1]
        nombre = nombre.split("_")[-1]
        nombre = nombre.split(".")[0]
         
        return tamaño, matriz_solucion, matriz_usuario, completado, progreso, nombre, pistas

    def guardar_matriz(self, matriz, completado, progreso, pistas):
        try:
            with open(self.archivoPuzle, 'r') as file:
                lineas = file.readlines()[4:]
            file.close()
            with open(self.archivoPuzle, 'w') as file:
                file.write(f"{'True' if completado else 'False'}\n")
                file.write(f"{'True' if progreso else 'False'}\n")
                file.write(f"{len(matriz)}\n")
                file.write(f"{pistas}\n")

                for i in range(len(matriz)): # Escribir la matriz de solución
                    file.write(lineas[i])

                for fila in matriz: # Escribir la matriz de progreso
                    file.write(' '.join(map(str, fila)) + '\n')
            
            file.close()
        except Exception as e:
            print(f"Error al escribir el archivo {self.archivoPuzle}: {e}")
        


    def cargar_tablero(self, tablero):
        matriz_solucion, matriz_usuario, progreso, completado, pistas = self.leer_matriz()
        if matriz_solucion and matriz_usuario:
            tablero.set_matriz(matriz_usuario)
            print("Tablero cargado con éxito.")
        else:
            print("No se pudo cargar el tablero.")