"""10. Clase ArchivoTexto:

Métodos: guardar_texto(), leer_texto().

Usa manejo de archivos con with open() y captura errores de lectura/escritura."""


class ArchivoTexto:
    def __init__(self, nom_archivo: str):
        self.nom_archivo = nom_archivo

    def guardar_texto(self, texto: str):
        try:
            with open(self.nom_archivo, "w", encoding="UTF-8") as archivo:
                archivo.write(texto)
            print(f"Texto guardado de forma exitosa\n {self.nom_archivo}")
        except FileNotFoundError:
            print(f"El archivo {self.nom_archivo} no existe")
        except OSError:
            print(f"[ERROR] al ingresar al archivo {self.nom_archivo}")

    def leer_texto(self):
        try:
            with open(self.nom_archivo, "r", encoding="UTF_8") as archivo:
                contenido = archivo.read()
                print("Mostrando el contenido del texto. \n")
                print(contenido)
        except PermissionError:
            print("No tienes permisos para leer este texto")
        except OSError:
            print("[ERROR] algo salio mal")

    def agregar_texto(self, texto: str):
        try:
            with open(self.nom_archivo, "a", encoding="UTF-8") as archivo:
                archivo.write("\n")
                archivo.write(texto)
        except PermissionError:
            print("No tienes permiso para editar este archivo")
        except OSError:
            print("[ERROR] algo salio mal")


texto1 = ArchivoTexto("Primer oop con texto plano")
texto1.guardar_texto(
    "A veces para avanzar hay que ser pacientes y sobre todo hacer un esfuerzo \n para adquirir y dominar los conocimientos que queremos "
)
texto1.agregar_texto(
    "No tengas miedo al fracaso, ya notaste que va de la mano con el progreso"
)
texto1.leer_texto()
