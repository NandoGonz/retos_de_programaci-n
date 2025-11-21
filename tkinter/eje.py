class Persona:
    def __init__(self, nombre: str, edad: int, correo: str):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.__contrasena = "1234"  # solo se puede acceder a el atraves de un método dentro de la clase get y set.
        self._ciudad = "Chibolo"  # no lo reconoce por fuera de la función, debe estar siempre por dentro.

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y mi correo es {self.correo} y vivio  en {self._ciudad}"

    def get_contrasena(self):
        return self.__contrasena

    def set_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena


p1 = Persona("Luis", 29, "lfgb@correo")
print(p1.presentarse())
print(p1.get_contrasena())
p1.set_contrasena("4321")
print(p1.get_contrasena())
print(p1._ciudad)
