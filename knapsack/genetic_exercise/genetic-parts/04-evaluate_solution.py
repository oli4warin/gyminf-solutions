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

    #Hinweis: Mit list(solution) kann man den Lösungskandidaten als
    #Liste von Nullen und Einsen schreiben, aber diese Elemente sind
    #dann nach wie vor Strings, die man zum Rechnen in Zahlen
    #verwandeln muss!
    sol = list(solution)
    n = len(distribution)
    #Der Inhalt der Variable result sollte am Ende aus der Summe von
    #Produkten aus beiden Listen bestehen:
    #result = sol[0]*distribution[0] + sol[1]*distribution[1] + ...
    #Beachten Sie, dass die Elemente aus sol wie erwähnt zunächst noch
    #Strings sind, die für diese Rechnung noch in Integers umgewandelt werden
    #müssen!

    #Ihre Implementierung
    return result
    
