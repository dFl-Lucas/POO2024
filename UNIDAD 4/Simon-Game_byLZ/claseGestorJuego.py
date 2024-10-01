from claseJugador import Jugador
from VentanaJuego import JuegoPrincipal
from claseGestorJugador import GestorJugador

class GestorJuego:
    __nombre = str
    __puntos = int
    __juego = object
    __gestor_J = object

    def __init__(self, nom, encoder, gest):
        self.__nombre = str(nom)
        self.__puntos = 0
        self.__juego = JuegoPrincipal(self)
        self.__gestor_J = gest
        self.__encoder = encoder
   
    def ejecutar(self):
        self.__juego.mainloop()

    def setPuntos(self, puntos):
        self.__puntos = int(puntos)

    def getGestor(self):
        return self.__gestor_J

    def getNombre(self):
        return self.__nombre
    
    def getPuntos(self):
        return self.__puntos

    def cargarJugador(self):
        xjugador = Jugador(Jugador=self.getNombre(), Fecha=None, Hora=None, Puntaje=self.getPuntos()) #crea un nuevo jugador con el nombre y los puntos obtenidos
        self.__gestor_J.añadir(elemento=xjugador) # añade a lista de jugadores el nuevo jugador
        diccionario = self.__gestor_J.toJson() #crea un diccionario con la lista de jugadores
        self.__encoder.guardarJSONArchivo(diccionario) # y lo guarda en un archivo json