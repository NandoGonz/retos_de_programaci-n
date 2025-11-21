"""✅ 4. Figuras geométricas con área

Clase abstracta Figura:

calcular_area()

Clases:

Cuadrado

Círculo

Triángulo

Método común:

abrir área formateada

📌 Práctica:

Abstracción + polimorfismo"""

from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):
    """Clase abstracta padre"""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto que sera sobre escrito en las clases hijas"""


class Cuadrado(Figura):
    """Clae hija cuadrado"""

    def __init__(self, longitud: float):
        super().__init__()
        self.longitud = longitud

    def calcular_area(self):
        """Método sobre escrito para mostrar info de la sub clase Cudrado"""
        return f"El área del cuadrado es {self.longitud ** 2}"


class Circulo(Figura):
    """Clase hija circulo"""

    def __init__(self, radio: float):
        super().__init__()
        self.radio = radio

    def calcular_area(self):
        """Método sobre escrito para mostrar info de la sub clase Circulo"""
        return f"El área del circulo es {pi * (self.radio ** 2)}"


class Triangulo(Figura):
    """Clase hija triangulo"""

    def __init__(self, base: float, altura: float):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Método sobre escrito para mostrar info de la sub clase Triangulo"""
        return f"El area del circulo es {(self.base * self.altura) / 2}"


print("\n Mostrando el área de algunas figuras geometricas")
cuadrado = Cuadrado(6.5)
print(cuadrado.calcular_area())
ciruclo = Circulo(4.3)
print(ciruclo.calcular_area())
triangulo = Triangulo(5, 4.5)
print(triangulo.calcular_area())
