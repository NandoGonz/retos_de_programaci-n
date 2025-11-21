"""🔹 Ejercicio 3 – Abstracción con clases base

Crea una clase abstracta Transporte con un método abstracto moverse().
Implementa las clases hijas:

Auto

Bicicleta
Cada una debe sobrescribir el método y mostrar un mensaje diferente."""

from abc import ABC, abstractmethod


class Transporte(ABC):

    @abstractmethod
    def moverse(self):
        print("El transporte esta activo")


class Auto(Transporte):

    def moverse(self):
        print("El auto esta en movimiento")


class Bicicleta(Transporte):
    def moverse(self):
        print("La bicicleta esta siendo reparada")


trans1 = Auto()
trans1.moverse()
trans2 = Bicicleta()
trans2.moverse()
