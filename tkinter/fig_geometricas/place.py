import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejempla de place")

# Creamos labels y posicionamos con place
"""label1 = tk.Label(ventana, text="Label 1")
label1.place(x=50, y=50)

label2 = tk.Label(ventana, text="Label 2")
label2.place(x=100, y=100)"""

# Usando coordenadas relativas
label1 = tk.Label(ventana, text="Label 1")
label1.place(relx=0.25, rely=0.25)

label2 = tk.Label(ventana, text="Label 2")
label2.place(relx=0.5, rely=0.5)
ventana.mainloop()
