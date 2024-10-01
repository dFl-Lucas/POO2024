from claseNodo import Nodo
from claseLibro import Libro
from claseCD import CD
from clasePublicaciones import Publicaciones
import csv

class Lista:
    __comienzo: Nodo
    __actual = Nodo
    __indice = int
    __tope = int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def cargarArchivo(self):
        archivoL = open('C:\\Users\\Lucas Z\\Documents\\POO 2024\\UNIDAD 3\\Ejercicio 4\\libros.csv', 'r')
        readerL = csv.reader(archivoL, delimiter=';')
        band = True
        for fila in readerL:
            if band == True:
                band = False
            else:
                elemento = Libro(fila[0], fila[1], float(fila[2]), fila[3], fila[4], int(fila[5]))
                self.agregar_Al_Final(elemento)
        print('Carga de Datos satisfactoria')
        archivoL.close()

        archivoCD = open('C:\\Users\\Lucas Z\\Documents\\POO 2024\\UNIDAD 3\\Ejercicio 4\\cd.csv', 'r')
        readerCD = csv.reader(archivoCD, delimiter=';')
        band = True
        for fila in readerCD:
            if band == True:
                band = False
            else:
                elemento = CD(fila[0], fila[1], float(fila[2]), int(fila[3]), fila[4])
                self.agregar_Al_Final(elemento)
        print('Carga de Datos satisfactoria')
        archivoL.close()


    def agregar_Al_Inicio(self, elemento):
        assert isinstance(elemento, Publicaciones), 'Debe ser de clase publicacion'
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def agregar_Al_Final(self, elemento):
        assert isinstance(elemento, Publicaciones), 'Debe ser de clase publicacion'
        nodo = Nodo(elemento)
        if self.__comienzo == None:
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nodo)
            self.__tope += 1

    def listarDatos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def obtenerCabeza(self):
        return self.__comienzo.getDato()
    
    def obtenerCola(self):
        aux = self.__comienzo
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()
        return aux.getDato()
    
    def obtenerTamaño(self):
        return self.__tope
    
    def eliminarCabeza(self):
        aux = self.__comienzo
        if aux == None:
            print('No se puede eliminar porque la lista esta vacia')
        else:
            self.__comienzo = aux.getSiguiente()
            del aux
    
    def eliminarCola(self):
        aux = self.__comienzo
        if aux == None: 
            print('No hay nada que borrar, ya que la lista esta vacia')
        elif aux.getSiguiente() == None:
            self.__comienzo = None
        else:
            while aux.getSiguiente().getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(None)

    def eliminarPorDato(self, elemento_a_buscar):
        assert type(elemento_a_buscar) == str, 'Debe ser una palabra'
        aux = self.__comienzo
        encontrado = False
        if aux.getDato().getTitulo() == elemento_a_buscar:
            encontrado = True
            print('Encontrado:'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente()
            self.__tope -= 1
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if aux.getDato().getTitulo() == elemento_a_buscar:
                    encontrado = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            if encontrado:
                print('Encontrado:'+str(aux.getDato()))
                ant.setSiguiente(aux.getSiguiente())
                self.__tope -= 1
            else:
                print('El elemento a buscar {}, no está en la lista'.format(elemento_a_buscar))

    def buscarDato(self, elemento_a_buscar):
        #assert type(elemento_a_buscar) == al tipo de dato que deberia ser, 'Deberia ser tal de tal tipo o tal cosa'
        aux = self.__comienzo
        encontrado = False
        #aux = aux.getSiguiente() #si el elemento esta al final esta linea puede ir o no, ya que funciona igual con o sin esta linea (pero si busco el primer elemento no lo encuentra asique es mejor no poner esta linea)
        while aux != None and encontrado is False:
            if aux.getDato().getTitulo() == elemento_a_buscar:
                print(f'EL dato es:\n{aux.getDato()}')
                encontrado = True
            else:
                aux = aux.getSiguiente()
        if encontrado is False:
            print(f'El elemento "{elemento_a_buscar}" no se encuentra en la lista')

    def buscarPorIndice(self, indice):
        if indice >= 0 and indice < self.__tope:
            aux = self.__comienzo
            for i in range(indice):
                aux = aux.getSiguiente()
            return aux.getDato()
        else: 
            raise Exception('Indice no valido, esta fuera de rango')
        
    def cambiarDatoPorIndice(self, indice, nuevoElemento):
        if indice >= 0 and indice < self.__tope:
            aux = self.__comienzo
            for i in range(indice):
                aux = aux.getSiguiente()
            aux.setDato(nuevoElemento)
        else: 
            raise Exception('Indice no valido, esta fuera de rango')

    def elimiarPorIndice(self, indice):
        if indice >= 0 and indice < self.__tope:
            if indice == 0:
                aux = self.__comienzo
                self.__comienzo = aux.getSiguiente()
            else:              
                aux = self.__comienzo
                for i in range(indice):
                    ant = aux
                    aux = aux.getSiguiente()
                ant.setSiguiente(ant.getSiguiente().getSiguiente())
        else: 
            raise Exception('Indice no valido, esta fuera de rango')
        
    def listarDatosConIndice(self):
        i = 0
        for publicacion in self:
            print(f'Publicacion: {publicacion.getTitulo()} \tIndice: {i}')
            i += 1

    def mostrarDatos(self):
        for publicacion in self:
            print(f'{publicacion}\n')

    def mostrarDatos2(self):
        for publicacion in self:
            imp = publicacion.impVenta()
            print(f'Titulo: {publicacion.getTitulo()} \tCategoria: {publicacion.getCategoria()} \tImporte de venta: {imp}\n')

    def tipoElemento(self, pos):
        if pos >= 0 and pos < self.__tope:
            aux = self.__comienzo
            for i in range(pos):
                aux = aux.getSiguiente()
            if isinstance(aux.getDato(), Libro):
                print(f'{aux.getDato().getTitulo()} Es del tipo Libro impreso')
            elif isinstance(aux.getDato(), CD):
                print(f'{aux.getDato().getTitulo()} Es del tipo CD')
        else:
            print(f'Indice ingresado invalido\nDebe se un numero entre 0 y {self.__tope - 1}')

    def cantidadPorElemento(self):
        contL = 0
        contCD = 0
        for publicacion in self:
            if isinstance(publicacion, Libro):
                contL += 1
            elif isinstance(publicacion, CD):
                contCD += 1
        print(f'La cantidad del tipo Libro es: {contL}')
        print(f'La cantidad del tipo CD es: {contCD}')

    def cantidadPorElemento2(self):
        contP = 0
        contL = 0
        contCD = 0
        for publicacion in self:
            if isinstance(publicacion, Publicaciones):
                contP += 1
            elif isinstance(publicacion, Libro):
                contL += 1
            elif isinstance(publicacion, CD):
                contCD += 1
        print(f'La cantidad del tipo publicacion es: {contP}')
        print(f'La cantidad del tipo Libro es: {contL}')
        print(f'La cantidad del tipo CD es: {contCD}')

    
'''if __name__ == '__main__':
    MyLista = Lista()
    MyLista.agregar_Al_Inicio(Libro('Hola','Infantil',3000.50,'Lucas Hernan','29/05/2024',15))
    MyLista.agregar_Al_Inicio(Libro('Casa','Adultos',3100.50,'Lucas Z','29/07/2024',10))
    MyLista.agregar_Al_Final(Libro('Avion','Infantil',2500.50,'Hernan A','30/05/2024',18))
    MyLista.agregar_Al_Final(Libro('Perro','Adultos',2000.50,'Kiara','15/02/2024',8))
    MyLista.agregar_Al_Inicio(Libro('POO','xxx',1500.40,'porfesores','30/05/2024',100))
    print('ANTES DE ELIMINAR')
    MyLista.listarDatos()
    print(f'Cantidad de elementos en la lista: {int(MyLista.obtenerTamaño())}')
    print(f'Inicio de la lista:\n{MyLista.obtenerCabeza()}')
    print(f'Cola de la lista:\n{MyLista.obtenerCola()}')
    #MyLista.eliminarPorDato('Avion')
    #MyLista.eliminarCabeza()
    #MyLista.eliminarCola()
    #print('DESPUES DE ELIMINAR')
    #MyLista.listarDatos()
    #for dato in MyLista:
     #print(f'Datos de la lista:\n{dato}')
    #MyLista.buscarDato('Perro')
    #print(f'dato:\n{MyLista.buscarPorIndice(2)}')
    #MyLista.cambiarDatoPorIndice(2,Libro('La casa Rosada','Adultos', 2700.20,'Pedro Juarez','16/08/2019',45))
    #print(f'dato:\n{MyLista.buscarPorIndice(2)}')
    print('antes')
    MyLista.listarDatos()
    MyLista.elimiarPorIndice()
    print('despues')
    MyLista.listarDatos()
    MyLista.listarDatosPorIndice()
    MyLista.mostrarDatos()
    #MyLista.tipoElemento(2)
    #MyLista.cantidadPorElemento()'''