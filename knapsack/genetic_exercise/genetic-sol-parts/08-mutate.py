def mutate(candidate):
    """
    mutiert einen lösungskandidaten gemäss der eingestellten mutationsrate.
    dazu wird jede einzelne stelle aus der binärzahl (d.h. jedes "gen")
    durchgegangen und zufällig entschieden, ob es geflippt wird (wechsel von 0
    auf 1 bzw. umgekehrt):
    Die Wahrscheinlichkeit für so einen flip wird jeweils durch die variable
    mutation_rate festgelegt.
        parameter:
            candidate: ein lösungskandidat als binärzahl (string)
        rückgabewert:
            die mutierte version des lösungskandidaten als binärstring
    """

    mutant = ""
    genes = list(candidate)
    for i in range(len(genes)):
        if (random.random() < mutation_rate):
            genes[i]=(int(genes[i])+1)%2
        mutant += str(genes[i])
    return mutant
    
