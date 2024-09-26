from gturtle import *

makeTurtle()
hideTurtle()

def zifferblatt():
    setPenColor("black")
    setPenWidth(15)
    penUp()
    repeat 12:
        forward(210)
        penDown()
        backward(30)
        penUp()
        forward(30)
        backward(210)
        right(360/12)
    
    setPenWidth(3)
    repeat 60:
        forward(210)
        penDown()
        backward(10)
        penUp()
        forward(10)
        backward(210)
        right(360/60)
    penDown()
        
def sekZeiger(second):
    heading(360/60*second)
    setPenWidth(7)
    setPenColor("red")
    forward(180)
    dot(35)
    backward(180)

def minZeiger(minute):
    heading(360/60*minute)
    setPenWidth(15)
    setPenColor("black")
    forward(160)
    backward(160)
    
zifferblatt()
savePlayground()
second=0
minute=0
repeat:
    repeat 60:
        minZeiger(minute)
        sekZeiger(second)
        second = (second+1)%60
        delay(1000)
        clear()
    minute=(minute+1)%60
