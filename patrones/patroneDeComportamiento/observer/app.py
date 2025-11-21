"""El patrón de diseño Observer en Python
define una relación de dependencia uno a muchos entre objetos, donde un objeto (sujeto) notifica a otros objetos (observadores) sobre los cambios en su estado. Los observadores se suscriben al sujeto para recibir notificaciones automáticas y, al cambiar el estado del sujeto, se actualizan todos los observadores suscritos sin que el sujeto necesite conocer sus implementaciones concretas
"""


class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self._precio = precio
        self._subscriptores = []

    def subscrubir(self, cliente):
        self._subscriptores.append(cliente)

    def notificar(self):
        for cliente in self._subscriptores:
            cliente.actualizar(self.nombre, self._precio)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, n_precio):
        if n_precio < self._precio:
            print(
                f"El producto {self.nombre} bajo del precio {self._precio} a {n_precio}"
            )
            self._precio = n_precio
            self.notificar()
        else:
            self._precio = n_precio


class Cliente:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def actualizar(self, producto: str, n_precio: float):
        print(f"{self.nombre} fue notificado")


laptop = Producto("Laptp Gamer", 1200)
cliente1 = Cliente("juan")
cliente2 = Cliente("Luis")

laptop.subscrubir(cliente1)
laptop.subscrubir(cliente2)


laptop.precio = 1100
