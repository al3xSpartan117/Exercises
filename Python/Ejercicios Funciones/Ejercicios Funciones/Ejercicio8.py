#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, 
#varianza y desviación típica.

#alex.nava2
import math
muestras = []
n = int(input("Cuantas muestras deseas introducir?\n"))

for i in range(n):
    muestra = float(input("Escribe la muestra numero " + str(i+1) + ":"))
    muestras.append(muestra)

def calculos(lista):
    diccionario = {}

    #MEDIA
    total = 0
    for j in lista:
        total += j
    media = total/len(lista)
    diccionario["media"]=round(media,2)
    #VARIANZA
    x=0
    for k in lista:
        x+=(k-media)**2
    varianza = x/len(lista)-1
    varianza = round(varianza,2)
    diccionario["varianza"]=varianza
    #DESVIACION
    desviacion = round(math.sqrt(varianza),2)
    diccionario["desviacion"]=desviacion
    return diccionario

print(calculos(muestras))