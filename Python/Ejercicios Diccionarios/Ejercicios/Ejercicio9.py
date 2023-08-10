#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un 
# diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa 
# debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva 
# factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se 
# preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar 
# por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

#preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar
#Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
#Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
#Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad 
#pendiente de cobro.

#instagran:alex.nava2

facturas = {}
bandera = "s"
pendiente=0
cobrado=0
while bandera == "s":
    op = input("MENU\nQue accion deseas realizar:\n1-Agregar factura\n2-Pagar factura\n3-SALIR\n")

    if op == "1":
       numf = int(input("AGREGAR FACTURA\nNumero de factura:\n"))
       valor = float(input("Importe de factura:\n"))
       facturas[numf] = valor
       pendiente += valor
       print("Pendiente: $"+ str(pendiente))
       print("Cobrado el dia de hoy: $"+str(cobrado)+"\n\n")


    elif op == "2":
       numf=int(input("PAGAR FACTURA\nEscribe el numero de la factura:\n"))
       if numf in facturas:
           pendiente -= facturas[numf]
           cobrado   += facturas[numf]
       else:
           print("ERROR: No se encontro la factura")

       print("Pendiente: $"+ str(pendiente))
       print("Cobrado el dia de hoy: $"+str(cobrado)+"\n\n")
    elif op == "3":
         print("Pendiente: $"+ str(pendiente))
         print("Cobrado el dia de hoy: $"+str(cobrado)+"\n\n")
         bandera = "n"




    
       







