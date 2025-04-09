import tkinter as tk
ventana = tk.Tk()
ventana.title("conversion")
ventana.geometry("400x500")
boton = tk.Button (ventana,text= "Binario")
boton.pack()

import tkinter as tk
from tkinter import messagebox
resultado =""

def toBin():
    try:
        numero = int (txt.get())
        while numero > 0:
            resultado =str(numero % 2) + resultado
            numero //=2
            Ibl_resultado.config(text=f"Resultado en Binario: {resultado}")
    except ValueError:
        messagebox.shower("Error","Por favor ingrese un numero decimal valido")
ventana.mainloop()