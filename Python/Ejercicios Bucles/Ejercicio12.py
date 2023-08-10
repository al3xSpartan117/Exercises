#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de 
#veces que aparece la letra en la frase.

frase = input("Escribe una frase:\n")   #Alejandro
letra = input("Escribe una letra:\n")   #e
cont=0
for i in frase:      
    if i  == letra:
        cont+=1 

print("La letra " + letra + " aparece " + str(cont) + " veces ")    