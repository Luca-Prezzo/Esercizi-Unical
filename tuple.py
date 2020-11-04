tuple
t = (10,15,8)   # una tupla con 3 valori
(a,b,c) = t
print(a)
print(b)
print(c)

a,b = b,a       # si possono scambiare i valori
print(a)
print(b)

lista = [10,100,1000]
p = tuple(lista)
print(p)