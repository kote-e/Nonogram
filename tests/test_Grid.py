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
        self.matrizIndices = [ #Indices de la matriz solución
            [[1],[1],[4,1],[1],[1],[1],[1],[4,1],[1],[1]],
            [[1,1],[1,1],[1,1],[1,1],[],[],[1,1],[1,1],[6],[]]
        ]
        self.grid = Grid(self.blockCant, self.matrizUsuario, self.matrizIndices, self.matrizSolucion)

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
    def test_comprobarFila(self):
        self.assertTrue(self.grid.comprobarFila(self.matrizUsuario[0],self.matrizSolucion[0]))
        self.assertFalse(self.grid.comprobarFila(self.matrizUsuario[4],self.matrizSolucion[4]))
    def test_comprobarColumna(self):
        self.assertTrue(self.grid.comprobarColumna([self.matrizSolucion[i][0] for i in range(self.blockCant)],[self.matrizSolucion[i][0] for i in range(self.blockCant)]))
        self.assertFalse(self.grid.comprobarColumna([self.matrizUsuario[i][1] for i in range(self.blockCant)],[self.matrizSolucion[i][1] for i in range(self.blockCant)]))
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