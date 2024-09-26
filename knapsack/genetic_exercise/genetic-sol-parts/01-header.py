"""
Genetischer Algorithmus zur Lösung des Rucksackproblems
"""

import random
from functools import cmp_to_key

#Liste der Werte der Gegenstände:
val = [4, 10, 3, 1, 15, 27, 13, 11]
#Liste der Gewichte der Gegenstände:
weights = [4, 3, 3, 1, 10, 11, 7, 3]

knapsack_capacity = 25 #Maximale Kapazität des Rucksacks
population_size = 5    #Grösse der Population in einer Generation
generations = 200      #Anzahl Generationen
pairing_rate = 5       #Wieviele Paarungen sollen pro Generation stattfinden?
mutation_rate = 0.1    #Wahrscheinlichkeit, dass ein Gen mutiert

