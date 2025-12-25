"""✅ 8. Gestión de notas

Clase Alumno:

lista de notas

agregar_nota()

_promedio()

Propiedad para mostrar promedio

Otra clase Curso que tenga una lista de alumnos.

📌 Práctica:

propiedades + listas + encapsulamiento
"""


class Alumno:
    """
    Representa a un estudiante y permite gestionar sus calificaciones.
    """

    def __init__(self, nombre: str):
        """
        Inicializa un nuevo alumno.

        Args:
            nombre (str): El nombre del alumno.
        """
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota: float):
        """
        Agrega una nota a la lista de calificaciones del alumno.

        Args:
            nota (float): La calificación a agregar.
        """
        # nota = float(input("Agrega una calificación: "))
        self.notas.append(nota)

    def calcular_promedio(self):
        """
        Calcula el promedio de las notas del alumno.

        Returns:
            float: El promedio calculado. Retorna 0.0 si no hay notas.
        """
        if not self.notas:
            return 0.0
        prommedio = sum(self.notas) / len(self.notas)
        return prommedio


class Curso:
    """
    Gestiona una colección de alumnos y permite consultar sus promedios.
    """

    def __init__(self):
        """Inicializa un curso con una lista vacía de alumnos."""
        self.alumnos = []

    def agregar_alumno(self, alumno):
        """
        Agrega un objeto Alumno a la lista del curso.

        Args:
            alumno (Alumno): La instancia del alumno a agregar.
        """
        self.alumnos.append(alumno)

    def mostrar_promedio(self):
        """
        Recorre la lista de alumnos e imprime el promedio de cada uno en consola.
        """
        for alumno in self.alumnos:
            print(
                f"El alumno {alumno.nombre}: tiene un promedio de {alumno.calcular_promedio()}"
            )


curso = Curso()
a1 = Alumno("Adriana")
a1.agregar_nota(3.4)
a1.agregar_nota(4.5)
a1.agregar_nota(2.5)
a1.agregar_nota(3.8)
curso.agregar_alumno(a1)
# curso.mostrar_promedio()

a2 = Alumno("Nando")
a2.agregar_nota(4.5)
a2.agregar_nota(3.6)
a2.agregar_nota(2.9)
a2.agregar_nota(4.3)
curso.agregar_alumno(a2)
curso.mostrar_promedio()
