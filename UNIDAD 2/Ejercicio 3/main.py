from clasemenu import Menu
from claseFacturacion import FacturacionFarmacia

def test():
    matriz = FacturacionFarmacia(5, 7)
    matriz.mostrarDat()
    opcion = int(input(''' 
                    MENU DE OPCIONES
 [1] Cargar factura
 [2] Calcular total facturado en la semana por una sucursal
 [3] Calcular sucucrsal que mas facturo en un dia
 [4] Calcular sucursal con menos facturacion en la semana
 [5] Calcular total facturado en la semana por todas las sucursales
 [6] Salir
 -->'''))
    menuOp = Menu()
    while opcion != 6:
        menuOp.opcion(opcion, )
        if opcion == 1:
            dia = int(input('Ingrese dia de la semana: '))
            sucu = int(input('Ingrese numero de sucursal: '))
            importe = float(input('Ingrese importe de factura: '))
            menuOp.opcion(opcion, dia, sucu, importe, matriz)
        elif opcion == 2:
            sucu2 = int(input('Ingrese numero de sucursal: '))
            menuOp.opcion2(op=2, suc=sucu2, mat=matriz)
        elif opcion == 3:
            print()
        elif opcion == 4:
            print()
        elif opcion == 5:
            print()
        else:
            print('Ingrese una opcion valida')

if __name__ == '__main__':
    test()
