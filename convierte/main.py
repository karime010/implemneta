import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("conversion")
ventana.geometry("400x500")
boton = tk.Button (ventana,text= "Binario",command=toBin)
boton.pack()

resultado =""

txt=tk.Entry(ventana)
txt.pack()

Ibl_resultado=tk.Label(ventana)
Ibl_resultado.pack()

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