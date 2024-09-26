from gturtle import *

def hexagon():
    repeat 6:
        forward(100)
        right(360/6)

def flower():
    repeat 8:
        hexagon()
        right(360/8)
        
makeTurtle()
hideTurtle()

setPenColor("blue")

repeat:
    flower()
    right(1)
    delay(20)
    clear()