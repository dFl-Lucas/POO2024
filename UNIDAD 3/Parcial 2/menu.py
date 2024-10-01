from gestorVehiculos import GestorVehiculo
from claseAutobus import Autobus
from claseVanes import Vanes

def menu():
    GestorV = GestorVehiculo()
    GestorV.cargarDatos()

    op = int(input('''
        -------> MENU DE OPCIONES <-------
    [1] Agregar vehiculos a la coleccion
    [2] Tipo de vehiculo
    [3] Cantidad de vehiculos de cada tipo
    [4] Mostrar datos de vehiculos
    [5] Salir
    --> '''))
    while op != 5:
        if op == 1:
            tipo = (int(input('''
    Ingrese el tipo de vechiculo que desea agregar:
    [1] Autobus
    [2] Van
    ''')))
            while tipo != 1 and 2:
                tipo = (int(input('''
    Ingrese el tipo de vechiculo que desea agregar:
    [1] Autobus
    [2] Van
    ''')))
            if tipo == 1:
                marca = input('Ingrese la marca del vehiculo: ')
                Modelo = input('Ingrese el modelo del vehiculo: ')
                añoF = int(input('Ingrese el año de fabricacion: '))
                capPas = int(input('Ingrese la capacidad de pasajeros: '))
                numPla = int(input('Ingrese el numero de plazas: '))
                distREc = float(input('Ingrese la distancia recorrida: '))
                tarifBase = float(input('Ingrese la tarfifa base: '))
                tipoS = input('Ingrese el tipo de servicio: ')
                turno = input('Ingrese el turno en que se brindo: ')
                elemento = Autobus(marca, Modelo, añoF, capPas, numPla, distREc, tarifBase, tipoS, turno)
                GestorVehiculo.agregarElemento(elemento)

            else:
                marca = input('Ingrese la marca del vehiculo: ')
                Modelo = input('Ingrese el modelo del vehiculo: ')
                añoF = int(input('Ingrese el año de fabricacion: '))
                capPas = int(input('Ingrese la capacidad de pasajeros: '))
                numPla = int(input('Ingrese el numero de plazas: '))
                distREc = float(input('Ingrese la distancia recorrida: '))
                tarifBase = float(input('Ingrese la tarfifa base: '))
                tipoCarroceria = input('Ingrese el tipo de carroceria: ')
                elemento = Vanes(marca, Modelo, añoF, capPas, numPla, distREc, tarifBase, tipoCarroceria)
                GestorV.agregarElemento(elemento)
                
        elif op == 2:
            posicion = int(input('Ingrese una posicion de la lista: '))

            GestorV.mostrarPos(posicion)
            
        elif op == 3:
            GestorV.cantidaPorTipo()

        elif op == 4:
            GestorV.recorreVehiculos()
            #GestorV.recorreV()
        else:
            print('Ingrese una opcion correcta')
        
        op = int(input('''
        -------> MENU DE OPCIONES <-------
    [1] Agregar vehiculos a la coleccion
    [2] Tipo de vehiculo
    [3] Cantidad de vehiculos de cada tipo
    [4] Mostrar datos de vehiculos
    [5] Salir
    --> '''))
    print('Salió')

if __name__ == '__main__':
    menu()