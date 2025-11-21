"""✅ 2. Inventario de productos
Solicita al usuario ingresar el nombre y cantidad en stock de 10 productos de una tienda.
Si la cantidad es menor a 5 unidades, muestra una alerta de bajo inventario."""

from prettytable import PrettyTable

productos = []
productos_a_vender = int(input("ingrese la cantidad de productos a vender: "))
for producto in range(productos_a_vender):
    print(f"\n ingresa el valor del producto-->{producto+1}")
    nombre_del_producto = input("ingrese el nombre del producto: ")
    cantidad_del_producto = int(input("ingrese la cantidad del producto: "))
    unidades_minimas = 5
    productos.append(
        {
            "nombre": nombre_del_producto,
            "cantidad": cantidad_del_producto,
            "unidades-minima": unidades_minimas,
        }
    )

productos_a_reabastecer = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] < producto["unidades-minima"]
]

if productos_a_reabastecer:
    print("\nProductos que necesitan reabastecimiento:")
    for producto in productos_a_reabastecer:
        print(f" !ALERTA¡ se debe reestablecer el siguiente producto-->{producto}")
else:
    print("\nNo hay productos que necesiten reabastecimiento en este momento.")

tabla = PrettyTable()
tabla.field_names = ["nombre", "cantidad"]


for p in productos:
    tabla.add_row([p["nombre"], p["cantidad"]])
    tabla.add_divider()

print(tabla)
