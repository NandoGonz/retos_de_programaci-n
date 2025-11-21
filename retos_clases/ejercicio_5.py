"""10. Lista de Objetos
Crea una lista de objetos Producto y muestra el nombre de todos los productos cuyo stock sea mayor a 0.
"""


class Producto:
    def __init__(self, articulo: str, cantidad: int):
        self.articulo = articulo
        self.cantidad = cantidad


productos = [Producto("mango", 7), Producto("uva", 9), Producto("manzana", 0)]
for p in productos:
    if p.cantidad > 0:
        print(p.articulo)
