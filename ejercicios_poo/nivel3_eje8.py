"""8. Clase NotasEstudiante:

Usa un diccionario donde clave = nombre, valor = lista de notas.

Métodos: agregar_nota(), promedio_estudiante(), mejor_estudiante()."""


class NotasEstudiante:
    def __init__(self):
        self.notas = {}
        self.promedios = {}
        self.menu()

    def registrar_alumno(self):
        nombre = input("Ingrese el nombre del alumno: ").title()
        if nombre not in self.notas:
            self.notas[nombre] = []
            print("Alumno agregado de forma correcta")
        else:
            print("Ya exite un alumno con este nombre")

    def asignar_nota(self):
        nombre = input("Ingrese el nombre del alumno: ").title()
        nota = float(input("Ingrese la nota del alumno: "))
        if nombre in self.notas:
            self.notas[nombre].append(nota)
            print("Nota aignada correctamente")

    def promedio_estudiante(self):
        for nombre, nota in self.notas.items():
            if nota:
                promedio = sum(nota) / len(nota)
                print(f"El alumno {nombre} | Tiene un promedio de {promedio}")

    def mejor_alumno(self):
        for nombre, nota in self.notas.items():
            if nota:
                promedio = sum(nota) / len(nota)
                self.promedios[nombre] = promedio
                if 4.5 < self.promedios[nombre] < 5.0:
                    print(
                        f"El mejor alumno es {nombre} con un promedio de {self.promedios[nombre]}"
                    )
                else:
                    print("No hay un mejor alumno")
        print("No hay alumnos registrados")

    def menu(self):

        while True:
            print("\n Bienvenido al menú de su inventario")
            print("1. Registrar Alumno")
            print("2. Asignar nota")
            print("3. Promedio de los alumnos")
            print("4. Mejor alumno")
            print("0. Salir")
            try:
                opcion = int(input("Ingrese una opción: "))
                match opcion:
                    case 1:
                        self.registrar_alumno()
                    case 2:
                        self.asignar_nota()
                    case 3:
                        self.promedio_estudiante()
                    case 4:
                        self.mejor_alumno()
                    case 0:
                        print("📤 Saliendo del sistema")
                        break

            except ValueError:
                print("⚠️ Dígite una opción valida o un valor númerico ")


e1 = NotasEstudiante()
