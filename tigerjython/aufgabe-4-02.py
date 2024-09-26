from gturtle import *

def triangle():
    repeat 3:
        forward(200)
        left(360/3)
        
makeTurtle()
hideTurtle()

right(90)
setPos(-450,0)

repeat:
    triangle()
    penUp()
    forward(1)
    delay(10)
    penDown()
    clear()