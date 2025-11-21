'''Solicita la cantidad de materias inscritas por un estudiante y muestra si tiene sobrecarga académica (más de 7 materias)'''

materias_inscritas = int(input("ingrese la cantidad de materias inscritas>: "))

if materias_inscritas > 7:
    print(f"la cantidad de matrias es {materias_inscritas} tiene sobre carga academica")
    
else:
    print(f"la cantidad de materis inscritas es {materias_inscritas} no tiene sobre carga academica")  
    