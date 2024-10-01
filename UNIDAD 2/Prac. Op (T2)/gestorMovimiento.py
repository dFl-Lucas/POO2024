import csv
import numpy as np
from claseMovimiento import Movimiento

class GestorMovimiento:
    __cant = int
    __dimension = int
    __incremento = int
    __ArregloMovimientos = np.ndarray

    def __init__(self, dim=21):
        self.__cant = 0
        self.__dimension = dim
        self.__incremento = 5
        self.__ArregloMovimientos = np.empty(self.__dimension, dtype=Movimiento)

    def agregarMovimiento(self, unMovi):
        if self.__dimension == self.__cant:
            self.__dimension += self.__incremento
            self.__ArregloMovimientos.resize(self.__dimension)
        self.__ArregloMovimientos[self.__cant]=unMovi
        self.__cant += 1
    
    def cargaMov(self):
        archivo = open('MovimientosAbril2024.csv','r')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = not band
            else:
                unMov = Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4]))
                self.agregarMovimiento(unMov)
        print('Carga de Movimientos satisfactoria')
        archivo.close()

    def contarMov(self, nroC):
        i = 0
        band = False
        while i < len(self.__ArregloMovimientos) and band == False:
            if self.__ArregloMovimientos[i].getNroC() == nroC:
                band = True
            else:
                i += 1
        return band 
    
    def ordenar(self):
        self.__ArregloMovimientos = np.sort(self.__ArregloMovimientos)
        #self.__ArregloMovimientos[:self.__cant].sort() sirve para ordenar hasta el indice indicado evitando las componentes vacias o basura
        print('Se ordenaron los movimientos por numero de cuenta')

    def mostrar(self):
        for i in range(len(self.__ArregloMovimientos)):
            print('{}'.format(self.__ArregloMovimientos[i]))
