from gturtle import *

makeTurtle()
hideTurtle()

def vieleck(n,seite,farbe,dicke):
    setPenColor(farbe)
    setPenWidth(dicke)
    repeat n:
        forward(seite)
        right(360/n)
        
left(90)
vieleck(3,100,"lightblue",3)
vieleck(4,100,"blue",3)
vieleck(5,100,"green",3)
vieleck(6,100,"magenta",3)
vieleck(7,100,"orange",3)
vieleck(8,100,"red",3)