#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el 
#programa debe mostrar un error.

dividendo = float(input("Introduce el dividendo:\n"))
divisor =float(input("Introduce el divisor:\n"))

if divisor == 0:
    print("ERROR")
else:
    print(dividendo/divisor)