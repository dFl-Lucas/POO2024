import csv
from moto import ClaseMoto
class GestorMotos:
    __listaMoto: list

    def __init__(self):
        self.__listaMoto = []

    def cargarDatosM(self):
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 2\\Ejercicio 4\\datosMotos.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unaMoto = ClaseMoto(fila[0], fila[1], fila[2], float(fila[3]))
                self.__listaMoto.append(unaMoto)
        print('Datos cargados correctamente')
        archivo.close()
    
    def buscaConductor(self, pat):
        i = 0
        band = False
        while i<len(self.__listaMoto) and band is False:
            if self.__listaMoto[i].getPatente() == pat:
                band = i
            i += 1
        return band

    def Opcion5(self, Pat, gestorP):
        indice = self.buscaConductor(Pat)
        print (f'DATOS DEL CONDUCTOR')
        print(f'Nombre y apellido: {self.__listaMoto[indice].getNyA()}')
        sum = 0
        cont = 0
        for i in range(len(gestorP._GestorPedidos__listaPedidos)):
            if gestorP._GestorPedidos__listaPedidos[i].getPat() == Pat:
                sum += gestorP._GestorPedidos__listaPedidos[i].getReal()
                cont += 1
        prom = float(sum/cont)
        print('El promedio real de entrega es: {:.2f}'.format(prom))

    def validarPat(sefl, patente):
        i = 0
        band = False
        while i<len(sefl.__listaMoto) and band is False:
            if sefl.__listaMoto[i].getPatente() == patente:
                band = True
            i += 1
        return band
    
    def Opcion6(self, gestorP):
        for i in range(len(self.__listaMoto)):
            print(f' PATENTE: {self.__listaMoto[i].getPatente()}\n CONDUCTOR: {self.__listaMoto[i].getNyA()}')
            print(f'ID DE PEDIDO            TIEMPO ESTIMADO         TIEMPO REAL         PRECIO')
            sum = 0
            for j in range(len(gestorP._GestorPedidos__listaPedidos)):
                if gestorP._GestorPedidos__listaPedidos[j].getPat() == self.__listaMoto[i].getPatente():
                    idped = int(gestorP._GestorPedidos__listaPedidos[j].getId())
                    tEst = int(gestorP._GestorPedidos__listaPedidos[j].getEst())
                    tReal = int(gestorP._GestorPedidos__listaPedidos[j].getReal())
                    pre = float(gestorP._GestorPedidos__listaPedidos[j].getPrecio())
                    sum += pre
                    print(f'{idped}                     {tEst}                      {tReal}                   {pre}')
            print('Total: ${:.2f}'.format(sum))
            print('Comision: {:.2f}'.format((20*sum)/100))
            
