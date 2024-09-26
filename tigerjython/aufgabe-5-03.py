from gturtle import *

def vieleck(n,seite):
    repeat n:
        forward(seite)
        right(360/n)
    forward(seite)

makeTurtle()
hideTurtle()

repeat 6:
    vieleck(4,40)
    left(360/6)
right(90)
forward(40)
left(90)

repeat 6:
    vieleck(6,40)
    left(360/12)
    vieleck(4,40)
    left(360/12)
