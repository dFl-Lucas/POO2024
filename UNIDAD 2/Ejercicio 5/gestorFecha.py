import csv
from claseFecha import Fecha
class GestorFecha:
    __listaF = list

    def __init__(self):
        self.__listaF = []

    def cargaF(self): #cargamos los datos desde el archivo
        archivo = open("C:\\Users\\Lucas Z\\Documents\\Python\\UNIDAD 2\\Ejercicio 5\\fechasFutbol.csv", "r")
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unaFecha = Fecha(fila[0], int(fila[1]), int(fila[2]), int(fila[3]), int(fila[4]))
                self.__listaF.append(unaFecha)
        print('"Carga de datos satisfactoria"')
        archivo.close()
    
    def mostrar(self): #mostramos todos los datos del objeto equipo
        for i in range(len(self.__listaF)):
            print('{}'.format(self.__listaF[i]))

    def puntos(self, golesL, golesV): #Funcion para decirme cuantos puntos suma de acuerdo a los goles del local y visitante
        p = 0
        if golesL > golesV:
            p = 3
        elif golesL < golesV:
            p = 0
        else:
            p = 1
        return p

    def listarE(self, id): #Listado de las fechas disputadas por los equipos
        GolesF = 0
        GolesC = 0
        DifGoles = 0
        Pts = 0
        for i in range(len(self.__listaF)):#recorremos la lista de quipos para buscar el equipo a travez de su id que ingresaron 

            if self.__listaF[i].getIDL() == id:
                fe = self.__listaF[i].getFecha()
                gl = int(self.__listaF[i].getGL())
                gv = int(self.__listaF[i].getGV())
                dg = gl - gv
                pts = self.puntos(gl, gv)
                GolesF += gl
                GolesC += gv
                DifGoles += dg
                Pts += pts
                print('{:^10}    {:^10}           {:^10}               {:^10}           {:^10}'.format(fe, gl, gv, dg, pts))

            elif self.__listaF[i].getIDV() == id:
                xfe = self.__listaF[i].getFecha()
                xgl = int(self.__listaF[i].getGL())
                xgv = int(self.__listaF[i].getGV())
                xdg = xgv - xgl
                xpts = self.puntos(xgv, xgl)
                GolesF += xgv
                GolesC += xgl
                DifGoles += xdg
                Pts += xpts
                print('{:^10}    {:^10}           {:^10}               {:^10}           {:^10}'.format(xfe, xgv, xgl, xdg, xpts))
            
        print('Totales:      {:^10}           {:^10}               {:^10}           {:^10}'.format( GolesF, GolesC, DifGoles, Pts))
 
    def actualizarDatos(self, gestorE): #obtiene los datos de las fechas para poder actualizar los datos de los equipos
        for i in range(len(self.__listaF)):
            IDL =int(self.__listaF[i].getIDL())
            IDV = int(self.__listaF[i].getIDV())
            GL = int(self.__listaF[i].getGL())
            GV = int(self.__listaF[i].getGV())
            gestorE.actualiza(IDL, IDV, GL, GV)