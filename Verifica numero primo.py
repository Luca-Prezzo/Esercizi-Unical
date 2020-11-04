n = int(input("inserisci numero:"))
e_primo=True
for d in range(2,n//2):
   if n%d == 0:
       e_primo = False
       break
if e_primo:
   print(n,"è primo")
else:
   print(n,"non è primo")