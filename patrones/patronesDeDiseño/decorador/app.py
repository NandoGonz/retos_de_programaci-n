"""Un decorador en Python
es una función que toma otra función como argumento, añade funcionalidad a ella y devuelve una nueva función modificada sin cambiar su código original. Se aplican directamente sobre la definición de la función usando el símbolo @ y permiten agregar características como el registro (logging), la medición del tiempo de ejecución o la autenticación de manera reutilizable
"""


class Cafe:
    def costo(self):
        return 5


# # Creamos la clase que sera utilizada como decorador para modidicar a la clase padre
class DecoradorCafe:
    def __init__(self, cafe):
        self._cafe = cafe

    def costo(self):
        return (
            self._cafe.costo()
        )  # esta forma de retornar en mi método hara las veces de decorador


# Implementamos el decorador con otra clase
class ConLeche(DecoradorCafe):
    def costo(self):
        return (
            super().costo() + 2
        )  # Co mo nuestro objetivo es aumentar el costo al decorador le sumaremos dos y así sucesivamente


class ConChocolate(DecoradorCafe):
    def costo(self):
        return super().costo() + 3


class AnadirAzucar(DecoradorCafe):
    def costo(self):
        return super().costo() + 1


# Instanciamos nuestros cafes
cafe = Cafe()
print(f"Cafe sencillo tiene un valor de $ {cafe.costo()}")

cafe = ConLeche(cafe)
print(f"El cafe con leche tiene un valor de $ {cafe.costo()}")

cafe = ConChocolate(cafe)
print(f"El cafe con chocolate tiene un coste de $ {cafe.costo()}")

cafe = AnadirAzucar(cafe)
print(f"El cafe con azucar tiene un valor de {cafe.costo()}")
