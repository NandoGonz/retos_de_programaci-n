"""✅ 6. Sistema de Archivos

Clase ArchivoTexto:

guardar(texto)

leer()

append(texto)

Maneja -:

Error de archivo no encontrado

Error de permisos

OSError

📌 Práctica:

con open() + excepciones"""


class ArchivoTexto:
    def __init__(self, n_texto: str):
        self.n_texto = n_texto

    def leer(self):
        try:
            with open(self.n_texto, "r", encoding="UTF-8") as archivo:
                contenido = archivo.read()
                print("\n")
                print("Mostrando el texto")
                print(contenido)
        except FileNotFoundError:
            print(f"No hay permisos para leer el archivo {self.n_texto}")
        except OSError:
            print("[ERROR] Al ingresar al archivo")

    def agregar_texto(self, texto: str):
        try:
            with open(self.n_texto, "a", encoding="UTF-8") as archivo:
                archivo.write("\n")
                archivo.write(texto)
            print("texto agregado con extio")
        except PermissionError:
            print("No tienes permiso para editar este archivo")
        except OSError:
            print("[ERRROR] Algo salio mal")

    def guardar_texto(self, texto: str):
        try:
            with open(self.n_texto, "w", encoding="UTF-8") as archivo:
                archivo.write(texto)
            print("Texto guardado con exito")
        except FileExistsError:
            print("El archivo no existe")
        except OSError:
            print(f"[ERROR] Al ingresar al archivo {self.n_texto}")


texto1 = ArchivoTexto("Frases")
texto1.guardar_texto("La felicidad al igual que la fortuna es efimera")
texto1.agregar_texto("Todo deseo busca satisfacer un fragmento del alma")
texto1.leer()
