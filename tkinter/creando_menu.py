"""
comparación ente Menubutton, Menu y menús contextuales
- Meubutton: Botón que muestra un menú cuando hace clic en él
-Menu: Barra de menú que se encuentra en la parte superior de la ventana de la aplicación
- Menús contextuales: Menús que aparecen al hacer clic con el botón derecho del ratón en un aárea
especifica de la vnetana
"""

import tkinter as tk

ventana = tk.Tk()

menubutton = tk.Menubutton(ventana, text="Archivo")
menubutton.pack()

menu = tk.Menu(menubutton)
menubutton.config(menu=menu)

# añadiendo elemnetos al menu
"""menu.add_command(label="Abrir")
menu.add_command(label="Guardar")"""

# Creando una función para añadir botones al menu

def abrir_archivo():
    print("Archivo abierto")

menu.add_command(label="Abrir", command=abrir_archivo)
menu.add_command(label="Guardar")

ventana.mainloop()

# añadiendo elemnetos al menu
"""menu.add_command(label="Abrir")
menu.add_command(label="Guardar")"""

# Creando una función para añadir botones al menu
