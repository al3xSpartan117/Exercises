#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono 
# es <teléfono>.

#alex.nava2

info = {"nombre":"","edad":"","direccion":"","telefono":""}

for i in info:
    dato = str(input("Cual es tu "+ i +"\n"))
    info[i]=dato

print(info["nombre"] + " tiene " + info["edad"] + " años, vive en " + info["direccion"] +  " y su número de teléfono es " + info["telefono"])