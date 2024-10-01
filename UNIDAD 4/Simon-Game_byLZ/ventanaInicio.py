import tkinter as tk
from tkinter import *
from tkinter import ttk, font

class VentanaInicio:
    __ventana = None
    __jugador = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('PySimon-Game')
        self.__ventana.iconbitmap('C:\\Users\\Lucas Z\\Documents\\POO 2024\\UNIDAD 4\\Simon-Game_byLZ\\juego.ico')
        self.__ventana.resizable(False, False)
        self.__ventana.geometry('258x127+530+340')

        fuente = font.Font(weight='bold' , name='Lexend', size=12)
        marco = ttk.Frame(self.__ventana, borderwidth=5, relief='raised', padding=(5,5))
        marco.grid(row=0, column=0)

        marco.configure(style="Custom.TFrame")
        estilo = ttk.Style()
        estilo.configure("Custom.TFrame", background="gray80")

        etiqueta1 = ttk.Label(marco, text='Ingrese su nombre', font=fuente, padding=(5,5), background='gray80')
        etiqueta1.grid(row=0, column=0, columnspan=2)

        NomJugador = ttk.Label(marco, text='Jugador:', font=fuente, padding=(5,5), background='gray80')
        NomJugador.grid(row=1, column=0)

        self.__jugador = StringVar()
        self.__jugador.set('')

        entrada1 = tk.Entry(marco, textvariable=self.__jugador, width=25, bg='gray65')
        entrada1.grid(row=1, column=1)

        boton = tk.Button(marco, text='Aceptar', command=self.cerrar, font=fuente, padx=5, pady=5, background='gray78')
        boton.grid(row=2, column=0, columnspan=2)
        self.__ventana.mainloop()
    
    def getNombre(self):
        return self.__jugador.get()
    
    def cerrar(self):
        self.__ventana.destroy()