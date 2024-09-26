from gturtle import *

makeTurtle()
hideTurtle()

penUp()
left(90)
forward(160)
right(90)

repeat 3:
    setPenColor("red")
    repeat 2:
        repeat 4:
            penDown()
            dot(15)
            penUp()
            forward(25)
        backward(4*25)
        right(90)
        forward(25)
        left(90)
    setPenColor("blue")
    repeat 3:
        repeat 4:
            penDown()
            dot(15)
            penUp()
            forward(25)
        backward(4*25)
        right(90)
        forward(25)
        left(90)
