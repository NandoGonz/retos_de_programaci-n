resultados = []
num = int(input("\n tabla del: "))

for i in range(1, 10):
    resultado = num * i

    if num > 0:
        print(f"{num} * {i} = {resultado}")
        resultados.append(resultado)
    else:
        print("ingreso un valor no valido")
print(resultados)
print(resultados[3:6])
print(resultados[::-1])
