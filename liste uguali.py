


c = 0
lista1 = [1,2,3,4,5,5,6,7,8,9,0]
lista2 = [5,2,8,5,6,9,3,1,7,0,4]



for i in range(len(lista1)):
    for j in range(len(lista2)):
        if lista1[i] == lista2[j]:
            c += 1



print("Ci sono",c,"elementi uguali")



if c == len(lista1) and c == len(lista2):
    print("Le due liste sono uguali!")



else:
    print("le liste sono diverse")