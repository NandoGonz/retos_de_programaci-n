"""Crea una clase Cuenta con un atributo privado __saldo.
Implementa métodos para depositar y retirar dinero,
validando que el saldo nunca sea negativo."""


class Cuenta:
    def __init__(self, saldo: float):

        self.__saldo = saldo

    def depositar(self, monto: float):
        if self.__saldo > 0:
            self.__saldo += monto

    def retirar(self, monto: float):
        if self.__saldo <= 0:
            self.__saldo -= monto

    def mostrar_saldo(self):
        if self.__saldo > 0:
            return f"El saldo disponible es {self.__saldo}"


c1 = Cuenta(5000)
c1.depositar(500)
c1.retirar(450)
print(c1.mostrar_saldo())
c1.retirar(6000)
print(c1.mostrar_saldo())


