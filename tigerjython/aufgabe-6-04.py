from gturtle import *

def square(size):
    repeat 4:
        forward(size)
        right(90)

makeTurtle()
hideTurtle()

squareSize=200
repeat 40:
    square(squareSize)
    left(10)
    squareSize *= 0.97
