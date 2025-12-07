"""✅ 10. Sistema de Logs

Clase Logger:

registrar(mensaje)→ guardar con fecha en archivo plano

ver_logs()→ muestra contenido

filtrar(busqueda) → devuelve líneas coincidentes

📌 Práctica:

Manejo de archivos + procesamiento de texto + excepción"""

from datetime import datetime


class Logger:
    """Clse padre con el atributo registro donde se registran las tareas"""

    def __init__(self, registro):
        self.registro = registro

    def registrar(self, texto):
        """Métdodo encargado de escribiruna tarea en el archvio"""
        try:
            date = datetime.now().strftime(
                "%Y-%m-%d %I:%M:%p"
            )  # Creamos una variable para asignar la hora de creación

            with open(self.registro, "w", encoding="UTF-8") as archivo:
                archivo.write(
                    f"Registro creado a la hora: {date}\n"
                )  # con el metodo write escribismos la hoa dentro del archivo
                archivo.write(
                    "#" * 50
                )  #  Para crear un separador entre la hora y el texto creado
                archivo.write("\n")
                archivo.write(
                    texto
                )  # Ingresamos la tarea que vamos a escribir en el archivo.txt
            print("Tarea gaurdada con esxito en el logger")
        except FileNotFoundError:
            print(f"El archivo {self.registro} no existe")
        except OSError:
            print("[ERROR] al ingresar al archivo")

    def ver_logs(self):
        """Método creado para ver el contenido del archivo"""
        try:

            with open(self.registro, "r", encoding="UTF-8") as archivo:
                contenido = archivo.read()
                print("mostrando logs \n")
                print(contenido)
        except PermissionError:
            print("No tienes permiso para ingresar al archivo")
        except OSError:
            print("[ERROR] algo salio mal")

    def agregar_registro_nuevo(self, n_texto):
        """Método creado para agregar un nuesvo registro al archivo"""
        try:
            with open(self.registro, "a", encoding="UTF-8") as archivo:
                archivo.write("\n")
                archivo.write(n_texto)
            print("Tarea guardada de forma exitosa")
        except FileNotFoundError:
            print("El archivo al que desea agregar la tarea no existe")
        except OSError:
            print("[ERROR] algo salio mal")

    def filtrar(self, busqueda):
        """Devuelve una lista de líneas donde aparece la palabra buscada."""
        try:
            with open(self.registro, "r", encoding="UTF-8") as archivo:
                lineas = archivo.readlines()

            # filtrar coincidencias
            coincidencias = [
                linea.strip() for linea in lineas if busqueda.lower() in linea.lower()
            ]

            if coincidencias:
                print("\n🔎 COINCIDENCIAS ENCONTRADAS:")
                for c in coincidencias:
                    print(" -", c)
            else:
                print("❌ No se encontraron coincidencias.")

            return coincidencias

        except FileNotFoundError:
            print("❌ No existe archivo para buscar.")
            return []
        except OSError:
            print("❌ ERROR al procesar la búsqueda.")
            return []


# intancianso objetos
log1 = Logger("Tareas diarias")
log1.registrar("Es bueno volver a practicar")
log1.ver_logs()
log1.agregar_registro_nuevo("Cada dia noto más mi desconocimiento")
log1.agregar_registro_nuevo("hoy aprednid algo nuevo")
log1.filtrar("Es")
log1.filtrar("cada")
log1.filtrar("sopa")
