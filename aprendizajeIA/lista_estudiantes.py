"""1. Lista de estudiantes
Crea una lista donde se guardan los nombres de estudiantes.

Permite agregar un estudiante nuevo.

Si el usuario intenta agregar un nombre vacío, lanza un ValueError.

Muestra al final todos los estudiantes inscritos"""

estudiantes = []
while True:

    try:
        romper = input(
            "Escriba 'salir' si desea salir o presione enter para registrar un estudiante: "
        )
        if romper == "salir":
            print("Está saliendo del registro de estudiantes...")
            break

        n_estudiante = input("Ingrese el nombre del estudiante: ").title()
        if n_estudiante == "":
            raise ValueError("⚠️  El nombre del estudiante no puede estar vacio")
        print("✅ Estudiante agregado con exito")
        estudiantes.append(n_estudiante)

    except ValueError as e:
        print(e)

for i, estudiantes in enumerate(estudiantes):
    print(f"👨👧 {i+1, estudiantes}")
