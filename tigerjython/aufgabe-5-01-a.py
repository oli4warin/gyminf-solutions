from gturtle import *

makeTurtle()
hideTurtle()

def treppe(n):
    repeat n:
        forward(15)
        right(90)
        forward(20)
        left(90)
        
treppe(10)