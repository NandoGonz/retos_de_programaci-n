"""3. Clase Producto:

Atributos: nombre, precio,stock

Métodos: actualizar_stock(),cambiar_precio()

Usa abs() para manejar reducciones de stock y try/except para validar precios."""


class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def cambiar_precio(self, n_preico: float):
        try:
            if n_preico < 0:
                raise ValueError("El precio debe ser mayor a 0 para ser modificado")
            self.precio = n_preico
            print(f"Precio actualizado el nuevo precio es {n_preico}")
        except ValueError as e:
            print(e)

    def actualizar_stock(self, cantidad: int):
        if cantidad > 0:
            self.stock += cantidad
            print(
                f"Stock actulizado la nueva cantidad es {self.stock} se sumaron {cantidad}"
            )
        elif cantidad < 0:
            if abs(cantidad) < self.stock:
                self.stock += cantidad
                print(
                    f"Stock actulizado la nueva cantidad es {self.stock} se restaron {-cantidad}"
                )
            else:
                print(
                    f"La cantidad {-cantidad} es mayor al stock disponibe {self.stock}"
                )
        else:
            print("Error al momento de actulizar, debe verificar")

    def mostrar_info(self):
        print(
            f"Producto {self.nombre} | Cantidad {self.stock} | Precio $ {self.precio}"
        )


prod = Producto("Pera", 4500, 10)
prod.cambiar_precio(4000)
prod.actualizar_stock(9)
prod.cambiar_precio(-5000)
prod.actualizar_stock(-9)
prod.actualizar_stock(-12)
prod.mostrar_info()
