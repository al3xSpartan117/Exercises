#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un 
# programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el 
# precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barras=int(input("Porfavor introduzca las barras vendidas que no son del dia: "));

print("Precio habitual: 3.49€");
descuento=float((3.49/100)*60);
print("Descuento por barra: " + str(descuento));
preciofinal=float(3.49-descuento);
total=barras*preciofinal;

print("Precio total final: " +str(total));



