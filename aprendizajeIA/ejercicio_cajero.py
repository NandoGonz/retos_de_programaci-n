"""Simula un cajero en consola:

El usuario empieza con un saldo inicial de $1000.

El menú debe tener estas opciones:

1. Consultar saldo

2. Depositar dinero

3. Retirar dinero

0. Salir

Si intenta retirar más de lo que tiene → mostrar error.

El programa se repite hasta que elija 0

# ⚠️ Mejoras para el cajero

Modifica tu cajero automático para:

No permitir depósitos negativos.

No permitir retiros mayores al saldo.

Mostrar el historial de transacciones al salir (lista con los movimientos)."""

SALDO_INICIAL = 1000
movimientos = []
print("Bienvenido al cajero automático")
while True:
    print("#" * 20)
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar historial de transacciones")
    print("0. Salir")
    print("#" * 20)
    try:
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                print(f"💲Su saldo es: {SALDO_INICIAL:,.2f}")

            case 2:
                deposito = float(input("Ingrese la cantidad a depositar: "))
                if deposito > 0:
                    SALDO_INICIAL += deposito
                    print("✅ Transacción exitosa")
                    print(f"💲su saldo es: {SALDO_INICIAL:,.2f}")
                    movimientos.append(f"Se deposito la cantidad de $ {deposito:,.2f}")
                else:
                    print("⚠️ No se permite depositar cantidades negativas")

            case 3:
                retiro = float(input("Ingrese la cantidad a retirar: "))
                if retiro <= SALDO_INICIAL:
                    SALDO_INICIAL -= retiro
                    print("✅ Transacción exitosa")
                    print(f"💲Su saldo es: {SALDO_INICIAL:,.2f}")
                    movimientos.append(f"Se retiro la cantidad de $ {retiro:,.2f}")
                else:
                    print("⚠️ No tiene suficiente saldo para la transacción")

            case 4:
                if movimientos:
                    for m, transaccion in enumerate(movimientos):
                        print(f"Movimiento {m + 1} ----> {transaccion}")
                else:
                    print("⚠️ No se ha realizado ningun movimiento")

            case 0:
                print("📤 Saliendo del cajero")
                break
    except ValueError:
        print("Ingrese una de las opciones indicadas")
