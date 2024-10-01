import numpy as np
import csv
from ClaseCabaña import Cabaña

class GestorCabaña:
    __cant = int
    __dimension = int
    __incremento = int
    __ArregloCabañas = np.ndarray

    def __init__(self, dim=10):
        self.__cant = 0
        self.__dimension = dim
        self.__incremento = 5
        self.__ArregloCabañas = np.empty(self.__dimension, dtype=Cabaña)

    def agregarCabaña(self, unaCabaña):
        if self.__dimension == self.__cant:
            self.__dimension += self.__incremento
            self.__ArregloCabañas.resize(self.__dimension)
        self.__ArregloCabañas[self.__cant]=unaCabaña
        self.__cant += 1
    
    def cargaCabañas(self):
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\Recup. Prac. Op(T1)\\Cabañas.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = not band
            else:
                unaCabaña = Cabaña(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]))
                self.agregarCabaña(unaCabaña)
        print('Carga de cabañas satisfactoria')
        archivo.close()

    def Opcion1(self, cantHues, gestorR):
        for i in range(len(self.__ArregloCabañas)):
            num = self.__ArregloCabañas[i].getNum()
            band = gestorR.buscarNum(num)
            if self.__ArregloCabañas[i].getCap() >= cantHues:
                if band is True:
                    print(f'La cabaña {self.__ArregloCabañas[i].getNum()} tiene una capacidad de {self.__ArregloCabañas[i].getCap()} huespedes')
                else:
                    print('na hay cabañas disponibles con esa capacidad')

