import tkinter as tk

ventana = tk.Tk()
ventana.title("Primer grid")
"""
# Creamos labels y los posicionamos con grid
label = tk.Label(ventana, text="label 1")
label.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(ventana, text="label 2")
label2.grid(row=1, column=0, padx=5, pady=5)
"""

label1 = tk.Label(ventana, text="celda 1,1")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(ventana, text="celda 1,2")
label2.grid(row=0, column=1, padx=10, pady=10)

label3 = tk.Label(ventana, text="celda 2,1")
label3.grid(row=1, column=0, padx=10, pady=10)

label4 = tk.Label(ventana, text="celda 2,2")
label4.grid(row=1, column=1, padx=10, pady=10)

ventana.mainloop()
