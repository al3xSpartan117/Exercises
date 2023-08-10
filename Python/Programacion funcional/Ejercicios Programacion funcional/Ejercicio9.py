lista = [5,7,9,6,3,1]
diccionario = {"hola":6, "adios":4}

def filtro(num):
    return num > 5

prueba = filter(filtro, lista)

print(list(prueba))


for i in diccionario.items():
    print(i[1])