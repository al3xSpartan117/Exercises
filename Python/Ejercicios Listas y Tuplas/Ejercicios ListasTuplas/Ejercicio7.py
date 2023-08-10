#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones 
#múltiplos de 3, y muestre por pantalla la lista resultante.

abc = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print(len(abc))

for i in range(len(abc), 0, -1):
   if i % 3==0:
      abc.pop(i-1)

print(abc)