#Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y 
#logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla 
#con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

# alex.nava2
import math

def calculadora():
    n = int(input("Escribe un numero entero:\n"))
    op = input("Que funcion deseas aplicar?\n 1-Coseno\n 2-Seno\n 3-Tangente\n 4-Logaritmo\n 5-Exponencial\n")

    if op == "1":
        for i in range(1, n+1, 1):
            print("El coseno de " + str(i) + " es " + str(math.cos(i)))
    elif op == "2":
        for i in range(1, n+1, 1):
            print("El seno de " + str(i) + " es " + str(math.sin(i)))
    elif op == "3":
        for i in range(1, n+1, 1):
            print("La tangente de " + str(i) + " es " + str(math.tan(i)))
    elif op == "4":
        for i in range(1, n+1, 1):
            print("El logaritmo de " + str(i) +" es " + str(math.log(i)))
    elif op == "5":
        for i in range(1, n+1, 1):
            print("La exponencial de " + str(i) + "es " + str(math.exp(i)))
b = "s"
while b == "s":
  calculadora()
  b = input("Quieres volver al menu?\nEscribe s si no escribe n")
