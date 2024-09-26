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

    candidate_a = population[random.randint(0, len(population)-1)]
    candidate_b = population[random.randint(0, len(population)-1)]
    if (evaluate_solution(candidate_a,val) > evaluate_solution(candidate_b,val)):
        return candidate_a
    return candidate_b

