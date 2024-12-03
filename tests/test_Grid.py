import unittest
from Grid import Grid

class TestGrid(unittest.TestCase):

    def setUp(self):
        self.blockCant = 10
        self.matrizUsuario = [ # Matriz de ejemplo, con valores que el usuario podria haber colocado
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,1,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0]
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
        self.grid = Grid(self.blockCant, self.matrizUsuario, self.matrizSolucion)

    def test_getMatrizTranspuesta(self):
        matrizOriginal = [
            [1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        matrizTranspuesta = [
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0]
        ]
        self.assertEqual(self.grid.getMatrizTranspuesta(matrizOriginal), matrizTranspuesta)
    def test_comprobarSolucionTablero(self):
        self.assertFalse(self.grid.comprobarSolucionTablero(self.matrizUsuario))
        self.assertTrue(self.grid.comprobarSolucionTablero(self.matrizSolucion))
    def test_listaAIndice(self):
        fila = [0,1,0,1,1,1,0,0,1,1]
        self.assertEqual(self.grid.listaAIndice(fila),[1,3,2])    
    def test_contarBloquesIguales(self):
        self.assertEqual(self.grid.contarBloquesIguales(self.matrizUsuario,self.matrizSolucion), 8)  
    def test_contarBloquesMarcados(self):
        self.assertEqual(self.grid.contarBloquesMarcados(self.matrizSolucion), 18)
        self.assertEqual(self.grid.contarBloquesMarcados(self.matrizUsuario), 13)
    def test_getPorcentajeCompletado(self):
        self.assertEqual(self.grid.getPorcentajeCompletado(self.matrizUsuario, self.matrizSolucion), self.grid.contarBloquesIguales(self.matrizUsuario,self.matrizSolucion)/self.grid.contarBloquesMarcados(self.matrizSolucion))