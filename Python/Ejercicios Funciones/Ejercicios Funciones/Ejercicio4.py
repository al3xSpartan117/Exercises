#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin 
#IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el 
#porcentaje de IVA, deberá aplicar un 21%.

#INSTAGRAM:alex.nava2

cantidad = float(input("Monto:\n"))
iva = float(input("Cual es el impuesto a aplicar:"))

def impuesto(monto, iva=21):
    return ((monto / 100)*iva)+monto


print(impuesto(cantidad, iva))
print(impuesto(cantidad))










