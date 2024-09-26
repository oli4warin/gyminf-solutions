from gturtle import *

makeTurtle()
hideTurtle()

def whiteSquare():
    repeat 4:
        forward(30)
        right(90)
        
def blackSquare():
    setFillColor("black")
    startPath()
    whiteSquare()
    fillPath()
    
def column():
    repeat 4:
        blackSquare()
        forward(30)
        whiteSquare()
        forward(30)
        
def doubleColumn():
    column()
    right(90)
    forward(60)
    right(90)
    column()

def checkboard():
    repeat 4:
        doubleColumn()
        left(180)
        
checkboard()
    
