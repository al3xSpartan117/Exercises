#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla 
#el número de euros y el número de céntimos del precio introducido.

precio = input("Introduce el precio: ")

print("Euros: ", precio[:precio.find(".")], "Centimos: ", precio[precio.find("."):])