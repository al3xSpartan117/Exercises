#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese 
#número hasta cero separados por comas.

num = int(input("Escribe un numero entero:\n"))

if num < 0:
    print("No se permiten numeros negativos")
else:
    for i in range(num,0,-1):
        print(i, end=",")

#instagram: alex.nava2
#NicoPepperFunk 
#y como seria con un while?

num = int(input("Escribe un numero entero:\n"))

if num < 0:
    print("No se permiten numeros negativos")
else:
    while num > -1:
        print(num, end=",")
        num = num-1


