# ingrsar por teclado las variables y los datos solicitados
# creo una lista vacia para guardarmis potencias
potencias = []
# pido al usuario que ingrese un exponente
base = int(input("ingrese un exponente positivo: "))
# uso un ciclo for para obtner una base que vaya del 1 al 9
for exponente in range(1, 11):
    # genero el resultado de la potencia
    resultado = base**exponente
    # uso un ciclo if para registrar solo números positivos
    if exponente > 0:
        # imprimo los resultados y se los agrego a mi liata vacia
        print(f"la base de {base} elevado a {exponente} es: {resultado} ")
        potencias.append(resultado)
print(potencias)
