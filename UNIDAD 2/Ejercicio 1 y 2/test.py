from CajaDeAhorro import CajaDeAhorro 

def test():
    for i in [1,2,3]:
        nro = input('Ingrese numero de cuenta: ')
        cuil = input('Ingrese su cuil: ')
        ape = input(' Ingrese su apellido: ')
        nom = input('Ingrese su nombre: ')
        sal= float(input('Ingrese su saldo: '))
        
        objeto = CajaDeAhorro(nro, cuil, ape, nom, sal)

        objeto

        ext = float(input('Ingrese monto a extraer: '))
        objeto.extraer(ext)

        dep = float(input('Ingrese monto a depositar: '))
        objeto.depositar(dep)

        cuit = input('Ingrese cuit a validar: ')
        objeto.validar(cuit)
