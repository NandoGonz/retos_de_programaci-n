'''✅ 1. Control de compras en una tienda
Una tienda desea registrar el total de compras de 5 clientes. Si una compra supera los $200.000, se debe aplicar un 20% de descuento. Imprime el valor final a pagar por cada cliente.'''
valorCompra = []
descuento = 0.20
for i in range(5):
    clliente = print(f"cliente: {i+1}")
    compra = float(input("ingrese el valor de la compra: "))
    valorCompra.append(compra)
    if compra > 200000:
        pagoDescuento = compra * descuento     
        total_a_pagar = compra - pagoDescuento
        print(f"su compra es de{compra} y tiene un descuento de {pagoDescuento} debe pagar {total_a_pagar}")
    else:
        print(f"su compra es de{compra} no tiene descuento")    
       
print(valorCompra)       