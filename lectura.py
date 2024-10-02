import pygame, sys

from traitlets import This
from constantes import *
from enum import Enum
from Tablero import Tablero
import os


class Lectura:
    def __init__(self, archivo_solucion, archivo_guardado):
        self.archivo_solucion = archivo_solucion
        self.archivo_guardado = archivo_guardado

    def leer_matriz(self, archivo):
        matriz = []
        try:
            if os.path.exists(archivo):  # Verifica si el archivo existe
                with open(archivo, 'r') as file:
                    for linea in file:
                        fila = list(map(int, linea.split()))  # Convierte cada línea en una lista de enteros
                        matriz.append(fila)
            else:
                print(f"Error: El archivo {archivo} no existe.")
        except Exception as e:
            print(f"Error al leer el archivo {archivo}: {e}")
        return matriz

    def guardar_matriz(self, matriz):
        try:
            with open(self.archivo_guardado, 'w') as file:
                for fila in matriz:
                    file.write(' '.join(map(str, fila)) + '\n')
            print(f"Matriz guardada en {self.archivo_guardado}")
        except Exception as e:
            print(f"Error al guardar la matriz en {self.archivo_guardado}: {e}")

    #  cargar el estado de un Tablero desde la matriz leída
    def cargar_tablero(self, tablero: Tablero):
        matriz = self.leer_matriz(self.archivo_solucion)
        if matriz:
            tablero.set_matriz(matriz)
            print("Tablero cargado con éxito.")
        else:
            print("No se pudo cargar el tablero.")