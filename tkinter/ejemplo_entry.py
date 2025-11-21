import tkinter as tk

ventana = tk.Tk()
ventana.title("mi primer entry")

# creamos el nombre de la entrada
etiqueta = tk.Label(ventana, text="Lo de abajo es un entry")
etiqueta.pack()

# creamos la entrada que recibira la información del ususario
entrada = tk.Entry(ventana)
entrada.pack()

# Modificando el aspecto de la entrada
entrada.config(
    fg="blue", bg="lightgray", font=("Arial, 12")
)  # en el font va el tipo de letra y el tamaño de esta
entrada.pack()
# Agregando texto por defecto
entrada.insert(0, "Ingresa algo")

# visualizando el texto del insert
# Creamos una varable y le asignamos el valor entrada, usamos el método get() para mostrar la info
"""texto = entrada.get()
print(texto)"""


# Aplicando lo aprendido en un método
# CREAMOS EL MÉTODO
def aplicar_texto():
    # Usamos la variable texto para ver que inserto el ususario
    texto = entrada.get()
    # A la etiqueta le cambiamos el texto que le dimos por defecto por le del usuario
    etiqueta.config(text=texto)


# Para hacer un llamado correcto de este método crearemos un nuevo boton y destro de este lo llamaremos
boton_aplicar = tk.Button(ventana, text="Aplicar texto", command=aplicar_texto)
# siempre vamos el contenido de la interfaz llamando a lavariable y usanod el método pack()
boton_aplicar.pack()

ventana.mainloop()
