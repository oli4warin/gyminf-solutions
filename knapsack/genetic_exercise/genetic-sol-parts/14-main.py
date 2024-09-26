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

