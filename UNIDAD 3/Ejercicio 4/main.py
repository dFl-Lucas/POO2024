from claseLista import Lista
from claseLibro import Libro
from claseCD import CD
import unittest

def menu():
    GestorLista = Lista()
    GestorLista.cargarArchivo()
    op = int(input('''
        -------> MENU DE OPCIONES <-------
    [1] Agregar publicacion
    [2] Mostrar tipo de publicacion
    [3] Mostrar cantidad de publicaciones de cadad tipo
    [4] Mostrar todas las publicaciones
    [5] Salir
    --> '''))
    while op != 5:
        if op == 1:
            tipo = int(input('''
    Seleccione el tipo de publicacion que desea agregar
    [1] Tipo Libro impreso
    [2] Tipo Audio libro
    --> '''))
            while tipo != 1 and 2:
                tipo = int(input('''
    Seleccione el tipo de publicacion que desea agregar
    [1] Tipo Libro impreso
    [2] Tipo Audio libro
    --> '''))

            if tipo == 1:
                titulo = input('Ingrese el titulo: ')
                categoria = input('Ingrese la categoria: ')
                precio_base = float('Ingrese el precio base: ')
                nom_autor = input('Ingrese nombre del autor: ')
                fecha_edi = input('Ingrese fecha de edicion: ')
                cant_pag = int(input('Ingrese la cantidad de paginas: '))
                nuevoLibro = Libro(titulo, categoria, precio_base, nom_autor, fecha_edi, cant_pag)
                GestorLista.agregar_Al_Final(nuevoLibro)

            else:
                titulo = input('Ingrese el titulo: ')
                categoria = input('Ingrese la categoria: ')
                precio_base = float('Ingrese el precio base: ')
                tiempo_rep = int(input('Ingrese el tiempo de reproduccion: '))
                nom_narr = input('Ingrese el nombre del narrador: ')
                nuevoCD = CD(titulo, categoria, precio_base, tiempo_rep, nom_narr)
                GestorLista.agregar_Al_Final(nuevoCD)
            
        elif op == 2:
            pos = int(input('Ingrese una posicion de la lista: '))
            GestorLista.tipoElemento(pos)
            
        elif op == 3:
           GestorLista.cantidadPorElemento()

        elif op == 4:
            GestorLista.mostrarDatos2()
        else:
            print('Ingrese una opcion correcta')
        
        op = int(input('''
        -------> MENU DE OPCIONES <-------
    [1] Agregar publicacion
    [2] Mostrar tipo de publicacion
    [3] Mostrar cantidad de publicaciones de cadad tipo
    [4] Mostrar todas las publicaciones
    [5] Salir
    --> '''))
    print('Salió')

if __name__ == '__main__':
    menu()
