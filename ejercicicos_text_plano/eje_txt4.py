'''✅ EJERCICIO 4 — Guardar coincidencias en otro archivo

📄 Archivo origen: mensajes.txt

Error en el sistema
Proceso exitoso
Error de conexión
Todo correcto


📄 Archivo destino: errores.txt

🎯 Objetivo:

Leer mensajes.txt

Guardar solo las líneas que contienen "Error" en errores.txt

📌 Pistas:

if "Error" in linea

modo"w"'''

with open("mensajes.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Error en el sistema\n")
    archivo.write("Proceso exitoso\n")
    archivo.write("Error de conexión\n")
    archivo.write("Todo correcto\n")

list_mensaje = []
with open("mensajes.txt", "r", encoding="UTF-8") as archivo:
    mensaje = archivo.readlines()
    for m in mensaje:
        list_mensaje.append(m)

errores = []
with open("errores.txt", "w", encoding="UTF-8") as archivo:
    for e in list_mensaje:
        if "Error" in e:
            errores.append(e.strip())
    for e in errores:
        archivo.write(f"{e}\n")

with open("errores.txt", "r", encoding="UTF-8") as archivo:
    error_encon = archivo.readlines()
    for e in error_encon:
        print(e.strip())
