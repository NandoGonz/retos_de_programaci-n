"""4. Contador de palabras en un texto
Crea una función que recibe un texto y devuelve un dict con cada palabra y cuántas veces aparece.
Ejemplo:

"hola mundo hola"


Resultado:

{"hola": 2, "mundo": 1}"""


def contador_palabras(texto):
    """Método creado para reemplazar caracteres y contar palabras repetidas"""
    texto = texto.lower()
    simbolo = (
        ",",
        ";",
        ".",
        ":",
        "!",
        "¿",
        "¡",
        "?",
    )
    # Recorremos y remplazamos los sigientes simbolos en el texto por un espacio
    for s in simbolo:
        texto = texto.replace(s, " ")

    palabras = texto.split()  # dividimos el texto en palabras usando split()

    # creamos un diccionario vacio
    contador = {}

    # Recorremos el texto para contar las palbras y agregarlas al diccionario
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    print("\n Contando palabras")
    for p, c in contador.items():
        print(f"{p} ---> {c}")


texto_a_contar = input("Escriba el texto para contar sus palabras: ")
contador_palabras(texto_a_contar)
