#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y 
#su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la 
#lista de la compra y el coste total, con el siguiente formato

#instagram: alex.nava2

cesta = {}

bandera = "s"
total=0
while bandera == "s":
    articulo = str(input("Nombre del articulo:\n"))
    precio = float(input("Precio del articulo: $"))

    cesta[articulo] = precio

    bandera = str(input("Quieres agregar otro articulo? presiona (s) de lo contrario presiona (n)"))

for i in cesta:
    print(i + " ------------- " + str(cesta[i]))
    total += cesta[i]

print("Total a pagar: $"+ str(total))


