"""✅ 9. Carrito de compras

Clases:

Producto: nombre, precio

Carrito: lista de productos

agregar_producto()

total()

Crea 3 tipos de productos:

Normal

Con descuento

especial

Aplicación polimorfismo → cada uno calcula su precio final diferente"""


class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio(self, cantidad: int) -> float:
        return self.precio * cantidad


class Normal(Producto):
    def calcular_precio(self, cantidad: int) -> float:
        return super().calcular_precio(cantidad)


class ConDescuento(Producto):
    def calcular_precio(self, cantidad: int) -> float:
        total = self.precio * cantidad
        if 5 < cantidad <= 10:
            return total * 0.95
        return total


class Especial(Producto):
    def calcular_precio(self, cantidad: int) -> float:
        total = self.precio * cantidad
        if cantidad > 10:
            return total * 0.50
        return total


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def pago_total(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.calcular_precio(cantidad)
        return total


compra = Carrito()
compra.agregar_producto(Especial("pera", 4500), 4)
compra.agregar_producto(Normal("ajo", 500), 5)
compra.agregar_producto(ConDescuento("smartPhone", 15000), 6)
print(f"Total a pagar: ${compra.pago_total():,.2f}")
