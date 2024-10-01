from claseGestorLadrillo import GestorLadrillo
from claseGestorMaterial import GestorMaterial

def menu():
    G_M = GestorMaterial()
    G_L = GestorLadrillo()
    G_M.cargarDatos()
    G_L.cargarDatos(G_M)

    op = int(input('''
    [1] Mostrar costo y caractersticas de materiales de ladrillo
    [2] Mostrar costo de cada ladrilo
    [3] Mostrar datos de ladrillos
    [4] Salir
    -->'''))
    while op != 4:
        if op == 1:
            id= int(input('Ingrese identificador de ladrillo: '))
            G_L.Opcion1(id)
    
        elif op == 2:
            G_L.Opcion2(G_M)
            
        elif op == 3:
            G_L.Opcion3()
        else:
            print('Ingrese una opcion correcta')
        
        op = int(input('''
    [1] Mostrar costo y caractersticas de materiales de ladrillo
    [2] Mostrar costo de cada ladrilo
    [3] Mostrar datos de ladrillos
    [4] Salir
    -->'''))
    print('Salió')

if __name__ == '__main__':
    menu()
