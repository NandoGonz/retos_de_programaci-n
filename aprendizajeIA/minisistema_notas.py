"""5. Mini sistema de notas (listas + diccionario)

Crea un diccionario notas donde la clave sea el nombre del estudiante y el valor una lista de notas.

Permite:

Agregar una nota a un estudiante (si no existe, se crea).

Calcula el promedio de un estudiante.

Mostrar quién tiene la mejor nota promedio."""

notas_estudiante = {}

while True:
    print("\n Mini sistem ade notas")
    print("1. Agregar estudiante")
    print("2. Agregar notas")
    print("3. Calcular promedio")
    print("4. Mostar notas")
    print("0. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                nombre = input("Ingrse el nombre del estudiante: ").title()
                if nombre not in notas_estudiante:
                    notas_estudiante[nombre] = []
                    print(f"✅ El estudiante {nombre} fue agregado de forma corrrecta")
                else:
                    print("El estudiante ya está registrado")

            case 2:
                nombre = input("Ingrese el nombre del estudiante: ").title()
                if nombre in notas_estudiante:
                    try:
                        nota = float(input("Ingrese la nota del estudiante: "))
                        if 0 >= nota <= 5:
                            notas_estudiante[nombre].append(nota)
                            print(f"✅ Nota registrada de forma correcta nota: {nota}")
                        else:
                            print("⚠️ La nota debe ser entre 0 y 5")
                    except ValueError:
                        print("⚠️ Debe ingresar un valor numérico")

            case 3:
                for nombre, nota in notas_estudiante.items():
                    if nota:
                        promedio = sum(nota) / len(nota)
                        if promedio > 3:
                            print(
                                f"El estudiante {nombre} aprobo promedio es de: {promedio}"
                            )
                        else:
                            print(
                                f"El estudiante {nombre} reprobo se promedio es de: {promedio}"
                            )
            case 4:
                for nombre, nota in notas_estudiante.items():
                    print(f"El alumno {nombre} tiene las siguientes notas {nota}")

            case 0:
                print("Saliendo del mini sistema de notas")
                break

    except ValueError:
        print("Ingrese una opción correcta")
