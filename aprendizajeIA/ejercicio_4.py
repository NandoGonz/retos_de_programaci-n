import tkinter as tk

"""Banco (POO + Listas de Objetos)

Clase CuentaBancaria con atributos titular (str) y saldo (float).

Métodos: depositar(monto: float), retirar(monto: float), mostrar_saldo() -> str.

Crea 3 cuentas y guárdalas en una lista.

Haz depósitos y retiros recorriendo la lista con un bucle"""


"""class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto: float):
        if monto > 0:
            self.saldo += monto
        print(f"✅ Transacción realizada con exito su saldo es ${self.saldo:,.2f}")
        print(monto)

    def retirar(self, monto: float):
        if monto > self.saldo:
            print("❌ Saldo insuficiente para realizar el retiro")
        elif monto > 0:
            self.saldo -= monto
            print(f"✅ Retiro de realizado correctamente ${monto:,.2f}")
        return self.saldo

    def mostrar_saldo(self) -> str:
        return f"Su saldo actual es de: ${self.saldo:,.2f}"


cuenta1 = CuentaBancaria("Nando", 500000)
cuent2 = CuentaBancaria("Kristina", 340000)
cuenta3 = CuentaBancaria("Adriana", 700000)

cuentas = [cuenta1, cuent2, cuenta3]

for cuenta in cuentas:
    cuenta.depositar(500)
    cuenta.retirar(1000)
    cuenta.retirar(500)
    cuenta.retirar(1000000)
    print(cuenta.mostrar_saldo())"""

ventana = tk.Tk()
ventana.title("Cajero el amigo")



ventana.mainloop()
