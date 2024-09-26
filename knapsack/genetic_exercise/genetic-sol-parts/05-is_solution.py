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

