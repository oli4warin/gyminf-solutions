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

