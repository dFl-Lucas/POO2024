def menu():
        menu = int(input('*** MENU DE OPCIONES *** \n 1: Cargar factura \n 2: Calcular total de facturacion de sucursal \n 3: Calcular sucursal que mas facturo en un dia \n 4: Calcular sucursal con menos facturacion de la semana \n 5: Calcular total facturado de todas las sucursales en la semana \n 6: Salir \n'))
        while menu != 6:
             if menu == 1:
                  dia = int(input('Ingrese dia de la semana: '))
                  sucu = int(input('Ingrese numero de sucursal: '))
                  importe = float(input('Ingrese importe de factura: '))
                  matriz[sucu -1][dia -1] += importe

             elif menu == 2:
                  sucu2 = int(input('Ingrese numero de sucursal: '))
                  totalSucu2 = 0
                  for j in range(7):
                       totalSucu2 += matriz[sucu2-1][j]
                  print('El total de facturacion de la sucursal {} es {}'.format(sucu2, totalSucu2))

             elif menu == 3:
                  dia2 = int(input('Ingrese dia de la semana: '))
                  mas = 0
                  for i in range(5):
                       if matriz[i][dia2-1] > mas:
                            mas = matriz[i][dia2-1]
                            aux = i
                  print('La sucursal que mas facturo el dia {} es la sucursal numero: {}'.format(dia2, i +1))

             elif menu == 4:
                  total1 = 0
                  total2 = 99999999999999999999999999999999999
                  for r in range(5):
                       for k in range(7):
                            total1 += matriz[r][k]
                       if total2 > total1:
                            total2 = total1
                            sucu3 = r
                       total1 = 0
                  print('La sucursal con menos facturacion de la semana es {}'.format(sucu3 + 1))
                            
             elif menu == 5:
                  totalF = 0
                  totalF2 = 0
                  for r in range(5):
                       for k in range(7):
                            totalF += matriz[r][k]
                       totalF2 += totalF
                       totalF = 0
                  print('El total facturado por todas las sucursales en la semana es: {}'.format(totalF2))

             else:
                  print('Ingrese una opcion correcta')

             menu = int(input('*** MENU DE OPCIONES *** \n 1: Cargar factura \n 2: Calcular total de facturacion de sucursal \n 3: Calcular sucursal que mas facturo en un dia \n 4: Calcular sucursal con menos facturacion de la semana \n 5: Calcular total facturado de todas las sucursales en la semana \n 6: Salir \n'))       


if __name__ == '__main__':
    valor = 0
    (M, N) = (5, 7)
    matriz = [[valor]*N for _ in range(M)]
    for i in range(M):
        print(matriz[i])
    
    '''for j in matriz: #FORMA DE MOSTRAR LA MATRIZ SIN CORCHETES NI COMAS
        for element in j:
            print(element, end=" ")
        print()'''
    
    menu()
    for i in range(M):
        print(matriz[i])