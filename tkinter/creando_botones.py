import tkinter as tk

ventana = tk.Tk()
ventana.title("mi primer boton en tk")

boton = tk.Button(ventana, text="presionar aquí")
boton.config(fg="white", bg="pink", font=("Verdana", 14))
boton.pack()

etiqueta = tk.Label(ventana, text="hola, soy un label")
etiqueta.pack()


def boton_presionado():
    """dandole funcionamiento al boton"""
    print("Boton activado")


boton.config(
    command=boton_presionado
)  # el comando command= nos ayuda a darle funcionamiento al boton
# boton_presionado()


def cambiar_texto():
    etiqueta.config(text="Boton presionado")


boton.config(command=cambiar_texto)


ventana.mainloop()
