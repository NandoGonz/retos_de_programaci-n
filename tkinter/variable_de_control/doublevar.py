import tkinter as tk

ventana = tk.Tk()
ventana.title("DoublenVar")

decimal = tk.DoubleVar(value=3.14)

# Un control deslizante, tiene un rango de valores los cuales varian según el deslizamieto qeu le demos
control_deslizante = tk.Scale(
    ventana, variable=decimal, from_=0, to=10, resolution=0.01, orient=tk.HORIZONTAL
)

control_deslizante.pack()

ventana.mainloop()
