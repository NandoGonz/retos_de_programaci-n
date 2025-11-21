"""✅ 3. Registro de ventas en una droguería
Una droguería vende medicamentos durante el día. Pide al usuario el número de ventas y el valor de cada una. Si el valor total del día supera $500.000, muestra un mensaje de "Buen día de ventas", de lo contrario muestra "Ventas bajas".
"""

from prettytable import PrettyTable

while True:
    try:
        num_ventas = int(input("cantidad de ventas: "))
        if num_ventas > 0:
            break
    except ValueError:
        print("ingrese un valor numerico positivo")


totalVentas = 0
medicamento = []
for ventas in range(num_ventas):
    medicaNom = input(f"\n nombre del medicamento {ventas+1}: ")
    valorVenta = float(input(f"ingrese el valor de la venta {ventas+1}: "))
    medicamento.append({"nombre": medicaNom, "precio": valorVenta})
    totalVentas += valorVenta

if totalVentas > 500000:
    print(f"la venta es de {totalVentas:,.2f} ha sido un !buen dia de ventas!")
else:
    print(f"las ventas es de {totalVentas:,.2f} ha sido un dia regular")


print(totalVentas)
print(medicamento)

tabla = PrettyTable()

tabla.field_names = ["nombre", "precio", "total venta"]

for m in medicamento:
    tabla.add_row([m["nombre"], m["precio"], totalVentas])
    tabla.add_divider()


print(tabla)
