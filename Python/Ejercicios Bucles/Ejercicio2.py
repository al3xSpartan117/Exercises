#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad).

edad = int(input("Escribe tu edad:\n"))

for i in range(edad): #[0,1,2..21]
    print(i+1)
