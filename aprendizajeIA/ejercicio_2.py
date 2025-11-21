"""Crea una clase Estudiante con atributos nombre, edad y carrera.

Agrega un método presentarse() que devuelva un string con sus datos.

Usa anotaciones de tipo.

Crea una lista de estudiantes y muéstralos con un bucle."""


class Estudiante:

    def __init__(self, nombre: str, edad: int, carrera: str):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."


"""e1 = Estudiante("Luis", 29, "sistema")
e2 = Estudiante("Adriana", 30, "Administración")
e3 = Estudiante("Kristina", 3, "Kinder")

estudiantes = []

estudiantes.append(e1)
estudiantes.append(e2)
estudiantes.append(e3)

for e in estudiantes:
    print(e.presentarse())"""


estudiantes = [
    Estudiante("Luis", 29, "sistemas"),
    Estudiante("Adriana", 30, "Administración"),
    Estudiante("Kristina", 3, "Kinder"),
]


estudiantes.append(Estudiante("juan", 67, "economía"))
for e in estudiantes:
    print(e.presentarse())
