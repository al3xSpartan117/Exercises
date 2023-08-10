#Escribir un programa que almacene las matrices

# A= [1,2,3]    B=[-1,0]
#    [4,5,6]      [0, 1]
#                 [1, 1]
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

#INSTAGRAM: alex.nava2

a = ((1, 2, 3), 
     (4, 5, 6))      #2x3  3x2

b = ((-1, 0),
     (0, 1),
     (1,1))

resultado = [[0,0],
             [0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            resultado[i][j] += a[i][k]*b[k][j]    #0+
 

for t in range(len(resultado)):
    resultado[t]=tuple(resultado[t])
    print(resultado[t])



