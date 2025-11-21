"""🔹 Ejercicio 2 – Control con getters y setters

Crea una clase Empleado con atributos privados __nombre y __salario.
Usa métodos getter y setter para modificar el salario, validando que no sea menor a un salario mínimo.
"""


class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.__nombre = nombre
        self.__salario = salario

    @staticmethod
    def salario_minimo(salario_min: float):
        return salario_min

    @property
    def salario(self):
        return (
            f" El empleado {self.__nombre} tiene un salario de ${self.__salario:,.2f}"
        )

    @salario.setter
    def salario(self, n_salario: float):
        if n_salario > Empleado.salario_minimo(1500000):
            self.__salario = n_salario
            print("Salario modificado con exito")
            return self.__salario
        print("El salrio no fue modificado")


emp1 = Empleado("Jose", 1200000)
print(emp1.salario)
emp1.salario = 1300000
emp1.salario = 2000000
print(emp1.salario)
