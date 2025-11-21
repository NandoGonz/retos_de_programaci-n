"""3. Conjuntos de cursos
Tienes dos conjuntos:

cursos_matematicas = {"Luis", "Ana", "Pedro"}

cursos_ingles = {"Pedro", "Carla", "Luis"}

Haz un programa que:

Muestre los estudiantes que están en ambos cursos .

Muestre los estudiantes que están solo en matemáticas .

Muestre los estudiantes que están en al menos un curso"""

cursos_matematicas = {"Luis", "Ana", "Pedro"}

cursos_ingles = {"Pedro", "Carla", "Luis"}


def estudiante_ambos_cursos():
    """usamos la intersección entre conjuntos para retornar el alumno que esta registrado en ambos cursos"""
    estudiante = (
        cursos_matematicas & cursos_ingles
    )  # podemos usar el método intersection()
    return estudiante


def solo_mat():
    """retornamos solo los alumnos del curso de matmática"""
    return cursos_matematicas


def estudiantes_en_un_curso():
    """usaremos la diferencia simetrica para retornar los alumnos que están al menos en un curso"""
    estudiantes_solo_en_un_curos = cursos_matematicas.symmetric_difference(
        cursos_ingles  # tambien podemos usar el simbolo ^
    )
    return estudiantes_solo_en_un_curos


print(f"Los alumnos en ambos cursos es {estudiante_ambos_cursos()}")
print(f"Los alumnos del curso de matemáticas son {solo_mat()}")
print(f"los alumnos que estan al menos en un curso son {estudiantes_en_un_curso()}")
