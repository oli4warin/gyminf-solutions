import random
def random_oracle(instance):
    """ 
    Entscheidet zufällig, ob Greedy oder oracle_says_yes verwendet werden soll.
        Parameter:
            instance: Instanz des Rucksackproblems (Liste mit Gewichten)
        Rückgabewert:
            Liste mit den eingepackten Gewichten: Wird ein Gegenstand
            eingepackt, wird dessen Gewicht an der entsprechenden Stelle in die
            Liste eingetragen. Andernfalls wird eine Null eingetragen.
    """
    oracle = bool(random.getrandbits(1)) #Zufällig 'True' oder 'False'
    # Ergänzen Sie hier!

