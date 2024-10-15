import unittest
from Grid import Grid

class TestGrid(unittest.TestCase):

    def setUp(self):
        self.blockCant = 10
        self.matrizValoresBloques = [ # Matriz de ejemplo, con valores que el usuario podria haber colocado
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,0],
            [1,1,1,1,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1]
        ]
        self.matrizSolucion = [ # Nonograma de ejemplo
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,1,0],
            [0,0,1,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        self.matrizIndices = [ #Indices de la matriz solución
            [[1],[1],[4,1],[1],[1],[1],[1],[4,1],[1],[1]],
            [[1,1],[1,1],[1,1],[1,1],[],[],[1,1],[1,1],[6],[]]
        ]
        self.grid = Grid(self.blockCant, self.matrizValoresBloques, self.matrizIndices, self.matrizSolucion)

    def test_contarBloquesIguales(self):
        self.assertEqual(self.grid.contarBloquesIguales(self.matrizValoresBloques,self.matrizSolucion), 8)  
    def test_contarBloquesMarcados(self):
        self.assertEqual(self.grid.contarBloquesMarcados(self.matrizSolucion), 18)
        self.assertEqual(self.grid.contarBloquesMarcados(self.matrizValoresBloques), 13)
    def test_calcularPorcentaje(self):
        self.assertEqual(self.grid.calcularPorcentaje(self.matrizValoresBloques, self.matrizSolucion), self.grid.contarBloquesIguales(self.matrizValoresBloques,self.matrizSolucion)/self.grid.contarBloquesMarcados(self.matrizSolucion)) # Deberia ser 8/18 = 0.44...)