from gestorCliente import GestorCliente
from gestorMovimiento import GestorMovimiento

def menu():
    GC = GestorCliente()
    Gm = GestorMovimiento()
    GC.cargaCli()
    Gm.cargaMov()
    op = int(input('''
[1] Actualizar y ver datos
[2] Ver movimientos del mes
[3] Ordenar Gestor Movimientos
[4] Salir
-->'''))
    while op != 4:
        if op == 1:
            dni = int(input('Ingrese DNI: '))
            GC.Opcion1(dni, Gm)
                
        elif op == 2:
            xdni = int(input('Ingrese DNI:'))
            GC.Opcion2(xdni, Gm)
            
        elif op == 3:
            Gm.ordenar()
        else:
            print('Ingrese una opcion correcta')
        
        op = int(input('''
[1] Actualizar y ver datos
[2] Ver movimientos del mes
[3] Ordenar Gestor Movimientos
[4] Salir
-->'''))
    print('Salió')