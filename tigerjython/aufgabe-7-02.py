gedachteZahl=0

antwort=input("Befindet sich die gedachte Zahl auf der Karte 1? (j/n)")
if antwort == "j":
    gedachteZahl += 1
antwort=input("Befindet sich die gedachte Zahl auf der Karte 2? (j/n)")
if antwort == "j":
    gedachteZahl += 2
antwort=input("Befindet sich die gedachte Zahl auf der Karte 3? (j/n)")
if antwort == "j":
    gedachteZahl += 4
antwort=input("Befindet sich die gedachte Zahl auf der Karte 4? (j/n)")
if antwort == "j":
    gedachteZahl += 8
antwort=input("Befindet sich die gedachte Zahl auf der Karte 5? (j/n)")
if antwort == "j":
    gedachteZahl += 16
antwort=input("Befindet sich die gedachte Zahl auf der Karte 6? (j/n)")
if antwort == "j":
    gedachteZahl += 32
antwort=input("Befindet sich die gedachte Zahl auf der Karte 7? (j/n)")
if antwort == "j":
    gedachteZahl += 64
    
print(gedachteZahl)
