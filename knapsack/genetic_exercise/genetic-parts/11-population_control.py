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
    
