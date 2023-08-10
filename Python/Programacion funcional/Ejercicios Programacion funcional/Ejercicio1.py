#Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera 
#función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones 
#anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el 
#precio final de la cesta.

# INSTAGRAM: alex.nava2
#   {50:20, 30:5, 45:10}

def descuento(precio, porcentaje):
    return precio - (precio/100)*porcentaje

def iva(precio, porcentaje):
    return (precio/100)*16

def ticket(cesta, funcion):
    total = 0
    for precio, porcentaje in cesta.items():
        total += funcion(precio, porcentaje)

    return total

print("El iva es:" + str(ticket({50:20, 30:5, 45:10}, iva)))
print("El total con descuento sin iva es:" + str(ticket({50:20, 30:5, 45:10}, descuento)))
print("El total es: " + str(ticket({50:20, 30:5, 45:10}, descuento)+ticket({50:20, 30:5, 45:10}, iva)))

        