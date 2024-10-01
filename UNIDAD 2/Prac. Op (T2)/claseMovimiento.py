class Movimiento:
    __NroCuenta = int
    __Fecha = str
    __Decrip = str
    __tipoMov = str 
    __importe = float

    def __init__(self, nroC, fecha, des, tipoM, imp):
        self.__NroCuenta = nroC
        self.__Fecha = fecha
        self.__Decrip = des
        self.__tipoMov = tipoM
        self.__importe = imp

    def getNroC(self):
        return self.__NroCuenta
    
    def getFecha(self):
        return self.__Fecha
    
    def getDesc(self):
        return self.__Decrip
    
    def getTM(self):
        return self.__tipoMov
    
    def getIMP(self):
        return self.__importe
    
    def __str__(self):
        return f' Numero de cuenta: {self.__NroCuenta}\n Fecha: {self.__Fecha}\n Descripcion: {self.__Decrip}\n Tipo de movimiento: {self.__tipoMov}\n Importe: {self.__importe}\n'
  
    def __lt__ (self, otro):
        return self.__NroCuenta < otro.getNroC()