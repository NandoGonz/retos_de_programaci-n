"""Crea una clase Producto con atributos nombre (público), _stock (protegido) y __precio (privado).
Implementa métodos para vender y reponer stock."""


class Producto:
    def __init__(self, nombre: str, stock: int, precio: float):
        self.nombre = nombre
        self._stock = stock
        self.__precio = precio

    def venta(self, cantidad: int):
        if self._stock >= cantidad:
            self._stock -= cantidad

    def reponer_stock(self, cantidad: int):
        self._stock += cantidad

    def estado_stock(self):
        print(
            f"{self.nombre} --> stock: {self._stock} --> precio unitario: {self.__precio} "
        )


p1 = Producto("Coco", 6, 2500)
p1.venta(3)
p1.reponer_stock(2)
print(p1.estado_stock())
