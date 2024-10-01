import unittest
from claseLibro import Libro
from claseLista import Lista
from claseCD import CD

class TestDeValidacion(unittest.TestCase):
    def setUp(self):
        self.__listaEnlazada = Lista()
        self.__libro = Libro('Perro','Adultos',2000.50,'Kiara','15/02/2024',8)
        self.__cd = CD('Casa','Adultos',2000.50,5,'Pedro Juarez')
        self.__listaEnlazada.agregar_Al_Final(self.__libro)
        self.__listaEnlazada.agregar_Al_Inicio(self.__cd)

    def test_obtener_tamaño(self):
        self.assertEqual(self.__listaEnlazada.obtenerTamaño(), 2)

    def test_obtener_cab(self):
        self.assertEqual(self.__listaEnlazada.obtenerCabeza(), self.__cd)
    def test_obtener_cola(self):
        self.assertEqual(self.__listaEnlazada.obtenerCola(), self.__libro)


if __name__=='__main__':
    unittest.main()