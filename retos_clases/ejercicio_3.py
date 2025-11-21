""". Constructor con Validación
Crea una clase Libro cuyo constructor valide que el número de páginas y el precio no sean negativos.
Lanza un ValueError si no se cumple."""


class libro:
    def __init__(self, titulo: str, paginas: int = 100, precio: float = 0.0):
        if paginas < 0 or precio < 0:
            raise ValueError("Las páginas y el precio no pueden ser negativos")
        self.titulo = titulo
        self.paginas = paginas
        self.precio = precio

    def mostrar_info(self):
        return f"El libro {self.titulo} tiene {self.paginas} páginas y tiene un precio de ${self.precio}"


libro1 = libro("cualquiera", 45, 500)
print(libro1.mostrar_info())
print()
libro2 = libro("random")
print(f"Titulo {libro2.titulo} | Páginas {libro2.paginas} | Precio ${libro2.precio}")
