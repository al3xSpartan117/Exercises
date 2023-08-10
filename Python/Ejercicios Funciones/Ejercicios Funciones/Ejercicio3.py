#Escribir una función que reciba un número entero positivo y devuelva su factorial.
#instagram: alex.nava2

n = int(input("Escribe un numero para obtener su factorial:\n"))


def factorial(n):
    multiplicacion = 1
    for i in range(n): 
        multiplicacion *= i+1
    print(multiplicacion)
    
if n < 0:
    print("No se aceptan numeros negativos")
else:
    factorial(n)





#4!=4(3)(2)(1)
