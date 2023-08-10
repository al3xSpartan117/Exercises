#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a 
# intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un 
# programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

cantidad=float(input("Cantidad de dinero a depositar en la cuenta de ahorro: "));

interes=round((cantidad/100)*4,2);

dos=round(interes*2,2);
tres=round(interes*3,2);

print("Cantidad primer año: " + str(interes)+"Cantidad segundo año: "+ str(dos) + "Cantidad tercer año: " + str(tres));
