class CajaDeAhorro:
    __NroCuenta: str
    __Cuil: str
    __Apellido: str
    __Nombre: str
    __Saldo: float
    def __init__(self, NroCuenta, Cuil, Nombre, Apellido, Saldo):
        self.__NroCuenta = NroCuenta
        self.__Cuil = Cuil
        self.__Apellido = Apellido
        self.__Nombre = Nombre
        self.__Saldo = Saldo
    
    def Mostrar_datos(self):
        print('Numero de cuenta: {}'.format(self.__NroCuenta))
        print('Cuil: {}'.format(self.__Cuil))
        print('Apellido: {}'.format(self.__Apellido))
        print('Nombre: {}'.format(self.__Nombre))
        print('Saldo: {}'.format(self.__Saldo))
    
    def extraer(self, importe):
        if self.__Saldo >= importe:
            self.__Saldo = self.__Saldo - importe
            print('Saldo Actual: {}'.format(self.__Saldo))
        else:
            return -1

    def depositar(self, importe):
        if importe > 0:
            self.__Saldo += importe
            print('Saldo Actual: {}'.format(self.__Saldo))
        else:
            print('Error')

    def validar(self, xcuil):
        if len(xcuil) == 13:
            xcuil = xcuil.replace("-", "")
            cuilIngresado = xcuil
            lcuil = []
            j = 0
            for j in range(len(xcuil[:-1])):
                c = int(xcuil[j])
                lcuil.append(c)
            
            pesos = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
            suma = 0
            resto = 0
            i = 0
            digitoV = 0
            for i in range(len(lcuil)):
                suma += lcuil[i] * pesos[i]
            resto = suma % 11

            if resto == 0:
                digitoV = 0
            elif resto == 1:
                if lcuil[0] == 2 and lcuil[1] == 0:
                    digitoV = 9
                    lcuil[1] = 3
                    lcuil.append(digitoV)
                elif lcuil[0] == 2 and lcuil[1] == 7:
                    digitoV = 4
                    lcuil[1] = 3
                    lcuil.append(digitoV)
            else:
                digitoV = 11 - resto
                lcuil.append(digitoV)

            if lcuil == cuilIngresado:
                print('Cuil verificado')
            else:
                print('Cuil invalido')
                print('El cuil correcto seria: {}'.format(lcuil))
        else:
            print('Cuil erroneo')