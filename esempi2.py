







# ESERCIZIO CONTARE GLI ZERI NELLA LISTA
def conta_zeri(lista):
    c = 0                   #inizializzo il contatore
    for n in l:         #per ogni n in lista
        if n == 0:          #se n è = 0
            c += 1          #aggiungo 1
    return c



def contiente_uguali_consecutivi(lista):
    for n in range(1,len(lista)):
        if lista[i] == lista[i-1]:
            return True
    return False



def contiene_uguali(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if i != j and lista[i] == lista[j]:
                return True
    return False



def tutti_uguali(lista):
    return lista.count(lista[0]) == len(lista)

def e_palindroma(lista):
    n = len(lista)
    for i in range(n):
        if lista[i] != lista[n-1-i]:
            return False
    return True



def uguali(lista_1,lista_2):
    if len(lista_1) != len(lista_2):
        return False
    for i in range(len(lista_1)):
        if lista_1[i] != lista_2[i]:
            return False
    return True
