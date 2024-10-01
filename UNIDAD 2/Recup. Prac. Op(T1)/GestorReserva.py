import csv
from ClaseReserva import Reserva

class GestorReserva:
    __listaReservas = list

    def __init__(self):
        self.__listaReservas = []

    def agregarReserva(self, unReserva):
        self.__listaReservas.append(unReserva)
    
    def cargarReservas(self):
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\Recup. Prac. Op(T1)\\Reservas.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                unaRes = Reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), float(fila[6]))
                self.agregarReserva(unaRes)
        print('Carga de Clientes satisfactoria')
        archivo.close()

    def buscarNum(self, numero):
        i = 0 
        band = False
        while i<len(self.__listaReservas) and band is False:
            if self.__listaReservas[i].getNumC() == numero:
                band = True
            i += 1
        return band
    
    def Opcion2(self, fecha):
        print(f'Reservas para la fecha: {fecha}')
        print('{:^10}    {:^10}    {:^10}    {:^10}     {:^10}'.format('N° de cabaña', 'Importe diario', 'Cantidad de dias', 'Seña', 'Importe a cobrar'))
        for i in range(len(self.__listaReservas)):
            if self.__listaReservas[i].getFecha() == fecha:
                #pedir el numero de cabaña asignado y buscar el imp diario de esa cabaña
                print('{:^30}      {:^30}      {:^30}      {:^30}      {:^30}'.format(self.__listaReservas[i].getNumC(), self.__listaReservas[i].getImp))