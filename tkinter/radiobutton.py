import tkinter as tk

ventana = tk.Tk()
ventana.title("Radiobutton")  # estos nos ayudan para escoger una sola opción
# los checkbutton nos permiten sekleccionar o identificar más de una opción si es requerido
"""opcion1 = tk.Radiobutton(
    ventana,
    text="Opción 1",
    font=(
        "Time new Roman",
        16,
    ),
    fg="blue",
    bg="Lightgray",
)
# Tmbién podemos darle formato a los radiobutton
opcion1 = tk.Radiobutton(
    ventana, text="Opción", font=("Arial", 14), fg="blue", bg="lightgray"
)
opcion1.pack()
"""
# Creando un radiobutton con más opciones
# Creamos una variable de control
variable_control = tk.IntVar()


# Cambiando el color de la ventana por medio de una función
def cambiar_color():
    color_selecionado = variable_control.get()
    if color_selecionado == 1:
        ventana.config(bg="yellow")
    elif color_selecionado == 2:
        ventana.config(bg="green")


boton1 = tk.Radiobutton(
    ventana,
    text="boton1",
    font=("Times new Roman", 12),
    fg="red",
    bg="pink",
    variable=variable_control,
    value=1,
    command=cambiar_color,
)
boton2 = tk.Radiobutton(
    ventana,
    text="boton2",
    font=("Boston", 12),
    fg="blue",
    bg="lightgray",
    variable=variable_control,
    value=2,
    command=cambiar_color,
)


boton1.pack()
boton2.pack()


# Uso de funciones para darle funcinalidad a los botones
def mostrar_seleccion():
    print(f"Opción seleccionada: {variable_control.get()}")


button = tk.Button(ventana, text="Mostrar selacción", command=mostrar_seleccion)
button.pack()


ventana.mainloop()
