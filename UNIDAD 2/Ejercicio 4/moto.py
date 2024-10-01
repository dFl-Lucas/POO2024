class ClaseMoto:
    __pat:str
    __marca:str
    __NyA = str
    __km:float

    def __init__(self, patente, marca, nya, kilometraje):
        self.__pat = patente
        self.__marca = marca
        self.__NyA = nya
        self.__km = kilometraje
    
    def __str__(self):
        return f' Patente: {self.__pat}\n Marca: {self.__marca}\n Nombre y apellido: {self.__NyA}\n Kilometraje: {self.__km}'
    
    def getPatente(self):
        return self.__pat
    
    def getMarca(self):
        return self.__marca

    def getNyA(self):
        return self.__NyA

    def getConductor(self):
        return self.__nom + self.__ape
    
    def getKm(self):
        return self.__km