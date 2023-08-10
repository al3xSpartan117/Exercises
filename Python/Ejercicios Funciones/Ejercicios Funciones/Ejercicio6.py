#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

#instagram: alex.nava2 

muestras = []

n = int(input("Cuantas muestras vas a introducir?\n"))

for i in range(n):
    muestra = float(input("Escribe la muestra " + str(i+1) + ":"))
    muestras.append(muestra)

def media(lista):
    total = 0
    for i in lista:
        total += i
    promedio = total/len(lista)
    return promedio

print("El promedio es: " + round(media(muestras),3))
