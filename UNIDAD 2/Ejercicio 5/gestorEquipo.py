import csv
from claseEquipo import Equipo
class GestorEquipo:
    __listaE = []

    def __init__(self):
        self.__listaE = []
    
    def cargaE(self):
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 2\\Ejercicio 5\\equipos2024.csv", "r")
        reader = csv.reader(archivo, delimiter= ',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else: 
                id = int(fila[0])
                nom = fila[1]
                gf = int(fila[2])
                gc = int(fila[3])
                dg = int(fila[4])
                pts = int(fila[5])
                unEquipo = Equipo(id, nom, gf, gc, dg, pts)
                self.__listaE.append(unEquipo)
        print('"Carga de datos satisfactoria"')
        archivo.close()
    
    def mostrar(self): #mostramos todos los datos del objeto
        for i in range(len(self.__listaE)):
            print('{}'.format(self.__listaE[i]))
    
    def buscarEquipo(self, nom): #buscamos el quipo a traves de su nombre y si se encuentra retornamos su id
        i = 0
        band = False
        while i < len(self.__listaE) and band == False:
            if (self.__listaE[i].getNom().upper() == nom):
                band = True
            else:
                i += 1
        if band == True:
            band = self.__listaE[i].getID()
        return band
    
    def Opcion3(self, nom, gestorF):#mostramos los datos de las fechas disputadas por los equipos en formato de lista
        dato = self.buscarEquipo(nom)
        if dato != False: #si el nombre que ingresaron del equipo no existe no se ejecuta esto
            print('Equipo: {}'.format(nom))
            print('{:^10}      {:^10}    {:^10}      {:^10}    {:^10}'.format('Fecha', 'Goles a favor', 'Goles en contra', 'Diferencia de goles', 'Puntos'))
            gestorF.listarE(dato)
        else:
            print('Equipo no encontrado')
    
    def puntos(self, golesL, golesV): #Funcion para decirme cuantos puntos suma de acuerdo a los goles del local y visitante
        p = 0
        if golesL > golesV:
            p = 3
        elif golesL < golesV:
            p = 0
        else:
            p = 1
        return p

    def actualiza(self, idl, idv, gl, gv): #actualiza los datos de los equipos con los datos de las fechas que obtuvimos a travez de el gestor de fechas
        for i in range(len(self.__listaE)): #recorremos la lista de quipos y preguntamos si el equipo tiene la misma id que la del equipo local o visitante que nos mando el gestor de fechas
            if self.__listaE[i].getID() == idl: #si es igual a la del equipo local hace esto
                p = self.puntos(gl, gv)
                self.__listaE[i].actualizaFecha(gl, gv, p)
            elif self.__listaE[i].getID() == idv: #si es igual a la del equipo visitante hace esto otro
                p = self.puntos(gv, gl)
                self.__listaE[i].actualizaFecha(gv, gl, p)

    def ordenarTabla(self): #Ordena la lista de quipos en forma descendente, es decir, de mayor a menor
        self.__listaE.sort(reverse=True)

    def tablaDePosiciones(self): #muestra la lista ordenada enteriormente en formato de tabla de posiciones solo con los datos necesarios para ello
        print('{:^10} {:^10} {:^10} {:^10} {:^10}'.format('EQUIPO', 'GF', 'GC', 'DG', 'PTS'))
        for i in range(len(self.__listaE)):
            print('{:^10} {:^10} {:^10} {:^10} {:^10}'.format(self.__listaE[i].getNom(), self.__listaE[i].getGF(), self.__listaE[i].getGC(), self.__listaE[i].getDG(), self.__listaE[i].getP()))

    def escribirArchivo(self): #escribe en un archivo la tabla de posiciones ordenada
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 2\\Ejercicio 5\\TablaPosiciones.csv", "w", newline='')
        writer = csv.writer(archivo, delimiter=',')
        writer.writerow(['Equipo','Goles a Favor','Goles en contra','Diferencia de goles','Puntos'])
        for i in range(len(self.__listaE)):
            NOM = self.__listaE[i].getNom()
            GF = int(self.__listaE[i].getGF())
            GC = int(self.__listaE[i].getGC())
            DG = int(self.__listaE[i].getDG())
            PUNTOS = int(self.__listaE[i].getP())
            writer.writerow([f'{NOM}',f'{GF}',f'{GC}',f'{DG}',f'{PUNTOS}'])
        print('Archivo cargado correctamente')
        archivo.close()