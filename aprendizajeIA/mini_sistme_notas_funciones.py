"""5. Mini sistema de notas (listas + diccionario)

Crea un diccionario notas donde la clave sea el nombre del estudiante y el valor una lista de notas.

Permite:

Agregar una nota a un estudiante (si no existe, se crea).

Calcula el promedio de un estudiante.

Mostrar quién tiene la mejor nota promedio."""

notas_estudiante = {}


def menu():
    """Muestra las opciones del mini sistema"""
    print("\n Mini sistema de notas")
    print("1. Agregar estudiante")
    print("2. Agregar notas")
    print("3. Calcular promedio")
    print("4. Mostar notas")
    print("0. Salir")


def agregar_estudiante():
    """Función que agrega un estudiante nuevo a la mini sistma"""
    nombre = input("Ingrse el nombre del estudiante: ").title()
    if nombre not in notas_estudiante:
        notas_estudiante[nombre] = []
        print(f"✅ El estudiante {nombre} fue agregado de forma corrrecta")
    else:
        print("El estudiante ya está registrado")


def agregar_notas():
    """Con esta función agregamos nota al estudiante y validamos el rango de valor de la misma"""
    nombre = input("Ingrese el nombre del estudiante: ").title()
    if nombre in notas_estudiante:
        try:
            nota = float(input("Ingrese la nota del estudiante: "))
            if nota >= 0 and nota <= 5:
                notas_estudiante[nombre].append(nota)
                print(f"✅ Nota registrada de forma correcta nota: {nota}")
            else:
                print("⚠️ La nota debe ser entre 0 y 5")
        except ValueError:
            print("⚠️ Debe ingresar un valor numérico")


def calcular_promedio():
    """Se encarga de calcular el promedio del estudiante"""
    for nombre, nota in notas_estudiante.items():
        if nota:
            promedio = sum(nota) / len(nota)
            if promedio > 3:
                print(f"El estudiante {nombre} aprobo promedio es de: {promedio}")
            else:
                print(f"El estudiante {nombre} reprobo se promedio es de: {promedio}")


def mostrar_notas():
    """función se encarga de mostrar las notas"""
    for nombre, nota in notas_estudiante.items():
        print(f"El alumno {nombre} tiene las siguientes notas {nota}")


def main():
    """Función para controlar el funcionamiento del mini sistema"""
    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    agregar_estudiante()
                case 2:
                    agregar_notas()
                case 3:
                    calcular_promedio()
                case 4:
                    mostrar_notas()
                case 0:
                    print("📤 Saliendo del mini sistema de calificaciones")
                    break
        except ValueError:
            print("Ingrese una opción valida")


if __name__ == "__main__":
    main()
