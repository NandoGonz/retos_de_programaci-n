# Importa la librería tkinter y la renombra como tk para facilitar su uso.
import tkinter as tk

# Crea la ventana principal de la aplicación.
ventana = tk.Tk()

# Crea un widget de menú (la barra de menú principal) y lo asocia a la ventana principal.
barra_menu = tk.Menu(ventana)
# Configura la ventana para que use 'barra_menu' como su barra de menú.
ventana.config(menu=barra_menu)

# Crea un nuevo menú desplegable (como "Archivo", "Editar", etc.) que pertenecerá a la barra de menú principal.
archivo_menu = tk.Menu(barra_menu)
# Agrega una opción de tipo "cascada" a la barra de menú principal.
# Esta opción tendrá el texto "Archivo" y, al hacer clic, desplegará el 'archivo_menu'.
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)

# Agrega un comando (una opción clickeable) con la etiqueta "Nuevo" al menú "Archivo".
archivo_menu.add_command(label="Nuevo")
# Agrega otro comando con la etiqueta "Abrir" al menú "Archivo".
archivo_menu.add_command(label="Abrir")
# Agrega una línea separadora para organizar visualmente las opciones del menú.
archivo_menu.add_separator()
# Agrega el comando "Salir" debajo del separador en el menú "Archivo".
archivo_menu.add_command(label="Salir")

# Inicia el bucle principal de la aplicación, que mantiene la ventana abierta y a la espera de eventos.
ventana.mainloop()
