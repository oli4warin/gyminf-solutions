from gturtle import *

makeTurtle()
hideTurtle()

setPenWidth(15)
penUp()
repeat 12:
    forward(210)
    penDown()
    backward(30)
    penUp()
    forward(30)
    backward(210)
    right(360/12)

setPenWidth(3)
repeat 60:
    forward(210)
    penDown()
    backward(10)
    penUp()
    forward(10)
    backward(210)
    right(360/60)