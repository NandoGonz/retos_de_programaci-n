"""importamos la libreria de tkinter"""

import tkinter as tk


# Crear la ventana
ventana = tk.Tk()

# Título de la ventana
ventana.title("Mi primera frame con Tkinter")

# Tamaño de la ventana
ventana.geometry("400x300")


# Modificando el color de fondo
ventana.configure(bg="dodger blue")

labelframe = tk.LabelFrame(
    ventana, text="Grupo de widgets", bg="yellow", padx=10, pady=10
)
labelframe.configure(width=300, height=200)
labelframe.pack()

ventana.mainloop()
