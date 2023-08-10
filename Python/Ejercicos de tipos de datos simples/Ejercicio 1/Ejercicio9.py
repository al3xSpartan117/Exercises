#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre 
#por pantalla el capital obtenido en la inversión.

cantidad=float(input("Cual es la cantidad a invertir: "));
interes=float(input("Cual es el interes: "));
tiempo=float(input("Cual es la cantidad de años: "));

ganancia=(cantidad/100)*interes;
gananciaTotal=round(ganancia*tiempo,2);

print("Capital obtenido: "+str(gananciaTotal));