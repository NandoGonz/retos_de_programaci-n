"""✅ 7. Control de medicamentos en stock
Ingresa 6 medicamentos y su cantidad disponible. Si algún medicamento tiene menos de 10 unidades, imprime una advertencia para hacer pedido urgente.
"""

medicina = []
unidadesDemedicina = []
for medicamentos in range(6):
    nombreMedicamento = input(f"ingresa el nombre de un medicameto {medicamentos+1}: ")
    cantidadMedicamento = int(input("ingresa la cantidad disponible del medicamento: "))
    medicina.append(nombreMedicamento)
    unidadesDemedicina.append(cantidadMedicamento)

    if cantidadMedicamento < 10:
        print(
            f"ALERTA, debe solicitar más medicamentos {nombreMedicamento} urgente solo hay {cantidadMedicamento}"
        )
    else:
        print(
            f"cantidad de medicamentos {nombreMedicamento} es {cantidadMedicamento} todo es normal, no hay ALERTA"
        )

print(medicina)
print(unidadesDemedicina)

# finalizar inventario de la siguiente manera damos una cuenta total de la medicina y su cantidad.
print("\n contedo de medicamentos")

for medicamentos in range(6):
    # colocamos el iterador dentro de corchete al momento de la  invcacion de nuestra lista para imprimirlo de forma individual
    print(
        f"medicamento {medicina[medicamentos]}-{unidadesDemedicina[medicamentos]} unidades"
    )


print("\n fin del conteo de medicina")
