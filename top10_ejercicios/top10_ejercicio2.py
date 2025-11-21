"""✅ 2. Control de inventario con Productos

Clase Producto:

__nombre, __precio,__stock

Método vender(cantidad)→ valida stock

Método comprar(cantidad)

Propiedad solo lectura para precio

📌 Práctica:

Encapsulamiento + métodos + propiedades"""


class Producto:
    """Clase padre, con atributos privados"""

    def __init__(self, nombre: str, precio: float, stock: int):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def leer_precio(self):
        """Método para mostrar el precio del producto"""
        return self.__precio

    def vender(self, cantidad: int):
        """Método encargado de contrloar las ventas"""
        try:
            if cantidad > self.__stock:
                raise ValueError(
                    "⚠️ Cantidad ingresada debe ser menor o igual al stock en venta"
                )
            if cantidad <= 0:
                raise ValueError(
                    "La cantidad debe ser mayor a cero, para ejecutar la venta"
                )
            self.__stock -= cantidad
            print(f"Se vendio la cantidad de {cantidad} del producto {self.__nombre}")
        except ValueError as e:
            print(e)

    def comprar(self, cantidad: int):
        """Método encargado de registrar la compra de stocks existentes y nuevos"""
        try:
            if cantidad <= 0:
                raise ValueError("⚠️ La cantidad ingresada debe ser positiva")
            self.__stock += cantidad
            print(f"Stock {self.__nombre} actulizado nueva cantidad {self.__stock}")
        except ValueError as e:
            print(e)


p1 = Producto("Manzana", 1900, 10)
p1.vender(5)
p1.comprar(10)
print(p1.leer_precio)

print("\n")
print("Nuevo producto")
p2 = Producto("Pera", 1800, 10)
p2.vender(11)
p2.comprar(-9)
print(p2.leer_precio)
