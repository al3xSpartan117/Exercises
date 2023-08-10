#Realizar un programa que convierta una fecha de nacimiento a numeros romanos en formato dd/mm/aaaa

#INSTAGRAM: alex.nava2

romanos = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
bandera = "S"

while bandera == "S":
 fecha = input("Escribe tu fecha de nacimiento en formato dd/mm/aaaa\n")
 lista_fecha = fecha.split("/") #["25", "10", "1995"]
 dia = lista_fecha[0]
 mes = lista_fecha[1]
 anio = lista_fecha[2]
 if (int(dia) > 31) or (int(mes)>12) or (int(anio) > 3999):
    print("Fecha no valida")
    bandera = "S"
 else:
    bandera = "N"

#2795
#MM CM XC V
#CD
def conversor(dato):
    resta = 0
    if len(dato) == 4:
       resta = 0
    elif len(dato) == 3:
       resta = 1
    elif len(dato) == 2:
       resta = 2
    elif len(dato) == 1:
       resta = 3

    millar = ""
    centena = ""
    decena = ""
    unidad = ""
    for mcdu in range(len(dato), 0, -1):
        if mcdu == 4:
            millar = romanos[1000]*int(dato[0])
        elif mcdu == 3:#--------------------------------------------------------------CENTENA
            #C CC CCC CD D DC DCC DCCC CM M
            if (int(dato[1-resta]) > 0) and (int(dato[1-resta]) < 4):
                centena = romanos[100]*int(dato[1-resta])
            elif int(dato[1-resta]) == 4:
                centena = romanos[100]+romanos[500]
            elif int(dato[1-resta]) == 5:
                centena = romanos[500]
            elif (int(dato[1-resta]) > 5) and (int(dato[1-resta]) < 9):
                centena = romanos[500] + romanos[100]*(int(dato[1-resta])-5)
            elif int(dato[1-resta]) == 9:
                centena = romanos[100]+romanos[1000]
        elif mcdu == 2:#--------------------------------------------------------------DECENAS
            #X XX XXx XL L LX LXX LXXX XC C
            if (int(dato[2-resta]) > 0) and (int(dato[2-resta]) < 4):
                decena = romanos[10]*int(dato[2-resta])
            elif int(dato[2-resta]) == 4:
                decena = romanos[10]+romanos[50]#XL
            elif int(dato[2-resta]) == 5:
                decena = romanos[50]
            elif (int(dato[2-resta]) > 5) and (int(dato[2-resta]) < 9):
                decena = romanos[50] + romanos[10]*(int(dato[2-resta])-5)
            elif int(dato[2-resta]) == 9:
                decena = romanos[10]+romanos[100]
        elif mcdu == 1:#--------------------------------------------------------------UNIDADES
            #I II III IV V VI VII VIII IX X
            if (int(dato[3-resta]) > 0) and (int(dato[3-resta]) < 4):
                unidad = romanos[1]*int(dato[3-resta])
            elif int(dato[3-resta]) == 4:
                unidad = romanos[1]+romanos[5]#XL
            elif int(dato[3-resta]) == 5:
                unidad = romanos[5]
            elif (int(dato[3-resta]) > 5) and (int(dato[3-resta]) < 9):
                unidad = romanos[5] + romanos[1]*(int(dato[3-resta])-5)
            elif int(dato[3-resta]) == 9:
                unidad = romanos[1]+romanos[10]
      
    return millar+centena+decena+unidad

print(conversor(dia) + "/" + conversor(mes) + "/" + conversor(anio))


#MMCDLVI
#0123   INDICE
#2365   
#256   -1
#12    -2
#2     -3

#XXVI