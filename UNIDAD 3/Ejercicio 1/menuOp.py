from gestorEdificio import GestorEdificio

def menu():
    GE = GestorEdificio()
    GE.carga()
    op = int(input('''
[1] Mostrar datos de deparamentos
[2] Calcular superficie total de edificio
[3] Calcular superfice de departamento 
[4] Mostrar cantidad de departamentos con 3 dormitorios y mas de un baño
[5] Salir
--> '''))
    while op != 5:
        if op == 1:
            edi = input('Ingrese nombre de edificio: ') #Ingresa un nombre de edifcio 
            edi = edi.replace(' ','') #le quitamos los espacios en blanco
            GE.Opcion1(edi.upper()) #y transformamos la cadena a todo mayuscula

        elif op == 2:
            xedi = input('Ingrese nombre de edificio: ') #realizo los mismos pasos que arriba
            xedi = xedi.replace(' ','')
            GE.Opcion2(xedi.upper())
        elif op ==3:
            dueño = input('Ingrese apellido y nombre de propietario: ') #Pedimos que ingrese el apellido y nombre para evitar confuciones
            dueño = dueño.replace(' ','') #realizo los mismos que en las opciones 1 y 2 para pasar el nombre que ingreso
            GE.Opcion3(dueño.upper())
        elif op == 4:
            num = int(input('Ingrese numero de piso: ')) 
            GE.Opcion4(num)
            pass
        else:
            print('Ingrese una opcion valida')
        
        op = int(input('''
[1] Mostrar datos de deparamentos
[2] Calcular superficie total de edificio
[3] Calcular superfice de departamento 
[4] Salir
--> '''))
    print('Salió')

