##import turtle
##
##for i in range(1,4000):
##    turtle.color("yellow")
##    turtle.speed(0)
##    turtle.left(199)
##    turtle.forward(400)
##------------------------------------------------------
##n = int(input("inserisci numero:"))
##f=1
##for t in range(n,1,-1):
##    f *= t
##
##print("fattoriale di" ,n, "è", f)
##------------------------------------------------------
##n = int(input("inserisci numero:"))
##e_primo=True
##for d in range(2,n//2):
##    if n%d == 0:
##        e_primo = False
##        break
##if e_primo:
##    print(n,"è primo")
##else:
##    print(n,"non è primo")
##------------------------------------------------------
##
##import turtle
##
##turtle.speed(10)
##turtle.color("red")
##for i in range(5):
##    turtle.right(144)
##    turtle.forward(550)
##-------------------------------------------------------
import turtle

turtle.fillcolor("red")
turtle.begin_fill()
turtle.pensize(10)
turtle.circle(240)
turtle.end_fill()
