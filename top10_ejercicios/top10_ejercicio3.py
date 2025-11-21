from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, salario):
        self.salario = salario

    @abstractmethod
    def calcular_pago(self):
        pass


class EmpleadoFijo(Empleado):
    def calcular_pago(self):
        return self.salario


class EmpleadoPorHora(Empleado):
    def __init__(self, salario_hora, horas_trabajadas):
        super().__init__(salario_hora)
        self.horas = horas_trabajadas

    def calcular_pago(self):
        return self.salario * self.horas


# Lista de empleados
empleados = [
    EmpleadoFijo(2000000),
    EmpleadoPorHora(150000, 8),
    EmpleadoPorHora(45000, 5),
]

# Cálculo individual + nómina total
nomina_total = 0

for empleado in empleados:
    pago = empleado.calcular_pago()
    print(f"Pago empleado: ${pago:,.2f}")
    nomina_total += pago

print("\nNómina total:")
print(f"${nomina_total:,.2f}")
