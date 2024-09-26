from gturtle import *

def hoelzchen():
    setPenWidth(4)
    setPenColor("yellow")
    forward(100)
    setPenColor("red")
    dot(12)
    penUp()
    backward(100)
    penDown()
    
def space(length):
    setX(getX()+length)

def reihe(n):
    setX(-600)
    setY(200)
    clear("black")
    repeat n:
        hoelzchen()
        space(40)

        
def zug(spieler,n):
    while True:
        x=input(spieler+": Wie viele Hölzchen möchten Sie entfernen? (1,2 oder 3)")
        if x<=n and (x==1 or x==2 or x==3):
            break
        else:
            msgDlg("Ungültige Eingabe! Bitte wiederholen!")
    reihe(n-x)
    return n-x

def gewonnen(spieler,n):
        if n==0:
            msgDlg(spieler + " hat gewonnen.")
            return True
        return False
    
def spiel():
    n=input("Mit wie vielen Hölzchen soll gespielt werden?")
    name1=str(input("Wie heisst Spieler:in 1?"))
    name2=str(input("Wie heisst Spieler:in 2?"))
    while n>0:
        reihe(n)
        for player in [name1, name2]:
            n = zug(player,n)
            if gewonnen(player,n):
                return player

makeTurtle()
hideTurtle()


spiel()