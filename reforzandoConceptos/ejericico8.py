"""🔹 Ejercicio 8 – Sistema educativo (avanzado)

Diseña un sistema con:

Clase abstracta Persona con el método mostrar_info().

Clases hijas Estudiantey Profesor, cada una con sus atributos y comportamiento.
Aplicación de encapsulamiento para proteger la información personal."""

from abc import ABC, abstractmethod


class Persona(ABC):

    @abstractmethod
    def mostrar_info(self):
        return "Saludo"


class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, n_id_colegio: int) -> None:
        super().__init__()
        self.__nombre = nombre
        self.edad = edad
        self.__n_id_colegio = n_id_colegio

    # el método heredado funcionara como un aespecie de getter en ala clase hija
    def mostrar_info(self):
        return f"Alumno {self.__nombre} | Edad {self.edad} | id_colegio {self.__n_id_colegio}"


class Profersor(Persona):
    def __init__(self, nombre: str, cc: int, direccion: str):
        super().__init__()
        self.nombre = nombre
        self.__cc = cc
        self.__direccion = direccion

    # el método heredado funcionara como un aespecie de getter en ala clase hija
    def mostrar_info(self):
        return f"Profesor {self.nombre} | direcciín {self.__direccion} | número de id {self.__cc}"


estu1 = Estudiante("Kristina", 4, 1234)
print(estu1.mostrar_info())

profe1 = Profersor("Cipriano", 1089453, "Barrio La Franciscana cll 16 #13-16")
print(profe1.mostrar_info())
