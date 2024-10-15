import pygame, sys

from traitlets import This
from constantes import *
from enum import Enum
from Tablero import Tablero
import os


class Lectura:
    def __init__(self, archivo_puzle):
        self.archivo_puzle = archivo_puzle

    def leer_matriz(self):
        matriz_solucion = []
        matriz_usuario = []
        completado = False
        progreso = False
        try:
            if os.path.exists(self.archivo_puzle):
                with open(self.archivo_puzle, 'r') as file:
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
                print(f"Error: El archivo {self.archivo_puzle} no existe.")
        except Exception as e:
            print(f"Error al leer el archivo {self.archivo_puzle}: {e}")
        return matriz_solucion, matriz_usuario, progreso, completado

    def guardar_matriz(self, matriz):
        try:
            with open(self.archivo_puzle, 'r') as file:
                lineas = file.readlines()[3:]  # Leer de la cuarta línea (solución y progreso)
            with open(self.archivo_puzle, 'w') as file:
                file.write(f"{'True' if completado else 'False'}\n")
                file.write(f"{'True' if progreso else 'False'}\n")
                file.write(f"{len(matriz_usuario)}\n")

                file.writelines(lineas)

                for fila in matriz_usuario:
                    file.write(' '.join(map(str, fila)) + '\n')

    def cargar_tablero(self, tablero):
        matriz_solucion, matriz_usuario, progreso, completado = self.leer_matriz()
        if matriz_solucion and matriz_usuario:
            tablero.set_matriz(matriz_usuario)
            print("Tablero cargado con éxito.")
        else:
            print("No se pudo cargar el tablero.")