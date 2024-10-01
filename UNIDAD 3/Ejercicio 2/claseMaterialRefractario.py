class MaterialRefractario:
    __material = int
    __caracteristicas = str
    __cantUtilizada = float
    __costoAdicional = float

    def __init__(self, mat, carac, cantU, costA):
        self.__material = mat
        self.__caracteristicas = carac
        self.__cantUtilizada = cantU
        self.__costoAdicional = costA

    def getMaterial(self):
        return self.__material
    
    def getCarac(self):
        return self.__caracteristicas
    
    def getCantUti(self):
        return self.__cantUtilizada
    
    def getCostAd(self): 
        return self.__costoAdicional
    
    def __str__(self):
        return f'''
    Material: {self.__material}
    Caracteristica: {self.__caracteristicas}
    Cantida utilizada de material: {self.__cantUtilizada}
    Costo adicional: {self.__costoAdicional}
'''