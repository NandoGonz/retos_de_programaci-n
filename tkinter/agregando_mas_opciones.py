import tkinter as tk

ventana = tk.Tk()

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

archivo_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=barra_menu)

archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir")

# Añadir un menú 'Editar' a la barra de menú
editar_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Editor", menu=editar_menu)

# Añadir  'Opciones' al menu
editar_menu.add_command(label="Deshacer")
editar_menu.add_command(label="Rehacer")

ventana.mainloop()
