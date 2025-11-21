# Importamos la librería tkinter y la renombramos como tk para que sea más fácil de usar.
import tkinter as tk

# Creamos la ventana principal de la aplicación.
ventana = tk.Tk()
# Le asignamos un título a la ventana.
ventana.title("Ejemplo multi-boton")


# Definimos una función que se ejecutará cuando se haga clic en un botón.
# Esta función se conoce como "callback" o "manejador de eventos".
def on_click(event):
    # El parámetro 'event' contiene información sobre el evento que ocurrió (como el clic del ratón).
    # 'event.widget' se refiere al widget (en este caso, el botón) que disparó el evento.
    # Accedemos a su propiedad 'text' para saber qué botón fue presionado y lo imprimimos en la consola.
    print(f"{event.widget['text']} presionado")


# Creamos una lista de botones usando una "list comprehension" (comprensión de listas).
# Esto crea 3 botones (para i en el rango de 0 a 2) y los guarda en la lista 'buttons'.
# Cada botón tendrá un texto diferente: "Bóton 0", "Bóton 1", "Bóton 2".
buttons = [tk.Button(ventana, text=f"Bóton {i}") for i in range(3)]

# Recorremos la lista de botones que acabamos de crear.
for button in buttons:
    # El método pack() organiza el botón en la ventana, haciéndolo visible.
    button.pack()
    # El método bind() asocia un evento con una función (callback).
    # "<Button-1>" es el evento de clic izquierdo del ratón.
    # Cuando se hace clic izquierdo en este botón, se llamará a la función 'on_click'.
    button.bind("<Button-1>", on_click)

# Iniciamos el bucle principal de la aplicación. Esto mantiene la ventana abierta
# y a la espera de eventos (como clics de botón, movimientos del ratón, etc.).
ventana.mainloop()
