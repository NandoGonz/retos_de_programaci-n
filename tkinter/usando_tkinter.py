import tkinter as tk

# Crear la ventana
ventana = tk.Tk()

# Título de la ventana
ventana.title("Mi primera app con Tkinter")

# Tamaño de la ventana
ventana.geometry("400x300")

# Tamaño minimo
ventana.minsize(300, 300)

# Tamaño maximo
ventana.maxsize(500, 500)


# Modificando el color de fondo
ventana.configure(bg="dodger blue")

# Bloqueando el tamaño de la ventana
ventana.resizable(False, False)

# Moificacion lateral
# ventana.resizable(True, False)

# Modificacion vertical
# ventana.resizable(False, True)

# Mostrar ventana en bucle
ventana.mainloop()
