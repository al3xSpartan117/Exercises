#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
#Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla 
#con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y 
#<nota> cada una de las correspondientes notas introducidas por el usuario.

materias= ["Matematicas", "Física", "Química", "Historia", "Lengua", "Biologia"]

calificaciones = []

for i in materias:
    cal=float(input("Cuanto sacaste en " + i +":\n"))
    calificaciones.append(cal)

for j in range(len(materias)):
    print("En " + materias[j] +"has sacado: " + str(calificaciones[j]))
