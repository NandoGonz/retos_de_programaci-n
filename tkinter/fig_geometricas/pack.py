import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo práctico pack")

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

button1 = tk.Button(frame_botones, text="Botón 1")
button1.pack(side="left", padx=5)

button2 = tk.Button(frame_botones, text="Botón 2")
button2.pack(side="left", padx=5)

button3 = tk.Button(frame_botones, text="Botón 3")
button3.pack(side="left", padx=5)

button4 = tk.Button(frame_botones, text="Botón 4")
button4.pack(side="left", padx=5)

ventana.mainloop()
