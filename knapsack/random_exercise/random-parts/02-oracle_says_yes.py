def oracle_says_yes(instance):
    """ 
    Wartet ab, bis ein Gegenstand mit Wert >0.5 auftaucht. Dieser wird
    eingepackt. Danach wird Greedy verwendet.
        Parameter:
            instance: Instanz des Rucksackproblems (Liste mit Gewichten)
        Rückgabewert:
            Liste mit den eingepackten Gewichten: Wird ein Gegenstand
            eingepackt, wird dessen Gewicht an der entsprechenden Stelle in die
            Liste eingetragen. Andernfalls wird eine Null eingetragen.
    """
    choices=[]
    wait = True
    for weight in instance:
        if wait:
            #
            # Ergänzen Sie die Funktion hier!
            #
        else:
            if sum(choices)+weight <=1:
                choices.append(weight)
            else:
                choices.append(0)
    return choices

