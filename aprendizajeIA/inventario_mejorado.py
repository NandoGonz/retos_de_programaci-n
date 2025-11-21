"""Crea una clase Producto con atributos: nombre, precio, stock.

Haz una lista con varios productos.

Permite vender (restar stock).

Permite reponer (sumar stock).

Muestra el inventario completo después de cada operación"""


class Producto:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
        self.list = []

    def vender(self, amount: int):
        # if amount:
        if amount <= self.stock:
            self.stock -= amount
            total = self.price * amount
            print(
                f"Se vendieron {amount} de {self.name} por el precio de ${total:,.2f}"
            )
            self.list.append(
                f"Se vendieron {amount} {self.name} por el precio de {self.price:,.2f}"
            )
        else:
            print("No hay suficientes stocks para realizar la venta")

    def reponer(self, amount: int):
        if amount > 0:
            self.stock += amount
            print("Se repuso el stock de forma correcta")
            self.list.append(
                f"Se agrego la cantidad de {amount} al producto {self.name} hay una cantidad de {self.stock}"
            )
        else:
            print("La cantidad a reponer no puede ser negativa")

    def mostrar_inventario(self):
        if self.list:
            return "\n".join(self.list)
        else:
            return "El inventario está vacío"


p1 = Producto("pera", 2500, 0)
p1.vender(10)
p1.reponer(-8)
p1.mostrar_inventario()


p2 = Producto("sandia", 4500, 30)
p2.vender(10)
p2.reponer(8)
p2.mostrar_inventario()

p3 = Producto("manzana", 1500, 15)
p3.vender(10)
p3.reponer(5)
p3.mostrar_inventario()


print("#" * 25)
print(p1.mostrar_inventario())
print(p2.mostrar_inventario())
print(p3.mostrar_inventario())
print("#" * 25)
