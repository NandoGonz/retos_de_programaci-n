"""✅ 5. Biblioteca

Crear:

Libro

__titulo, __autor,__stock

Biblioteca

Lista de libros

Métodos:

agregar_libro()

prestar_libro()

devolver_libro()

buscar_libro()

📌 Práctica:

Encapsulamiento + listas + validaciones"""


class Libro:
    """Representa un libro con autor, título y stock."""

    def __init__(self, autor: str, titulo: str, stock: int):
        """Inicializa un objeto Libro con su autor, título y stock inicial."""
        self.__autor = autor
        self.__titulo = titulo
        self.__stock = stock

    def mostrar_autor(self):
        """Devuelve el autor del libro."""
        return self.__autor

    def mostrar_titulo(self):
        """Devuelve el título del libro."""
        return self.__titulo

    def mostrar_stock(self):
        """Devuelve el stock disponible del libro."""
        return self.__stock

    def devolver(self):
        """Incrementa el stock del libro en uno al ser devuelto."""
        self.__stock += 1

    def prestar(self):
        """Decrementa el stock en uno si hay libros disponibles para prestar."""
        if self.__stock <= 0:
            raise ValueError("La cantidad de stocks es insuficiente")
        self.__stock -= 1

    def mostrar_info(self):
        """Devuelve una cadena con la información completa del libro."""
        return f"Hay {self.__stock} disponibles del libro {self.__titulo} del autor {self.__autor}"


class Biblioteca:
    """Gestiona una colección de libros, permitiendo agregarlos, prestarlos y buscarlos."""

    def __init__(self):
        """Inicializa la biblioteca con una lista vacía de libros."""
        self.libros = []

    def agregar_libro(self, titulo: str, autor: str, stock: int):
        """Agrega un libro a la biblioteca o actualiza su stock si ya existe."""
        if titulo:
            for libro in self.libros:
                if libro.mostrar_titulo() == titulo:
                    # Si el libro ya existe, solo se actualiza el stock.
                    libro._Libro__stock += stock
                    # libro.agregar_stock(stock) forma correcta de agregar stock

                    return

        # Si no existe → crear nuevo
        nuevo = Libro(autor, titulo, stock)
        self.libros.append(nuevo)
        print("Libro agregado correctamente.")

    def prestar_libro(self, titulo: str):
        """Busca un libro por título y lo presta si hay stock disponible."""
        if titulo:
            for libro in self.libros:
                if libro.mostrar_titulo() == titulo:
                    try:
                        libro.prestar()
                        print("Libro prestado de forma exitosa")
                    except ValueError as e:
                        print(e)
                        return
            print("El libro no existe")

    def devolver_libro(self, titulo: str):
        """Busca un libro por título y registra su devolución incrementando el stock."""
        if titulo:
            for libro in self.libros:
                if libro.mostrar_titulo() == titulo:
                    libro.devolver()
                    print("Libro devuelto")
                    return
            print("El libro no existe")

    def buscar_libro(self, texto: str):
        """Busca libros cuyo título o autor coincidan con el texto de búsqueda."""
        # creamos una lista vacia para guardar los resultados
        resultados = []
        if texto:
            for libro in self.libros:
                if (
                    texto.lower() in libro.mostrar_titulo().lower()
                    or texto.lower() in libro.mostrar_autor().lower()
                ):
                    resultados.append(libro)
        if resultados:
            print("\nResultados encontrados")
            for libro in resultados:
                print(" -", libro.mostrar_info())
        else:
            print("No se encontro ninguna coincidencia")


biblio = Biblioteca()

biblio.agregar_libro("Harry Potter", "J.K. Rowling", 5)
biblio.agregar_libro("El Señor de los Anillos", "Tolkien", 3)
biblio.agregar_libro("Harry Potter", "J.K. Rowling", 2)  # actualiza stock

biblio.prestar_libro("Harry Potter")
biblio.devolver_libro("Harry Potter")

biblio.buscar_libro("har")  # búsqueda parcial
