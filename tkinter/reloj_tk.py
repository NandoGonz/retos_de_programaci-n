"""importamos la libreria time"""

import time

import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo reloj")

etiqueta = tk.Label(ventana, text="hola, soy un reloj")
etiqueta.pack()


def actualizar_hora():
    etiqueta.config(text=time.strftime("%H: %M: %S"))
    ventana.after(
        1000, actualizar_hora
    )  # con el método after()podemos actulizar la hora cada cierto tiempoo


actualizar_hora()
ventana.mainloop()
