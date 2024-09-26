from gturtle import *

makeTurtle()
hideTurtle()

def octagon():
    repeat 8:
        forward(50)
        right(360/8)
        
def hexagon():
    repeat 6:
        forward(60)
        right(360/6)

def graphic1():
    setPenColor("blue")
    repeat 12:
        octagon()
        right(360/12)
        
def graphic2():
    setPenColor("red")
    repeat 6:
        hexagon()
        right(360/6)
        
graphic1()
penUp()
right(90)
forward(400)
left(90)
penDown()
graphic2()
