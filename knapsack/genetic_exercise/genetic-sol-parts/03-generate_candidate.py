def generate_candidate():
    """
    Erzeugt einen Lösungskandidaten, indem eine Zufallszahl aus dem korrekten
    Bereich in eine Binärzahl umgewandelt und gegebenenfalls von links mit
    Nullen aufgefüllt wird, um die gewünschte Stellenzahl zu garantieren:
        Parameter:
            (keine)
        Rückgabewert:
            Eine zufällige Zahl in Binärschreibweise, mit genauso vielen
            Stellen wie es Gegenstände gibt als String. Zahlen mit weniger als
            der nötigen Anzahl Binärstellen werden von links entsprechend mit
            Nullen aufgefüllt. Zum Beispiel wird 00011011 statt 11011 bei 8
            möglichen Gegenständen zurückgegeben. Diese Zahl entspricht dann
            dem Lösungskandidaten "4., 5., 7. und 8. Gegenstand in den Rucksack
            nehmen".
    """

    n = len(val)
    minimum = 0
    maximum = 2**n-1
    candidate_number = random.randint(minimum, maximum+1)
    return convert_to_binary(candidate_number).rjust(n,"0")

