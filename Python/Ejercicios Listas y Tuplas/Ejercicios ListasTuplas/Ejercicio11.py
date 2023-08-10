#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla 
#su producto escalar.

#INSTAGRAM: alex.nava2

vecA = [1,2,3]
vecB = [-1,0,2]
resultado = 0
for i in range(len(vecA)):
    resultado += vecA[i]*vecB[i]

print("El producto escalar es: " + str(resultado))

pe1= vecA[0]*vecB[0]
pe2= vecA[1]*vecB[1]
pe3= vecA[2]*vecB[2]

resultado2=pe1+pe2+pe3

print("comprobacion " + str(resultado2))

