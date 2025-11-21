import tkinter as tk

ventana = tk.Tk()
# Creamos nuestra stringvar
texto = tk.StringVar(value="Hola Mundo")

# Podemos darle un nuevo valor o agregar valor a nuestra variable en caso de que este vacia usado el método set()
texto.set("Aprendiendo cosas nuevas")

"""# Usamos el método get() par visulizar la info de nuestra variable de control
print(texto.get())
"""

# Agregando widgets a nuestra varaible de control "entry"
entrada = tk.Entry(
    ventana, textvariable=texto
)  # debemso agregar el textvariable para identificar nuestra variable
entrada.pack()

# usando funcioners callback
# Creamos una etiqueta
etiqueta = tk.Label(ventana)
etiqueta.pack()


# Creamos la función
def actulizar_etiqueta(*args):  # pasamso como argumeto *args para que funcione
    etiqueta.config(text=texto.get())


# Actualizando el texto usando el método trace(), detecta cambios en el valor de la variable
texto.trace("w", actulizar_etiqueta)

ventana.mainloop()
