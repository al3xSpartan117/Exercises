#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Menos de 10 000        5%
#Entre 10 000 y 20 000 15%
#Entre 20 000 y 35 000 20%
#Entre 35 000 y 60 000 30%
#Mas de 60 000         45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le 
#corresponde.

renta = float(input("Cuanto es tu renta anual:\n"))


if renta >= 60000:
    print("45%")
elif renta <60000 and renta >= 35000:
    print("30%")
elif renta >= 20000 and renta <35000:
    print("20%")
elif renta >= 10000 and renta < 20000:
    print("15%")
else:
    print("5%") 
    
   

