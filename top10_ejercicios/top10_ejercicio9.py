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
    """
    Clase base que representa un producto genérico.
    Define la estructura básica y el comportamiento por defecto para el cálculo de precios.
    """

    def __init__(self, nombre: str, precio: float):
        """
        Inicializa un nuevo producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio unitario del producto.
        """
        self.nombre = nombre
        self.precio = precio

    def calcular_precio(self, cantidad: int) -> float:
        """
        Calcula el precio total para una cantidad dada.

        Args:
            cantidad (int): Número de unidades.

        Returns:
            float: El precio total sin descuentos especiales.
        """
        return self.precio * cantidad


class Normal(Producto):
    """
    Representa un producto normal que no tiene reglas de descuento especiales.
    Hereda de Producto.
    """

    def calcular_precio(self, cantidad: int) -> float:
        """Calcula el precio usando la lógica estándar de la clase padre."""
        return super().calcular_precio(cantidad)


class ConDescuento(Producto):
    """
    Representa un producto que puede tener descuento dependiendo de la cantidad comprada.
    """

    def calcular_precio(self, cantidad: int) -> float:
        """
        Calcula el precio total aplicando un 5% de descuento si la cantidad
        es mayor a 5 y menor o igual a 10.
        """
        total = self.precio * cantidad
        if 5 < cantidad <= 10:
            return total * 0.95
        return total


class Especial(Producto):
    """
    Representa un producto especial con un descuento significativo por volumen alto.
    """

    def calcular_precio(self, cantidad: int) -> float:
        """
        Calcula el precio total aplicando un 50% de descuento si la cantidad es mayor a 10.
        """
        total = self.precio * cantidad
        if cantidad > 10:
            return total * 0.50
        return total


class Carrito:
    """
    Gestiona una colección de productos y calcula el total de la compra.
    """

    def __init__(self):
        """Inicializa un carrito de compras vacío."""
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto y la cantidad deseada al carrito.

        Args:
            producto (Producto): Instancia de Producto (o sus subclases).
            cantidad (int): Cantidad de unidades a comprar.
        """
        self.productos.append((producto, cantidad))

    def pago_total(self):
        """
        Calcula el total a pagar sumando el precio de cada producto en el carrito.
        Utiliza polimorfismo para llamar al método calcular_precio específico de cada tipo de producto.

        Returns:
            float: El monto total de la compra.
        """
        total = 0
        for producto, cantidad in self.productos:
            total += producto.calcular_precio(cantidad)
        return total


compra = Carrito()
compra.agregar_producto(Especial("pera", 4500), 4)
compra.agregar_producto(Normal("ajo", 500), 5)
compra.agregar_producto(ConDescuento("smartPhone", 15000), 6)
print(f"Total a pagar: ${compra.pago_total():,.2f}")
