class CuentaBancaria:
    __nombre = str
    __apellido = str
    __cuil = str
    __saldo = float

    def __init__(self, nombre, apellido, cuil, saldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil
        self.__saldo = saldo
    
    def obtenerSal(self):
        return self.__saldo

    def obtenerApe(self):
        return self.__apellido

    def obtenerNom(self):
        return self.__nombre

    def obtenerCuil(self):
        return self.__cuil