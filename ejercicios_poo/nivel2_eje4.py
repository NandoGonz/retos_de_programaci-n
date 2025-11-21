"""4. Clase Empleado y subclase Gerente:

Empleado tiene nombre, salario.

Gerente hereda de Empleado y agrega departamento.

Sobrescribe el método mostrar_info() para incluir el departamento."""


class Empleado:
    """Clase padre que le hereda sus atributos y métodos a las clases hijas"""

    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        """Método para mostrqr el comportamiento de los atribtos"""
        return f"El empleado {self.nombre} tiene un salario de ${self.salario:,.2f}"

    def metodo_exigido(self):
        """Creado para cumplir con los líneamientos de pylint"""


class Gerente(Empleado):
    """Sub clase que hereda de super clase empleado"""

    def __init__(self, nombre: str, salario: float, departamento: str):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        return (
            f"{super().mostrar_info()} y trabaja en departamento de {self.departamento}"
        )

    def aumento_salarial(self, comportamiento: str, aumento: float):
        """Genera un aumento salarial que depende del comportamiento del empleado"""
        if comportamiento == "Bueno":
            self.salario += aumento
            return f"Recibiste un aumento de ${aumento:,.2f} felicidades"
        return "No recibes ningun tipo de aumento"


gerente1 = Gerente("Luis F. González", 1500000, "Gerencia")
print(gerente1.mostrar_info())
print(gerente1.aumento_salarial("malo", 500000))
print(gerente1.aumento_salarial("Bueno", 250000))
print(gerente1.mostrar_info())
