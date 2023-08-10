#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se 
#añada un nuevo dato debe imprimirse el contenido del diccionario.

#INSTAGRAM: alex.nava2

informacion = {}
bandera = 1
while bandera==1:
    dato = str(input("Que informacion vas a agregar?(nombre, edad, sexo, teléfono, correo electrónico, etc.)\n"))
    dato = dato.lower()
    valor= str(input("Escribe el dato:\n"))

    informacion[dato] = valor
    
    print(informacion)

    print("Quieres seguir ejecutando el programa?\n Presiona 1 de lo contrario presiona 2")
    bandera= int(input())



print("FIN")