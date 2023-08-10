#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en 
#español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe 
#crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el 
#diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

#INSTAGRAM: alex.nava2

diccionario = {}

palabras = input("Escribe las palabras en el formato: - hola:hello,perro:dog,casa:house -")

for i in palabras.split(","):
    clave, valor = i.split(":")

    diccionario[clave] = valor

frase = input("Escribe una frase en español para traducir:\n")

for j in frase.split(" "):
    if j in diccionario:
        print(diccionario[j], end=" ")
    else:
        print(j, end=" ")


