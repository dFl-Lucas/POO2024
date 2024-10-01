class Ladrillo:
    __alto = 7
    __largo = 25
    __ancho = 15
    __cantidad = int
    __identificador = int
    __kgMatPriUti = float
    __costo = float
    __materialRefractario = list

    def __init__(self, cant, id, kgU, costo):
        self.__cantidad = cant
        self.__identificador = id
        self.__kgMatPriUti = kgU
        self.__costo = costo
        self.__materialRefractario = []

    def agregarElemento(self, mat):
        if (mat in self.__materialRefractario) is False:
            self.__materialRefractario.append(mat)
            print(f'Se agrego el material correctamente')
        else:
            print(f'No se pudo agregar el material porque ya lo tiene')

    def listarMaterial(self):
        print(f'Costo: {self.__costo}')
        for i in range(len(self.__materialRefractario)):
            print(f'Caracteristica del material: {self.__materialRefractario[i].getCarac()}')

    def getMateriales(self):
        materiales = ''
        for i in range(len(self.__materialRefractario)):
            materiales += str(self.__materialRefractario[i].getMaterial()) + ', '
        return materiales
    
    def costoAs(self):
        costo = self.__costo
        for material in self.__materialRefractario:
            costo += material.getCostAd()
        return costo

    def getAlto(self):
        return self.__alto
    
    def getLargo(self):
        return self.__largo
    
    def getAncho(self):
        return self.__ancho
    
    def getCant(self): 
        return self.__cantidad
    
    def getID(self):
        return self.__identificador
    
    def getKgUt(self):
        return self.__kgMatPriUti
    
    def getCosto(self):
        return self.__costo

    def materiales(self):
        for i in range(len(self.__materialRefractario)):
            print('{}'.format(self.__materialRefractario[i]))

    def __str__(self):
        return f'''
    Alto: {self.__alto}
    Largo: {self.__largo}
    Ancho: {self.__ancho}
    Cantidad: {self.__cantidad}
    Identificador: {self.__identificador}
    Kg de material utilizado: {self.__kgMatPriUti}
    Costo: {self.__costo}
    {self.materiales}
'''