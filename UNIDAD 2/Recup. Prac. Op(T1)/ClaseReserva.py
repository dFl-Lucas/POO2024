class Reserva:
    __numR = int
    __nom = str
    __numCabAsig = int
    __fechaIn = str
    __cantHues= int
    __cantDias = int
    __impSeña = float

    def __init__(self, nr, nom, nca, fi, ch, cd, imps):
        self.__numR = nr
        self.__nom = nom
        self.__numCabAsig = nca
        self.__fechaIn = fi
        self.__cantHues = ch
        self.__cantDias = cd
        self.__impSeña = imps

    def getNumR(self):
        return self.__numR
    
    def getNom(self):
        return self.__nom
    
    def getNumC(self):
        return self.__numCabAsig
    
    def getFechaI(self):
        return self.__fechaIn
    
    def getCanH(self):
        return self.__cantHues
    
    def getCantD(self):
        return self.__cantDias
    
    def getImpS(self):
        return self.__impSeña