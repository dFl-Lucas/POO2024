import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
import random

class JuegoPrincipal(tk.Tk):
    #__ventanaJuego = None
    __secuencia_Jugador = None
    __secuencia = None
    __Gestor = object
    __aciertos = int
    __colores = list

    def __init__(self, gestor):
        super().__init__()
        #self.__ventanaJuego = Tk()
        self.__secuencia = []
        self.__secuencia_Jugador = []
        self.__aciertos = 0
        self.__Gestor = gestor
        self.__colores = ['verde','rojo','amarillo','azul']
        self.title('PySimon-Game')
        self.iconbitmap('C:\\Users\\Lucas Z\\Documents\\POO 2024\\UNIDAD 4\\Simon-Game_byLZ\\juego.ico')
        self.resizable(width=False, height=False)
        self.geometry('272x400')
        self.update_idletasks()
        self.geometry('+555+240')
        self.update_idletasks()
        self.ventana()

    def ventana(self):
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu)
        opciones = tk.Menu(barra_menu)
        barra_menu.add_cascade(label='Opciones', menu=opciones)
        opciones.add_command(label='Ver Puntajes', command=self.ver_puntajes)
        opciones.add_separator()
        opciones.add_command(label='Salir', command=self.destroy)
      
        self.etiqueta = ttk.Label(self, text=f'{self.__Gestor.getNombre()}:                                          0', font=('Lexend', 12))
        self.etiqueta.grid(row=0, column=0, padx=3, pady=3, sticky='w')

        self.canvas = tk.Canvas(self, width=268, height=328)
        self.canvas.grid(row=1, column=0)

        self.botonVerde = self.canvas.create_rectangle(5, 5, 125, 155, fill='green4', width=1)
        self.canvas.tag_bind(self.botonVerde, '<Button-1>', lambda event: self.secuencia_jugador('verde'))

        self.botonRojo = self.canvas.create_rectangle(145, 5, 265, 155, fill='red4', width=1)
        self.canvas.tag_bind(self.botonRojo, '<Button-1>', lambda event: self.secuencia_jugador('rojo'))

        self.botonAmarillo = self.canvas.create_rectangle(5, 175, 125, 325, fill='yellow4', width=1)
        self.canvas.tag_bind(self.botonAmarillo, '<Button-1>', lambda event: self.secuencia_jugador('amarillo'))

        self.botonAzul = self.canvas.create_rectangle(145, 175, 265, 325, fill='blue4', width=1)
        self.canvas.tag_bind(self.botonAzul, '<Button-1>', lambda event: self.secuencia_jugador('azul'))

        self.boton = tk.Button(self, text='Comenzar', font=('Lexend', 12), command=self.empezar)
        self.boton.grid(row=2, columnspan=3, padx=3, pady=3)

    def empezar(self): #Aca se inicializa todo ya que se ejecuta solo la primera ronda 
        self.__aciertos = 0
        self.__secuencia = []
        self.__secuencia_Jugador = []
        self.actualizar_pts()
        self.secuencia_juego()

    def secuencia_juego(self): #Al comenzar o luego de cada secuencia correcta se vacia la lista de secuencia del jugador
        self.__secuencia_Jugador = []
        self.secuencia_colores()
        self.after(1000, self.mostrar_secuencia)#espero 1 segundo y inicio el juego

    def secuencia_colores(self):
        self.__secuencia.append(random.choice(self.__colores)) #Elige un color al azar de la lista de colores disponibles y lo agrega a la lista

    def mostrar_secuencia(self):
        i = 0
        for color in self.__secuencia:
            self.after(i * 1000, lambda color=color: self.cambia_color(color)) 
            i +=1

    def cambia_color(self, color): #aca pregunto que color es "color" y segun cual sea es el color que se va cambiar
        if color == 'verde':
            self.canvas.itemconfig(self.botonVerde, fill='lawn green') #cambiamos el color a uno mas brillante
            self.after(400, lambda: self.canvas.itemconfig(self.botonVerde, fill='green4')) #esperamos 4ms y volvemos al color original

        elif color == 'rojo':
            self.canvas.itemconfig(self.botonRojo, fill='red')
            self.after(400, lambda: self.canvas.itemconfig(self.botonRojo, fill='red4'))

        elif color == 'amarillo':
            self.canvas.itemconfig(self.botonAmarillo, fill='yellow')
            self.after(400, lambda: self.canvas.itemconfig(self.botonAmarillo, fill='yellow4'))
                
        elif color == 'azul':
            self.canvas.itemconfig(self.botonAzul, fill='blue')
            self.after(400, lambda: self.canvas.itemconfig(self.botonAzul, fill='blue4'))

    
    def secuencia_jugador(self, color):
        self.__secuencia_Jugador.append(color) #agrego a la lista de sencuencia del jugador el color seleccionado por el jugador
        self.cambia_color(color) #reutilizamos la funcion cambia color para que el usuario distiga que color presiono
        if len(self.__secuencia) == len(self.__secuencia_Jugador): #comparamos el len de las listas de secuencia de jugador y del juego
            if self.__secuencia == self.__secuencia_Jugador: # si son iguales se le suman todos los puntos de cada acierto
                self.__aciertos += len(self.__secuencia_Jugador)
                self.actualizar_pts() # se actualizan los puntos
                self.secuencia_juego()# continuea el juego

            else: #si no son iguales, termina e juego
                self.etiqueta.config(text=f'Juego terminado                Puntaje: {self.__aciertos}')
                self.guardar(self.__aciertos) # se guarda los datos del jugador
    
    def actualizar_pts(self):
        self.etiqueta.config(text=f'{self.__Gestor.getNombre()}:                                        {self.__aciertos}') #actualiza el puntaje 

    def guardar(self, acier):
        self.__Gestor.setPuntos(acier) #guarda los puntos del jugador 
        self.__Gestor.cargarJugador() #cargar el jugador
    
    def ver_puntajes(self):
        tabla_Puntajes = Toplevel()
        #tabla_Puntajes.geometry('380x200')
        tabla_Puntajes.resizable(False,False)
        tabla_Puntajes.title('Galeria de Puntajes')
        tabla_Puntajes.iconbitmap('C:\\Users\\Lucas Z\\Documents\\POO 2024\\UNIDAD 4\\Simon-Game_byLZ\\juego.ico')

        fuente = font.Font(weight='normal', size=12)

        marco = tk.Frame(tabla_Puntajes, padx=5 ,pady=5, relief='raised')
        marco.grid(row=0, column=0, sticky='nswe')

        jugador = tk.Label(marco, text='Jugador', font=fuente)
        jugador.grid(row=0, column=0, padx=3, pady=3)

        fecha = tk.Label(marco, text='Fecha', font=fuente)
        fecha.grid(row=0, column=1, padx=3, pady=3)

        hora = tk.Label(marco, text='Hora', font=fuente)
        hora.grid(row=0, column=2, padx=3, pady=3)

        puntaje = tk.Label(marco, text='Puntaje', font=fuente)
        puntaje.grid(row=0, column=3, padx=3, pady=3)

        listaJugadores = self.__Gestor.getGestor() #traigo del gestorjuego la lsta de jugadores
        listaJugadores.ordenar() #ordeno la lista por puntaje
        listaOrdenada = listaJugadores.getLista() #obtengo la lista ordenada

        for i in range(len(listaOrdenada)):  
            nombre = tk.Label(marco, text=listaOrdenada[i].getNombre(), font=('arial',12))
            nombre.grid(row=i+1, column=0, padx=5, pady=5)

            fecha1 = tk.Label(marco, text=listaOrdenada[i].getFecha(), font=('arial',12))
            fecha1.grid(row=i+1, column=1, padx=5, pady=5)

            hora1 = tk.Label(marco, text=listaOrdenada[i].getHora(), font=('arial',12))
            hora1.grid(row=i+1, column=2, padx=5, pady=5)

            puntos = tk.Label(marco, text=listaOrdenada[i].getPuntaje(), font=('arial',12))
            puntos.grid(row=i+1, column=3, padx=5, pady=5)

        #salir = tk.Button(tabla_Puntajes, text='Salir', command=tabla_Puntajes.destroy, font=('arial',12))
        #salir.grid(row=1, column=0, sticky='nswe')



