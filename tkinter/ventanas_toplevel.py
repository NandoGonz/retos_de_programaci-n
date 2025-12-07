from tkinter import *

ventana = Tk()
ventana.title("Ventana Principal")
ventana.geometry("600x400")


"""def abrir_ventana_toplevel():
    ventana_toplevel = Toplevel(ventana)
    ventana_toplevel.title("Ventana Toplevel")
    ventana_toplevel.geometry("300x200+50+50")
    label = Label(ventana_toplevel, text="Ventana Toplevel")
    label.pack()


boton = Button(ventana, text="Abrir Ventana Toplevel", command=abrir_ventana_toplevel)
boton.pack()"""

ventana_toplevel = Toplevel(ventana)
ventana_toplevel.title("Ventana Toplevel")
ventana_toplevel.geometry("300x200+50+50")
label = Label(ventana_toplevel, text="Ventana Toplevel")
label.pack()


# Creando boton para cerrar la ventana
def cerrar_ventana_toplevel(ventana):
    ventana.destroy()


boton_cerrar = Button(
    ventana,
    text="Cerrar Ventana Toplevel",
    command=lambda: cerrar_ventana_toplevel(ventana_toplevel),
)
boton_cerrar.pack()
ventana.mainloop()
