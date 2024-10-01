class Departamento:
    __idDep = int
    __AyN = str
    __numPiso = int
    __numDep = int
    __cantHab = int
    __cantBaños = int
    __supCub = float

    def __init__(self, id, ayn, nP, nD, cH, cB, superCub):
        self.__idDep = id
        self.__AyN = ayn
        self.__numPiso = nP
        self.__numDep = nD
        self.__cantHab = cH
        self.__cantBaños = cB
        self.__supCub = superCub

    def __str__(self):
        return 'Id: {}\n Nombre y apellido del propietario: {}\n Numero de piso: {}\n Numero de Departamento: {}\n Cantidad de habitaciones: {}\n Cantidad de baños: {}\n Superficie cubierta: {}'.format(self.__idDep, self.__NyA, self.__numPiso, self.__numDep, self.__cantHab, self.__cantBaños, self.__supCub)

    def getID(self):
        return self.__idDep
    
    def getAyN(self):
        return self.__NyA

    def getNumP(self):
        return self.__numPiso

    def getnumD(self):
        return self.__numDep

    def getCantH(self):
        return self.__cantHab

    def getCantB(self):
        return self.__cantBaños
    
    def getSuperCub(self):
        return self.__supCub