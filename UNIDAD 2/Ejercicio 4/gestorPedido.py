import csv
from pedido import ClasePedido
class GestorPedidos:
    __listaPedidos: list

    def __init__(self):
        self.__listaPedidos = []
    
    def cargarDatosP(self):
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 2\\Ejercicio 4\\datosPedidos.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unPedido = ClasePedido(fila[0], int(fila[1]), fila[2], int(fila[3]), float(fila[5]), int(fila[4]))
                self.__listaPedidos.append(unPedido)
        print('Datos cargados correctamente')
        archivo.close()

    def Opcion3(self, pat, id, comidas, tEst, precio):
        nuevoPedido = ClasePedido(pat,id, comidas, tEst, precio)
        self.__listaPedidos.append(nuevoPedido)

    def Opcion4(self, pat, idPed, tiempoR):
        i = 0
        band = False
        while i<len(self.__listaPedidos) and band is False:
            if (self.__listaPedidos[i].getPat() == pat) and (self.__listaPedidos[i].getId() == idPed):
                self.__listaPedidos[i].modificaTiempo(tiempoR)
                band = True
            i += 1
        print('Tiempo real modificado correctamente')
   
    def mostrarPedidos(self, pat):
        for i in range(len(self.__listaPedidos)):
            if self.__listaPedidos[i].getPat() == pat:
                print(f'{self.__listaPedidos[i].getId()}            {self.__listaPedidos[i].getEst()}           {self.__listaPedidos[i].getReal()}          {self.__listaPedidos[i].getPrecio()}')
    
    def ordenar(self):
        self.__listaPedidos.sort()

    def mostrar(self):
        for i in range(len(self.__listaPedidos)):
            print('{}'.format(self.__listaPedidos[i]))