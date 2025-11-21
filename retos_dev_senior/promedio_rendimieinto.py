'''✅ 6. Promedio y rendimiento de un curso
Solicita la nota de 8 estudiantes en la materia de matemáticas. Calcula el promedio. Si el promedio es mayor o igual a 4.0, muestra "Buen rendimiento del grupo", si no, "Rendimiento bajo".'''

#ingresar por tecaldo las variables y los datos soliciados

notas = []
paraPromedio = 8

# llenamos nustra lista con un ciclo for
for i in range(8):
    # el {i+1} lo usamos para que el mensaje en pantalla pida desde la nota 1 en adelante, de lo contrario empieza en cero
    nota = float(input(f"ingrese una nota{i+1}: "))
    
    # implementamos el ciclo while, teniendo en cuenta que no sabemos cuantas veces se van a equivocar ingresando los datos
# lo podríamos ver como el condicional if

    while nota < 0 or nota > 5.0:
        print("nota no valida")
        nota = float(input(f"ingrese una nota{i+1}:  "))
    notas.append(nota)
    
# hallaremos el promedio, al tener el promedio establecido usaremos la función sum()
# usamos el for para especificar el recorrido de nuestro iterador i. para que me sume los promedios y me de un resultado total.
promedio = sum(notas[i] / paraPromedio for i in range(8))    
    
# validamos el promedio 
if promedio >= 4.0 and promedio <= 5.0:
    print(f"promedio en matemátcas es {promedio:.2f} su rendimiento es alto")   
else:
    print(f"su promedio es {promedio:.2f} su rendimiento en matematicas es bajo")     
    
print(notas)   
    
      

    