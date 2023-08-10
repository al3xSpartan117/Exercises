#Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

#Instagram: alex.nava2

def clasificador(nota):
    if nota <=5:
        return "RP"
    elif nota <=7:
        return "AP"
    elif nota <=9:
        return "SB"
    elif nota ==10:
        return "EX"

def principal(notas):
    return list(map(clasificador, notas))


print(principal([3, 5, 6, 10, 10, 9, 8, 7]))