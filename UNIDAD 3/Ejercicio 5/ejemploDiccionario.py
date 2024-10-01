class Alumno:
    __registro: int
    __nombre: str
    __apellido: str
    __carrera: str
    def __init__(self, registro, nombre, apellido, carrera):
        self.__registro=registro
        self.__nombre=nombre
        self.__apellido=apellido
        self.__carrera=carrera
    def __str__(self):
        cadena='Registro: {}, Carrera: {}\n'.format(self.__registro, self.__carrera)
        cadena+='Apellido: {}, Nombre: {}\n'.format(self.__apellido, self.__nombre)
        return cadena
    
if __name__=='__main__':
    diccionario = dict({'registro':12345, 'nombre':'Carla',
                'apellido':'Ibaceta','carrera':'LCC'})
    unAlumno= Alumno(**diccionario)
    print(unAlumno)