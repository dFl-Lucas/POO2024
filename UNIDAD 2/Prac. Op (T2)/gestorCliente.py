import csv
from claseCliente import Cliente

class GestorCliente:
    __listaCli = list

    def __init__(self):
        self.__listaCli = []

    def agregarCli(self, unCliente):
        self.__listaCli.append(unCliente)
    
    def cargaCli(self):
        archivo = open('ClientesFarmaCiudad.csv','r')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band == True:
                band = False
            else:
                unCliente = Cliente(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4]))
                self.agregarCli(unCliente)
        print('Carga de Clientes satisfactoria')

        archivo.close()

    def buscarDni(self, xdni):
        i = 0
        band= False
        indice= -1
        while i < len(self.__listaCli) and band == False:
            if self.__listaCli[i].getDNI() == xdni:
                indice = i
                band = True
            i += 1
        return indice
    
    def Opcion1(self, dni, gestorMov):
        pos = self.buscarDni(dni)
        if pos != -1:
            cliente = self.__listaCli[pos].getNom() +" "+ self.__listaCli[pos].getApe()
            NumC = self.__listaCli[pos].getNROC()
            SalAnt= self.__listaCli[pos].getSaldo()
            print(f'''
Cliente: {cliente}                        Numero de cuenta: {NumC}
Saldo anterior: {SalAnt}
Movimientos
Fecha          Descripcion                  Importe         Tipo de Movimiento
            ''')
            for i in range(len(gestorMov._GestorMovimiento__ArregloMovimientos)):
                if gestorMov._GestorMovimiento__ArregloMovimientos[i].getNroC() == NumC:
                    fecha = gestorMov._GestorMovimiento__ArregloMovimientos[i].getFecha()
                    desc = gestorMov._GestorMovimiento__ArregloMovimientos[i].getDesc()
                    tipoMov = gestorMov._GestorMovimiento__ArregloMovimientos[i].getTM()
                    imp = float(gestorMov._GestorMovimiento__ArregloMovimientos[i].getIMP())

                    if tipoMov == 'C':
                        SalAnt += imp
                    if tipoMov == 'P':
                        SalAnt -= imp
                    print('{:15} {:20} {:15}                {:10}'.format(fecha, desc, imp, tipoMov))
        
            print(f'Saldo actual: {SalAnt}')
            self.__listaCli[pos].actualizaSaldo(SalAnt)
        else:
            print('DNI NO ENCONTRADO')
   
    def Opcion2(self, xdni, gestorM):
        pos = self.buscarDni(xdni)
        if pos != -1: 
            numC = int(self.__listaCli[pos].getNROC())
            cant = gestorM.contarMov(numC)
            if  cant == False:
                print('No tuvo movimientos en el mes de Abril')
                print(f'Apellido: {self.__listaCli[pos].getNom()} Nombre: {self.__listaCli[pos].getApe()}')
            else:
                print('Si tuvo movimientos en el mes de abril')
        else:
            print('DNI NO ENCONTRADO')
    
    def mostrar(self):
        for i in range(len(self.__listaCli)):
            print('{}'.format(self.__listaCli[i]))