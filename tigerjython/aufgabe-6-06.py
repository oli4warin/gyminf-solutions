from gturtle import *

def star(size):
    repeat 5:
        forward(size)
        right(144)

def fillStar(size,color):
    setPenColor(color)
    setFillColor(color)
    startPath()
    star(size)
    fillPath()
    
def ringOfStars(numberOfStars,starSize,starColor,radius):
    penUp()
    angle=90
    heading(angle)
    backward(starSize/2)
    repeat numberOfStars:
        heading(angle)
        forward(radius)
        heading(90)
        penDown()
        fillStar(starSize,starColor)
        penUp()
        heading(angle)
        backward(radius)
        angle+=360/numberOfStars
    penDown()

def rectangle(width, height):
    repeat 2:
        forward(width)
        left(90)
        forward(height)
        left(90)
        
def centerRectangle(width, height):
    penUp()
    backward(height/2)
    right(90)
    backward(width/2)
    penDown()
    rectangle(width,height)
    penUp()
    forward(width/2)
    left(90)
    forward(height/2)

def fillCenterRectangle(width, height,color):
    setPenColor(color)
    setFillColor(color)
    startPath()
    centerRectangle(width,height)
    fillPath()
    
def europeFlag(width):
    height=2/3*width
    fillCenterRectangle(width,height,"blue")
    ringOfStars(12,width/20,"yellow",0.7*height/2)
    
        
makeTurtle()
hideTurtle()

europeFlag(400)
