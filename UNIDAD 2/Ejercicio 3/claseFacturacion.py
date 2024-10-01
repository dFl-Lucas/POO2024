class FacturacionFarmacia:
    __Facturacion = list

    def __init__(self, M, N, valor = 0):
        self.__Facturacion = [[valor]*N for _ in range(M)]

    def agregarLista(self, xlist):
        self.__Facturacion.append(xlist)

    def mostrarDat(self):
        for j in self.__Facturacion:
            for elemento in j:
                print(elemento, end='   ')
            print()