import csv
from claseAutobus import Autobus
from claseVanes import Vanes

class GestorVehiculo:
    __listaVehiculos = list

    def __init__(self):
        self.__listaVehiculos = []

    def agregarElemento(self, elemento):
        self.__listaVehiculos.append(elemento)
    
    def cargarDatos(self):
        archivo = open('/home/lia-m-01/Escritorio/Parcial 2/vehiculos.csv','r')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                if fila[0] == 'A':
                    elemento = Autobus(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8], fila[9])
                    self.agregarElemento(elemento)
                
                elif fila[0] == 'V':
                    elemento = Vanes(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8])
                    self.agregarElemento(elemento)
        print('Carga de Vehiculos satisfactoria')
        archivo.close()
    
    def mostrar(self):
        for i in range(len(self.__lista)):
            print('{}'.format(self.__lista[i]))

    def mostrarPos(self, xpos):
        i = 0
        band = False
        while i<len(self.__listaVehiculos) and band is False:
            if i == xpos:
                band = True
                if isinstance(self.__listaVehiculos[i], Autobus):
                    print(f'El elemento en la posicion {xpos} es del tipo Autobus')
                elif isinstance(self.__listaVehiculos[i], Vanes):
                    print(f'El elemento en la posicion {xpos} es del tipo Van')
            i += 1
    
    def cantidaPorTipo(self):
        cantA = 0
        cantV = 0
        for i in range(len(self.__listaVehiculos)):
            if isinstance(self.__listaVehiculos[i], Autobus):
                cantA += 1
            elif isinstance(self.__listaVehiculos[i], Vanes):
                cantV += 1
        print(f'La cantidad de vehiculos del tipo Autobus es: {cantA}')
        print(f'La cantidad de vehiculos del tipo Van es: {cantV}')

    def recorreVehiculos(self):
        for i in range(len(self.__listaVehiculos)):
            imp = self.__listaVehiculos[i].TarifaTransporte()
            print(f'Modelo: {self.__listaVehiculos[i].getModelo()}\t Año de fabricacion: {self.__listaVehiculos[i].getAñoF()}\nCapacidad de pasajeros: {self.__listaVehiculos[i].getCapPas()}\tTarifa de Servicio: {imp}\n')

    def recorreV(self):
        for vehiculo in self.__listaVehiculos:
            vehiculo.recorreV()
            