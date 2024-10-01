from ventanaInicio import VentanaInicio
from claseGestorJuego import GestorJuego
from claseGestorJugador import GestorJugador
from ObjectEncoder import ObjectEncoder

if __name__ == '__main__':
    inicio = VentanaInicio() #inicia la ventana inicial y pido el nombre del jugador y se cierra
    nombre = inicio.getNombre() #traigo el nombre que se ingreso
    gestor_jugador = GestorJugador()
    jsonF = ObjectEncoder("C:\\Users\\Lucas Z\\Documents\\POO 2024\\UNIDAD 4\\Simon-Game_byLZ\\pysimonpuntajes.json")
    diccionario = jsonF.leerJSONArchivo()
    gestor_jugador = jsonF.decodificar(diccionario)
    gestor_juego = GestorJuego(nombre, jsonF, gestor_jugador)
    gestor_juego.ejecutar()