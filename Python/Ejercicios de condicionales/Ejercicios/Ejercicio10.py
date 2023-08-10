#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de
#  pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le 
# muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la 
# mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
# vegetariana o no y todos los ingredientes que lleva.

print("Pizzería Bella Napoli\n".upper())
respuesta=input("Quieres una pizza Vegetariana? (S o N)\n")

if respuesta.lower() == "s":
   ingrediente= int(input("Elige el ingrediente de tu pizza:\n 1-Pimiento\n 2-Tofu"))
   if ingrediente == 1:
       print("Tu pizza llevara:\nPimiento\nMozzarella\nTomate")
   elif ingrediente == 2:
       print("Tu pizza llevara:\nTofu\nMozzarella\nTomate")
   else:
       print("ERROR")
else:
     ingrediente= int(input("Elige el ingrediente de tu pizza:\n 1-Peperoni\n 2-Jamon\n 3-Salmon"))
     if ingrediente == 1:
       print("Tu pizza llevara:\nPeperoni\nMozzarella\nTomate")
     elif ingrediente == 2:
       print("Tu pizza llevara:\nJamon\nMozzarella\nTomate")
     elif ingrediente == 3:
       print("Tu pizza llevara:\nSalmon\nMozzarella\nTomate")
     else:
       print("ERROR")
     