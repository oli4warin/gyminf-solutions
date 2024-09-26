from gturtle import *

makeTurtle()
hideTurtle()

def triangle():
    repeat 3:
        forward(30)
        left(360/3)
    forward(30)
        
def orangeTriangle():
    setFillColor("orange")
    setPenColor("orange")
    startPath()
    triangle()
    fillPath()
    
def redTriangle():
    setFillColor("red")
    setPenColor("red")
    startPath()
    triangle()
    fillPath()
    
repeat 6:
    orangeTriangle()
    right(360/12)
    redTriangle()
    right(360/12)
    
