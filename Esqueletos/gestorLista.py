import csv
class GestorX:
    __lista = list

    def __init__(self):
        self.__lista = []

    def agregarElemento(self, elemento):
        self.__lista.append(elemento)
    
    def cargarDatos(self):
        archivo = open('X','r')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                elemento = C(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4]))
                self.agregarElemento(elemento)
        print('Carga de Clientes satisfactoria')
        archivo.close()
    
    def mostrar(self):
        for i in range(len(self.__lista)):
            print('{}'.format(self.__lista[i]))