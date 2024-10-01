class Fecha:
    __FechaP = str
    __idEL = int
    __idEV = int
    __G_EL = int
    __G_EV = int

    def __init__(self, fp, idel, idev, gl, gv):
        self.__FechaP = fp
        self.__idEL = idel
        self.__idEV = idev
        self.__G_EL = gl
        self.__G_EV = gv

    def getFecha(self):
        return self.__FechaP
    
    def getIDL(self):
        return self.__idEL
    
    def getIDV(self):
        return self.__idEV
    
    def getGL(self):
        return self.__G_EL
    
    def getGV(self):
        return self.__G_EV
    
    def __str__(self):
        return ' Fecha de partido:{}\n ID del equipo local:{}\n ID del equipo visitante:{}\n Goles del equipo local:{}\n Goles del quipo visitante:{}\n'.format(self.__FechaP, self.__idEL, self.__idEV, self.__G_EL, self.__G_EV)