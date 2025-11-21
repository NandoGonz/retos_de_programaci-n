''' 4. Descuento por edad en la droguería
Una droguería quiere dar un 10% de descuento a personas mayores de 60 años. Solicita los datos de 5 clientes: nombre, edad y valor de la compra. Aplica el descuento si corresponde y muestra el total a pagar.'''
# ingresar pot teclado las variables y los datos 
# usaremos un ciclo while y for 
#nombre = input("inggrese su nombre ")
descuento = 0.10       
clientes = []

for cliente in range(1,6):
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese la edad: "))
    valor_de_la_compra = float(input("ingrese el valor de su compra: "))
    clientes.append(nombre)
    
    
    if edad > 60 and valor_de_la_compra > 0:
        total_a_cobrar = valor_de_la_compra * descuento
        total_a_pagar_a_pagar = valor_de_la_compra - total_a_cobrar 
        print(f" el cliente {nombre} es mayor de 60, tiene: {edad} y su compra es de {valor_de_la_compra} y obtiene un descuento de {total_a_cobrar} total a pagar {total_a_pagar_a_pagar}")
        
    else:
        print(f" por su edad {edad} no cuenta con descuento pagar {valor_de_la_compra}")   
print(f"\n nombre cleintes {clientes}")    
    
    
            
        
