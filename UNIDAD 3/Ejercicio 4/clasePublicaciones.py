class Publicaciones:
    __titulo = str
    __categoria = str
    __precioBase = float

    def __init__(self, tit, cat, pre):
        self.__titulo = tit
        self.__categoria = cat
        self.__precioBase = pre
    
    def __str__(self):
        return f'Titulo: {self.__titulo}\tCategoria: {self.__categoria}\tPrecio base: {self.__precioBase}'

    def impVenta(self, dato=0):
        return self.__precioBase + dato
    
    def resto(self, dato):
        return dato
    
    def getPB(self):
        return self.__precioBase
    
    def getTitulo(self):
        return self.__titulo
     
    def getCategoria(self):
        return self.__categoria