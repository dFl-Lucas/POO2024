def menu():
    G1 = GestorX1()
    G2 = GestorX2()
    G1.carga1()
    G2.carga2()
    op = int(input('''
        -------> MENU DE OPCIONES <-------
    [1] Opcion 1
    [2] Opcion 2
    [3] Opcion 3
    [4] Salir
    --> '''))
    while op != 4:
        if op == 1:
            d= int(input('Ingrese: '))
            GC.Opcion1(dni, g1)
                
        elif op == 2:
            x = int(input('Ingrese:'))
            GC.Opcion2(xdni, G2)
            
        elif op == 3:
            Gm.ordenar()
        else:
            print('Ingrese una opcion correcta')
        
        op = int(input('''
        -------> MENU DE OPCIONES <-------
    [1] Opcion 1
    [2] Opcion 2
    [3] Opcion 3
    [4] Salir
    --> '''))
    print('Salió')