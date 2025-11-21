"""7. Clase Inventario:

Usa un diccionario para guardar productos y cantidades.

Métodos: agregar_producto(), mostrar_inventario(), buscar_producto()."""

from prettytable import PrettyTable


class Inventario:
    """Clase padre"""

    def __init__(self):
        self.stock = {}
        self.menu()

    def agregar_prodcutos(self):
        """Método para agregar un producto y la cantidad al inventario"""
        nombre = input("Ingrese el nombre del producto: ").title()
        cantidades = int(input("Ingrese la cantidad del producto: "))

        if nombre not in self.stock:
            self.stock[nombre] = cantidades
            print("✅ Producto agregado con exito")
        else:
            self.stock[nombre] += cantidades
            print("⚠️ El prodcuto ya existe, ✅ se agrego la nueva cantidad")

    def mostrar_inventario(self):
        """Método que muestra los productos y sus cantidades en inventario"""
        tabla = PrettyTable()
        tabla.title = "Productos en inventario"
        tabla.field_names = ["Nombre", "Cantidad"]

        for n, p in self.stock.items():
            tabla.add_row([n, p])
            tabla.add_divider()
        print(tabla)

    def buscar_producto(self):
        """Método para buscar los productos de manera individual"""
        nombre = str(input("Ingrese el nombre del producto a buscar: ")).title()

        if nombre in self.stock:
            print(f"✅ Producto {nombre} --> Cantidad {self.stock[nombre]}")
        else:
            print("⚠️ El producto no existe en el inventario")

    def menu(self):
        """Método que muestra las opciones del inventrio"""

        while True:
            print("\n Bienvenido al menú de su inventario")
            print("1. Agregar producto")
            print("2. Mostrar inventario")
            print("3. Buscar producto")
            print("0. Salir")
            try:
                opcion = int(input("Ingrese una opción: "))
                match opcion:
                    case 1:
                        self.agregar_prodcutos()
                    case 2:
                        self.mostrar_inventario()
                    case 3:
                        self.buscar_producto()
                    case 0:
                        print("📤 Saliendo del inventario")
                        break

            except ValueError:
                print("⚠️ Dígite una opción valida o un valor númerico ")


invent = Inventario()
"""invent.agregar_prodcutos("Manzana", 10)
invent.agregar_prodcutos("Pera", 5)
invent.mostrar_inventario()
invent.buscar_producto("Manzana")
invent.buscar_producto("Pera")"""
