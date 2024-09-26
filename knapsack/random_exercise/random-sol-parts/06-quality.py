def quality(algorithm,instance,num_iterations=10000):
    """
        Parameter:
            algorithm:      Algorithmus, der verwendet werden soll
            instance:       Instanz des Rucksackproblems (Liste mit Gewichten)
            num_iterations: Anzahl Durchführungen, bevor der Durchschnitt
                            berechnet wird
        Rückgabewert:
            Geschätzte Approximationsgüte mit Hilfe des durchschnittlich
            erreichten Wertes.
    """
    return bruteforce_sum(instance)/average_gain(algorithm,instance,num_iterations)

