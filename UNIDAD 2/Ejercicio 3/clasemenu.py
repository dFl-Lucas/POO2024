from claseFacturacion import FacturacionFarmacia
class Menu:
    __swicher = None

    def __init__(self):
        self.__swicher = { '1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.opcion3,
                           '4':self.opcion4,
                           '5':self.opcion5,
                           '6':self.salir
                        }
        
    def opcion(self, op, imp, sucu , matriz):
        func = self.__swicher.get(op, lambda: print('Opcion incorrecta'))
        func(op, imp,sucu, matriz)

    def opcion1(self, op, imp, matriz):
        if op == 1:
            matriz += imp

    def opcion2(self, op, suc, mat):
        if op == 2:
            total = 0
            for j in range(7):
                total += mat[suc-1][j]
            print('El total facturado en la semana por la sucursal numero {} es: {}'.format(suc, total))

    def opcion3(self, op, dia, mat):
        if op == 3:
            max = 0
            for i in range(5):
                if mat[i][dia-1]:
                    max = mat[i][dia-1]
                    aux = i
            print('La sucursal que mas facturo el dia {} es las numero: '.format(dia, i+1))

    def opcion4(self, op, mat):
        if op == 4:
            sum = 0
            min = 9999999999999999999999999999999999999999
            for i in range(5):
                for j in range(7):
                    sum += mat[i][j]
                if mat[i][j] < min:
                    min = mat[i][j]
                    aux = i
                sum = 0
            print('La sucursal que menos facturo en la semana es la sucursal numero: {}'.format(aux +1))
            
    def opcion5(self, op, mat):
        if op == 5:
            total = 0
            for i in range(5):
                for j in range(7):
                    total += mat[i][j]
            print('El total facturado en la semana por todas las sucursales es: {}'.format(total))

    def salir(self):
        print('Salió efectivamente')