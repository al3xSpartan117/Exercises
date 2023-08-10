#Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función 
#dada a cada uno de los elementos de la lista.
#instagram:alex.nava2
nombres = ["AlEx", "RoDrIGO", "AlvaRO", "FeRNANda"]
resultante = []


def mayusculas(lista):
    for i in lista:
        i = i.upper()
        resultante.append(i)
    
    return resultante
def minusculas(lista):
    for i in lista:
        i = i.lower()
        resultante.append(i)
    
    return resultante
def titulo(lista):
    for i in lista:
        i = i.title()
        resultante.append(i)
    
    return resultante


def principal(lista, funcion):
    resultado = funcion(lista)
    return resultado


print(principal(nombres, mayusculas))
