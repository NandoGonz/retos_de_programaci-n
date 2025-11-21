"""1. Clase Persona:

Atributos: nombre,edad

Método:mostrar_info()

Si la edad es menor de 0, lanza un ValueError."""


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        try:
            if self.edad < 0:
                raise ValueError("La edad debe ser mayor a 0")
            print(f"Me llamo {self.nombre} y tengo {self.edad} años de edad")
        except ValueError as e:
            print(e)


p1 = Persona("Luis", -6)
p1.mostrar_info()
p2 = Persona("Adriana", 8)
p2.mostrar_info()
