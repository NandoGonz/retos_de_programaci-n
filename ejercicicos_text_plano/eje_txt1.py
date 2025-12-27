"""✅ EJERCICIO 1 — Leer archivo línea por línea

📄 Archivo: frases.txt

Contenido:

Aprender Python es genial
Practicar todos los días
La constancia gana

🎯 Objetivo:

Leer el archivo

Mostrar cada línea sin saltos de línea

🧠 Pistas:

readlines()

.strip()"""

# ---------------------------------------------------------
# Paso 1: Creación del archivo y escritura inicial
# ---------------------------------------------------------
# Usamos 'w' (write) para crear el archivo o sobrescribirlo si ya existe.
with open("frases.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Aprender Python es genial\n")
    archivo.write("Practicar todos los dias\n")
    # Nota: Con 'with', no es necesario usar archivo.close(), Python lo hace automático.

# ---------------------------------------------------------
# Paso 2: Anexar contenido
# ---------------------------------------------------------
# Usamos 'a' (append) para agregar texto al final sin borrar el contenido previo.
with open("frases.txt", "a", encoding="UTF-8") as archivo:
    archivo.write("La constancia gana")

# ---------------------------------------------------------
# Paso 3: Lectura y visualización
# ---------------------------------------------------------
# Usamos 'r' (read) para leer el contenido.
with open("frases.txt", "r", encoding="UTF-8") as archivo:
    # readlines() lee todo el archivo y guarda cada línea como un elemento de una lista.
    cont = archivo.readlines()

    # Iteramos sobre la lista de líneas
    for c in cont:
        # .strip() elimina los espacios en blanco y saltos de línea al inicio y final.
        print(c.strip())
