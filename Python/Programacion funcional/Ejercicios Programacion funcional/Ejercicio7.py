#Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con 
#las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.

#INSTAGRAM:  alex.nava2


#{"matematicas":4} --------> {"MATEMATICAS":"RP"}
def clasificador(nota):
    if nota <= 5:
        return "RP"
    elif nota <=7:
        return "AP"
    elif nota <=9:
        return "SB"
    elif nota ==10:
        return "EX"
    else:
        return "ERROR"

def principal(diccionario):
    materias= map(str.upper, diccionario.keys())
    notas= map(clasificador, diccionario.values())
    return dict(zip(materias, notas))


print(principal({"matematicas":4, "fisica":6, "biologia":10, "historia":8}))













