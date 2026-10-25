#Calculadora de descuentos
#mayor a 1000 20 de descuento
# entre 500 y 1000 10%

monto= float(input("Por favor, ingrese el monto de la compra: "))

if monto <0:
    print ("Error: El monto debe ser positivo, mayor a cero")
else:
    if monto>=1000:
        descuento = monto*0.2
    elif monto>=500:
        descuento= monto*0.1
    else:
        descuento = 0
    print("Monto: ",monto)
    print("Descuento: ", descuento)
    print("Total a pagar: ", monto-descuento)
    
        
             