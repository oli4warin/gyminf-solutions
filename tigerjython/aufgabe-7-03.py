points=0
answer=input("Ist Mathematik besser als Französisch? (j/n)")
if answer=="j":
    points += 1

answer=input("Ist Mathematik wichtiger als Französisch? (j/n)")
if answer=="j":
    points += 1

answer=input("Ist Mathematik wichtiger als alle anderen Fächer? (j/n)")
if answer=="j":
    points += 1

answer=input("Ist 42 grösser als 43? (j/n)")
if answer=="n":
    points += 1

answer=input("Ist 2023 eine Primzahl? (j/n)")
if answer=="n":
    points += 1
    
print(points)
