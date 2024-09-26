from gturtle import *

def quadrat(seite):
    repeat 4:
        fd(seite)
        rt(90)

def reihe(n,seite):
    repeat n:
        quadrat(seite)
        rt(90)
        fd(seite)
        lt(90)

def gitter(m,n,seite):
    repeat m:
        reihe(n,seite)
        left(90)
        forward(n*seite)
        right(90)
        forward(seite)
    
makeTurtle()
ht()

gitter(3,5,30)
