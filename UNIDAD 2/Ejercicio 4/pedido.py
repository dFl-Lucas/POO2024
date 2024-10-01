class ClasePedido:
    __patAsig: str
    __IdPed: int
    __ComPed: str
    __tEst: int
    __tReal: int
    __precio: float

    def __init__(self, pat, id, comidas, tEstimado, precio, tReal=0):
        self.__patAsig = pat
        self.__IdPed = id
        self.__ComPed = comidas
        self.__tEst = tEstimado
        self.__precio = precio
        self.__tReal = tReal

    def __str__(self):
        return f' Patente asignada: {self.__patAsig}\n Id de pedido: {self.__IdPed}\n Comidas: {self.__ComPed}\n Tiempo estimado: {self.__tEst}\n Tiempo real: {self.__tReal}\n Precio: {self.__precio}'
    
    def modificaTiempo(self, tiempo):
        self.__tReal = tiempo

    def __lt__(self, otro):
        return self.__patAsig < otro.getPat()

    def getPat(self):
        return self.__patAsig
    
    def getId(self):
        return self.__IdPed
    
    def getEst(self):
        return self.__tEst
    
    def getReal(self):
        return self.__tReal
    
    def getPrecio(self):
        return self.__precio