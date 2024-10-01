import csv
from claseMaterialRefractario import MaterialRefractario

class GestorMaterial:
    __listaM = list

    def __init__(self):
        self.__listaM = []

    def agregarElemento(self, elemento):
        self.__listaM.append(elemento)
    
    def cargarDatos(self):
        archivo = open('C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 3\\Ejercicio 2\\materiales.csv','r')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                elemento = MaterialRefractario(int(fila[0]), fila[1], float(fila[2]), float(fila[3]))
                self.agregarElemento(elemento)
        print('Carga de Datos satisfactoria')
        archivo.close()
    
    def buscaMat(self, id):
        i = 0
        band = False
        while i<len(self.__listaM) and band is False:
            if self.__listaM[i].getMaterial() == id:
                band = self.__listaM[i]
            i += 1
        return band

    def mostrar(self):
        for i in range(len(self.__listaM)):
            print('{}'.format(self.__listaM[i]))

    def getAdicional(self, indice):
        return self.__listaM[indice].getCostAd()