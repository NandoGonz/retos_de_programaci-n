"""🔹 Ejercicio 1 – Encapsulamiento básico

Crea una clase CuentaBancariacon atributos privados: __titular, __saldo.
Implementar métodos:

depositar(monto)

retirar(monto)

mostrar_saldo()
Valida que no se puedan hacer depósitos o retiros negativos."""


class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, monto: float):
        if monto >= 0:
            self.__saldo += monto
            print("Deposito realizado de forma correcta")
        else:
            print("No se pueden hacer depositos menores a cero")

    def retirar(self, monto):
        if monto < 0:
            print("El monto debe ser mayor a cero")
        elif monto < self.__saldo:
            self.__saldo -= monto
            print("Retiro realizado con exito")
        else:
            print("El monto no puede ser mayor al saldo")
            return self.__saldo

    def mostrar_saldo(self):
        return f"El señor {self.__titular} tiene un saldo de ${self.__saldo:,.2f} pesos"


cuenta1 = CuentaBancaria("Jose", 5000)
cuenta1.depositar(500)
cuenta1.depositar(-500)
cuenta1.retirar(450)
cuenta1.retirar(-450)
cuenta1.retirar(6000)
print(cuenta1.mostrar_saldo())
