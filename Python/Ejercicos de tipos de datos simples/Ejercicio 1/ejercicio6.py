#Escribir un programa que lea un entero porsitivo,  n , 
# introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta  n .

n=int(input("Hasta que numero quiere que se sumen los enteros?"));

suma=(n*(n+1))/2;

print("La suma es: " + str(suma));