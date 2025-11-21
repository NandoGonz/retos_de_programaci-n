"""
🔹 Ejercicio 6 – Sistema bancario (intermedio)

Defina una clase base Cuenta con métodos abstractos depositar()y retirar().
Crea dos clases hijas:

CuentaAhorros

CuentaCorriente
Ambas deben implementar las funciones, pero con condiciones distintas (por ejemplo, límites de retiro).
"""

from abc import abstractmethod, ABC


class Cuenta(ABC):

    @abstractmethod
    def depositar(self):
        return None

    @abstractmethod
    def retirar(self):
        return None


class CuentaAhorros(Cuenta):
    def __init__(self, cantidad: float) -> None:
        super().__init__()
        self.cantidad = cantidad

    def depositar(self):
        try:
            monto = float(input("Ingrese la cantidada a depositar: $"))
            if monto < 0:
                raise ValueError(
                    "El monto debe ser positivo para realizar la transacción"
                )
            self.cantidad += monto
            return self.cantidad
        except ValueError as e:
            print(e)

    def retirar(self):
        try:
            monto = float(input("Ingrese la canitdad a retirar: $"))
            if monto > float(1200000):
                raise ValueError(
                    "El monsto excede el límite permitido para esta transacción"
                )
            self.cantidad -= monto
            return self.cantidad
        except ValueError as e:
            print(e)


class CuentaCorriente(Cuenta):
    def __init__(self, cantidad: float) -> None:
        super().__init__()
        self.cantidad = cantidad

    def depositar(self):
        try:
            monto = float(input("Ingrese la cantidad a depositar: $ "))
            if monto > float(1500000):
                raise ValueError("La cantidad excede el límite establecido")
            self.cantidad += monto
            return self.cantidad
        except ValueError as e:
            print(e)

    def retirar(self):
        try:
            monto = float(input("Ingrese la cantidad a retirar: $ "))
            if monto < 1000000:
                raise ValueError("El monto es inferior al limite establecido")
            self.cantidad -= monto
            return self.cantidad
        except ValueError as e:
            print(e)


c_ahorro = CuentaAhorros(3200000)
print(c_ahorro.depositar())
print(c_ahorro.retirar())

c_corriente = CuentaCorriente(5000000)
print(c_corriente.depositar())
print(c_corriente.retirar())
