"""Crea una clase Cuenta con:

Atributo privado __saldo inicializado en 0.

Métodos:

depositar(monto) → aumenta el saldo si es positivo.

retirar(monto) → disminuye el saldo si hay suficiente dinero.

mostrar_saldo() → retorna el saldo actual."""


class Cuenta:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, monto: float):
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito realizado con exito nuevo saldo $ {self.__saldo}")
        else:
            print("⚠️  El monto no puede ser negativo")

    def retirar(self, monto):
        """Uso en tu clase Cuenta Modifica el método retirar() para que use try/except y lance un error personalizado si el monto es mayor al saldo."""
        try:
            if monto > self.__saldo:
                raise ValueError(
                    f"⚠️ el monto debe ser menor al saldo disponible monto ${monto} saldo disponible ${self.__saldo} "
                )
            elif monto <= self.__saldo:
                self.__saldo -= monto
                print(f"✅  Retiro realizado con exito $ {monto}")
        except ValueError as e:
            print(e)

    def mostrar_saldo(self):
        return self.__saldo


cuenta1 = Cuenta()
cuenta1.depositar(50000)
cuenta1.retirar(25000)
cuenta1.depositar(-700)
cuenta1.retirar(30000)
print(f"El saldo disponible es {cuenta1.mostrar_saldo()}")
