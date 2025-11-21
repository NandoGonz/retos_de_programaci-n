"""6. Clase Rectángulo:

Atributos: ancho,alto

Métodos: calcular_area(),calcular_perimetro()

Usa validación para no aceptar valores negativos"""

# perimetro = 2(L + A)
# Area = L * A


class Rectangulo:
    def __init__(self, alto: int, ancho: int):
        self.alto = alto
        self.ancho = ancho

    def calcular_area(self):
        return f"El área del rectangulo es = {self.ancho * self.alto}  cm"

    def calcular_perimetro(self):
        return f"El perimetro del rectangulo es = {2 * (self.ancho + self.alto)} cm"


area_rectangulo = Rectangulo(5, 8)
print(area_rectangulo.calcular_area())
print(area_rectangulo.calcular_perimetro())
