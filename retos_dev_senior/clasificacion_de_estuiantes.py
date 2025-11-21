"""clasificación de estudiantes por nota pide la nota final de 10 estudiantes. Clasifica cada uno asi
nota >= 4.5 excelente,
nota entre 3.5 y 4.4 bueno,
nota entre 3.0 y 3.4 regular,
nota < 3.0 insuficiente"""

estudiantes = []
definitiva = []
for alumnos in range(10):
    alumno = input(f"nombre del alumno {alumnos+1} : ")
    nota = float(input("ingrese la nota: "))
    estudiantes.append(alumno)
    definitiva.append(nota)

    if nota >= 4.5 and nota <= 5.0:
        print("excelente")
    elif nota >= 3.5 and nota <= 4.4:
        print("bueno")
    elif nota >= 3.0 and nota <= 3.4:
        print("regular")
    else:
        print("insuficiente")
print("\n estás son las notas de cada alumno")

# imprimos las nots para cada alumno de forma clara
for alumnos in range(10):
    print(f"la nota del estudiante {estudiantes[alumnos]} es {definitiva[alumnos]}")

print("\n estas son todas las notas recibidas")
