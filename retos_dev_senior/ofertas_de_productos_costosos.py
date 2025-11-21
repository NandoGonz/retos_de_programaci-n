"""✅ 9. Ofertas por productos costosos
En una tienda se registran los precios de 7 productos. Si el precio de un producto es mayor a $1.000.000, mostrar "Producto de lujo". Al final, indicar cuántos productos fueron clasificados como lujo.
"""

productos = []
productoLujo = []
PRECIO_DE_LUJO = 1000000


def prodcutosLujo():
    for producto in range(3):
        nombre = input("nombre del producto: ")
        precio_del_producto = float(input("ingrese el valor del producto: "))
        productos.append({"nombre": nombre, "precio": precio_del_producto})

        producto_de_lujo = [
            producto["nombre"]
            for producto in productos
            if producto["precio"] > PRECIO_DE_LUJO
        ]

    if producto_de_lujo:
        print("\n prodcutos de lujo")
    for producto in producto_de_lujo:
        print(f"es un producto de lujo --> {producto}")

    productoLujo.append(producto_de_lujo)
    print(productos)
    print(f"prodcutos de lujo --> {productoLujo}")


if __name__ == "__main__":
    prodcutosLujo()
