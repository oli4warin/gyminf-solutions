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

def oracle_says_yes(instance):
    """ 
    Wartet ab, bis ein Gegenstand mit Wert >0.5 auftaucht. Dieser wird
    eingepackt. Danach wird Greedy verwendet.
        Parameter:
            instance: Instanz des Rucksackproblems (Liste mit Gewichten)
        Rückgabewert:
            Liste mit den eingepackten Gewichten: Wird ein Gegenstand
            eingepackt wird dessen Gewicht an der entsprechenden Stelle in die
            Liste eingetragen. Andernfalls wird eine Null eingetragen.
    """
    choices=[]
    wait = True
    for weight in instance:
        if wait:
            if weight >0.5 and weight <=1:
                choices.append(weight)
                wait = False
            else:
                choices.append(0)
        else:
            if sum(choices)+weight <=1:
                choices.append(weight)
            else:
                choices.append(0)
    return choices

import random
def random_oracle(instance):
    """ 
    Entscheidet zufällig, ob Greedy oder oracle_says_yes verwendet werden soll.
        Parameter:
            instance: Instanz des Rucksackproblems (Liste mit Gewichten)
        Rückgabewert:
            Liste mit den eingepackten Gewichten: Wird ein Gegenstand
            eingepackt wird dessen Gewicht an der entsprechenden Stelle in die
            Liste eingetragen. Andernfalls wird eine Null eingetragen.
    """
    oracle = bool(random.getrandbits(1)) #Zufällig 'True' oder 'False'
    if oracle:
        return greedy(instance)
    else:
        return oracle_says_yes(instance)

from itertools import combinations
def bruteforce_sum(instance):
    """
    Findet durch Ausprobieren den maximal erreichbaren Wert:
        Parameter:
            instance: Instanz des Rucksackproblems (Liste mit Gewichten)
        Rückgabewert: Maximal erreichbarer Wert
    """
    max_weight = 0
    for i in range(len(instance)):
        for combination in combinations(instance, i+1):
            weight = sum(combination)
            if weight <= 1 and weight > max_weight:
                max_weight = weight
    return max_weight

def average_gain(algorithm,instance,num_iterations):
    """
        Parameter:
            algorithm:      Algorithmus, der verwendet werden soll
            instance:       Instanz des Rucksackproblems (Liste mit Gewichten)
            num_iterations: Anzahl Durchführungen, bevor der Durchschnitt berechnet 
                            wird
        Rückgabewert:
            Durchschnittlich erreichter Wert
    """
    gain = 0
    for _ in range(num_iterations):
        gain += sum(algorithm(instance))
    return gain/num_iterations

def quality(algorithm,instance,num_iterations=10000):
    """
        Parameter:
            algorithm:      Algorithmus, der verwendet werden soll
            instance:       Instanz des Rucksackproblems (Liste mit Gewichten)
            num_iterations: Anzahl Durchführungen, bevor der Durchschnitt
                            berechnet wird
        Rückgabewert:
            Geschätzte Approximationsgüte mit Hilfe des durchschnittlich
            erreichten Wertes.
    """
    return bruteforce_sum(instance)/average_gain(algorithm,instance,num_iterations)

print(quality(random_oracle,[0.01,1]))
