from gturtle import *

makeTurtle()
hideTurtle()

def treppe(n):
    repeat n:
        forward(200/n)
        right(90)
        forward(300/n)
        left(90)
        
treppe(10)