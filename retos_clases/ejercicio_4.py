"""9. Herencia Simple
Crea una clase Empleado que herede de Persona y agregue el atributo puesto y un método trabajar().
"""


class Persona:
    def __init__(self, nombre: str, edad: int, ciudad: str = "Sicilia"):
        self.nombre = nombre  # atributo
        self.edad = edad  # atributo
        self.ciudad = ciudad  # atributo con un


class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, ciudad: str, cargo: str):
        super().__init__(nombre, edad, ciudad)
        self.cargo = cargo

    def trabajar(self):
        return f"""EL empleado {self.nombre} 
tiene {self.edad}
vive en {self.ciudad}
trabaja como {self.cargo} en la empresa"""


empleado1 = Empleado("Luis", 29, "Chivolo", "Desarrollador backend")
print(empleado1.trabajar())
