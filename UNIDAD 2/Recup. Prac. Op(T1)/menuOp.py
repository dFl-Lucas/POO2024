from GestorCabaña import GestorCabaña
from GestorReserva import GestorReserva

def menu():
    GC = GestorCabaña()
    GR = GestorReserva()
    GC.cargaCabañas()
    GR.cargarReservas()

    op = int(input('''
[1] Mostrar cantidad de cabañas con cantidad de huespedes igual al numero de ingresado
[2] Mostrar Listado de reservas 
[3] Salir
-->'''))
    while op != 3:
        if op == 1:
            cantH= int(input('Ingrese una cantidad de huespedes : '))
            GC.Opcion1(cantH, GR)
                
        elif op == 2:
            fecha = int(input('Ingrese una fecha:'))
            GC.Opcion2(fecha)

        else:
            print('Ingrese una opcion correcta')

        op = int(input('''
[1] Mostrar cantidad de cabañas con cantidad de huespedes igual al numero de ingresado
[2] Mostrar Listado de reservas 
[3] Salir
-->'''))
    print('Salió')