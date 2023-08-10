#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por 
#las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Escribe tu nombre:\n")
sexo = input("Escribe tu sexo como M O H:\n")

abc="abcdefghijklmnopqrstuvwxyz"

inicial = nombre[:1].lower()
pos=abc.find(inicial)

if sexo.lower() == "m":
    if pos <= 12:
        print("Grupo A")
    else:
        print("Grupo B")
else:
    if pos >= 13:
        print("Grupo A")
    else:
        print("Grupo B")


