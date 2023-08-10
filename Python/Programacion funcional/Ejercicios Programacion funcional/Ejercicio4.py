#Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista 
#que devuelvan True al aplicarles la función booleana.

#instagran: alex.nava2 

nums = [60, 70, 15, 80, 90, 2, 3, 6, 20]     

def booleana(num):
    if num > 50:
        return True
    else:
        return False

def principal(funcion, lista):
    resultante = []
    for i in lista:
        if funcion(i) == True:
            resultante.append(i)

    return resultante

print(principal(booleana, nums))









