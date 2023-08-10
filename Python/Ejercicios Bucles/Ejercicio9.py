#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
#contraseña hasta que introduzca la contraseña correcta.

password = "123456789"
contra = input("Escribe la contraseña:\n")

while contra != password:
    contra = input("La contraseña es incorrecta, intentelo de nuevo:\n")


print("BIENVENIDO")
