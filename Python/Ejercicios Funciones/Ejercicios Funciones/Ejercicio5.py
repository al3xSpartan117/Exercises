#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera 
#función.
#alex.nava2

import math

radio = float(input("Cual es el radio?\n"))

def area(radio):
    return math.pi*(radio**2)

def volumen(h):
    return area(radio)*h



op = input("Deseas obtener (1)area o (2)volumen")

if op == "1":
    print(round(area(radio),2))
elif op == "2":
    h = float(input("Cual es la altura"))
    print(round(volumen(h),2))






