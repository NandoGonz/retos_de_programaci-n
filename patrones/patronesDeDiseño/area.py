"""Usando el método de fábrica crearemos un programa que calcule el área de un triangulo, un circulo y un cuadrado"""

from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Circulo(Figura):
    def calcular_area(self, radio: float):
        print(f"El área del circulo es: {pi * radio:,.2f}")


class Triangulo(Figura):
    def calcular_area(self, base: float, altura: float):
        print(f"La base del triangulo es: {(base * altura ) / 2:,.2f}")


# Creamos nuestra fabrica
class AreasFabrica:
    @staticmethod
    def tipo(tipo: str):
        if tipo == "circulo":
            return Circulo()
        elif tipo == "triangulo":
            return Triangulo()
        else:
            raise ValueError("Figura desconocida, area imposible de calcular")


areasfab = AreasFabrica.tipo("triangulo")
areasfab.calcular_area(4, 4)
# se puede hacer una fabrica de areas, pero viola ciertos estandares(paso más argumentos que acepta el método de la clase padre)
