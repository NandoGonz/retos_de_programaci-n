"""🔹 Ejercicio 7 – Abstracción en animales

Crea una clase abstracta Animalcon el método hacer_sonido().
Crea tres clases hijas ( Perro, Gato, Vaca) que implementan el método.
Usa polimorfismo para recorrer una lista de animales y ejecutar sus sonidos.
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        print("Haciendo sondio")


class Perro(Animal):
    def hacer_sonido(self):
        print("El 🐶 Hace guauuu")


class Gato(Animal):
    def hacer_sonido(self):
        print("El 😺 hace Miauuu")


class Vaca(Animal):
    def hacer_sonido(self):
        print("La 🐮 hace Muuuuuuu")


animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hacer_sonido()
