#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Escribe una palabra:\n")

palabra_reves = palabra

palabra = list(palabra)
palabra_reves = list(palabra_reves)
palabra_reves.reverse()


if  palabra == palabra_reves:
    print("ES UN PALINDROMO")
else:
    print("NO ES UN PALINDROMO")