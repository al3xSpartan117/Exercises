#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
#Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas 
#aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificaciones=[]
for i in materias:
    cal = float(input("Cuanto sacaste en "+ i + ":\n"))
    calificaciones.append(cal)


for j in range(5):
    if calificaciones[j]<60:
        print("Tienes que repetir la materia de "+ materias[j])
        print(calificaciones)

