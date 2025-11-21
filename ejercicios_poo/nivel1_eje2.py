"""2. Clase CuentaBancaria:

Atributo privado: __saldo

Métodos: depositar(), retirar(),mostrar_saldo()

Usa try/except si el retiro es mayor que el saldo."""


class CuentaBancaria:
    def __init__(self, saldo: float):
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(f"Su saldo es de {self.__saldo}")

    def deposiar(self, cantidad: float):
        try:
            if cantidad < 0:
                raise ValueError("La cantidad debe ser mayor a 0")
            self.__saldo += cantidad
            print(f"Deposito de {cantidad} exitoso")
        except ValueError as e:
            print(e)

    def retirar(self, cantidad: float):
        try:
            if abs(cantidad) >= self.__saldo:
                raise ValueError(
                    "La cantidad a retirar deber ser menor o igual al saldo"
                )
            self.__saldo -= cantidad
            print(f"Retiro realizado con exito {cantidad}")
        except ValueError as e:
            print(e)


c1 = CuentaBancaria(50000)
c1.deposiar(100)
c1.deposiar(-50)
c1.retirar(200)
c1.retirar(60000)
c1.mostrar_saldo()
