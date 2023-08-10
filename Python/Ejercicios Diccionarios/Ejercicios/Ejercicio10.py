#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un 
# diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente 
# (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente 
# preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar 
# cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función 
# de la opción elegida el programa tendrá que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#Terminar el programa.

#INSTAGRAM: alex.nava2

clientes = {}
bandera = "s"

while bandera == "s":
    op = input("MENU\nQue opcion deseas realizar\n(1)Agregar cliente\n(2)Eliminar cliente\n(3)Mostrar cliente\n(4)Listar todos los clientes\n(5)Listar clientes preferentes\n(6)SALIR\n")

    if op == "1":
      #(nombre, dirección, teléfono, correo, preferente)
      nif = input("NIF: ")
      nombre = input("Nombre: ")
      direccion = input("Direccion: ")
      telefono = input("Telefono: ")
      correo = input("Correo: ")
      preferente = input("Es usuario preferente?(true/false): ")
      preferente = preferente.lower()
      cliente = {"nombre":nombre,"direccion":direccion,"telefono":telefono,"correo":correo,"preferente":preferente,}
      clientes[nif]=cliente

    elif op == "2":
         nif = input("\nELIMINAR USUARIO\nEscribe el NIF del usuario:\n")
         if nif in clientes:
              for clave, valor in clientes[nif].items():
                   print(clave + " : " + valor)
                

              del(clientes[nif])
              print("USUARIO ELIMINADO\n")
         else:
             print("Este usuario no existe\n")
         print("\n")

    elif op == "3":
        nif = input("\nBUSCAR CLIENTE\nEscribe el NIF del usuario:\n")
        if nif in clientes:
             for clave, valor in clientes[nif].items():
                 print(clave + " : " + valor)
        else:
             print("Este usuario no existe\n")
        print("\n")
    elif op == "4":
        for nif in clientes:
            print("--------------------------------")
            for clave, valor in clientes[nif].items():
                 print(clave + " : " + valor)
    elif op == "5":
        for j in clientes:
            for k in clientes[j].items():
                if "true" in k:
                    for y in clientes[j].items():
                     if "nombre" in y:
                      clave = y[0].title()
                      valor = y[1].title()
                      print("USUARIO VIP: "+j+" "+clave+":"+valor+"\n")
                    

        
    elif op == "6":
        bandera = "n"

