#Elabore un algoripmo que muestre la factura de la siguiente compra el señor Pedro Ramires compro en falabella 2 gins de 125.000 mil cada uno 2 camisas de 45.000 mil cada una, una camisa tipo polo por 30.000 mil.
#Tener en cuenta lo siguinte: 
#Si la compra lleva camisa tipo polo tiene un descuento del 5%.
#Si la compra es superior a 200.000 mil se realiza un descuento del 30%.
#Mostrar el total a pagar y el total del descuento en pesos.

gins = 125000
camisa = 45000
camisapolo = 30000
total = (gins * 2) * (camisa * 2) + camisapolo
descuento = 0
if total > 200000:
    descuento = total * 0.3
    totalpagar = total - descuento
    print(f"El total de la compra es: {totalpagar} mil pesos.")
    print(f"El descuento es de {descuento} mil pesos.")
else:
    if camisapolo > 0:
        descuentocamisapolo = total * 0.05
        totalpagar = total - descuentocamisapolo 
        print(f"El descuento es de {descuentocamisapolo} mil pesos.")
    else:
        totalpagar = total
        print(f"El total de la compra es: {total} mil pesos.")
        print(f"El total a pagar es: {totalpagar} mil pesos.")