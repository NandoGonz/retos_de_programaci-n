# Importa la librería tkinter y la renombra como tk para facilitar su uso.
import tkinter as tk

# Crea la ventana principal de la aplicación.
ventana = tk.Tk()


# Define una función que se ejecutará para mostrar el menú contextual.
# El parámetro 'event' contiene información sobre el evento que la llamó (en este caso, el clic del ratón).
def mostrar_menu_contextual(event):
    # El método tk_popup() muestra el menú en una ubicación específica de la pantalla.
    # event.x_root y event.y_root son las coordenadas X e Y del cursor del ratón en la pantalla
    # cuando se produjo el evento (clic derecho).
    menu_contextual.tk_popup(event.x_root, event.y_root)


# Crea un widget de menú que pertenecerá a la ventana principal.
# tearoff=0 evita que aparezca una línea punteada al inicio del menú que permite "desprenderlo".
menu_contextual = tk.Menu(ventana, tearoff=0)
# Agrega una opción (comando) con la etiqueta "Cortar" al menú contextual.
menu_contextual.add_command(label="Cortar")
# Agrega una opción con la etiqueta "Copiar".
menu_contextual.add_command(label="Copiar")
# Agrega una opción con la etiqueta "Pegar".
menu_contextual.add_command(label="Pegar")

# Asocia un evento a la ventana principal.
# El evento "<Button-3>" corresponde al clic derecho del ratón.
# Cuando se hace clic derecho en la ventana, se llama a la función 'mostrar_menu_contextual'.
ventana.bind("<Button-3>", mostrar_menu_contextual)

# Inicia el bucle principal de la aplicación, que mantiene la ventana abierta y a la espera de eventos.
ventana.mainloop()
