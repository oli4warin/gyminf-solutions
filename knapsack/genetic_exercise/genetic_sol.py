"""
Genetischer Algorithmus zur Lösung des Rucksackproblems
"""

import random
from functools import cmp_to_key

#Liste der Werte der Gegenstände:
val = [4, 10, 3, 1, 15, 27, 13, 11]
#Liste der Gewichte der Gegenstände:
weights = [4, 3, 3, 1, 10, 11, 7, 3]

knapsack_capacity = 25 #Maximale Kapazität des Rucksacks
population_size = 5    #Grösse der Population in einer Generation
generations = 200      #Anzahl Generationen
pairing_rate = 5       #Wieviele Paarungen sollen pro Generation stattfinden?
mutation_rate = 0.1    #Wahrscheinlichkeit, dass ein Gen mutiert

def convert_to_binary(n):
    """
    Konvertiert eine natürliche Zahl in eine Binärzahl:
        Parameter:
            n: Eine natürliche Zahl (Integer)
        Rückgabewert:
            n als Binärzahl (String)
    """
    if n > 1:
        return convert_to_binary(n//2)+str(n%2)
    return str(n%2)
   
def generate_candidate():
    """
    Erzeugt einen Lösungskandidaten, indem eine Zufallszahl aus dem korrekten
    Bereich in eine Binärzahl umgewandelt und gegebenenfalls von links mit
    Nullen aufgefüllt wird, um die gewünschte Stellenzahl zu garantieren:
        Parameter:
            (keine)
        Rückgabewert:
            Eine zufällige Zahl in Binärschreibweise, mit genauso vielen
            Stellen wie es Gegenstände gibt als String. Zahlen mit weniger als
            der nötigen Anzahl Binärstellen werden von links entsprechend mit
            Nullen aufgefüllt. Zum Beispiel wird 00011011 statt 11011 bei 8
            möglichen Gegenständen zurückgegeben. Diese Zahl entspricht dann
            dem Lösungskandidaten "4., 5., 7. und 8. Gegenstand in den Rucksack
            nehmen".
    """

    n = len(val)
    minimum = 0
    maximum = 2**n-1
    candidate_number = random.randint(minimum, maximum+1)
    return convert_to_binary(candidate_number).rjust(n,"0")

def evaluate_solution(solution, distribution):
    """
    Berechnet die gewichtete Summe der Lösung für eine gegebene Verteilung
    Die Verteilung kann z.b. die Liste der Gegenstandsgewichte oder die Liste
    der Gegenstandswerte sein. Auf diese Weise kann dieselbe Funktion verwendet
    werden, um sowohl das Gesamtgewicht einer Lösung, als auch den Gesamtwert
    einer Lösung zu berechnen:
    Diese Funktion zählt also alle Gewichte bzw. alle Werte der Gegenstände,
    die bei einem gegebenen Lösungskandidaten gewählt werden, zusammen.
        Parameter:
            solution:       Ein Lösungskandidat als Binärzahl (String)
            distribution:   Eine Liste von Zahlen, die als Summationsgewichte
                            dienen (konkret die Liste der Gewichte oder die
                            Liste der Werte)
        Rückgabewert:       Die gewichtete Summe, also der Gesamtwert bzw. das
                            Gesamtgewicht des Lösungskandidaten
    """

    sol = list(solution)
    n = len(distribution)
    result = 0
    for i in range(n):
        result += distribution[i]*int(sol[i])
    return result
    
def is_solution(solution):
    """
    Überprüft, ob ein gegebener Lösungskandidat tatsächlich eine Lösung
    darstellt (also die Rucksackkapazität nicht sprengt) und gibt entsprechend
    True oder False aus:
        Parameter:
            solution:       Ein zu überprüfender Lösungskandidat
        Rückgabewert:
            True, falls der Lösungskandidat tatsächlich eine Lösung ist (also
            den Rucksack nicht überfüllt)
            False, falls dieser Lösungskandidat nicht funktioniert (also die
            Kapazität des Rucksacks sprengt)
    """

    return (evaluate_solution(solution,weights) <= knapsack_capacity)

def generate_population():
    """
    Generiert eine Liste von gültigen Lösungen der Länge population_size:
        Parameter:
            (keine)
        Rückgabewert:
            Eine Liste der Länge population_size, bestehend aus Binärzahlen
            (Strings) mit jeweils genauso vielen Stellen, wie es Gegenstände
            gibt, so dass die entsprechenden Lösungen funktionieren (also nicht
            ein zu hohes Gewicht ergeben)
    """

    population = []
    for i in range(population_size):
        candidate = generate_candidate()
        while(not is_solution(candidate)):
            candidate = generate_candidate()
        population.append(candidate)
    return population
    
def tournament(population):
    """
    Wählt zwei zufällige Lösungen aus einer Population und gibt
    diejenige mit dem höheren Wert zurück:
        Parameter:
            population: Eine Liste von Lösungen (Binärstrings)
        Rückgabewert:
            Von zwei zufällig gewählten Lösungen aus der Liste diejenige
            mit der grösseren Fitness (also dem höherem Wert)
    """

    candidate_a = population[random.randint(0,len(population)-1)]
    candidate_b = population[random.randint(0,len(population)-1)]
    if (evaluate_solution(candidate_a,val) > evaluate_solution(candidate_b,val)):
        return candidate_a
    return candidate_b

def mutate(candidate):
    """
    mutiert einen lösungskandidaten gemäss der eingestellten mutationsrate.
    dazu wird jede einzelne stelle aus der binärzahl (d.h. jedes "gen")
    durchgegangen und zufällig entschieden, ob es geflippt wird (wechsel von 0
    auf 1 bzw. umgekehrt):
    Die Wahrscheinlichkeit für so einen flip wird jeweils durch die variable
    mutation_rate festgelegt.
        parameter:
            candidate: ein lösungskandidat als binärzahl (string)
        rückgabewert:
            die mutierte version des lösungskandidaten als binärstring
    """

    mutant = ""
    genes = list(candidate)
    for i in range(len(genes)):
        if (random.random() < mutation_rate):
            genes[i]=(int(genes[i])+1)%2
        mutant += str(genes[i])
    return mutant
    
def breed(population):
    """
    Wählt zwei mal mit Hilfe der tournament-Funktion je eine tendentiell
    "fitte" Lösung aus und kombiniert diese so erhaltenen zwei Lösungen
    ("Eltern") zu zwei neuen Lösungskandidaten: Dazu werden sie an einer
    zufällig gewählten Stelle aufgetrennt und kreuzweise wieder neu
    zusammengesetzt. Die beiden Resultate werden dann noch mutiert und
    anschliessend, sofern sie als Lösungen funktionieren, zurückgegeben.
    Diese Rückgabeliste beinhaltet also im besten Fall 2 "überlebensfähige
    Kinder", im schlechtesten Fall kann die Rückgabeliste aber auch leer
    sein (nämlich dann wenn keines der erzeugten "Kinder überlebensfähig" ist)
        Parameter:
            population: Eine Liste von Lösungen (jeweils Binärstrings)
        Rückgabewert:
            Eine Liste mit bis zu 0, 1 oder 2 neuen Lösungen (Kinder)
    """

    children = []
    parent_a = tournament(population)
    parent_b = tournament(population)
    cut = random.randint(1,len(parent_a)-1)
    child1 = mutate(parent_a[:cut] + parent_b[cut:])
    child2 = mutate(parent_b[:cut] + parent_a[cut:])
    if (is_solution(child1)):
        children.append(child1)
    if (is_solution(child2)):
        children.append(child2)
    return children

def comparator(candidate_a, candidate_b):
    """
    Hilfsfunktion, um die Lösungen inder population_control-Funktion der
    Fitness nach sortieren zu können:
    (Diese Funktion muss im Moment nicht verstanden werden)
    Eperteninfo: Need reverse order (highest value first)
        Parameter:
            candidate_a: Eine Lösung
            candidate_b: Eine Lösung
        Rückgabewert:
            Eine positive Zahl, falls candidate_a weniger Wert hat als
            candidate_b
            Eine negative Zahl, falls candidate_a mehr Wert hat als candidate_b
            Null falls beide Kandidaten gleich viel Wert haben
    """

    return evaluate_solution(candidate_b, val)-evaluate_solution(candidate_a, val)

def population_control(population):
    """
    Sortiert eine population absteigend nach Wert und lässt davon nur die
    besten Lösungen übrig, indem alle Lösungen mit zu kleinem Wert entfernt
    werden, so dass am Ende die Liste wieder nur höchstens soviele Einträge hat
    wie in der Variablen population_size angegeben:
    Das Resultat ist eine Liste der gewünschten Grösse, bestehend aus den
    "bisher besten" Lösungen. Die "unfitten" Lösungen sterben also aus. Als
    nützlicher Nebeneffekt ist die entstehende Liste auch gleich nach Wert
    absteigend sortiert.
    Parameter:
        population: Eine Liste von Lösungen (Binärstrings)
    Rückgabewert:
        Eine Liste der Länge population_size, bestehend aus den besten
        Lösungen, sortiert nach Wert (absteigend)
    """

    decimated_population = []
    population = sorted(population, key=cmp_to_key(comparator))
    for i in range(population_size):
        decimated_population.append(population[i])
    return decimated_population
    
def population_control(population):
    """
    Sortiert eine population absteigend nach Wert und lässt davon nur die
    besten Lösungen übrig, indem alle Lösungen mit zu kleinem Wert entfernt
    werden, so dass am Ende die Liste wieder nur höchstens soviele Einträge hat
    wie in der Variablen population_size angegeben.
    Das Resultat ist eine Liste der gewünschten Grösse, bestehend aus den
    "bisher besten" Lösungen. Die "unfitten" Lösungen sterben also aus. Als
    nützlicher Nebeneffekt ist die entstehende Liste auch gleich nach Wert
    absteigend sortiert.
    Parameter:
        population: Eine Liste von Lösungen (Binärstrings)
    Rückgabewert:
        Eine Liste der Länge population_size, bestehend aus den besten
        Lösungen, sortiert nach Wert (absteigend)
    """

    decimated_population = []
    population = sorted(population, key=cmp_to_key(comparator))
    for i in range(0,population_size-1):
        decimated_population.append(population[i])
    return decimated_population
    
def print_best_candidate(population):
    """
    Gibt die aktuell beste Lösung auf der Konsole aus. Dazu wird
    population_control aufgerufen und der erste Eintrag der von dort
    zurückgegebenen Liste als beste Lösung betrachtet:
    Am Ende wird die von population_control generierte Liste als Rückgabewert
    durchgereicht, damit im Hauptprogramm die wegen des Sortierens
    verhältnismässig teure population_control-Funktion nicht unnötig oft
    aufgerufen werden muss (einmal um den besten Kandidaten anzuzeigen und
    einmal um die Population zu dezimieren).
    Parameter:
        population: Die Liste der aktuellen Lösungen
    Rückgabewert:
        Die von der Funktion population_control zurückgegebene Liste
    """

    decimated_population = population_control(population)
    best_candidate = decimated_population[0]
    best_value = evaluate_solution(best_candidate, val)
    print("Aktuell beste Lösung: "+best_candidate+" mit einem Wert von "+str(best_value))
    return decimated_population

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
"""HAUPTPROGRAMM
Beschreibung:
1) Population generieren
2) Population der Fitness nach sortieren (absteigend),
   gegebenenfalls dezimieren, und die aktuell beste
   Lösung sowie deren Wert ausgeben auf der Konsole.
3) So viele Paarungen (breed) durchführen wie in der
   Variablen pairing_rate angegeben. Die jeweils
   dabei entstehenden Kinder zur Population hinzufügen.
4) Wiederhole Schritte 2 und 3 so häufig, bis
   genügend Generationen entstanden sind (gemäss der
   Variablen generations).
"""

population = generate_population()
for i in range(generations):
    population = print_best_candidate(population)
    for j in range(pairing_rate):
        new_children = breed(population)
        population.extend(new_children)

