#Escribir una funcion que pida un numero entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese 
#numero, done n es el numero introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por 
#pantalla informando de ello.

#instagram: alex.nava2

def juanes(xbox):
    nombre = "tabla-" + str(xbox) + ".txt"
    if xbox>0 and xbox<11:
        try:
            f = open(nombre)
        except FileNotFoundError:
            return("ARCHIVO NO ENCONTRADO")
        else:
            print(f.read())
            f.close()
            return("LISTO!!!")    
    else:
        return("NUMERO INVALIDO")


print(juanes(8))





