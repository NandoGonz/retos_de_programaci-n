"""Crea una clase Estudiante con:

Atributos:

nombre (público).

__nota (privado).

Métodos:

asignar_nota(nota) → valida que esté entre 0 y 5 antes de asignarla.

obtener_nota() → retorna la nota.

es_aprobado() → retorna True si la nota es >= 3, si no False."""


class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__nota = 0

    def asignar_nota(self, nota: float):
        """5 Validación en Estudiante
        Haz que asignar_nota() lance un error si la nota es mayor a 5 o menor a 0, y que se capture con try/except para mostrar un mensaje claro.
        """
        if nota < 0 or nota > 5:
            raise ValueError("⚠️ La nota es invalida debe ser > 3 y < 5")
        self.__nota = nota
        print(f"✅ nota asignada de forma correcta {nota}")

    def obtner_nota(self):
        return self.__nota

    def es_aprobado(self):
        if self.__nota > 3 and self.__nota < 5:
            print(
                f"✅ El estudiante {self.nombre} tiene una calificación de {self.__nota} y a aprobado"
            )
        else:
            print(
                f"⚠️  El estudiante {self.nombre} tiene una calificación de {self.__nota} y a reprobado"
            )


print("Mostrando a los alumnos y sus calificaciones\n")
print("Usando try y except\n")
print("=" * 70)
estudiante1 = Estudiante("luis")
estudiante2 = Estudiante("Adriana")
estudiante3 = Estudiante("Kristina")
estudiante4 = Estudiante("Emiro")
try:
    estudiante1.asignar_nota(4.5)
    print(f"Calificiación: 🗒️ {estudiante1.obtner_nota()}")
    estudiante1.es_aprobado()
except ValueError as e:
    print(e)
print("=" * 70)

try:
    estudiante2.asignar_nota(2.6)
    print(f"Calificiación: 🗒️ {estudiante2.obtner_nota()}")
    estudiante2.es_aprobado()
except ValueError as e:
    print(e)
print("=" * 70)

try:
    estudiante3.asignar_nota(4.5)
    print(f"Calificiación: 🗒️ {estudiante3.obtner_nota()}")
    estudiante3.es_aprobado()
except ValueError as e:
    print(e)
print("=" * 70)

try:
    estudiante4.asignar_nota(8)
    print(f"Calificiación: 🗒️ {estudiante4.obtner_nota()}")
    estudiante4.es_aprobado()
except ValueError as e:
    print(e)
