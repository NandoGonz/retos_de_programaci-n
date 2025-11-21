"""Crea una clase Producto con:

Atributos:

nombre (público).

__precio (privado).

__stock (privado).

Métodos:

actualizar_stock(cantidad) → suma/resta al stock.

cambiar_precio(nuevo_precio) → cambia el precio si es positivo.

mostrar_info() → retorna nombre, precio y stock."""


class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def actualizar_stock(self, cantidad: int):
        if cantidad:
            if cantidad > 0:
                self.__stock += cantidad
                print(f"✅ Stock actulizado se agrego la cantidad de {cantidad} stocks")
            elif cantidad < 0:
                self.__stock -= abs(cantidad)
                print(f"✅ Stock actulizado se resto la cantidad de {abs(cantidad)}")

    def cambiar_precio(self, nuevo_precio):
        try:
            self.__precio = float(nuevo_precio)
            if nuevo_precio > 0:
                print(f"✅ Precio del stock modificado {nuevo_precio}")
            else:
                print("⚠️ El precio debe ser positivo")
        except ValueError:
            print(f"⚠️ El valor debe ser numérico, el valor ingresado es {nuevo_precio}")

    def mostrar_info(self):
        return f"📦 El producto {self.nombre} | tiene un valor de $ {self.__precio} | cuenta con {self.__stock} en stock"


p1 = Producto("Manzana", 1500, 10)
p1.actualizar_stock(-9)
p1.actualizar_stock(6)
p1.cambiar_precio(1200)
p1.cambiar_precio("dos mil")
print(p1.mostrar_info())
