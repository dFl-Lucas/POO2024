from claseVehiculo import Vehiculo

class Vanes(Vehiculo):
    __tipoCarroceria = str

    def __init__(self, mar, mod, añoF, capP, numP, distR, tarB, tipoC):
        super().__init__(mar, mod, añoF, capP, numP, distR, tarB)
        self.__tipoCarroceria = tipoC

    def getTipoCarr(self):
        return self.__tipoCarroceria
    
    def TarifaTransporte(self, dato=0):
        porciento = 0
        if self.__tipoCarroceria == 'minivan':
            porciento = (10 * super().getTarifaBase()) / 100
            return super().TarifaTransporte(-porciento)
        else: 
            porciento = (2.5 * super().getTarifaBase()) / 100
            return super().TarifaTransporte(porciento)
        
    def recorreV(self):
        return super().recorreV(self.TarifaTransporte())

    def __str__(self):
        return f'Tipo de carroceria: {self.__tipoCarroceria}'