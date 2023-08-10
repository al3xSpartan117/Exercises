#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, 
# y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

#alex.nava2

asignaturas= {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos=0
for i in asignaturas:
    print(i + " tiene " + str(asignaturas[i]) + " creditos")
    creditos += asignaturas[i]

print("El total de creditos es: " + str(creditos))