"""Crea una clase Coche con atributos marca, modelo y año.

Agrega un método mostrar_info() que devuelva la información del coche en un string.

Crea al menos dos objetos de tipo Coche y muestra su información."""


class Coche:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def mostrar_info(self):
        return f"La marca del coche es {self.brand} su modelo es {self.model} y es del año {self.year}"


coche1 = Coche("Toyota", "Corolla", 2018)
# print(coche1.mostrar_info())

# 👉 Crea dos coches más (coche2 y coche3) y muestra la información de todos usando un bucle.

coche2 = Coche("Renualt", "323 HS", 1996)
# print(coche2.mostrar_info())

coche3 = Coche("Hoda", "Civic", 2000)
# print(coche3.mostrar_info())
