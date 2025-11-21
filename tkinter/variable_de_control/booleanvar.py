import tkinter as tk

ventana = tk.Tk()

booleano = tk.BooleanVar(value=True)

# print(booleano.get())

casilla = tk.Checkbutton(ventana, text="Aceptar", variable=booleano)
casilla.pack()


# Actualizando valor boolenao
def actualizar(*args):
    print(booleano.get())


booleano.trace("w", actualizar)


ventana.mainloop()
