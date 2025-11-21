'''Solicita la cantidad de productos vendidos y el precio unitario, luego muestra el total de ventas

productosVendidos = int(input("ingrese la cantidad de productos vendidos: "))
totalVentas = 0 
articulosVendidos = []
for prodcutos in range(productosVendidos):
    nombreProducto = input("ingrese el nombre del producto: ")
    precioProducto = float(input("ingrese el precio del producto: "))
    articulosVendidos.append(f"{nombreProducto} --- {precioProducto}")
    totalVentas += precioProducto
    
print(articulosVendidos)    
print(f"El total vendido es de: {totalVentas}")   '''

'''Pide la edad de un usuario y muestra si puede acceder a un sistema restringido para mayores de 21 años'''

edadUsuario = int(input("ingrese la edad: "))
if edadUsuario > 21:
    print(f" su edad es ---> {edadUsuario} puede ingrersar al sistema")
else:
    print(f"su edad es ---> {edadUsuario} no puede ingresar al sistema")  