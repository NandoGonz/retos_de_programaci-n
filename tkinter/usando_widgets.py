import tkinter as tk

ventana = tk.Tk()
ventana.title("primer label")
ventana.geometry("450x350")

etiqueta = tk.Label(ventana, text="Hola, soy tu primer label")
etiqueta.pack()

# si queremso modificar algo de nuestra interfaz grafica isamos el método config()
etiqueta.config(text="Soy el nuevo nombre del label")
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 12, "italic"))
etiqueta.pack()


ventana.mainloop()
