### Verificare se un numero è pari o dispari
##
##x = int(input("inserire un numero >>> "))
##if x%2 != 0:
##    print(x, "è dispari")
##else:
##    print(x,"è pari")





### verificare se un anno è bisestile
##
##anno = int(input("Inserisci un anno >>> "))
##
##if anno % 4 == 0 and anno % 100 != 0 or anno % 400 == 0:
##    print(anno,"è bisestile")
##else:
##    print(anno, "non è bisestile")






### password
##
##codice = int(input("inserisci la chiave di decifrazione >>> "))
##if codice == 12092001 or codice == 28091998:
##    print("Puoi entrare")
##else:
##    print("Non puoi entrare")







# # valutazione del triangolo

# lato1 = int(input("lato1 >>> "))
# lato2 = int(input("lato2 >>> "))
# lato3 = int(input("lato3 >>> "))

# if lato1 >= lato2+lato3 or lato2 <= lato1 + lato3 or lato3 >= lato1+lato2:
#     print("il triangolo non esiste")

# elif lato1==lato2 and lato2==lato3:
#     print("il triangolo è equilatero")

# elif lato1==lato2 or lato2==lato3 or lato1==3:
#     print("il triangolo è isoscele")

# else:
#     print("il triangolo è scaleno")





# # max di 3 numeri

# n1 = int(input("inserisci il primo numero >>> "))
# n2 = int(input("inserisci il secondo numero >>> "))
# n3 = int(input("inserisci il terzo numero >>> "))

# if n1 >= n2 and n1 >= n3:
#     massimo = n1
# if n2 >= n1 and n2 >= n3:
#     massimo = n2
# if n3 >= n1 and n3 >= n2:
#     massimo = n3
# print("il massimo è",massimo)








# #calcolo tax per reddito
# # se reddito < 10000 ---- no tax
# # se 10000 < reddito < 25000 ---- 15%
# # se 25000 < reddito < 50000 ---- 30%
# # reddito > 50000 ---- 45%

# reddito_da_tassare = int(input("Inserisci il tuo reddito >>> "))

# limite_aliquota_45 = 50000
# limite_aliquota_30 = 25000
# limite_aliquota_15 = 10000

# if reddito_da_tassare > limite_aliquota_45:
#     tasse = 0.45 * reddito_da_tassare

# elif reddito_da_tassare > limite_aliquota_30:
#     tasse = 0.3 * reddito_da_tassare

# elif reddito_da_tassare > limite_aliquota_15:
#     tasse = 0.15 * reddito_da_tassare

# print("Tasse:",tasse)





# pari e dispari

# pari = 0
# dispari = 0

# continua = True

# while continua:
#     x = int(input("inserisci un valore: "))
#     if x >= 0:
#       if x % 2 == 0:
#            pari += 1
#       else:
#            dispari += 1
#     else:
#         continua = False

# print("i valori dispari sono:", dispari)

# print("i valori pari sono:", pari)






#somma dei valori dispari da 1 a n (v1)

# n = int(input("N = "))
# i = 1
# somma = 0
# while i<=n:
#     if i%2==1:
#         somma += i
#     i += 1
# print("La somma di tutti i valori dispari, da 1 a",n, "è",somma)



#           RIVEDERE
#somma dei dispari da 1 a n (v2)
# somma = 0
# n = int(input("N = "))

# for i in range(1, n+1):
#     if i%2 == 1:
#         somma += i
# print("La somma di tutti i valori dispari, da 1 a",n, "è",somma)




#somma dei dispari da 1 a n (v3)

# n = int(input("N = "))
# somma = 0

# for i in range(1,n+1,2):
#     somma += i

# print("La somma di tutti i valori dispari, da 1 a",n, "è",somma)





#somma dei dispari da 1 a n (v4)

# n = int(input("N = "))
# somma = sum(range(1,n+1,2))
# print("La somma è",somma)




# calcolo potenze v1

# base = int(input("Dammi un numero >>> "))
# esponente = int(input("Dammi un esponente >>> "))

# potenza = base ** esponente

# print("la potenza è",potenza)