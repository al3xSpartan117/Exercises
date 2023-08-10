#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el 
#diccionario.

#INSTAGRAM: alex.nava2


divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

opcion = str(input("Que divisa deseas visualizar?\n"))
opcion = opcion.title() 

if opcion in divisas:
  print(divisas[opcion])
else:
  print("No se encontro la divisa :(")





