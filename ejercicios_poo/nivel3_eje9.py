"""9. Clase Calculadora:

Métodos: sumar(), restar(), dividir(), multiplicar().

Usa try/except para evitar división entre cero."""


class Calculadora:
    def __init__(self):
        self.menu()

    def sumar(self):
        num1 = float(input("ingrese un número: "))
        num2 = float(input("ingrese un número: "))
        resultado = num1 + num2
        print(f"El valor de la suma es {resultado}")

    def restar(self):
        num1 = float(input("ingrese un número: "))
        num2 = float(input("ingrese un número: "))
        resultado = num1 - num2
        print(f"El valor de la resta es {resultado}")

    def multiplicar(self):
        num1 = float(input("ingrese un número: "))
        num2 = float(input("ingrese un número: "))
        resultado = num1 * num2
        print(f"El valor de la multiplicación es {resultado}")

    def dividir(self):
        num1 = float(input("ingrese un número: "))
        num2 = float(input("ingrese un número: "))
        try:
            resultado = num1 / num2
            print(f"El valor de la división es {resultado}")
        except ZeroDivisionError:
            print("La operación no se ejecuto, no se pude dividir por cero")

    def menu(self):
        while True:
            print("\n Bienvenido al menú de la Calculadora")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("0. Salir")

            try:
                opcion = int(input("Ingrese una opción: "))
                match opcion:
                    case 1:
                        self.sumar()
                    case 2:
                        self.restar()
                    case 3:
                        self.multiplicar()
                    case 4:
                        self.dividir()
                    case 0:
                        print("📤 Saliendo de la Calculadora")
                        break
            except ValueError:
                print("Ingrese una opción valida o un valor númerico")


calculadora = Calculadora()
