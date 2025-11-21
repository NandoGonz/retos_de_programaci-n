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

# Agregando Frame (marco) a la interfaz
# Primer frame
frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="red", bd=5)
frame1.pack()

frame2 = tk.Frame(frame1)  # Creando un Frame dentro de otro
frame2.configure(width=100, height=100, bg="black", bd=5)
frame2.pack()

# Creamos un boton, este pertenece a las clase objetos de tkinter
boton = tk.Button(frame1, text="mí primer boton")
boton.pack()  # para activar el boton debemos usar el método pack()
# Mostrar ventana en bucle siempre al final
ventana.mainloop()
