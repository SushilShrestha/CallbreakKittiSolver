import random

from GeneticAlgorithm.objective_function import objective_function


def best_2_of_random_5(population):
    parents = []
    for i in range(5):
        parent = random.choice(population)
        score = objective_function(parent)
        parents.append((parent, score))
    parents = sorted(parents, key=lambda x:x[1], reverse=True)
    return parents[0][0], parents[1][0]


def tournament_selection(population):
    pass


