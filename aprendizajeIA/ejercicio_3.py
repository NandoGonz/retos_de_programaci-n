"""Inventario de Productos

Crea una clase Producto con atributos nombre (str), precio (float) y stock (int).

Agrega métodos:

mostrar_info() → devuelve un string.

actualizar_stock(cantidad: int) → modifica el stock.

Crea una lista de productos y simula ventas y reposiciones."""


class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad: int):
        if cantidad > 0:
            self.stock += cantidad
            print(
                f"✅ Se agregaron {cantidad} unidades. Stock actualizado: {self.stock}"
            )
        elif cantidad < 0:
            if abs(cantidad) <= self.stock:
                self.stock += cantidad  # cantidad es negativa, entonces resta
                print(
                    f"🛒 Se vendieron {-cantidad} unidades. Stock actualizado: {self.stock}"
                )
            else:
                print(f"⚠️ No hay suficiente stock de {self.nombre} para la venta.")
        else:
            print("ℹ️ No se actualizó el stock.")
        return self.stock

    def mostrar_info(self):
        return f"Nombre {self.nombre} | Precio $ {self.precio} | Stock {self.stock}"


p1 = Producto("manzana", 1500, 8)
p2 = Producto("pera", 2000, 10)
p3 = Producto("uva", 1000, 18)

productos = [p1, p2, p3]

for producto in productos:
    print(f"\n📦 {producto.mostrar_info()}")
    producto.actualizar_stock(5)  # agregar stock
    producto.actualizar_stock(-6)  # vender
    producto.actualizar_stock(-20)  # prueba de venta mayor al stock
