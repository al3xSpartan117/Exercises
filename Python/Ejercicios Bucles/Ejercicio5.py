#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre 
#por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inversion = float(input("Cuanto vas a invertir?\n"))
interes = float(input("Cuanto es el interes?\n"))
tiempo = int(input("Cuantos años?\n"))

for i in range(1, tiempo+1, 1):
    print("En {año} años tu ganancia sera de {ganancia}".format(año=i, ganancia=((inversion/100)*interes)*i))

