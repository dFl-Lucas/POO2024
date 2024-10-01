from claseDepartamento import Departamento
class Edificio:
    __id = int
    __nombre = str
    __direccion = str
    __nomEmpresa = str
    __cantPiso = int
    __cantDep = int
    __Departamento = list

    def __init__(self, id, nom, dir, nomE, canP, canD):
        self.__id = id
        self.__nombre = nom
        self.__direccion = dir
        self.__nomEmpresa = nomE
        self.__cantPiso = canP
        self.__cantDep = canD
        self.__Departamento = []
    
    def getNom(self):
        return self.__nombre

    def getID(self):
        return self.__id

    def agregarDepartamento(self, xid, nya, np, nd, ch, cb, sc):
        unDepto = Departamento(xid, nya, np, nd, ch, cb, sc)
        self.__Departamento.append(unDepto)

    '''def __del__(self, ):
        print('Borrando departamento...')
        del self.__Departamento'''
    
    def mostrarPropietario(self): #muestra los datos del propietario que se ingreso
        for i in range(len(self.__Departamento)):
            print('Departamento: {}     Propietario: {}'.format(self.__Departamento[i].getID() ,self.__Departamento[i].getAyN()))

    def sumaSuperficie(self): #suma todas las superficies de los departamentos
        sumaT = 0
        for i in range(len(self.__Departamento)):
            sumaT += self.__Departamento[i].getSuperCub()
        return sumaT

    def buscaProp(self, propietario): #busca el propietario que se ingreso
        i = 0
        band = False
        while i<len(self.__Departamento) and band is False: # compara el nombre que se ingreso con todos los nombre de propietarios de los departamentos
            if self.__Departamento[i].getAyN().upper().replace(' ','') == propietario:
                band = i #retornar el indice nos srve para saber que departamento es el del propietario que se ingreso
            i += 1
        return band #retorna el indice si lo encontro 
    
    def supDep(self, ind): #obtiene la superficie del departamento que indica ese indice
        supD = self.__Departamento[ind].getSuperCub()
        return supD
    
    def buscaPiso(self, xnum): 
        cont = 0
        for i in range(len(self.__Departamento)): # itera en todos los departamentos buscando aquellos que tangan 3 habitaciones y mas de 1 baño
            if self.__Departamento[i].getNumP() == xnum:
                if self.__Departamento[i].getCantH() == 3 and self.__Departamento[i].getCantB() > 1:
                    cont += 1
        return cont
        

    def mostrar2(self): #muestra los datos de cada edificio con sus respectivos datos de los departamentos
        print('Id: {}\n Nombre: {}\n Direccion: {}\n Nombre de empresa: {}\n Cantidad de pisos: {}\n Cantidad de departamentos: {}\n'.format(self.__id, self.__nombre, self.__direccion, self.__nomEmpresa, self.__cantPiso, self.__cantDep))
        for i in range(len(self.__Departamento)): #se realiza una iteracion en departamentos para asi poder mostrarlos ya que es una lista 
            print('{}'.format(self.__Departamento[i]))