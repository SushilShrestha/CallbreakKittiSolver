from GeneticAlgorithm.config import INITIAL_POPULATION


def replace_worst(population, population_score):
    sorted_population = sorted(zip(population, population_score), key=lambda x: x[1], reverse= True)
    top_population = sorted_population[:INITIAL_POPULATION]
    return zip(*top_population)


