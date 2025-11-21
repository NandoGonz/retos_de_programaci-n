"""🔹 Ejercicio 4 – Abstracción con cálculos

Crea una clase abstracta FiguraGeometricacon un método abstracto calcular_area().
Implementa las clases:

Rectangulo

Triangulo

Circulo
Cada clase debe tener sus propios atributos y calcular su área correctamente."""

from abc import ABC, abstractmethod
from math import pi


class FiguraGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        print("Claculando el área de las figuras")


class Rectangulo(FiguraGeometrica):

    def calcular_area(self, largo: float, ancho: float):
        return f" La área del Rectangulo es {largo * ancho}"


class Triangulo(FiguraGeometrica):

    def calcular_area(self, base: float, altura: float):
        return f" El área del triangulo es {(base * altura) / 2}"


class Circulo(FiguraGeometrica):

    def calcular_area(self, radio: float):
        return f"El área del circulo es {pi * radio ** 2:.2f}"


r1 = Rectangulo()
print(r1.calcular_area(4.5, 6.5))
print()
t1 = Triangulo()
print(t1.calcular_area(6, 4.5))
print()
c1 = Circulo()
print(c1.calcular_area(7.2))
