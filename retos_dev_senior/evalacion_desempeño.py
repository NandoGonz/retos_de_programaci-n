"""8. Evaluación de desempeño académico
Un colegio desea registrar las calificaciones de 5 estudiantes en tres materias. Calcula el promedio de cada estudiante y determina si pasa (promedio ≥ 3.0) o reprueba. Muestra el estado de cada uno.
"""

# pedir los datos y crear nuestras variables
estudiante1 = []
estudiante2 = []
estudiante3 = []
estudiante4 = []
estudiante5 = []
paraPromedio = 3
nombre = input("ingrese nombre: ")

try:
    for i in range(3):
        notas = float(input(f"ingrese una nota{i+1}: "))
        estudiante1.append(notas)
except ValueError:
    print("ingrese un valor numerico")
promedio = sum(estudiante1[i] / paraPromedio for i in range(3))


if promedio >= 3:
    print(
        f"el estdiante {nombre} tiene un promedio de {promedio:.2f} por lo tanto aprueba"
    )
else:
    print(f"el estudiante {nombre} tiene un promedio de {promedio:.2f} reprueba")
print(estudiante1)

nombre = input("ingrese nombre: ")
try:
    for i in range(3):
        notas = float(input(f"ingrese una nota{i+1}: "))
        estudiante2.append(notas)
except ValueError:
    print("ingrese un valor numerico")
promedio = sum(estudiante2[i] / paraPromedio for i in range(3))


if promedio >= 3:
    print(
        f"el estdiante {nombre} tiene un promedio de {promedio:.2f} por lo tanto aprueba"
    )
else:
    print(f"el estudiante {nombre} tiene un promedio de {promedio:.2f} reprueba")
print(estudiante2)

nombre = input("ingrese nombre: ")
try:
    for i in range(3):
        notas = float(input(f"ingrese una nota{i+1}: "))
        estudiante3.append(notas)
except ValueError:
    print("ingrese un valor numerico")
promedio = sum(estudiante3[i] / paraPromedio for i in range(3))


if promedio >= 3:
    print(
        f"el estdiante {nombre} tiene un promedio de {promedio:.2f} por lo tanto aprueba"
    )
else:
    print(f"el estudiante {nombre} tiene un promedio de {promedio:.2f} reprueba")
print(estudiante3)

nombre = input("ingrese nombre: ")
try:
    for i in range(3):
        notas = float(input(f"ingrese una nota{i+1}: "))
        estudiante4.append(notas)
except ValueError:
    print("ingrese un valor numerico")
promedio = sum(estudiante4[i] / paraPromedio for i in range(3))


if promedio >= 3:
    print(
        f"el estdiante {nombre} tiene un promedio de {promedio:.2f} por lo tanto aprueba"
    )
else:
    print(f"el estudiante {nombre} tiene un promedio de {promedio:.2f} reprueba")
print(estudiante4)


nombre = input("ingrese nombre: ")
try:
    for i in range(3):
        notas = float(input(f"ingrese una nota{i+1}: "))
        estudiante5.append(notas)
except ValueError:
    print("ingrese un valor numerico")
promedio = sum(estudiante5[i] / paraPromedio for i in range(3))


if promedio >= 3:
    print(
        f"el estdiante {nombre} tiene un promedio de {promedio:.2f} por lo tanto aprueba"
    )
else:
    print(f"el estudiante {nombre} tiene un promedio de {promedio:.2f} reprueba")
print(estudiante5)
