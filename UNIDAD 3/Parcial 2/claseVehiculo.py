class Vehiculo:
    __marca = str
    __modelo = str
    __añoFabricacion = int
    __capPasajeros = int
    __numPlazas = int
    __distRecorrida = float
    __tarifaBase = float

    def __init__(self, mar, mod, añoF, capP, numP, distR, tarB):
        self.__marca = mar
        self.__modelo = mod
        self.__añoFabricacion = añoF 
        self.__capPasajeros = capP
        self.__numPlazas = numP
        self.__distRecorrida = distR
        self.__tarifaBase = tarB

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAñoF(self):
        return self.__añoFabricacion
    
    def getNumP(self): 
        return self.__numPlazas
    
    def getCapPas(self):
        return self.__capPasajeros
    
    def getDistReco(self):
        return self.__distRecorrida
    
    def getTarifaBase(self):
        return self.__tarifaBase
    
    def TarifaTransporte(self, dato=0):
        return self.__tarifaBase + dato
    
    '''def recorreV(self, dato=TarifaTransporte()):
        cadena = f'Modelo: {self.__modelo}\t Año de fabricacion: {self.__añoFabricacion}\nCapacidad de pasajeros: {self.__capPasajeros}\t'
        cadena += f'{dato}'''

    def __str__(self):
        return f'''
Marca: {self.__marca}
Modelo: {self.__modelo}
Año de fabricacion: {self.__añoFabricacion}
Numero de plazas: {self.__numPlazas}
Capacidad de pasajeros: {self.__capPasajeros}
Distancia recorrida: {self.__distRecorrida}
Tarifa base: {self.__tarifaBase}
'''