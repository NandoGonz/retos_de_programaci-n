import tkinter as tk

ventana = tk.Tk()
ventana.title("Usando checkbutton")
variable_check1 = (
    tk.BooleanVar()
)  # cuando solo creamos mas de un boton usamos el comando BooleanVar()
# variable_check2 = tk.BooleanVar()


# Creamso una función para cambiar el estado del boton
# def on_checkbutton_cambio():
#   print("Checkbutton cambiado")


def habilitar():
    if variable_check1.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")


check1 = tk.Checkbutton(
    ventana,
    text="Habilitar botón",
    font=("Times new Roman", 14),
    fg="blue",
    bg="lightgray",
    variable=variable_check1,
    command=habilitar,
)

boton = tk.Button(ventana, text="Botón", state="disabled")
"""check2 = tk.Checkbutton(
    ventana,
    text="Opción 1",
    font=("Times new Roman", 14),
    fg="yellow",
    bg="red",
    variable=variable_check2,
)"""
check1.pack()
# check2.pack()
boton.pack()

ventana.mainloop()
