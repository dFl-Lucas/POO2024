class Equipo:
    __Id = int
    __nombre = str
    __GF = int
    __GC = int
    __DG = int
    __puntos = int

    def __init__(self, id, nom, GF, GC, DG, PTS):
        self.__Id = id
        self.__nombre = nom
        self.__GF = GF
        self.__GC = GC
        self.__DG = DG
        self.__puntos = PTS

    def getID(self):
        return self.__Id
    
    def getNom(self):
        return self.__nombre
    
    def getGF(self):
        return self.__GF
    
    def getGC(self):
        return self.__GC
    
    def getDG(self):
        return self.__DG
    
    def getP(self):
        return self.__puntos
    
    def __str__(self):
        return ' ID de equipo:{}\n Nombre:{}\n Goles a favor:{}\n Goles en contra:{}\n Diferencia de goles:{}\n Puntos:{}\n'.format(self.__Id, self.__nombre, self.__GF, self.__GC, self.__DG, self.__puntos)

    def actualizaFecha(self, gf, gc, p): #Actualiza los datos del equipo con los datos de sus fechas disputadas
        self.__GF += gf
        self.__GC += gc
        self.__puntos += p
        self.__DG += (gf-gc)

    def __gt__(self, otro): #Sobrecargamos el operador de mayor que para ordenar la lista de quipos respecto de los puntos del equipo
        if self.__puntos == otro.getP(): #si los puntos son iguales se fija en la diferencia de goles
            if self.__DG == otro.getDG(): # si la diferncia tambien son iguales se fija en los goles a favor
                return self.__GF > otro.getGF()
            else: 
                return self.__DG > otro.getDG()  #si la diferencia no son iguales hace esto
        else:
            return self.__puntos > otro.getP() #si los puntos son distintos hace esto
    
        