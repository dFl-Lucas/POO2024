class Cliente:
    __nombre = str
    __apellido = str
    __dni = int
    __nroCuenta = int
    __saldoAnt = float

    def __init__(self, nom, ape, dni, nroC, salAnt):
        self.__nombre = nom
        self.__apellido = ape
        self.__dni = dni
        self.__nroCuenta = nroC
        self.__saldoAnt = salAnt

    def getNom(self):
        return self.__nombre
    
    def getApe(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def getNROC(self):
        return self.__nroCuenta
    
    def getSaldo(self):
        return self.__saldoAnt
    
    def actualizaSaldo(self, nuevoSaldo):
        self.__saldoAnt = nuevoSaldo
    
    def __str__(self):
        return f' Nombre: {self.__nombre}\n Apeliido: {self.__apellido}\n DNI: {self.__dni}\n Numero de cuenta: {self.__nroCuenta}\n Saldo Anterior: {self.__saldoAnt}\n'