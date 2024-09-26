def average_gain(algorithm,instance,num_iterations):
    """
        Parameter:
            algorithm:      Algorithmus, der verwendet werden soll
            instance:       Instanz des Rucksackproblems (Liste mit Gewichten)
            num_iterations: Anzahl Durchführungen, bevor der Durchschnitt berechnet 
                            wird
        Rückgabewert:
            Durchschnittlich erreichter Wert
    """
    gain = 0
    for _ in range(num_iterations):
        gain += sum(algorithm(instance))
    return gain/num_iterations

