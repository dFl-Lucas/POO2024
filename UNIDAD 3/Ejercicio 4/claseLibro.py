from clasePublicaciones import Publicaciones

class Libro(Publicaciones):
    __NomAutor = str
    __fechEdicion = str
    __cantPag = int

    def __init__(self, tit, cat, pre, nomA, fechE, cantP):
        super().__init__(tit, cat, pre)
        self.__NomAutor = nomA
        self.__fechEdicion = fechE
        self.__cantPag = cantP

    def __str__(self):
        return super().__str__() + f'\nNombre de Autor: {self.__NomAutor}\tFecha de edicion: {self.__fechEdicion}\tCantidad de paginas: {self.__cantPag}'
    
    def calculaFecha(self):
        fecha = str
        nueva_fecha = self.__fechEdicion.replace('/','')
        for i in nueva_fecha:
            if i > 4:
                fecha + nueva_fecha[i]
        return int(fecha)

    def impVenta(self):
        añoEdicion = self.__fechEdicion[6:10]
        antiguedad = 2024 - int(añoEdicion)
        porciento = (antiguedad * float(super().getPB())) / 100
        return super().impVenta(-porciento)