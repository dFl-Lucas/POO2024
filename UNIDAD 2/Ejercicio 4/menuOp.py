from gestorMoto import GestorMotos
from gestorPedido import GestorPedidos

def Menu():
    GM = GestorMotos()
    GP = GestorPedidos()
    op = int(input('''
    [1] Cargar datos de motos
    [2] Cargar datos de pedidos 
    [3] Cargar nuevo pedido
    [4] Actualizar tiempo real de entrega 
    [5] Mostrar datos del conductor
    [6] Generar listado de motos
    [7] Ordenar pedidos por numero de patente         
    [8] Salir
    ---> '''))
    while op != 8:
        if op == 1:
           GM.cargarDatosM()

        elif op == 2:
            GP.cargarDatosP()

        elif op == 3:
            patAsig= input('Ingrese patente de la moto asignada: ')
            res = GM.validarPat(patAsig.upper())

            while res is False:
                print('No existe una moto con esa patente (Ingrese una patente válida)')
                patAsig= input('Ingrese patente de la moto asignada: ')
                res = GM.validarPat(patAsig.upper())

            idpedido= int(input('Ingrese id de pedido: '))
            comidas = input('Ingrese comidas pedidas: ')
            tiempoEst= int(input('Ingrese tiempo estimado de entrega (en minutos): '))
            precio = float(input('Ingrese el precio del pedido: '))
            GP.Opcion3(patAsig.upper(), idpedido, comidas, tiempoEst, precio)

        elif op == 4:
            xpatAsig= input('Ingrese patente de la moto asignada: ')
            xres = GM.validarPat(xpatAsig.upper())

            while xres is False:
                print('No existe una moto con esa patente (Ingrese una patente válida)')
                xpatAsig= input('Ingrese patente de la moto asignada: ')
                xres = GM.validarPat(xpatAsig.upper())

            idped= int(input('Ingrese id de pedido: '))
            treal = int(input('Ingrese el tiempo real de entrega (En minutos): '))
            GP.Opcion4(xpatAsig.upper(), idped, treal)
        
        elif op == 5: 
            patAs= input('Ingrese patente de la moto asignada: ')
            yres = GM.validarPat(patAs.upper())

            while yres is False:
                print('No existe una moto con esa patente (Ingrese una patente válida)')
                patAs= input('Ingrese patente de la moto asignada: ')
                yres = GM.validarPat(patAs.upper())
            
            GM.Opcion5(patAs, GP)

        elif op == 6:
           GM.Opcion6(GP)

        elif op == 7:
            GP.ordenar()

        else:
            print('Ingrese una opcion correcta')

        op = int(input('''
    [1] Cargar datos de motos
    [2] Cargar datos de pedidos 
    [3] Cargar nuevo pedido
    [4] Actualizar tiempo real de entrega 
    [5] Mostrar datos del conductor
    [6] Generar listado de motos
    [7] Ordenar pedidos por numero de patente         
    [8] Salir
    ---> '''))
        