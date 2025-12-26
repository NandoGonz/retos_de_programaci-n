# creamos una variable archivo y usamos el método open() para abrir nuestro archivo
# en el método open escibimos el nombre del archivo que queremso editar
archivo = open(
    "miPrimerTexto.txt", "w", encoding="UTF-8"
)  # utf_8 es para caracteres especiales
# con el método write puedo escribir dentro del archivo.txt
archivo.write("1: Debo tener presente en todo momento los conceptos básicos")
# con el método close cierro el archivo, esto es por seguridad
# Siempre se agrega un salto de linea
archivo.write("\n")
archivo.write(
    "2: Debo experimentar con la mayoria de herramientas que nos brindan los formatos"
)
archivo.write("\n")
archivo.write("3: Ya empiezo a entender")
archivo.close()

tareas = [
    "1: No es bueno hacer todo dento del mismo archivo",
    "2: Solo será por este vez",
]

archivo1 = open("lista_tareas.txt", "w", encoding="UTF-8")
for tarea in tareas:
    archivo1.write(tarea)
    archivo1.write("\n")
archivo1.close()

# Lectura de datos usando with
with open("lista_tareas.txt", encoding="UTf-8") as archivo:
    # extraemos la info líena por líne usando el método readline()
    lineas = archivo.readline()

# Agregando un anueva tarea
n_tarea = "3: Hacer de uno a dos ejercicios de los conceptos que ya domine"
with open("lista_tareas.txt", "a", encoding="UTF-8") as archivo1:
    archivo1.write(n_tarea)
    archivo1.write("\n")

n_tarea = "4: Me siento algo perdido en este tema y es gracioso, no es muy complicado"
with open("lista_tareas.txt", "a", encoding="UTF-8") as archivo1:
    archivo1.write(n_tarea)
    archivo1.write("\n")


# Lectura de datos usando with
with open("lista_tareas.txt", encoding="UTf-8") as archivo1:
    # extraemos la info líena por líne usando el método readline() retorna una lista
    lineas = archivo1.readlines()
    print(lineas)
