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
    
