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
    
