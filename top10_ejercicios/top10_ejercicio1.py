"""✅ 1. Clase Alumno + validaciones

Crea una clase Alumno:

Atributos privados: __nombre,__edad

Si edad < 0 →ValueError

mostrar_info()Retorna datos del alumno

Usa @propertypara obtener/actualizar edad

📌 Práctica:

Encapsulamiento + propiedad + excepciones"""


class Alumno:
    """Clase padre, con atributos privados"""

    def __init__(self, nombre: str, edad: int):
        try:
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            self.__nombre = nombre
            self.__edad = edad
        except ValueError as e:
            print(e)

    @property
    def edad(self):
        """Método getter usando decorador, retorna la edad"""
        return self.__edad

    @edad.setter
    def edad(self, n_edad: int):
        """Método setter con decorador, modifica la edad"""
        try:
            if n_edad < 0:
                raise ValueError("La edad debe ser postiva")
            self.__edad = n_edad
            print("Edad actulizada de forma correcta")
            return self.__edad
        except ValueError as e:
            print(e)

    def mostrar_info(self):
        """Metodo encargado de mostrar la información del alumno"""
        print(f"Alumno {self.__nombre} | Edad {self.__edad}")


alumno1 = Alumno("Kristina", 4)
alumno1.mostrar_info()
print(alumno1.edad)
alumno1.edad = 5
alumno1.mostrar_info()
