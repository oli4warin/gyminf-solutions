from gturtle import *

makeTurtle()
hideTurtle()

def dreieck():
    repeat 3:
        forward(100)
        right(360/3)

right(90)
repeat 6:
    dreieck()
    left(360/6)
    
