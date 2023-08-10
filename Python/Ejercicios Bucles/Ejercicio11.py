#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra 
#introducida empezando por la última.

cad = input("Introduce una palabra:\n")

for i in range(len(cad)-1, -1, -1):
    print(cad[i])
