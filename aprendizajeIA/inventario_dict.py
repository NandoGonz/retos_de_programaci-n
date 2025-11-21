"""2. Diccionario de inventario
Crea un diccionario que guarda productos y sus cantidades.

Función para agregar un producto (clave: nombre, valor: cantidad).

Si el producto ya existe, suma al stock.

Si la cantidad es negativa, lanza un error.

Mostrar todo el inventario."""

from prettytable import PrettyTable

inventario = {}


def agregar_producto(nombre, valor):
    inventario[nombre] = valor
    if nombre in inventario:
        inventario[nombre] = valor + valor
        print("✅ Producto agregado con exito")

    try:
        if valor < 0:
            raise ValueError("⚠️  El valor no puede ser negativo ")
    except ValueError as e:
        print(e)


while True:
    validar = input("Escriba 'salir' para salir o enter para continuar: ")
    if validar == "salir":
        print("📤 Saliendo del inventario...")
        break
    n_producto = input("Ingrese el nombre del producto: ")
    v_producto = int(input("Ingrese la cantidad del producto: "))
    agregar_producto(n_producto, v_producto)
print(inventario)

table = PrettyTable()
table.title = "Inventario de productos"
table.field_names = ["Nombre", "Cantidad"]

for p, v in inventario.items():
    table.add_row([p, v])
    table.add_divider()
print(table)
