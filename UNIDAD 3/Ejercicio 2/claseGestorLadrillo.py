import csv
from claseLadrillo import Ladrillo

class GestorLadrillo:
    __listaL = list

    def __init__(self):
        self.__listaL = []

    def agregarElemento(self, elemento):
        self.__listaL.append(elemento)
    
    def cargarDatos(self, gestorM):
        archivo = open('C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 3\\Ejercicio 2\\ladrillos.csv','r')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                elemento = Ladrillo(int(fila[0]), int(fila[1]), float(fila[2]), float(fila[3]))
                self.agregarElemento(elemento)
                unMaterial = gestorM.buscaMat(int(fila[1]))
                if unMaterial != False:
                    elemento.agregarElemento(unMaterial)
        print('Carga de Datos satisfactoria')
        archivo.close()
    
    def mostrar(self):
        for i in range(len(self.__listaL)):
            print('{}'.format(self.__listaL[i]))

    def mostrarMateriales(self):
        for i in range(len(self.__listaL)):
            print('{}'.format(self.__listaL[i].materiales()))

    def buscaLadrillo(self, id):
        i = 0
        band = False
        while i<len(self.__listaL) and band is False:
            if self.__listaL[i].getID() == id:
                band = i
            i += 1
        return band

    def Opcion1(self, id):
        pos = self.buscaLadrillo(id)
        if type(pos) is int:
            self.__listaL[pos].listarMaterial()
        else: 
            print('No se encontro ningun material con esa ID')

    def Opcion2(self, gestorM):
        for i in range(len(self.__listaL)):
            total = self.__listaL[i].getCosto() + gestorM.getAdicional(i)
            print('El costo total del ladrillo es: {:.2f}'.format(total))
    
    def Opcion3(self):
        print('Identificador \tMaterial \tCosto Asociado')
        for i in range(len(self.__listaL)):
            id = self.__listaL[i].getID()
            materiales = self.__listaL[i].getMateriales()
            if materiales != '':
                costoAsociado = self.__listaL[i].costoAs()
                print('    {}\t    \t   {}\t\t  {:.2f}'.format(id, materiales, costoAsociado))
            else:
                print(f'    {id}\t      \t{'-'}\t\t{'-'}')
