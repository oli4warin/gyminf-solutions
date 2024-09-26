## Test 1: Funktioniert convert_to_binary richtig?
## Ausgabe sollte sein:
## 1100
## 10000
## 10010
## Für den Test die folgenden 3 Zeilen aktivieren:
#print(convert_to_binary(12))
#print(convert_to_binary(16))
#print(convert_to_binary(18))
## Ende Test 1

## Test 2: Produziert generate_candidate Lösungskandidaten im richtien Format?
## Ausgabe sollten 3 zufällige Binärzahlen der
## Länge 8 sein (wenn Sie die Anzahl der Gegenstände
## nicht verändert haben). Resultate mit weniger als 8
## Stellen sollten von links entsprechend mit Nullen
## aufgefüllt werden, also sollte z.b. statt
## 1101 die Variante 00001101 da stehen.
## Für den Test die folgenden 3 Zeilen aktivieren:
#print(generate_candidate())
#print(generate_candidate())
#print(generate_candidate())
## Ende Test 2

## Test 3: Berechnet evaluate_solution die gewichtete Summe korrekt?
## Ausgabe sollte sein:
## 49
## 11
## 36
## Für den Test die folgenden 3 Zeilen aktivieren:
#print(evaluate_solution("01010101", val))
#print(evaluate_solution("11110000", weights))
#print(evaluate_solution("11111111", [1,2,3,4,5,6,7,8]))
## Ende Test 3

## Test 4: Erkennt is_solution, ob ein Lösungskadidat gültig ist?
## (Funktioniert nur zuverlässig wenn die Standardwerte für
## val, weights und knapsack_capacity nicht verändert wurden!)
## Ausgabe sollte sein:
## True
## True
## False
## Für den Test die folgenden 3 Zeilen aktivieren:
#print(is_solution("01010010"))
#print(is_solution("00000000"))
#print(is_solution("11111110"))
## Ende Test 4

## Test 5: Erzeugt generate_population eine Liste gültiger Lösungen der korrekten Länge?
## Die Ausgabe sollte so aussehen, wobei die erste Zeile
## jedesmal etwas anders aussieht (aber immer aus 10 zu-
## fälligen Lösungen bestehen sollte)
## ['00001101', '01010010', '01100101', '10001000', '10100000', '10110101', '10010001', '01010110', '01011011']
## True
## True
## True
## True
## True
## True
## True
## True
## True
## Für den Test die folgenden 4 Zeilen aktivieren:
#test = generate_population()
#print(generate_population())
#for i in range(len(test)):
#    print(is_solution(test[i]))
## Ende Test 5
