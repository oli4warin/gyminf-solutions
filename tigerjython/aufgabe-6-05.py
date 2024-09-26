from gturtle import *

dotSize=20
distance=30

def punkte(n):
    repeat n:
        dot(dotSize)
        penUp()
        forward(distance)
        penDown()
    penUp()
    backward(n*distance)
    right(90)
    forward(distance)
    left(90)
    penDown()



makeTurtle()
hideTurtle()

setPenColor("blue")
anzahl=input("Bitte geben Sie die Anzahl ein")
n=0


repeat anzahl:
    n+=1
    punkte(n)

repeat anzahl:
    n-=1
    punkte(n)

    