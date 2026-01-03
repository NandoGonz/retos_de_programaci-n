"""✅ EJERCICIO 5 — Limpiar texto y guardarlo

📄 Archivo: datos.txt

   Python
   Archivos
   Texto plano

🎯 Objetivo:

Leer el archivo

Eliminar espacios extra

Guardar el texto limpio en datos_limpios.txt

📌 Resultado esperado:

Python
Archivos
Texto plano"""

with open("datos.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("   Python \n")
    archivo.write("   Archivos \n")
    archivo.write("      Texto plano \n")

datos_limpios = []
with open("datos.txt", "r", encoding="UTF-8") as archivo:
    dato = archivo.readlines()
    for d in dato:
        datos_limpios.append(d.strip())

with open("datos_limpios.txt", "w", encoding="UTF-8") as archivo:
    for d in datos_limpios:
        archivo.write(f"{d}\n")

with open("datos_limpios.txt", "r", encoding="UTF-8") as archivo:
    datos = archivo.readlines()
    for d in datos:
        print(d.strip())
