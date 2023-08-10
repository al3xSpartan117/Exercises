#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y 
#los muestre por pantalla ordenados de menor a mayor.

premio = []

for i in range(6):
    ganador = int(input("Escribe el numero ganador:\n"))
    premio.append(ganador)

premio.sort()

print("Los numeros ganadores son:\n" + str(premio))

