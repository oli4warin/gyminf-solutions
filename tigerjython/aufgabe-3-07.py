from gturtle import *

makeTurtle()
hideTurtle()

def blatt():
    repeat 30:
        forward(6)
        right(4)
    right(60)
    repeat 30:
        forward(6)
        right(4)
    right(60)

        
def gruenesBlatt():
    setFillColor("green")
    startPath()
    blatt()
    fillPath()

def gelbesBlatt():
    setFillColor("yellow")
    startPath()
    blatt()
    fillPath()
        
def gelbeBlume():
    repeat 6:
        gelbesBlatt()
        right(360/6)

def grueneBlume():
    repeat 6:
        gruenesBlatt()
        right(360/6)

def gruenGelbeBlume():
    gelbeBlume()
    left(360/12)
    grueneBlume()


gruenGelbeBlume()
    
    
