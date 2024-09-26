from gturtle import *

def spielfigur(farbe):
    setPenColor(farbe)
    setPenWidth(2)
    dot(30)
    fd(25)
    dot(22)
    bk(25)
    rt(30)
    bk(30)
    fd(30)
    lt(60)
    bk(30)
    fd(30)
    rt(30)
    
makeTurtle()
ht()

anzahlSpielfiguren=input("Bitte Anzahl der Spielfiguren")
farbe=input("Bitte Farbe eingeben")

repeat anzahlSpielfiguren:
    spielfigur(farbe)
    penUp()
    right(90)
    fd(50)
    left(90)
    penDown()