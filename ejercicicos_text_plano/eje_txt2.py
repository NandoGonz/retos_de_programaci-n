"""✅ EJERCICIO 2 — Contar líneas del archivo

📄 Archivo: tareas.txt

Contenido:

Estudiar Python
Hacer ejercicios
Leer documentación

🎯 Objetivo:

Contar las líneas que tiene el archivo

Mostrar el total

📌 Resultado esperado:

El archivo tiene 3 líneas"""

# ---------------------------------------------------------
# Paso 1: Creación del archivo
# ---------------------------------------------------------
# Abrimos el archivo en modo escritura ('w').
# Si el archivo ya existe, esto borrará su contenido anterior.
with open("tareas.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Estudiar Python\n")

# ---------------------------------------------------------
# Paso 2: Agregar contenido
# ---------------------------------------------------------
# Abrimos el archivo en modo adjuntar ('a' - append).
# Esto permite agregar nuevas líneas al final sin borrar lo existente.
with open("tareas.txt", "a", encoding="UTF-8") as archivo:
    archivo.write("Hacer ejercicios\n")
    archivo.write("Leer documentación\n")

# ---------------------------------------------------------
# Paso 3: Lectura y conteo
# ---------------------------------------------------------
list_cont = []
# Abrimos el archivo en modo lectura ('r').
with open("tareas.txt", "r", encoding="UTF-8") as archivo:
    # readlines() lee todo el archivo y retorna una lista donde cada elemento es una línea.
    para_list = archivo.readlines()

    # Iteramos sobre las líneas obtenidas
    for c in para_list:
        # .strip() elimina los espacios en blanco al inicio, al final (incluyendo el salto de línea)
        list_cont.append(c.strip())

    # Mostramos la cantidad de elementos en la lista procesada
    print(f"La cantidad de líneas son: {len(list_cont)}")
