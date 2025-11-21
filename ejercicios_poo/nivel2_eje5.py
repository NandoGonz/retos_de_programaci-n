"""5. Clase Vehiculo:

Subclases: Coche, Moto

Cada subclase tiene un método mostrar_tipo().

Usa super() para heredar atributos del padre.

Puedo crear mis propios atributos, basados en la calse"""


class Vehiculo:
    """Clase padre"""

    def __init__(self, modelo: str, marca: str, ano: int):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano


class Moto(Vehiculo):
    """Clase hija"""

    def __init__(self, modelo: str, marca: str, ano: int, tipo: str):
        super().__init__(modelo, marca, ano)
        self.tipo = tipo

    def mostrar_tipo_moto(self):
        """Métododo propio de la clase hija"""
        print(
            f"🏍️ La moto {self.modelo} de la marca {self.marca} del año {self.ano} es de tipo {self.tipo}"
        )


class Coche(Vehiculo):
    """Clase hija"""

    def __init__(self, modelo: str, marca: str, ano: int, n_puertas: int):
        super().__init__(modelo, marca, ano)
        self.n_puertas = n_puertas

    def mostrar_tipo_coche(self):
        """Métododo propio de la clase hija"""
        print(
            f"🚗 El coche {self.modelo} de la marca {self.marca} del año {self.ano} tiene {self.n_puertas} de puertas"
        )


moto1 = Moto("KLX", "kawasaki", 2000, "Enduro")
coche1 = Coche("Land crusier", "Toyota", 1996, 4)
moto1.mostrar_tipo_moto()
coche1.mostrar_tipo_coche()
