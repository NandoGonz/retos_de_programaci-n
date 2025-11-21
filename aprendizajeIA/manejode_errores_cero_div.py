"""1 Manejo de división entre cero
Crea una función que pida dos números y muestre la división, manejando el error si el divisor es cero.
"""


def dividir(num_1: float, num_2: float):
    try:
        resultado = num_1 / num_2
        return resultado
    except ZeroDivisionError:
        print("⚠️  No se puede realizar una división por cero")

    finally:
        print("✅ División terminada")


print(dividir(15, 0))  # Imprime la exceoción que hemos establecido
print("#" * 60)
print(dividir(15, 5))
