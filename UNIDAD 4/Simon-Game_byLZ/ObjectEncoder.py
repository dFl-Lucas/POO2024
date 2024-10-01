import json
from pathlib import Path
from claseGestorJugador import GestorJugador
from claseJugador import Jugador

class ObjectEncoder:
    __RutaArchivo=object

    def __init__(self, ruta):
        self.__RutaArchivo = ruta

    def decodificar(self,d):
        if "__class__" not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name == 'GestorJugador':
                jugador=d['Jugador']
                gestorJugador=class_()
                for i in range(len(jugador)):
                    djugador=jugador[i]
                    class_name=djugador.pop('__class__')
                    class_=eval(class_name)
                    atributos=djugador['__atributos__']
                    unjugador=class_(**atributos)
                    gestorJugador.añadir(unjugador)
        return gestorJugador
    
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__RutaArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self):
        with Path(self.__RutaArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
                