#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en 
#formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
#alex.nava2
meses= {"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}

fecha = str(input("Escribe una fecha en formato dd/mm/aaaa\n"))

dia=fecha[0:2]
mes=fecha[3:5]
año=fecha[6:10]

print(dia + " de " + meses[mes]  + " de " + año)