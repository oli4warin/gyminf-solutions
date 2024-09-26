def greedy(instance):
    """
    Führt den Greedy-Algorithmus aus: Ein Gegenstand wird eingepackt, sofern er
    im Rucksack Platz hat.
        Parameter:
            instance: Instanz des Rucksackproblems (Liste mit Gewichten)
        Rückgabewert:
            Liste mit den eingepackten Gewichten: Wird ein Gegenstand
            eingepackt wird dessen Gewicht an der entsprechenden Stelle in die
            Liste eingetragen. Andernfalls wird eine Null eingetragen.
    """
    choices=[]
    for weight in instance:
        if weight + sum(choices) <= 1:
            choices.append(weight)
        else:
            choices.append(0)
    return choices

