from gturtle import *

makeTurtle()
hideTurtle()

def baum0():
    forward(20)
    backward(20)

def baum1():
    forward(20)
    right(30)
    baum0()
    left(60)
    baum0()
    right(30)
    backward(20)
    
def baum2():
    forward(30)
    right(30)
    baum1()
    left(60)
    baum1()
    right(30)
    backward(30)
    
def baum3():
    forward(40)
    right(30)
    baum2()
    left(60)
    baum2()
    right(30)
    backward(40)
    
baum3()
    
