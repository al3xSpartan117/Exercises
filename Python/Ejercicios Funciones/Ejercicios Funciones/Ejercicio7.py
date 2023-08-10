#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
#INSTAGRAM: alex.nava2

muestras = [45,33,68,2,4,16,5,3,8,9,200]

def cuadrados(lista):
    lista_cuadrados = []

    for i in lista:
        cuadrado = i**2
        lista_cuadrados.append(cuadrado)
    return lista_cuadrados

print("Los cuadrados son: " + str(cuadrados(muestras)))
