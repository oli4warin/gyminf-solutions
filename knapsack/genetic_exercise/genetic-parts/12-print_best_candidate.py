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

