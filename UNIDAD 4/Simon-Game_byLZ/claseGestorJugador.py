from claseJugador import Jugador

class GestorJugador:
    __listaJugador = list

    def __init__(self):
        self.__listaJugador = []
    
    def añadir(self, elemento):
        self.__listaJugador.append(elemento)

    def ordenar(self):
        self.__listaJugador.sort(reverse=True)

    def getLista(self):
        return self.__listaJugador
    
    def cargar(self, d):
        self.__listaJugador = d
    
    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            Jugador=[Jugador.toJSON() for Jugador in self.__listaJugador]
        )
        return d