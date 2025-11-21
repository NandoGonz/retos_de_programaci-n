import tkinter as tk

ventana = tk.Tk()
entero = tk.IntVar(value=29)

print(entero.get())

"""# Creando radiobutton
opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=entero, value=1)
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=entero, value=2)
opcion2.pack()"""

# usando checkbutton
casilla = tk.Checkbutton(
    ventana, text="Aceptar", variable=entero, onvalue=1, offvalue=0
)
casilla.pack()


# Actulizando el comportameinto de la variable por medio de un callback
def actualizar(*args):
    print(entero.get())


entero.trace("w", actualizar)
ventana.mainloop()
