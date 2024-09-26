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

