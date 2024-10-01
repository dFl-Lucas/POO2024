from claseVehiculo import Vehiculo

class Autobus(Vehiculo):
    __tipoServicio = str
    __turnoEnQueSeBrindo = str
   
    def __init__(self, mar, mod, añoF, capP, numP, distR, tarB, tipS, turno):
        super().__init__(mar, mod, añoF, capP, numP, distR, tarB)
        self.__tipoServicio = tipS
        self.__turnoEnQueSeBrindo = turno

    def getTipoSer(self):
        return self.__tipoServicio
    
    def getTurno(self):
        return self.__turnoEnQueSeBrindo
    
    def TarifaTransporte(self):
        porciento = 0
        if (self.__turnoEnQueSeBrindo == 'noche') and (self.__tipoServicio == 'turismo'):
            porciento = (20 * super().getTarifaBase()) / 100
        else:
            porciento = (5 * super().getTarifaBase()) / 100
        return super().TarifaTransporte(porciento)
    
    def recorreV(self):
        return super().recorreV(self.TarifaTransporte())
    
    def __str__(self):
        return f'Tipo de servicio: {self.__tipoServicio}\n Turno en que se brindo: {self.__turnoEnQueSeBrindo}\n'
