from gturtle import *

def reifen():
    dot(260)
    setPenColor("white")
    dot(220)

def felge():
    setPenColor("lightgray")
    setPenWidth(10)
    dot(220)
    setPenColor("white")
    dot(200)
    setPenColor("lightgray")
    repeat 6:
        forward(100)
        backward(100)
        left(360/6)
    setPenColor("black")
    dot(30)

def rad():
    reifen()
    felge()
    
makeTurtle()
hideTurtle()

repeat:
    rad()
    right(1)
    delay(3000/360)
    clear()