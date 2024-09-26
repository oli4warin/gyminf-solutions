from gturtle import *

def triangle(size):
    repeat 3:
        forward(size)
        left(360/3)

makeTurtle()
hideTurtle()

right(90)
n=input("Bitte geben Sie die Anzahl Dreiecke ein")
length=200
repeat n:
    triangle(length)
    length -= 200/n

