#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una 
#fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
#diccionario debe mostrar un mensaje informando de ello.

#Platano 1.35
#Manzana 0.80
#Pera    0.85
#Naranja 0.70

#alex.nava2

frutas = {"platano":"1.35","manzana":"0.80","pera":"0.85","naranja":"0.70",}

opcion = str(input("Que fruta deseas comprar?\n"))
opcion = opcion.lower()

if opcion in frutas:
 kilos = float(input("Cuantos kilos deseas llevar?\n"))
 precio = kilos*(float(frutas[opcion]))
 print("El precio es: $"+ str(precio))
else:
    print("Lo sentimos esa fruta no esta en el inventario :(")