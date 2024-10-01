class Cabaña:
    __num = int
    __canHab = int
    __cantCamG = int
    __cantCamChi = int
    __impDia = float
    __capacidad = int

    def __init__(self, n, ch, cg, cc, impd):
        self.__num = n
        self.__canHab = ch
        self.__cantCamG = cg
        self.__cantCamChi = cc
        self.__impDia = impd
        self.__capacidad = (cg*2)+cc
    
    def getNum(self):
        return self.__num
    
    def getCanH(self):
        return self.__canHab
    
    def getCanCG(self):
        return self.__cantCamG
    
    def getCanCC(self):
        return self.__cantCamChi
    
    def getImpD(self):
        return self.__impDia
    
    def getCap(self):
        return self.__capacidad
    
    def __ge__(self, otro):
        #capacidad = (self.__cantCamG * 2) + self.__cantCamChi
        return self.__capacidad >= otro