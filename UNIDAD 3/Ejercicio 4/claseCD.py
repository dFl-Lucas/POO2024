from clasePublicaciones import Publicaciones

class CD(Publicaciones):
    __tiempoRepr = int
    __nomNarrador = str

    def __init__(self, tit, cat, pre, tiemRe, nomNarr):
        super().__init__(tit, cat, pre)
        self.__tiempoRepr = tiemRe
        self.__nomNarrador = nomNarr

    def __str__(self):
        return super().__str__() + f'\nTiempo de reproduccion: {self.__tiempoRepr}\tNombre de Narrador: {self.__nomNarrador}'
    
    def impVenta(self):
        porciento = (10 * super().getPB()) / 100
        return super().impVenta(porciento)
    
        