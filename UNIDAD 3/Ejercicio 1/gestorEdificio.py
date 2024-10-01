import csv
from claseEdificio import Edificio

class GestorEdificio:
    __listaE = list

    def __init__(self):
        self.__listaE = []

    def carga(self):
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 3\\Ejercicio 1\\EdificioNorte.csv",'r') #cargamos los datos del archivo en sus clases correspondientes
        reader = csv.reader(archivo, delimiter=';')
        unEdi = None
        for fila in reader:# realizamos la carga de edificios y departamantos a la vez ya que se encuentran en el mismo archivo
            if len(fila) == 6: #como sabemos que la longitud de los datos del edificio es igual a 6 la utilizamos para realizar la carga 
                unEdi = Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.__listaE.append(unEdi)
            else: #si la longitud es distinta de 6 sabemos que se trata de un departamento 
                xid = int(fila[1])
                xayn = fila[2]
                xnp = int(fila[3])
                xnd = int(fila[4])
                ch = int(fila[5])
                cb = int(fila[6])
                sp = float(fila[7])
                unEdi.agregarDepartamento(xid, xayn, xnp, xnd, ch, cb, sp)
        archivo.close()
        print('Carga de datos exitosa')
    
    def mostrar(self): #muestra todos los datos de los edificios y departamentos pero depende de la otra funcion mostrar de edificio paara funcionar correctamente
        for i in range (len(self.__listaE)):
            print('{}'.format(self.__listaE[i].mostrar2()))

    def buscarEdificio(self, edificio): #realiza la busqueda del edificio ingresado, si lo encuentra devuelve el indice
        i = 0
        band = False
        while i<len(self.__listaE) and band is False:
            if self.__listaE[i].getNom().upper().replace(' ','') == edificio: #pasamos a mayuscula y le quitamos los espacios en blanco para que quede igual al que ingresamos y no nos de error
                band = i
            i += 1
        return band

    def Opcion1(self, edi):
        indice = self.buscarEdificio(edi)
        if type(indice) == int: # si el edificio se encontro indice va ser de tipo entero
                print(f'{self.__listaE[indice].getNom()}             Id de Edificio: {self.__listaE[indice].getID()}')
                self.__listaE[indice].mostrarPropietario()
        else:
            print('Edificio no encontrado o nombre incorrecto')

    def Opcion2(self, edi):
        indice = self.buscarEdificio(edi)
        if type(indice) == int:  # si el edificio se encontro indice va ser de tipo entero
            SupTotal = self.__listaE[indice].sumaSuperficie()
            print(f'Edificio: {self.__listaE[indice].getID()}\n Superficie cubierta: {SupTotal}')
        else: 
            print('Edificio no encontrado')

    def BuscaProp(self, prop): #buscamos el propietario que se ingreso
        i = 0
        band = False
        while i<len(self.__listaE) and band is False: #recorremos la lista de de edificios
            if type(self.__listaE[i].buscaProp(prop)) == int: #preguntamos si el resultado de la funcion es tipo entero si lo encontro
                band = i
            i += 1
        return band #retorna el indice del edificio

    def Opcion3(self, prop):
        indice = self.BuscaProp(prop)
        if type(indice) == int: #pregunta si el resultado de la funcion es entero si es asi es porque encontro al propietario ingresado
            pos = int(self.__listaE[indice].buscaProp(prop)) #hacemos uso de la funcion que utilizamos para buscar el propietario ya que esta funcion nos devuelve el indice del departamento del propietario que se ingreso
            supDep = int(self.__listaE[indice].supDep(pos)) # utilizamos el idndice de la funcion anterior para obtener la superfice del departamento
            print('La superficie del departamento es: {}'.format(supDep))
            supT = self.__listaE[indice].sumaSuperficie() #obtenemos la superficie total del edificio para sacar el porcentaje
            porcentajeCubierto = (supDep*100) / supT
            print('El porcentaje cubierto del edificio es: {:.2f}'.format(porcentajeCubierto))
        else:
            print('No se encontro ese propietario')
    
    def Opcion4(self, num):
        res = 0
        for i in range(len(self.__listaE)): #iteramos en todos los edificios porque hay varios edificios que pueden llegar a tener ese numero de piso
            res += self.__listaE[i].buscaPiso(num)
        print('La cantidad de departamentos con 3 habitaciones y mas de un baño es: {}'.format(res))