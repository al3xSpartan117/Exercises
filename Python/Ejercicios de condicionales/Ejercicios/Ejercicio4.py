#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Introduce un numero entero:\n"))

d=numero%2

if d == 0:
    print("Es numero par")
else:
    print("Es un numero impar")
