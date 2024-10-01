import datetime

class Jugador:
    __jugador = str
    __fecha = str
    __hora = str
    __puntaje = int

    def __init__(self, **kwards):
        self.__jugador = kwards['Jugador']
        self.__puntaje = int(kwards['Puntaje'])

        DiaDeHoy = datetime.date.today()
        hora = datetime.datetime.today()

        if kwards["Fecha"] == None:
            self.__fecha = str(DiaDeHoy.day)+'/'+str(DiaDeHoy.month)+"/"+str(DiaDeHoy.year)
        else:
            self.__fecha = kwards["Fecha"]
        
        if kwards["Hora"] == None:
            self.__hora = str(hora.hour)+':'+str(hora.minute)+':'+str(hora.second)
        else:
            self.__hora = kwards["Hora"]
    
    def getNombre(self):
        return self.__jugador

    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getPuntaje(self):
        return self.__puntaje
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                Jugador = self.getNombre(),
                Fecha = self.getFecha(),
                Hora = self.getHora(),
                Puntaje = self.getPuntaje()
            )
        )
        return d

    def __gt__(self, otro):
        return self.__puntaje > otro.getPuntaje()