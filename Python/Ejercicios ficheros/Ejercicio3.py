#Escribir una funcion que pida dos numeros n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de 
#ese numero, y muestre por pantalla la linea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla 
#informando de ello.

#INSTAGRAM: alex.nava2alex.nava2


def MyChemicalRomance(n,m):
    if (n<0 or n>10) or (m<0 or m>10):
        return("ERROR... Verifica los numeros que ingresaste...")
    else:
        NombreArchivo = "tabla-" + str(n) + ".txt" #tabla-.txt

        try:
           f = open(NombreArchivo)
        except FileNotFoundError:
            return("NO SE ENCONTRO EL ARCHIVO!!!")
        else:
            lineas = f.readlines()
            print(lineas[m-1])#7
            f.close()
            return("LISTO!!")


print(MyChemicalRomance(5,6))




  