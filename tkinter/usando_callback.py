import tkinter as tk


# Una función callback solon se ejecuta cuando se realiza el evento
# Creamos una función
def on_click(event):
    print("Botón presionado")


Ventana = tk.Tk()

button = tk.Button(Ventana, text="Haz clic aquí")
button.pack()

# El métdono permite asociar el evento (Button-1) con la función on_click
# el evento <Button-1> nos indica que el evento solo sucedera si clicamos el clic izquierdo
# <Button-1> clic izquierdo
# <Button-2> boton de scrol
# <Button-3> clic derecho
button.bind("<Button-1>", on_click)


# También podemos usar las teclas del teclado para ejecutar un evento
def on_key_press(event):
    if event.char == "a":
        print("Tecla 'a' precionada")


Ventana.bind("<KeyPress>", on_key_press)


# Evento de redirección de ventana
def on_resize(event):
    print(f"La ventana ha sido redimensionada a {event.width}x{event.height}")


# Solo muestra las corrdenadas dentro de la ventana de la interfaz

Ventana.bind("<Configure>", on_resize)


# Evento de movimiento de mouse
def on_mouse_move(event):
    print(f"Raton movido a {event.x}x{event.y}")


Ventana.bind("<Motion>", on_mouse_move)

Ventana.mainloop()
