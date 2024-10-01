
from gestorEquipo import GestorEquipo
from gestorFecha import GestorFecha
def menu():
        ge = GestorEquipo()
        gf = GestorFecha()
        op = int(input('''
    [1] Cargar datos de equipos
    [2] Cargar datos de fechas 
    [3] Ver listado de equipo
    [4] Actualizar tabla de equipos
    [5] Ordenar tabla de posiciones
    [6] Almacenar tabla de posiciones en un archivo
    [7] Salir
    ---> '''))
        while op != 7:
            if op == 1:
                ge.cargaE() #carga los datos del archivo de equipos

            elif op == 2:
                gf.cargaF() #carga los datos del archivo de fechas

            elif op == 3:
                E = input('Ingrese nombre de equipo: ') #pide un nombre de equipo para mostrar sus fechas disputadas
                ge.Opcion3(E.upper(), gf)

            elif op == 4:
                gf.actualizarDatos(ge) #actualiza los datos del equipo de acuerdo a las fechas disputadas
                
            elif op == 5: 
                ge.ordenarTabla() #ordena la lista de acuerdo a los puntos
                print('                    TABLA DE POSICIONES')
                ge.tablaDePosiciones() #muestra la tabla de posiciones
            elif op == 6:
                ge.escribirArchivo() #Guarda la tabla de posiciones ordenada en la opcion anterior en un archivo csv
            else:
                print('Ingrese una opcion correcta')

            op = int(input('''
    [1] Cargar datos de equipos
    [2] Cargar datos de fechas 
    [3] Ver listado de equipo
    [4] Actualizar tabla de equipos
    [5] Ordenar tabla de posiciones
    [6] Almacenar tabla de posiciones en un archivo
    [7] Salir
    ---> '''))
        print('Salió')