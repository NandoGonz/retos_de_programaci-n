"""✅ EJERCICIO 3 — Buscar una palabra en el archivo

📄 Archivo: notas.txt

Contenido:

Hoy estudié Python
Python es muy útil
Mañana practicaré más

🎯 Objetivo:

Pedir una palabra al usuario

Mostrar las líneas que la contienen

📌 Ejemplo:

Ingrese palabra: Python
→ Hoy estudié Python
→ Python es muy útil"""

with open("notas.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Hoy estudié Python\n")
    archivo.write("Python es muy útil\n")
    archivo.write("Mañana practicare más\n")

lista_notas = []
with open("notas.txt", "r", encoding="UTF-8") as archivo:
    notas = archivo.readlines()
    for n in notas:
        lista_notas.append(n.strip())

filtrar = []
palabra = input("Ingrese una palabra para buscar: ").strip()
for p in lista_notas:
    if palabra in p:
        filtrar.append(p.strip())
for i in filtrar:
    print(i)
