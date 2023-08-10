#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
# contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable 
# sin tener en cuenta mayúsculas y minúsculas.

password = "HolaMundo"

contra = input("Introduce tu contraseña:\n")

if password.lower() == contra.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

