def breed(population):
    """
    Wählt zwei mal mit Hilfe der tournament-Funktion je eine tendentiell
    "fitte" Lösung aus und kombiniert diese so erhaltenen zwei Lösungen
    ("Eltern") zu zwei neuen Lösungskandidaten: Dazu werden sie an einer
    zufällig gewählten Stelle aufgetrennt und kreuzweise wieder neu
    zusammengesetzt. Die beiden Resultate werden dann noch mutiert und
    anschliessend, sofern sie als Lösungen funktionieren, zurückgegeben.
    Diese Rückgabeliste beinhaltet also im besten Fall 2 "überlebensfähige
    Kinder", im schlechtesten Fall kann die Rückgabeliste aber auch leer
    sein (nämlich dann wenn keines der erzeugten "Kinder überlebensfähig" ist)
        Parameter:
            population: Eine Liste von Lösungen (jeweils Binärstrings)
        Rückgabewert:
            Eine Liste mit bis zu 0, 1 oder 2 neuen Lösungen (Kinder)
    """

    children = []
    parent_a = tournament(population)
    parent_b = tournament(population)
    cut = random.randint(1,len(parent_a)-1)
    child1 = mutate(parent_a[:cut] + parent_b[cut:])
    child2 = mutate(parent_b[:cut] + parent_a[cut:])
    if (is_solution(child1)):
        children.append(child1)
    if (is_solution(child2)):
        children.append(child2)
    return children

