#Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con 
#las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.

#INSTAGRAM: alex.nava2

asignaturas = {"matematicas":4, "Biologia":6, "Fisica":10, "Historia":8, "Quimica":2}

def clasificador(nota):
    if nota <=5:
        return "RP"
    elif nota <= 7:
        return "AP"
    elif nota <= 9:
        return "SB"
    elif nota == 10:
        return "EX"
    else:
        return "ERROR"


def principal(diccionario):
    claves = map(str.upper, diccionario.keys())
    valores = map(clasificador, diccionario.values())
    resultado = dict(zip(claves, valores))
    for clave, valor in diccionario.items():
        if valor <= 5:
            del(resultado[clave.upper()])
    return  resultado

print(principal(asignaturas))


