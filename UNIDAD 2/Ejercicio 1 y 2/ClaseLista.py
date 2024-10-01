from ClaseCuentaBancaria import CuentaBancaria

class Lista:
    __cuentas = list

    def __init__(self):
        __cuentas = []

    def agregarCuenta(self, unaCuenta):
        self.__cuentas.append(unaCuenta)

    def obtenerDatos(self, xcuil):
        encontrado = False
        while CuentaBancaria != 0 or encontrado == True:
            hcuil = CuentaBancaria.obtenerCuil
            if hcuil == xcuil:
                encontrado = True
        
        if encontrado == True:
            xnom = CuentaBancaria.obtenerNom
            print('Nombre: {}'.format(xnom))
            xape = CuentaBancaria.obtenerApe
            print('Apellido: {}'.format(xape))
            xsal = CuentaBancaria.obtenerSal
            print('Saldo: {}'.format(xsal))
        else:
            print('CUIL No valido') 