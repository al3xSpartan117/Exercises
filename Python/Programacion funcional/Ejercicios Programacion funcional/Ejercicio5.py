#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
#instagram: alex.nava2

def funcion(frase):
    palabras = frase.split()
    longitudes = map(len, palabras)
    for i in longitudes:
        print(i)
    return dict(zip(palabras, longitudes))

print(funcion("Hola amigos suscribete y sigueme en instagram"))


longitudes2 = [1, 2, 4, 7, 9]

print(longitudes2)