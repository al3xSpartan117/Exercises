#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que 
#terminará.

#while True:
    #frase = input("Escribe una frase:\n")
    #if frase == "salir":
    #    break
    #print(frase)



hola = {1000:20, 40:30, 10:30}

print(hola.items())

for clave, valor in hola.items():
    print(str(clave) + " y " + str(valor))