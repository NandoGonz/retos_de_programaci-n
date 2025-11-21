"""Crea una clase Cuenta con un atributo privado __saldo.
Implementa métodos para depositar y retirar dinero,
validando que el saldo nunca sea negativo."""


class Cuenta:
    def __init__(self, saldo: float):

        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, monto):
        if monto >= 0:
            self.__saldo += monto


cuenta = Cuenta(5000)
print(cuenta.saldo)
cuenta.saldo = -60
print(cuenta.saldo)
